# Independent isolated audit: convex affine-tail baseline

## Verdict and audit boundary

**Scoped pass. No required mathematical repair was found for the intended eligibility and finite-system lemma.** The activation calculations, limiting initial two-sample laws, initial mode estimates, initial strict nonlinearity, finite-GF continuation, raw Hessian estimate, and sufficiently-large-width exact-GD stopping argument are valid. The constants in the displayed opposite-label bound are conservative but correct.

Two qualifications are essential to this verdict: the deterministic Gaussian covariance recursion describes the **limiting initial empirical law**, and the velocity/action argument concerns the **forward hidden fields** `z^(ell), h^(ell)`. The proof supplies bounded values for the backward fields and kernel blocks, not corresponding uniform velocity/action estimates for those objects. The text's convergence language and its explicit appeal to differentiated forward maps support these readings. Making them explicit would improve precision; no broader interpretation is certified here.

This is not a population continuation theorem, a mean-field theorem, a feature-learning theorem, or a proof of nonlinearity after training. The candidate explicitly disclaims those conclusions. The scalar curvature observation at its end is a proposed direction, not an established trained-network estimate.

Audit date: 2026-09-06. Mathematical inputs were restricted to the candidate and the fixed-model/metric section of the contract. No other mathematical file, project history, prior review, research-ledger entry, agent, experiment, or external mathematical source was used. All calculations below are symbolic elementary arguments. In particular, the Gaussian averaging and net arguments and the finite-ODE continuation argument are supplied rather than delegated to an external theorem.

The procedural skill was read in full from `/home/amir/.codex/skills/solve-math-rigorously/SKILL.md`. It guided the checks of quantifiers, degenerate cases, and proof completeness; the user's narrower input restrictions governed the audit.

### Exact source identification

SHA-256 of the complete source files at audit intake:

```text
d527ba30de64cd6dec00a774faae1987eb14203187b81fced84941171d87f028  /tmp/l3-two-sample-proof-DLuelg/CONVEX_AFFINE_TAIL_BASELINE.md
e1f04d537a7650962f60c2eb33b305e7ad604813c2ee6a937d283ea11aa43b40  /tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md
```

Candidate: all 234 lines were read. Contract: only lines 10–81, containing the fixed model, metric, update, observation convention, target scope, and kernel definitions, were read as mathematical content. A heading-only search located the section boundaries. The research ledger and provenance/policy sections were not read or used. The full contract hash identifies the supplied file; hashing does not make its unused portions mathematical inputs. Neither source file was modified by this audit.

**Concurrent-source-change record.** The end-of-audit check reproduced the candidate hash above, but the complete contract file had changed externally to SHA-256 `1461e507927317e77c481bc1a51931f1e676c6473af410a48c858715da481218`. Only the permitted contract lines 10–81 were re-read; their text matches the initially inspected model section. The other portions were not inspected to locate or interpret the change. SHA-256 of the permitted section as emitted by `sed -n '10,81p'` at the ending check is `e633994927965510b9c0605d27ed221b33de485caa7cda2bb9029a6343707d0e`. The full-file intake and ending hashes are both recorded so this review does not misleadingly claim that the entire contract remained unchanged. Its verdict depends only on the permitted model section and the unchanged candidate.

## 1. Fixed model and raw metric

Write `w=W^(4)` and `c=log 2`. For a vector `v` with `n` coordinates, put

\[
 |v|_n=\|v\|_2/\sqrt n.
\]

For a raw parameter increment `V=(V_1,V_2,V_3,v_4)`, the specified squared Hilbert norm is

\[
 \|V\|_{\rm raw}^2
 =\frac dn\|V_1\|_F^2+\|V_2\|_F^2+\|V_3\|_F^2
  +\frac1n\|v_4\|_2^2.
\]

The samples satisfy `||x_a||^2=d`, `C_aa=1`, `C_12=rho in [-1,1)`, and `|y_a|=1`. The scalar output and loss are

\[
 f_a=n^{-1}w^Th^{(3)}_a,\qquad r_a=f_a-y_a,
 \qquad L=r_1^2+r_2^2.
\]

With the contract's residual-free backward vectors, direct differentiation gives the four blocks of the raw gradient of a single prediction:

\[
 \nabla_1 f_a=\frac1d\delta^{(1)}_a x_a^T,\quad
 \nabla_\ell f_a=\frac1n\delta^{(\ell)}_a(h^{(\ell-1)}_a)^T
 \quad(\ell=2,3),\quad
 \nabla_4 f_a=h^{(3)}_a.
\]

For example, the ordinary Frobenius derivative in the first block is `delta^(1)_a x_a^T/n`; multiplying by the inverse metric factor `n/d` gives the displayed first block. The readout derivative is `h^(3)_a/n` in Euclidean coordinates and `h^(3)_a` in the raw metric. Thus

\[
 \nabla_{\rm raw}L=2\sum_a r_a\nabla_{\rm raw} f_a
\]

reproduces every prescribed update exactly. There is no missing factor of `n`, `d`, or two. The gradient-flow field is precisely the raw increment divided by the step size.

Block inner products of these prediction gradients give

