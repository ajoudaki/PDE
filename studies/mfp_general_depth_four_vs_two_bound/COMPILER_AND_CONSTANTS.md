# Singular-Price compiler and explicit constants

This note works only with the inverse-free population DAG in
`WIDTH_AND_RANK.md`.  Its purpose is to prove regularity at the coalesced
covariance and to give a finite activation-envelope bound.  No derivative of
a finite-width network is used.

Fix a horizon \(T\ge1\).  The theorem uses \(T=4\), but keeping \(T\) in
this note makes the time dependence visible.

## 1. A finite chronological compiler

For \(L\ge2\), stage \(t\in\{1,\ldots,T\}\) consists of the following
Gaussian calls.

1. The bottom call uses
   \((U,\chi_{2,0},\ldots,\chi_{2,t-1})\).  It reconstructs the bottom
   fields through time \(t\), then returns their new Gram and response
   entries.
2. For \(\ell=2,\ldots,L-1\), the ascending call uses
   \((\xi_{\ell,0},\ldots,\xi_{\ell,t},
      \chi_{\ell+1,0},\ldots,\chi_{\ell+1,t-1})\).  It reconstructs the
   layer-\(\ell\) fields through time \(t\), then returns the new feature
   Gram and upward-response entries.
3. The top call uses \((A,\xi_{L,0},\ldots,\xi_{L,t})\).  It returns
   \(F_{t,L}\), and, when \(t<T\), the new top-cotangent Gram and response
   entries.
4. When \(t<T\), for \(\ell=L-1,\ldots,2\), the descending call uses
   \((\xi_{\ell,0},\ldots,\xi_{\ell,t},
      \chi_{\ell+1,0},\ldots,\chi_{\ell+1,t})\).  It reconstructs the
   forward and cotangent fields through time \(t\), then returns the new
   cotangent Gram and downward-response entries.

Every covariance is a direct sum of feature and cotangent Gram blocks
returned by earlier calls.  Hence this is acyclic.  The number of calls and
the largest Gaussian dimension are

\[
 N_{T,L}=TL+(T-1)(L-2)=(2T-1)L-2T+2,
 \qquad D_T=2T+1.                                      \tag{1.1}
\]

For \(L=1\), one two-dimensional call over independent \((A,U)\) compiles
the exact scalar recursion

\[
 A_{s+1}=A_s+h\phi(Z_s),\qquad
 Z_{s+1}=Z_s+hA_s\phi'(Z_s),\qquad 0\le s<T.            \tag{1.2}
\]

Thus the formula \(N_{T,1}=1\) remains correct.  For \(T=4\),

\[
 N_{4,L}=7L-6,\qquad D_4=9.                             \tag{1.3}
\]

The call sequence has the explicit initialization

\[
 Q_{\ell,00}=1,\qquad
 K_{\ell,00}=d^{L-\ell+1},\qquad
 \sigma_{\ell,00}=0,
 \qquad d=\mathbb E\phi'(G)^2,                          \tag{1.4}
\]

