# Independent audit: odd-activation fitted endpoint theorem

Verdict: **PASS**, for the theorem's stated fixed-problem assumptions,
including odd activations, a proper training span, and
\(Q^{(L)}_{11}\ge\beta^{-40L}\). No strengthening of the original label
cap is required under those assumptions. The proof controls the actual
fully trained endpoint. Its frozen-feature predictor is only a comparator.

The audit read only the three assigned scientific inputs and the required
rigorous-math and canonical-notation skills, including the neural-network
reference. It did not inspect other study artifacts, prior verdicts, or the
additional files included by the manuscript. The author corrected one
centering phrase during the audit; the final phrase was checked directly.
The verdict attaches to these SHA-256 hashes:

| Input | SHA-256 |
| --- | --- |
| `ODD_DEPTH_ENDPOINT.md` | `e0babb343a9de9a1c16cfbcbb775a7ec7a3f8d4800dcbc216699c5b21c913677` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |

The theorem initially supplied for review had hash
`c928e2e9f4e3c0b8de0e6c18df08c348bf0abe2219791a10d79813da6339ade7`.
The sole change checked between those versions replaces a reference to
conditional means by conditional-population centering constants. Exact
conditional expectations of empirical inverse statistics are unnecessary.

## Scope and source assumptions

The inherited source setup has fixed \(m\ge2\), \(L\ge2\), inputs
\(x_a=\sqrt d\,v_a\) with \(\|v_a\|=1\), Gaussian initialized weights,
zero initialized readout, and block mobilities \((n,1,\ldots,1,n)\).
The loss is \(m^{-1}\sum_a r_a^2\), where \(r_a=f_n(x_a)-y_a\).
The source population Gram \(Q=Q^{(L)}\) is positive definite;
\(\gamma=\lambda_{\min}(Q)\), \(\lambda=\gamma/m\le1\), and
\(Y=\|y\|/\sqrt m>0\). All data and activations stay fixed as width grows.

The source fitting lemma supplies the estimates needed here. Its real-flow
argument uses only a bound on real activation derivatives; replacing its
half-strip derivative bound by the smaller real bound in the local
coefficients does not invalidate that argument. The original envelope
\(\beta\) still bounds those coefficients. No source assumption requires
\(m\le d\), or \(m\) to be bounded by the training-span dimension.

## 1. Fitting event and unused Gaussian coordinates

Let \(k\) be the dimension of the training span and let
\(R\in\mathbb R^{d\times k}\) have orthonormal columns spanning it.
The active first-layer matrix is \(W^{(1)}R\), and the effective normalized
training inputs are \(R^\top v_a\). Equivalently, the fitting lemma is
applied to the dimension-\(k\) inputs \(\sqrt k R^\top v_a\). These have
norm \(\sqrt k\), preserve all input inner products and population Grams,
and give exactly the original training equations in the active coordinates.

Consequently there is a fitting event of probability tending to one that
depends only on \(W^{(1)}_0R\) and the initialized hidden matrices. It gives
parameter convergence, exact fitting, the hidden operator bounds, training
feature RMS bound \(2H\), and
\[
 \rho(t)\le Ye^{-\lambda t/2},\qquad
 \int_0^\infty\rho(t)\,dt\le2Y/\lambda,
 \quad \rho(t)=\|r(t)\|/\sqrt m.
\]

For the prescribed unit vector \(v\) orthogonal to the training span,
\(\dot W^{(1)}v=0\). The vector \(Z=W^{(1)}_0v\) is standard Gaussian
and independent of the active initialization. This follows from orthogonal
projections of each isotropic Gaussian first-layer row. The complete training
trajectory is active-measurable. In particular, no full-input-sphere fitting
event that reveals \(Z\) is needed.

After this conditioning the initialized and trained query maps are odd
functions of \(Z\), since every activation is odd and there are no biases.
Their vector expectations vanish even though the trained matrices depend
on the labels.

## 2. Comparison with the frozen-feature interpolator

Write \(B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n\) and
\(u_t=w_t/\sqrt n\). Then \(f_n(t,X)=B_t^\top u_t\) and
\(\dot u_t=-(2/m)B_t r_t\). On the initial Gram event define
\[
 u_*=B_0(B_0^\top B_0)^{-1}y,\qquad e=\|u_*\|.
\]
One has \(B_0^\top u_*=y\) and \(e\le\sqrt2Y/\sqrt\lambda\).