\[
 K^{(1)}_{ab}=C_{ab}\frac{(\delta^{(1)}_a)^T\delta^{(1)}_b}{n},
\]

\[
 K^{(\ell)}_{ab}=
 \frac{(\delta^{(\ell)}_a)^T\delta^{(\ell)}_b}{n}
 \frac{(h^{(\ell-1)}_a)^Th^{(\ell-1)}_b}{n},\qquad
 K^{(4)}_{ab}=\frac{(h^{(3)}_a)^Th^{(3)}_b}{n}.
\]

Consequently `dot f_a=-2 sum_b sum_ell K^(ell)_ab r_b` in finite GF. The fact that `C_12` may be negative does not invalidate the first block: the entire two-by-two matrix is a Gram matrix in the raw first-weight space. The first-weight velocity has right factor in the span of the two inputs, so its orthogonal-to-input-span component is indeed fixed.

## 2. Every activation assertion

These checks concern candidate lines 10–49, and the affine-tail description in its title.

For finite real `z`, let `p=e^z/(1+e^z)`. Then `0<p<1` and

\[
 p'=p(1-p),\qquad
 \phi'=1+p,\qquad \phi''=p(1-p).
\]

It follows that `1<phi'<2`, `0<phi''<=1/4`, and `0<log phi'<log 2`. The curvature maximum is attained at zero; the derivative and logarithmic bounds at the tails are not attained at finite `z`. Strict positive curvature proves strict convexity and excludes an affine restriction on any interval of positive length. It supplies no positive uniform lower bound on curvature, since curvature tends to zero in both tails.

For `z>=0`, `log(1+e^z)<=z+c`; for `z<=0`, it is at most `c`. Therefore

\[
 |\phi(z)|\le |z|+\log(1+e^z)\le2|z|+c.
\]

The second derivative is a polynomial in `p`. Differentiating any polynomial `P(p)` gives `p(1-p)P'(p)`, another polynomial. This proves boundedness of each derivative of each fixed order at least two on the compact interval `p in [0,1]`. It does not assert one common bound for all derivative orders, nor does the candidate need that stronger statement.

The algebraic identity `log(1+e^z)-log(1+e^-z)=z` gives

\[
 \phi(z)-\phi(-z)=3z.
\]

Also `(1+e^z)(1+e^-z)=4 cosh^2(z/2)`, so

\[
 \phi(z)+\phi(-z)=2\log(2\cosh(z/2)).
\]

Equivalently, with the even function

\[
 g(z)=\log(2\cosh(z/2)),
 \qquad \phi(z)=\tfrac32z+g(z),\qquad g(z)\ge c,
\]

both identities hold with the stated constants. In particular `phi` is not pointwise positive: it tends to minus infinity as `z` tends to minus infinity. Its tail expansions are `phi(z)=2z+log(1+e^-z)` at the positive tail and `phi(z)=z+log(1+e^z)` at the negative tail, with the remainder tending to zero in each case.

For the Euler defect, put `s=log(1+e^z)`. Since `log p=z-s` and `log(1-p)=-s`,

\[
 -p\log p-(1-p)\log(1-p)=s-pz
 =\phi(z)-z\phi'(z).
\]

Both terms on the left are strictly positive for `0<p<1`. Its derivative with respect to `p` is `log((1-p)/p)` and its second derivative is `-1/[p(1-p)]`; hence its unique maximum is `c` at `p=1/2`. The exact range is `(0,c]`. This verifies the identity, sign, and constant. It is not Euler homogeneity: already `phi(0)=c` excludes degree-one homogeneity. The source correctly declines to infer a matrix balance from this scalar identity.

The comparison at lines 16–17 is also correct on its own terms: for `psi(z)=z+1+tanh(z)/2`, differentiation gives `psi''(z)=-sech^2(z)tanh(z)`, positive for negative `z` and negative for positive `z`. No other fact about that candidate was consulted or used.

Finally, the fundamental theorem of calculus and `1<=phi'<=2` give, with either ordering of `u,v`,

\[
 |u-v|\le|\phi(u)-\phi(v)|\le2|u-v|.
\]

The non-strict formulation includes `u=v` and is valid although the derivative inequalities are strict at finite points.

## 3. Initial Gaussian law: what is exact and what is a limit

Candidate lines 53–69 give the correct limiting recursion. A precision point is that the deterministic covariance at layers two and three is not their unconditional finite-width covariance law. The exact finite-width statement is conditional and has a random empirical covariance.

Let

\[
 Q^{(\ell)}_{ab,n}=\frac1n\sum_i h^{(\ell)}_{a,i}h^{(\ell)}_{b,i}.
\]

The first-layer row pairs are exactly independent copies of a centered Gaussian pair with covariance `C`. At layer `ell=2,3`, conditional on all preceding layers, the row pairs are independent centered Gaussian pairs with covariance `Q^(ell-1)_n`. Indeed,

\[
 \mathbb E[z^{(\ell)}_{a,i}z^{(\ell)}_{b,i}\mid\text{preceding layers}]
 =\sum_j\frac1n h^{(\ell-1)}_{a,j}h^{(\ell-1)}_{b,j},
\]

