# A quartic-in-time theorem for the exact fifth step-doubling jet

Date: 25 August 2026.

## 1. Theorem

Fix a finite hidden depth \(L\ge1\).  Assume

\[
 \psi\in C^{12}(\mathbb R),\qquad
 \mathbb E\psi(G)^2=1,
 \qquad G\sim N(0,1),
 \tag{1.1}
\]

and

\[
 M_\psi=\max\left\{1,
 \sup_x\frac{|\psi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\psi^{(r)}\|_\infty
 \right\}<\infty.
 \tag{1.2}
\]

For every fixed integer \(N\) and fixed \(\eta\), take width to infinity
first and denote the resulting expected output by \(F_{N,L}(\eta)\).  Put

\[
 \Delta_{t,L}(\eta)=F_{2t,L}(\eta)-F_{t,L}(2\eta).
 \tag{1.3}
\]

The singular Price compiler, evaluated at the five fixed horizons
\(m=1,\ldots,5\), gives activation-defined Gaussian integrals

\[
 \mathcal J_{5,m,L}^{\mathrm{PJ}}(\psi).
 \tag{1.4}
\]

They are defined by the inverse-free Gaussian recursion before they are
identified with any output derivative.

Put

\[
 q_0=0,\qquad
 q_m=\frac{\mathcal J_{5,m,L}^{\mathrm{PJ}}(\psi)}{5!},
 \qquad1\le m\le5,
 \tag{1.4a}
\]

and define the forward differences

\[
 \Theta_{5,j}
 =\sum_{m=0}^{j}(-1)^{j-m}{j\choose m}q_m,
 \qquad1\le j\le5.
 \tag{1.4b}
\]

Let \(V\in\mathbb Q^{5\times5}\) be

\[
 V_{md}=m^d,
 \qquad 1\le m,d\le5,
 \tag{1.5}
\]

and define the five activation numbers

\[
 \gamma_{d,\psi,L}
 =\frac1{5!}\sum_{m=1}^5
 (V^{-1})_{dm}\mathcal J_{5,m,L}^{\mathrm{PJ}}(\psi).
 \tag{1.6}
\]

Then, for every integer \(N\ge0\),

\[
 \boxed{
 [\eta^5]F_{N,L}(\eta)
 =\sum_{d=1}^5\gamma_{d,\psi,L}N^d.}
 \tag{1.7}
\]

Consequently

\[
 \boxed{
 \beta_{t,\psi,L}:=[\eta^5]\Delta_{t,L}(\eta)
 =\sum_{j=1}^5d_{5,j}(t)\Theta_{5,j}
 =\sum_{d=1}^4(2^d-32)\gamma_{d,\psi,L}t^d,}
 \tag{1.8}
\]

where

\[
\begin{aligned}
d_{5,1}(t)&=-30t,\\
d_{5,2}(t)&=t(15-14t),\\
d_{5,3}(t)&=-2t(t-1)(2t-5),\\
d_{5,4}(t)&=\frac{t(t-1)}6(-4t^2+32t-45),\\
d_{5,5}(t)&=\frac{t(t-1)(t-2)}3(4t-9).
\end{aligned}
\tag{1.8a}
\]

so the fifth step-doubling coefficient is a polynomial of degree at most
four.  In particular, with

\[
 K_{\psi,L}
 :=\sum_{d=1}^4|2^d-32|\,|\gamma_{d,\psi,L}|,
 \tag{1.9}
\]

one has the activation-only bound

\[
 \boxed{
 |\beta_{t,\psi,L}|\le K_{\psi,L}t^4,
 \qquad t\ge1.}
 \tag{1.10}
\]

The sharper Newton-form constant

\[
 C^{\mathrm{loc}}_{\psi,L}
 =30|\Theta_{5,1}|+14|\Theta_{5,2}|+4|\Theta_{5,3}|
 +\frac23|\Theta_{5,4}|+\frac43|\Theta_{5,5}|
 \tag{1.10b}
\]

satisfies

\[
 \boxed{|\beta_{t,\psi,L}|
 \le C^{\mathrm{loc}}_{\psi,L}t^4.}
 \tag{1.10c}
\]

This power is sharp already at \(L=1\) for the identity activation: there

\[
 F_{N,1}(\eta)=\frac{(1+\eta)^{2N}-(1-\eta)^{2N}}2
\]

and hence

\[
 [\eta^5]\Delta_{t,1}(\eta)
 =\frac{64}{3}t^4-56t^3+\frac{140}{3}t^2-12t.
 \tag{1.10d}
\]

The target depth \(L=2\) also has a nonzero quartic identity control,

\[
 [\eta^5]\Delta_{t,2}(\eta)
 =\frac{2452}{3}t^4-1896t^3
 +\frac{4403}{3}t^2-369t.
 \tag{1.10e}
\]

There is also a completely explicit envelope.  Let

\[
 B_\psi=\max\{4,M_\psi\},
 \tag{1.11}
\]

and let \(E_{L,5}\) be the terminating integer in Section 5.  Then

\[
 \boxed{
 C^{\mathrm{loc}}_{\psi,L}
 \le\frac{227}{180}B_\psi^{E_{L,5}},}
 \tag{1.12}
\]

and equivalently

\[
 \boxed{
 |\Delta_{t,L}^{(5)}(0)|
 \le\frac{454}{3}B_\psi^{E_{L,5}}t^4.}
 \tag{1.13}
\]

The exact constants in (1.4b), (1.6), (1.9), and (1.10b) use only Gaussian
activation integrals, the fixed depth, and explicit integer arithmetic.
The coarse bound (1.12) instead uses the stated weighted activation
envelope.  None contains an output supremum, trained trajectory, response
modulus, or continuity radius.

## 2. The generated-core fifth-order Euler germ

The fixed-step adaptive-conditioning theorem first identifies the actual
finite-width network with the inverse-free Gaussian DAG pointwise for every
fixed nonzero common step, after taking width to infinity.  At zero both
expected outputs are zero, so the identification holds there as
well.  Only this already width-limited function is differentiated below;
no finite-width derivative or interchange of \(n\to\infty\) with
\(\eta\to0\) is used.

The exact temporal width-limit DAG is, at every fixed step schedule, the
simultaneous population Euler construction

\[
 \theta_{s+1}=\theta_s+\varepsilon_s\,\mathbf g(\theta_s)
 \tag{2.1}
\]

on the fixed population parameter space

\[
 \mathcal P_L
 =\mathcal H_L\oplus
 \bigoplus_{a=2}^L\operatorname{HS}(\mathcal H_{a-1},\mathcal H_a)
 \oplus\mathcal H_1.
 \tag{2.2}
\]

Here \(\theta_0=(A,0,\ldots,0,U)\); the zero connector coordinates are
the trainable Hilbert--Schmidt increments, while the initialization
connectors below are fixed external bounded operators.

Each initialization connector is one fixed bounded operator

\[
 W_{a,0}=I_a+J_a^*,
 \qquad W_{a,0}^*=I_a^*+J_a,
 \tag{2.3}
\]

and learned increments are Hilbert--Schmidt.  For a cylindrical query

\[
 X=\Phi(J_ac_1,\ldots,J_ac_q,\zeta),
\]

the intrinsic adjoint identity is

\[
 J_a^*X=\sum_{i=1}^q
 \mathbb E[\partial_i\Phi]\,c_i,
 \tag{2.4}
\]

with the analogous formula for \(I_a^*\).  The aggregate vector is formed
before a norm is taken, so (2.4) remains valid at singular Grams.

### Lemma 2.1 (common generated \(C^5\) germ)

For every fixed finite \((L,N)\), the fixed-space construction (2.1)--(2.4)
has all mixed scalar derivatives through total order five along the finite
family of elementary Euler directions of order at most five.  They commute,
belong to every finite \(L^p\), and agree node by node with the derivatives
of the inverse-free temporal Gaussian DAG at the coalesced step vector.

#### Proof

Fix independent step coordinates
\(\varepsilon_0,\ldots,\varepsilon_{N-1}\), put
\(\mathfrak m=(\varepsilon_0,\ldots,\varepsilon_{N-1})\), and perform the
complete chronological construction in the finite algebra

\[
 \mathscr A_5
 =\mathbb R[\varepsilon_0,\ldots,\varepsilon_{N-1}]/\mathfrak m^6.
 \tag{2.5}
\]

Equivalently, for every field \(X\), retain
\(X^{[\alpha]}=\partial_\varepsilon^\alpha X(0)\) for
\(|\alpha|\le5\).  Product and update nodes use the finite multiindex
Leibniz rule.  Activation nodes use the finite multiset-partition identity

\[
 (\psi(Z))^{[\alpha]}
 =\sum_{\pi\in\Pi(\alpha)}
 \psi^{(|\pi|)}(Z^{[0]})
 \prod_{B\in\pi}Z^{[\nu(B)]}.
 \tag{2.6}
\]

It remains to check that reused adjoints do not lose source terms.  At any
fixed chronology node write the current moving query as

\[
 X(\varepsilon)=
 \Phi\!\left(\varepsilon;
 J_ac_1(\varepsilon),\ldots,J_ac_q(\varepsilon),
 \zeta(\varepsilon)\right),
\]

where \(\zeta\) is independent of the allocated \(J_a\)-source block, and
put \(\rho_i(\varepsilon)=\mathbb E[\partial_i\Phi]\).  Identity (2.4)
holds for every value of \(\varepsilon\), not just at the origin.  Therefore
its complete marked derivative is

\[
 (J_a^*X)^{[\alpha]}
 =\sum_{i=1}^q\sum_{\beta\le\alpha}
 {\alpha\choose\beta}
 \rho_i^{[\alpha-\beta]}c_i^{[\beta]}.
 \tag{2.7}
\]

The symmetric formula holds for \(I_a^*\).  Formula (2.7) explicitly
contains every derivative of the moving source \(c_i\); iterating it is the
complete source-response convolution, so no separate finite-list or
source-order assumption is being made.

We now induct lexicographically over the finite temporal/layer chronology
and the finite set \(\{|\alpha|\le5\}\).  Gaussian endpoint fields start in
every finite \(L^p\).  The induction closes because:

1. raw actions commute with the scalar derivatives and satisfy
   \[
    \|I_ax\|_p=\|G\|_p\|x\|_2,
    \qquad
    \|J_ac\|_p=\|G\|_p\|c\|_2;
   \]
2. (2.7), Leibniz, and Hölder reduce an adjoint derivative to a finite sum
   of earlier all-moment fields and scalar expectations;
3. learned actions are finite sums of rank-one maps and
   \(\|y\otimes x\|_{\mathrm{HS}}=\|y\|_2\|x\|_2\);
4. (2.6), bounded derivatives, and the linear-growth bound preserve every
   finite moment.

For response and Gram expectations at a singular source covariance, use
the following already proved singular-Price argument.  Replace a covariance
\(C(\varepsilon)\) by \(C(\varepsilon)+\delta I\), apply the ordinary Price
identity at \(\delta>0\), and couple the regularized and singular Gaussians
by their positive-semidefinite square roots.  The square-root difference is
at most \(\sqrt\delta\); truncation of the common standard Gaussian followed
by the polynomial dominators above permits \(\delta\downarrow0\) in every
mixed derivative through order five.  A response begins with one spatial
derivative and five Price operations add at most ten more, so the largest
activation derivative requested is \(\psi^{(12)}\), exactly covered by
(1.2).

There are finitely many chronology nodes, finitely many multiindices in
(2.5), and finitely many terms in (2.6)--(2.7); hence the construction
terminates.  Taylor's integral formula and the same dominators show that
these marked coefficients are actual commuting mixed derivatives in every
finite \(L^p\), rather than formal symbols.

Finally, (2.3)--(2.4) and their transpose analogues identify, node by node
and at every fixed step vector, the fixed-operator construction with the
inverse-free temporal Gaussian DAG.  Thus their marked derivatives agree.
\(\square\)

Lemma 2.1 is a fixed-schedule statement after the width limit.  It neither
uses a finite-width Taylor expansion nor asserts a norm uniform in \(N\).

For the rest of the proof, write \(\mathbf G_k[v_1,\ldots,v_k]\) and
\(\mathcal T_k[v_1,\ldots,v_k]\) for the generated mixed tensors of
\(\mathbf g\) and \(\mathcal F\) furnished by Lemma 2.1.  These symbols are
defined only on the finite all-moment family generated recursively below;
they do **not** assert ambient Fréchet differentiability on an open
\(L^2\)-ball.  Put \(\mathbf G_0=\mathbf g(\theta_0)\).

## 3. Universal fifth-order time polynomial

Put \(g=\mathbf G_0\).  Let \(Y_r(N)\) be the coefficient of
\(\eta^r\) in the population Euler state after \(N\) equal steps:

\[
 \theta_N(\eta)=\theta_0+
 \sum_{r=1}^5\eta^rY_r(N)+o(\eta^5).
 \tag{3.1}
\]

The following is a finite recursive definition.  Set

\[
 Y_r(0)=0,
 \qquad Y_1(N)=Ng.
 \tag{3.2}
\]

For \(r=2,\ldots,5\), define

\[
 Y_r(N)=\sum_{s=0}^{N-1}
 \sum_{k=1}^{r-1}\frac1{k!}
 \sum_{\substack{j_1+\cdots+j_k=r-1\\j_i\ge1}}
 \mathbf G_k
 [Y_{j_1}(s),\ldots,Y_{j_k}(s)].
 \tag{3.3}
\]

Every sum is finite and uses only \(Y_j\) with \(j<r\), so the recursion
terminates.  It is exactly coefficient extraction in (2.1): the increment
has one external factor \(\eta\), and the inner sums are the Taylor
coefficients of \(\mathbf g\).

By induction, \(Y_r(N)\) is a vector-valued polynomial in \(N\) of degree at
most \(r\).  Indeed, each summand in (3.3) has degree at most
\(j_1+\cdots+j_k=r-1\) in \(s\), and summation from \(s=0\) to \(N-1\)
raises polynomial degree by at most one.

Let \(\mathcal F\) be the population output.  Its fifth coefficient is

\[
 A_5(N):=[\eta^5]F_{N,L}(\eta)
 =\sum_{k=1}^{5}\frac1{k!}
 \sum_{\substack{j_1+\cdots+j_k=5\\j_i\ge1}}
 \mathcal T_k
 [Y_{j_1}(N),\ldots,Y_{j_k}(N)].
 \tag{3.4}
\]

Thus \(A_5(N)\) is a scalar polynomial of degree at most five and
\(A_5(0)=0\).  This proof uses only the generated tensors supplied by
Lemma 2.1; global Fréchet \(C^5\) smoothness on an \(L^2\) ball is not
assumed.

The same coefficient extraction proves the underlying general pattern.  For
each \(1\le r\le5\), there are activation/depth numbers
\(\Theta_{r,1},\ldots,\Theta_{r,r}\) such that

\[
 [\eta^r]F_{N,L}(\eta)
 =\sum_{j=1}^r{N\choose j}\Theta_{r,j}.
 \tag{3.5}
\]

Consequently

\[
 [\eta^r]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}
 =\sum_{j=1}^r
 \left\{{2t\choose j}-2^r{t\choose j}\right\}\Theta_{r,j}
 \tag{3.6}
\]