The note's coefficients \(U_j,F_j,F\) correctly give, on a finite interval,
with \(M=\sup_t\|u_t\|\) and \(A_t=\int_0^t\rho\),
\[
 \|B_t-B_0\|_{\rm op}/\sqrt m\le2FMA_t.
\]
Each normalized hidden-block velocity is at most
\(2U_j\rho\|u\|\); forward differentiation gives the stated recursion
for \(F_j\). The matrix bound follows by bounding its Frobenius norm.

The exact energy identity is
\[
 \tfrac12\partial_t\|u_t-u_*\|^2
 =-2\rho^2+\frac2m\langle(B_t-B_0)^\top u_*,r_t\rangle.
\]
Its time integral gives
\(\|u_t-u_*\|^2\le e^2+4FMeA_t^2\). At a maximizing time with
\(M\ge e\), expanding \((M-e)^2\) yields
\(M\le2e+4FeA_T^2\). The original cap implies
\(4FA_T^2\le16F(Y/\lambda)^2\le1\), so \(M\le3e\), uniformly
over the interval and hence over all times.

If \(P\) is projection onto the range of \(B_0\), integration of the
readout equation gives
\[
 \|(I-P)u_\infty\|\le24Fe(Y/\lambda)^2.
\]
Using interpolation at the actual endpoint,
\(B_0^\top(u_\infty-u_*)=-(B_\infty-B_0)^\top u_\infty\), and the
smallest singular value \(\sqrt{\gamma/2}\), gives
\[
 \|P(u_\infty-u_*)\|
 \le4\sqrt2FM^2Y/\lambda^{3/2}
 \le72Fe(Y/\lambda)^2.
\]
Thus the note's bound with coefficient \(120\) is valid; the sum of the
two displayed coefficients is only \(96\). No additional inverse-gap
factor has been dropped.

## 3. The fluctuation-scale correction

Condition on the active initialization throughout this paragraph. The
initialized layer-\(j\) query map is
\(K_j=s(8s)^{j-1}\)-Lipschitz. Gaussian Poincaré in the needed form says
that for a Lipschitz scalar function \(g\) of a standard Gaussian vector,
\(\operatorname{Var}(g(Z))\le\mathbb E\|\nabla g(Z)\|^2\).
Applying this to \(a^\top h_0^{(j)}(Z)\) bounds its variance by
\(K_j^2\|a\|^2\). Its mean is zero by oddness. Summing over the rows
of any fixed matrix \(E\) therefore gives
\[
 \mathbb E_Z\|Eh_0^{(j)}(Z)\|^2\le K_j^2\|E\|_F^2.
\]
The matrix \(E\) can be a trained displacement: after active conditioning
both it and the initialized hidden matrices are fixed. No independence
between those matrices is being asserted.

The hidden displacements satisfy
\(\|W^{(j)}_\infty-W^{(j)}_0\|_F\le4U_jMY/\lambda\).
Subtracting forward recursions using
\[
 W^{(j)}_\infty h^{(j-1)}_\infty-W^{(j)}_0h^{(j-1)}_0
 =W^{(j)}_\infty(h^{(j-1)}_\infty-h^{(j-1)}_0)
 +(W^{(j)}_\infty-W^{(j)}_0)h^{(j-1)}_0
\]
proves the note's \(L^2(Z)\) feature difference bound
\(4MYT_L/\lambda\). The first-layer difference at this query is zero.

For \(f_{\rm RF}=u_*^\top h_0^{(L)}(Z)/\sqrt n\), decompose the
prediction difference into changed readout acting on initial features and
final readout acting on changed features. This gives
\[
 \|f_n(\infty,\sqrt d v)-f_{\rm RF}\|_{L^2(Z)}
 \le\frac{120K_LFe(Y/\lambda)^2+4M^2YT_L/\lambda}{\sqrt n}.
\]
The second numerator is at most
\(36\sqrt2 eY^2T_L/\lambda^{3/2}\), hence at most
\(36\sqrt2 eT_L(Y/\lambda)^2\) because \(\lambda\le1\).
This explicitly verifies equation (11), including that inherited assumption.
The bound concerns the actual trained endpoint and has no hidden
\(\sqrt n\) loss.

