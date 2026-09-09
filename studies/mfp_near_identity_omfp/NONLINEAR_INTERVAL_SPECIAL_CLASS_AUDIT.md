# Nonlinear interval-remainder special-class audit

Date: 25 August 2026.

## 1. Verdict

Let

\[
 \Delta_{t,L}(h)=F_{2t,L}(h)-F_{t,L}(2h),
 \qquad t\in\mathbb N,
 \tag{1.1}
\]

where width is taken to infinity at each fixed finite \((t,h)\) before
anything is differentiated in \(h\).  Two distinct statements must not be
conflated.

1. For every normalized activation in the weighted \(C^{12}\) class, the
   exact coefficient \([h^5]\Delta_{t,L}\) is an activation-defined
   polynomial of degree at most four in \(t\).  This is unconditional.
2. For a fixed genuinely nonlinear activation, no proof currently gives a
   polynomial-in-\(t\) bound for the full interval remainder
   \[
    \sup_{0<|h|\le \rho/t}
    \frac{|\Delta_{t,2}(h)-\kappa_{t,2}h^3|}{|h|^5}.
    \tag{1.2}
   \]

The search below finds no admissible nonlinear finite-dimensional closure
that repairs the second problem.  Finite Fourier, finite chaos, polynomial,
Bernstein, and finite provenance restrictions either reduce to the affine
case or fail to close at a nonzero step.  The strongest unconditional
nonlinear interval theorem presently available has an explicit but
super-polynomial horizon constant.  Thus the polynomial interval theorem is
still open already at \(L=2\), and consequently at \(L=3\).

This is a statement about what the proved OMFP machinery establishes.  It is
not a counterexample to the underlying nonlinear interval conjecture.

## 2. The two unconditional results

Assume

\[
 \psi\in C^{12}(\mathbb R),\qquad
 \mathbb E\psi(G)^2=1,
 \tag{2.1}
\]

and

