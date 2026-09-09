# Abstract coupled step-doubling lemma

This lemma explains the expected \(t^2\) and \(t^4\) powers.  Its
application to the width-first reused-matrix network is conditional on the
population response-state bridge isolated in `SHARP_CONJECTURE.md`.

## 1. Schedule notation

Let \(X\) be a Banach space, \(V:X\to X\), and

\[
 E_h(x)=x+hV(x).
\]

For a finite step schedule \(\delta=(\delta_1,\ldots,\delta_m)\), define

\[
 \mathcal F_m(x;\delta)
 =\ell(E_{\delta_m}\circ\cdots\circ E_{\delta_1}x).
                                                               \tag{1.1}
\]

Assume all schedules below stay in a set on which (1.1) is \(C^5\), and
that for every schedule with \(\|\delta\|_1\le\rho\),

\[
 \left|D_\delta^5\mathcal F_m(x;\delta)
 [v_1,\ldots,v_5]\right|
 \le Q\prod_{i=1}^5\|v_i\|_1.                         \tag{1.2}
\]

The same \(Q\) must work for every schedule length.  This is the
horizon-uniform hypothesis that the fixed-horizon Gaussian compiler does
not currently provide.

Let an expectation or other linear functional over the initial state be
included in \(\ell\).  Suppose the resulting step-doubling discrepancy

\[
 \Delta_t(h)=\mathcal F_{2t}(x;(h,\ldots,h))
 -\mathcal F_t(x;(2h,\ldots,2h))                       \tag{1.3}
\]

is odd in \(h\).

## 2. Exact coupled defect identity

Replace the \(t\) coarse blocks by pairs of fine steps, one block at a
time.  The resulting hybrid telescope writes \(\Delta_t\) as a sum of
\(t\) local split defects.  At the \(j\)-th replacement, keep the
surrounding hybrid schedule fixed and write

\[
 H_j(r,s;h)=\mathcal F(\ldots,r,s,\ldots)
 -\mathcal F(\ldots,r+s,\ldots),                       \tag{2.1}
\]

where the omitted entries are either \(h\) or \(2h\).  Since \(E_0\) is
the identity,

\[
 H_j(r,0;h)=H_j(0,s;h)=0.
\]

Two applications of the fundamental theorem of calculus therefore give
the exact identity

\[
 H_j(h,h;h)
 =h^2d_{j,t}(h),                                       \tag{2.2}
\]

\[
 d_{j,t}(h)=\int_0^1\!\int_0^1
 \partial_{rs}H_j(\alpha h,\beta h;h)
 \,d\alpha\,d\beta.                                  \tag{2.3}
\]

Consequently,

\[
 \Delta_t(h)=h^2S_t(h),\qquad
 S_t(h)=\sum_{j=1}^t d_{j,t}(h).                       \tag{2.4}
\]

This is a coupled identity: no absolute value has yet separated the fine
and coarse trajectories.

## 3. Degree-four remainder

Differentiating (2.3) three times in \(h\) uses five schedule derivatives
in total.  Every schedule coefficient has absolute value at most two and
the total schedule length is at most \(2t\).  From (1.2), multilinearity,
and the two terms in (2.1),

\[
 |d_{j,t}^{(3)}(h)|\le2Q(2t)^3=16Qt^3               \tag{3.1}
\]

whenever \(2t|h|\le\rho\).  Summing over \(j\) gives

\[
 |S_t^{(3)}(h)|\le16Qt^4.                              \tag{3.2}
\]

Because \(\Delta_t\) is odd and \(h^2\) is even, the continuous
extension of \(S_t\) at zero is odd.  Taylor's integral identity applied
to \(S_t\) yields

\[
 |S_t(h)-S_t'(0)h|
 \le\frac{8}{3}Qt^4|h|^3.                             \tag{3.3}
\]

Multiplying by \(h^2\) proves

\[
 \boxed{
 |\Delta_t(h)-S_t'(0)h^3|
 \le\frac83Q\,t^4|h|^5,
 \qquad 2t|h|\le\rho.}                               \tag{3.4}
\]

Thus the degree-four power comes from the \(t\) local defects and the
three derivatives of their hybrid schedules.  A separate bound on the
two fifth derivatives would miss this cancellation and give \(t^5\).