## 4. Conditional normal limit and random centering

Set \(q=Q_{11}\) and \(e_0^2=y^\top Q^{-1}y\). Orthogonality makes the
initial population covariance between query and training coordinates zero.
At each successive layer the latent Gaussian blocks are then independent;
oddness preserves zero feature cross-moments. At the last layer the limiting
training feature vector \(H\) and query feature \(H_*\) are independent,
with \(\mathbb EH_*^2=q\) and \(\mathbb EHH^\top=Q\). Therefore
\[
 \operatorname{Var}(H_*H^\top Q^{-1}y)=qe_0^2>0.
\]

For the finite-width argument, condition instead on all initialized layers
before the last hidden layer, including their query coordinates. This is a
different conditioning from Section 3; the two arguments are combined only
by unconditional probability bounds. Write \(S\) for the preceding
empirical augmented Gram. Conditional on \(S\), last-layer neuron rows are
iid Gaussian transforms. The finite-dimensional Gram converges to its
population value by conditional Chebyshev and continuity of the Gaussian
feature expectations. Linear growth supplies the required bounded moments
on bounded covariance sets, also at singular covariances.

Define the conditional-population quantities
\[
 Q(S)=\mathbb E_S HH^\top,\quad
 q(S)=\mathbb E_S HH_*,\quad
 c(S)=q(S)^\top Q(S)^{-1}y.
\]
Near the limiting covariance, \(Q(S)^{-1}\) is uniformly bounded.
The empirical interpolator is \(\widehat q^\top\widehat Q^{-1}y\).
The inverse identity and conditional moment bounds give
\[
 \sqrt n(f_{\rm RF}-c(S))
 =\frac1{\sqrt n}\sum_{i=1}^n
 (H_{*,i}-q(S)^\top Q(S)^{-1}H_i)
 H_i^\top Q(S)^{-1}y+o_{\mathbb P}(1).
\]
The remainder before multiplication by \(\sqrt n\) is
\(O_{\mathbb P}(n^{-1})\). Each summand has mean zero. Its variance tends
to \(qe_0^2\), and its third absolute moment is uniformly bounded, since
it has at most quadratic growth in a Gaussian vector with bounded covariance.
The characteristic-function expansion with third-order remainder proves
the triangular central limit theorem for every deterministic sequence of
covariances approaching the limit. A contradictory sequence proves the
needed local uniformity.

Consequently, for two independent runs, conditionally on their lower layers,
\[
 \sqrt n\{f_{\rm RF}-\widetilde f_{\rm RF}-c(S)+c(\widetilde S)\}
 \ \Longrightarrow\ N(0,2qe_0^2).
\]
Weak convergence to this continuous distribution is uniform in interval
endpoints. The potentially uncontrolled shift
\(\sqrt n(c(S)-c(\widetilde S))\) therefore causes no problem: among all
intervals of a given length, the centered interval has greatest mass under
a centered normal law. The claimed small-interval probability is bounded by
\[
 2\Phi(1/(4\sqrt2))-1
 \le\frac1{4\sqrt\pi}<\frac16.
\]
This argument does not assert a centered unconditional normal limit, does
not need a convergence rate for the preceding Gram, and does not identify
\(c(S)\) with an exact finite-width conditional expectation. Exceptional
singular empirical Grams have vanishing probability and may be assigned a
dummy comparator value without affecting the conclusion.

## 5. Constants and transfer of the lower bound

Initial Gram convergence implies \(e\to e_0\) in probability. On each
active fitting event intersected with \(e\le\sqrt2e_0\), the two endpoint
corrections have difference with \(L^2\) norm at most
\(2\sqrt2De_0(Y/\lambda)^2/\sqrt n\). Conditional Markov followed by
averaging therefore bounds the probability of error exceeding
\(\sqrt q e_0/(8\sqrt n)\) by
\[
 512D^2(Y/\lambda)^4/q.
\]
No independence between a fitting event and the frozen predictor is needed.
If \(D(Y/\lambda)^2\le\sqrt q/64\), this bound is \(1/8\). The limiting
success probability after subtracting the small-interval and exceptional
events is at least \(1-1/6-1/8=17/24>1/2\). The triangle inequality
gives exactly the theorem's threshold \(\sqrt q e_0/(8\sqrt n)\).