has degree at most \(r-1\) in \(t\).  Indeed, the degree-\(r\) terms from
the two meshes cancel.  The fifth-order theorem is the case \(r=5\), with
the constants made noncircular and quantitative in Sections 4--5.

## 4. Activation-integral identification and quartic cancellation

The singular Price compiler proves, independently of Section 3, that the
already width-limited output is \(C^5\) at the singular covariance and

\[
 F_{m,L}^{(5)}(0)
 =\mathcal J_{5,m,L}^{\mathrm{PJ}}(\psi),
 \qquad 1\le m\le5.
 \tag{4.1}
\]

By uniqueness of derivatives, (3.4) and (4.1) compute the same numbers.
Since \(A_5\) has degree at most five and zero constant term, its values at
\(m=1,\ldots,5\) determine it.  The inverse Vandermonde formula is exactly
(1.6), proving (1.7).

The same interpolation in the Newton basis gives

\[
 A_5(N)=\sum_{j=1}^5{N\choose j}\Theta_{5,j}.
 \tag{4.1a}
\]

Indeed, (1.4b) is the ordinary forward-difference formula and Newton
interpolation is exact for every polynomial of degree at most five.  Hence

\[
 \beta_{t,\psi,L}
 =\sum_{j=1}^5
 \left\{{2t\choose j}-32{t\choose j}\right\}\Theta_{5,j}.
 \tag{4.1b}
\]

