# General polynomial frozen subsystem: exact top order and obstruction

## Setup

Let

\[
 \phi(x)=\sum_{k=0}^dc_kx^k,
 \qquad d\ge2,qquad c_d>0,qquad
 \mathbb E\phi(G)^2=1.
\]

The RMS normalization plays no role below except to fix the common scale.
Consider the frozen two-dimensional Euler recursion

\[
\begin{aligned}
A_{n+1}&=A_n+h\phi(Z_n),\\
Z_{n+1}&=Z_n+hA_n\phi'(Z_n),
\end{aligned}                                                     \tag{1}
\]

with independent \(A_0,Z_0\sim N(0,1)\), and observable

\[
 O_n=A_n\phi(Z_n).
\]

Write

\[
 D_t(h)=\mathbb EO_{2t}(h)-\mathbb EO_t(2h).
\]

The question is whether the single monomial obtained by choosing only the
top activation terms \(c_dx^d\) and \(dc_dx^{d-1}\) can yield an all-order
lower bound at \(h=\rho/t\) when the lower \(c_k\)'s have arbitrary signs.

## 1. Exact maximal step degree

Let \(\delta_n\) denote the largest \(h\)-degree of either state coordinate.
Since both coordinates start in degree zero and the two nonlinear update
terms have maximal degrees

\[
 1+d\delta_n,qquad
 1+\delta_n+(d-1)\delta_n,
\]

one has

\[
 \delta_0=0,qquad
 \delta_{n+1}=1+d\delta_n,qquad
 \boxed{\delta_n=\frac{d^n-1}{d-1}.}               \tag{2}
\]

The maximal output degree is therefore

\[
 \boxed{m_n=(d+1)\delta_n
 =\frac{d+1}{d-1}(d^n-1).}                         \tag{3}
\]

The coefficient at this order is more informative than a single pure
monomial.  Put

\[
 a_n=[h^{\delta_n}]A_n,qquad
 z_n=[h^{\delta_n}]Z_n.
\]

At the first step,

\[
 a_1=\phi(Z_0),qquad z_1=A_0\phi'(Z_0).           \tag{4}
\]

For every \(n\ge1\), only the top outer monomials can attain the next
maximal \(h\)-degree, so

\[
 a_{n+1}=c_dz_n^d,qquad
 z_{n+1}=dc_da_nz_n^{d-1}.                         \tag{5}
\]

Finally,

\[
 [h^{m_n}]O_n=c_da_nz_n^d.                         \tag{6}
\]

Track only the exponents of \((a_1,z_1)\).  One application of (5) sends

\[
 (A,Z)\longmapsto(dZ,A+(d-1)Z).
\]

The output uses the exponent row \(\ell=(1,d)\), and

\[
 \ell
 \begin{pmatrix}0&d\\1&d-1\end{pmatrix}
 =d\ell.                                           \tag{7}
\]

Consequently there is an explicit constant \(C_{d,n}>0\), made only of
powers of \(c_d\) and \(d\), such that