The coefficient envelope is valid. In particular,
\(F\le\beta^{10L}\), \(K_L\le\beta^{2L}\), and
\(T_L\le2LHs^3(9s)^{2L-4}\le\beta^{7L}\) for the inherited \(L\ge2\).
Thus \(D\le\beta^{16L}\). The original label cap and the added diagonal
condition give
\[
 D(Y/\lambda)^2\le\beta^{-44L}
 \le\beta^{-20L}/64\le\sqrt q/64.
\]
Without the diagonal condition, the alternative additional cap
\(Y\le\lambda q^{1/4}/(8\sqrt D)\) correctly supplies the same inequality.
It must not be inferred from the original cap for arbitrary odd activations.

There is also a valid simpler consequence: equal input norms imply
\(\operatorname{tr}Q=mq\), so
\[
 qy^\top Q^{-1}y\ge q\|y\|^2/\lambda_{\max}(Q)
 \ge\|y\|^2/m=Y^2.
\]
The weaker threshold \(Y/(8\sqrt n)\) therefore has the same probability
guarantee under the theorem's assumptions.

## 6. Concrete activations and remaining limits

The strip assumptions hold for arbitrary layerwise mixtures of \(\tanh\),
\(\arctan\), \(\sin\), and \(z+\tanh z\), by choosing a common strip
strictly inside the nearest tanh and arctan singularities. Their first
derivatives are bounded on that strip; the last activation is unbounded on
the real axis, as allowed.

For a standard Gaussian \(G\), the supplied density bound proves
\(\mathbb E[G^2\mathbf1_{|G|\le1}]>1/8\). On \([-1,1]\), both tanh
and arctan have absolute value at least half the absolute argument.
Monotonicity then gives Gaussian second moment at least
\(\min(q,1)/32\) for every positive variance \(q\). The sine identity
\((1-e^{-2q})/2\ge\min(q,1)/4\) is correct. For \(z+\tanh z\), equal
signs of the summands give second moment at least \(q\). Starting from
variance one, any mixture consequently has
\(Q^{(L)}_{11}\ge32^{-L}\ge\beta^{-40L}\). Layerwise activations with
unit Gaussian second moment also preserve diagonal variance one.

A separately checked consequence extends this concrete list to erf and
asinh, including mixtures with the four functions above. The function erf
is entire, with \(|\operatorname{erf}'(x+iy)|\le2e^{a^2}/\sqrt\pi\) on
any fixed strip \(|y|<a\). Concavity on \([0,1]\) and
\(e^{-t^2}\ge1-t^2\) give
\(\operatorname{erf}(u)\ge u\operatorname{erf}(1)
\ge4u/(3\sqrt\pi)>u/2\). On a strip \(|y|<a<1\), asinh has its
analytic real branch and
\[
 |1+(x+iy)^2|^2=(1+x^2-y^2)^2+4x^2y^2\ge(1-a^2)^2,
\]
so its derivative is bounded by \((1-a^2)^{-1/2}\). Its real derivative
on \([0,1]\) is at least \(1/\sqrt2\), hence
\(\operatorname{asinh}(u)\ge u/\sqrt2>u/2\) for positive \(u\) there.
Both functions are odd and increasing, so the same Gaussian second-moment
bound \(\min(q,1)/32\) and diagonal recursion apply. This consequence
does not modify the frozen theorem file.

No theorem-level correction remains. For maximum clarity, the sentence
describing the centered normal difference may display the explicitly
\(\sqrt n\)-scaled formula in Section 4 of this report; that scaling is
already supplied by the preceding CLT argument and following probability
bound. The use of \(\lambda\le1\) in equation (11) is also worth making
explicit, but it is an existing hypothesis.

The conclusion does not cover nonodd activations or full-span training.
This audit certifies neither an impossibility result for those cases nor
the separate obstruction document referenced by the note, which was
outside the frozen input scope. The width threshold remains unquantified,
and the assertion is eventual at each individual width, exactly as stated.
