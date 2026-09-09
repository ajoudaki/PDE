# Independent adversarial audit of the uniform quadratic no-go theorem

Date: 25 August 2026.

## Verdict

**PASS, with the limit-order premise stated explicitly.**  For every fixed
normalized quadratic activation

\[
 \psi(x)=p x+q x^2,\qquad p^2+3q^2=1,\qquad q\ne0,
\]

and every fixed \(\rho>0\), the actual finite-width network admits the
finite-width comparison

\[
 \Delta_{t,n}(h)\ge D_{t,n}(h)\qquad(h\ge0),                 \tag{A.1}
\]

where the right side is the defect after deleting the first-layer feature
update.  At each separately fixed \((t,h)\), the polynomial-activation
fixed-program bridge gives

\[
 \lim_{n\to\infty}D_{t,n}(h)=D_t(h),\qquad
 \lim_{n\to\infty}\Delta_{t,n}(h)=\Delta_t(h).              \tag{A.2}
\]

The scalar frozen defect has an explicitly positive term whose order is
\(3(4^t-1)\).  Its Gaussian moment grows fast enough that

\[
 D_t(\rho/t)\longrightarrow+\infty.                         \tag{A.3}
\]

Thus the theorem's conclusion is correct.  This is an all-orders effect;
no fixed fifth-jet calculation is used anywhere in this audit.

The order of operations in (A.2)--(A.3) is essential:

\[
 \text{for each }t:\quad n\to\infty\text{ at }h=\rho/t,
 \qquad\text{then}\qquad t\to\infty.                       \tag{A.4}
\]

No joint \((n,t)\)-limit and no exchange of these limits is asserted.

One material defect in the first draft was found and repaired: it claimed
that each top \(h\)-coefficient was a single pure-\(q\) monomial.  That is
false when \(p\ne0\), because linear and quadratic branches tie in
\(h\)-degree at the first step.  Section 3 proves the needed, and strictly
weaker, coefficientwise containment.  The divergence conclusion is
unchanged.

## 1. Exact finite-width embedding

Use the scalar first-layer preactivations \(u_j\) as the trainable bottom
coordinates.  With

\[
 H_j=\psi(u_j),\quad
 z_i=n^{-1/2}\sum_jW_{ij}H_j,\quad
 f_n=n^{-1}\sum_i a_i\psi(z_i),
\]

the rescaled ascent field is exactly

\[
\begin{aligned}
 \dot a_i&=\psi(z_i),\\
 \dot W_{ij}&=n^{-1/2}a_i\psi'(z_i)H_j,\\
 \dot u_j&=\psi'(u_j)n^{-1/2}\sum_iW_{ij}a_i\psi'(z_i).
\end{aligned}                                               \tag{A.5}
\]

An Euler step of size \(h\) in (A.5) is precisely the network update in the
theorem.  When \(p,q\ge0\), every scalar coefficient of (A.5) and of
\(f_n\), viewed as polynomials in the raw variables
\((a_i,W_{ij},u_j)\), is nonnegative.  Factors \(n^{-1}\) and
\(n^{-1/2}\) are positive and do not change this statement.

Delete only the last line of (A.5).  Then every \(H_j\) is constant.  Put

\[
 Q_n=n^{-1}\sum_jH_j^2.
\]

For a fixed top row, direct substitution into the first two Euler updates
gives the exact closed recursion

\[
 A^+=A+h\psi(Z),\qquad
 Z^+=Z+hQ_nA\psi'(Z).                                      \tag{A.6}
\]

There is no approximation in (A.6):