and different rows use disjoint independent Gaussian weights. A shared random conditional covariance generally prevents unconditional row independence. The source's initialization-only qualification is necessary and correct.

Here is a direct justification of the claimed deterministic limiting law. It also covers the singular root at `rho=-1`.

For a positive semidefinite two-by-two matrix `Q` with `q_11>0`, construct a Gaussian pair using independent scalar standard Gaussians `G,H`:

\[
 Z_1=\sqrt{q_{11}}G,\qquad
 Z_2=\frac{q_{12}}{\sqrt{q_{11}}}G+
 \sqrt{q_{22}-q_{12}^2/q_{11}}\,H.
\]

This formula remains valid when the last square root is zero. Its coefficients vary continuously with `Q` on this domain. Coupling two such pairs with the same `G,H` shows convergence in squared mean when their covariances converge. The Lipschitz bound on `phi` then gives convergence in squared mean of their features. By Cauchy–Schwarz applied to the difference of two products, the map

\[
 F_{ab}(Q)=\mathbb E[\phi(Z_a)\phi(Z_b)]
\]

is continuous, including at the singular root. The same coupling proves continuity of expected bounded Lipschitz tests of the Gaussian pair or feature pair. This avoids assuming invertibility at the root or making an unjustified density argument there.

For the required averaging, `|phi(z)|^4<=128|z|^4+8c^4`. The elementary Gaussian fourth moment `E Z^4=3q^2` therefore gives

\[
 \mathbb E|\phi(Z)|^4\le384q^2+8c^4.
\]

Moreover, `(n^-1 sum_i h_i^2)^2<=n^-1 sum_i h_i^4`. Starting with unit Gaussian marginal variance, conditioning and this inequality prove uniformly bounded fourth moments through all three fixed layers. For a cross product, `E(h_1^2 h_2^2)<=sqrt(Eh_1^4 Eh_2^4)`, so its second moment is uniformly bounded as well.

Conditional independence of rows now gives

\[
 \mathbb E\left|Q^{(\ell)}_{ab,n}
       -F_{ab}(Q^{(\ell-1)}_n)\right|^2\le\frac{C_\ell}{n}
\]

for `ell=2,3`, and the analogous bound at layer one with fixed covariance `C`. The constants here are fixed-depth moment bounds, not covariance entries. The elementary estimate `P(|X|>epsilon)<=E|X|^2/epsilon^2` turns these bounds into convergence in probability. Continuity of `F` then gives inductively

\[
 Q^{(1)}_n\longrightarrow F(C),\quad
 Q^{(2)}_n\longrightarrow F(F(C)),\quad
 Q^{(3)}_n\longrightarrow F(F(F(C))).
\]

The same conditional variance argument for any bounded Lipschitz test proves the corresponding initial empirical-law statement. For tests of at most quadratic growth, fourth-moment bounds control the truncated tails: `E[|H|^2 1_{|H|>R}]<=E|H|^4/R^2`. Thus the averaging argument supports precisely the second moments used later; it is not an unsupported exchange of a limit with an unbounded test.

Let `Z^(1)` have covariance `C`, put `H^(1)=phi(Z^(1))`, and for later layers let `Z^(ell)` have covariance `E[H^(ell-1)(H^(ell-1))^T]`. This is the source's recursion. The covariance here is the feature **second moment**, not its centered covariance. Although the features have positive mean, each next preactivation pair is centered, because the new matrix has centered independent entries. Subtracting feature means would be an actual error; the candidate does not do so.

Equal marginal laws propagate because `C_11=C_22=1`, each activation is identical, and the next diagonal variances are the corresponding equal second moments. All these moments are finite by linear growth. A nondegenerate Gaussian and strictly increasing `phi` give a nonconstant feature, hence strictly positive feature variance and second moment. The next Gaussian variance is that positive second moment, closing the induction.

For completeness, the readout normalization also behaves consistently. Conditional on the last hidden layer, the initial prediction pair is centered Gaussian with covariance `Q^(3)_n/n^3`, since each readout entry has variance `n^-2` and the output has an additional factor `1/n`. Uniform feature moments imply `f_a(0)->0` in squared mean and `L(0)->2` in probability. This extra observation is not needed for the deterministic bound on `L(0)` below.

## 4. Initial modes, antiparallel inputs, and strict nonlinearity

### Opposite-label constant

At the root,

\[
 \mathbb E|Z^{(1)}_1-Z^{(1)}_2|^2=2(1-\rho)=D_0.
\]

At later layers the covariance recursion gives

\[
 \mathbb E|Z^{(\ell)}_1-Z^{(\ell)}_2|^2
 =\mathbb E|H^{(\ell-1)}_1-H^{(\ell-1)}_2|^2
 =D_{\ell-1}.
\]

Squaring the activation increment bounds and taking expectations yields `D_(ell-1)<=D_ell<=4D_(ell-1)`. Three applications give `D_0<=D_3<=64D_0`. Dividing by four, exactly as required by the vector `(1,-1)/2`, gives

\[
 \frac{1-\rho}{2}
 \le \mathbb E\left|\frac{H^{(3)}_1-H^{(3)}_2}{2}\right|^2
 \le 32(1-\rho).
\]