\[
 \boxed{
 [h^{m_n}]O_n
 =C_{d,n}\,phi(Z_0)^{d^{n-1}}
  \{A_0\phi'(Z_0)\}^{d^n}.}                       \tag{8}
\]

This identity includes **all** mixed lower-coefficient choices which occur
at maximal \(h\)-order.  The pure top-degree monomial is only one term in
its expansion.

Taking expectation and using independence gives

\[
 \boxed{
 [h^{m_n}]\mathbb EO_n
 =C_{d,n}\,\mathbb EA_0^{d^n}\,
 \mathbb E\!left[
   \phi(G)^{d^{n-1}}\phi'(G)^{d^n}
 \right].}                                        \tag{9}
\]

## 2. Exact parity dichotomy

There is also an activation-independent step-size parity.  With

\[
 S(A,Z)=(-A,Z),
\]

the observable obeys \(O(Sx)=-O(x)\), while its gradient vector field
obeys \(g(Sx)=-Sg(x)\).  Hence

\[
 E_{-h}(Sx)=S E_h(x).
\]

The initialization law is \(S\)-invariant, so

\[
 \mathbb EO_n(-h)=-\mathbb EO_n(h).                 \tag{9a}
\]

Thus every even \(h\)-coefficient vanishes.  This independently checks the
degree parity below: when \(d\) is even, \(m_n\) is odd; when \(d\) is odd,
\(m_n\) is even.

### Even \(d\)

If \(d\) is even, both exponents in the last expectation in (9), as well as
the exponent of \(A_0\), are even.  Therefore

\[
 [h^{m_n}]\mathbb EO_n>0                           \tag{10}
\]

for every \(n\ge1\), independently of every lower-coefficient sign.  The
integrand is pointwise nonnegative and is not almost surely zero.

Since \(m_t<m_{2t}\), the coarse polynomial \(\mathbb EO_t(2h)\) has no
term of degree \(m_{2t}\).  Hence

\[
 [h^{m_{2t}}]D_t(h)=[h^{m_{2t}}]\mathbb EO_{2t}(h)>0.             \tag{11}
\]

This is an exact positive *coefficient* statement.  It is not yet a
pointwise lower bound at \(h=\rho/t\).

### Odd \(d\)

If \(d\) is odd, then \(d^n\) is odd.  The independent readout-source factor
in (9) vanishes:

\[
 \mathbb EA_0^{d^n}=0.
\]

Thus

\[
 \boxed{[h^{m_n}]\mathbb EO_n=0\quad(d\text{ odd}).}             \tag{12}
\]

This kills the entire maximal-order coefficient, not merely the selected
pure monomial.  Any odd-degree no-go proof must identify and control a lower
\(h\)-order parity-repaired family.  The even-degree argument cannot be
ported verbatim.

## 3. The pure top monomial does not dominate mixed branches

Even in the favorable even-degree case, the single pure monomial need not
be the principal part of (9).  This failure is quantitative.

Fix \(a\ne0\) and take the RMS-normalized shifted power

\[
 \phi_a(x)=s_a(x+a)^d,
 \qquad
 s_a=\left(\mathbb E(G+a)^{2d}\right)^{-1/2}>0.     \tag{13}
\]

It has degree \(d\) and positive leading coefficient.  In (9), put

\[
 r=d^{n-1},\qquad s=d^n.
\]

Then

\[
 \phi_a(G)^r\phi_a'(G)^s
 =s_a^{r+s}d^s(G+a)^K,
 \qquad K=dr+(d-1)s=d^{n+1}.                       \tag{14}
\]

For even \(d\), \(K\) is even.  The pure top monomial contributes
\(\mathbb EG^K\).  The full mixed expansion satisfies

\[
\begin{aligned}
\mathbb E(G+a)^K
&=\sum_{j\ {m even}}{K\choose j}a^{K-j}\mathbb EG^j\\
&\ge \mathbb EG^K+{K\choose2}a^2\mathbb EG^{K-2}\\
&=\mathbb EG^K\left(1+\frac{Ka^2}{2}\right),       \tag{15}
\end{aligned}
\]

because \(\mathbb EG^K=(K-1)\mathbb EG^{K-2}\).  Therefore

\[
 \frac{\text{pure top-monomial contribution}}
      {\text{complete maximal-order coefficient}}
 \le\frac1{1+Ka^2/2}\longrightarrow0.             \tag{16}
\]

A single mixed term already exceeds the pure term by a factor asymptotic to
\(Ka^2/2\).  The coefficient-count growth cannot be discarded.  This is a
counterexample to literal pure-branch domination with a perfectly regular,
RMS-normalized polynomial activation.  Choosing \(a<0\) also supplies
alternating lower coefficients when appropriate; (15) is unchanged because
only even Gaussian powers survive.

## 4. Why a positive top coefficient does not prove the finite-step bound

For the quadratic positive-coefficient class, coefficientwise positivity
gave

\[
 D_t(h)\ge [h^{m_{2t}}]D_t\,h^{m_{2t}}qquad(h>0).
\]

With arbitrary lower signs this implication is unavailable.  Gaussian
expectation preserves the sign of a coefficient; it does not turn a signed
coefficient polynomial into a positive one.  Formula (11) only controls the
largest power of \(h\), whereas the desired evaluation uses
\(h=\rho/t\to0\).

The logical gap cannot be repaired by leading-coefficient positivity alone.
For example, polynomials

\[
 P_t(h)=L_th^{M_t}-2L_t\frac\rho t h^{M_t-1},
 \qquad L_t>0,
\]

have positive leading coefficient but

\[
 P_t(\rho/t)=-L_t(\rho/t)^{M_t}<0.
\]

This example is not claimed to be a network output; it identifies the exact
missing estimate: one needs a structural bound on the complete signed lower
coefficient ledger, not merely the maximal branch.

The shifted-power calculation shows why a naive attempt to obtain that bound
by comparing every mixed branch to the pure branch also fails.  Mixed terms
can overwhelm the pure term already inside the one coefficient whose total
sign is protected by even powers.

## 5. Audited conclusion

The rigorous general statement currently available is:

\[
\begin{array}{c|c|c}
&d\text{ even}&d\text{ odd}\\ \hline
\text{maximal state degree}&\delta_n=(d^n-1)/(d-1)&\text{same}\\
\text{maximal output degree}&m_n=(d+1)\delta_n&\text{same}\\
\text{expected maximal coefficient}&>0&=0\\
\text{pure monomial dominates mixed terms?}&\text{no in general}&\text{no; it vanishes}\\
\text{pointwise }D_t(\rho/t)\text{ lower bound}&\text{not proved}&\text{not proved}
\end{array}
\]

Thus the quadratic no-go theorem extends immediately neither to arbitrary
signed even-degree polynomials nor to odd degree by a pure-top-branch
argument.  For even degree, a viable next route would need a signed
Laplace/large-deviation analysis of the **complete** scalar recursion.  For
odd degree, it must first identify the highest parity-surviving family.  Any
claim of a general polynomial uniform-tail obstruction without one of those
additional arguments remains open.

## 6. A complete scalar no-go for every pure monomial degree

Although arbitrary signed lower coefficients remain unresolved, odd degree
is not itself a counterexample.  Let

\[
 \phi(x)=c x^d,
 \qquad c=(\mathbb EG^{2d})^{-1/2}>0.               \tag{17}
\]

All formal coefficients of the scalar vector field and observable are
nonnegative.  Hence the positive-polynomial step-doubling lemma applies, and
Gaussian expectation preserves its coefficientwise order.

Put

\[
 s=d^N,qquad m_N=\frac{d+1}{d-1}(s-1).
\]

If \(d\) is even, the maximal branch contains

\[
 [h^{m_N}]\mathbb EO_N
 \ge c^{m_N+1}\mathbb EG^{s}\mathbb EG^{ds}.        \tag{18}
\]

The omitted integer powers of \(d\) are at least one.  At \(N=2t\), both
moments survive, the coarse degree is smaller, and coefficientwise
positivity gives

\[
 D_t(\rho/t)
 \ge c^{m_{2t}+1}(\rho/t)^{m_{2t}}
       \mathbb EG^{d^{2t}}\mathbb EG^{d^{2t+1}}.    \tag{19}
\]

This tends to \(+\infty\) by the Gaussian factorial estimate.

For odd \(d\), the degree-\(m_N\) expectation vanishes, but an exact
degree-\(m_N-1\) branch survives.  Regard the maximal terminal monomial as
a positive constant times

\[
 a_1^r z_1^s,
 \qquad r=d^{N-1},\quad s=d^N,
\]

where the first Euler step is

\[
 A_1=A_0+hcZ_0^d,qquad
 Z_1=Z_0+hdcA_0Z_0^{d-1}.                           \tag{20}
\]

Choose the old \(A_0\) term in exactly one of the \(r\) copies of \(A_1\),
and choose the update term in every other first-step factor and every later
factor.  This removes exactly one power of \(h\) and one power of \(c\).
The resulting raw exponents are

\[
 A_0^{s+1}Z_0^{d(r-1)+(d-1)s}
 =A_0^{s+1}Z_0^{d(s-1)}.                            \tag{21}
\]

Because \(d\) and \(s\) are odd, both exponents in (21) are even.  Its
coefficient is positive.  Therefore

\[
 [h^{m_N-1}]\mathbb EO_N
 \ge c^{m_N}\mathbb EG^{s+1}\mathbb EG^{d(s-1)}.   \tag{22}
\]

Again the omitted integer factor is at least one.  At \(N=2t\), the coarse
degree is below \(m_{2t}-1\), so

\[
 D_t(\rho/t)
 \ge c^{m_{2t}}(\rho/t)^{m_{2t}-1}
       \mathbb EG^{d^{2t}+1}
       \mathbb EG^{d(d^{2t}-1)}.                   \tag{23}
\]

Let \(K=d(d^{2t}-1)\), which is even.  Then

\[
 \mathbb EG^K\ge\left(\frac{K}{2e}\right)^{K/2}.
\]

Writing \(s=d^{2t}\), the logarithm of the right side of (23), divided by
\(s\), is bounded below by

\[
 d\,t\log d-\frac{d+1}{d-1}\log t
 +O_{c,d,\rho}(1),
\]

which tends to \(+\infty\).  Thus

\[
 \boxed{D_t(\rho/t)\to+\infty
 \quad\text{for every pure monomial degree }d\ge2.}              \tag{24}
\]

This proves that neither odd monomials nor their parity cancellation at the
absolute top degree furnish a counterexample.  It does not restore the
argument for a general signed polynomial: lower activation monomials destroy
coefficientwise positivity and can enter the same near-maximal orders as the
branch in (21).

The same proof actually covers every polynomial with

\[
 c_0,\ldots,c_d\ge0,qquad c_d>0.                   \tag{24a}
\]

Indeed, the scalar vector field and observable are then coefficientwise
positive.  For even \(d\), retain the pure \(c_dx^d\) maximal branch in
(18).  For odd \(d\), retain the same one-old-factor branch in (21)--(23).
Every omitted activation branch only adds nonnegative coefficients before
and after Gaussian expectation.  Replacing \(c\) by \(c_d\) in the lower
bounds proves

\[
 D_t(\rho/t)\to+infty
 \quad\text{whenever all activation coefficients are nonnegative}.       \tag{24b}
\]

For this coefficientwise-positive class the conclusion transfers to the
actual two-hidden-layer network.  Every coordinate of the finite-width
ascent field and its output is a positive polynomial in the raw variables.
Deleting the bottom \(u\)-update is therefore monotone by the exact paired
step-doubling lemma, so

\[
 \Delta_t^{\rm full}(h)\ge D_t(h),qquad h\ge0.      \tag{24c}
\]

The fixed-program NETSOR\({}^\top+\)Moment bridge used for the quadratic
case applies verbatim to every fixed finite-degree polynomial: the program
is still finite and all coordinate maps are polynomially smooth.  Hence the
width-first passage in (24c) is justified at every fixed \((t,h)\).  It
follows that the complete \(L=2\) uniform remainder fails for every
normalized polynomial satisfying (24a), at every fixed degree \(d\ge2\).

This full-network transfer is precisely what is lost for arbitrary signed
coefficients: deletion of the bottom update is then not coefficientwise
monotone.

## 7. Shifted powers, including alternating coefficients, are not counterexamples

The monomial result extends to every normalized shifted power

\[
 \phi(x)=c(x+a)^d,
 \qquad c=\left(\mathbb E(G+a)^{2d}\right)^{-1/2}>0.              \tag{25}
\]

Put \(Y=Z+a\).  Then the scalar recursion and observable become exactly

\[
\begin{aligned}
A^+&=A+hcY^d,\\
Y^+&=Y+hcdAY^{d-1},\\
O&=cAY^d,
\end{aligned}                                                     \tag{26}
\]

but now \(Y_0\sim N(a,1)\).  If \(a\ge0\), every noncentral Gaussian moment
is nonnegative, since

\[
 \mathbb E(G+a)^k
 =\sum_{j\ {m even}}{k\choose j}a^{k-j}\mathbb EG^j\ge0.       \tag{27}
\]

Thus coefficientwise positivity survives expectation and the proof of
(24) applies unchanged.

If \(a<0\), put \(\widetilde Y=-Y\).  For even \(d\), (26) is unchanged in
form with \(\widetilde Y_0\sim N(-a,1)\).  For odd \(d\), also put
\(B=-A\); the pair \((B,\widetilde Y)\) again obeys (26), and the observable
is \(cB\widetilde Y^d\).  In both cases the shifted mean is \(|a|\ge0\).
Therefore

\[
 \boxed{D_t(\rho/t)\to+\infty
 \quad\text{for every normalized shifted power }c(x+a)^d.}      \tag{28}
\]

For negative \(a\), the coefficients of \((x+a)^d\) alternate.  Hence
alternating lower signs alone are not a counterexample.

This signed shifted-power conclusion also transfers to the full network.
Let \(a>0\), write \(\psi_+(x)=c(x+a)^d\),
\(\psi_-(x)=c(x-a)^d\), and put \(s=(-1)^d\).  Then

\[
 \psi_-(-x)=s\psi_+(x).                             \tag{29}
\]

For the two-hidden-layer parameters \((r,W,u)\), where \(r\) denotes the
top readout vector, define the orthogonal sign map

\[
 R(r,W,u)=(sr,-sW,-u).                              \tag{30}
\]

Under \(R\), the lower feature changes by \(H\mapsto sH\), the connector
preactivation changes by \(z\mapsto-z\), the top feature changes by another
factor \(s\), and the readout changes by \(s\).  Hence

\[
 f_{\psi_-}(R\theta)=f_{\psi_+}(\theta).            \tag{31}
\]

Differentiation conjugates the two gradient Euler maps, and Gaussian
initialization is invariant under \(R\).  Therefore their width-first
outputs agree.  Since \(\psi_+\) has nonnegative coefficients, (24c) applies
to it and thus also to \(\psi_-\).

The unresolved case is a genuinely general signed polynomial which cannot
be reduced by these orthogonal sign conjugacies to a coefficientwise-positive
program.
