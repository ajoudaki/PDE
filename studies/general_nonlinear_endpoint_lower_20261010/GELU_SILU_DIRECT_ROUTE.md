# Direct GELU/SiLU endpoint route: weighted covariance and readout localization

2026-10-11. Scoped independent theoretical route. Scientific inputs read in
full were `paper/compact.tex`, `paper/compact_fitting.tex`,
`NONODD_SCALAR_ROUTE.md`, `NONODD_INNOVATION_ROUTE.md`, and
`POSITIVE_ROUTE.md`. No experiment, other study, prior review, or additional
paper dependency was used. The rigorous-math, conjecture-investigation, and
canonical-notation skills, including the neural-network reference, were
applied.

The arbitrary-depth actual-endpoint theorem remains open in this route.
There are three proved additions. First, the full conditional covariance
lower bound fails already at initialization for all-GELU and all-SiLU, not
only for the earlier mixed-activation example. Second, a weighted version
of the Gaussian Hermite covariance lemma is valid for arbitrary adaptive
biases and avoids cross-cancellation by poorly conditioned neurons. Third,
the actual fitted readout retains a fixed fraction of its energy on neurons
whose conditional query-preactivation means are bounded. The third result
uses the original label cap, with no extra restriction on fixed labels.
Together these identify a direct route that does not have to compare a tiny
variance constant with a perturbative remainder. Its unresolved step is a
weighted covariance frame for deep non-Gaussian query features.

## 1. Exact target and the unused query randomness

Fix either
\[
\phi(z)=z\Phi(z)\quad\text{(exact GELU)},\qquad
\phi(z)=\frac{z}{1+e^{-z}}\quad\text{(SiLU)},
\]
and use that same activation at every hidden layer. Here \(\Phi\) is the
standard normal distribution function. Use the canonical forward pass
\[
h^{(1)}(x)=\phi(W^{(1)}x/\sqrt d),\quad
h^{(j)}(x)=\phi(W^{(j)}h^{(j-1)}(x)),\quad
f_n(x)=w^\top h^{(L)}(x)/n.
\]
The loss is \(\mathcal L=m^{-1}\sum_a r_a^2\), where
\(r_a=f_n(x_a)-y_a\). The actual gradient flow has block mobilities
\((n,1,\ldots,1,n)\), Gaussian initialization as in the paper, and
\(w(0)=0\). In particular,
\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\qquad
\dot w=-\frac2m\sum_a r_a h_a^{(L)},\qquad v_a=x_a/\sqrt d,
\]
with the ordinary backward responses and hidden updates from the paper.
Let \(S=\operatorname{span}\{v_a\}\) be proper and fix a unit
\(v\in S^\perp\). Condition on the active initialization: the first-layer
coordinates on \(S\), and all initialized hidden matrices. The training
trajectory is measurable under this conditioning and
\[
W_t^{(1)}v=Z,\qquad Z\sim N(0,I_n),
\tag{1}
\]
independently of it. Thus the actual endpoint query is obtained by starting
with \(h^{(1)}(Z)=\phi(Z)\) and applying the trained hidden matrices.

The desired conclusion is that, for two independent actual trained runs,
there are fixed \(c,p>0\), independent of width, such that eventually
\[
\Pr\{|f_n(\infty,\sqrt d\,v)
       -\widetilde f_n(\infty,\sqrt d\,v)|\ge c/\sqrt n\}\ge p.
\tag{2}
\]
All data and the nonzero labels remain fixed, with
\(\lambda=\gamma/m\le1\) and \(Y\le\lambda\beta^{-30L}\).