Thus both constants in candidate (1) are correct. The factor 32 is `4^3 * 2 / 4`, not an omitted-depth or mode-normalization error. The lower bound is positive for every allowed `rho`, including `rho=-1`. It vanishes as `rho` approaches the excluded value one, as permitted by the contract. No uniform angle separation is claimed or needed.

### Same-label constant and upper finiteness

A centered Gaussian is symmetric. Using `phi(z)=3z/2+g(z)` gives

\[
 \mathbb E\phi(Z)=\mathbb E g(Z)\ge c.
\]

Therefore, irrespective of dependence between the two equal marginals,

\[
 \mathbb E\left|\frac{H^{(3)}_1+H^{(3)}_2}{2}\right|^2
 \ge\left(\mathbb E\frac{H^{(3)}_1+H^{(3)}_2}{2}\right)^2
 \ge c^2.
\]

This is a second-moment lower bound from a nonzero mean, not a lower bound on the activation itself. The source makes that distinction correctly.

The source does not display an explicit same-label upper constant, but its finiteness claim is sufficient and correct. An elementary explicit bound is available: if `b_ell=(E|H^(ell)_a|^2)^(1/2)`, then `b_1<=2+c` and `b_ell<=2b_(ell-1)+c`. Thus `b_3<=8+7c`. Since `|(u+v)/2|^2<=(u^2+v^2)/2`, the same-label squared norm is at most `(8+7c)^2`.

Writing the last feature second-moment matrix as `[[Q,S],[S,Q]]`, its eigenvectors are the same/opposite vectors and its eigenvalues are `Q+S,Q-S`. The displayed squared mode norms are **half** these eigenvalues, because `(1,±1)/2` has squared Euclidean norm `1/2`. Consequently the source bounds imply eigenvalue lower bounds `2c^2` and `1-rho`, respectively. This checks the normalization against the raw readout kernel block `K^(4)`.

### Positive definiteness, including the singular root

For `-1<rho<1`, the root Gaussian has a density positive everywhere on the plane: the independent-Gaussian representation above has an invertible linear coefficient matrix. If `c_1 phi(Z_1)+c_2 phi(Z_2)=0` almost surely, continuity makes this identity hold everywhere. Otherwise a neighborhood on which it is nonzero would have positive probability. Fixing one coordinate and varying the other, strict monotonicity forces first `c_1=0` and then `c_2=0`. Since the quadratic form of the feature second-moment matrix is the expected square of this linear combination, this proves positive definiteness.

At `rho=-1`, the pair is exactly `(G,-G)` and has no planar full support. The candidate correctly treats this separately. Subtracting the asserted identity at `-G` from that at `G` gives `3(c_1-c_2)G=0`, hence `c_1=c_2`. Adding then gives `2c_1 g(G)=0`; since `g>=c>0`, both coefficients vanish.

An explicit check makes the degeneracy resolution transparent. At layer one,

\[
 Q=\tfrac94+\mathbb E g(G)^2,\qquad
 S=-\tfrac94+\mathbb E g(G)^2.
\]

The two eigenvalues are `9/2` and `2E g(G)^2`, both positive. In particular `D_1=9` while `D_0=4`, consistent with the recursion bounds. Subsequent Gaussian pairs have positive definite covariance and the full-support argument applies. Only the root **Gaussian covariance** is singular; the first and all later **feature second-moment matrices** are positive definite. The candidate does not wrongly assert positive definiteness of the root covariance.

### Strict distributional nonlinearity

For every layer and sample in the limiting initial law, the Gaussian preactivation has variance `q>0`. The source's full-support argument is valid: an almost-sure affine equality would, by continuity, hold everywhere and contradict `phi''>0`.

The positive best-affine approximation error can also be computed directly without invoking a projection theorem. Since `Z` is centered and `g` is even, `E[Zg(Z)]=0`. For any real `a,b`,

\[
 \mathbb E|\phi(Z)-aZ-b|^2
 = (\tfrac32-a)^2q+\mathbb E|g(Z)-b|^2
 = (\tfrac32-a)^2q+\operatorname{Var}(g(Z))
   +(\mathbb E g(Z)-b)^2.
\]

The minimizing coefficients are `a=3/2` and `b=E g(Z)`, and the error is `Var(g(Z))>0`. Positivity follows because `g` takes different values on two intervals each having positive nondegenerate Gaussian probability. All expectations exist by the growth bound. This verifies existence of the best approximation and strict positivity of its error, rather than merely the absence of one guessed affine fit.

This is distributional nonlinearity, not a claim about fitting a finite list of observed neuron coordinates. Nor does positivity at initialization imply positive approximation error at every later time.

## 5. Initial primal event and raw-ball control

These checks concern candidate lines 114–148. The deterministic statements require only that the initial maximum primal size be at most `M_0`; Gaussianity is used to make that event probable, not in the subsequent trajectory argument.

For the first matrix, the squared scaled Frobenius norm has mean `d` and variance `2d/n`. Indeed it is `(d/n)` times a sum of `nd` independent squares of `N(0,1/d)` variables. Thus its norm converges in probability to `sqrt d`. For the readout, the squared RMS norm has mean `n^-2`, so its probability of exceeding any fixed positive threshold tends to zero by the elementary second-moment/Markov bound.

