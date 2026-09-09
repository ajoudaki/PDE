# Hostile audit of the proposed single all-source norm

## Verdict

The requested all-source stability theorem cannot be proved with a single
same-space norm of the form

\[
 \|V\|_{\mathfrak X}
 =\sum_{m\geq 0}w_m\|\mathcal D^mV\|_{L^{p_m}},
 \qquad w_m>0,
 \tag{0.1}
\]

regardless of the choices of the weights \(w_m\) and exponents
\(p_m\in[1,\infty]\).  The first failed inequality is the requested
same-space product estimate

\[
 \|UV\|_{\mathfrak X}
 \leq C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}.
 \tag{0.2}
\]

A single raw Gaussian source gives a cylindrical counterexample.  If
\(p_0<\infty\), repeated application of (0.2) would bound Gaussian powers
exponentially in their degree, whereas their \(L^{p_0}\) norms grow like
\(n^{n/2}\).  If \(p_0=\infty\), the raw Gaussian is not in
\(\mathfrak X\).  Setting \(w_0=0\) does not repair the issue: (0.1) then is
not a norm, does not see constants, and cannot control Gaussian expectations
or terminal outputs.

There is a second, independent same-radius obstruction.  A coefficientwise
Leibniz estimate forces analytic/factorial decay of \(w_m\), while estimating
the reused-adjoint identity directly as a source-order shift forces
\(w_{m-1}/w_m\) to be uniformly bounded.  These requirements are mutually
incompatible.  Equivalently, if Gaussian integration by parts is used to
replace the derivative shift by Gaussian creation, multiplication by the
Gaussian coordinate is unbounded on the same space.

This is a no-go theorem for the norm template (0.1), not a counterexample to
the desired OMFP remainder inequality.  A viable proof would need at least a
scale of spaces carrying both an analytic-source radius and a stochastic-tail
or chaos-degree radius, with controlled radius loss repaid by the actual step
weights.  A norm depending only on source order cannot encode both losses.
Consequently the claimed uniform nonlinear remainder theorem remains
**OPEN**.  The obstruction is already present for \(L=2\), so there is no
audited transfer to \(L=3\).

## 1. Minimal consequences of the requested closure theorem

It is enough to work on one standard Gaussian coordinate.  Let
\(G\sim N(0,1)\), and let \(\mathcal D\) be its cylindrical Malliavin
derivative.  The width-first OMFP generated core contains such raw
coordinates at initialization.  In particular,

\[
 \mathcal D^0G=G,\qquad \mathcal DG=1,\qquad
 \mathcal D^mG=0\quad(m\geq2).
 \tag{1.1}
\]

Thus, when \(p_0<\infty\),

\[
 N_G:=\|G\|_{\mathfrak X}
 =w_0\|G\|_{p_0}+w_1<\infty.
 \tag{1.2}
\]

Closure under products with an activation-defined constant must imply (0.2)
on this cylindrical core.  The learned rank-one update already uses products,
and the requested proof asks for a product lemma before any particular
chronology is estimated.  Iterating (0.2) would give

\[
 \|G^n\|_{\mathfrak X}
 \leq C_\times^{n-1}N_G^n,
 \qquad n\geq1.
 \tag{1.3}
\]

The zeroth source-order summand in (0.1), on the other hand, gives

\[
 \|G^n\|_{\mathfrak X}
 \geq w_0\|G^n\|_{p_0}
 =w_0\|G\|_{np_0}^{n}.
 \tag{1.4}
\]

The contradiction between (1.3) and (1.4) is quantified next.

## 2. Cylindrical Gaussian-power no-go

### Lemma 2.1 (Gaussian moment lower bound)

There is a numerical \(c_*>0\) such that

\[
 \|G\|_q\geq c_*\sqrt q,
 \qquad q\geq1.
 \tag{2.1}
\]

#### Proof

For \(q\geq1\), integrate the Gaussian density over
\([\sqrt q,\sqrt q+q^{-1/2}]\).  On that interval,

\[
 x^2\leq q+3,
\]

and hence

\[
 \mathbb P\!\left(\sqrt q\leq G\leq
 \sqrt q+q^{-1/2}\right)
 \geq \frac{e^{-3/2}}{\sqrt{2\pi q}}e^{-q/2}.
 \tag{2.2}
\]