Expanding the five bracketed polynomials gives exactly (1.8a).

For reference,

\[
V^{-1}=
\begin{pmatrix}
5&-5&10/3&-5/4&1/5\\
-77/12&107/12&-13/2&61/24&-5/12\\
71/24&-59/12&49/12&-41/24&7/24\\
-7/12&13/12&-1&11/24&-1/12\\
1/24&-1/12&1/12&-1/24&1/120
\end{pmatrix}.
 \tag{4.2}
\]

Substitute (1.7) into (1.3).  The degree-five term cancels because
\(2^5-32=0\), giving (1.8).  The triangle inequality and \(t^d\le t^4\)
for \(1\le d\le4\), \(t\ge1\), give (1.9)--(1.10).

Directly from (1.8a), for every integer \(t\ge1\),

\[
 \frac{|d_{5,j}(t)|}{t^4}
 \le 30,\ 14,\ 4,\ \frac23,\ \frac43
 \quad(j=1,\ldots,5).
 \tag{4.3}
\]

For \(j=4\), check \(t=1,\ldots,6\) directly and use
\(|-4t^2+32t-45|\le4t^2\) for \(t\ge7\); the other four estimates follow
immediately from their factorizations.  Equation (4.3) proves
(1.10b)--(1.10c).

This cancellation is universal: it is the order-five consistency
cancellation between one Euler mesh and its dyadic refinement, not a special
property of the identity activation.