A short derivation verifies the proposed hidden-matrix estimate. A maximal set of sphere points separated by more than `epsilon` is an `epsilon`-net. Disjoint balls of radius `epsilon/2` about its points fit inside the ball of radius `1+epsilon/2`; comparing volumes bounds its size by `(1+2/epsilon)^n`. For `epsilon=1/4` this is `9^n`.

For unit vectors and their net approximations,

\[
 |u^TWv-u_0^TWv_0|
 \le\|u-u_0\|\|W\|_{op}+\|v-v_0\|\|W\|_{op}
 \le\tfrac12\|W\|_{op}.
\]

Taking suprema gives `||W||_op<=2 max_net |u_0^TWv_0|`. For each fixed pair, the bilinear form is Gaussian with variance `1/n`. Completing the square in the scalar Gaussian integral gives `E exp(sX)=exp(s^2/(2n))`; applying Markov's inequality to the exponential and optimizing `s` gives `P(|X|>t)<=2 exp(-nt^2/2)`. A union bound over at most `9^(2n)` pairs yields

\[
 \mathbb P(\|W\|_{op}>2t)
 \le2\exp\{n(2\log9-t^2/2)\}.
\]

For example `t=4`, hence operator threshold eight, makes the exponent negative. Applying this to both hidden matrices and combining with the first/readout bounds proves the claimed high-probability event for any sufficiently large fixed `M_0>max(sqrt d,8)`. This argument uses no asymptotic spectral theorem.

If `||V||_raw<=R`, every individual weighted block norm is at most `R`. Hidden-matrix operator increments are bounded by their Frobenius increments. The triangle inequality therefore raises every primal norm by at most `R`. The affine raw ball about the initial state has primal size at most `M=M_0+R`, exactly as asserted.

For either input,

\[
 |z^{(1)}_a|_n\le\|W^{(1)}\|_F\|x_a\|/\sqrt n\le M.
\]

The growth bound and matrix operator bounds give the stated deterministic recursions

\[
 H_1=2M+c,\qquad H_2=2MH_1+c,\qquad H_3=2MH_2+c,
 \qquad |h^{(\ell)}_a|_n\le H_\ell.
\]

The backward definitions, with no residual inserted, give

\[
 |\delta^{(3)}_a|_n\le2M,\quad |q^{(2)}_a|_n\le2M^2,
 \quad |\delta^{(2)}_a|_n\le4M^2,
 \quad |q^{(1)}_a|_n\le4M^3,\quad |\delta^{(1)}_a|_n\le8M^3.
\]

Thus `|f_a|<=MH_3` and `|r_a|<=F:=MH_3+1`. The four raw norms of `grad f_a` are bounded respectively by

\[
 8M^3,\qquad4M^2H_1,\qquad2MH_2,\qquad H_3.
\]

For example the hidden-block Frobenius norm is the product of the RMS norms of its two vectors; the first block uses `||x_a||=sqrt d` to cancel the raw metric factor. If `J` is the sum of these four bounds, then `||grad f_a||_raw<=J` and `||grad L||_raw<=4FJ`. One valid polynomial choice in candidate (2) is

\[
 A(M)=MH_3+F+4FJ.
\]

A deterministic initial loss bound needed for the stop proof is

\[
 L_* = 2\big(M_0H_3(M_0)+1\big)^2.
\]

All these constants are independent of width; any dependence on fixed `d` enters through the chosen `M_0`.

## 6. Raw Hessian: explicit tracking of the square-root-width factor

These checks concern candidate lines 150–172. Write `D_u` for an ordinary directional derivative in a raw unit direction. Such a direction satisfies

\[
 \|u_1\|_F\le\sqrt{n/d},\quad
 \|u_2\|_{op},\|u_3\|_{op}\le1,\quad |u_4|_n\le1.
\]

First derivative bounds follow with the following width-independent constants:

\[
 t_1=1,\quad s_1=2,\qquad
 t_\ell=H_{\ell-1}+Ms_{\ell-1},\quad s_\ell=2t_\ell
 \quad(\ell=2,3).
\]

Indeed `|D_u z^(1)|_n<=1`; the next preactivation derivative is `u_ell h^(ell-1)+W^(ell)D_u h^(ell-1)`, and activation differentiation multiplies coordinatewise by a number at most two. Thus `|D_u z^(ell)|_n<=t_ell` and `|D_u h^(ell)|_n<=s_ell`.

For any two vectors,

\[
 |a\mathbin{\odot}b|_n
 \le\|a\|_\infty |b|_n
 \le\sqrt n\,|a|_n|b|_n.
\]

This verifies the factor in candidate line 163, including its `1/4`. The first preactivation has zero mixed second derivative, and

\[
 |D_uD_v h^{(1)}|_n\le\tfrac14\sqrt n.
\]

At subsequent layers,

\[
 D_uD_v z^{(\ell)}
 =u_\ell D_vh^{(\ell-1)}+v_\ell D_uh^{(\ell-1)}
   +W^{(\ell)}D_uD_vh^{(\ell-1)},
\]