## 4. Cubic time algebra

In this section write \(f=\ell\) for the scalar observable and let
\(\Lambda\) include expectation over the initial population state.

For an autonomous Euler pullback, put

\[
 P_hq=q\circ E_h,qquad
 A_rq=\frac1{r!}D^rq[V,\ldots,V].                      \tag{4.1}
\]

Up to any fixed order \(m\),

\[
 P_h=I+\sum_{r=1}^m h^rA_r+o(h^m).
\]

Selecting the \(l\) nonidentity factors from \(P_h^k\) gives

\[
 [h^m]\,\Lambda(P_h^k f)
 =\sum_{l=1}^m{k\choose l}c_{m,l},                    \tag{4.2}
\]

\[
 c_{m,l}=\Lambda\!\left(
 \sum_{r_1+\cdots+r_l=m}A_{r_1}\cdots A_{r_l}f
 \right).                                             \tag{4.3}
\]

The order of the noncommuting operators in (4.3) is their temporal order.
It follows that the coefficient of \(h^m\) in the step-doubling
discrepancy is

\[
 \sum_{l=1}^m d_{m,l}(t)c_{m,l},\qquad
 d_{m,l}(t)={2t\choose l}-2^m{t\choose l}.             \tag{4.4}
\]

For \(m=3\), the degree-three part cancels and (4.4) is quadratic in
\(t\).  Without using gradient symmetry it can be written from its first
two values as

\[
 K_t=tK_1+{t\choose2}(K_2-2K_1).                      \tag{4.5}
\]

If \(X\) is a Hilbert space and \(V=\nabla f\) in a fixed, constant
Hilbert metric, the reduction is explicit.  At the initial state put

\[
 g=V,\qquad A=DV[g],\qquad B=D^2V[g,g],\qquad C=DV[A],
\]

\[
 S=\Lambda D^3f[g,g,g],\qquad H=\Lambda\|A\|^2.
                                                               \tag{4.6}
\]

Three differentiations of
\(x_{s+1}(h)=x_s(h)+hV(x_s(h))\) at zero give

\[
 x_k'=kg,\qquad x_k''=k(k-1)A,
\]

