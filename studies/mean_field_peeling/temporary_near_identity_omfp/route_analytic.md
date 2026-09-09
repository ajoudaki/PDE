# Route analytic: a graded provenance norm for the near-identity homotopy

## 1. Binary verdict

Consider the normalized activation

\[
 \psi_\alpha(x)=c_\alpha\{x+\alpha\varphi(x)\},\qquad
 c_\alpha=\left(\mathbb E[G+\alpha\varphi(G)]^2\right)^{-1/2}.
 \tag{1.1}
\]

The activation-amplitude idea has a real structural advantage: at every
amplitude order, including every moving-source and transported-defect mark,
the highest-order unknown is governed by the identity-background Volterra
operator.  All nonlinear terms are lower in amplitude order.  This is an
exact statement, not a heuristic.

The graded Gaussian norm proposed below also resolves the ordinary Holder
moment tower: products of variables of stochastic degrees \(d_1,\ldots,d_r\)
map contractively into degree \(D=\sum d_i\).  It moreover shows precisely
how an adjoint source must retain the provenance of its opposite-layer
coefficient.  In particular, it passes the test \(X=Jc\), \(J^*X=c\), rather
than asserting a false ambient \(L^p\) estimate.

Nevertheless, the norm by itself does **not** close the all-amplitude
aggregate-adjoint majorant.  The unresolved operation is the conversion of a
degree-\(D\) marked field into a deterministic response coefficient.  The
best ambient estimate has the sharp cost

\[
             |\mathbb E X|\le (2D)^{D/2}\|X\|_{\mathsf G_D}.
 \tag{1.2}
\]

Since response trees at amplitude order \(k\) can have \(D\asymp k\), this
cost is superexponential in \(k\).  It is not controlled merely by making
\(|\alpha|\) small.  A causal time-simplex or Gaussian-contraction gain may
cancel it on the actual generated response trees, but that gain is not a
consequence of the graded norm and has not been proved.

Thus the binary answer is:

* the graded/provenance construction closes every **individual algebraic
  operation** and every fixed finite amplitude coefficient;
* it does **not yet** prove an exponential-in-order majorant, a positive
  amplitude radius uniform in the horizon, or the nonlinear \(L=2\)
  fifth-remainder theorem;
* the exact missing inequality is the factorial response-contraction estimate
  (FRC) in Section 8.

This is still a useful advance.  It replaces the vague request for an
all-moment generated-core bound by one explicit tree-contraction inequality
and explains what a genuinely stronger OMFP calculus must add.

## 2. A concrete residual class

For the analytic route it is natural to strengthen the residual class.  Fix
\(M,A\ge1\), and assume

\[
 \varphi\in C^\infty(\mathbb R),\qquad
 \|\varphi^{(r)}\|_\infty\le M A^r\quad(r\ge0).
 \tag{2.1}
\]

This is a genuine nonlinear class: bounded band-limited functions such as a
scaled sine belong to it.  It is stronger than a usual real-analytic
envelope \(MA^rr!\).  The stronger Bernstein envelope is chosen so that the
\(1/r!\) in an activation Taylor coefficient is retained rather than lost.

Let

\[
 m_1=\mathbb E[G\varphi(G)],\qquad
 m_2=\mathbb E[\varphi(G)^2].
\]

Then

\[
 c_\alpha=(1+2m_1\alpha+m_2\alpha^2)^{-1/2}.       \tag{2.2}
\]

Because \(|m_1|\le M\) and \(m_2\le M^2\),

\[
             |\alpha|M\le\frac14
 \quad\Longrightarrow\quad
             \frac45\le c_\alpha\le\frac43 .       \tag{2.3}
\]

The slightly weaker bounds \(3/4\le c_\alpha^{-1}\le5/4\) follow directly
from the reverse triangle inequality.  The coefficients of (2.2) are
completely activation-defined.  On the complex circle
\(|\alpha|=(4M)^{-1}\),

\[
 |2m_1\alpha+m_2\alpha^2|\le\frac12+\frac1{16}=\frac9{16},
\]

so the principal branch is analytic there and has modulus at most
\(4/\sqrt7<2\).  Cauchy's estimate therefore gives the explicit bound

\[
 |[\alpha^k]c_\alpha|\le 2(4M)^k .                   \tag{2.4}
\]