## 5. A closed activation-envelope constant

This section spells out the integer \(E_{L,5}\).  Put \(D=12\) and define

\[
 R_0=1,
 \qquad R_{k+1}=112(R_k+1),
 \qquad 0\le k<48,
 \tag{5.1}
\]

\[
 c_0=4(R_{48}+1),
 \qquad
 c_{q+1}=64\,13^{10}(c_q+1)^2,
 \qquad0\le q<24,
 \tag{5.2}
\]

and set \(C=c_{24}\).  For

\[
 \mu_{D,p}(w)
 =\sum_{q=0}^p{p\choose q}w^{q/2}2^{q/2}
 \frac{\Gamma((D+q)/2)}{\Gamma(D/2)},
 \tag{5.3}
\]

put

\[
 \nu=\mu_{12,C}(169),
 \qquad
 a=\left\lceil\log_2(2^C\nu)\right\rceil,
 \qquad p=2C,
 \qquad r=C+a.
 \tag{5.4}
\]

Finally let

\[
 M_{L,5}=\begin{cases}11(L-1),&L\ge2,\\1,&L=1,
 \end{cases}
 \tag{5.5}
\]

and

\[
 \boxed{
 E_{L,5}=2L\,p^{M_{L,5}}
 +r\frac{p^{M_{L,5}}-1}{p-1}.}
 \tag{5.6}
\]

