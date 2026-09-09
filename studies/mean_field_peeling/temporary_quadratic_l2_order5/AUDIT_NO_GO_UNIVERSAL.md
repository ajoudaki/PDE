# Hostile audit of `UNIFORM_NO_GO_THEOREM.md`

## Verdict

The coefficientwise comparison, frozen-block reduction, surviving
high-degree monomial, coarse/fine subtraction, and final uniform-tail
contradiction are mathematically sound **provided the full quadratic
width-first limits exist and are finite at every fixed horizon and fixed
step size used in the statement**.

That proviso is not currently discharged inside the proposed theorem.  The
fixed-step OMFP identification previously established under bounded
derivatives and at-most-linear activation growth does not automatically
cover a quadratic activation.  Thus the no-go theorem is presently either

1. a correct conditional theorem under explicit fixed-step width-limit
   existence, or
2. a correct dichotomy: either those width-first limits fail to exist, or,
   if they exist, they cannot satisfy the proposed uniform remainder bound.

It is not yet a self-contained unconditional theorem identifying the full
quadratic network's width-first limit.  A direct polynomial/Wick moment
proof for each fixed horizon would close this one remaining bridge.

There is also a nonessential presentational gap: the explicit polynomial
for \(J_{p,q}\) is asserted rather than derived in this note.  The no-go
requires only \(|\kappa_t|\le C_{p,q}t^2\), which follows from the universal
cubic Newton formula once coefficient convergence is justified.  Therefore
the unproved displayed coefficients of \(J_{p,q}\) are not needed for the
obstruction.

## 1. Audit of coefficientwise monotonicity

Work in the semiring

\[
 \mathcal R_+=\mathbb R_+[x_1,\ldots,x_d,h,\lambda].
\]

The elementary substitution fact needed by the proof is:

> If \(P,U_1,\ldots,U_d,R_1,\ldots,R_d\in\mathcal R_+\), then
> \(P(U+R)-P(U)\in\mathcal R_+\).

It suffices to check a monomial.  The product

\[
 \prod_j(U_j+R_j)^{\nu_j}-\prod_jU_j^{\nu_j}
\]

is the sum of precisely those binomial-expansion terms which choose at
least one \(R_j\), so every coefficient is nonnegative.

For \(g_\lambda=g_0+\lambda g_1\), with \(g_0,g_1\) coefficientwise
positive, let

\[
 E_\lambda(x)=x+hg_\lambda(x),\quad
 A_\lambda=E_\lambda\circ E_\lambda,\quad
 B_\lambda(x)=x+2hg_\lambda(x).
\]

Then

\[
 A_\lambda=B_\lambda+L_\lambda,qquad
 L_\lambda=h\{g_\lambda(x+hg_\lambda(x))-g_\lambda(x)\},
\]

and the substitution fact proves \(L_\lambda\in\mathcal R_+^d\), jointly
in \((x,h,\lambda)\).  If
\(A_\lambda^s=B_\lambda^s+R_s\), with \(R_s\in\mathcal R_+^d\), then

\[
\begin{aligned}
A_\lambda^{s+1}-B_\lambda^{s+1}
={}&B_\lambda(B_\lambda^s+R_s)-B_\lambda(B_\lambda^s)\\
&+L_\lambda(A_\lambda^s)\in\mathcal R_+^d.
\end{aligned}
\]

The induction starts at \(s=1\).  Composing with a positive observable
preserves the order.  Hence the paired defect is a polynomial in
\(\lambda\) with nonnegative coefficients.  Its \(\lambda^0\) coefficient
is exactly the defect for \(g_0\), while its value at \(\lambda=1\) is the
full defect.  The claimed deletion monotonicity is therefore valid; it is
not an illicit pointwise comparison at negative state values.

For \(p,q\ge0\), the reduced network coordinates

\[
H=pu+qu^2,quad z=n^{-1/2}WH,quad
C=a(p+2qz),quad b=n^{-1/2}W^TC
\]

