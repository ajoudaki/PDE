# Bounded assessment of a slower-than-root counterexample

Scope: the actual canonical dense finite network and its population, fixed finite data and labels independent of width, Gaussian initialization, zero initial readout, the manuscript's positive initial Gram gap and sufficiently small fixed labels. The error includes the whole physical-time supremum and a fixed finite-second-moment query law. This note is a theoretical diagnostic, not a proof of a trained width rate.

## 1. What a negative construction must respect

The manuscript already gives qualitative all-time convergence in probability in this scope. Consequently an error bounded below by a positive constant with a probability bounded away from zero cannot be a counterexample under these same hypotheses. Qualitative convergence does not rule out a slower vanishing rate such as \(n^{-\alpha}\), \(\alpha<1/2\), or a logarithmic rate.

A dataset with angle \(\vartheta_n\to0\) as width grows changes the theorem's quantifiers: its Gram gap and admissible small-label threshold can degenerate with width. Such a family may refute a constant uniform over datasets, but not a \(C_\delta(\text{fixed data})/\sqrt n\) theorem. A bad constant for one fixed near-degenerate dataset likewise is not a changed exponent.

Exact duplicate inputs or, for odd activations, exact antipodes have a singular feature Gram. They fail the full-Gram assumption. Compatible labels may reduce to a smaller problem; incompatible labels violate fitting. Neither case supplies the required negative construction.

## 2. Near-coincident two-input stress: the small mode also has small fluctuations

Take two tanh hidden layers and circle inputs
\[
x_0=\sqrt d\,e_1,\qquad
x_\vartheta=\sqrt d(\cos\vartheta\,e_1+\sin\vartheta\,e_2),
\]
embedded in any \(d\ge2\). Labels \(y=(\epsilon,-\epsilon)\) excite the weak mode, with \(\epsilon>0\) fixed and chosen within the manuscript's threshold for the fixed angle. This is a candidate stress, not a claimed negative example.

Write the initialized first preactivation columns as independent standard Gaussian vectors \(a,b\), and the initialized hidden matrix as \(W\), whose entries are independent \(N(0,1/n)\). Define
\[
h=\tanh a,\qquad s=\operatorname{sech}^2a,\qquad
z=Wh,\qquad T=W(s\odot b).
\]
The initial second-layer feature along the input circle is
\[
g(\vartheta)=\tanh\!\left(W\tanh(a\cos\vartheta+b\sin\vartheta)\right),
\quad
g'(0)=\operatorname{sech}^2z\odot T.
\]
Let \(\Gamma_{w,n}(\vartheta)=H^\top H/(2n)\), where the two columns of \(H\) are \(g(0),g(\vartheta)\), and let \(e_-=(1,-1)/\sqrt2\). For every finite initialization,
\[
e_-^\top\Gamma_{w,n}(\vartheta)e_-
 =\frac{\|g(\vartheta)-g(0)\|_2^2}{4n},
\]
\[
C_n:=\lim_{\vartheta\to0}
 \frac{e_-^\top\Gamma_{w,n}(\vartheta)e_-}{\vartheta^2}
 =\frac1{4n}\sum_{j=1}^n\operatorname{sech}^4(z_j)T_j^2.
\tag{1}
\]
This is a Rayleigh quotient at finite width, not a claim that \(e_-\) is its exact eigenvector.

For a standard Gaussian \(G\), put
\[
q_*=\mathbb E\tanh^2G,\qquad
v_*=\mathbb E\operatorname{sech}^4G,\qquad
\beta(q)=\mathbb E\operatorname{sech}^4(\sqrt q\,G).
\]
Then
\[
C_*=\tfrac14v_*\beta(q_*)>0,\qquad
|\mathbb EC_n-C_*|\le C/n,\qquad
\mathbb E|C_n-C_*|^2\le C/n.
\tag{2}
\]

### Proof of the quantitative claim

Conditional on \(a,b\), the row pairs \((z_j,T_j)\) are independent centered Gaussian pairs with covariance entries
\[
q_n=\frac{\|h\|_2^2}n,\quad
v_n=\frac{\|s\odot b\|_2^2}n,\quad
c_n=\frac{h^\top(s\odot b)}n.
\]
For a centered Gaussian pair \((Z,T)\) with these covariance entries and a smooth bounded function \(F\) with bounded derivatives, two Gaussian integrations by parts give
\[
\mathbb E[T^2F(Z)]
 =v_n\mathbb EF(Z)+c_n^2\mathbb EF''(Z).
\tag{3}
\]
One verification conditions \(T\) on \(Z\) for \(q_n>0\), uses
\(\mathbb E[Z^2F(Z)]=q_n\mathbb EF(Z)+q_n^2\mathbb EF''(Z)\),
and cancels the inverse powers of \(q_n\). Continuity covers the degenerate case.