\[
 D_uD_vh^{(\ell)}
 =\phi'(z^{(\ell)})D_uD_vz^{(\ell)}
  +\phi''(z^{(\ell)})
    (D_uz^{(\ell)}\mathbin{\odot}D_vz^{(\ell)}).
\]

For `n>=1`, define `b_1=1/4` and

\[
 b_\ell=4s_{\ell-1}+2Mb_{\ell-1}+\tfrac14t_\ell^2.
\]

The last two displayed identities then prove inductively `|D_uD_v h^(ell)|_n<=b_ell sqrt n`: the two matrix-direction terms contribute at most `2s_(ell-1)`, while the propagated mixed derivative contributes at most `Mb_(ell-1)sqrt n`, before multiplication by the activation derivative. There is no product of two mixed second derivatives and no further factor of `sqrt n` from this propagation.

The readout derivatives include its parameter-direction terms:

\[
 D_u f_a=n^{-1}\big(u_4^Th^{(3)}_a+w^TD_uh^{(3)}_a\big),
\]

\[
 D_uD_v f_a=n^{-1}\big(u_4^TD_vh^{(3)}_a
      +v_4^TD_uh^{(3)}_a+w^TD_uD_vh^{(3)}_a\big).
\]

By Cauchy–Schwarz their bounds are

\[
 |D_uf_a|\le G:=H_3+Ms_3,\qquad
 |D_uD_vf_a|\le C_f\sqrt n,\qquad C_f:=2s_3+Mb_3.
\]

Finally,

\[
 D_uD_v L=2\sum_{a=1}^2
  \big(D_uf_aD_vf_a+r_aD_uD_vf_a\big).
\]

It follows that

\[
 |D_uD_vL|\le4G^2+4FC_f\sqrt n
 \le B(M)\sqrt n,\qquad B(M):=4G^2+4FC_f.
\]

These are finite polynomials in `M`. The raw metric is independent of the parameter location, so `D_uD_vL` is exactly the raw-Hessian bilinear form. Taking its supremum over raw unit `u,v` gives the operator bound claimed in (3). A claim of a width-independent Hessian bound would not be supported by this proof; the actual claimed square-root-width bound is supported.

## 7. Finite gradient flow: energy and continuation

For a finite-width solution to `dot theta=-grad_raw L`, the ordinary chain rule in this constant Hilbert metric gives

\[
 \frac{dL}{dt}=-\|\nabla_{\rm raw}L\|_{\rm raw}^2.
\]

Since `L>=0`, integration yields

\[
 \int_0^t\|\dot\theta\|_{\rm raw}^2ds\le L(0),\qquad
 \int_0^t\|\dot\theta\|_{\rm raw}ds\le\sqrt{tL(0)}.
\]

The second inequality is Cauchy–Schwarz and uses no upper bound on the instantaneous gradient. It bounds both length and displacement, not merely a net energy change. Consequently on `[0,T]` the primal size is at most `M_0+sqrt(TL_*)`, uniformly in width on the initial event.

For clarity, there is no hidden global-existence assumption in this use of energy. Local existence and uniqueness can be obtained directly: in a sufficiently small finite-dimensional parameter ball, the smooth vector field has a finite bound `V` and a finite derivative bound `K`. Choose a time interval so that its length times `V` is at most the ball radius and its length times `K` is less than `1/2`. Iterating `theta_(m+1)(t)=theta(0)+integral_0^t F(theta_m(s)) ds` remains in the ball and contracts successive uniform differences by at least a factor two. The uniformly convergent iterates solve the integral equation; the same difference estimate proves uniqueness locally.

Suppose such a solution could end at a finite maximal time `tau`. For `s<t<tau`, the energy inequality gives

\[
 \|\theta(t)-\theta(s)\|_{\rm raw}\le\sqrt{(t-s)L(0)}.
\]

Thus it has a finite limit as `t` tends to `tau` in the finite-dimensional raw space. The local construction at that limit continues it, and local uniqueness joins the solutions. This contradicts finite maximal time. This also explains precisely the no-escape step in candidate lines 179–181. The existence assertion is finite-dimensional for each `n`; it proves no infinite-dimensional restart theorem.

## 8. Exact GD: descent, stopping, and interpolation

Fix `T>=0`, let `eta=n^-2`, and choose the displayed `L_*` and

\[
 R>\sqrt{2(T+1)L_*}+2,\qquad M=M_0+R.
\]

Here `A(M), B(M)` are fixed independently of width. Both required small-step conditions hold for all sufficiently large `n`, because

\[
 \eta A(M)=A(M)n^{-2}\to0,\qquad
 \eta B(M)\sqrt n=B(M)n^{-3/2}\to0.
\]

On a step segment inside the larger raw ball, set `g=grad_raw L(theta)`. Twice integrating the derivative of `s -> L(theta-s eta g)` gives

\[
 L(\theta-\eta g)
 \le L(\theta)-\eta\|g\|_{\rm raw}^2
       +\frac12\eta^2 B(M)\sqrt n\,\|g\|_{\rm raw}^2
 \le L(\theta)-\frac\eta2\|g\|_{\rm raw}^2.
\]

