# Proof contract: generic H=2, B=1 correction through order five

Status: frozen before the order-five computation.

## 1. Model and limit order

We use exactly

\[
u_j=\frac{w_j^\top x}{\sqrt{d_0}},\qquad
z_i=\frac1{\sqrt n}\sum_{j=1}^nW_{ij}\phi(u_j),\qquad
f_n=\frac1n\sum_{i=1}^na_i\phi(z_i),
\]

with independent standard-Gaussian initialization and

\[
D_n=n\nabla f_n\cdot\nabla,\qquad
F^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n].
\]

Every differentiation is performed at finite width before any limit.  The
primary calculation treats deterministic forward variances first and is then
specialized to \(Q^0=Q^1=Q^2=1\).

## 2. Required terminal language

For the unit-Gram result the only nonlinear atoms allowed are

\[
M_{\nu_0\nu_1\cdots\nu_R}
=\mathbb E_{G\sim N(0,1)}
 \prod_{r=0}^R\phi^{(r)}(G)^{\nu_r}.
\]

The displayed formulas for \(A=F'(0)\), \(B=F^{(3)}(0)\), and
\(C=F^{(5)}(0)\) must be finite deterministic arithmetic expressions in
these atoms.  A canonically factored expression or an emitted sparse
polynomial is acceptable if every coefficient and monomial is explicit.

Forbidden from the terminal result are tangent variables, backward carriers,
Gaussian innovations, pseudoinverses, implicit Stein derivatives, empirical
covariances, unnamed covariances, or instructions to evaluate a recursion.
Any multivariate Gaussian atom that survives must display its complete
covariance, constructed only from the forward Grams.  The preferred result
eliminates all such atoms into products of one-dimensional moments.

No Hermite or polynomial approximation of \(\phi\) is permitted.

## 3. Exact finite-width identity to audit

In whitened coordinates \(\vartheta=\theta/\sqrt n\), put
\(p=\nabla_\vartheta f\), \(H=\nabla_\vartheta^2f\),
\(T=\nabla_\vartheta^3f\), \(U=\nabla_\vartheta^4f\), and
\(V=\nabla_\vartheta^5f\).  Since
\(D_n=p\cdot\nabla_\vartheta\), the proposed six-family identity is

\[
\boxed{
D_n^5f_n=
2V[p,p,p,p,p]
+22U[Hp,p,p,p]
+14T[T[p,p],p,p]
+30T[H^2p,p,p]
+36T[Hp,Hp,p]
+16\lVert H^2p\rVert^2.}
\]

This identity is a candidate until independently differentiated, checked in
raw coordinates with all powers of \(n\), and matched to an independent
Taylor-jet implementation.

## 4. Claim ladder and mandatory gates

No theorem-level promotion occurs until all gates pass:

1. exact finite-width order-five identity, including all six families;
2. complete equality-partition, width-counting, Wick--Stein, and transpose-
   response ledger;
3. two independently implemented atom canonicalizers agree coefficientwise;
4. readout parity gives \(F(0)=F''(0)=F^{(4)}(0)=0\);
5. exact controls:
   \(\phi(x)=x\) gives \((A,B,C)=(3,48,1464)\), and
   \(\phi(x)=x^2\) gives
   \((111,1685184,77400633120)\);
6. constant and affine controls plus a preregistered smooth nonpolynomial
   finite-width regression;
7. a precise large-width probability bridge and uniform-integrability
   statement;
8. explicit separation of finite-width identities, formal candidates,
   algebraically audited forms, and theorem-level limits.

If flattening fails, the deliverable is an exact unresolved-branch ledger;
no response recursion may be substituted for \(C\).

## 5. Preregistered nonpolynomial experiment

Use

\[
\phi(x)=\frac{\sin x}{\sqrt{\mathbb E\sin^2G}},\qquad G\sim N(0,1),
\]

so that the unit forward variance is preserved at both hidden layers.  Before
looking at Monte Carlo output, first require seedwise equality of two exact
finite-width order-five jet implementations.  Then compare the flattened
prediction with a weighted affine extrapolation in \(1/n\).

- pass: prediction and extrapolated intercept differ by at most 3 standard
  errors;
- fail: a replicated difference greater than 5 standard errors;
- inconclusive: 3--5 standard errors or failed extrapolation diagnostics.

Only an otherwise valid inconclusive experiment may be enlarged.  The cap is
10,000 networks and width 512.

## 6. Large-width theorem envelope

The intended theorem tier assumes that \(\phi\) is polynomially smooth:
\(\phi\in C^\infty\) and every derivative is polynomially bounded.  This is
the envelope under which the exact fixed tensor program has almost-sure and
all-finite-\(L^p\) convergence, hence uniform integrability and convergence of
expectations.  A merely finite-order \(C^5\) assumption belongs only to the
finite algebraic identity unless a separate moment/UI proof is supplied.

## 7. Derived quantities

Only after \(A,B,C\) pass the gates define

\[
\mu_0=\frac{B}{2A^2},\qquad
\mu_1=\frac{4B^2-AC}{24A^5},
\]

and construct the Padé approximation to \(K(y)=F'(F^{-1}(y))\), not directly
to the loss curve.

