# Route C: dyadic summability through response energy

## 0. Verdict

For the exact width-first two-hidden-layer OMFP dynamics, the implication

\[
\sum_{j\ge 0}\frac{B_{2^j}}{2^{5j}}<\infty
\tag{0.1}
\]

is **not presently proved** from the activation assumptions

\[
\phi\in C^{12},\qquad
M_\phi:=\max\left\{1,
\sup_x\frac{|\phi(x)|}{1+|x|},
\max_{1\le r\le 12}\|\phi^{(r)}\|_\infty\right\}<\infty .
\tag{0.2}
\]

The weaker condition (0.1) is nevertheless enough for scalar dyadic
convergence.  It permits considerably more growth than the previously sought
bound \(B_m\lesssim m^4\).  In particular, any bound

\[
B_m\le C_\phi m^{5-\delta},\qquad \delta>0,
\tag{0.3}
\]

on dyadic \(m\) suffices.  A weighted response-energy argument is a plausible
way to prove (0.3), because the exact population dynamics is causal and every
old-source response is multiplied by its step size.  The argument currently
stops at mixed generated/source jets across a reused matrix and its adjoint.
The obstruction already occurs at depth two; the exact additional lemma needed
to transfer the estimate through a third layer is stated in Section 7.

There is also a sharp logical limitation.  Fixed-horizon \(C^5\) regularity,
the correct cubic coefficient, and a finite remainder constant for every
fixed horizon do not imply (0.1).  Section 4 gives an entire scalar family
showing this.  This is a counterexample to that *inference*, not a counterexample
realized by an OMFP network.  No admissible-activation OMFP counterexample is
known here.

The labels **proved**, **conditional**, and **open** below are literal.

## 1. Canonical formulation of the coefficient condition

Let \(F_m(h)\) be the width-first expected output after \(m\) recomputed
gradient steps of size \(h\), and put

\[
\Delta_m(h):=F_{2m}(h)-F_m(2h),
\qquad
D_m(h):=\Delta_m(h)-\kappa_m h^3.
\tag{1.1}
\]

Fix \(\rho>0\).  The coefficient in (0.1) must be made canonical.  Define

\[
b_m^*(\rho):=
\sup_{0<|h|\le \rho/m}\frac{|D_m(h)|}{|h|^5}.
\tag{1.2}
\]

If the interval is contained in the fixed-horizon regularity interval, then
the established fixed-\(m\) theorem makes (1.2) finite.  Moreover,
\(b_m^*(\rho)\) is the least valid fifth-order coefficient on that interval.

This normalization is necessary.  If \(B_m\) is merely said to be *some*
valid coefficient, then replacing it by \(B_m+m^{100}\) preserves the
inequality and destroys summability.  Thus the invariant hypothesis is

\[
\boxed{\displaystyle
\sum_{j\ge0}\frac{b_{2^j}^*(\rho)}{2^{5j}}<\infty,}
\tag{1.3}
\]

or else summability of a particular, completely specified construction which
majorizes \(b_m^*(\rho)\).

## 2. What the weaker hypothesis proves

### Proposition 2.1 (proved: scalar dyadic Cauchy criterion)

Assume, for dyadic \(m\), that

\[
|\kappa_m|\le K_\phi m^2
\tag{2.1}
\]

and (1.3) holds.  Define

\[
G_m(T):=F_m(T/m).
\tag{2.2}
\]

Then \((G_{2^j})_{j\ge0}\) is uniformly Cauchy on every interval
\([-R,R]\) with \(R\le2\rho\).  More precisely,

\[
\|G_{2m}-G_m\|_{L^\infty[-R,R]}
\le \frac{K_\phi R^3}{8m}
+\frac{b_m^*(\rho)R^5}{32m^5}.
\tag{2.3}
\]

#### Proof

Set \(h=T/(2m)\).  Then \(|h|\le\rho/m\), and

\[
G_{2m}(T)-G_m(T)
=F_{2m}(h)-F_m(2h)
=\kappa_m h^3+D_m(h).
\]

Using (1.2), (2.1), and \(|T|\le R\) gives (2.3).  Summing (2.3) over
\(m=2^j\) gives a geometric cubic series and, by (1.3), a convergent
remainder series.  The Weierstrass criterion proves uniform Cauchy convergence.
\(\square\)