This is (4), with the correct factor for a sum loss. The segment premise is removed as follows.

Let `N=ceil(T/eta)`; then `N eta<=T+eta<=T+1`. Suppose a first node `k<=N` reaches or leaves radius `R-1`. Every earlier node has radius less than `R-1`. Each step starting at such a node has length at most `eta A(M)<1`; by the triangle inequality its entire straight segment lies inside radius `R`. This argument uses the gradient bound only at the starting point, already inside the larger ball. It therefore applies also to the putative exit step and is not circular.

Summing the descent inequality through step `k` yields

\[
 \sum_{j<k}\eta\|g_j\|_{\rm raw}^2\le2L(0).
\]

Weighted Cauchy–Schwarz then gives exactly

\[
 \sum_{j<k}\eta\|g_j\|_{\rm raw}
 \le\sqrt{\Big(\sum_{j<k}\eta\Big)
                  \Big(\sum_{j<k}\eta\|g_j\|_{\rm raw}^2\Big)}
 \le\sqrt{2k\eta L(0)}
 \le\sqrt{2(T+1)L_*}<R-1.
\]

Node displacement is at most this path length, contradicting the exit. Hence all nodes through `N` remain in the smaller ball and the descent and action sums are valid. The slack in the source, `R>sqrt(2(T+1)L_*)+2`, is more than sufficient. Choosing the ceiling explicitly shows that the final partial segment at a non-mesh observation time is also covered.

On step `j`, raw linear interpolation has constant velocity `-g_j`; convexity of the norm ball keeps the interpolation between its endpoints inside the smaller ball. Its integrated squared raw speed through time `T` is at most the complete sum through `N`, hence at most `2L_*`. This proves the raw path-action bound and the primal bound. It does not treat the interpolated slope as the current instantaneous gradient.

The width quantifier matters: the argument gives these constants for **all sufficiently large widths**, with threshold depending on the fixed horizon and initial-size bound. It does not establish descent at `eta=n^-2` for every small width, and the detailed source does not claim that. Every individual finite GD update is well defined because the activation is smooth and finite at all finite parameters; the stronger uniform descent statement uses the threshold above.

## 9. Observation scope and limits of the estimates

### What the proof controls

For a forward field `F_a(theta)=z^(ell)_a` or `h^(ell)_a`, Section 6 above gives a constant `C_F(M)` such that

\[
 |DF_a(\theta)V|_n\le C_F(M)\|V\|_{\rm raw}.
\]

For GF, the chain rule and the raw energy inequality therefore imply

\[
 \int_0^T|\dot F_a|_n^2dt\le C_F(M)^2L_*.
\]

For recomputed raw-GD fields, on the interior of step `j`,

\[
 \frac{d}{dt}F_a(\theta(t))=DF_a(\theta(t))(-g_j),
\]

so the corresponding integral is at most `2C_F(M)^2L_*`. Finite sums cover all three forward layers and both samples with width-independent constants. The same reasoning controls prediction velocities, using `G`, and residual velocities because labels are fixed. Loss velocities can also be bounded using `||grad L||<=A(M)`. These latter extensions are consequences of the proved estimates, not prerequisites for them.

Recomputation matters: the hidden path is the nonlinear forward map of the straight raw-parameter interpolation, not a straight interpolation of stored hidden states. The candidate uses the correct convention. At interior mesh nodes take the derivative from the outgoing segment; at an observed terminal mesh node take the incoming derivative, as specified by the contract. Values at finitely many nodes do not change an integrated squared-velocity bound. The same derivative estimates bound those one-sided values wherever needed.

Backward field **values** are bounded by Section 5. All four kernel blocks are bounded because their individual prediction-gradient blocks are bounded. Explicitly their absolute entries are at most

\[
 64M^6,\qquad16M^4H_1^2,\qquad4M^2H_2^2,\qquad H_3^2,
\]

respectively; `|C_ab|<=1` follows from the input normalization and Cauchy–Schwarz. Each block is a Gram matrix, and predictions have already been bounded. The reference to (2) at candidate line 214 is slightly abbreviated: a bound on the **sum loss gradient alone** would not bound each prediction-gradient block because of possible cancellation. The individual backward/forward estimates immediately preceding (2), or the directional bounds used for (3), supply the needed bound. There is no missing hypothesis, but citing those estimates directly would be more precise.

### What “hidden paths” must not silently include

The forward derivative proof does not give a width-independent derivative bound for `delta`, `q`, or the kernels. Differentiating a backward gate introduces, for example,

\[
 D\delta^{(3)}=Dw\mathbin{\odot}\phi'(z^{(3)})
   +w\mathbin{\odot}\phi''(z^{(3)})Dz^{(3)},
\]

whose second term is a product of two RMS-controlled vectors. It can cost `sqrt n`.

An explicit deterministic calculation demonstrates the limitation of the available ball bounds. Set all three weight matrices to zero and set `w=m sqrt n e_1` for a fixed `m>0`. All primal norms are bounded by `m`. Then `h^(2)=c 1`, `z^(3)=0`. Take the raw unit direction with only third-matrix block `V_3=e_1 1^T/sqrt n`. It gives `Dz^(3)=c sqrt n e_1`, and therefore