\[
 M_\psi=
 \max\left\{
 1,\sup_x\frac{|\psi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\psi^{(r)}\|_\infty
 \right\}<\infty,
 \qquad B_\psi=\max\{4,M_\psi\}.
 \tag{2.2}
\]

### 2.1 Exact fifth jet

The width-first singular-Price compiler and the marked temporal/static
intertwining give five Gaussian activation numbers
\(\Theta_{5,m}(\psi,L)\), \(1\le m\le5\), such that

\[
 [h^5]F_{N,L}(h)
 =\sum_{m=1}^5 {N\choose m}\Theta_{5,m}(\psi,L).
 \tag{2.3}
\]

Hence

\[
 [h^5]\Delta_{t,L}(h)
 =\sum_{m=1}^5
 \left\{{2t\choose m}-32{t\choose m}\right\}
 \Theta_{5,m}(\psi,L).
 \tag{2.4}
\]

The degree-five part cancels.  In particular, the audited numerical
envelope is

\[
 \boxed{
 |[h^5]\Delta_{t,L}(h)|
 \le \frac{227}{180}B_\psi^{E_{L,5}}t^4.}
 \tag{2.5}
\]

Here \(E_{L,5}\) is the terminating activation-envelope exponent of the
fixed-horizon Price compiler.  Equation (2.5) is a theorem about
\(\Delta_{t,L}^{(5)}(0)/5!\), not about the value of a fifth derivative
away from zero.

### 2.2 Full interval, fixed-horizon compiler

For every fixed \(t\), the same width-first compiler proves

\[
 \boxed{
 |\Delta_{t,L}(h)-\kappa_{t,L}h^3|
 \le B_\psi^{E_{L,2t}}|h|^5,
 \qquad |h|\le\tfrac12.}
 \tag{2.6}
\]

Here

\[
 \kappa_{t,L}=\frac{t(2t-1)}2J_{\psi,L}
 \tag{2.6a}
\]

is the already constructed Gaussian activation integral in the orientation
(1.1).

The constant is explicit and activation-defined.  At depth two,

\[
 E_{2,N}
 =4p_N^{2N+1}
 +r_N\frac{p_N^{2N+1}-1}{p_N-1},
 \tag{2.7}
\]

where the displayed finite integer recursion in
`temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md`, Section 5, defines
\(p_N=2C_N\) and \(r_N=C_N+\alpha_N\).  In particular \(p_N\ge2\), so

\[
 E_{2,2t}\ge4\,2^{4t+1}.
 \tag{2.8}
\]

Thus the available certificate in (2.6) is not polynomial in \(t\).  This
does not show that the true least constant is large; it shows exactly why
the current fixed-horizon compiler does not prove (1.2).

For the normalized near-identity family

\[
 \psi_{\alpha,\varphi}(x)
 =\frac{x+\alpha\varphi(x)}
 {\|G+\alpha\varphi(G)\|_2},
 \qquad
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R,
 \qquad |\alpha|R\le\tfrac14,
 \tag{2.9}
\]

one has \(B_{\psi_{\alpha,\varphi}}=4\).  Consequently both (2.5) and
(2.6) are unconditional for a genuine nonlinear class when
\(\alpha\ne0\) and \(\varphi''\not\equiv0\).  Only (2.5) has polynomial
horizon dependence.

## 3. Why the exact jet does not imply the interval theorem

The implication fails as a matter of logic, even for odd entire scalar
families.  Let \(q_t\) be any quartic polynomial and define

\[
 H_t(h)=\kappa_t h^3+q_t h^5+e^t h^7.
 \tag{3.1}
\]

Then

\[
 [h^5]H_t=q_t=O(t^4),
 \tag{3.2}
\]

while at \(h=\rho/t\),

\[
 \frac{|H_t(h)-\kappa_t h^3|}{|h|^5}
 \ge \frac{e^t\rho^2}{t^2}-|q_t|.
 \tag{3.3}
\]

No polynomial in \(t\) bounds the right-hand side.  This is a proof-route
falsifier, not a claim that \(H_t\) is an OMFP output.  It proves that no
argument using only jets through order five can establish (1.2).

The OMFP distinction is equally concrete.  At \(h=0\), the Euler state
does not move.  A coefficient of scalar order five can mark at most five
update slices, so chronological choices are counted by
\({N\choose m}\), \(m\le5\).  At \(h\ne0\), the same marked insertions are
transported through all the unmarked Jacobians

\[
 I+hD\mathbf g(\theta_s),
 \qquad 0\le s<N.
 \tag{3.4}
\]

Polynomial counting of the marked positions does not bound the product in
(3.4).  One needs a generated-core estimate of the form

\[
 \|I+hD\mathbf g(\theta_s)\|_{\mathrm{reach}}
 \le1+C_\psi|h|,
 \tag{3.5}
\]

together with its mixed source/step and local-defect analogues.  The
aggregate-adjoint estimate needed to prove (3.5) is the unresolved depth-two
bridge.

## 4. No genuinely nonlinear finite-chaos subclass

### Proposition 4.1

If \(f:\mathbb R\to\mathbb R\) is continuous, has at most linear growth,
and \(f(G)\) belongs to a finite sum of one-dimensional Wiener chaoses, then
\(f\) is affine.

#### Proof

A finite sum of the first \(M\) one-dimensional Gaussian chaoses is the
space of polynomials in \(G\) of degree at most \(M\).  Hence
\(f(G)=P(G)\) almost surely for such a polynomial \(P\).  The Gaussian
density is positive everywhere, so continuity gives \(f=P\) on all of
\(\mathbb R\).  At-most-linear growth forces \(\deg P\le1\). \(\square\)

Thus finite chaos cannot supply the requested genuinely nonlinear class.

## 5. No finite multiplicative function algebra

Finite closure under ordinary derivatives is insufficient because every
nonlinear activation node also creates products.  There is a stronger
obstruction to a finite exact product algebra.

### Proposition 5.1

Let \(\mathcal A\subset C(\mathbb R)\) be a finite-dimensional unital
algebra under pointwise multiplication.  Every \(f\in\mathcal A\) is
constant.

#### Proof

Multiplication by \(f\) is a linear endomorphism \(M_f\) of the
finite-dimensional space \(\mathcal A\).  Its characteristic polynomial
\(p\) satisfies \(p(M_f)=0\).  Applying this identity to the unit function
gives

\[
 p(f(x))=0\qquad(x\in\mathbb R).
 \tag{5.1}
\]

Therefore the connected set \(f(\mathbb R)\) is contained in the finite
root set of \(p\), and hence is a singleton. \(\square\)

This rules out an exact finite algebra of activation atoms, their products,
and constants.  It does not rule out an infinite analytic scale.

## 6. Finite Fourier is destroyed by one nonzero-step smoothing

The fact that derivatives of sine and cosine stay in a two-dimensional
space only helps at a fixed Taylor order.  It does not give a positive-step
state closure.

Take the scalar Gaussian smoothing operator suggested by the OMFP
peeling heuristic,

\[
 (\mathcal P_h f)(x)=\mathbb E_A f(x+hA f(x)),
 \qquad A\sim N(0,1).
 \tag{6.1}
\]

For \(f(x)=\sin x\), Gaussian integration gives exactly

\[
 (\mathcal P_h f)(x)
 =\sin x\exp\!\left(-\frac{h^2}{2}\sin^2x\right)
 =e^{-h^2/4}\sin x
   \exp\!\left(\frac{h^2}{4}\cos2x\right).
 \tag{6.2}
\]

For every \(h\ne0\), the final exponential has infinitely many Fourier
coefficients.  Indeed, for \(u>0\),

\[
 e^{u\cos2x}
 =\sum_{k\in\mathbb Z}I_{|k|}(u)e^{2ikx},
 \qquad
 I_k(u)=\sum_{j=0}^{\infty}
 \frac{(u/2)^{2j+k}}{j!(j+k)!}>0.
 \tag{6.3}
\]

Thus even after the top Gaussian variable has been integrated out, a single
nonzero-step operator leaves every finite Fourier space.  Therefore the
proposed scalar peeling operators already have no finite-Fourier invariant
class.  In the actual moving-query DAG, finite Fourier labels still make
each fixed-order Gaussian integral explicit, but no exact invariant
positive-step Fourier state has been established.

Polynomial residuals do not help: the growth condition makes every
polynomial activation affine.  A Bernstein polynomial composed with a
bounded compactifying map is admissible, but it is a nonpolynomial Gaussian
functional and has infinitely many Hermite chaoses by Proposition 4.1.

## 7. A finite source/provenance ledger cannot be exact

Let \(J\) be an isonormal source and \(c\ne0\).  For a smooth nonlinear
atom,

\[
 \mathscr D_J^r\{\varphi(Jc)\}
 =\varphi^{(r)}(Jc)c^{\otimes r}.
 \tag{7.1}
\]

For sine, every order in (7.1) is nonzero.  Moreover the intrinsic aggregate
adjoint identity is

\[
 J^*V=\mathbb E[\mathscr D_JV].
 \tag{7.2}
\]

Applying (7.2) to an already source-marked moving query creates the next
source order.  Hence no fixed finite source-order ledger is invariant under
arbitrarily many reused-matrix adjoint operations.  This remains true for a
finite Fourier residual.

At the exact fifth jet, only finitely many update insertions survive and a
finite ledger closes.  At a nonzero step, the undifferentiated transported
state already contains all prior updates, so in this repeated-adjoint
representation the maximum response order is not bounded by five.  This is
the precise structural reason the fixed fifth-jet compiler terminates while
the proposed positive-step finite ledger does not.

## 8. Quantitative audit of the near-identity homotopy

Suppose a perturbative estimate treats every nonlinear step as an
unweighted factor \(1+C|\alpha|\).  After \(t\) steps it gives

\[
 (1+C|\alpha|)^t\le e^{C|\alpha|t}.
 \tag{8.1}
\]

Keeping this below \(t^q\) forces

\[
 |\alpha|\le \frac{q\log t}{Ct},
 \tag{8.2}
\]

which gives no fixed nonlinear interval.  By contrast, the correctly
weighted Euler estimate

\[
 1+C|\alpha||h|
 \tag{8.3}
\]

accumulates to at most \(e^{C|\alpha|t|h|}\), uniformly bounded on
\(|h|t\le\rho\).  Thus small fixed \(\alpha\) can work only if every
moving-query and aggregate-adjoint response retains its causal factor of
\(h\).  Fixed-\(t\) continuity in \(\alpha\), even real analyticity for
each \(t\), does not prove that weighted estimate.

There is also no perturbation theorem in the ambient
\(C^2(L^2,L^2)\) norm.  If \(\varphi''\not\equiv0\), the second derivative
of the Nemytskii map at a Gaussian field would be

\[
 (v,w)\longmapsto
 \frac{\alpha}{\|G+\alpha\varphi(G)\|_2}
 \varphi''(Z)vw.
 \tag{8.4}
\]

On a nonatomic Gaussian space choose sets \(E_m\) of probabilities
\(p_m\downarrow0\) inside an interval where \(|\varphi''|\ge c>0\), and
put \(v_m=w_m=p_m^{-1/2}{\bf1}_{E_m}\).  Their \(L^2\) norms equal one,
whereas the \(L^2\) norm of (8.4) is at least a constant times
\(|\alpha|p_m^{-1/2}\).  It is infinite as a bilinear operator for every
\(\alpha\ne0\), while it is zero at \(\alpha=0\).  The relevant ambient
operator seminorm is therefore discontinuous at the identity.

This obstruction does not disprove generated-core continuity.  It proves
that such continuity must be established intrinsically on the exact
reachable OMFP queries.

## 9. Best surviving nonlinear candidate

A small finite-Fourier residual, especially a shifted sine

\[
 \psi_{\alpha}(x)
 =\frac{x+\alpha(c+\sin x)}
 {\|G+\alpha(c+\sin G)\|_2},
 \tag{9.1}
\]

remains a useful candidate because all local scalar derivatives and their
Gaussian integrals are explicit.  It does not, by itself, prove a theorem.
The first unresolved depth-two estimate already contains

\[
 \sup_{\substack{s\le2t,\ |h|t\le\rho\\0\le q\le3}}
 t^{-q}
 \left\|\partial_h^q J^*x_s^{\langle1\rangle}\right\|_4<\infty,
 \tag{9.2}
\]

together with the one-source-marked aggregate versions.  Here
\(x_s^{\langle1\rangle}\) is the first activation-amplitude coefficient on
the exact identity-background recursion.  A proof of (9.2) must exploit
reachable-query provenance; there is no ambient substitute.  For example,
if \(c\in L^2\setminus L^4\), then \(X=Jc\) has a perfectly valid Gaussian
source representation but

\[
 J^*X=c\notin L^4.
 \tag{9.3}
\]

Finite Fourier coefficients do not rule out (9.3).  At depth three an
additional reused connector creates another response hierarchy, so an
\(L=2\) result would not transfer without a connector-local factorial
contraction theorem.

The sharp plausible route is therefore an all-source analytic **scale**,
not a finite ledger: Gaussian creation loses analytic radius, while the
chronological step simplex must repay that loss through its factors of
\(|h|\).  No such reachable-core contraction theorem has yet been proved.

## 10. Audit of `FIFTH_JET_POLYNOMIAL_THEOREM.md`

The algebraic cancellation in that file is correct: if

\[
 [h^5]F_{N,L}(h)=\sum_{d=1}^5\gamma_dN^d,
 \tag{10.1}
\]

then

\[
 [h^5]\Delta_{t,L}
 =\sum_{d=1}^4(2^d-32)\gamma_dt^d.
 \tag{10.2}
\]

Its constant \((127/10)B_\psi^{E_{L,5}}\) is valid but much coarser than
(2.5).  The identity activation supplies a nonzero quartic, so degree four
is sharp at the coefficient level.

Three qualifications are essential.

1. The sentence in its Section 7 saying that the theorem is “stronger than
   the requested \(O(t^5)\) milestone” is misleading if the milestone is a
   uniform finite-step remainder.  The theorem is stronger only in the
   degree of the **exact fifth coefficient**.  It does not imply (1.2).
2. Its near-identity Section 6 is valid only at this coefficient level.
   The displayed \(o_t(h^5)\) is explicitly horizon-dependent and cannot be
   promoted to a uniform interval estimate.
3. The notation \(D^k\mathbf g(\theta_0)\) should be read as the generated
   rooted-tree multilinear germ, not as an ambient Frechet derivative on an
   \(L^2\) ball.  Standalone use of the polynomial-Euler argument requires
   the previously proved horizon-compatible fixed-operator/marked-Price
   intertwining.  Without that dependency, Lemma 2.1 is only an induction
   outline; with it, the exact coefficient theorem is supported.

There are also rendering-only defects (`max`, `eta`, `ell`, `le`, and
`Delta` appear without their TeX backslashes in a few displays).  They do
not change the mathematical verdict.

**Post-audit repair.**  The theorem was subsequently revised to use the
generated tensors \(\mathbf G_k,\mathcal T_k\), to display the complete
order-five marked adjoint convolution, to correct the exact-versus-interval
wording and rendering, and to promote the sharper Newton constant
\(227/180\).  Thus the three qualifications above are now explicit in the
theorem itself; the interval-remainder boundary is unchanged.

## 11. Final claim ledger

\[
\begin{array}{c|c}
\text{claim}&\text{status}\\ \hline
\text{exact }[h^5]\Delta_{t,L}=O_{\psi,L}(t^4)
 &\text{proved for every fixed finite }L\\
\text{fixed-}t\text{ full }h^5\text{ remainder with explicit constant}
 &\text{proved, constant }B_\psi^{E_{L,2t}}\\
\text{polynomial-in-}t\text{ full interval remainder at }L=2
 &\text{open for every proved genuinely nonlinear class}\\
\text{same at }L=3&\text{open}\\
\text{proposed finite Fourier/chaos/provenance closure}&\text{ruled out}\\
\text{all-source analytic-scale closure}&\text{plausible but unproved}
\end{array}
\tag{11.1}
\]

Accordingly, the exact quartic fifth jet is the strongest unconditional
polynomial-horizon nonlinear result presently justified.  It must not be
reported as the requested uniform finite-step remainder theorem.