Therefore

\[
 \|G\|_q
 \geq \sqrt q\left(
 \frac{e^{-3/2}}{\sqrt{2\pi q}}e^{-q/2}
 \right)^{1/q}.
 \tag{2.3}
\]

The factor after \(\sqrt q\) has a strictly positive infimum on
\([1,\infty)\), which proves (2.1).  \(\square\)

### Theorem 2.2 (no same-space product norm)

Let \(w_m>0\) and \(p_m\in[1,\infty]\).  No space with norm (0.1) can
simultaneously

1. contain a raw Gaussian coordinate \(G\); and
2. satisfy (0.2) with a finite constant \(C_\times\).

This conclusion is independent of the aggregation chosen for source tensors
of positive order.

#### Proof

If \(p_0=\infty\), then the zeroth term is
\(w_0\|G\|_\infty=\infty\), so the first requirement fails.  Suppose that
\(p_0<\infty\).  Combining (1.3), (1.4), and Lemma 2.1 yields

\[
 w_0\bigl(c_*\sqrt{np_0}\bigr)^n
 \leq C_\times^{n-1}N_G^n.
 \tag{2.4}
\]

Taking \(n\)-th roots gives

\[
 w_0^{1/n}c_*\sqrt{np_0}
 \leq C_\times^{1-1/n}N_G.
 \tag{2.5}
\]

The left side tends to infinity and the right side remains bounded.  This is
a contradiction.  Only the \(m=0\) summand was used, so no choice of
\(w_m,p_m\) for \(m\geq1\), and no tensor-history aggregation, can repair
it.  \(\square\)

The theorem is a spectral-radius obstruction in elementary form.  A
same-space Banach-algebra estimate makes powers of each element grow at most
exponentially.  Any norm that dominates one fixed positive Gaussian moment
makes powers of an unbounded Gaussian grow superexponentially.

### Corollary 2.3 (Gaussian creation is also unbounded)

Multiplication by the source coordinate,

\[
 M_G:V\longmapsto GV,
 \tag{2.6}
\]

cannot be bounded on \(\mathfrak X\).  Indeed, if
\(\|M_GV\|_{\mathfrak X}\leq C_G\|V\|_{\mathfrak X}\), iteration from the
constant \(1\) gives an exponential upper bound for \(\|G^n\|_{\mathfrak
X}\), contradicting the proof above.

This matters for the exact adjoint identity.  On one Gaussian coordinate,

\[
 \mathbb E[\mathcal D V]=\mathbb E[GV].
 \tag{2.7}
\]

Thus one may try to avoid a source-derivative shift by Gaussian integration
by parts, but the replacement operation is precisely the unbounded creation
operator (2.6).  Conditional versions of (2.7), needed when other source
blocks remain random, have the same problem.

## 3. The source-shift versus Leibniz incompatibility

The preceding theorem already rules out the requested norm.  There is also a
purely source-order obstruction to the proposed direct proof.

Suppose one estimates every source-history term after Leibniz expansion in
the positive \(\ell^1\) sum (0.1).  Same-radius product closure requires the
coefficient inequalities

\[
 w_m{m\choose k}
 \leq C_Pw_kw_{m-k},
 \qquad 0\leq k\leq m,
 \tag{3.1}
\]

because

\[
 \mathcal D^m(UV)
 =\sum_{k=0}^m{m\choose k}
 \operatorname{Sym}(\mathcal D^kU\otimes
                    \mathcal D^{m-k}V).
 \tag{3.2}
\]

If the reused adjoint is estimated from its demanded derivative form

\[
 J^*V=\mathbb E[\mathcal D_JV],
 \tag{3.3}
\]

then an output history of order \(m-1\) consumes an input history of order
\(m\).  A same-radius bound with constant \(C_A\) requires

\[
 w_{m-1}\leq C_Aw_m,
 \qquad m\geq1.
 \tag{3.4}
\]

These two coefficient rules cannot hold simultaneously.  Taking \(k=1\)
in (3.1) gives

\[
 \frac{w_{m-1}}{w_m}
 \geq \frac{m}{C_Pw_1},
 \tag{3.5}
\]