\[
\begin{aligned}
Z^+
&=n^{-1/2}\sum_j
 \left(W_j+\frac h{\sqrt n}A\psi'(Z)H_j\right)H_j\\
&=Z+hQ_nA\psi'(Z).
\end{aligned}
\]

Conditional on \((H_j)_j\), the row pairs are iid,

\[
 A_0\sim N(0,1),\qquad Z_0\sim N(0,Q_n),
\]

and are independent.  Since \(H_j=\psi(u_j)\) has moments of every order,
the iid law gives \(Q_n\to1\) in every finite \(L^r\).  A fixed-horizon
iterate of (A.6) is a finite polynomial in \((A_0,Z_0,Q_n)\).  Gaussian
moment evaluation and finite-moment convergence therefore give

\[
 \lim_{n\to\infty}D_{t,n}(h)=D_t(h),                         \tag{A.7}
\]

where \(D_t\) uses independent standard \(A_0,Z_0\) and

\[
 A_{k+1}=A_k+h(pZ_k+qZ_k^2),\qquad
 Z_{k+1}=Z_k+hA_k(p+2qZ_k).                                 \tag{A.8}
\]

### The full-network width limit for a quadratic activation

The older bounded-derivative/linear-growth bridge cannot simply be cited
for \(x\mapsto px+qx^2\).  The relevant bridge is instead the fixed-program
polynomially-smooth one.  For every separately fixed \(t\), the \(2t\)-step
network is one finite Gaussian program containing:

* finitely many uses of the same Gaussian matrix and its transpose;
* coordinatewise polynomial maps \(\psi,\psi'\);
* finitely many empirical moment scalars; and
* one terminal empirical average.

Here is the exact reduction of the trained connector.  If \(W^0\) is the
initialized matrix, then

\[
 W^s=W^0+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^T.      \tag{A.8a}
\]

Consequently every trained-matrix action is replaced, without an error, by

\[
\begin{aligned}
z^s&=\frac{W^0H^s}{\sqrt n}
 +h\sum_{r<s}\langle H^r,H^s\rangle_n C^r,\\
b^s&=\frac{(W^0)^TC^s}{\sqrt n}
 +h\sum_{r<s}\langle C^r,C^s\rangle_n H^r.          \tag{A.8b}
\end{aligned}
\]

Thus a horizon \(N\) uses the finite predictable action list

\[
W^0H^0,(W^0)^TC^0,\ldots,
W^0H^{N-1},(W^0)^TC^{N-1},W^0H^N,                  \tag{A.8c}
\]

plus coordinatewise polynomial and empirical-moment lines.  Equations
(A.8a)--(A.8c) explicitly include every learned rank-one term, reused
matrix action, and transpose action in the fixed program.

The activation is \(C^\infty\), and every derivative is polynomially
bounded (all derivatives above order two vanish).  Consequently the
all-finite-\(L^r\) fixed-program theorem recorded and adversarially checked
in `generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md`, Section 1,
applies at each fixed horizon.  It supplies almost-sure and \(L^r\)
convergence of the terminal scalar for every finite \(r\), including all
transpose responses and reused-matrix dependencies.  Hence the annealed
limit in the second part of (A.2) exists.  This invocation is horizon by
horizon; it supplies no estimate uniform in \(t\), and none is needed for
(A.4).

Thus the quadratic growth issue does not leave a width-first gap in this
particular fixed-horizon argument.

## 2. Coefficientwise fine/coarse comparison

Let \(g\) and \(O\) be polynomials with nonnegative coefficients and put

\[
 E_h(x)=x+hg(x),\qquad A=E_h^2,\qquad B=E_{2h}.
\]

Then

\[
 A(x)-B(x)=h\{g(x+hg(x))-g(x)\}.                           \tag{A.9}
\]

For a monomial \(cx^\nu\) of a component of \(g\), the corresponding
difference is

\[
 c\left[\prod_j(x_j+hg_j(x))^{\nu_j}-x^\nu\right].         \tag{A.10}
\]

After expanding the product, the cancelled term is the unique term that
chooses \(x_j\) from every factor.  Every remaining term has a
nonnegative coefficient.  Therefore \(A\succeq B\) coefficientwise.
Positive-polynomial composition is order preserving, so induction gives

\[
 A^t\succeq B^t,\qquad O\circ A^t\succeq O\circ B^t.      \tag{A.11}
\]

For deletion monotonicity write the full field as \(g_0+\lambda g_1\),
where \(g_1\) is precisely the bottom-update block.  Every coefficient in
\((x,h,\lambda)\) is nonnegative.  Repeating (A.9)--(A.11) in the enlarged
polynomial ring proves that the full paired defect has the form

\[
 P_0(x,h)+\lambda P_1(x,h)+\cdots+\lambda^MP_M(x,h),
 \qquad P_r\succeq0,                                       \tag{A.12}
\]

and \(P_0\) is exactly the frozen paired defect.  At \(\lambda=1\), this
proves coefficientwise domination by the frozen system.

After composing every iterate back to the independent centered Gaussian
initialization, each raw monomial has expectation either zero or a product
of positive double factorials.  Taking expectation in (A.12) therefore
preserves coefficientwise order.  This proves (A.1), not merely a
pointwise comparison along a particular initialization.

I attempted the natural counterexamples to (A.12): mixed signs of raw
variables, matrix reuse, transpose reuse, and odd Gaussian monomials.  None
is a counterexample.  Coefficientwise positivity concerns coefficients,
not the values of the raw variables; reuse only repeats variables; and odd
monomials vanish rather than contribute negatively.  The argument would
fail for a negative activation coefficient, but Section 5 below removes
signs by conjugacy before positivity is invoked.

## 3. Independent derivation of the surviving term

Let

\[
 \delta_N=2^N-1.
\]

For \(N\ge1\), induction in (A.8) gives the following **distinguished
pure-\(q\) monomial containments** in the coefficientwise order:

\[
\begin{aligned}
 [h^{\delta_N}]A_N
 &\succeq c_Nq^{\delta_N}A_0^{r_N}Z_0^{s_N},\\
 [h^{\delta_N}]Z_N
 &\succeq d_Nq^{\delta_N}A_0^{u_N}Z_0^{v_N}.       \tag{A.13}
\end{aligned}
\]

Equality in (A.13) would be false when \(p\ne0\): already at the first
step the same top \(h\)-degree also contains \(pZ_0\) in \(A_1\) and
\(pA_0\) in \(Z_1\).  Only the displayed monomial containment is needed.

with \(c_N,d_N\in\mathbb N\).  At \(N=1\),

\[
 c_1=1,\quad d_1=2,\quad
 (r_1,s_1)=(0,2),\quad(u_1,v_1)=(1,1).             \tag{A.14}
\]

Suppose (A.13) holds at \(N\).  The update gives the degree upper bound

\[
 \deg_h A_{N+1},\deg_h Z_{N+1}\le2\delta_N+1
 =\delta_{N+1}.                                    \tag{A.14a}
\]

Inside \(hqZ_N^2\), choose the distinguished monomial from each copy of
\(Z_N\).  Inside \(2hqA_NZ_N\), choose the distinguished monomial from
\(A_N\) and \(Z_N\).  All coefficients are nonnegative, so these choices
cannot be cancelled and give

\[
\begin{aligned}
c_{N+1}&=d_N^2,&(r_{N+1},s_{N+1})&=(2u_N,2v_N),\\
d_{N+1}&=2c_Nd_N,&(u_{N+1},v_{N+1})&=(r_N+u_N,s_N+v_N).
                                                               \tag{A.15}
\end{aligned}
\]

The containments in (A.15), together with (A.14a), prove both (A.13) and
\(\deg_hA_N=\deg_hZ_N=\delta_N\).
The first exponent pair remains even-even and the second remains odd-odd.
Both pairs have total degree \(2^N\).

In the output \(A_N(pZ_N+qZ_N^2)\), the \(qA_NZ_N^2\) branch has strictly
larger possible \(h\)-degree than the \(pA_NZ_N\) branch.  Selecting the
three distinguished monomials in that branch gives, again coefficientwise,

\[
\begin{aligned}
m_N&:=\deg_h\mathbb E[A_N\psi(Z_N)]=3(2^N-1),\\
[h^{m_N}]\mathbb E[A_N\psi(Z_N)]
 &\ge c_Nd_N^2q^{3(2^N-1)+1}
   \mathbb EG^{R_N}\,\mathbb EG^{S_N}>0,            \tag{A.16}
\end{aligned}
\]

where \(R_N,S_N\) are even and

\[
 R_N+S_N=3\cdot2^N.                                \tag{A.17}
\]

The coarse \(t\)-step output has degree \(m_t<m_{2t}\).  By the
coefficientwise positivity already proved, the degree-\(m_{2t}\) fine term
cannot be cancelled by any lower term.  Thus, for \(h>0\),

\[
D_t(h)\ge
q^{3(4^t-1)+1}h^{3(4^t-1)}
\mathbb EG^{R_{2t}}\mathbb EG^{S_{2t}}.             \tag{A.18}
\]

The omission of \(c_{2t}d_{2t}^2\) only weakens the lower bound because
that integer is at least one.

The separate exact-rational program `audit_uniform_no_go.py` expands
(A.8) directly in \(\mathbb Q[h,A_0,Z_0]\), without importing a jet or
OMFP compiler.  It verifies the degrees in (A.16), positivity of the
leading Gaussian moment, and coefficientwise positivity of the paired
defect through \(t=2\).

## 4. Growth at \(h=\rho/t\)

For an even integer \(K=2m\),

\[
 \mathbb EG^K=(2m-1)!!\ge m!\ge(m/e)^m.             \tag{A.19}
\]

The first inequality compares factors \(2j-1\ge j\).  For the second,

\[
 \log m!=\sum_{j=1}^m\log j
 \ge\int_1^m\log x\,dx
 =m\log m-m+1.
\]

By (A.17), one of \(R_{2t},S_{2t}\) is at least
\(3\cdot4^t/2\), and the other even moment is at least one.  Substitution
of \(h=\rho/t\) into (A.18) gives

\[
 D_t(\rho/t)\ge L_t,
\]

\[
L_t=
q^{3(4^t-1)+1}
\left(\frac\rho t\right)^{3(4^t-1)}
\left(\frac{3\cdot4^t}{4e}\right)^{3\cdot4^t/4}.  \tag{A.20}
\]

All bases in (A.20) are positive because this part of the proof has
\(q>0\).  Direct division gives

\[
 \frac{\log L_t}{4^t}
 =\frac34t\log4-3\log t+C_{q,\rho}+o(1),           \tag{A.21}
\]

where \(C_{q,\rho}\) is finite for every fixed \(q,\rho>0\).  The first
term is linear in \(t\), whereas the only negative unbounded term is
logarithmic.  Hence \(L_t\to\infty\).

Combining (A.1), (A.2), (A.7), and (A.20) proves (A.3).

## 5. Sign audit

The positivity proof assumed \(p,q\ge0\).  This does not restrict the
theorem.  The identities

\[
 \psi_{p,-q}(-x)=-\psi_{p,q}(x),\qquad
 \psi_{-p,-q}(x)=-\psi_{p,q}(x)                    \tag{A.22}
\]

are implemented on parameter space by the orthogonal maps

\[
 R_1(a,W,u)=(-a,W,-u),\qquad
 R_2(a,W,u)=(-a,-W,u).                              \tag{A.23}
\]

Direct substitution gives

\[
 f_{p,-q}(R_1\theta)=f_{p,q}(\theta),\qquad
 f_{-p,-q}(R_2\theta)=f_{p,q}(\theta).             \tag{A.24}
\]

If \(f_2(R\theta)=f_1(\theta)\) with \(R\) orthogonal, differentiation
gives

\[
 \nabla f_2(R\theta)=R\nabla f_1(\theta).
\]

Thus the Euler maps are conjugate for every step size and every horizon.
The iid Gaussian initialization is invariant under \(R_1,R_2\), so
\(F_N\) depends only on \((|p|,|q|)\).  This reduces all \(q\ne0\) cases
to the positive-coefficient case.  The pure quadratic endpoint \(p=0\)
is included.

## 6. Remainder quantifiers

Let \(\kappa_t=[h^3]\Delta_t(h)\).  Its explicit quadratic-activation
formula is finite and satisfies \(|\kappa_t|\le C_{p,q}t^2\).  Therefore

\[
 |\kappa_t|(\rho/t)^3\le C_{p,q}\rho^3/t\to0.       \tag{A.25}
\]

Equations (A.3) and (A.25) give

\[
 |\Delta_t(\rho/t)-\kappa_t(\rho/t)^3|\to\infty.   \tag{A.26}
\]

At the same endpoint,

\[
 t^4(\rho/t)^5=\rho^5/t.
\]

Hence the proposed \(Ct^4h^5\) bound fails for every finite \(C\) on
every positive total-time interval.  Replacing \(t^4\) by \(t^r\) for
any fixed \(r\) does not help: \(t^r(\rho/t)^5\) is polynomial in \(t\),
while the lower bound (A.20) grows faster than every polynomial.

The quantifiers do **not** say that a \(t\)-dependent activation
coefficient \(q_t\to0\) fails, nor do they address negative step sizes.
They say exactly that every fixed nonzero quadratic component fails on
every fixed positive total-time interval.

## Final audit table

| Obligation | Verdict |
|---|---|
| Exact finite-width network and frozen embedding | pass, equations (A.5)--(A.8) |
| Reused-matrix/full-network width limit | pass horizon by horizon under the polynomially-smooth fixed-program theorem |
| Coefficientwise paired positivity | pass, equations (A.9)--(A.12) |
| Deletion monotonicity | pass; no counterexample under the stated positive-coefficient hypotheses |
| Surviving all-order term | pass, equations (A.13)--(A.18) |
| Gaussian-moment lower bound | pass, equations (A.19)--(A.21) |
| Sign removal | pass by exact orthogonal conjugacy |
| Width-first then time-limit quantifiers | pass, equation (A.4) |
| Uniform \(t^4h^5\) conclusion | disproved for every fixed \(q\ne0\) |
