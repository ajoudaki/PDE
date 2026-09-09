# Adversarial audit of the quadratic uniform no-go theorem

## Verdict

**PASS.** The coefficientwise comparison with the frozen lower block, the
distinguished pure-quadratic all-order monomial, the Gaussian-moment lower
bound, and the activation-sign conjugacies have no sign or cancellation
defect.

The fixed-horizon annealed width limit for the unbounded quadratic activation
is supplied by `FIXED_H_QUADRATIC_WIDTH_LEMMA.md`.  That lemma expands every
trained connector exactly into the finite action list of the initialized
Gaussian matrix and its transpose, then invokes the all-finite-\(L^r\)
polynomially-smooth fixed-program theorem whose hypotheses are checked in
`generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md`, Section 3.1.  A
quadratic is polynomially smooth, the horizon is fixed before the theorem is
applied, and the resulting \(L^1\) convergence is exactly the annealed bridge
needed for (3.3).  No time-uniform estimate is imported.  The separate manual
stopping construction in `FIXED_H_QUADRATIC_BRIDGE.md` is not used.

## 1. Positive-polynomial comparison

Write

\[
 E_{h,\lambda}=I+h(g_0+\lambda g_1),
\]

where \(g_1\) is exactly the deleted \(u\)-coordinate update. If \(p,q\ge0\),
the observable and every coordinate of \(g_0,g_1\) are polynomials with
nonnegative coefficients in the raw network coordinates. Differentiating the
positive-coefficient network polynomial does not introduce a negative
coefficient.

Set \(B_\lambda=E_{2h,\lambda}\) and
\(A_\lambda=E_{h,\lambda}^2=B_\lambda+L_\lambda\). For a monomial of
\(g_0+\lambda g_1\), subtracting its value at \(x\) from its value at
\(x+h(g_0+\lambda g_1)(x)\) removes only the product term that selects the
old coordinate in every factor. Every surviving term is positive. Thus
\(L_\lambda\succeq0\) jointly in \((x,h,\lambda)\).

If \(A_\lambda^s=B_\lambda^s+R_s\), \(R_s\succeq0\), then

\[
 A_\lambda^{s+1}-B_\lambda^{s+1}
 =B_\lambda(B_\lambda^s+R_s)-B_\lambda(B_\lambda^s)
  +L_\lambda(B_\lambda^s+R_s)\succeq0.
\]

Hence the paired defect has nonnegative coefficients jointly in \(\lambda\).
Its \(\lambda^0\) coefficient is exactly the frozen-\(u\) paired defect and
is a coefficientwise sub-polynomial of the full defect at \(\lambda=1\).
Expectation over independent centered raw Gaussians preserves the inequality:
odd monomials average to zero and even monomials to positive products of
double factorials. Equation (2.1) is therefore correct.

Deleting the \(u\)-update need not leave a gradient vector field. This is
irrelevant: the comparison lemma requires only a positive polynomial vector
field.

## 2. Frozen-block embedding and width passage

With \(H_j=\psi(u_j)\) fixed,

\[
 Q_n=\frac1n\sum_jH_j^2,\qquad
 a_i^+=a_i+h\psi(z_i),\qquad
 z_i^+=z_i+hQ_na_i\psi'(z_i).
\]

