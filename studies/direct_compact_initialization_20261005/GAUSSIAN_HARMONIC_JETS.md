# Gaussian harmonic moments and an evaluable second-jet source

Status: author-checked low-order results, 2026-10-06. This note proves an
explicit logarithmic harmonic approximation for the initial first layer,
a joint Gaussian-mark construction for a tagged first-layer second jet,
and exact finite-width moment computation for polynomialized finite jets.
It does not prove growing-order uniformity or the requested full neural
trajectory theorem.

The scoped sources are the assignment, this study's author artifacts,
`docs/notation.qmd`, and the complete maintained sections on polynomial
Gaussian moments (`docs/02-gaussian-reuse.qmd`, section 4), normalized
Gaussian forests (`docs/07-observable-closure.qmd`, section B), and
general-dimensional first-order initialized coefficients (the final
substantive section of the same chapter). The other authorized study was
not used. The shared instructions and research/proof skills were reread.
The canonical-notation skill remains inaccessible (`Permission denied`);
the supervisor-authorized explicit-notation fallback is retained.

## 1. Exact harmonic covariance for an actual first-layer neuron

Take \(d\ge2\), fix two orthonormal vectors \(e_1,e_2\), and consider
the spherical input circle

\[
 x(\theta)=\sqrt d\,(e_1\cos\theta+e_2\sin\theta),
 \qquad 0\le\theta<2\pi.
\]

For a standard Gaussian first-layer row, its two projections
\(a=(a_1,a_2)\) are independent standard Gaussians. Its initial feature is

\[
 h_a(\theta)=\phi(a_1\cos\theta+a_2\sin\theta),\qquad \phi=\tanh.
\]

Define its complex Fourier coefficients by

\[
 c_k(a)=\frac1{2\pi}\int_0^{2\pi}h_a(\theta)e^{-ik\theta}\,d\theta,
 \qquad k\in\mathbb Z.
 \tag{1}
\]

Write the Gaussian vector in polar coordinates as
\(a=r(\cos\alpha,\sin\alpha)\). Then \(\alpha\) is uniform on
\([0,2\pi)\), independent of \(r\), whose density is
\(r e^{-r^2/2}\) on the positive line. The change of variables in (1)
gives

\[
 c_k(a)=t_k(r)e^{-ik\alpha},\qquad
 t_k(r)=\frac1{2\pi}\int_0^{2\pi}\phi(r\cos u)e^{-iku}\,du.
 \tag{2}
\]

The numbers \(t_k(r)\) are real, and \(t_{-k}=t_k\), because the
integrand without its exponential is even in \(u\). Antipodal oddness
gives \(t_k=0\) for even \(k\), including zero. Integrating the polar
phase therefore proves

\[
 \mathbb Ec_k=0,\qquad
 \mathbb E[c_k\overline{c_l}]=\delta_{kl}\lambda_k,
 \qquad
 \lambda_k=\int_0^\infty t_k(r)^2r e^{-r^2/2}\,dr.
 \tag{3}
\]

Every odd mode has \(\lambda_k>0\). To verify this without assuming a
special-function formula, expand tanh near zero as
\(\phi(z)=\sum_{j\ge0}a_jz^{2j+1}\). Its differential equation
\(\phi'=1-\phi^2\) gives \(a_0=1\) and

\[
 (2j+1)a_j=-\sum_{p+q=j-1}a_pa_q\quad(j\ge1).
\]

Induction shows \(a_j=(-1)^jb_j\) with \(b_j>0\). The highest
Fourier coefficient of \(\cos^k u\) is \(2^{-k}\). Thus, for positive
odd \(k=2j+1\),
\(t_k(r)=2^{-k}a_jr^k+O(r^{k+2})\) near zero. It is nonzero on a
small interval, and the Rayleigh density is positive there, proving the
claim. The local expansion exists because
\(\tanh z=(e^{2z}-1)/(e^{2z}+1)\) is analytic near zero.

The population kernel has the equivalent Gaussian and Fourier formulas

\[
 \begin{aligned}
 K(\theta,\psi)
 &=\mathbb E[h_a(\theta)h_a(\psi)]\\
 &=\mathbb E[\phi(G_1)\phi(\cos(\theta-\psi)G_1
                       +\sin(\theta-\psi)G_2)]\\
 &=\sum_{k\in\mathbb Z}\lambda_k e^{ik(\theta-\psi)},
 \end{aligned}
 \tag{4}
\]

where \(G_1,G_2\) are independent standard Gaussians. The convergence
justifying the last formula is established next. This is a nonzero
covariance kernel even though every coefficient mean in (3) vanishes.

## 2. An explicit stretched-exponential angular tail

For \(z=x+iy\),

\[
 |\tanh z|^2=
 \frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}\le1
 \qquad (|y|\le\pi/4).
\]