whereas (3.4) gives \(w_{m-1}/w_m\leq C_A\).  Together they would imply

\[
 m\leq C_PC_Aw_1
\]

for every integer \(m\), an impossibility.

This argument has a precise scope.  It rules out coefficientwise absolute
closure of the all-source hierarchy in one radius.  A grammar-specific
cancellation performed before absolute values could evade (3.1), and an
integration-by-parts estimate could evade (3.4).  The latter option returns
to the unbounded creation operator in Corollary 2.3.  Therefore neither of
the two generic routes proves the requested same-space estimate.

The familiar candidate

\[
 w_m=\frac{r^m}{m!}
 \tag{3.6}
\]

makes (3.1) exact with \(C_P=1\), but

\[
 \frac{w_{m-1}}{w_m}=\frac mr
 \tag{3.7}
\]

is unbounded.  Geometric weights make the shift bounded but leave the
binomial coefficient in (3.2) unbounded.  This is not a poor tuning of a
particular weight sequence; it is the contradiction (3.5).

## 4. An admissible analytic residual that exposes the radius loss

The activation class in the question contains functions whose derivative
envelope genuinely has factorial size.  Consider

\[
 \varphi(x)=\frac1{1+x^2}.
 \tag{4.1}
\]

It is bounded, genuinely nonlinear, and

\[
 \varphi^{(m)}(x)
 =\frac{(-1)^mm!}{2i}
 \left((x-i)^{-m-1}-(x+i)^{-m-1}\right),
 \tag{4.2}
\]

so

\[
 \|\varphi^{(m)}\|_\infty\leq m!.
 \tag{4.3}
\]

Thus (4.1) belongs to the stated class with \(M=A=1\), and
\(\varphi''\not\equiv0\).

For every even \(m\), \(|\varphi^{(m)}(0)|=m!\).  By (4.3) at order
\(m+1\), for

\[
 |x|\leq\frac1{2(m+1)}
\]

the mean-value theorem gives

\[
 |\varphi^{(m)}(x)|\geq\frac{m!}{2}.
 \tag{4.4}
\]

Let \(c_\gamma>0\) be a numerical lower bound for the standard Gaussian
density on \([-1/4,1/4]\).  Then

\[
 \mathbb P\!\left(
 |G|\leq\frac1{2(m+1)}\right)
 \geq\frac{c_\gamma}{m+1}.
 \tag{4.5}
\]

For every \(p_m\geq1\), (4.4)--(4.5) imply

\[
 \|\varphi^{(m)}(G)\|_{p_m}
 \geq \frac{m!}{2}
       \left(\frac{c_\gamma}{m+1}\right)^{1/p_m}
 \geq \frac{c_\gamma m!}{2(m+1)}
 \quad(m\text{ even}).
 \tag{4.6}
\]

For a unit raw source direction \(e\),

\[
 \mathcal D^m\{\varphi(W(e))\}
 =\varphi^{(m)}(W(e))e^{\otimes m}.
 \tag{4.7}
\]

Hence the proposed norm of this single activation atom contains the series
in (4.6).  If direct adjoint-shift closure (3.4) held, then

\[
 w_m\geq w_0C_A^{-m}.
 \tag{4.8}
\]

The even terms in (0.1) would consequently be bounded below by

\[
 \frac{c_\gamma w_0}{2}
 \frac{m!}{(m+1)C_A^m},
 \tag{4.9}
\]

which do not even tend to zero.  Thus, for the full activation class in the
question, the direct derivative-shift route cannot both contain every
activation atom and keep the adjoint bounded at one analytic radius.

For the normalized near-identity activation, all derivatives of order
\(m\geq2\) in (4.7) are merely multiplied by the nonzero constant
\(\alpha/\|G+\alpha\varphi(G)\|_2\).  Making \(|\alpha|\) arbitrarily small
does not change convergence of the source-order series.  Therefore no
positive \(\alpha_0\) repairs this structural conflict.

## 5. Singular source histories must be quotiented first

Even apart from Theorems 2.2 and 3.1, a coordinatewise absolute aggregation
over source histories is not defined intrinsically at a singular Gaussian
Gram.

Let \(\xi_1=\xi_2=G\), so their covariance matrix is

