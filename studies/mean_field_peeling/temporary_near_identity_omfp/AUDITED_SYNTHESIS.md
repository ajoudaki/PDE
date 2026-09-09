# Audited synthesis: the near-identity nonlinear homotopy

Date: 25 August 2026.

## 1. Final verdict

The homotopy

\[
 \psi_{\alpha,\varphi}(x)
 =\frac{x+\alpha\varphi(x)}
 {\|G+\alpha\varphi(G)\|_2},
 \qquad G\sim N(0,1),
 \tag{1.1}
\]

is a strong research direction, but it does not presently prove a fixed
nonzero nonlinear neighborhood with the uniform depth-two remainder

\[
 \left|
 F_{2t,2}(h)-F_{t,2}(2h)-\kappa_{\alpha,2,t}h^3
 \right|
 \le C_{\varphi,2}t^4|h|^5,
 \qquad |h|t\le\rho_{\varphi,2}.
 \tag{1.2}
\]

What is proved is:

1. normalization and a genuine explicit nonlinear activation class;
2. explicit Lipschitz openness of the exact cubic Gaussian invariant at
   every fixed depth, including \(L=2,3\);
3. an exact arbitrary-activation fifth-jet theorem: the fifth
   step-doubling coefficient is a polynomial of degree at most four in
   \(t\), with terminating Gaussian-integral and activation-envelope
   constants;
4. failure of ambient \(C^2(L^2,L^2)\) Nemytskii/Frechet smoothness, and
   discontinuity of that \(C^2\) seminorm at the identity;
5. insufficiency of fixed-horizon continuity, even analyticity, for the
   time-refinement problem;
6. coefficientwise algebraic triangularity at each fixed finite schedule and
   fixed finite marked expression; and
7. a precise identification of the missing all-source-order
   aggregate-adjoint estimate.

Two independent audits rejected the attempted proof of that last estimate.
Consequently, (1.2) remains open for every proved genuinely nonlinear class.
The same is true at \(L=3\).

Every network quantity in this note uses the required order of limits:

\[
 F_{N,L}^{(\alpha)}(h)
 =\lim_{n\to\infty}F_{N,L,n}^{(\alpha)}(h)
 \quad\text{at fixed }(N,h,\alpha),
 \tag{1.3}
\]

and only the already identified width-first DAG is subsequently expanded in
\(h\) or \(\alpha\).  No finite-width Taylor expansion or diagonal
width/mesh limit is used.

## 2. What had and had not been tried

A normalized residual-sine activation had previously been selected as the
cleanest perturbative candidate for the depth-three IDE problem.  That work
proved that two shortcuts fail: its nonlinear correction survives at fixed
nonzero amplitude after the width limit, and the full finite-width
sensitivity is not dimension-uniform.

The present amplitude-triangular, horizon-weighted OMFP program had not been
closed.  The new work below develops that formulation and audits its first
two proposed closures.

## 3. Unconditional nonlinear openness of the cubic coefficient

Let

\[
 \varphi\in C^{12}(\mathbb R),\qquad
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R,
 \qquad |\alpha|R\le\frac14,
 \qquad \varphi''\not\equiv0.
 \tag{3.1}
\]

Then

\[
 \frac34\le \|G+\alpha\varphi(G)\|_2\le\frac54,
 \tag{3.2}
\]

and \(\psi_{\alpha,\varphi}\) is genuinely nonlinear for
\(\alpha\ne0\).  Let \(J_{\psi,L}\) be the exact nine-Gaussian-moment cubic
invariant of the width-first OMFP DAG.  The finite interval compiler in
`CUBIC_OPENNESS.md` gives a numerical, terminating constant \(\mathcal L_L\)
such that

\[
 \boxed{
 |J_{\psi_{\alpha,\varphi},L}-J_{\mathrm{id},L}|
 \le\mathcal L_L|\alpha|R,}
 \tag{3.3}
\]

where

\[
 J_{\mathrm{id},L}=\frac{2L(L+1)^2(L+2)}3.
 \tag{3.4}
\]

Hence

\[
 0<|\alpha|<\min\left\{
 \frac1{4R},
 \frac{J_{\mathrm{id},L}}{2R\mathcal L_L}
 \right\}
 \tag{3.5}
\]

implies