The recursion has 48 assignments in (5.1), 24 in (5.2), and finitely many
terms in (5.3), so it terminates.  The audited Price envelope gives

\[
 |\mathcal J_{5,m,L}^{\mathrm{PJ}}(\psi)|
 \le B_\psi^{E_{L,m}}
 \le B_\psi^{E_{L,5}},
 \qquad1\le m\le5.
 \tag{5.7}
\]

The rowwise \(\ell^1\) norms of the first four rows of (4.2) are

\[
 \frac{887}{60},\qquad
 \frac{595}{24},\qquad
 \frac{335}{24},\qquad
 \frac{77}{24}.
 \tag{5.8}
\]

Therefore

\[
 \sum_{d=1}^4|2^d-32|
 \sum_{m=1}^5|(V^{-1})_{dm}|
 =1524.
 \tag{5.9}
\]

Equations (1.6), (1.9), and (5.7)--(5.9) prove

\[
 K_{\psi,L}\le\frac{1524}{120}B_\psi^{E_{L,5}}
 =\frac{127}{10}B_\psi^{E_{L,5}},
\]

which is a valid monomial-basis envelope.  The Newton basis is sharper.
Since \(q_0=0\), (1.4b) and (5.7) give

\[
 |\Theta_{5,j}|
 \le\frac{2^j-1}{120}B_\psi^{E_{L,5}}.
 \tag{5.10}
\]