all have nonnegative coefficients in the formal raw variables.  So do the
three ascent blocks \(\psi(z)\), \(CH\), and \(b\psi'(u)\), and the
observable \(a\psi(z)\).  Deleting the last block is exactly a decomposition
\(g=g_0+g_1\) of the type just proved.  This part passes.

## 2. Audit of Gaussian expectation

At finite width the formal variables \((a_i,W_{ij},u_j)\) are independent
standard Gaussians.  For a monomial \(X^\nu\),

\[
 \mathbb E X^\nu
 =\prod_k\mathbb E G^{\nu_k},
\]

which is zero if some \(\nu_k\) is odd and strictly positive otherwise.
Thus applying expectation to a coefficientwise-positive polynomial cannot
create a negative coefficient in \((h,\lambda)\).  All moments are finite
because the horizon is fixed and the integrand is a finite polynomial.
Consequently the finite-width inequality

\[
 \Delta^{\rm full}_{t,n}(h)
 \ge \Delta^{\rm frozen}_{t,n}(h),\qquad h\ge0,
\]

is valid.

This argument uses independence of the *initial raw variables*, not any
false independence of trained coordinates.  The trained coordinates have
already been expanded as polynomials of the independent initialization.

## 3. Frozen-block limit

When the \(u\)-update is deleted, \(H_j=\psi(u_j^0)\) is fixed and

\[
 Q_n=\frac1n\sum_jH_j^2.
\]

The exact updates imply

\[
 A^+=A+h\psi(Z),qquad
 Z^+=Z+hQ_nA\psi'(Z).
\]

Conditional on the first layer, \(A\sim N(0,1)\),
\(Z\sim N(0,Q_n)\), independently.  Since \(Q_n\to1\) in every
\(L^r\) and a fixed-horizon output is polynomial in \((A,Z,Q_n)\), its
expectation converges to the two-dimensional recursion in the proposed
proof.  Therefore the frozen width limit is rigorously identified.

Passing the finite-width inequality to

\[
 \Delta_t(h)\ge D_t(h)
\]

is valid whenever the full fixed-\((t,h)\) limit defining \(\Delta_t\)
exists.  This is exactly where the missing full quadratic width-limit lemma
enters; no other limit interchange is hidden here.

## 4. Audit of the all-order monomial and coarse subtraction

For the scalar recursion, let \(\delta_N=2^N-1\).  The degree recurrence is

\[
 d_{N+1}=1+2d_N,qquad d_0=0,
\]

so both state coordinates have maximal \(h\)-degree \(\delta_N\) when
\(q\ne0\).

At the first update, the top \(h\)-degree contains both the linear and the
quadratic activation choices.  Hence it would be false to claim that the
entire leading coefficient is a single monomial.  The revised statement in
the proposed theorem correctly uses \(\succeq\): select only \(qZ^2\) and
\(2qAZ\), and thereafter select their recursively generated quadratic
highest-degree terms.  Coefficientwise positivity ensures that all omitted
terms only increase the coefficient.

Starting from

\[
(r_0,s_0)=(1,0),\qquad(u_0,v_0)=(0,1),\qquad c_0=d_0=1,
\]

the selected branch obeys

\[
\begin{aligned}
c_{N+1}&=d_N^2,&(r_{N+1},s_{N+1})&=2(u_N,v_N),\\
d_{N+1}&=2c_Nd_N,&(u_{N+1},v_{N+1})&=(r_N+u_N,s_N+v_N).
\end{aligned}
\]

Thus both raw-variable degrees equal \(2^N\).  For \(N\ge1\), the selected
\(A_N\) exponent pair is even-even and the selected \(Z_N\) pair is
odd-odd.  The selected contribution in
\(qA_NZ_N^2\) therefore has even exponents, total degree \(3\cdot2^N\),
and strictly positive Gaussian expectation.

The output's maximal \(h\)-degree is

\[
 m_N=3(2^N-1).
\]

There is a sharper exact check on the selected exponents at the even horizon
\(N=2t\).  Across two selected quadratic updates, the exponent column for
either raw source is multiplied by

\[
 M=\begin{pmatrix}2&2\\1&3\end{pmatrix}.
\]

The output monomial \(A_{2t}Z_{2t}^2\) applies the row vector \((1,2)\),
and

\[
 (1,2)M=4(1,2).
\]

Starting from source-exponent columns \((1,0)^T\) and \((0,1)^T\) gives

\[
 R_{2t}=4^t,
 \qquad S_{2t}=2\cdot4^t.                           \tag{A.1}
\]

This independently verifies parity and the total
\(R_{2t}+S_{2t}=3\cdot4^t\), and yields a stronger moment lower bound than
the pigeonhole estimate used in the proposal.

The coarse polynomial \(F_t(2h)\) has degree \(m_t<m_{2t}\), so it has no
coefficient at \(h^{m_{2t}}\).  Moreover the positive-polynomial lemma
shows that every coefficient of the full scalar defect
\(D_t=F^{\rm scalar}_{2t}(h)-F^{\rm scalar}_t(2h)\) is nonnegative.
Therefore the selected fine monomial survives coarse subtraction and gives
the stated pointwise lower bound for every \(h>0\).  This step passes.

## 5. Growth calculation

At \(N=2t\), the selected Gaussian exponents satisfy

\[
 R_{2t}+S_{2t}=3\cdot4^t.
\]

They are even, so one is \(2m\) with
\(m\ge3\cdot4^t/4\).  Since

\[
 \mathbb EG^{2m}=(2m-1)!!\ge m!\ge(m/e)^m,
\]

the lower bound \(L_t\) in the proposal is valid.  More explicitly,

\[
\begin{aligned}
\frac{log L_t}{4^t}
={}&\left(3-\frac2{4^t}\right)\log q
 +\left(3-\frac3{4^t}\right)(\log\rho-\log t)\\
&+\frac34\left(t\log4+\log\frac3{4e}\right).
\end{aligned}
\]

For fixed \(q>0\) and \(\rho>0\), the positive linear term
\(\frac34t\log4\) dominates \(3\log t\) and all constants.  Hence
\(L_t\to\infty\).  This remains true for arbitrarily small but fixed
\(q\ne0\); it is not uniform if \(q=q_t\to0\) with the horizon.

## 6. Signs

The conjugacies are correct.  First,

\[
 \psi_{p,-q}(-x)=-\psi_{p,q}(x),
\]

and \(R_1(a,W,u)=(-a,W,-u)\) makes the lower feature and top activation
both change sign while the readout also changes sign, giving
\(f_{p,-q}(R_1\theta)=f_{p,q}(\theta)\).  Second,
\(R_2(a,W,u)=(-a,-W,u)\) conjugates simultaneous replacement
\(\psi\mapsto-\psi\).  Both maps are orthogonal and preserve the Gaussian
initialization law.  Differentiating the output identities conjugates the
gradient Euler maps.  These two operations generate all sign choices of
\((p,q)\), so reduction to \((|p|,|q|)\) is valid.

## 7. Does the argument really refute the uniform remainder?

Yes, under the fixed-step existence proviso.  At \(h=\rho/t\),

\[
 \Delta_t(h)\ge L_t\to\infty,
\]

whereas the cubic term is only \(O_{p,q}(t^2h^3)=O_{p,q}(1/t)\).  Therefore

\[
 |\Delta_t(\rho/t)-\kappa_t(\rho/t)^3|\to\infty.
\]

The proposed right-hand side satisfies

\[
 Ct^4(\rho/t)^5=C\rho^5/t\to0.
\]

Thus one endpoint of every claimed interval already contradicts the bound.
In fact \(L_t\) dominates every fixed polynomial, so replacing \(t^4\) by
\(t^r\), for any fixed \(r\), does not help.

The quantifiers are important:

- \(q\ne0\) is fixed before \(t\to\infty\);
- \(\rho>0\) is fixed before \(t\to\infty\);
- the proof uses the allowed positive endpoint \(h=\rho/t\);
- it does not rule out horizons depending on \(q\), nonlinear amplitudes
  \(q_t\to0\), or step windows shrinking faster than \(1/t\).

Finally, this does not contradict the exact local result
\([h^5]\Delta_t=O(t^4)\).  The obstruction comes from a coefficient whose
order \(3(4^t-1)\) itself grows with \(t\), so no fixed-order jet can see it.

## Required correction before unconditional release

Replace the phrase “as in the established OMFP construction” by one of the
following:

1. explicitly assume that \(F_N(h)=\lim_n\mathbb Ef_n(\theta_N)\) exists
   and is finite for every fixed \((N,h)\); or
2. add a direct fixed-horizon polynomial/Wick theorem proving that limit for
   quadratic \(\psi\).

Also either derive the displayed \(J_{p,q}\) polynomial from the audited
cubic compiler or replace it by an activation-defined finite constant
\(C_{p,q}\).  With these qualifications, the no-go proof passes.