\[
 J_{\psi_{\alpha,\varphi},L}
 \ge\frac12J_{\mathrm{id},L}>0.
 \tag{3.6}
\]

In particular,

\[
 J_{\mathrm{id},2}=48,
 \qquad J_{\mathrm{id},3}=160.
 \tag{3.7}
\]

The same compiler gives the fully numerical sufficient choices

\[
 0<|\alpha|<\frac{24}{85475R}\quad(L=2),
 \qquad
 0<|\alpha|<\frac{80}{8610421R}\quad(L=3)
 \tag{3.7a}
\]

for the conclusion \(J_{\psi_{\alpha,\varphi},L}\ge
J_{\mathrm{id},L}/2\).  These constants are intentionally coarse.

With the convention

\[
 \Delta_{t,L}(h)=F_{2t,L}(h)-F_{t,L}(2h),
\]

the exact cubic coefficient is

\[
 \kappa_{\alpha,L,t}
 =\frac{t(2t-1)}2J_{\psi_{\alpha,\varphi},L}.
 \tag{3.8}
\]

Thus a genuine nonlinear open interval is proved for the cubic term.  This
does not imply an open interval for the fifth remainder.

### 3.1 The exact fifth coefficient is already quartic in time

The near-identity continuity argument is unnecessary at the level of the
exact fifth Taylor coefficient.  For every admissible activation and every
separately fixed finite depth, put

\[
 \Delta_{t,L}(h)=F_{2t,L}(h)-F_{t,L}(2h).
\]

The width-first marked Euler construction proves

\[
 \boxed{
 [h^5]\Delta_{t,L}(h)
 =\sum_{m=1}^5
 \left\{{2t\choose m}-32{t\choose m}\right\}
 \Theta_{5,m}(\phi,L).}
 \tag{3.9}
\]

The five \(\Theta_{5,m}\) are finite differences of the signed
singular-Price jets at the fixed horizons \(1,\ldots,5\), hence explicit
Gaussian activation integrals constructed before derivative identification.
The degree-five term cancels, so (3.9) has degree at most four in \(t\).  The
independently audited estimate is

\[
 \boxed{
 |[h^5]\Delta_{t,L}(h)|
 \le C^{\mathrm{loc}}_{\phi,L}t^4
 \le\frac{227}{180}B_\phi^{E_{L,5}}t^4.}
 \tag{3.10}
\]

For the normalized residual class (3.1), \(B_\psi=4\), so the right side is
uniform in every \(0<|\alpha|R\le1/4\), at \(L=2\), \(L=3\), and every
fixed \(L\).  Thus the requested positive polynomial result for the exact
\(h^5\) coefficient is proved, with exponent \(4\), not merely \(5\).

This does not prove (1.2): (3.10) controls the fifth derivative at the
single point \(h=0\), whereas (1.2) controls the whole interval
\(|h|\le\rho/t\).  Higher odd jets can still affect that interval.  The
proof and independent audits are in `FIFTH_JET_POLYNOMIAL_THEOREM.md`,
`FIFTH_JET_POLYNOMIAL_INDEPENDENT_AUDIT.md`, and
`ORDER5_WIDTH_FIRST_ARTIFACT_AUDIT.md`.

## 4. Why ordinary continuity cannot prove the desired theorem

### 4.1 Ambient \(C^2(L^2,L^2)\) Nemytskii obstruction

Let \(N_\alpha(u)=\psi_{\alpha,\varphi}\circ u\) on a nonatomic Gaussian
probability space.  If \(\varphi''\not\equiv0\), choose an interval \(I\)
and \(c>0\) on which \(|\varphi''|\ge c\).  For a Gaussian field \(Z\),
choose \(E_m\subset\{Z\in I\}\) with probability \(p_m\downarrow0\), and
put

\[
 v_m=w_m=p_m^{-1/2}{\bf1}_{E_m}.
\]

Then \(\|v_m\|_2=\|w_m\|_2=1\), while any second Frechet derivative would
have to satisfy

\[
 D^2N_\alpha(Z)[v_m,w_m]
 =\frac{\alpha}{\|G+\alpha\varphi(G)\|_2}
   \varphi''(Z)v_mw_m.
\]

Therefore

\[
 \|D^2N_\alpha(Z)[v_m,w_m]\|_2
 \ge
 \frac{|\alpha|c}{\|G+\alpha\varphi(G)\|_2}p_m^{-1/2}
 \longrightarrow\infty.
 \tag{4.1}
\]