Consequently, each of the following explicit estimates is sufficient:

\[
b_m^*(\rho)\le C_\phi m^{5-\delta}
\quad(\delta>0),
\tag{2.4}
\]

or, on dyadics,

\[
b_{2^j}^*(\rho)
\le C_\phi\frac{2^{5j}}{(1+j)^{1+\delta}}.
\tag{2.5}
\]

The borderline estimates \(C m^5\) and
\(C m^5/(1+\log_2m)\) do not imply (1.3).

Proposition 2.1 concerns only the scalar readout.  It neither identifies a
state-space limit nor proves a semigroup law or an IDE.

## 3. The existing explicit compiler coefficient does not satisfy (1.3)

This section concerns the particular majorant constructed in
`temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md`; it makes no claim about
the minimal coefficient (1.2).

For horizon \(N\), that construction has

\[
M_{L,N}=(2N+1)(L-1),\qquad p_N=2C_N,
\]

and

\[
E_{L,N}
=2L p_N^{M_{L,N}}
+r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.
\tag{3.1}
\]

Its activation base obeys \(B_\phi\ge4\), and its positive recursion gives
\(p_N\ge2\).  At depth \(L=2\),

\[
E_{2,N}\ge4\,2^{2N+1}.
\tag{3.2}
\]

The comparison of horizons \(m\) and \(2m\) uses \(N=2m\), so its explicit
coefficient obeys

\[
B_\phi^{E_{2,2m}}
\ge4^{\,4\,2^{4m+1}}.
\tag{3.3}
\]

Therefore

\[
\frac{B_\phi^{E_{2,2^{j+1}}}}{2^{5j}}\longrightarrow\infty.
\tag{3.4}
\]

In particular, the existing compiler majorant cannot prove (1.3).  Since it is
only an intentionally coarse majorant, (3.4) is not evidence that
\(b_m^*(\rho)\) itself grows rapidly.

## 4. Fixed-horizon information alone cannot imply dyadic summability

### Proposition 4.1 (proved: adversarial scalar family)

Let \((\kappa_m)\) be any prescribed real sequence on the positive integers.
There are odd entire functions \(F_m\) such that, for every fixed \(m\),

\[
F_{2m}(h)-F_m(2h)=\kappa_mh^3+R_mh^5,
\tag{4.1}
\]

with finite \(R_m\), while

\[
\sum_{j\ge0}\frac{|R_{2^j}|}{2^{5j}}=\infty.
\tag{4.2}
\]