No output or trained-trajectory quantity occurs in this class.

## 3. Exact amplitude triangularity

Write divided coefficients as

\[
             V^{\langle k\rangle}=[\alpha^k]V_\alpha.
\]

For an activation node,

\[
 [\alpha^k]\psi_\alpha(V_\alpha)
 =\sum_{j=0}^k c_jV^{\langle k-j\rangle}
  +\sum_{j=0}^{k-1}c_j
       [\alpha^{k-1-j}]\varphi(V_\alpha).            \tag{3.1}
\]

The last coefficient is explicitly

\[
 [\alpha^m]\varphi(V_\alpha)
 =\sum_{r=0}^m\frac{\varphi^{(r)}(V^{\langle0\rangle})}{r!}
   \sum_{\substack{k_1+\cdots+k_r=m\\k_i\ge1}}
       \prod_{i=1}^rV^{\langle k_i\rangle}.          \tag{3.2}
\]

Consequently the coefficient \(V^{\langle k\rangle}\) enters (3.1) only
through the linear identity term \(c_0V^{\langle k\rangle}=V^{\langle
k\rangle}\).  Every derivative of order at least two in the field variable
comes from the externally marked \(\alpha\varphi\) term and hence uses
amplitude orders below \(k\).

The same assertion survives all marks needed by the paired-Euler defect.
Indeed, normalized step differentiation, the hybrid interpolation
derivative, the fixed raw maps \(I,J\), the fixed adjoints \(I^*,J^*\),
expectation, and coefficient extraction are linear and commute.  Leibniz and
Fa\`a di Bruno only partition the total amplitude order.  If one factor has
order \(k\), every other factor has order zero; at \(\alpha=0\) all
nonlinear activation derivatives vanish.  Hence the complete order-\(k\)
marked ledger has the exact form

\[
 \mathcal L^{\langle k\rangle}
 =\mathcal R_{\rm id}\,
   \mathcal S_k(\mathcal L^{\langle0\rangle},\ldots,
                \mathcal L^{\langle k-1\rangle}),    \tag{3.3}
\]

where \(\mathcal R_{\rm id}\) is the identity-background causal resolvent.
This also applies to the aggregate adjoint response because Gaussian
integration by parts is linear in both the query and every moving source
direction.  Thus no term of the form
\(\alpha\,\mathcal L^{\langle k\rangle}\times\text{random field}\)
occurs in the order-\(k\) equation.

Equation (3.3) is the rigorous reason the near-identity route is more
promising than a direct nonlinear moment induction.

## 4. The graded all-moment scale

For a probability space \(\Omega\), define

\[
 \mathsf G_0(\Omega)=L^\infty(\Omega),qquad
 \|X\|_{\mathsf G_D}
 =\sup_{p\ge2}\frac{\|X\|_p}{(Dp)^{D/2}},\quad D\ge1. \tag{4.1}
\]

The integer \(D\) is a stochastic product degree, not an amplitude order.

### Lemma 4.1 (graded product, proved)

If \(X_i\in\mathsf G_{d_i}\), \(d_i\ge1\), and
\(D=\sum_{i=1}^rd_i\), then

\[
       \left\|\prod_{i=1}^rX_i\right\|_{\mathsf G_D}
       \le\prod_{i=1}^r\|X_i\|_{\mathsf G_{d_i}}.     \tag{4.2}
\]

A bounded factor multiplies the right side by its \(L^\infty\) norm.

#### Proof

Use Holder exponents \(q_i=D/d_i\), for which
\(\sum_iq_i^{-1}=1\).  For every \(p\ge2\),

\[
\begin{aligned}
 \left\|\prod_iX_i\right\|_p
 &\le\prod_i\|X_i\|_{pq_i} \\
 &\le\prod_i\{d_i(pD/d_i)\}^{d_i/2}
             \|X_i\|_{\mathsf G_{d_i}} \\
 &=(pD)^{D/2}\prod_i\|X_i\|_{\mathsf G_{d_i}}.
\end{aligned}
\]

Divide by \((pD)^{D/2}\) and take the supremum. \(\square\)

### Lemma 4.2 (raw Gaussian action, proved)

For either raw isometry \(I\) or \(J\),

\[
 \|Ix\|_{\mathsf G_1}\le\|x\|_2,qquad
 \|Jc\|_{\mathsf G_1}\le\|c\|_2.                   \tag{4.3}
\]

#### Proof

The raw image is a centered Gaussian of variance \(\|x\|_2^2\) or
\(\|c\|_2^2\).  The Gaussian moment bound
\(\|G\|_p\le\sqrt p\) proves (4.3). \(\square\)

### Lemma 4.3 (degree collapse, proved and sharp in order)

For \(X\in\mathsf G_D\),

\[
 \|X\|_2\le(2D)^{D/2}\|X\|_{\mathsf G_D},
 \qquad
 |\mathbb EX|\le(2D)^{D/2}\|X\|_{\mathsf G_D}.       \tag{4.4}
\]

For even \(D\), \(X=G^D\) shows that the factor necessarily has order
\(D^{D/2}\): \(\mathbb EG^D=(D-1)!!\).

#### Proof

The first inequality is (4.1) evaluated at \(p=2\), and the second follows
from \(|\mathbb EX|\le\|X\|_2\).  For the example, the Gaussian moment bound
\(\|G\|_q\le\sqrt q\) gives

\[
 \|G^D\|_p=\|G\|_{Dp}^D\le(Dp)^{D/2},
 \qquad \|G^D\|_{\mathsf G_D}\le1.                  \tag{4.5}
\]

For even \(D\), however,

\[
 \mathbb EG^D=(D-1)!!
 \ge (D/e)^{D/2}/C\sqrt D                              \tag{4.6}
\]

for a numerical \(C\), by Stirling's inequalities.  Hence no replacement
of (4.4) by \(C_0C_1^D\) is valid on the ambient graded space. \(\square\)

The product theorem solves the repeated Holder escalation in the old
\(L^4,L^8,\ldots\) approach.  Lemma 4.3 is the new, sharply exposed
bottleneck.

## 5. Provenance is mandatory for reused adjoints

The value norm (4.1) cannot make \(J^*\) or \(I^*\) bounded.  The correct
object is a marked expression retaining the opposite-layer coefficient of
every raw source.

If

\[
 X=\Psi(Jc_1,\ldots,Jc_m,\zeta),                     \tag{5.1}
\]

where \(\zeta\) is independent of this source block, then the exact intrinsic
adjoint identity is

\[
 J^*X=\sum_{i=1}^m\mathbb E[\partial_i\Psi]c_i.       \tag{5.2}
\]

The source mark on \(Jc_i\) is therefore the pointer \(c_i\), not merely
the fact that \(Jc_i\) is a degree-one Gaussian.  Moving-query derivatives
replace \(c_i\) by all of its differentiated directions and apply the same
identity.  At a singular Gram, one first forms the vector in (5.2) and only
then takes a norm; no inverse or coordinatewise absolute response is used.

For a finite cylindrical expression, define its provenance expansion by the
following terminating rewrite rules:

1. retain each raw source together with its opposite-layer pointer;
2. use Leibniz and the ordinary chain rule at products and activation nodes;
3. replace every adjoint call by (5.2), or its \(I^*\) analogue;
4. combine the resulting opposite-layer vectors before estimating them;
5. assign stochastic degrees additively at products, degree zero to bounded
   activation derivatives, and degree one to a fresh raw Gaussian value.

For fixed chronology, fixed amplitude order, and the finite differential
budget used by the defect, the rewrite terminates: every adjoint removal
lowers the number of unresolved raw-source marks, coefficient extraction
lowers the remaining amplitude order in every nonlinear branch, and temporal
dependencies are strictly chronological.

This calculus passes the ambient counterexample.  Let
\(c\in L^2\setminus L^4\) and \(X=Jc\).  The value \(X\) is Gaussian, but its
provenance contains the pointer \(c\), and (5.2) gives \(J^*X=c\).  Hence its
degree-four marked norm is infinite.  No false conclusion
\(J^*:L^p\to L^4\) is made.

What this proves is an exact **calculus**, not a horizon-uniform estimate.
The size of the fully expanded provenance tree remains to be bounded.

## 6. Fixed-order closure and its limitation

At amplitude order \(k\), every activation term is given by the finite Bell
polynomial (3.2).  If at most four step/hybrid marks and one source mark are
retained, a deliberately coarse grammar induction assigns every resulting
stochastic monomial degree at most

\[
                         D\le12(k+1).                 \tag{6.1}
\]

To see this, first resum every purely identity-background propagation into
\(\mathcal R_{\rm id}\) in (3.3); its deterministic Gram kernels are assigned
degree zero and are controlled by the proved identity theorem.  This step is
essential: expanding those kernels back into Gaussian moments would create a
spurious degree proportional to the chronology length.  In the remaining
forcing tree, charge every positive-order child in (3.2) to one of the \(k\)
available amplitude units.  Each genuinely nonlinear local vertex has the
external amplitude mark, and the depth-two forward/backward grammar with the
finite differential budget creates at most a fixed number of new stochastic
leaves per such mark.  Leibniz partitions both the differential marks and the
amplitude units, so the charges of the children add rather than multiply.  A
direct induction over the four forward/backward node types gives the loose
factor twelve in (6.1).  Product degrees add by Lemma 4.1.  Raw actions reset
their value degree to one but retain the pointer degree in the provenance
ledger.  The constant twelve is used only to record linear, rather than
chronology-dependent, degree growth.

Thus every fixed \(k\) expression has finite moments of every order under
(2.1), and all its operations are controlled by Lemmas 4.1--4.3 and (5.2).
This recovers fixed-horizon amplitude regularity without an \(L^p\) tower.

It does not give a useful bound after summing over \(k\).  From (4.4) and
(6.1), even the optimistic estimate

\[
 \|V^{\langle k\rangle}\|_{\mathsf G_{12(k+1)}}\le C^k  \tag{6.2}
\]

would imply only

\[
 \|V^{\langle k\rangle}\|_2
 \le \{24(k+1)\}^{6(k+1)}C^k,                       \tag{6.3}
\]

whose power series has radius zero.  Therefore (6.2), despite looking like
an analytic majorant, is insufficient.

The same loss appears inside the recursion before the terminal readout:
Gram and response coefficients repeatedly apply expectation to marked
products.  One cannot postpone every degree collapse until the end.

## 7. Why the Bernstein envelope is not by itself enough

At one activation node, (2.1) and (3.2) provide the favorable factor

\[
                   \frac{MA^r}{r!}                    \tag{7.1}
\]

for an \(r\)-fold branch.  This controls a single high-arity product.  It
does not automatically control a response tree made from many low-arity
vertices.  For example, a binary response tree receives only a factor
\(2^{-1}\) from each local Taylor coefficient, while its total stochastic
degree can grow linearly with the number of vertices.  The degree-collapse
cost in (4.4) is then potentially \(k^{k/2}\).

Chronological update weights may supply the missing factorial through a
time-simplex sum.  A chain of \(m\) strict history edges indeed satisfies

\[
 \sum_{i_1<\cdots<i_m}\prod_{j=1}^m|\varepsilon_{i_j}|
 \le\frac1{m!}\left(\sum_i|\varepsilon_i|\right)^m.   \tag{7.2}
\]

But a branched response tree is governed by its partial-order or tree
factorial, not automatically by \(m!\).  Moreover some current-layer
response operations are unweighted, although their nonlinear part carries
one amplitude mark.  Establishing enough combined time-simplex and Gaussian
contraction gain for all such trees is a new theorem.  Neither causal
divisibility alone nor Lemma 4.1 proves it.

## 8. The exact missing theorem

For each chronology length \(N\), let
\(\mathfrak T_{N,k,q}^{(2)}\) be the finite set of fully expanded, intrinsic
depth-two provenance trees obtained from:

* amplitude order \(k\);
* normalized step derivative order \(q\le3\);
* at most one hybrid transported-defect mark;
* every aggregate source response generated by (5.2);
* the exact coarse/fine chronological schedules with
  \(\sum_s|\varepsilon_s|\le\tau\).

For a tree \(T\), let \(D(T)\) be its stochastic degree, \(w_T\) the product
of its actual step weights, normalization coefficients, Taylor factorials,
and deterministic identity-background kernels, and \(g_T\) the product of
the \(\mathsf G_d\)-norms of its activation/Gaussian leaves.  Source vectors
are combined intrinsically before this projective tree norm is formed.
Equivalently, \(\mathfrak T_{N,k,q}^{(2)}\) is first quotiented by equality of
the fixed-adjoint aggregate vector; \(|w_T|g_T\) denotes the norm of that
aggregate vector, not the sum of absolute values of representation-dependent
response coordinates.

The missing factorial response-contraction estimate is

\[
 \boxed{
 \sup_{N\ge1}\sup_{\sum|\varepsilon_s|\le\tau}
 \sum_{T\in\mathfrak T_{N,k,q}^{(2)}}
      (2D(T))^{D(T)/2}|w_T|g_T
 \le C_0C_1^k,
 \quad k\ge0,\ q\le3 .}                              \tag{FRC\(_2\)}
\]

Here \(C_0,C_1,\tau\) must be explicit functions only of \(M,A\), the
identity constants (at depth two one may start from \(K_2=27\)), and numerical
Gaussian moments.  This is not an output modulus: every summand is generated
by the explicit source-response grammar, and the left side is fixed before a
terminal output is evaluated.

FRC\(_2\) would prove a positive uniform amplitude radius.  Indeed, for
\(|\alpha|<(2C_1)^{-1}\), summing the amplitude series gives every marked
field and the three normalized defect derivatives a bound at most \(2C_0\).
The transported macro-defect lemma would then give

\[
 \left|\Delta_{t,2}(h)
 -\frac{t(2t-1)}2J_{\psi_\alpha,2}h^3\right|
 \le C(M,A)t^4|h|^5,
 \qquad |h|t\le\tau/4,                                \tag{8.1}
\]

with \(C(M,A)\) obtained by inserting \(2C_0\) into the finite defect
recursion.  The implication is rigorous; FRC\(_2\) is open.

The first nontrivial test of FRC\(_2\) is the aggregate version of

\[
 \sup_{N,s,|h|N\le\tau}
 \left\|J^*x_s^{\langle1\rangle}\right\|_4<\infty,    \tag{8.2}
\]

together with its three normalized step derivatives and transported mark.
The provenance rewrite explains why (8.2) may hold for the generated
susceptibility even though it fails ambiently; it does not yet supply the
uniform projective row-sum bound.

## 9. Depth three

Amplitude triangularity and the graded product theorem are independent of
depth.  At \(L=3\), a provenance tree carries a connector label and may
alternate between two adjoint pairs.  The counterexample test must be passed
at each connector separately.

If FRC\(_2\) were proved by a connector-local argument stable under replacing
each leaf norm by the already controlled lower-connector norm, the same proof
would suggest

\[
 C_{0,3}\le P(M,A,C_{0,2}),\qquad
 C_{1,3}\le P(M,A,C_{1,2})                            \tag{9.1}
\]

for an explicit finite polynomial \(P\).  The identity part is available at
all depths, with \(K_3=108\).  What is not proved is that alternating
connector contractions preserve the factorial gain required in FRC.  Thus
there is no valid \(L=3\) transfer yet, although there is no new obstruction
before the unresolved \(L=2\) contraction.

## 10. Audit

1. **Limit order.**  Every object is the fixed-schedule width-first OMFP DAG.
   Amplitude and step estimates are applied only afterwards.
2. **No ambient adjoint bound.**  Section 5 retains source provenance and
   explicitly reproduces \(J^*Jc=c\).
3. **No hidden generated-core assumption.**  The uniform tree estimate is
   displayed as the open FRC\(_2\), not folded into the definition of the
   norm or asserted from fixed-order finiteness.
4. **Singular Grams.**  Aggregate response vectors are formed before norms;
   no coordinatewise row norm or inverse Gram is used.
5. **Analyticity.**  Fixed-order coefficient extraction is proved.  A
   horizon-uniform positive radius is not inferred from it.
6. **Constants.**  The proved norm constants are exactly one in (4.2)--(4.3)
   and \((2D)^{D/2}\) in (4.4).  The proposed radius
   \((2C_1)^{-1}\) is conditional on the explicitly stated FRC constant.
7. **Depth three.**  No connector transfer is claimed without the factorial
   contraction theorem.

The proposed homotopy therefore has a good shot at pushing OMFP forward, but
the next result to prove is not ordinary Lipschitz continuity in \(\alpha\).
It is FRC\(_2\), or a stronger Gaussian/Fock contraction theorem that implies
it.