Substitution in (1.10b) yields

\[
 \begin{aligned}
 C^{\mathrm{loc}}_{\psi,L}
 &\le\frac1{120}
 \left\{30+14\cdot3+4\cdot7
 +\frac23\cdot15+\frac43\cdot31\right\}
 B_\psi^{E_{L,5}}\\
 &=\frac{227}{180}B_\psi^{E_{L,5}}.
 \end{aligned}
 \tag{5.11}
\]

This is (1.12).  Multiplication by \(5!=120\) gives (1.13).

## 6. A genuine nonlinear class at depths two and three

Let

\[
 \varphi\in C^{12}(\mathbb R),
 \qquad
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R,
 \qquad
 \varphi''\not\equiv0,
 \tag{6.1}
\]

and define

\[
 s_\alpha=\|G+\alpha\varphi(G)\|_2,
 \qquad
 \psi_{\alpha,\varphi}(x)
 =\frac{x+\alpha\varphi(x)}{s_\alpha}.
 \tag{6.2}
\]

If

\[
 0<|\alpha|R\le\frac14,
 \tag{6.3}
\]

then \(3/4\le s_\alpha\le5/4\), the activation is genuinely nonlinear,
and

\[
 \sup_x\frac{|\psi_{\alpha,\varphi}(x)|}{1+|x|}\le\frac43,
 \qquad
 \|\psi_{\alpha,\varphi}'\|_\infty\le\frac53,
 \qquad
 \max_{2\le r\le12}
 \|\psi_{\alpha,\varphi}^{(r)}\|_\infty\le\frac13.
 \tag{6.4}
\]

Hence \(M_{\psi_{\alpha,\varphi}}\le5/3\) and
\(B_{\psi_{\alpha,\varphi}}=4\).  Theorem 1 therefore gives, simultaneously
for this entire genuine nonlinear class,

\[
 \boxed{
 |[\eta^5]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}|
 \le\frac{227}{180}\,4^{E_{L,5}}t^4.}
 \tag{6.5}
\]

At \(L=2\) and \(L=3\), respectively,

\[
 E_{2,5}=4p^{11}+r\frac{p^{11}-1}{p-1},
 \qquad
 E_{3,5}=6p^{22}+r\frac{p^{22}-1}{p-1},
 \tag{6.6}
\]

with the same numerical integers \((p,r)\) from (5.4).  Thus the depth and
activation dependencies are completely explicit.

Combining this with oddness and the already proved cubic coefficient gives
the width-first local expansion

\[
 F_{2t,L}(\eta)-F_{t,L}(2\eta)
 =\kappa_{\psi,L,t}\eta^3
  +\beta_{t,\psi,L}\eta^5+o_t(\eta^5),
 \tag{6.7}
\]

where \(\kappa_{\psi,L,t}=t(2t-1)J_{\psi,L}/2\) and
\(|\beta_{t,\psi,L}|\le(227/180)4^{E_{L,5}}t^4\).

## 7. Exact boundary of the result

The theorem is a positive polynomial-in-time result for the exact fifth
Taylor coefficient of the already width-limited output.  At the **jet
level**, it improves the requested polynomial target from \(O(t^5)\) to
the sharp universal power \(O(t^4)\).

It does **not** prove the uniform nonzero-step remainder

\[
 \sup_{0<|\eta|\le\rho/t}
 \frac{|\Delta_{t,L}(\eta)
 -\kappa_{\psi,L,t}\eta^3|}{|\eta|^5}
 \le C_{\psi,L}t^4.
 \tag{7.1}
\]

The Peano remainder in (6.7) may still depend on \(t\).  Thus this theorem
must not be read as the uniform finite-step remainder estimate requested in
earlier rungs of the project.  Passing from the jet theorem to (7.1) is
exactly where the all-source aggregate-adjoint factorial-contraction problem
from the near-identity audit remains open.

No finite-width Taylor expansion is used here: width is taken first at each
fixed step, the fixed-h Gaussian DAG is identified with the fixed-operator
population Euler map, and only that width-first map is differentiated.