The functions can also be chosen to have the exact extensive linear law
\(F_m'(0)=m\lambda\), for any fixed \(\lambda\).

#### Proof

Choose arbitrary \(\beta_m\) for odd \(m\), and recursively set

\[
\beta_{2m}:=8\beta_m+\kappa_m.
\tag{4.3}
\]

This defines \(\beta_m\) uniquely for every positive integer.  Let

\[
c_m:=m^6,
\qquad
F_m(h):=m\lambda h+\beta_mh^3+c_mh^5.
\tag{4.4}
\]

The linear terms in \(F_{2m}(h)-F_m(2h)\) cancel.  Equation (4.3) gives the
cubic term \(\kappa_mh^3\), and

\[
R_m=c_{2m}-32c_m=(64-32)m^6=32m^6.
\]

Thus the series in (4.2) equals \(32\sum_{j\ge0}2^j\), which diverges.
For every \(\rho>0\), the canonical modulus (1.2) is exactly
\(b_m^*(\rho)=32m^6\), so this divergence is not caused by inflating a valid
coefficient.
\(\square\)

This proposition respects every scalar conclusion supplied by a fixed-horizon
fifth-order theorem: smoothness, exact first-order cancellation, an arbitrary
prescribed cubic coefficient, and a finite fifth-order constant at every
fixed \(m\).  Hence those conclusions do not logically imply (1.3).

It is important not to overstate the proposition.  The family (4.4) was not
shown to be generated by the OMFP network.  Thus it does **not** disprove
dyadic summability under the full exact-network assumptions.  It proves that a
new horizon-uniform network estimate is indispensable.

## 5. Exact depth-two structure relevant to a response-energy proof

After taking width to infinity at a fixed step sequence
\((\varepsilon_s)\), the inverse-free chronological DAG has the form

\[
a_s=A+\sum_{i<s}\varepsilon_i y_i,
\qquad
u_s=U+\sum_{i<s}\varepsilon_i d_i,
\tag{5.1}
\]

\[
z_s=\xi_s+\sum_{i<s}
(\rho_{si}+\varepsilon_iQ_{is})\delta_i,
\qquad
\delta_s=a_s\phi'(z_s),
\tag{5.2}
\]

\[
r_s=\chi_s+\sum_{i\le s}\sigma_{si}x_i
+\sum_{i<s}\varepsilon_iK_{is}x_i,
\qquad
d_s=r_s\phi'(u_s),
\tag{5.3}
\]

where \(x_s=\phi(u_s)\), \(y_s=\phi(z_s)\); \(Q,K\) are the corresponding
Gram coefficients; and \(\rho,\sigma\) are the adjoint response coefficients
in the fixed chronological realization.  The proven causal divisibility is

\[
\rho_{si}=\varepsilon_i\bar\rho_{si}\quad(i<s),
\qquad
\sigma_{si}=\varepsilon_i\bar\sigma_{si}\quad(i<s),
\tag{5.4}
\]

while the sole current response is

\[
\sigma_{ss}=\mathbb E[a_s\phi''(z_s)].
\tag{5.5}
\]

Thus (5.2)--(5.3) are Volterra equations:

\[
z_s=\xi_s+\sum_{i<s}\varepsilon_i
(Q_{is}+\bar\rho_{si})\delta_i,
\tag{5.6}
\]

\[
r_s=\chi_s+\sigma_{ss}x_s
+\sum_{i<s}\varepsilon_i(K_{is}+\bar\sigma_{si})x_i.
\tag{5.7}
\]

Every historical contribution therefore carries one time weight.  This is the
structural reason a horizon-free estimate at bounded total variation is
plausible.

### Lemma 5.1 (proved: weighted correlated-Gaussian exponential bound)

Let \((G_s)\) be any finite centered jointly Gaussian family with
\(\mathbb E G_s^2\le V^2\).  If \(w_s\ge0\),
\(\tau=\sum_sw_s\), and \(\lambda\ge0\), then

\[
\mathbb E\exp\!\left(\lambda\sum_sw_s|G_s|\right)
\le2\exp\!\left(\frac{\lambda^2\tau^2V^2}{2}\right).
\tag{5.8}
\]

#### Proof

For \(\tau=0\) the claim is immediate.  Otherwise set
\(\alpha_s=w_s/\tau\).  Convexity of the exponential gives

\[
e^{\lambda\sum_sw_s|G_s|}
\le\sum_s\alpha_se^{\lambda\tau|G_s|}.
\]

For a centered Gaussian \(G\) of variance at most \(V^2\),

\[
\mathbb E e^{q|G|}
\le\mathbb E(e^{qG}+e^{-qG})
\le2e^{q^2V^2/2}.
\]

Average this inequality with weights \(\alpha_s\). \(\square\)

Lemma 5.1 requires neither independence nor nonsingularity of the covariance.
Together with (5.6)--(5.7), it controls products generated by scalar causal
Gronwall recurrences whose coefficients are weighted absolute Gaussian fields.

### Where the closure fails

The exact old-source tangent recurrences contain, among others, the products

\[
a_s\phi''(z_s)\,\zeta_s^i,
\qquad
r_s\phi''(u_s)\,p_s^i,
\tag{5.9}
\]

and differentiation in the step parameter produces mixed generated/source
jets of these terms.  A cylindrical derivative with respect to an old formal
source holds all later raw Gaussian actions fixed.  It is therefore not the
same object as the transported parameter tangent, which differentiates future
actions such as \(I x_s\) and \(J\delta_s\) as well.  At singular Gram matrices,
individual source coefficients also depend on the chosen chronological
realization; only the aggregate adjoint response action is intrinsic.

Ordinary Holder estimates applied to (5.9) raise the needed moment order at
each pass.  There is no available ambient estimate

\[
\|J^*X\|_{L^p}\le C_p\|X\|_{L^p},\qquad p>2,
\tag{5.10}
\]

for the reused-matrix adjoint.  Indeed, the fixed-operator construction permits
\(c\in L^2\setminus L^p\), \(X=Jc\), and hence \(J^*X=c\).
Gaussian hypercontractivity does not repair (5.10): after repeated composition
with a non-polynomial \(\phi\), the state is not a Gaussian polynomial of a
horizon-independent chaos degree.  Truncating its chaos expansion introduces
a new tail estimate, which has not been proved uniformly in the horizon.

Thus Lemma 5.1 closes the *scalar weighted transport* part but not the coupled
moving-action/adjoint-response part.  This is the exact depth-two gap.

## 6. A precise sufficient response-energy statement

The following is a conditional bridge, stated to isolate the missing estimate
rather than to hide it in an output modulus.

Fix the chronological population DAG (5.1)--(5.7).  Let
\(\mathcal H_m(h)\) be the finite ledger consisting of:

1. the normalized parameter jets \(m^{-q}\partial_h^qV\), \(0\le q\le3\),
   of the generated fields \(V\in\{a,u,z,r,x,y,d,\delta\}\);
2. the corresponding jets of every **aggregate** response action in
   (5.6)--(5.7);
3. the aggregate contractions of first old-source derivatives with their
   chronological source directions, together with up to three parameter
   derivatives (hence total differential order at most four), that occur when
   the response actions are differentiated; and
4. the transported hybrid direction and its three parameter derivatives in
   the exact coarse-step versus two-fine-step factorization.

This is a finite syntactic ledger for each \(m\): there are \(2m\) time nodes,
one reused connector in its forward and adjoint directions, and only four
derivative levels, so chronological differentiation terminates after finitely
many applications of the product and chain rules.  Crucially, the ledger uses
aggregate response actions, not representation-dependent individual
coefficients at singular covariances.

The exact paired-Euler telescoping identity, with the sign convention (1.1),
is

\[
\Delta_m(h)=h^2Q_m(h),\qquad
Q_m(h)=\sum_{j=0}^{m-1}A_{j,m}(h),
\tag{6.0}
\]

where \(A_{j,m}\) is the \(j\)-th transported local defect.  Both
\(\Delta_m\) and \(Q_m\) are odd.  Expand
\(m^{-3}A_{j,m}'''(h)\) by the product and chain
rules all the way down to entries of \(\mathcal H_m(h)\).  Let
\(\mathfrak E_m(h)\) be the maximum over \(j\) of the sum of the absolute
expectations of the resulting monomials.  This is a finite, deterministic
functional of the activation-state/response ledger.  In particular,

\[
|A_{j,m}'''(h)|\le m^3\mathfrak E_m(h).
\tag{6.0a}
\]

All source-coordinate terms are first recombined into their aggregate adjoint
actions and only then placed inside absolute values.  Reversing those two
operations would make \(\mathfrak E_m\) representation-dependent at singular
Grams and is not allowed.

### WRE\(_\alpha\) (open)

There exist \(\rho_\phi,C_\phi<\infty\) and \(\alpha<1\), depending only on
(0.2), such that, whenever \(|h|\le\rho_\phi/m\),

\[
\mathfrak E_m(h)\le C_\phi m^\alpha.
\tag{6.1}
\]

In constructing \(\mathfrak E_m\), the derivative with respect to \(h\) is
normalized by the powers of \(m\) in item 1, and each causal historical
derivative is paired with its
actual step weight from (5.4), (5.6), or (5.7); no unweighted sum of source
coefficients is permitted.  The left side of (6.1) is a state/response ledger
quantity, not a derivative or continuity modulus of \(F_m\).

By (6.0a)--(6.1),

\[
\sup_{|v|\le\rho_\phi/m}|Q_m'''(v)|
\le C_\phi m^{4+\alpha}.
\tag{6.1a}
\]

Since \(Q_m\) is odd, \(Q_m(0)=Q_m''(0)=0\).  Taylor's theorem and
\(\kappa_m=Q_m'(0)\) give

\[
|D_m(h)|
\le\frac{|h|^5}{6}
\sup_{|v|\le|h|}|Q_m'''(v)|.
\tag{6.1b}
\]

Consequently (6.1) gives the explicit conditional estimate

\[
b_m^*(\rho_\phi)\le \frac{C_\phi}{6}m^{4+\alpha}.
\tag{6.2}
\]

Consequently WRE\(_\alpha\), for any \(\alpha<1\), implies (1.3), since

\[
\sum_{j\ge0}\frac{b_{2^j}^*(\rho_\phi)}{2^{5j}}
\le \frac{C_\phi}{6}\sum_{j\ge0}2^{-(1-\alpha)j}<\infty.
\tag{6.3}
\]

Statement (6.2) is conditional because WRE\(_\alpha\) is open.  It is not an
output-derived assumption: (6.1) is a finite Leibniz--Holder functional of
activation-state and intrinsic response-energy estimates on the explicit DAG.
Proving it requires a coupled causal resolvent estimate for the mixed jets
identified in (5.9), including future moving Gaussian actions.  Lemma 5.1 alone
does not supply that estimate.  In particular, (6.1) must not be replaced by
the superficially similar but circular hypothesis
\(\sup|D_m^{(5)}|\lesssim m^{4+\alpha}\).

The especially clean \(m^4\) remainder corresponds to \(\alpha=0\), but scalar
dyadic convergence needs only \(\alpha<1\).

## 7. Exact third-layer transfer that would be needed

At connector \(a\in\{2,3\}\), the depth-three chronological DAG has the same
Volterra pair

\[
z_{a,s}=\xi_{a,s}+\sum_{r<s}\varepsilon_r
(Q^{a-1}_{rs}+\bar\rho^a_{sr})\delta_{a,r},
\tag{7.1}
\]

\[
r_{a-1,s}=\chi_{a,s}+\sigma^a_{ss}x_{a-1,s}
+\sum_{r<s}\varepsilon_r
(K^a_{rs}+\bar\sigma^a_{sr})x_{a-1,r}.
\tag{7.2}
\]

Thus a depth-two proof would transfer to depth three if one proved the
following connector lemma.

### Connector transfer \(\Gamma_{\phi,a}\) (open)

Suppose the lower-layer ledger contains, for
\(p\in\{2,4,8,16,32\}\) and every parameter/mixed derivative of total order at
most four,

\[
\|\text{generated field}\|_{L^p}
+\|\text{aggregate response action}\|_{L^p}
\le C_{a-1} m^{\alpha_{a-1}},
\qquad \alpha_{a-1}<1,
\tag{7.3}
\]

after the causal step weights are included.  Then the Gaussian conditioning
and adjoint response construction at connector \(a\) should produce the same
ledger upstairs with

\[
C_{a}\le\Gamma_{\phi,a}(C_{a-1}),
\qquad
\alpha_a=\Psi_{\phi,a}(\alpha_{a-1})<1,
\tag{7.4}
\]

where \(\Gamma_{\phi,a}\) and \(\Psi_{\phi,a}\) are independent of horizon and
Gram rank.  The horizon-uniform lemma sought in the earlier work is the
stronger special case \(\Psi_{\phi,a}(0)=0\); for the scalar dyadic criterion it
would be enough to remain strictly below one after the final connector.

The exact new terms to control in this transfer are the upper-layer analogues
of (5.9), together with their mixed jets:

\[
a_{a,s}\phi''(z_{a,s})\zeta_{a,s}^{i},
\qquad
r_{a,s}\phi''(u_{a,s})p_{a,s}^{i},
\tag{7.5}
\]

and the moving raw actions created when a parameter derivative hits future
queries.  A proof must estimate the aggregate adjoint action directly; applying
an ambient \(L^p\) bound for \(J_a^*\) would be invalid by (5.10).

If WRE\(_{\alpha_2}\) were proved at the first connector and the transfer were
proved with \(\alpha_3=\Psi_{\phi,3}(\alpha_2)<1\), then (6.2)--(6.3) would hold
at depth three with exponent \(4+\alpha_3\) and activation/depth coefficient
\(\Gamma_{\phi,3}(C_\phi)/6\).  Neither implication is currently
unconditional.

## 8. Limit-order audit

All quantities above obey the required order of limits:

1. fix an integer \(m\) and a nonzero \(h\);
2. take width \(n\to\infty\) to identify \(F_m(h)\) with the population DAG;
3. establish regularity and estimates on that already identified DAG;
4. only then set \(h=T/m\) and let dyadic \(m\to\infty\).

For each fixed \((m,T)\), \(T/m\) is still fixed during the width limit.  The
scalar Cauchy argument therefore needs no interchange between width and mesh
limits.  Conversely, a finite-width Taylor expansion with \(h=T/m\) followed
by a diagonal \((n,m)\)-limit would not prove Proposition 2.1 for the stated
width-first objects and is not used here.

## 9. Quadratic no-go audit

The canonical raw-square example \(\phi(x)=x^2\) develops a fixed predictor
increase by feature time

\[
(0.09+o(1))/\sqrt{\log n},
\]

so its physical-MSE transition time tends to zero.  It therefore rules out a
general continuous compact-time readout/IDE theorem whose assumptions include
that model.

This no-go does not directly contradict the present route: \(x^2\) violates
(0.2), because it has superlinear growth and an unbounded first derivative.
It does impose two audit constraints:

* no conclusion here may be extended to raw-square without a new mechanism;
* scalar convergence of \(G_m\) cannot by itself be promoted to convergence of
  the full state or to a physical-time IDE.

## 10. Claim ledger

### Proved

* The canonical coefficient is (1.2); arbitrary inflated \(B_m\)'s are not a
  meaningful object for summability.
* The dyadic summability condition (1.3), together with the quadratic cubic
  coefficient bound, gives scalar uniform dyadic convergence by (2.3).
* Growth strictly below \(m^5\), and the logarithmic variant (2.5), suffice.
* The currently recorded explicit compiler majorant fails the summability
  test already at depth two.
* Fixed-horizon scalar regularity and exact cubic matching alone do not imply
  summability (Proposition 4.1).
* The weighted correlated-Gaussian estimate (5.8) is horizon-free and valid at
  singular covariance.

### Conditional

* WRE\(_\alpha\) with \(\alpha<1\) implies
  \(b_m^*\lesssim m^{4+\alpha}\), hence scalar dyadic convergence.
* A rank- and horizon-uniform connector transfer preserving \(\alpha<1\) would
  carry the result from depth two to depth three.

### Open

* WRE\(_\alpha\) for the exact reachable depth-two OMFP population DAG under
  (0.2), for any \(\alpha<1\).
* The connector transfer (7.3)--(7.4), already because of mixed moving-query
  and adjoint-response jets.
* An admissible-activation OMFP counterexample to (1.3).  Proposition 4.1 is
  only a counterexample to deduction from the currently proved scalar
  fixed-horizon statements.
* State-space convergence, a semigroup law, and identification of an IDE from
  the scalar dyadic limit.

## 11. Hostile audit

1. **Coefficient inflation.**  An arbitrary valid \(B_m\) is noncanonical and
   can always be inflated.  Every summability claim in this note therefore uses
   the least modulus (1.2) or a named explicit construction.
2. **Network realizability.**  Proposition 4.1 is not labelled as an OMFP
   counterexample.  It refutes only an inference from fixed-horizon scalar
   conclusions.
3. **Current response.**  The term \(\sigma_{ss}x_s\) in (5.7) is not assigned
   a fictitious step factor.  Only historical responses use (5.4).
4. **Singular Grams.**  No covariance inverse is used.  Source-coordinate
   terms are recombined into aggregate adjoint actions before norms or absolute
   values are taken.
5. **Moving versus cylindrical derivatives.**  The missing moving actions are
   explicitly included in the open ledger; old-source tangents are not
   identified with transported parameter tangents.
6. **Moment closure.**  Lemma 5.1 is used only for weighted Gaussian scalar
   transport.  It is not claimed to imply an ambient \(L^p\) bound for \(J^*\)
   or a horizon-independent hypercontractive estimate.
7. **Remainder algebra.**  The conditional power \(m^{4+\alpha}\) follows from
   the exact factorization (6.0), the explicit normalization (6.0a), a sum of
   exactly \(m\) defects, and Taylor's factor \(1/6\).  It is not obtained by
   assuming a fifth derivative bound on the terminal output.
8. **Limit order.**  Width is taken first for every fixed \((m,h)\).  No
   finite-width Taylor expansion or diagonal width/mesh limit occurs.
9. **Strength of conclusion.**  Proposition 2.1 gives a scalar dyadic limit on
   \(|T|\le2\rho\), not an all-time state limit, semigroup, or IDE.
10. **Quadratic obstruction.**  Raw-square is outside (0.2), so it is neither
    silently included nor dismissed; its no-go result blocks any unjustified
    extension of the conclusion.

After these checks, the unconditional result remains Proposition 2.1 plus the
negative logical statements of Sections 3--5.  WRE\(_\alpha\) and the
third-layer transfer remain open.