The factor \(Q_n\) and the factor \(2\) in
\(\psi'(z)=p+2qz\) are correct. Conditional on \((H_j)\), the row pairs are
iid with independent

\[
 a_i^0\sim N(0,1),\qquad z_i^0\sim N(0,Q_n).
\]

Since \(Q_n\to E\psi(G)^2=1\) in every finite moment, and a fixed-horizon
output is a finite polynomial in \((a_i^0,z_i^0,Q_n)\), its expectation
converges to the scalar recursion (3.2). This part is unconditional.

At finite width,

\[
 \Delta_{t,n}^{\rm full}(h)\ge
 \Delta_{t,n}^{\rm frozen}(h).
\]

Taking limits preserves this inequality once the full-network annealed limit
is available. This is the only place where the missing quadratic fixed-step
bridge is needed.

For each fixed \((N,h)\), the full trained quadratic network is a finite
NETSOR-transpose-type program: finitely many \(W/W^\top\) multiplications,
coordinatewise polynomials, products, and empirical scalar averages. The
quadratic activation is \(C^\infty\) and every derivative has polynomial
growth. The polynomially-smooth finite-program result recorded in the local
probability audit gives almost-sure and \(L^r\) convergence for every finite
\(r\), hence annealed convergence of the terminal average. Its relevant
hypotheses hold:

1. program length \(2N+1\) is finite during the width limit;
2. initialization is independent Gaussian;
3. all coordinate maps are polynomially smooth; and
4. the terminal output is a scalar of the same finite program.

The main theorem should cite this bridge explicitly. Citing only the
at-most-linear-growth theorem would be invalid.

## 3. Highest-degree term

For

\[
 A^+=A+h(pZ+qZ^2),\qquad Z^+=Z+hA(p+2qZ),
\]

put \(\delta_N=2^N-1\). At \(N=1\), the degree-one coefficients also
contain the linear-activation branches \(pZ_0\) and \(pA_0\). What is
needed is the following distinguished pure-\(q\) monomial containment:

\[
 [h]A_1\ \supset\ qZ_0^2,
 \qquad [h]Z_1\ \supset\ 2qA_0Z_0.
\]

Here \(\supset\) means that the displayed monomial occurs with the displayed
positive coefficient, not equality of the full coefficient. Inductively
select these monomials inside \(A_N,Z_N\). Feeding them through the quadratic
branches \(hqZ_N^2\) and \(2hqA_NZ_N\) produces selected monomials at degree
\(1+2\delta_N=\delta_{N+1}\), with coefficients

\[
 c_{N+1}=d_N^2,\qquad d_{N+1}=2c_Nd_N.
\]

The selected \(A_N\) monomial is even-even in \((A_0,Z_0)\), while the
selected \(Z_N\) monomial is odd-odd; the recurrence preserves these
parities. Other \(p\)-containing monomials can occur at the same
\(h\)-degree, but all raw coefficients are nonnegative, so none can cancel
the selected branch. Selecting the outer quadratic branch \(qA_NZ_N^2\)
therefore gives a contained output monomial of degree \(3\delta_N\) whose
Gaussian expectation is strictly positive. Uniqueness is neither true nor
needed.

Two exact low-order checks are

\[
 [h^3]E[A_1\psi(Z_1)]
 \quad\text{contains the contribution }12q^4,
\]

and

\[
 [h^9]E[A_2\psi(Z_2)]
 \quad\text{contains the contribution }
 64q^{10}E[A_0^4]E[Z_0^8]=20160q^{10}.
\]

These selected contributions agree with
\(c_Nd_N^2q^{3\delta_N+1}\) and rule out a missing factor of two in the
distinguished branch. The coarse \(t\)-step polynomial has degree at most
\(3(2^t-1)\), strictly
below the retained fine-grid degree \(3(4^t-1)\). Positivity of the complete
paired defect justifies retaining this single fine-grid coefficient.

## 4. Gaussian moment lower bound

The two even exponents of the retained \(N=2t\) term sum to \(3\cdot4^t\).
If the larger is \(K=2m\), then

\[
 K\ge\frac32\,4^t,\qquad
 EG^K=(2m-1)!!\ge m!\ge(m/e)^m.
\]

For all sufficiently large \(t\), the base is greater than one, so

\[
 EG^K\ge
 \left(\frac{3\,4^t}{4e}\right)^{3\,4^t/4}.
\]

At \(h=\rho/t\), the logarithm of the retained term divided by \(4^t\) is

\[
 \frac34t\log4-3\log t+3\log(q\rho)+O(1),
\]

which tends to \(+\infty\) for every fixed \(q,\rho>0\). Dropping the
integer factor \(c_{2t}d_{2t}^2\ge1\) only weakens the lower bound.

The independently compiled cubic term is only quadratic in \(t\); at
\(h=\rho/t\) it is \(O(t^{-1})\). Its subtraction cannot affect the
divergence. The same argument defeats any fixed polynomial in \(t\)
multiplying \(h^5\).

## 5. Activation signs

The identities are valid through both hidden layers:

\[
 \psi_{p,-q}(-x)=-\psi_{p,q}(x).
\]

For \(R_1(a,W,u)=(-a,W,-u)\), the lower feature, middle preactivation, and
top feature each change sign in the needed order, and the readout sign
cancels:

\[
 f_{p,-q}(R_1\theta)=f_{p,q}(\theta).
\]

For \(R_2(a,W,u)=(-a,-W,u)\), replacing \(\psi\) by \(-\psi\) changes the
lower feature sign, the simultaneous \(W\)-sign change restores the middle
preactivation, and the top/readout signs cancel:

\[
 f_{-p,-q}(R_2\theta)=f_{p,q}(\theta).
\]

Both maps are orthogonal. Differentiating \(f_2(R_i\theta)=f_1(\theta)\)
gives

\[
 \nabla f_2(R_i\theta)=R_i\nabla f_1(\theta),
\]

so the discrete Euler maps are conjugate at the same positive step. Gaussian
initialization is invariant. These operations generate all four sign choices.

## Final status

With `FIXED_H_QUADRATIC_WIDTH_LEMMA.md` as the width bridge, the theorem is
unconditional and the audit verdict is **PASS**.  No issue was found in the
nonlocal obstruction itself.