At \(\alpha=0\), the same second derivative is zero.  Thus the ambient
\(C^2(L^2,L^2)\) seminorm jumps from zero to infinity.  The proved identity
Banach theorem is not open in this topology.

### 4.2 The quantifier obstruction

Define the least remainder coefficient

\[
 b_{t,L}^{(\alpha)}(\rho)
 =\sup_{0<|h|\le\rho/t}
 \frac{|\Delta_{t,L}^{(\alpha)}(h)
       -\kappa_{\alpha,L,t}h^3|}{|h|^5}.
 \tag{4.2}
\]

One convenient sufficient condition for absolute scalar dyadic convergence
is

\[
 \sum_{j\ge0}2^{-5j}b_{2^j,L}^{(\alpha)}(\rho)<\infty,
 \tag{4.3}
\]

provided also that the explicit cubic coefficient obeys
\(|\kappa_{t,L}^{(\alpha)}|\lesssim t^2\).  Indeed, at
\(t=2^j\), \(h=T/(2t)\), and \(|T|\le2\rho\), the cubic increments are
\(O(2^{-j})\), while (4.3) makes the fifth-order increments summable.

Analyticity of \(b_t(\alpha)\) for every fixed \(t\), together with
\(b_t(0)\lesssim t^4\), does not imply (4.3) on any common interval.  The
entire scalar witness

\[
 b_t(\alpha)=t^4e^{\alpha^2t^2}
 \tag{4.4}
\]

has both fixed-\(t\) properties but violates (4.3) for every
\(\alpha\ne0\).  This is a logical counterexample, not an OMFP output.

Thus continuity into the horizon-weighted sequence space

\[
 \ell^1_5=\left\{(q_j):\sum_j2^{-5j}|q_j|<\infty\right\},
 \tag{4.5}
\]

is one sufficient formulation.  A more primitive and noncircular route is
an OMFP response norm which implies (4.5).  Neither formulation is asserted
to be necessary.

## 5. The exact favorable triangularity

For the analytic route assume the explicit Bernstein residual class

\[
 \|\varphi^{(r)}\|_\infty\le MA^r,
 \qquad r\ge0,
 \qquad \varphi''\not\equiv0.
 \tag{5.1}
\]

This includes scaled finite Fourier sums, such as \(\sin x\).  Write

\[
 \mathcal E_\rho(\psi)
 :=\sum_{r=2}^{\infty}
   \frac{\rho^r}{r!}\|\psi^{(r)}\|_\infty.
 \tag{5.1a}
\]

This is a purely activation-defined analytic curvature energy: it vanishes
for the identity (and, more generally, affine activations).  For the
near-identity family, \(|\alpha|M\le1/4\) gives

\[
 \boxed{
 \mathcal E_\rho(\psi_{\alpha,\varphi})
 \le \frac43|\alpha|M
 \bigl(e^{A\rho}-1-A\rho\bigr).}
 \tag{5.1b}
\]

Indeed, every derivative of order \(r\ge2\) equals
\(c_\alpha\alpha\varphi^{(r)}\), with \(c_\alpha\le4/3\).  Thus
\(\mathcal E_\rho\) is the correct local measure of nonlinear insertions.
The analysis below proves that it is not, by itself, a proved global
response energy: reused adjoints create an unbounded source-order hierarchy.

Write

\[
 c_\alpha=\|G+\alpha\varphi(G)\|_2^{-1}
 =\sum_{j\ge0}c_j\alpha^j,
 \qquad V_\alpha=\sum_{k\ge0}\alpha^kV^{\langle k\rangle}.
\]

At one activation node,

\[
 [\alpha^k]\psi_\alpha(V_\alpha)
 =\sum_{j=0}^kc_jV^{\langle k-j\rangle}
 +\sum_{j=0}^{k-1}c_j
   [\alpha^{k-1-j}]\varphi(V_\alpha).
 \tag{5.2}
\]

The second sum uses only amplitude orders below \(k\).  Since \(c_0=1\),
the order-\(k\) unknown enters only through the identity linear term.
For each fixed finite schedule and each fixed finite marked cylindrical
expression, coefficient extraction commutes with the fixed raw Gaussian
maps, their true adjoints, normalized mesh differentiation, and the
transported-defect mark.  Consequently its formal order-\(k\) expression has
the triangular form