\[
 D\delta^{(3)}=(mc n/4)e_1,
 \qquad |D\delta^{(3)}|_n=(mc/4)\sqrt n.
\]

Thus a width-independent derivative bound for all backward maps is false under primal control alone. This example concerns the deterministic map estimate; it is not asserted to be a Gaussian-initialized trajectory and is not a counterexample to any unclaimed trajectory theorem. It shows why a broader velocity claim would need an additional argument. The source's invocation of **forward** derivatives is sufficient for its forward-path reading and insufficient for the broader reading.

### No accidental promotion to the full contract

The initial separation concerns the readout block `K^(4)`. It does not show that all hidden-layer kernel blocks are initially nonvanishing or that all layers learn in a population limit. In fact the initial readout RMS is of order `1/n` in probability. The bounded forward/hidden-operator estimates then make the initial backward RMS norms of the same order, and the first three kernel blocks of order `1/n^2` in probability. This is consistent with positive readout mode limits and underscores their limited role as eligibility checks.

The note proves neither convergence nor uniqueness of limiting trajectories. Separate uniform energy bounds for GF and GD do not identify a common limit. In particular the Hessian bound grows with width; plugging it into an ordinary finite-dimensional stability estimate does not automatically give a width-uniform trajectory comparison.

Nor do RMS/action bounds give uniform tails in squared norm or the requested `W_2` path-law conclusions. An elementary illustration is an empirical family of scalar paths consisting of one path `sqrt n t` and `n-1` zero paths. On `[0,T]` its average integrated squared speed is `T`, while its average squared supremum is `T^2`. Its empirical law tends weakly to the zero path, but its squared-distance cost to that point mass stays `T^2`; the squared tails are not uniformly integrable. This illustrates insufficiency of the estimates alone, not failure of the specified network. The candidate's warning about query tails is mathematically warranted.

For a scalar differentiable trajectory, one can integrate

\[
 \frac{d}{dt}\log\phi'(z(t))
 =\frac{\phi''(z(t))}{\phi'(z(t))}\dot z(t)
\]

to obtain an endpoint difference of magnitude at most `log 2`. That is a **signed** identity with the factor `dot z/phi'`. It supplies no bound on `integral phi''(z(t))dt`—a constant trajectory at zero makes that integral grow linearly—and no general bound on its absolute-variation analogue for repeatedly traversed scalar paths. It also does not sign matrix products or residual-weighted lower-layer forcing. The candidate calls such an extension unproved, which is the correct scope. No separate frozen-top calculation was read or credited here.

The statement that the contrast is not suppressed by a sixth power is defensible only in the immediate sense that the proved bound for this fixed activation contains no small nonlinear-amplitude parameter. No quantitative comparison with an unprovided research result is established or needed. In particular it is not a lower bound on hidden-layer learning strength.

## 10. Required repairs versus optional presentation

### Required mathematical repairs

**None for the scoped lemma audited above.** All requested identities and finite-system inequalities have a complete elementary justification, and the exact-GD first-exit argument closes with its stated slack. No changed activation, changed raw metric, extra probabilistic assumption, clipping, or unproved external theorem is needed.

The scope restrictions are substantive, not optional conclusions: initial nonlinearity is not trained-time nonlinearity; initial readout separation is not all-layer feature learning; forward-field action bounds are not backward/kernel action bounds; and bounded finite systems are not a constructed population dynamics. The candidate's concluding disclaimers correctly preserve these restrictions. A future use asserting any of the stronger conclusions would require new proof rather than a wording adjustment.

### Optional precision and presentation edits

1. At lines 53–64, say explicitly “limiting initial empirical law, with convergence in probability as width tends to infinity,” and distinguish the exact finite conditional covariance `Q_n` from its deterministic limit. The existing averaging/convergence wording already indicates this interpretation.

2. At lines 207–212 and in the concluding synopsis, say “forward hidden paths `(z^(ell),h^(ell))`” when asserting the velocity/action bounds. This makes the scope of the actual differentiated-map proof unmistakable in the presence of the broader contract's observation list.

3. At lines 213–214, cite the individual prediction-gradient or backward/forward bounds, rather than only the bound on the loss gradient in (2), for bounded kernel blocks. The required estimates are already present.

4. Display one deterministic choice `L_*=2(M_0H_3(M_0)+1)^2`, mention `ceil(T/eta)` when covering the terminal partial segment, and retain “for sufficiently large n” when summarizing the GD result. These make existing quantifiers and constants easier to inspect; they repair no failed inequality.

5. If desired, replace “nonempty interval” by “interval of positive length” to exclude singleton intervals, and clarify that bounded higher derivatives means a bound for each fixed order. These are conventional wording refinements, not substantive objections.

No sharpening of the mode constants is required. No population theorem or additional convergence theorem should be added as part of repairing this finite-dynamics note, because none is necessary for the stated result and none has been proved here.

**Final scoped conclusion:** the candidate passes as an initial eligibility lemma plus dimension-uniform primal and forward-action estimates for finite GF and, at each fixed horizon, sufficiently-large-width exact GD with the prescribed raw interpolation. The audit does not certify the open full two-label target.