\[
 \Sigma=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
 \tag{5.1}
\]

For every real \(R\), the same random field has the representation

\[
 G=R\xi_1+(1-R)\xi_2.
 \tag{5.2}
\]

The coordinate derivative vector of the right side is \((R,1-R)\).  Its
\(\ell^1\) norm is \(|R|+|1-R|\), and its Euclidean norm is
\((R^2+(1-R)^2)^{1/2}\); both can be made arbitrarily large although the
represented field is unchanged.  Higher coordinate-history tensors inherit
the same defect.

The only intrinsic first-order norm is the covariance-quotient norm

\[
 \|(R,1-R)\|_\Sigma
 =\bigl((R,1-R)\Sigma(R,1-R)^\top\bigr)^{1/2}=1.
 \tag{5.3}
\]

At every source order, one must therefore combine histories in the
Cameron--Martin tensor quotient before taking a norm.  No inverse covariance
is needed.  This resolves representation dependence, but it does not affect
the zeroth-order counterexample in Theorem 2.2.  Thus singular covariance is
not the first obstruction; it is an additional mandatory design constraint.

## 6. Why no moment ladder repairs the product failure

One might try to increase \(p_m\) with \(m\) so that Holder's inequality can
pay for the products created by Fa\`a di Bruno.  At source order zero this
cannot work.  The product term itself would require controlling
\(UV\) in \(L^{p_0}\) from two copies of \(L^{p_0}\); ordinary Holder gives
only \(L^{p_0/2}\).  Taking \(p_0=\infty\) excludes the raw Gaussian.  Higher
source derivatives do not change the contradiction (2.4), because every
power \(G^n\) has already been detected by the single positive term
\(w_0\|G^n\|_{p_0}\).

The same observation rules out replacing (0.2) by bounded Gaussian
creation.  It also explains why a sub-Gaussian norm alone is insufficient:
the product of two sub-Gaussian variables is generally only sub-exponential.
Stochastic growth must be graded or accompanied by a tail-radius loss.

## 7. A scale that repairs the elementary conflicts, but not yet OMFP

The no-go is specific to a single same-space norm.  The following elementary
one-coordinate scale illustrates the minimum kind of repair required.  For
\(r>0\) and \(\beta>0\), set

\[
 \|f\|_{r,\beta}
 =\sum_{m\geq0}\frac{r^m}{m!}
   \sup_{x\in\mathbb R}e^{-\beta x^2}|f^{(m)}(x)|.
 \tag{7.1}
\]

It contains the coordinate function and, for \(rA<1\), every residual
satisfying the stated real-derivative envelope (in particular (4.1)).

Three exact scale estimates hold.

### Product with tail loss

Leibniz's rule and convolution of the divided derivative weights give

\[
 \|fg\|_{r,\beta_1+\beta_2}
 \leq\|f\|_{r,\beta_1}\|g\|_{r,\beta_2}.
 \tag{7.2}
\]

Indeed, for \(m=k+\ell\),

\[
 \frac{r^m}{m!}{m\choose k}
 =\frac{r^k}{k!}\frac{r^\ell}{\ell!},
\]

and the two exponential weights multiply exactly.

### Differentiation with analytic-radius loss

If \(0<r'<r\), then

\[
 \|f'\|_{r',\beta}
 \leq\frac1{r-r'}\|f\|_{r,\beta}.
 \tag{7.3}
\]

To verify this, put \(q=r'/r\).  The coefficient of the \(n\)-th derivative
on the left divided by its coefficient on the right is

\[
 \frac nr q^{n-1}\leq\frac1{r(1-q)}=\frac1{r-r'},
\]

because \(nq^{n-1}\leq1+q+\cdots+q^{n-1}\).

### Gaussian creation and expectation with tail loss

If \(\beta'>\beta\), direct differentiation of \(xf(x)\) gives

\[
 \|xf\|_{r,\beta'}
 \leq\left\{r+\frac1{\sqrt{2e(\beta'-\beta)}}\right\}
       \|f\|_{r,\beta}.
 \tag{7.4}

Here
\(\sup_x|x|e^{-(\beta'-\beta)x^2}
=(2e(\beta'-\beta))^{-1/2}\).  If \(0<\beta<1/2\), then

\[
 |\mathbb Ef(G)|
 \leq(1-2\beta)^{-1/2}\|f\|_{r,\beta}.
 \tag{7.5}

Thus products consume tail radius, while differentiation consumes analytic
radius.  This is precisely what a single norm suppresses.

The scale (7.1) is only a diagnostic one-coordinate repair, not an OMFP
theorem.  A complete reachable-source construction would have to:

1. replace (7.1) by an intrinsic Cameron--Martin tensor/chaos version;
2. quotient singular source histories before applying the norm;
3. track a stochastic-tail or chaos-degree radius separately from source
   order;
4. show that every radius loss in \(I+\eta Dg\) is charged by the same
   causal factor \(|\eta|\); and
5. allocate total losses over \(t\) steps using \(t|\eta|\leq\rho\).

None of these requirements follows from (0.1).  In particular, merely
choosing faster-decaying \(w_m\) repairs composition but worsens the adjoint
shift, and choosing slower-decaying weights does the reverse.

## 8. Consequence for the requested one-step and remainder estimates

The requested one-step inequality

\[
 \|(I+\eta Dg(\theta_s))V\|_{\mathfrak X}
 \leq(1+C_0|\eta|)\|V\|_{\mathfrak X}
 \tag{8.1}
\]

was to be deduced from closure under products, activation composition,
rank-one updates, and reused adjoints.  The first of those closure lemmas is
false for every norm (0.1) that contains the initialization sources.  Hence
no activation-only value of \(C_0\) has been constructed.  The derivative
analogues of (8.1), the propagator estimate

\[
 \|\partial_\eta^rP_{j,t}(\eta)\|_{\mathfrak X}
 \leq C_rt^r,
\]

and the asserted bound on \(A_j'''\) therefore do not follow.

This failure is independent of \(t\), \(\eta\), and the small nonzero
amplitude \(\alpha\).  It is not cured by choosing \(|\eta|\leq\rho/t\),
because (0.2) was required as a local norm operation before chronological
step factors were used.  A grammar-specific tree or scale estimate could
attach those factors before taking absolute values; that would be a
different theorem and a different norm architecture.

Accordingly, under the exact qualifications in the question, the status is

\[
 \boxed{\text{OPEN}.}
\]

The first precise failed inequality is (0.2).  The obstruction is genuine
for every fixed same-space norm of the displayed template.  It does not show
that the desired \(Ct^4|\eta|^5\) remainder inequality is false; it shows
that proving it requires a radius-losing, step-weighted, intrinsic source
scale (or a cancellation theorem specific to the paired OMFP DAG), rather
than different numerical choices of \(w_m\) and \(p_m\) in (0.1).

## 9. Quantifier and loophole audit

1. **Width-first order.**  The counterexample is applied to a raw Gaussian
   node of the already established width-first DAG.  No finite-width Taylor
   expansion or limit exchange is used.
2. **All source orders.**  No truncation is made.  The obstruction occurs at
   source order zero, and Section 4 independently tests arbitrarily large
   source order.
3. **Activation class.**  The residual (4.1) satisfies the requested analytic
   envelope and is genuinely nonlinear.  The product obstruction is even
   independent of the residual.
4. **Small amplitude.**  Multiplying every nonlinear high derivative by a
   fixed nonzero \(\alpha\) cannot turn a divergent positive series into a
   convergent one.  The raw-Gaussian product obstruction already holds at
   \(\alpha=0\).
5. **Moment exponents.**  The proof covers every finite \(p_0\), while
   \(p_0=\infty\) excludes initialization.  Exponents at positive source
   orders never enter Theorem 2.2.
6. **Singular Grams.**  Section 5 identifies the mandatory quotient-before-
   norm rule.  The main counterexample does not rely on a nonsingular
   coordinate representation.
7. **Paired cancellation.**  No claim is made that separately bounding
   \(F_{2t}\) and \(F_t\) disproves the theorem.  The audit only rejects the
   proposed generic norm lemma.  A paired-DAG cancellation performed before
   products are normed remains a logically possible alternative.
8. **Depth three.**  Since the connector-local closure already fails at
   \(L=2\), there is no proved estimate to iterate through an additional
   connector.