\[
 \mathcal L^{\langle k\rangle}
 =\mathcal R_{\mathrm{id}}
 \mathcal S_k(\mathcal L^{\langle0\rangle},\ldots,
              \mathcal L^{\langle k-1\rangle}).
 \tag{5.3}
\]

This is the main positive reason the proposal has a good chance: the
nonlinear highest-order block never appears in the lower-order forcing.  The
identity-background linear response operator appears at every amplitude
order.  Its Hilbert-state part is solved, but its all-source marked resolvent
bound is not.

Equation (5.3) is an algebraic triangularity statement.  It does not bound
the all-order source-response hierarchy.

## 6. The exact surviving obstruction

For a cylindrical generated field

\[
 V=f(Jb_1,\ldots,Jb_m),
\]

the intrinsic reused-adjoint identity is

\[
 J^*V=\mathbb E[\mathscr D_JV]
 =\sum_{i=1}^m\mathbb E[\partial_i f]\, b_i.
 \tag{6.1}
\]

The aggregate vector on the right must be formed before taking norms; this
is essential at singular source Grams.  If the input already has a source
mark, then

\[
 J^*(D_\zeta V)=\mathbb E[\mathscr D_JD_\zeta V],
 \tag{6.2}
\]

which contains a second source derivative.  Repeating the exact adjoint
reduction creates all source orders.  A finite one-source ledger is not
closed.

The first concrete nonlinear susceptibility that the present proof cannot
bound is

\[
 \frac12\varphi''(z^{\langle0\rangle})
       (J^*x^{\langle1\rangle})^2.
 \tag{6.3}
\]

It requires, including all moving-query versions,

\[
 \sup_{\substack{t\ge1,\ s\le2t\\|h|t\le\rho}}
 \left\|
 t^{-q}\partial_h^q\partial_\lambda^r
 J^*x_s^{\langle1\rangle}
 \right\|_4<\infty,
 \quad 0\le q\le3,\quad r\in\{0,1\},
 \tag{6.4}
\]

together with its source-marked aggregate descendants.  There is no ambient
substitute: if \(c\in L^2\setminus L^4\) and \(X=Jc\), then \(X\) is
Gaussian but

\[
 J^*X=c\notin L^4.
 \tag{6.5}
\]

Thus (6.4) has to use the special reachable chronology.

## 7. Why the proposed analytic norms do not yet close it

The graded moment scale

\[
 \mathsf G_0=L^\infty,
 \qquad
 \|X\|_{\mathsf G_D}
 =\sup_{p\ge2}\frac{\|X\|_p}{(Dp)^{D/2}},
 \qquad D\ge1,
 \tag{7.1}
\]

has an exact product theorem: if \(d_i\ge1\) and
\(D=\sum_id_i\), then

\[
 \left\|\prod_iX_i\right\|_{\mathsf G_D}
 \le\prod_i\|X_i\|_{\mathsf G_{d_i}}.
 \tag{7.2}
\]

This resolves the old Holder exponent tower.  The scale itself does not
retain provenance; the enriched expression ledger must separately retain
each opposite-layer pointer.  With that enrichment, the calculus does not
make the false inference in (6.5).

Its general degree-collapse bound is

\[
 |\mathbb EX|\le(2D)^{D/2}\|X\|_{\mathsf G_D}.
 \tag{7.3}
\]

For \(X=G^D\), this has the correct superexponential order.  The available
grammar bound permits stochastic degree proportional to amplitude order.
Without an additional contraction estimate, a geometric bound in (7.1)
therefore does not yield a geometric bound after the Gram/response
expectations are formed.

A finite Fourier restriction does not remove this problem.  For
\(\lambda\ne0\),

\[
 e^{i\lambda G}
 =e^{-\lambda^2/2}
   \sum_{m\ge0}\frac{(i\lambda)^m}{m!}H_m(G),
 \tag{7.4}
\]

so every nonconstant Fourier residual has infinitely many Hermite chaoses.
More generally, any continuous at-most-linear function with finite Gaussian
chaos is affine.  Hence there is no genuinely nonlinear finite-chaos
subclass compatible with the activation assumptions.

## 8. A candidate sufficient next conjecture

