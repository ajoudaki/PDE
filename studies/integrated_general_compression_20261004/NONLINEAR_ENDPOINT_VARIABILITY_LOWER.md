# Actual nonlinear endpoint variability from an unobserved input direction

2026-10-04. Scoped independent derivation using the current study's complete
`GENERAL_EXPLICIT_FITTING.md`, its complete check, and the maintained notation
contract. No experiment or population-training comparison is used. This is
an internally derived lower bound for actual trained predictions. The first
hidden activation is the identity and the second is nonlinear; the result
does not claim that both hidden activations are nonlinear.

## 1. Model and endpoint statement

Fix unit training vectors \(v_a=x_a/\sqrt d\), \(a=1,\ldots,m\), and
nonzero labels \(y\in\mathbb R^m\). Suppose their span \(V\) has dimension
\(1\le r<d\). The sample rank may be less than \(m\). Choose any fixed
unit vector \(v_*\in V^\perp\), so the original query is
\(x_*=\sqrt d\,v_*\). Consider the canonical two-hidden-layer network
\[
 h^{(1)}(v)=Av,\qquad h^{(2)}(v)=\tanh(WAv),\qquad
 f_n(v)=w^\top h^{(2)}(v)/n,
\]
where \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Initialize their entries independently as
\(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and \(w=0\).
Use mean squared loss, residuals \(r_a=f_n(v_a)-y_a\), and block
mobilities \((n,1,n)\). The actual physical equations are
\[
 \delta_a=w\odot\operatorname{sech}^2(WAv_a),\qquad
 \dot A=-\frac2m\sum_a r_aW^\top\delta_av_a^\top,
\]
\[
 \dot W=-\frac2{mn}\sum_a r_a\delta_a(Av_a)^\top,
 \qquad \dot w=-\frac2m\sum_a r_a\tanh(WAv_a).            \tag{1}
\]
All parameter blocks follow these equations; no hidden block is frozen.

Let the limiting initialized top-feature covariance be
\[
 Q_{ab}=\mathbb E[\tanh(G_a)\tanh(G_b)],\qquad
 G\sim N(0,(v_a^\top v_b)_{a,b}),
\]
\[
 \gamma=\lambda_{\min}(Q)>0,\qquad
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,
 \qquad 0<Y\le\frac{\lambda}{8\sqrt{85}}.               \tag{2}
\]
Thus \(\gamma\) is the unweighted covariance gap. Define the label
energy and universal probability constant
\[
 E_y=\sqrt{y^\top Q^{-1}y},\qquad
 p_* =\frac1{20\,9^4\,80000^2}.                         \tag{3}
\]
These are positive and independent of width. There are training-measurable
events \(\mathcal G_n\), specified below, on which the actual endpoint
exists and fits \(y\). Conditionally on the training initialization, on
\(\mathcal G_n\),
\[
 \mathbb P\left\{|f_n(\infty,v_*)|\ge
                 \frac{Y}{400\sqrt n}\,\middle|\,\mathcal F_{\rm tr}\right\}
 \ge p_* .                                               \tag{4}
\]
There is also the label-energy version with threshold
\(E_y/(400\sqrt{2n})\).

For two independently initialized networks, trained on exactly these data
with the same physical dynamics, conditionally on both training
initializations and their good events,
\[
 \mathbb P\left\{
 |f_n^{(1)}(\infty,v_*)-f_n^{(2)}(\infty,v_*)|
 \ge\frac{E_y}{400\sqrt n}
 \,\middle|\,\mathcal F_{\rm tr}^{(1)},\mathcal F_{\rm tr}^{(2)}
 \right\}\ge p_* .                                      \tag{5}
\]
This is an endpoint statement about the actual nonlinear trained
predictions. It has no small-label Taylor remainder. In particular it
also lower-bounds their whole-sphere, all-time discrepancy.

Here is a fully explicit probability qualification. For \(0<\delta<1\),
let \(N_{\rm fit}^{(r)}(\delta)\) be the fitting threshold in (7) below.
For every
\[
 n\ge\max\{2^{32},N_{\rm fit}^{(r)}(\delta)\},
 \qquad
 \varepsilon_n=2ne^{-n/250}+n^2(en)^{-162/25},             \tag{6}
\]
one has \(\mathbb P(\mathcal G_n)\ge1-\delta-\varepsilon_n\).
The unconditional probability of the event in (5), together with existence
and fitting of both endpoints, is at least
\(p_*\max\{0,1-\delta-\varepsilon_n\}^2\).
The powers and constants are deliberately conservative.

The proof leaves the unused Gaussian coordinates independent of training,
establishes a covariance gap using the third Gaussian chaos, and applies
a fourth-moment inequality to the conditional endpoint prediction.

## 2. Training-only conditioning and the existing fitting theorem

Choose an orthonormal basis matrix \(U\in\mathbb R^{d\times r}\) for
\(V\). The training dynamics depend only on \(A U,W,w\), with unit inputs
\(U^\top v_a\in\mathbb R^r\). Equation (1) gives
\(\dot A(I-UU^\top)=0\). The reduced first block \(A_0U\) again has
independent standard Gaussian entries, independently of \(W_0\), and
\[
 Z:=A_0v_*\sim N(0,I_n)
\]
is independent of
\(\mathcal F_{\rm tr}:=\sigma(A_0U,W_0)\). Thus the complete training
trajectory and its endpoint are measurable in \(\mathcal F_{\rm tr}\),
and
\[
 f_n(t,v_*)=\frac1n w(t)^\top\tanh(W(t)Z).               \tag{7a}
\]
In particular, one must use an initialization event for this reduced
training system. Conditioning on the original full-sphere event in
dimension \(d\) would additionally restrict \(Z\) and would not justify
its independent Gaussian conditional law.

For identity--tanh, the fitting constants can be chosen as
\(b=0,s=H=1,t_2=2,L=2,F=85,U_2=2\). The source's explicit reduced
dimension threshold becomes, with \(e=\min\{1/4,\gamma/(2m)\}\),
\[
 N_{\rm fit}^{(r)}(\delta)=\left\lceil\max\left\{
 1,\frac{\log(16/\delta)}{8-2\log9},
 \frac{r\log9+\log(8/\delta)}{8-\log9},
 \frac{384(m^2+513^r)(2+2\sqrt2)^2}{\delta e^2}
 \right\}\right\rceil.                                  \tag{7}
\]
This uses a safe real second-derivative bound, rather than its sharp
value. The fitting theorem on its initialization tests gives, with
probability at least \(1-\delta\), global existence, physical parameter
convergence, exact endpoint interpolation, and
\[
 \sup_{t\ge0}\|W(t)\|_{\rm op}<9,\qquad
 \sup_{t\ge0}\|W(t)-W_0\|_F
 \le\frac{16Y^2}{\lambda^{3/2}}\le\frac{\sqrt\lambda}{340}
 \le\frac1{340}.                                      \tag{8}
\]
The last inequality uses \(\lambda\le Q_{aa}<1\).
For \(\mathsf H(t)=[\tanh(W(t)A(t)v_a)]_{a=1}^m\), those same
initialization tests and feature-displacement estimates also give
\[
 \left\|\frac{\mathsf H(0)^\top\mathsf H(0)}n-Q\right\|_{\rm op}
 \le\gamma/2,
 \qquad
 \left\|\frac{\mathsf H(t)-\mathsf H(0)}{\sqrt n}\right\|_{\rm op}
 \le\sqrt\gamma/8.                                   \tag{9}
\]
The first assertion is the covariance test explicitly constructed in
the fitting theorem's proof, rather than only its weaker displayed
least-eigenvalue consequence. The second follows from its per-sample
feature displacement \(\sqrt\lambda/8\), multiplied by \(\sqrt m\).
All events and bounds in this paragraph are measurable in
\(\mathcal F_{\rm tr}\).

## 3. A uniform third-Hermite coefficient

Let \(G\sim N(0,1)\), and let
\(H_3(g)=g^3-3g\) be the third probabilists' Hermite polynomial. For
\(9/10\le\sigma\le11/10\), define its normalized coefficient
\[
 a_3(\sigma)=\frac1{\sqrt6}\mathbb E[\tanh(\sigma G)H_3(G)].
\]
One Gaussian integration by parts gives
\[
 a_3(\sigma)
 =\frac\sigma{\sqrt6}\mathbb E[(G^2-1)\operatorname{sech}^2(\sigma G)]
 =\frac\sigma{\sqrt6}
       \operatorname{Cov}(G^2,\operatorname{sech}^2(\sigma G)).
                                                               \tag{10}
\]
The covariance is strictly negative because \(u\mapsto
\operatorname{sech}^2(\sigma\sqrt u)\) is strictly decreasing.
We need the following explicit uniform bound:
\[
                         a_3(\sigma)\le-1/100.          \tag{11}
\]
To verify it, take independent copies \(U=G^2,U'=G'^2\) and use
\[
 \operatorname{Cov}(U,g(U))
 =\tfrac12\mathbb E[(U-U')(g(U)-g(U'))].
\]
The integrand is nonpositive. On the two interchanged events
\(|G|\le1/2\), \(|G'|\ge3/2\), its absolute value is at least
\[
 2D,\qquad
 D=\operatorname{sech}^2(11/20)
                  -\operatorname{sech}^2(27/20)>1/2.
\]
The probabilities of the two one-dimensional events are at least
\(1/3\) and \(1/10\), respectively. For the first, integrate the
Gaussian density lower bound on \([-1/2,1/2]\). For the second,
integration by parts gives the elementary Mills lower bound
\[
 \mathbb P\{|G|\ge a\}\ge
 \frac{2a}{1+a^2}\frac{e^{-a^2/2}}{\sqrt{2\pi}}
 \quad(a>0),
\]
which is greater than \(1/10\) at \(a=3/2\).
For explicit rational checks, \(e^{1/8}\le8/7\), \(e<3\), and
\(\sqrt{2\pi}<18/7\) give the two probability lower bounds just used.
Also
\(\cosh(11/20)<29/25\), \(\cosh(27/20)>41/20\), hence
\[
 D>\frac{625}{841}-\frac{400}{1681}
   =\frac{714225}{1413721}>\frac12.
\]
The first cosh inequality follows by retaining its quadratic term and
bounding the remaining positive Taylor series by a geometric series
whose ratio is \(121/12000\); the second follows by retaining the
terms through degree six. Thus (10) is at most
\[
 -\frac{2(9/10)}{\sqrt6}\frac13\frac1{10}\frac12
 =-\frac3{100\sqrt6}<-\frac1{100},
\]
proving (11).

## 4. Covariance gap at Gaussian initialization and after training

Write \(W_{0,i}\) for the rows of \(W_0\),
\(\sigma_i=\|W_{0,i}\|_2\), and
\(C_{ij}=W_{0,i}^\top W_{0,j}/(\sigma_i\sigma_j)\).
The following event is measurable in \(W_0\):
\[
 9/10\le\sigma_i\le11/10\quad\hbox{for every }i,
 \qquad |C_{ij}|\le4\sqrt{\log(en)/n}\quad(i\ne j).       \tag{12}
\]
Its failure probability is at most \(\varepsilon_n\) in (6).
Indeed the chi-square moment generating function and Chernoff's bound
give, for \(0<\eta<1\),
\(\mathbb P\{|\sigma_i^2-1|>\eta\}\le2e^{-n\eta^2/8}\).
Take \(\eta=19/100\) and sum over rows; the resulting bound is at
most \(2ne^{-n/250}\). Conditionally on any nonzero \(W_{0,i}\),
\(W_{0,i}^\top W_{0,j}/\sigma_i\sim N(0,1/n)\).
On \(\sigma_j\ge9/10\), a correlation above the threshold in (12)
requires this scalar Gaussian to exceed \((18/5)\sqrt{\log(en)/n}\).
Its two-sided tail is at most \(2(en)^{-162/25}\). Summing over
unordered pairs gives the second term of \(\varepsilon_n\).

For \(n\ge2^{32}\),
\[
 \max_i\sum_{j\ne i}|C_{ij}|^3
 \le\frac{64[\log(en)]^{3/2}}{\sqrt n}\le\frac12.
\]
The last inequality holds at \(2^{32}\), using \(\log(e2^{32})<33\),
and persists because \([\log(en)]^{3/2}/\sqrt n\) is decreasing
for \(\log(en)>3\). Since \(C_{ii}=1\), the elementary row-sum
bound for a symmetric matrix gives
\[
                         C^{\circ3}\succeq\tfrac12 I_n. \tag{13}
\]
Here \(C^{\circ3}\) denotes entrywise cubing.

For clarity, the Gaussian-chaos covariance decomposition used next can
be obtained directly from
\(\mathbb E[e^{tG-t^2/2}e^{sG'-s^2/2}]=e^{C_{ij}ts}\).
Comparing coefficients gives
\(\mathbb E[H_k(G)H_l(G')]=\mathbf1_{k=l}\,k!C_{ij}^k\).
Expanding the bounded function \(\tanh(\sigma_iG)\) in the
orthonormal Gaussian Hermite basis consequently gives
\[
 \operatorname{Cov}_Z[\tanh(W_0Z)]
 =\sum_{k\ge1}\operatorname{diag}(a_k(\sigma_i))
                  C^{\circ k}\operatorname{diag}(a_k(\sigma_i)).
                                                               \tag{14}
\]
Each summand is positive semidefinite: \(C^{\circ k}\) is the Gram
matrix of the tensor powers of the normalized row vectors. The series
converges as a covariance form by the scalar \(L^2\) expansions; only
finitely many coordinates are involved at each fixed width. The third
summand, (11), and (13) prove
\[
                 \operatorname{Cov}_Z[\tanh(W_0Z)]
                         \succeq I_n/20000.             \tag{15}
\]
No least-singular-value bound for \(W_0\) is used.

For any deterministic vector \(a\in\mathbb R^n\) and matrix \(W\),
the scalar functions \(a^\top\tanh(WZ)\) and
\(a^\top\tanh(W_0Z)\) are odd, hence have mean zero. Lipschitz
continuity of tanh and Cauchy--Schwarz give
\[
 \|a^\top[\tanh(WZ)-\tanh(W_0Z)]\|_{L^2(Z)}
 \le\|a\|_2\|W-W_0\|_F.                               \tag{16}
\]
Intersect event (12) with the reduced fitting event to define
\(\mathcal G_n\). For every time, including the endpoint, (8), (15),
and the reverse triangle inequality in \(L^2(Z)\) imply
\[
 \begin{aligned}
 \|a^\top\tanh(W(t)Z)\|_{L^2(Z)}
 &\ge\left(\frac1{100\sqrt2}-\frac1{340}\right)\|a\|_2
 \ge\frac1{200\sqrt2}\|a\|_2.
 \end{aligned}
\]
Therefore, on this one training-measurable event,
\[
 \operatorname{Cov}_Z[\tanh(W(t)Z)]\succeq I_n/80000
 \quad\hbox{for every }t\in[0,\infty].                  \tag{17}
\]
The numerical comparison uses \(340>200\sqrt2\).

## 5. Readout size forced by fitting

Put \(\mathsf B(t)=\mathsf H(t)/\sqrt n\). Equation (9) gives
\(\mathsf B(0)^\top\mathsf B(0)\preceq(3/2)Q\).
For any \(c\in\mathbb R^m\),
\[
 \|\mathsf B(\infty)c\|_2
 \le\left(\sqrt{3/2}+\frac18\right)\sqrt{c^\top Qc},
\]
because \(Q\succeq\gamma I_m\). The square of this coefficient is
less than two. Consequently the actual trained Gram satisfies
\[
 G_\infty:=\mathsf B(\infty)^\top\mathsf B(\infty)\preceq2Q.
                                                               \tag{18}
\]
It is positive definite by the fitting theorem. Exact interpolation is
\(\mathsf B(\infty)^\top(w_\infty/\sqrt n)=y\).
The minimum norm solution of this linear constraint is
\(\mathsf B(\infty)G_\infty^{-1}y\): subtracting it from any solution
leaves an orthogonal vector. Hence
\[
 \frac{\|w_\infty\|_2^2}{n}
 \ge y^\top G_\infty^{-1}y\ge\tfrac12 y^\top Q^{-1}y
 =\tfrac12 E_y^2.                                      \tag{19}
\]
Independently, \(|\tanh|\le1\) and interpolation imply
\[
                         \|w_\infty\|_2/\sqrt n\ge Y.  \tag{20}
\]
Thus the lower bound concerns a nonzero fitted readout, not a readout
whose amplitude was imposed separately from training.

## 6. Fourth moment and actual endpoint anti-concentration

Condition on \(\mathcal F_{\rm tr}\) on \(\mathcal G_n\), and abbreviate
\(g(Z)=w_\infty^\top\tanh(W_\infty Z)/n\). This is an odd function
of a standard Gaussian vector, with mean zero. By (17),
\[
 \mathbb E_Zg^2\ge\frac{\|w_\infty\|_2^2}{80000n^2}.
\]
Its Euclidean Lipschitz constant is at most
\(L_g=9\|w_\infty\|_2/n\), since \(\|W_\infty\|_{\rm op}<9\).
The Gaussian Poincare inequality gives
\[
 \mathbb E_Zg^2\le L_g^2,\qquad
 \operatorname{Var}_Z(g^2)\le4L_g^2\mathbb E_Zg^2,
 \qquad \mathbb E_Zg^4\le5L_g^4.                       \tag{21}
\]
One direct proof of the inequality used here expands a smooth square
integrable function in multivariate orthonormal Hermites. Its variance
is the sum of squared coefficients of nonzero degree; its gradient
energy weights each such coefficient by its degree, which is at least
one. The Gaussian functions \(g,g^2\) here are smooth and bounded
with square integrable gradients, so the expansion applies. This also
justifies (21) without a concentration-theorem constant.

For a nonnegative random variable \(X\) with finite second moment,
Cauchy--Schwarz on \(\{X\ge\theta\mathbb EX\}\) gives
\[
 \mathbb P\{X\ge\theta\mathbb EX\}
 \ge(1-\theta)^2(\mathbb EX)^2/\mathbb EX^2
 \quad(0<\theta<1).
\]
Apply this with \(X=g^2\), \(\theta=1/2\), and (21). The readout
size cancels in the probability ratio, yielding
\[
 \mathbb P_Z\{|g|\ge\sqrt{\mathbb E_Zg^2/2}\}\ge p_*.
\]
Equation (20) makes the threshold at least \(Y/(400\sqrt n)\);
(19) gives the alternative \(E_y/(400\sqrt{2n})\). This proves (4).

For two independent initializations, condition on both training sigma
fields on their good events. The two remaining vectors \(Z_1,Z_2\)
are independent standard Gaussians. Their prediction difference is odd
in the joint Gaussian vector. Its conditional variance is at least
\[
 \frac{\|w_\infty^{(1)}\|_2^2+\|w_\infty^{(2)}\|_2^2}{80000n^2},
\]
and its squared Lipschitz constant is at most
\(81(\|w_\infty^{(1)}\|_2^2+\|w_\infty^{(2)}\|_2^2)/n^2\).
The identical fourth-moment argument gives probability at least \(p_*\).
Using (19) for both runs makes its threshold at least
\(E_y/(400\sqrt n)\), proving (5). Integrating the conditional
probability and using independence of the training events proves (6)'s
unconditional qualification.

If \(y\) lies in a least-eigenvalue eigenspace of \(Q\), then
\[
 E_y=\frac{\|y\|_2}{\sqrt\gamma}=Y\sqrt{m/\gamma}
     =Y/\sqrt\lambda.
\]
Thus (5) gives a genuine \(Y/\sqrt{\lambda n}\) lower scale in
that label direction. For every label vector, \(E_y\ge Y\), because
\(\lambda_{\max}(Q)\le\operatorname{tr}Q\le m\).

## 7. Nonlinearity and the limits of the claim

This construction uses a nonlinear second hidden layer and the actual
all-parameter gradient flow. Its unused first-layer input coordinates
are frozen by the exact training geometry, rather than by modifying the
optimizer. Hidden learning can be verified already for a single datum:
if \(a=A_0v_1\), \(z=W_0a\), and \(y_1\ne0\), then
\[
 \dot w(0)=2y_1\tanh z,\qquad
 \ddot W(0)=\frac{4y_1^2}{n}
       [\tanh z\odot\operatorname{sech}^2z]a^\top,
\]
\[
 \ddot A(0)=4y_1^2W_0^\top
       [\tanh z\odot\operatorname{sech}^2z]v_1^\top.
\]
Both hidden second derivatives are nonzero almost surely. The proof
nevertheless covers every finite training configuration satisfying
the stated span and covariance conditions, not only this example.

The result establishes a positive-probability lower bound at a single
fixed unobserved query and the fitted endpoint. It does not assert a
lower bound at every query, or for labels with \(Y=0\), or for input
spans equal to the entire ambient space. It does not establish such a
bound for every activation in the general strip class. In this example
the identity activation has unbounded values, and tanh is holomorphic
with bounded derivative on any sufficiently narrow common strip, so
the example belongs to the integrated theorem's activation class.
Its label assumption (2) is the existing dense-fitting allowance and
is implied by the integrated study's smaller common label cap.