and every empty \(\rho\)-history is zero.  RMS normalization and an upward
induction give the first identity.  At the top,
\(C_L^0=A\phi'(G_L)\), so its variance is \(d\) and its spatial-response
mean is zero because \(A\) is centered.  Descending, the incoming carrier
is centered and independent of the current forward source; multiplication
by \(\phi'(G_\ell)\) adds one factor \(d\) to the variance and preserves
the zero response mean.  This proves (1.4) and makes the first bottom call
executable without an unstated node.

## 2. Singular Price differentiation

An envelope \((C,p)\) means

\[
 |g(y)|\le C(1+\|y\|)^p.                               \tag{2.1}
\]

Propagate envelopes by

\[
 (C,p)\oplus(D,q)=(C+D,\max\{p,q\}),\qquad
 (C,p)\odot(D,q)=(CD,p+q).                             \tag{2.2}
\]

Gaussian-coordinate leaves have envelope \((1,1)\), scalar leaves have
\((|c|,0)\), and, if \({\cal E}(g)=(C,p)\), use

\[
 {\cal E}(\phi(g))=(M_\phi(1+C),p),\qquad
 {\cal E}(\phi^{(r)}(g))=(M_\phi,0),\quad1\le r\le12. \tag{2.3}
\]

Earlier scalar nodes are tokens \(S^{[j]}\), with

\[
 \partial_hS^{[j]}=S^{[j+1]}.                           \tag{2.4}
\]

For \(D\ge1\), integer \(p\ge0\), and \(v\ge0\), define

\[
 \mu_{D,p}(v)=
 \sum_{r=0}^p{p\choose r}v^{r/2}2^{r/2}
 \frac{\Gamma((D+r)/2)}{\Gamma(D/2)}.                  \tag{2.5}
\]

It follows from \(\|\Sigma^{1/2}G\|\le\sqrt v\|G\|\), whenever
\(v\ge\|\Sigma\|_{\rm op}\), that

\[
 \mathbb E(1+\|Y\|)^p\le\mu_{D,p}(v),
 \qquad Y\sim N(0,\Sigma).                             \tag{2.6}
\]

Consider one local call

\[
 N(h)=\mathbb E_{Y\sim N(0,\Sigma(h))}\psi(h,Y),       \tag{2.7}
\]

where \(\Sigma(h)\succeq0\) may change rank.  If the entries of
\(\Sigma\) are \(C^5\) and every mixed derivative
\(\partial_h^j\partial_Y^\alpha\psi\) with
\(j+\lceil|\alpha|/2\rceil\le5\) has a common polynomial envelope, then
\(N\in C^5\), including at singular covariances, and

\[
 \frac d{dh}N(h)=\mathbb E\left[
 \partial_h\psi(h,Y)+\frac12\Sigma'(h):D_Y^2\psi(h,Y)
 \right].                                               \tag{2.8}
\]

Here is a proof which does not differentiate a covariance square root.
Set \(\Sigma_\epsilon=\Sigma+\epsilon I\).  For \(\epsilon>0\), two
integrations by parts in the nonsingular Gaussian density prove (2.8) with
\(\Sigma_\epsilon\).  Couple

\[
 Y_{\epsilon,h}=\Sigma_\epsilon(h)^{1/2}G,\qquad
 Y_h=\Sigma(h)^{1/2}G.                                  \tag{2.9}
\]

The positive-semidefinite square-root inequality gives

\[
 \sup_h\|Y_{\epsilon,h}-Y_h\|
 \le\sqrt\epsilon\,\|G\|.                              \tag{2.10}
\]

On \(\{\|G\|\le R\}\), every relevant integrand converges uniformly by
uniform continuity on a compact set.  On its complement, (2.1) and the
Gaussian polynomial tail give a dominating quantity, uniformly in
\(h\) and \(0<\epsilon\le1\).  Integrating the nonsingular identity
between two values of \(h\), taking \(\epsilon\downarrow0\), and then
\(R\uparrow\infty\) proves (2.8).  Applying the same argument to each
derived integrand proves the assertion through order five.

### 2.1 Signed exact jets

The signed jet recursion is distinct from the absolute envelope recursion
below.  For a call (2.7), a term \((c,j,\alpha)\) represents

\[
 c(h)\,\mathbb E_{N(0,\Sigma(h))}
 [\partial_h^j\partial_Y^\alpha\psi(h,Y)],              \tag{2.10a}
\]

where \(c\) is an exact signed coefficient expression and \(\alpha\) is
an ordered spatial multiindex.  Start with

\[
 {\cal T}_0=\{(1,0,\varnothing)\}.                      \tag{2.10b}
\]

For one term define the finite signed multiset

\[
 \begin{aligned}
 {\mathscr D}(c,j,\alpha)=\{&(c',j,\alpha),
 (c,j+1,\alpha)\}\\
 &\cup\left\{
 \left(\frac12c\Sigma'_{ab},j,
 \alpha\mathbin{\|}(a,b)\right):1\le a,b\le D
 \right\},                                               \tag{2.10c}
 \end{aligned}
\]

where \(\|\) concatenates multiindices.  Formal differentiation of \(c\)
uses the signed product rule, the exact covariance derivatives, and the
earlier-node token rule

\[
 \partial_hS^{[j]}=S^{[j+1]}.                            \tag{2.10d}
\]

Let \({\cal T}_{r+1}\) be the signed union of
\({\mathscr D}(c,j,\alpha)\) over \({\cal T}_r\), combining identical
terms with their signs.  Define

\[
 {\cal J}_r(N;h)=
 \sum_{(c,j,\alpha)\in{\cal T}_r}
 c(h)\,\mathbb E_{N(0,\Sigma(h))}
 [\partial_h^j\partial_Y^\alpha\psi(h,Y)].              \tag{2.10e}
\]

Price's identity and induction on \(r\) prove

\[
 {\cal J}_r(N;h)=N^{(r)}(h),\qquad0\le r\le5.           \tag{2.10f}
\]

Execute this construction in the call order of Section 1.  Whenever a
token \(S^{[j]}\) occurs at \(h=0\), substitute the already returned exact
number \({\cal J}_j(S;0)\).  Every covariance jet needed in a call was
returned by an earlier call.  For a full coefficient, formally
differentiate its exact expression; in particular,

\[
 {\cal J}_j(\rho+hQ;0)
 ={\cal J}_j(\rho;0)+j{\cal J}_{j-1}(Q;0),
 \qquad {\cal J}_{-1}(Q;0)=0.                           \tag{2.10g}
\]

Before coefficient-expression expansion, each call has at most
\((D^2+2)^5\) raw terms, and every formal product-rule tree is finite.
There are \(N_{T,L}\) calls.  Thus (2.10b)--(2.10g) are a completely
specified terminating signed Gaussian-integration algorithm, independent
of any unknown output derivative.

### 2.2 Absolute envelopes

For the parallel absolute-value recursion, suppose

\[
 \bar c_j\ge\sup_{|h|\le1}\sum_{a,b=1}^D
 |\Sigma_{ab}^{(j)}(h)|,\qquad0\le j\le5.               \tag{2.11}
\]

Let \({\cal I}_{D,0}=\{\varnothing\}\) and
\({\cal I}_{D,s}=\{1,\ldots,D\}^s\) for \(s\ge1\), and put

\[
 P^{(0)}_{j,s}=
 \bigoplus_{\alpha\in{\cal I}_{D,s}}
 {\cal E}(\partial_h^j\partial_{Y_\alpha}\psi),
 \qquad j+\lceil s/2\rceil\le5.                        \tag{2.12}
\]

For all \(q,j,s\) with
\(q+j+\lceil s/2\rceil\le5\), define \(P^{(q)}_{j,s}\).
Starting from (2.12), recursively set

\[
 P^{(q+1)}_{j,s}=P^{(q)}_{j+1,s}
 \oplus\bigoplus_{a=0}^j
 \left[
 \left(\frac12{j\choose a}\bar c_{a+1},0\right)
 \odot P^{(q)}_{j-a,s+2}
 \right]                                                \tag{2.13}
\]

whenever
\(q+j+\lceil s/2\rceil<5\).  If
\(P^{(q)}_{0,0}=(C_q,p_q)\), define

\[
 \overline{\cal J}_q(N)=C_q\mu_{D,p_q}(\bar c_0).       \tag{2.14}
\]

Leibniz expansion of (2.8) proves

\[
 |N^{(q)}(h)|\le\overline{\cal J}_q(N),
 \qquad |h|\le1,\quad0\le q\le5.                     \tag{2.15}
\]

A response is compiled by using its once spatially differentiated
integrand in (2.12).  A learned-plus-response coefficient is compiled by

\[
 \overline{(R+hQ)}_j=\bar R_j+\bar Q_j+j\bar Q_{j-1},
 \qquad\bar Q_{-1}=0.                                  \tag{2.16}
\]

Equations (2.11)--(2.16), in the chronology of Section 1, are a completely
specified finite algorithm for all Gram, response, coefficient, auxiliary
moment, and output derivative bars.  Induction over the signed ledger
(2.10c) shows that replacing signed sums and products by
\(\oplus,\odot\), and every exact covariance derivative by its bar,
dominates every exact term and their total absolute sum.  Hence
(2.11)--(2.16) bound the exact jets; they do not define them.

The induction proving its applicability is short.  The first covariance
is constant.  If the first \(m\) calls have returned \(C^5\) scalar nodes,
the next covariance is a direct sum of Gram matrices of earlier fields;
it is positive semidefinite and \(C^5\).  Equations (2.1)--(2.4) supply
the mixed-derivative domination in (2.8).  Thus the next call is \(C^5\)
and returns the bars (2.14).  There are only \(N_{T,L}\) calls and only
indices with \(j+s\le10\).  A response starts with at most
\(\phi''\); the ten subsequent coordinate derivatives require at most
\(\phi^{(12)}\).  Therefore the recursion terminates and the assumed
activation class is sufficient.

## 3. A separated closed majorant

This section gives a deliberately coarse closed bound for the exact
compiler above.  It is useful because its time and depth dependence are
visible.

First define a raw-expression size bound

\[
 b_{T,0}=16,\qquad
 b_{T,t+1}=64(T+2)^2(b_{T,t}+1)^2,\quad0\le t<T,       \tag{3.1}
\]

and put

\[
 s_T=8(b_{T,T}+1),\qquad D_T=2T+1.                      \tag{3.2}
\]

Treat earlier scalar nodes and Gaussian coordinates as leaves; count a
sum, product, or activation composition as one node plus the sizes of its
children.  Suppose every old field has size at most \(b\ge16\).  After
binarizing all history sums, a forward carrier and feature have size at
most \(4(T+2)(b+1)\).  An output weight and top cotangent have size at most
\(8(T+2)(b+1)\).  A transpose carrier, lower cotangent, or bottom-update
field has size at most \(32(T+2)^2(b+1)\); this count includes both the
outer activation and the inner \(\phi'\) factor.  A Gram, output, response
before its one spatial derivative, or auxiliary second-moment integrand is
a product of at most two such fields plus one binary node.  Hence every one
of these sizes is at most
\(64(T+2)^2(b+1)^2\), the right side of (3.1).  Induction in time proves
the claimed raw-field and integrand bounds.

Let

\[
 A_T^{\rm op}=64\bigl(1+D_T^{10}+32D_T^2\bigr),         \tag{3.3}
\]

\[
 c_{T,0}=\max\{128,s_T\},\qquad
 c_{T,r+1}=A_T^{\rm op}(c_{T,r}+1)^2
 \quad(0\le r<24),                                     \tag{3.4}
\]

and set

\[
 C_T=c_{T,24},\qquad q_T=2C_T.                          \tag{3.5}
\]

These recursions terminate after \(T+24\) explicitly prescribed integer
operations.  To see that \(C_T\) is sufficient, fully expand and binarize
every expression.  One formal derivative changes a tree of size, token
degree, and envelope exponent at most \(c\) into one with all three at
most \(8(c+1)^2\), by structural induction over sums, products, and unary
activation nodes.  The response costs one derivative, mixed
\(h\)/coordinate derivatives cost at most ten, aggregation over ordered
coordinate multiindices costs a factor at most \(D_T^{10}\), the five
Price levels each have at most \(1+32D_T^2\) expanded summands, full
coefficient assembly costs one level, and covariance/direct-sum
bookkeeping costs two.  This is

\[
 1+10+1+5+1+2=20<24                                    \tag{3.6}
\]

applications of the map in (3.4).  Thus \(C_T\) bounds tree size, token
degree, and polynomial-envelope exponent for every item returned by one
call.

Define

\[
 g_T=2^{C_T}\mu_{D_T,C_T}(D_T^2C_T^2),                 \tag{3.7}
\]

and the activation-only base

\[
 b_\phi=\max\{2,M_\phi\}.                              \tag{3.8}
\]

**One-call bound.**  If every incoming token and covariance derivative
bar is at most \(S\ge2\), every returned bar is at most

\[
 g_T b_\phi^{C_T}S^{q_T}.                              \tag{3.9}
\]

Indeed, after the multiplicities counted in (3.6) are expanded, an
integrand has at most \(C_T\) leaves/nodes, hence envelope constant at
most \(2^{C_T}b_\phi^{C_T}S^{C_T}\) and exponent at most \(C_T\).
The entrywise covariance norm is at most \(D_T^2S\).  Equation (2.5),
\(S\ge1\), and \(q_T=2C_T\) bound the expectation by (3.9).

At initialization, every forward variance is one and every cotangent
variance is a power of

\[
 d=\mathbb E\phi'(G)^2\le M_\phi^2.
\]

Consequently take \(S_0=b_\phi^{2L}\) and iterate (3.9) through
\(N=N_{T,L}\) calls.  Put

\[
 A_{T,L}=\frac{q_T^N-1}{q_T-1},                         \tag{3.10}
\]

\[
 E_{T,L}=2Lq_T^N+C_TA_{T,L},                           \tag{3.11}
\]

\[
 \boxed{\mathcal S_{T,L}=g_T^{A_{T,L}}b_\phi^{E_{T,L}}.} \tag{3.12}
\]

Solving the scalar recurrence in (3.9) proves that every node and every
derivative bar of order at most five returned by the horizon-\(T\) compiler
is bounded by \(\mathcal S_{T,L}\) on \(|h|\le1\).  This includes every
diagonal feature moment needed in the rank argument of
`WIDTH_AND_RANK.md`.

For \(T=4\), write

\[
 \mathcal S_{4,L}=g_4^{A_{4,L}}b_\phi^{E_{4,L}},
 \qquad N_{4,L}=7L-6.                                  \tag{3.13}
\]

At depth three this becomes the completely explicit specialization

\[
 N_{4,3}=15,\qquad
 A_{4,3}=\frac{q_4^{15}-1}{q_4-1},\qquad
 E_{4,3}=6q_4^{15}+C_4A_{4,3}.                         \tag{3.14}
\]

## 4. The quantitative fifth-order remainder

Let \({\cal J}_r(F_{k,L})\) be the exact signed Gaussian integral produced
by (2.10b)--(2.10g) at the time-\(k\) top call, evaluated at \(h=0\).
Define

\[
 \kappa_{42,\phi,L}
 =\frac{{\cal J}_3(F_{4,L})-8{\cal J}_3(F_{2,L})}{6}.   \tag{4.1}
\]

This is a finite Gaussian-integral definition made before any output
derivative is identified.  At \(h=0\), all repeated forward sources for a
connector coalesce to one standard Gaussian and all repeated transpose
sources coalesce to one Gaussian with variance \(d^{L-\ell+1}\).  Hence
expanding (2.10b)--(2.10g) reduces (4.1) to finitely many one-dimensional
activation integrals

\[
 I_{a,\alpha}(\phi)=\mathbb E\left[
 G^a\prod_{r=0}^{12}\phi^{(r)}(G)^{\alpha_r}
 \right]                                                \tag{4.2}
\]

and elementary Gaussian moments.  The chronology (Section 1) and the
finite signed recursion specify every coefficient and terminate.  The
parallel envelopes (2.11)--(2.16) dominate their absolute values.

The singular Price lemma proves only afterwards that

\[
 {\cal J}_r(F_{k,L})=F_{k,L}^{(r)}(0),\qquad0\le r\le5. \tag{4.3}
\]

The sign change

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad
 \chi_{\ell,s}\mapsto-\chi_{\ell,s}                   \tag{4.4}
\]

leaves every feature node fixed and negates every cotangent and output
node.  Thus every \(F_{k,L}\) is odd.  For the linear jet, differentiate
the population Euler recursion at \(h=0\).  All time slices then coalesce
at initialization, so the displacement tangent after \(s\) steps is
\(s\mathcal G_0\), where \(\mathcal G_0\) is the initialization gradient.
Nodewise back-propagation gives

\[
 Df_0[\mathcal G_0]=\|\mathcal G_0\|_{\mathcal P}^2
 =1+d+d^2+\cdots+d^L.                                   \tag{4.4a}
\]

Indeed, the readout block contributes one, the matrix block ending at
layer \(a\) contributes the initialization cotangent variance
\(d^{L-a+1}\), and the first-layer block contributes \(d^L\).  Therefore
the same nodewise Gaussian recursion gives

\[
 F_{k,L}'(0)=k\Theta_L,\qquad
 \Theta_L=\sum_{j=0}^Ld^j.                              \tag{4.5}
\]

Therefore the constant, linear, quadratic, and quartic terms of
\(F_{4,L}(\eta)-F_{2,L}(2\eta)\) vanish, and (4.1) is its cubic
coefficient.

Taylor's integral remainder through degree four now gives

\[
 \begin{aligned}
 &\left|F_{4,L}(\eta)-F_{2,L}(2\eta)
       -\kappa_{42,\phi,L}\eta^3\right|\\
 &\qquad\le
 \frac{\overline{\cal J}_5(F_{4,L})
       +2^5\overline{\cal J}_5(F_{2,L})}{120}|\eta|^5
 \le\mathcal S_{4,L}|\eta|^5,                         \tag{4.6}
 \end{aligned}
\]

because \(33/120<1\).  The rank interval in `WIDTH_AND_RANK.md` must hold
for the fine step \(\eta\) and the coarse step \(2\eta\).  It is therefore
sufficient to define

\[
 \boxed{
 B_{\phi,42}(L)=\mathcal S_{4,L},\qquad
 h_{\phi,42}(L)=\frac1{16\sqrt{\mathcal S_{4,L}}}.}     \tag{4.7}
\]

Indeed, \(|2\eta|\le1/(8\sqrt{\mathcal S_{4,L}})\), the horizon-four
rank radius, and \(|2\eta|\le1\).  Every quantity in (4.7) is either the
activation-only base \(b_\phi\), a numerical horizon-four constant, or an
explicit function of \(L\).