For fixed \(r>0\), the function \(u\mapsto\tanh(r\cos u)\) is
analytic and bounded by one in the strip

\[
 |\operatorname{Im}u|\le s(r):=\operatorname{arsinh}(\pi/(4r)).
\]

Indeed \(|\operatorname{Im}(r\cos(u+iv))|\le r\sinh|v|\).
Shifting the Fourier contour inside this strip, with cancelling periodic
vertical sides, gives \(|t_k(r)|\le e^{-|k|s(r)}\).

For \(k\ge1\), split the radius at \(r=k^{1/3}\). On the smaller
radius event,
\(s(r)\ge\operatorname{arsinh}(\pi/(4k^{1/3}))
\ge k^{-1/3}\operatorname{arsinh}(\pi/4)\); the second inequality
uses concavity of arsinh and its value zero at zero. The remaining
Rayleigh probability equals \(e^{-k^{2/3}/2}\). Consequently

\[
 \lambda_k\le
 e^{-2\operatorname{arsinh}(\pi/4)k^{2/3}}
 +e^{-k^{2/3}/2}
 \le2e^{-k^{2/3}/2}.
 \tag{5}
\]

Let \(h_{a,L}(\theta)=\sum_{|k|\le L}c_k(a)e^{ik\theta}\), and
let \(K_L\) be (4) restricted to \(|k|\le L\). There are absolute
finite constants \(C,c>0\) such that

\[
 \mathbb E\sup_\theta|h_a(\theta)-h_{a,L}(\theta)|^2
 +\sup_{\theta,\psi}|K(\theta,\psi)-K_L(\theta,\psi)|
 \le C e^{-cL^{2/3}}.
 \tag{6}
\]

To justify the first assertion, each realized neuron has an absolutely
convergent Fourier series by its positive strip width. Bound its uniform
tail by \(\sum_{|k|>L}|c_k|\), then use Cauchy--Schwarz with weights
\(k^{-2}\). The expected squared tail is at most
\((\sum_{k\ne0}k^{-2})\sum_{|k|>L}k^2\lambda_k\).
By (5), split the exponential into two equal factors and bound one by its
value at \(L\); the sum of the other factor times \(k^2\) is finite.
This proves the first bound. The kernel bound follows from
\(\sum_{|k|>L}\lambda_k\) in exactly the same way. The same absolute
summability justifies exchanging expectation and the Fourier sums in (4).

Thus \(L=O(\log(C/\varepsilon)^{3/2})\) suffices both for uniform
population-kernel error \(\varepsilon\) and for root-mean-square
uniform feature error \(\varepsilon\), after changing the constants.
This is an actual logarithmic law-based source approximation. It concerns
the initial first layer; it is not a two-layer training theorem.

There is also a pointwise computable envelope suitable for selecting
neurons. For \(r>0\) define

\[
 e_L(a)=\frac{2e^{-(L+1)s(r)}}{1-e^{-s(r)}},\qquad r=|a|,
 \quad s(r)=\operatorname{arsinh}(\pi/(4r)),
 \tag{6a}
\]