With \(F=\operatorname{sech}^4\) and \(\gamma(q)=\mathbb EF''(\sqrt q\,G)\), (3) yields
\[
\mathbb E[C_n\mid a,b]
 =\tfrac14\{v_n\beta(q_n)+c_n^2\gamma(q_n)\}.
\tag{4}
\]
The conditional variance is at most \(3v_n^2/(16n)\), since \(0\le F\le1\) and \(\mathbb ET^4=3v_n^2\).

The triples \((h_i^2,s_i^2b_i^2,h_is_ib_i)\) are iid with all fixed moments finite. Their means are \((q_*,v_*,0)\). Their empirical second moments of centered averages are \(O(n^{-1})\), and their fourth moments are \(O(n^{-2})\). These follow by expanding powers of centered sums: only terms with no singleton index survive.

Gaussian integration by parts gives
\(\beta'(q)=\tfrac12\mathbb EF''(\sqrt qG)\) and
\(\beta''(q)=\tfrac14\mathbb EF^{(4)}(\sqrt qG)\).
These derivatives and \(\gamma\) are bounded on \(0\le q\le1\). Taylor expansion of \(v_n\beta(q_n)\) at \(q_*\), using
\(\mathbb E[v_n(q_n-q_*)]=O(n^{-1})\) and
\(\mathbb E[v_n(q_n-q_*)^2]=O(n^{-1})\), gives its bias \(O(n^{-1})\). Also \(\mathbb Ec_n^2=O(n^{-1})\).

For the mean-square estimate, split
\[
v_n\beta(q_n)-v_*\beta(q_*)
 =(v_n-v_*)\beta(q_n)+v_*\{\beta(q_n)-\beta(q_*)\}.
\]
Boundedness and Lipschitz continuity of \(\beta\) give squared expectation \(O(n^{-1})\); bounded \(\gamma\) and \(\mathbb Ec_n^4=O(n^{-2})\) control the other term in (4). Finally integrate the conditional variance bound. This proves (2), including the finite-width mean bias.

### Population weak eigenvalue

The population feature Gram has equal diagonal entries, so \(e_-\) is its weak eigenvector for sufficiently small nonzero \(\vartheta\). The first-layer covariance satisfies
\[
\mathbb E[\tanh G\,\tanh(G\cos\vartheta+G'\sin\vartheta)]
 =q_*-\tfrac12v_*\vartheta^2+o(\vartheta^2),
\]
where \(G'\) is an independent standard Gaussian. Differentiating the covariance under the Gaussian integral and integrating by parts proves this expansion; bounded tanh derivatives justify differentiation.

For the second-layer Gaussian pair, the derivative of its tanh-product expectation with respect to its off-diagonal covariance is the expectation of the product of the two tanh derivatives. At coincident variables this is \(\beta(q_*)\). This identity follows by differentiating the Gaussian covariance interpolation and integrating by parts, with bounded derivatives also covering the coincident limit. Consequently
\[
\lambda_{\min}(\Gamma_{w,\infty}(\vartheta))
 =C_*\vartheta^2+o(\vartheta^2).
\tag{5}
\]

Equations (1)–(5) show the diagnostic mechanism: in the near-coincident expansion, the weak training direction has size \(\vartheta^2\), and its random coefficient still has root-width fluctuations and \(1/n\) bias. Treating its error as a generic absolute \(n^{-1/2}\) entrywise error discards the small difference between the two features and exaggerates the relative singularity.

This takes the small-angle derivative at each fixed finite width and then estimates its coefficient. It does not exchange a joint angle/width limit, control every finite-angle Gram eigenvalue, or establish a trained rate. It gives no basis for claiming that highly correlated inputs alone cause a slower width exponent.

## 3. Current assessment and experiment decision

No construction in this bounded assessment proves a slower-than-root rate for the canonical trained dense model. The existing actual first-feedback calculation likewise has \(1/n\) bias and root-width fluctuation. These are local diagnostics, not a positive all-time theorem.

The matched-loss response calculation provides another warning: even a diverging second derivative of a loss-matched trajectory can occur from singular loss coordinates near interpolation while same-time sensitivities remain bounded. That mechanism, analyzed in LOSS_MATCHED_VARIATIONS.md, is not evidence of a slow dense width rate.

A useful experiment would need to separate finite-width mean bias, ordinary fluctuations, numerical fitting error, and a genuinely common population reference. A few nearly coincident inputs and a few widths without those controls cannot identify an asymptotic exponent. The available device check on 2026-10-01 reported that the NVIDIA driver could not be contacted. No training experiments, CPU substitute sweep, or numerical rate fit were run. No GPU setup or optimization work was undertaken.

The warranted conclusion is open, not negative. A future counterexample should locate a reachable feedback mechanism producing a slow empirical-to-population correction, rather than infer one from a degenerating data constant or from coordinate singularities.