Let \(\mathfrak T_{N,k,q}^{(2)}\) denote the trees that a future complete
recursive provenance compiler would generate from the exact depth-two
width-first DAG at amplitude order \(k\), normalized mesh order
\(t^{-q}\partial_h^q\), \(q\le3\), one transported-defect mark, and every
source order generated by (6.1).  At singular Grams, opposite-layer vectors
must first be combined in the intrinsic aggregate quotient and only then
normed.  Let \(D(T)\) be stochastic degree, with
\((2D)^{D/2}=1\) at \(D=0\); let \(w_T\) include the actual chronological
step weights, normalization coefficients, Taylor factorials, deterministic
identity kernels, and local contraction factors; and let \(g_T\) be the
product of the activation/Gaussian leaf norms.

The candidate asserts the existence of explicit

\[
 \tau=\tau(M,A)>0,
 \qquad C_0=C_0(M,A)<\infty,
 \qquad C_1=C_1(M,A)<\infty,
\]

also allowed to use the fixed numerical identity depth-two constants, such
that the factorial response-contraction estimate

\[
 \boxed{
 \sup_{N\ge1}\sup_{\sum_s|e_s|\le\tau}
 \sum_{T\in\mathfrak T_{N,k,q}^{(2)}}
 (2D(T))^{D(T)/2}|w_T|g_T
 \le C_0C_1^k,
 \quad k\ge0, q\le3.}
 \tag{FRC_2}
\]

The constants would have to be explicit functions only of \((M,A)\),
numerical Gaussian moments, and the identity depth-two constants.  This is
intended as an internal OMFP tree estimate, not an output modulus.  It is
currently a schematic conjectural target: the recursive tree compiler and a
domination lemma covering every intermediate Gaussian action, aggregate
adjoint contraction, and macro-defect node have not been constructed.

If that compiler, its domination lemma, and \(\mathrm{FRC}_2\) are all
proved, the expected radius is

\[
 |\alpha|\le
 \min\left\{\frac1{4M},\frac1{2C_1}\right\},
 \tag{8.1}
\]

because the resulting geometric ledger series would be bounded by
\(2C_0\).  The domination lemma would then permit substitution into the
already proved transported macro-defect recursion, producing an explicit
activation-only constant \(C(M,A,C_0,C_1,\tau)\) in (1.2), with the
explicit mesh radius

\[
 \rho_{\varphi,2}=\tau/4.
\]

This is a conditional proof program, not a completed implication in the
present artifact.

The essential new gain must combine three structures which none of the
current estimates combines:

1. chronological simplex factorials from step-divisible histories;
2. Wick/Gaussian contraction factorials when responses become expectations;
3. aggregate grouping before norms at singular reused-matrix Grams.

## 9. Depth three

The amplitude triangularity (5.3) and product theorem (7.2) remain valid at
\(L=3\).  There are now two reused connectors, and provenance trees can
alternate between their two adjoint pairs.  This proof route would require
an \(\mathrm{FRC}_3\)-type estimate stable under that alternation.  No argument
currently transfers \(\mathrm{FRC}_2\) to the second connector without
assuming the missing factorial gain.

Therefore:

* nonlinear cubic openness is proved at \(L=3\);
* the uniform nonlinear fifth remainder is open already at \(L=2\); and
* no unconditional \(L=3\) remainder or IDE consequence follows yet.

## 10. Audit record

The following proposed closures were rejected:

1. perturbation through an ambient \(C^2(L^2,L^2)\) Frechet seminorm;
2. fixed-\(t\) coefficient continuity or analyticity;
3. multiplying an unproved ambient adjoint norm by small \(|\alpha|\);
4. a finite Fourier/finite-chaos state closure;
5. a finite one-source response ledger; and
6. the claimed Volterra passage from a schematic aggregate expansion to a
   row-summed Gronwall inequality.

The last failure is specific: the proof neither included the second and
higher source derivatives created by (6.2), nor derived the required
source-row sums.  Its constant \(\Lambda\) therefore encoded the missing
theorem.

The near-identity proposal is consequently **promising but unproved** for
the desired nonlinear remainder class.  Its sharp value is that it supplies
\(\mathrm{FRC}_2\) as a concrete sufficient conjectural subproblem, while
giving an unconditional nonlinear openness theorem for the cubic invariant.