and set \(e_L(0)=0\). Summing the geometric Fourier bound gives
\(\sup_\theta|h_a(\theta)-h_{a,L}(\theta)|\le e_L(a)\)
for every mark \(a\). Moreover,

\[
 \mathbb E e_L(a)^2\le C e^{-cL^{2/3}}.
 \tag{6b}
\]

To check integrability and the rate, write
\(c_0=\operatorname{arsinh}(\pi/4)\). The previous concavity bound
and the cases \(r\le1\), \(r\ge1\) give
\(s(r)\ge c_0/(1+r)\). Also
\((1-e^{-s})^{-1}\le1+s^{-1}\), from \(e^s\ge1+s\).
Hence
\(e_L(a)\le C(1+r)e^{-c_0L/(1+r)}\). Split its squared expectation
at \(r=L^{1/3}\). The lower-radius part is bounded by
\(C(1+L^{1/3})^2e^{-c_0L^{2/3}}\), after adjusting constants for
\(L\ge1\). On the upper-radius part, discard the exponential factor
and integrate \((1+r)^2re^{-r^2/2}\); its tail is bounded by
\(C(1+L^{1/3})^2e^{-L^{2/3}/2}\). Absorbing these polynomial factors
into a weaker exponential proves (6b).

In particular, suppose any finite positive source rule has nodes
\(a_i\), weights \(D_i\ge0\), and the checked scalar property
\(\sum_iD_i e_L(a_i)^2\le4\mathbb Ee_L^2\). Then, without any
independence assumption on its selected nodes,

\[
 \sup_\theta\sum_iD_i|h_{a_i}(\theta)-h_{a_i,L}(\theta)|^2
 \le4\mathbb Ee_L^2\le C e^{-cL^{2/3}}.
 \tag{6c}
\]

Thus adding \(e_L\) as one source function to a selected feature Gram
can certify selected-node tail control. Constant or coordinate source
functions may be appended separately if a selection construction needs
them. This implication does not itself supply the selection theorem or
make its retained-mode covariance error vanish; those are distinct
properties to verify in a synthesis.

The joint coefficient law is also evaluable: sample the two-dimensional
Gaussian \(a\), then use (1) or (2) for all retained modes. Independently
sampling Gaussian coefficients with variances \(\lambda_k\) would match
(3) but would not produce this neuron law. For example, the actual
\(|c_k|\le1\), whereas a nondegenerate Gaussian coefficient is unbounded;
the actual phases and amplitudes also share the same \(\alpha,r\).

## 3. Zero means persist under the canonical learning dynamics

Consider the canonical two-tanh-layer network
\(f_n(x)=w^T\phi(W\phi(Ax/\sqrt d))/n\), with zero readout,
independent Gaussian matrices, mean squared loss, and block mobilities
\((n,1,n)\). Fix any finite dataset and labels.

Let \(S\) be a diagonal sign matrix on the first hidden population.
The transformation \((A,W,w)\mapsto(SA,WS,w)\) leaves every prediction
unchanged. It is orthogonal within each parameter block and commutes with
the constant scalar mobilities. Differentiating the invariant loss shows
that its gradient field transforms by the same map; uniqueness of the
finite smooth ODE therefore makes the whole flow equivariant. The
Gaussian initialization law and zero readout are invariant as well.

Choosing one negative sign shows that each first-layer neuron field has
the same law as its negative, at every time where the flow exists. Its
mean is zero. The same holds for every integrable harmonic coefficient
or time/feature jet of that neuron. A sign transformation
\((A,W,w)\mapsto(A,TW,Tw)\) gives the corresponding assertion in the
second population. At initialization every fixed-order jet is integrable:
its finite derivative formula contains finitely many Gaussian matrix
factors and bounded tanh derivatives, so a polynomial Gaussian envelope
is integrable.

This does not make predictions zero: readout and upper feature change sign
together, so their product is unchanged. Already for one sample,
\(\mathbb E\partial_tf_n(0,x_1)=2y\mathbb E\kappa_n\ne0\) when
\(y\ne0\), with \(\kappa_n=\|\phi(W\phi(Ax_1/\sqrt d))\|_2^2/n>0\)
almost surely. Averaging neuron fields or weights before applying the
network would erase the information retained in their joint products.