Both activations obey
\[
\phi(0)=0,\quad |\phi(z)|\le |z|,\quad
\phi(z)-\phi(-z)=z,\quad \sup_{z\in\mathbb R}|\phi'(z)|\le2.
\tag{3}
\]
For SiLU, use \(\sigma(-z)=1-\sigma(z)\) for
\(\sigma(z)=(1+e^{-z})^{-1}\), and
\(|z|\sigma(z)(1-\sigma(z))\le |z|e^{-|z|}\le1/e\).
For GELU, use \(\Phi(-z)=1-\Phi(z)\) and
\(|z|\Phi'(z)\le1/\sqrt{2\pi e}\).
Consequently the paper's population diagonal moments are at most one,
and its \(H=\max_{0\le j\le L}\sqrt{Q_{11}^{(j)}}\) equals one.
The third identity in (3) supplies an exact odd linear part of one
activation. It does not state an odd-part identity for a composition of
layers with nonzero intermediate means.

## 2. A full covariance lower bound fails for these activations too

At depth two and initialization, let \(X_j=\phi(Z_j)\) and
\(\mu=\mathbb E\phi(G)\), with \(G\sim N(0,1)\). Gaussian integration
by parts gives
\[
\mu=\frac1{2\sqrt\pi}>0\quad\text{for GELU},\qquad
\mu=\mathbb E[\sigma(G)(1-\sigma(G))]>0\quad\text{for SiLU}.
\tag{4}
\]
Write \(W=W_0^{(2)}\) and denote its \(i\)-th row by \(W_i\). Its
query preactivation is exactly
\[
W_iX=b_i+U_i,\qquad b_i=\mu\sum_jW_{ij},\qquad
U_i=\sum_jW_{ij}(X_j-\mu).
\tag{5}
\]
The row sums are independent \(N(0,1)\), so with probability tending to
one there is a row with \(b_i\le-\mu\sqrt{\log n}\). For example,
integrating the Gaussian density over
\([a,a+1/a]\), \(a=\sqrt{\log n}\), gives
\(\Pr\{G\le-a\}\ge Cn^{-1/2}/\sqrt{\log n}\); independence of the
rows then proves this claim. Simultaneously all row norms are at most two:
the chi-square exponential moment gives
\(\Pr\{\|W_i\|^2>4\}\le e^{-n}2^{n/2}\), and a union bound suffices.

For every deterministic row with norm at most two, \(\mathbb E_ZU_i^4\)
has an absolute upper bound. Indeed, if
\(\sigma_X^2=\mathbb E(X_1-\mu)^2\) and
\(M_4=\mathbb E(X_1-\mu)^4\), independence gives
\[
\mathbb E U_i^4
=3\sigma_X^4\|W_i\|^4
 +(M_4-3\sigma_X^4)\sum_j W_{ij}^4
\le(3\sigma_X^4+M_4)\|W_i\|^4.
\tag{6}
\]
The constants are finite by (3) and Gaussian fourth moments.

Put \(b_i=-t\), \(t>2\). On \(\{U_i\le t/2\}\), the activated
preactivation has square at most
\[
\eta_\phi(t)=\sup_{x\le-t/2}|\phi(x)|^2\longrightarrow0.
\]
For GELU, the elementary bound
\(u\Phi(-u)\le e^{-u^2/2}/\sqrt{2\pi}\) gives
\(\eta_\phi(t)\le e^{-t^2/4}/(2\pi)\). For SiLU,
\(|\phi(-u)|\le ue^{-u}\) gives
\(\eta_\phi(t)\le(t^2/4)e^{-t}\) for \(t\ge2\).
On \(\{U_i>t/2\}\), (3) and \(|U_i-t|\le3|U_i|\) give
\[
\mathbb E_Z\phi(-t+U_i)^2
\le\eta_\phi(t)+9\mathbb E[U_i^2\mathbf1_{U_i>t/2}]
\le\eta_\phi(t)+36\mathbb E U_i^4/t^2.
\tag{7}
\]
The last expression tends to zero uniformly over the stated row-norm
bound and over \(t\ge\mu\sqrt{\log n}\). Therefore
\[
\lambda_{\min}\bigl(\operatorname{Cov}_Z[
   \phi(W_0^{(2)}\phi(Z))]\bigr)\xrightarrow{\mathbb P}0.
\tag{8}
\]
This is a same-activation obstruction for both architectures under study.
It is compatible with the endpoint data assumptions: use two orthogonal
training directions and an orthogonal query. The first training Gram is
positive definite because \(\phi(G)\) is nonconstant; the resulting
two-dimensional Gaussian at layer two has full support. A nonzero linear
combination of its two activated coordinates cannot vanish identically,
since varying either coordinate would force \(\phi\) to be constant.
Thus the final training Gram is positive definite. Its diagonal is at
most one, so \(\gamma/m\le1\), and any nonzero fixed label vector small
enough to obey the original cap is admissible.

Equation (8) rules out a width-independent full-matrix lower bound even
before training. It does not imply that the covariance quadratic form at
the fitted readout is small.

## 3. A weighted covariance bound that allows arbitrary biases

Let \(A\in\mathbb R^{n\times r}\) have nonzero rows \(A_i\), and suppose
\[
a\le\|A_i\|\le A_+,\qquad
C_{ij}=\frac{A_iA_j^\top}{\|A_i\|\|A_j\|},\qquad
\|C\|_{\rm op}\le M,\qquad |C_{ij}|\le\rho<1\ (i\ne j).
\tag{9}
\]
Choose \(K\ge2\) so that \(\rho^{K-2}M^2\le1/2\). For arbitrary
\(b\in\mathbb R^n\), arbitrary \(R<\infty\), and
\(G\sim N(0,I_r)\), one has
\[
\operatorname{Cov}[\phi(AG+b)]\succeq c_R P_R,
\qquad (P_R)_{ii}=\mathbf1_{|b_i|\le R},
\tag{10}
\]
where \(c_R>0\) depends only on
\(\phi,a,A_+,M,\rho,R\), not on \(n,r,A,b\). This holds for either
activation and, more generally, for every nonaffine analytic Lipschitz
activation. There is no independence requirement on \(A\) and \(b\):
the assertion is deterministic in those objects.

To prove it, use the normalized probabilists' Hermite coefficients
\[
\alpha_k(b,s)=\mathbb E\left[
\phi(b+sG)\frac{H_k(G)}{\sqrt{k!}}\right],\qquad G\sim N(0,1).
\]
The Hermite generating-function identity for correlated Gaussian pairs
gives the exact covariance expansion
\[
\operatorname{Cov}[\phi(AG+b)]
=\sum_{k\ge1}\operatorname{diag}(\alpha_k(b_i,\|A_i\|))
 C^{\circ k}\operatorname{diag}(\alpha_k(b_i,\|A_i\|)).
\tag{11}
\]
Every term is positive semidefinite, because \(C^{\circ k}\) is the Gram
matrix of the normalized row tensor powers. Also, for \(k\ge K\),
\[
\sum_{j\ne i}|C_{ij}|^k
\le\rho^{k-2}\sum_jC_{ij}^2\le\rho^{k-2}M^2\le\tfrac12.
\]
Applying \(2|u_i u_j|\le u_i^2+u_j^2\) to the off-diagonal terms
therefore proves \(C^{\circ k}\succeq I/2\). Consequently (11) yields
the stronger weighted statement
\[
\operatorname{Cov}[\phi(AG+b)]
\succeq\frac12\operatorname{diag}\left\{
                  \sum_{k\ge K}\alpha_k(b_i,\|A_i\|)^2\right\}.
\tag{12}
\]
At every finite \(b\) and positive \(s\), the Hermite tail in braces
is positive. Otherwise \(\phi(b+sx)\) would agree almost everywhere
with a polynomial of degree below \(K\), then everywhere by continuity;
global Lipschitz continuity would make that polynomial affine. The tail
is continuous in \((b,s)\), since Lipschitz continuity gives continuity
in Gaussian \(L^2\). Its minimum over
\([-R,R]\times[a,A_+]\) is therefore positive. Half that minimum is
a valid \(c_R\) in (10).

This proof is stronger than restricting the covariance matrix to good
neurons. It gives a lower bound on the *whole* quadratic form by the
readout energy on good neurons, so arbitrary correlations with the other
neurons cannot cancel the lower bound. The elementary row geometry in
`POSITIVE_ROUTE.md` supplies, uniformly for a Frobenius perturbation of
size at most \(0.1\), the fixed choices
\(a=0.8,A_+=1.2,M=144,\rho=1/2,K=18\) on a Gaussian initialization
event of probability tending to one.

## 4. The actual fitted readout has energy on bounded-offset neurons

Return to the actual all-GELU or all-SiLU endpoint. Define
\[
B_0=[h_0^{(L)}(x_1),\ldots,h_0^{(L)}(x_m)]/\sqrt n,\quad
u_*=B_0(B_0^\top B_0)^{-1}y,\quad e=\|u_*\|,
\quad u_\infty=w_\infty/\sqrt n.
\tag{13}
\]
The readout estimate in Section 1 of `NONODD_SCALAR_ROUTE.md` gives,
on an active event of probability tending to one,
\[
\|u_\infty-u_*\|\le120F e(Y/\lambda)^2\le e/8,
\qquad \|u_\infty\|\le3e.
\tag{14}
\]
Here \(F\) is the fitting coefficient. The last inequality uses the
original cap: since \(H=1\), the supplied bound
\(8H\sqrt F\le\beta^{5L}\) gives
\(120F(Y/\lambda)^2\le(120/64)\beta^{-50L}<1/8\).
No activation-dependent variance constant appears in this use of the cap.

We first prove an empirical fourth-moment estimate with the interpolation
normalization \(e\), rather than the residual-activity normalization.
Write \(H_i\in\mathbb R^m\) for the \(i\)-th row of the initialized
training-feature matrix and \(q=(B_0^\top B_0)^{-1}y\). Eventually,
with probability tending to one,
\[
\lambda_{\min}(B_0^\top B_0)\ge\gamma/2,\qquad
\frac1n\sum_i\|H_i\|^4\le4m^2.
\tag{15}
\]
For the second assertion, condition on all preceding initialized training
features. Top rows are independent Gaussian transforms. Their conditional
fourth moments at each sample converge to
\(\mathbb E\phi(\sqrt{Q_{aa}^{(L-1)}}G)^4\le3\), by (3), and their
conditional eighth moments remain bounded. Conditional Chebyshev and
initialization Gram convergence therefore give
\(n^{-1}\sum_iH_{ia}^4\le4\) simultaneously for the fixed number of
samples. Finally \((\sum_aH_{ia}^2)^2\le m\sum_aH_{ia}^4\).
Thus (15) does not assume that \(q\) is independent of the rows.

Since \(\|q\|^2\le2e^2/\gamma\) and
\(\sqrt n\,u_{*,i}=H_i^\top q\), (15) proves
\[
n\sum_i u_{*,i}^4
\le\frac{16e^4}{\lambda^2}.
\tag{16}
\]
For any subset \(J\) of neurons, including one chosen adaptively from the
complete training state, Cauchy--Schwarz now gives
\[
\sum_{i\in J}u_{*,i}^2
\le\frac{4e^2}{\lambda}\sqrt{|J|/n}.
\tag{17}
\]

Define the actual conditional query means and final preactivation offset
by
\[
\mu_\infty^{(L-1)}=\mathbb E_Z h_\infty^{(L-1)}(Z),\qquad
b=W_\infty^{(L)}\mu_\infty^{(L-1)}.
\tag{18}
\]
Let \(s=\max(1,\|\phi'\|_\infty)\le2\) and
\(K_j=s(9s)^{j-1}\). The query map from \(Z\) to
\(h_\infty^{(j)}(Z)\) is \(K_j\)-Lipschitz and equals zero at zero.
The operator bounds on the active fitting event thus imply
\[
\frac{\|b\|}{\sqrt n}
\le9\frac{\|\mu_\infty^{(L-1)}\|}{\sqrt n}
\le9K_{L-1}=:C_b.
\tag{19}
\]
This is a conditional statement; no event involving the unused realization
of \(Z\) was added to the active conditioning.

Set \(R=64C_b/\lambda\), and let
\(J=\{i:|b_i|>R\}\). Equation (19) gives
\(|J|/n\le C_b^2/R^2\); (17) consequently gives
\(\sum_{i\in J}u_{*,i}^2\le e^2/16\). If \(P_R\) denotes the
diagonal projection onto \(\{|b_i|\le R\}\), then (14) yields
\[
\|P_Ru_\infty\|
\ge\|P_Ru_*\|-\|u_\infty-u_*\|
\ge\left(\frac{\sqrt{15}}4-\frac18\right)e
\ge\frac e{\sqrt2}.
\tag{20}
\]
This localization conclusion is proved for the *actual trained readout*
and actual endpoint offsets. Its cutoff may depend on the fixed data gap,
which is allowed. It is not a claim that the discarded neurons are
independent of the retained ones.

## 5. The sufficient direct bridge, and its exact remaining obstruction

Equations (14)--(20) show that it would suffice to prove, on an active
event whose probability stays positive (or tends to one),
\[
\operatorname{Cov}_Z[h_\infty^{(L)}(Z)]\succeq c_R P_R
\quad\text{with a fixed }c_R>0.
\tag{21}
\]
The desired direct consequence of (21) does not require the constant
\(c_R\) to exceed the size of a training perturbation. Indeed, (20) gives
\[
\operatorname{Var}_Z f_n(\infty,\sqrt d\,v)
\ge c_Re^2/(2n).
\tag{22}
\]
The same scalar function has Gaussian Lipschitz constant at most
\(3K_Le/\sqrt n\), by (14). For two independent runs, condition on both
active states, put \(D=f_n-\widetilde f_n\), and write
\(E=e^2+\widetilde e^2\). Then
\[
\operatorname{Var}(D)\ge c_RE/(2n),\qquad
\operatorname{Lip}(D)^2\le9K_L^2E/n.
\]
Gaussian Poincare applied first to \(D\), then to
\((D-\mathbb ED)^2\), gives
\(\mathbb E|D-\mathbb ED|^4\le405K_L^4E^2/n^2\).
These applications follow from the Gaussian Hermite expansion, with each
positive degree weighted by its degree in gradient energy; smooth
Lipschitz growth supplies the required integrability. Thus
\[
\frac{\mathbb ED^4}{(\mathbb ED^2)^2}
\le8\max\{1,1620K_L^4/c_R^2\}.
\tag{23}
\]
Paley--Zygmund applied to \(D^2\) at one half its expectation gives a
positive conditional probability, independent of width, that
\(|D|\ge\sqrt{c_RE/(4n)}\). Finally
\(e^2\to e_0^2=y^\top(Q^{(L)})^{-1}y>0\), by Gram convergence.
This proves (2) if (21) holds on a suitable positive-probability active
event for each run. Arbitrary conditional means are harmless in (23).

The exact identity at the final trained layer is
\[
h_\infty^{(L)}(Z)=\phi\left(
 W_\infty^{(L)}[h_\infty^{(L-1)}(Z)
                         -\mu_\infty^{(L-1)}]+b\right).
\tag{24}
\]
Unlike the input in (10), the centered vector inside this affine map is
not Gaussian. At depth two it is already the centered iid vector
\(\phi(Z)-\mathbb E\phi(Z)\); at greater depths its coordinates are
dependent. Matching its covariance to a Gaussian does not give (11):
the Hermite identity used there requires a jointly Gaussian pair of
preactivations. Nor does a covariance lower bound for that vector pass
through a nonlinear map by a general monotonicity principle.

The mean-adapted comparator of `NONODD_SCALAR_ROUTE.md`, Section 5, has
the same difficulty. Although its mixers are initialized matrices, its
adaptive offsets depend on all active weights, and its centered lower
features remain non-Gaussian. Conditioning on those offsets does not
produce independent Gaussian mixer rows. A high-order chaos argument
uniform over the adaptive biases and small trained mixer perturbations
would be a new sufficient mechanism; no such argument has been proved
here.

The route status is therefore **open at the weighted covariance frame
(21)**. The full-matrix alternative is disproved by (8); the scalar
readout localization required by a weighted approach is proved by (20).
This is a more specific remaining obligation than an unrestricted claim
that fitted readout energy might escape to saturated neurons. It does not
prove the original endpoint theorem, and it does not justify replacing
the actual deep query features by Gaussian or frozen features.