\[
 x_k'''=k(k-1)(k-2)C+
 \frac{k(k-1)(2k-1)}2B.                              \tag{4.7}
\]

Because \(V=\nabla f\), symmetry of the derivatives of \(f\) gives

\[
 \Lambda Df[B]=S,\qquad
 \Lambda Df[C]=\Lambda D^2f[g,A]=H.
\]

The third-order chain rule now yields, directly,

\[
 \frac{d^3}{dh^3}\Lambda f(x_k(h))\bigg|_{h=0}
 =
 2k(k-1)(2k-1)H+
 \frac{k(4k^2-3k+1)}2S.                              \tag{4.8}
\]

Subtracting eight times (4.8) at \(k=t\) from (4.8) at \(k=2t\), and
dividing by \(3!=6\), proves

\[
 K_t=t(2t-1)\left(\frac12S+2H\right).                 \tag{4.9}
\]

For \(m=5\), the five explicit polynomials are

\[
 \begin{aligned}
 d_{5,1}(t)&=-30t,\\
 d_{5,2}(t)&=t(15-14t),\\
 d_{5,3}(t)&=-2t(t-1)(2t-5),\\
 d_{5,4}(t)&=\frac{t(t-1)}6(-4t^2+32t-45),\\
 d_{5,5}(t)&=\frac{t(t-1)(t-2)}3(4t-9).
 \end{aligned}                                        \tag{4.10}
\]

Each has degree at most four.  Formula (4.10) describes the fifth
coefficient; inequality (3.4) is the stronger finite-step remainder.

## 5. A terminating schedule-derivative envelope

The constant \(Q\) in (1.2) need not be output-defined.  Suppose every
schedule with \(\|\delta\|_1\le\rho\) stays in a set on which

\[
 \|D^rV\|\le K_r\quad(0\le r\le5),\qquad
 \|D^r\ell\|\le A_r\quad(1\le r\le5).                 \tag{5.1}
\]

For completeness, define the partial exponential Bell polynomial by

\[
 B_{q,p}(z_1,\ldots,z_{q-p+1})
 =
 \sum_{\substack{\sum_r j_r=p\\\sum_r rj_r=q}}
 \frac{q!}{\prod_rj_r!}
 \prod_r\left(\frac{z_r}{r!}\right)^{j_r}.             \tag{5.2}
\]

Set

\[
 R_1=e^{K_1\rho}K_0,                                  \tag{5.3}
\]

and, successively for \(2\le q\le5\),

\[
 R_q=e^{K_1\rho}\left[
 \rho\sum_{p=2}^qK_pB_{q,p}(R_1,\ldots,R_{q-p+1})
 +q\sum_{p=1}^{q-1}K_pB_{q-1,p}(R_1,\ldots,R_{q-p})
 \right].                                             \tag{5.4}
\]

Then a valid explicit choice in (1.2) is

\[
 Q=\sum_{p=1}^5A_pB_{5,p}(R_1,\ldots,R_{6-p}).         \tag{5.5}
\]

Here is the proof, including the absence of a hidden horizon factor.
Write \(x_i=x_i(\delta_1,\ldots,\delta_i)\).  For directions
\(v_1,\ldots,v_q\), differentiating

\[
 x_i=x_{i-1}+\delta_iV(x_{i-1})
\]

gives three kinds of terms: propagation of \(D^qx_{i-1}\) by
\(I+\delta_iDV(x_{i-1})\); a term multiplied by \(\delta_i\) for each
partition of the \(q\) directions into at least two blocks; and, for
each of the \(q\) choices of a direction differentiating the explicit
\(\delta_i\), a derivative of \(V\circ x_{i-1}\) in the other
\(q-1\) directions.  Variation of constants bounds all propagation
products by

\[
 \prod_i(1+|\delta_i|K_1)\le e^{K_1\rho}.
\]

The second class sums with weight
\(\sum_i|\delta_i|\le\rho\).  In the third class, for each chosen
direction \(v_a\), the weights sum as
\(\sum_i|(v_a)_i|\le\|v_a\|_1\); hence there is no factor equal to the
schedule length.  Faà di Bruno identifies the partition sums with the
two Bell-polynomial sums in (5.4).  Induction on \(q=1,\ldots,5\)
therefore proves

\[
 \|D_\delta^qx_m\|_{(\ell^1)^q\to X}\le R_q
\]

uniformly in \(m\).  One final Faà di Bruno application to
\(\ell(x_m)\) gives (5.5).  The construction terminates after computing
\(R_1,\ldots,R_5\).

If a single number \(z\ge1\) bounds every \(K_r,A_r\), while
\(\rho\le1\) and \(K_1\rho\le1\), an entirely numerical polynomial
majorant is obtained by

\[
 u_1(z)=4z,
\]

\[
 u_q(z)=4z\left[
 \sum_{p=2}^qB_{q,p}(u_1,\ldots,u_{q-p+1})
 +q\sum_{p=1}^{q-1}B_{q-1,p}(u_1,\ldots,u_{q-p})
 \right],\quad2\le q\le5,                             \tag{5.6}
\]

\[
 q_5(z)=z\sum_{p=1}^5B_{5,p}(u_1,\ldots,u_{6-p}).
                                                               \tag{5.7}
\]

Since \(e<4\), induction gives \(R_q\le u_q(z)\), hence
\(Q\le q_5(z)\).  This is a positive polynomial of degree at most ten,
so \(q_5(z)\le q_5(1)z^{10}\) for \(z\ge1\).

## 6. What is needed for the neural-network application

To apply (3.4)--(4.6) after the width limit, one must construct an
autonomous, restartable population state satisfying all three properties:

1. its Euler schedule equals the inverse-free Gaussian response DAG for
   every mixed fine/coarse schedule;
2. its fifth schedule derivative obeys (1.2) with
   \(Q=Q_{\phi,L}\) independent of schedule length; and
3. its gradient adjoint is valid for the complete enlarged marked source
   history, including all differentiated response convolutions.

The existing fixed-horizon compiler proves none of these uniformly in the
horizon.  Therefore (3.4) is an exact abstract theorem and a conditional
network theorem, not yet the requested unconditional general-time result.
