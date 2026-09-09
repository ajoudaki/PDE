# Adversarial audit: uniform time-doubling bound

## Verdict

- **Abstract transported-defect theorem:** **PASS in substance.**  The
  pullback telescoping order, the exact factor (h^2), the parity reduction,
  and the (t^4) count are correct.  The displayed recursion gives finite
  constants depending only on the Banach-space derivative bound (K).
- **Instantiation for the actual reused-matrix population MLP:** **OPEN.**
  Under the stated (C^{12}), bounded-derivative, at-most-linear-growth
  activation assumptions, the current study does not prove the required
  horizon-independent generated-core (C^4) estimate.  Consequently (5.2)
  is conditional on (mathrm{UGC}_4(phi,L)), exactly as the note says.

No counterexample to the proposed (t^4) inequality was found.  The linear
one-hidden-layer model instead proves that the power (t^4) cannot in
general be reduced.

## 1. Exact algebra and pullback order

With (P_Mu=u\circ M), composition reverses:

\[
 P_MP_N=P_{N\circ M}.
\]

Nevertheless (P_M^t=P_{M^t}), and the noncommutative identity

\[
 A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j
\]

applied to (A=P_C), (B=P_B) gives the displayed formula (2.7).  Indeed,
the (j)-th term first reaches (C^{t-1-j}\theta _0), inserts the local
(C-B) defect there, and transports it through (j) fine macro-steps.
Thus there are exactly (t) transported defects; commutativity of (B) and
(C) is never used.

The identity

\[
 B_hx=C_hx+h^2a_h(x),\qquad
 a_h(x)=\int_0^1Dg(x+shg(x))g(x)\,ds
\]

is exact, and the sign in (2.4) is correct because

\[
 u(C_hx)-u(B_hx)
 =-h^2\int_0^1Du(C_hx+sh^2a_h(x))[a_h(x)]\,ds.
\]

Hence (d_t(h)=h^2Q_t(h)) exactly.

## 2. Parity and remainder factor

If (d_t) is odd and (Q_t\in C^3), then (Q_t) is odd, including at
zero by continuity.  Therefore (Q_t(0)=Q_t''(0)=0), and Taylor's integral
formula gives

\[
 |d_t(h)-Q_t'(0)h^3|
 \le \frac{|h|^5}{6}\sup_{|s|\le |h|}|Q_t'''(s)|.
\]

The factor (1/6) is correct.  Combining it with the definition

\[
 C_K=\frac16\sum_{q=0}^3{3\choose q}H_qW_{3-q}
\]

and the (t) summands in (Q_t) gives precisely (C_Kt^4|h|^5), with no
missing factor of two.

## 3. Audit of the (t)-powers and recursive constants

For every relevant pre-defect path, the total Euler coefficient is at most
(2t); the proof uses the harmless larger allowance (4t).  The homogeneous
tangent product is therefore bounded by

\[
 \exp\!\left(K|h|\sum_m\alpha_m\right)
 \le e^{4c_KK}<2.
\]

Direct differentiation gives normalized path jets of orders one, two, and
three proportional to (t,t^2,t^3).  The coefficients inside (4.3)--(4.5)
are respectively the sums obtained from (4.14)--(4.16), followed by the
homogeneous factor two.  The interpolation
(x+shg(x)) occurring in (a_h) is itself the old variable-step path with
one appended step of coefficient (s\in[0,1]); for the actual telescoping
paths its total coefficient remains below (4t).  This justifies using the
same (X_r) bounds for the two factors in (4.7).  This point is implicit in
the proof and should be made explicit in a release version, but it does not
alter the constants.

Similarly, (C_hx) is another admitted variable-step path, while the
derivatives of its added (h^2a_h) displacement are exactly the four terms
in (4.8).  The post-defect fine path has total coefficient at most (2t),
which accounts for the coefficients (2,4,6) and (2c) in (4.9).
Differentiating the transported tangent leaves three step-size derivatives,
each costing at most one factor (t); summing over the (t) local defects
therefore gives (t\cdot t^3=t^4).

The definitions (4.3)--(4.12) have only the fixed indices (0,1,2,3), and
each quantity uses only previously defined quantities.  They terminate.

## 4. Linear (L=1) falsification test

Take the allowed normalized activation (phi(x)=x).  One population
coordinate obeys

\[
 a^+=a+hu,\qquad u^+=u+ha,
\]

with independent standard Gaussian (a,u).  Diagonalizing with
(v_\pm=(a\pm u)/\sqrt2) gives the exact expected output

\[
 F_{N,1}(h)
 =\frac{(1+h)^{2N}-(1-h)^{2N}}2.
\]

Consequently

\[
 D_{t,1}(h)
 =\frac12\left\{(1+2h)^{2t}-(1-2h)^{2t}
 -(1+h)^{4t}+(1-h)^{4t}\right\}.
\]

Its cubic coefficient is

\[
 8{2t\choose3}-{4t\choose3}=-4t(2t-1),
\]

and its fifth coefficient is

\[
 32{2t\choose5}-{4t\choose5}
 =-\frac43t(t-1)(2t-1)(8t-9).
\]

For (t\ge2) this is nonzero and has leading size
(-\frac{64}{3}t^4).  Thus a uniform remainder with a power below (t^4)
is impossible.  The example is consistent with, and makes sharp, the
proposed (t^4) estimate; it does not falsify it.

## 5. Precise network obstruction

The fixed-operator bridge proves only fixed-finite-history facts:
generated fields have all moments, response identities hold, and scalar
maps along each finite generated list are differentiable.  It gives no
constant uniform in the number of exposed history directions.

This deficit cannot be repaired by treating the connector adjoint as an
ambient (L^p)-bounded operator.  For (p>2), choose
(c\in L^2(\Omega_a)\setminus L^p(\Omega_a)).  Since (J_a) maps every
Hilbert vector into first Gaussian chaos, (x=J_ac) is Gaussian and belongs
to every finite (L^q).  But

\[
 J_a^*x=J_a^*J_ac=c\notin L^p.
\]

Nor is nonlinear pointwise activation a globally (C^2) map
(L^2\to L^2): multiplication (L^2\times L^2\to L^2) is unbounded.
Therefore the Banach-space hypotheses cannot be inferred from
(W_{a,0}=I_a+J_a^*) being bounded on (L^2).

What is missing is a genuinely dynamical estimate, uniform in the horizon,
for the generated response sums and their first three step-size
derivatives in suitable (L^p) norms, depending only on total step
variation.  No such estimate is proved by the fixed-operator bridge or by
the fixed-horizon Price compiler.  Until it is supplied, the actual-network
uniform theorem must be labelled conditional/open.