## 4. Exact reused-matrix moments for the second feature jet

For the following explicit calculation there is one training point
\(x_1=x(0)=\sqrt d\,e_1\). Use feature time \(s\) so that
\(\dot s=2(y-f_n(x_1))\). At initialization put

\[
 h_i=\phi(a_{i1}),\qquad v=Wh,\qquad
 b(z)=\phi(z)\phi'(z),\qquad R=W^Tb(v),\qquad
 q_n=\|h\|_2^2/n.
\]

The first derivatives of hidden features vanish because the readout is
zero. Differentiating the exact feature flow gives the second derivative
of a first-layer neuron at a test angle:

\[
 J_i(\theta):=\partial_s^2h_i(0,\theta)
 =\cos\theta\,\phi'(a_i\cdot v_\theta)\phi'(a_{i1})R_i,
 \quad v_\theta=(\cos\theta,\sin\theta).
 \tag{7}
\]

The corresponding physical-time second derivative is \(4y^2J_i\),
since \(s'(0)=2y\) and the first feature derivative is zero.

For \(u\ge0\) define three scalar Gaussian expectations

\[
 \zeta(u)=\mathbb E b'(\sqrt uG),\qquad
 \beta(u)=\mathbb E b(\sqrt uG)^2,\qquad
 \chi(u)=\mathbb E(b^2)''(\sqrt uG).
\]

Conditioning on the entire first layer, Gaussian integration by parts in
each independent row of \(W\) gives the following exact finite-width
identities:

\[
 \begin{aligned}
 \mathbb E_W R_i&=h_i\zeta(q_n),\\
 \mathbb E_W[R_iR_j]
 &=\delta_{ij}\beta(q_n)
 +h_ih_j\left[(1-1/n)\zeta(q_n)^2+\chi(q_n)/n\right].
 \end{aligned}
 \tag{8}
\]

For the first equation,
\(\mathbb E_W[W_{ri}b(v_r)]=h_i\mathbb E_Wb'(v_r)/n\), and
sum over the \(n\) rows. For the second, unequal rows contribute
\((1-1/n)h_ih_j\zeta^2\). For an equal row, two integrations by
parts give

\[
 \mathbb E_W[W_{ri}W_{rj}b(v_r)^2]
 =\delta_{ij}\beta(q_n)/n+h_ih_j\chi(q_n)/n^2.
\]

Summing proves (8). This keeps the forward/transpose reuse exactly; a
fresh independent backward matrix would incorrectly remove its response.

Define the purely first-layer angular coefficient

\[
 j_k(a)=\frac1{2\pi}\int_0^{2\pi}
 \cos\theta\,\phi'(a\cdot v_\theta)\phi'(a_1)e^{-ik\theta}\,d\theta.
 \tag{9}
\]

Then the second-jet coefficient is exactly \(R_i j_k(a_i)\). For example,
its mixed and second moment entries at finite width are given by

\[
 \begin{aligned}
 \mathbb E[c_k(a_i)\overline{R_i j_l(a_i)}]
 &=\mathbb E[c_k(a_i)\overline{j_l(a_i)}h_i\zeta(q_n)],\\
 \mathbb E[R_i j_k(a_i)\overline{R_i j_l(a_i)}]
 &=\mathbb E\!\left[j_k(a_i)\overline{j_l(a_i)}
 \{\beta(q_n)+h_i^2[(1-1/n)\zeta(q_n)^2+\chi(q_n)/n]\}\right].
 \end{aligned}
 \tag{10}
\]

The expectations on the right still include the first-layer empirical
variance. Equation (10) is an exact reduction, not permission to replace
\(q_n\) by its mean at finite width.

Angular integration passes through every displayed Gaussian expectation
and integration-by-parts step. For (1), (9), and their finite parameter
derivatives, tanh derivatives are bounded and angular factors have modulus
at most one. With reused matrix factors, a fixed-order expression is
bounded by a polynomial in finitely many Gaussian coordinates. The angular
domain has finite measure and these Gaussian envelopes have finite
expectation. Fubini, dominated differentiation, and the vanishing Gaussian
boundary terms therefore justify the interchanges. No growing derivative
order is implicit.

## 5. A jointly evaluable three-Gaussian source for the tagged second jet

Put \(q=\mathbb E\phi(G)^2\), \(\zeta=\zeta(q)\),
\(\beta=\beta(q)\). A source for the limiting joint initial feature
and second-jet field of a fixed tagged neuron is

\[
 a_1,a_2,\Gamma\ \text{independent }\mathcal N(0,1),\qquad
 R_* =\zeta\phi(a_1)+\sqrt\beta\,\Gamma,
 \tag{11}
\]

together with \(h_a(\theta)\) and
\(J_*(\theta)=\cos\theta\phi'(a\cdot v_\theta)\phi'(a_1)R_*\).
It uses three Gaussian marks and scalar Gaussian integrals, and can be
evaluated at arbitrary angles. It is more information than a covariance
matrix, and uses no dense realization.

Here is the fixed-order width identification. Conditional on \(h,v\),
Gaussian row regression gives exactly

\[
 R\ \overset d=\ h\frac{T_n}{q_n}
 +\sqrt{B_n}\left(I-\frac{hh^T}{nq_n}\right)\gamma,
 \quad
 T_n=\frac1n\sum_rv_rb(v_r),\quad
 B_n=\frac1n\sum_rb(v_r)^2,
 \tag{12}
\]

where \(\gamma\) is a standard Gaussian vector independent of \(h,v\).
The exceptional event \(q_n=0\) has probability zero. The usual variance
calculation for averages of independent variables gives
\(q_n\to q\), and, conditionally on \(h\), the same calculation for
the independent \(v_r\sim\mathcal N(0,q_n)\) gives
\(T_n\to q\zeta\), \(B_n\to\beta\) in probability. The equality
\(\mathbb E[Zb(Z)]=q\mathbb E b'(Z)\) follows by Gaussian integration
by parts. Continuity in \(q_n\) follows by dominated convergence; all
required functions are bounded, including \(z b(z)\).

For a fixed tagged coordinate, the projection correction in (12) has
conditional variance \(h_i^2/(nq_n)\), which tends to zero in probability.
Thus on this coupling
\(R_i-[\zeta h_i+\sqrt\beta\gamma_i]\to0\) in probability.
This convergence also holds in mean square. To check uniform
integrability, write \(R_i=\sum_rX_r\), with
\(X_r=W_{ri}b(v_r)\). Conditionally on \(h\), these variables are
independent; their mean is \(O(1/n)\), second moment \(O(1/n)\), and
fourth moment \(O(1/n^2)\), using boundedness of \(b,b'\) and the
Gaussian moments of \(W_{ri}\). Expanding the fourth power of their
centered sum gives a bounded fourth moment for \(R_i\), uniformly in
\(n,h\). The coupled target in (11) also has a bounded fourth moment.
Truncation of the square at a fixed level now upgrades convergence in
probability to mean-square convergence.

The angular multiplier in (7) has modulus at most one. Hence this coupling
also gives
\(\mathbb E\sup_\theta|J_i(\theta)-J_*(\theta)|^2\to0\), with
the initial feature coupled identically. Any fixed finite number of tagged
neurons has the joint limit given by independent copies of (11): the
common empirical coefficients become deterministic and the projection
corrections vanish coordinatewise. No rate for a growing number of
neurons, harmonics, or derivative orders is asserted.

The limiting harmonic block Gram has the explicit entries

\[
 \begin{aligned}
 G^{00}_{kl}&=\delta_{kl}\lambda_k,\\
 G^{02}_{kl}&=\zeta\,\mathbb E[c_k(a)\overline{j_l(a)}\phi(a_1)],\\
 G^{22}_{kl}&=\mathbb E[j_k(a)\overline{j_l(a)}
                         (\beta+\zeta^2\phi(a_1)^2)].
 \end{aligned}
 \tag{13}
\]

These are two-dimensional Gaussian/angular integrals; the extra mark
\(\Gamma\) has been integrated out. The training direction breaks
rotational symmetry, so the last two blocks are not asserted diagonal.
All means remain zero by \((a,\Gamma)\mapsto(-a,-\Gamma)\).
Nevertheless the mixed block is nontrivial: at the training angle,

\[
 \mathbb E[h_a(0)J_*(0)]
 =\zeta\mathbb E[\phi(G)^2\phi'(G)^2]>0.
 \tag{14}
\]

Here \(\zeta>0\), since
\(q\zeta=\mathbb E[Z\phi(Z)\phi'(Z)]>0\). A centered independent
backward Gaussian would give zero in (14) and would omit the
\(\zeta^2\phi(a_1)^2\) term in (13).

## 6. What a law-based selection rule can actually use

For positive odd \(k\le L\), collect the real and imaginary parts of
\(c_k(a)\) and \(R_*j_k(a)\) into a real vector \(\Phi\in\mathbb R^D\),
where \(D=4\#\{1\le k\le L:k\text{ odd}\}\). Its full Gram
\(G=\mathbb E\Phi\Phi^T\) is determined by (13). Its coordinates
are jointly evaluable from (11). These two facts are separate inputs to
selection: knowing \(G\) alone would not reconstruct the source law.

For example, fix a ridge \(\eta>0\) and set

\[
 \ell(z)=\Phi(z)^T(G+\eta I)^{-1}\Phi(z),\quad
 Z=1+\operatorname{tr}[(G+\eta I)^{-1}G],\quad
 p(z)=\frac{1+\ell(z)}Z,
 \tag{15}
\]

where \(z=(a_1,a_2,\Gamma)\) has the standard three-Gaussian source
measure \(\nu\). The positive function \(p\) integrates to one.
Drawing from \(p\,d\nu\) and attaching weight \(1/p(z)\) gives the
exact importance identity

\[
 \mathbb E_{p\nu}\left[\frac{\Phi\Phi^T}{p}\right]=G.
 \tag{16}
\]

This is a law-defined selection and initialization of low-order source
marks, with no dense candidate pool. It is not yet initialization of a
small network with the full desired trained dynamics.

The selection distribution is evaluable, not merely existential. The
bounds \(|c_k|,|j_k|\le1\) imply
\(\ell(z)\le C_0D\eta^{-1}(1+\Gamma^2)\), with an absolute
constant \(C_0\). Use as proposal the same two standard Gaussians for
\(a\), but variance two for \(\Gamma\). The density ratio between
the target and this proposal is bounded by

\[
 (1+C_0D/\eta)\sqrt2(1+\Gamma^2)e^{-\Gamma^2/4}
 \le6(1+C_0D/\eta).
\]

Rejection sampling therefore has a finite expected number
\(O(1+D/\eta)\) of Gaussian proposals in exact real arithmetic.
It uses the explicit coefficient evaluations (1), (9), and (13), not an
unavailable trajectory. Numerical evaluation and stopping tolerances are
additional errors; no exact finite-bit sampler is claimed.

For \(P\) independent selected marks, let
\(\widehat G=P^{-1}\sum_{r=1}^P\Phi_r\Phi_r^T/p_r\). Write
\(B=(G+\eta I)^{-1/2}\). Then
\(\|B\Phi\Phi^TB/p\|_F=\ell/p\le Z\le D+1\).
Independence, the cancellation of centered cross terms, and
\((\ell/p)^2\le Z\ell/p\) give the concrete estimate

\[
 \mathbb E\|B(\widehat G-G)B\|_F^2
 \le\frac{Z\operatorname{tr}(BGB)}P
 \le\frac{D(D+1)}P.
 \tag{17}
\]

Markov's inequality yields an operator-norm error at most \(\varepsilon\)
with probability \(1-\delta\) when
\(P\ge D(D+1)/(\delta\varepsilon^2)\). This is a proved, conservative
moment-matrix guarantee. At accuracy \(n^{-1/2}\) its sample count is
not polylogarithmic; (17) is not presented as the final compact theorem.

For fixed \(L\), the matrix entries themselves admit finite quadrature
without neuron generation. Expand (13) as integrals over two Gaussian
coordinates and two angles. Gaussian truncation at
\(R=O(\sqrt{\log(1/\tau)})\) bounds the omitted mass by \(O(\tau)\).
On this four-dimensional box the integrand has first derivatives bounded
by \(C(L+R)\). A rectangular midpoint mesh with spacing
\(\tau/[C R^2(L+R)]\) has error \(O(\tau)\). Computing all entries
separately therefore has the explicit conservative arithmetic cost
\(O(D^2\tau^{-4}R^{10}(L+R)^4)\), with streamed quadrature and
\(O(D^2)\) stored matrix entries. The scalar constants in (13) use
one-dimensional Gaussian integrals. An additional ridge of the size of
the matrix error (at most \(D\) times the largest entry error) can absorb
that numerical error. These are source-computation costs, separate
from selection count and angular truncation.

One must not replace a nonlinear selection rule by the same rule applied
to averaged neurons or averaged weights. In particular,
\(\mathbb E\Phi=0\) does not determine \(G\), and in general
\(\mathbb E(G_n+\eta I)^{-1}\ne(\mathbb EG_n+\eta I)^{-1}\).
Even for a scalar equally likely to be one or two,
\(\mathbb E(1/X)=3/4\ne2/3=1/\mathbb EX\). Equations (15)--(17)
use a declared population Gram and the actual joint source marks; they
do not pretend to be the averaged weights of an empirical dense selector.

## 7. Exact finite-width Wick computation for polynomialized jets

There is also a finite-width answer to the computational question, provided
the polynomialization is stated. Replace tanh everywhere in the two-layer
network by a fixed polynomial \(P_D\) of degree \(D\), and use its
actual derivative in the gradient flow. This defines a different
polynomial network for the present lemma. No approximation of the tanh
dynamics follows without a separate error bound.

Fix a derivative order and finitely many harmonic/jet contractions.
At zero readout their coefficients are finite sums of Gaussian monomials,
with explicit powers of \(n^{-1/2}\), because every parameter derivative
uses the polynomial product and chain rules. Angular dependence is a
finite trigonometric polynomial, so its harmonic integral is an exact
constant-term extraction and may be done before or after expectation.

Here is an exact evaluator which never creates an \(n\)-row matrix.
Represent a summand by typed row and column index vertices; edges are
standard Gaussian variables \(G_{ij}=\sqrt nW_{ij}\), and the first-layer
Gaussian coordinates decorate column vertices. Suppose its normalization
is \(n^{-\gamma}\), its row/column vertex sets are \(R,C\), its
edge multiplicities are recorded explicitly, and the exponent of
first-layer coordinate \(\alpha\) at column vertex \(v\) is
\(p_{v\alpha}\). Define
\(m(0)=1\), \(m(2r)=(2r-1)!!\), and \(m(2r+1)=0\).

Enumerate set partitions \(\pi_R,\pi_C\) of the two vertex sets.
For partition blocks \(A,B\), let \(e_{AB}\) be the total number
of raw Gaussian matrix edges between them. Then the exact expectation is

\[
 n^{-\gamma}\sum_{\pi_R,\pi_C}
 (n)_{|\pi_R|}(n)_{|\pi_C|}
 \prod_{B\in\pi_C,\alpha}m\left(\sum_{v\in B}p_{v\alpha}\right)
 \prod_{A\in\pi_R,B\in\pi_C}m(e_{AB}),
 \tag{18}
\]

where \((n)_r=n(n-1)\cdots(n-r+1)\). Every labeling has exactly
one equality partition. Its blocks receive distinct labels in the two
populations, giving the two falling factorials. The remaining factors are
independent scalar Gaussians, giving their displayed moments. Gaussian
integration by parts proves \(m(2r)=(2r-1)m(2r-2)\), with vanishing
boundary term. This proves (18) at every finite \(n\), including widths
smaller than the number of abstract vertices.

The row and column partitions remain distinct even if their numerical
labels happen to coincide. Cross moments are obtained by disjoint union
of the abstract contractions before partitioning; this retains reuse and
all finite-width collision terms. For fixed tagged neuron labels, include
distinguished vertices, forbid merging distinct prescribed labels, and
replace \((n)_b\) by \((n-r)_{b-r}\) in a population with \(r\)
prescribed distinct labels. The same counting proof applies.

There is an honest, if potentially large, finite cost. Let a symbolic
expression contain \(T\) monomials, each with at most \(V\) abstract
index vertices and total Gaussian degree at most \(M\). At most
\(V^V\) pairs of typed partitions need be considered per monomial.
Each is evaluable in \(O(M+V^2+dV)\) arithmetic operations, apart from
the elementary falling-factorial and moment products. Streamed enumeration
uses \(O(M+V^2+dV)\) working indices, plus the stored output moments.
Gaussian integer moments have \(O(M\log(M+1))\) bits and the label
counts have \(O(V\log(n+1))\) bits. Input coefficient precision and
the number of summed terms add their usual arithmetic bit cost. Thus
there is no hidden \(n\times n\) initialization array, but exponential
dependence on symbolic order has not disappeared.

For scale, write \(B=D(D+1)\). The polynomial feature vector field has
parameter degree at most \(B\): direct degree counting in its readout,
middle-matrix, and first-matrix equations gives the same bound. Its
\(j\)-th Lie derivative of an observable of degree \(r\) has degree
at most \(r+j(B-1)\). The physical loss vector field has degree at
most \(2B+1\), so the corresponding bound is \(r+2jB\).
This follows inductively because differentiation lowers degree by one
and multiplication by the vector field raises it by at most its degree.
For fixed polynomial degree, Gaussian degree therefore grows at most
linearly in jet order, although monomial and partition counts can still
grow rapidly. Input harmonic degree is at most \(D\) for the first
hidden layer and \(D^2\) for the second hidden layer/output; parameter
differentiation does not raise the query input degree.

Formula (18) computes moments. It does not automatically sample the joint
finite-width law of the selected jets, nor provide expected nonlinear
selector weights, nor bound the error of polynomializing tanh. These
distinctions are already visible in the nontrivial exact low-order source
(11)--(14).

## Scope and internal checks

The positive conclusions are (3)--(6), (8)--(14), the law-based moment
selection identities (15)--(17), and the exact finite-width polynomial
evaluator (18). The first-layer harmonic tail is quantitative. The tagged
second-jet law is a fixed-order limit with a concrete jointly evaluable
source. The polynomial computation is exact at finite width but applies
to a stated polynomialized network.

Checks retained in the final source:

- Fourier normalization is \(1/(2\pi)\); \(c_k=t_ke^{-ik\alpha}\),
  and the covariance pairs \(c_k\) with \(\overline{c_l}\).
- Odd tanh removes even modes; every odd eigenvalue is strictly positive.
- The strip is bounded away from tanh's poles, and Gaussian tail/contour
  bounds are combined before summing modes.
- The second jet is an ordinary second derivative, not its Taylor
  coefficient; its physical-time factor is \(4y^2\).
- The same \(W\) appears forward and backward. Its response is retained
  in both the exact finite-width moments and the tagged Gaussian source.
- Angular and Gaussian operations are interchanged only under fixed-order
  integrable bounds. No high-order uniformity is inferred.
- Mean zero, diagonal initial covariance, joint source law, nonlinear
  selector weights, and finite-sample Gram accuracy remain separate claims.
- No old or unrelated study, experiment, Git operation, realized dense
  initialization, or response oracle was used. This internal author check
  is not independent review; the final source hash is reported separately.
