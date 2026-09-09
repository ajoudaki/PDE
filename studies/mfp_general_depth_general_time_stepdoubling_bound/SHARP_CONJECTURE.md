# Sharp general-time statement and current status

## Proposed theorem

For the exact width-first depth-\(L\) network, the intended statement is
that there exist activation/depth quantities

\[
 \kappa_{\phi,L},\qquad Q_{\phi,L}<\infty,qquad
 \rho_{\phi,L}>0,                                     \tag{1.1}
\]

computed solely from Gaussian activation integrals and a weighted
derivative envelope, such that for every integer \(t\ge1\),

\[
 \left|F_{2t,L}(\eta)-F_{t,L}(2\eta)
 -t(2t-1)\kappa_{\phi,L}\eta^3\right|
 \le\frac83Q_{\phi,L}t^4|\eta|^5                     \tag{1.2}
\]

whenever

\[
 2t|\eta|\le\rho_{\phi,L}.                            \tag{1.3}
\]

The \(t^2\) and \(t^4\) powers in (1.2) are sharp in general; see
`SCALAR_CHECK.md`.

## Exact abstract implication

The proposed theorem follows from the following population response-state
statement.

**Population Euler response-state hypothesis.**  There is a Banach state
space \(X_{\phi,L}\), an initialization functional \(\Lambda\), an
observable \(\ell\), and a \(C^5\) vector field \(V\) such that:

1. for every finite mixed schedule \(\delta\), the width-first Gaussian
   operator DAG equals
   \(\Lambda\ell(E_{\delta_m}\cdots E_{\delta_1}x_0)\), where
   \(E_h=I+hV\);
2. this identification is restartable, is invariant under inserting or
   deleting zero steps, and represents both schedules—and every hybrid
   schedule used while replacing a coarse block \((2h)\) by a fine pair
   \((h,h)\); no equality between the two unequal Euler maps is assumed;
3. every differentiated forward and transpose response uses the complete
   enlarged marked source histories, including the binomial convolutions
   of all \(\rho\)- and \(\sigma\)-jets;
4. every schedule of total variation at most \(\rho_{\phi,L}\) has

   \[
   \|D_\delta^5\mathcal F_m\|_{(\ell^1)^5\to\mathbb R}
   \le Q_{\phi,L},                                     \tag{2.1}
   \]

   independently of its length; and
5. the state space is Hilbert and \(V\) is the gradient of \(\ell\) in a
   fixed, constant population metric.

Under these five hypotheses, `ABSTRACT_STEP_DOUBLING.md` proves (1.2),
with

\[
 \kappa_{\phi,L}
 =\Lambda\left[
 \frac12D^3\ell[V,V,V]+2\|DV[V]\|^2\right].          \tag{2.2}
\]

The order-three marked Gaussian compiler now proves directly for the
actual width-first DAG that

\[
 [\eta^3]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}
 =t(2t-1)\kappa_{\phi,L},
\]

with \(\kappa_{\phi,L}\) defined by its terminating activation/depth
Gaussian recursion; see CUBIC_MARKED_BRIDGE.md.  This local formal-germ
theorem does not construct the nonzero mixed-schedule state required for
the remainder.

If only hypotheses 1--4 hold, without the gradient adjoint,
the cubic coefficient is still quadratic in \(t\), but has the more
general form

\[
 K_{t,\phi,L}
 =tK_{1,\phi,L}+{t\choose2}
 (K_{2,\phi,L}-2K_{1,\phi,L}).                         \tag{2.3}
\]

Here \(K_{j,\phi,L}=[\eta^3]\{F_{2j,L}(\eta)
-F_{j,L}(2\eta)\}\), as computed by the signed Gaussian Price
recursion; it is not defined through an unproved output derivative.

Formula (2.3) avoids the factor-six identity but still requires the
zero-step/marked-response functoriality in hypotheses 1--3.

## Explicit envelope once the state is constructed

Suppose, on the total-variation tube, that

\[
 K_r\ge\sup\|D^rV\|\quad(0\le r\le5),\qquad
 A_r\ge\sup\|D^r\ell\|\quad(1\le r\le5).              \tag{3.1}
\]

Let \(B_{q,p}\) be the partial exponential Bell polynomial.  Define

\[
 R_1=e^{K_1\rho}K_0,                                  \tag{3.2}
\]

and, for \(2\le q\le5\),

\[
 R_q=e^{K_1\rho}\left[
 \rho\sum_{p=2}^qK_pB_{q,p}(R_1,\ldots,R_{q-p+1})
 +q\sum_{p=1}^{q-1}K_pB_{q-1,p}(R_1,\ldots,R_{q-p})
 \right].                                             \tag{3.3}
\]

Then schedule Faà di Bruno and discrete Grönwall give the explicit choice

\[
 Q_{\phi,L}
 =\sum_{p=1}^5A_pB_{5,p}(R_1,\ldots,R_{6-p}).          \tag{3.4}
\]

The recursion terminates after four applications of (3.3).  Thus, if the
missing population construction supplied explicit activation/depth bounds
for the finite list \((K_r,A_r)\), equations (3.2)--(3.4) would immediately
produce the requested activation-only constant.  No concrete powers of
\(L\) for those missing bounds have been obtained here; hiding \(L\) in
their subscripts is not an explicit depth-dependence theorem.

## Status after proof search

The abstract implication, scalar theorem, exact all-depth cubic law, and
every fixed-\((t,L)\) quantitative theorem are proved.  The stronger
nonzero population Euler response-state hypothesis is **open** for the
reused-matrix width-first DAG.  The fixed-horizon Price compiler does not
imply it: its source dimension, rank radius, and envelope grow with the
history length, and it only controls a common step rather than arbitrary
mixed schedules.

The missing items are therefore precise:

1. a restartable nonzero mixed-schedule response state through order
   five, stronger than the proved order-three formal germ;
2. a total-time feature-moment/rank argument covering (1.3); and
3. the horizon-independent mixed-schedule derivative estimate (2.1).

Until these are proved, (1.2) is a sharp conjecture and a conditional
theorem, not an unconditional result for \(L\ge2\).
