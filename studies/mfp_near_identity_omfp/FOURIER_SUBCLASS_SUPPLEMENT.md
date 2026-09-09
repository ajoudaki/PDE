# Finite-Fourier and finite-chaos supplement

Date: 25 August 2026.

## 1. Question and conclusion

This note tests whether the near-identity program closes after restricting the
residual to a finite Fourier or Bernstein class and retaining finitely many
chaos/provenance marks.

The conclusion is negative for that finite closure:

\[
 \boxed{
 \text{finite Fourier residual}
 +
 \text{finite chaos/provenance ledger}
 \not\Longrightarrow
 \text{the required aggregate-adjoint estimate}.}
 \tag{1.1}
\]

There are three rigorous reasons.

1. No genuinely nonlinear, globally at-most-linear activation is a finite
   Gaussian-chaos function. The proposed finite-chaos admissible subclass is
   empty.
2. Every nonconstant finite Fourier residual has infinitely many Hermite
   chaoses already at its first application to a Gaussian.
3. The exact amplitude expansion first needs a new estimate at order three:
   a uniform \(L^4\) bound for \(J^*x^{\langle1\rangle}\), including moving
   step/source jets. Finite Fourier coefficients do not imply this estimate,
   and a finite derivative/provenance ledger cannot represent the recursively
   reused Gaussian adjoint exactly.

An all-order analytic/Fock **scale**, combined with causal step weights, is
still a viable research route. This audit does not rule it out. It proves
that the finite-Fourier restriction does not by itself finish the \(L=2\)
theorem and that a fixed finite-chaos or finite-response closure cannot do so.

## 2. Explicit finite-Fourier class

For \(K\ge1\) and \(R\ge1\), let

\[
 \varphi(x)
 =
 a_0+
 \sum_{\nu=1}^{K}
 \left(
 a_\nu\cos(\lambda_\nu x)
 +
 b_\nu\sin(\lambda_\nu x)
 \right),
 \tag{2.1}
\]

where

\[
 \sum_{\nu=1}^{K}
 (|a_\nu|+|b_\nu|)
 (1+|\lambda_\nu|)^{12}
 +|a_0|
 \le R.
 \tag{2.2}
\]

This gives

\[
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R.
 \tag{2.3}
\]

Define

\[
 \psi_\varepsilon(x)
 =
 \frac{x+\varepsilon\varphi(x)}
 {\left(\mathbb E[G+\varepsilon\varphi(G)]^2\right)^{1/2}},
 \qquad G\sim N(0,1).
 \tag{2.4}
\]

For \(|\varepsilon|R\le1/4\), the normalization lies in
\([3/4,5/4]\), and every derivative of order at least two is bounded by
\((4/3)|\varepsilon|R\). This is an explicit genuinely nonlinear class
whenever the trigonometric polynomial in (2.1) is nonconstant.

## 3. The finite-chaos admissible subclass is empty

Let \(\mathcal H_m\) denote the \(m\)-th Wiener chaos of one standard
Gaussian.

### Theorem 3.1

Suppose \(f:\mathbb R\to\mathbb R\) is continuous, has at most linear
growth, and

\[
 f(G)\in\bigoplus_{m=0}^{M}\mathcal H_m
 \tag{3.1}
\]

for some finite \(M\). Then \(f\) is affine.

#### Proof

The one-dimensional chaos space
\(\bigoplus_{m=0}^{M}\mathcal H_m\) consists exactly of polynomials in
\(G\) of degree at most \(M\). Hence there is a polynomial \(P\) such that

\[
 f(G)=P(G)
 \quad\text{almost surely}.
 \tag{3.2}
\]

The Gaussian law has a strictly positive density on all of \(\mathbb R\).
Therefore \(f=P\) Lebesgue-almost everywhere. Since both functions are
continuous, \(f=P\) everywhere. A polynomial with at most linear growth has
degree at most one. Thus \(f\) is affine. \(\square\)

### Corollary 3.2

If \(\psi_\varepsilon\) from (2.4) is genuinely nonlinear, then
\(\psi_\varepsilon(G)\) has infinitely many nonzero Wiener-chaos
components.

This is not merely a defect of sine. It rules out every proposed
finite-chaos nonlinear subclass under the admissible growth condition.

## 4. A finite Fourier sum is not a finite Hermite sum

For the probabilists' Hermite polynomials,

\[
 e^{tx-t^2/2}
 =
 \sum_{m=0}^{\infty}\frac{t^m}{m!}H_m(x).
 \tag{4.1}
\]

Putting \(t=i\lambda\) gives the exact \(L^2(\gamma)\) expansion

\[
 e^{i\lambda G}
 =
 e^{-\lambda^2/2}
 \sum_{m=0}^{\infty}
 \frac{(i\lambda)^m}{m!}H_m(G).
 \tag{4.2}
\]

For \(\lambda\ne0\), every coefficient in (4.2) is nonzero. Sine retains
all odd orders and cosine retains all even orders. More generally, if a
nonconstant trigonometric polynomial had only finitely many Hermite
coefficients, Theorem 3.1 would make it a bounded polynomial and hence a
constant, a contradiction.

The earlier sine compiler's “finite Fourier” reduction concerns something
different. At one **fixed derivative order**, products of finitely many
sines and cosines reduce to a finite set of frequencies before taking a
Gaussian expectation. It explicitly does not establish convergence in
derivative order, positive time, or a recursively invariant Fourier state.

Thus a Fourier atom is a useful exact integration label, but it is not a
finite-chaos state label.

## 5. Scalar derivative closure does not give source-response closure

The span of \(\sin(\lambda x)\) and \(\cos(\lambda x)\) is invariant under
ordinary differentiation in \(x\). This does not close Malliavin derivatives
after the argument becomes an adaptive random field.

For a smooth random field \(z\),

\[
 D\sin(\lambda z)
 =
 \lambda\cos(\lambda z)\,Dz,
 \tag{5.1}
\]

and repeated differentiation gives

\[
 D^r e^{i\lambda z}
 =
 e^{i\lambda z}
 B_r\!\left(
 i\lambda Dz,\ldots,i\lambda D^rz
 \right),
 \tag{5.2}
\]

where \(B_r\) is the complete Bell polynomial. Therefore an exact
\(r\)-fold response requires \(D^rz\). The Fourier frequency label does not
encode this inner response graph.

Even for \(z=G\),

\[
 D^re^{i\lambda G}
 =
 (i\lambda)^re^{i\lambda G}\ne0
 \qquad(r\ge0).
 \tag{5.3}
\]

Hence no truncation at a fixed response order is exact under arbitrarily
many reused Gaussian integration-by-parts operations.

### Proposition 5.1

A finite alphabet consisting of Fourier frequencies and Malliavin/source
marks through a fixed order \(r_0\) is not invariant under the exact
moving-query aggregate-adjoint recursion.

#### Proof

For one Gaussian coordinate, the divergence identity is

\[
 \delta(u)=Gu-Du.
 \tag{5.4}
\]

One creation-response reduction of an adapted query requires \(Du\).
Applying the same reduction to the resulting moving query requires
\(D^2u\), and after \(r_0+1\) reductions it contains
\(D^{r_0+1}u\). Taking \(u=e^{i\lambda G}\), (5.3) shows this term is
nonzero. For a composed query, (5.2) additionally requires
\(D^{r_0+1}z\). Neither object is in the proposed finite ledger.
\(\square\)

Proposition 5.1 does not say that all-order analytic marks cannot work. It
says that a finite mark set does not provide exact closure.

## 6. No single diagonal Fock norm repairs the problem

Let

\[
 X=\sum_{m\ge0}x_mh_m,
 \qquad
 h_m=\frac{H_m}{\sqrt{m!}},
 \tag{6.1}
\]

and consider a diagonal Hilbert norm

\[
 \|X\|_w^2=\sum_{m\ge0}w_m|x_m|^2.
 \tag{6.2}
\]

Assume it controls \(L^2\), so there is \(c>0\) with \(w_m\ge c\) for all
\(m\). Gaussian creation satisfies

\[
 a^\dagger h_m=\sqrt{m+1}\,h_{m+1}.
 \tag{6.3}
\]

### Proposition 6.1

The creation operator cannot be bounded on any norm (6.2) which controls
\(L^2\).

#### Proof

If \(\|a^\dagger\|_{w\to w}\le C\), applying it to \(h_m\) gives

\[
 (m+1)w_{m+1}\le C^2w_m.
 \tag{6.4}
\]

Iteration yields

\[
 w_m\le\frac{C^{2m}}{m!}w_0\longrightarrow0,
 \tag{6.5}
\]

contradicting \(w_m\ge c\). \(\square\)

The Gaussian creation-response decomposition contains precisely such
creation operations. Thus a one-space analytic/Fock Banach theorem cannot be
obtained merely by choosing stronger diagonal chaos weights. A scale of
spaces with controlled radius loss, combined with causal step weights, may
still work; that is a substantially different theorem.

## 7. The exact order-three obstruction survives finite Fourier restriction

After taking width to infinity at a fixed schedule, write divided activation
coefficients

\[
 V^{\langle k\rangle}
 =
 \frac1{k!}
 \partial_\varepsilon^kV\big|_{\varepsilon=0}.
 \tag{7.1}
\]

The exact amplitude triangularity theorem shows that order \(k\) solves the
identity-background linear Volterra system with lower-order forcing.

Let

\[
 z_\varepsilon
 =
 z_0+\varepsilon z_1+\varepsilon^2z_2+\cdots.
 \tag{7.2}
\]

At amplitude order three, the top activation contains

\[
 \frac12\varphi''(z_0)z_1^2,
 \tag{7.3}
\]

and \(z_1\) contains

\[
 J^*x^{\langle1\rangle}.
 \tag{7.4}
\]

Since finite Fourier only gives
\(\|\varphi''\|_\infty<\infty\), controlling (7.3) in \(L^2\) still
requires

\[
 \|J^*x^{\langle1\rangle}\|_4<\infty.
 \tag{7.5}
\]

For the uniform coarse/fine theorem, the actual missing estimate is

\[
 \sup_{\substack{t\ge1,\ s\le2t\\ |h|t\le c}}
 \left\|
 t^{-q}\partial_h^q\partial_\lambda^r
 J^*x_s^{\langle1\rangle}
 \right\|_4
 <\infty,
 \qquad
 0\le q\le3,\quad r\in\{0,1\},
 \tag{7.6}
\]

including its one-source-marked aggregate versions.

The connector itself has no ambient substitute for (7.6). If
\(c\in L^2\setminus L^4\) and \(X=Jc\), then \(X\) is Gaussian and has all
finite moments, but

\[
 J^*X=c\notin L^4.
 \tag{7.7}
\]

This operator counterexample is independent of the activation's Fourier
coefficients. It does not prove that the particular generated
\(x^{\langle1\rangle}\) in (7.6) is bad. Rather, it proves that finite
Fourier regularity plus the existing identity \(L^2\) theorem does not imply
(7.6). A new reachable-query theorem is indispensable.

This is the precise sense in which the finite-Fourier restriction still does
not close the exact moving-query aggregate-adjoint inequality.

## 8. Coefficientwise amplitude expansion still needs an all-order majorant

Finite Fourier residuals are analytic, so every formal amplitude coefficient
exists. Let \(N_{t,k}\) denote any intrinsic norm of the complete order-\(k\)
mixed response ledger. A fixed nonlinear radius requires a bound such as

\[
 \sup_{t\ge1}N_{t,k}\le C_0C_1^k
 \qquad(k\ge0),
 \tag{8.1}
\]

after the mesh derivatives have been normalized by their powers of \(t\).
Then

\[
 \sum_{k\ge0}
 |\varepsilon|^kN_{t,k}
 \le
 \frac{C_0}{1-|\varepsilon|C_1}.
 \tag{8.2}
\]

Computing any finite number of coefficients cannot replace (8.1). For every
fixed \(K\), the analytic scalar family

\[
 B_t(\varepsilon)
 =
 t^4+\varepsilon^{K+1}t^6
 \tag{8.3}
\]

agrees with \(t^4\) through amplitude order \(K\) at zero but fails the
dyadic summability test for every fixed \(\varepsilon\ne0\). This is a
logical proof-route witness, not an OMFP realization.

The established triangularity reduces (8.1) to an identity-background
marked resolvent problem. Finite Fourier makes the local forcing explicit
and analytic, but it does not prove the resolvent estimate (7.6).

## 9. Bernstein variants

There are two possible meanings of a Bernstein restriction.

1. A polynomial in the raw coordinate is finite chaos, but global at-most
   linear growth forces it to be affine by Theorem 3.1.
2. A Bernstein polynomial composed with a bounded compactifying map, such
   as \(\tanh x\), is admissible and nonlinear, but it is a nonpolynomial
   function of a Gaussian and therefore has infinite Hermite chaos.

Thus Bernstein approximation is useful for fixed scalar integration or
uniform approximation on a compact set. It does not create an exact finite
Gaussian-response module for the unbounded, adaptively reused OMFP source.
Removing the approximation error uniformly in \(t\) would itself require the
same stability estimate that is currently missing.

## 10. What remains viable

The negative result is limited but sharp.

### Ruled out

1. A genuinely nonlinear finite-chaos activation satisfying the growth
   assumptions.
2. Exact closure by finitely many Fourier, chaos, and source-derivative
   marks.
3. A single diagonal Fock norm which both controls \(L^2\) and makes Gaussian
   creation bounded.
4. Promotion of finitely many correct amplitude coefficients to a fixed
   nonlinear interval.
5. Derivation of (7.6) from finite Fourier envelopes and the existing
   identity \(L^2\) theorem.

### Still viable

An all-order marked analytic scale could assign a radius to the full
source-response graph, allow one controlled radius loss under Gaussian
creation, and recover that loss from chronological step-simplex factors.
For a finite Fourier residual, the local derivative constants are explicit,
so this route has better prospects than for a merely \(C^{12}\) residual.

Its first nonnegotiable test is still (7.6). A proof must use the special
identity-background provenance of \(x^{\langle1\rangle}\), not an ambient
\(J^*\) inequality. If (7.6) is proved, the next task is the all-order
geometric bound (8.1).

## 11. Independent audit

1. **Empty-class claim.** Theorem 3.1 uses only completeness of Hermite
   polynomials, positivity of the Gaussian density, continuity, and growth.
   It does not confuse finite Fourier with finite chaos.
2. **Fourier expansion.** The sign and normalization in (4.2) follow directly
   from the Hermite generating function; its \(L^2\) norm is
   \(e^{-\lambda^2}\sum_m\lambda^{2m}/m!=1\).
3. **Response order.** Proposition 5.1 attacks a finite derivative ledger.
   It does not rule out a symbolic all-order coherent-state representation.
4. **Fock obstruction.** Proposition 6.1 applies only to one diagonal Hilbert
   norm controlling \(L^2\). It does not rule out a scale of spaces.
5. **Aggregate adjoint.** Equation (7.7) is an ambient operator obstruction,
   not a reachable-network counterexample. The generated-query estimate
   (7.6) remains open rather than falsified.
6. **Amplitude coefficients.** Equation (8.3) is a logical counterexample to
   finite-order inference, not an OMFP counterexample.
7. **Limit order.** All network coefficients discussed in Sections 7--8 are
   defined only after fixed-schedule width identification.
8. **Claim level.** No nonlinear \(L=2\) remainder theorem is declared.
   Finite Fourier improves analyticity of the forcing but leaves the exact
   moving-query aggregate-adjoint bridge open.

## 12. Audit of the proposed fixed-amplitude-order Volterra closure

The later version of route_volterra.md introduces Lemma 7.1 and claims that
its schematic equations (7.17)--(7.18) prove the uniform marked \(L^p\)
resolvent at every fixed amplitude order. That proof does not close.

### 12.1 Correct typing of the aggregate identity

Equation (4.3) is written with a comma:

\[
 \mathbb E[\partial_{\chi_i}V],b_i.
 \tag{12.1}
\]

As written, this is not a vector-valued expression. In coordinate-free form,
if \(\mathscr D_J\) is the Malliavin derivative with respect to the
isonormal \(J\)-source, the correct identity is

\[
 J^*V=\mathbb E[\mathscr D_JV].
 \tag{12.2}
\]

For a cylindrical representation

\[
 V=f(\chi_1,\ldots,\chi_m),
 \qquad
 \chi_i=Jb_i,
 \tag{12.3}
\]

this becomes

\[
 J^*V
 =
 \sum_{i=1}^{m}
 \mathbb E[\partial_i f]\,b_i.
 \tag{12.4}
\]

Formula (12.4) remains meaningful at a singular Gram only as the aggregate
Malliavin gradient in (12.2). Individual coordinate partial derivatives
depend on the chosen redundant representation. route_volterra.md states
this invariance but does not define (4.3) through (12.2), and its comma must
be replaced by scalar multiplication.

### 12.2 The one-source ledger is not closed under (12.2)

The more serious problem is derivative order. If \(V\) already carries one
source mark, say

\[
 V^{(1)}=D_\zeta V,
 \tag{12.5}
\]

then applying (12.2) gives

\[
 J^*V^{(1)}
 =
 \mathbb E[\mathscr D_JD_\zeta V],
 \tag{12.6}
\]

which contains a second source derivative. If \(\zeta\) is a moving query,
differentiating its direction adds further terms.

Lemma 7.1 ranges only over “no source mark, one source mark, and aggregate
adjoint sums.” It nevertheless claims the one-source-marked aggregate
versions required by (7.4). Estimating those aggregate adjoints through
(4.3) creates the missing second source mark, which is absent from the
ledger and from the recursion defining \(H_k(p)\).

This is not cosmetic. For a nonlinear Fourier atom,

\[
 D^re^{i\lambda z}
 =
 e^{i\lambda z}
 B_r(i\lambda Dz,\ldots,i\lambda D^rz)
 \tag{12.7}
\]

is nonzero at every source order. Thus the omitted higher-source terms do not
vanish even at fixed activation-amplitude order one.

The only way to avoid expanding (12.6) is to assume a direct \(L^p\) bound
for \(J^*\) on the generated marked core. That is precisely the
aggregate-adjoint theorem Lemma 7.1 is supposed to prove.

### 12.3 The implication (7.17) \(\Rightarrow\) (7.18) is asserted

Even for the unmarked aggregate, (7.17) does not establish the scalar
Volterra inequality (7.18). The proof supplies no displayed estimates for

\[
 \sum_{i,\mu}|e_i|
 |c^{\langle0\rangle}_{s;i,\mu}|,
 \qquad
 \sum_{i,\mu}|e_i|
 |c^{\langle k\rangle}_{s;i,\mu}|,
 \tag{12.8}
\]

nor does it derive the mixed-mark versions of these row sums. The constants
\(\mathcal I\) from the identity Banach theorem control Hilbert-state path
derivatives. They do not, without a new argument, control the
\(\ell^1\)-in-source row sums in (12.8). Counting local Leibniz terms by
\(N\) also does not bound their coefficients or the number of chronological
source paths.

Moreover, (7.18) uses a coefficient \(\Lambda_p\), but no
\(\Lambda_p\) is defined. The claimed Gronwall result then uses
\(\exp(4\Lambda/432)\), with \(\Lambda\) independent of \(p\). A possible
two-stage \(L^2\)-then-\(L^p\) argument is suggested by the definition of
\(H_k(p)\), but it is not derived: the term
\(c^{\langle k\rangle}V^{\langle0\rangle}\) must first be bounded by the
\(L^2\) coupled unknown and the Gaussian \(L^p\) norm, while the other
homogeneous term must have a \(p\)-independent response row sum. Neither
estimate is proved.

Thus (7.17) is a schematic restatement of the coupled aggregate response;
(7.18) is the desired marked resolvent estimate inserted as a conclusion.

### 12.4 Activation-derivative bookkeeping

If one assumes a genuinely closed ledger with three mesh derivatives, one
defect derivative, and one source derivative, then a backward activation
node can use at most

\[
 k+5
 \tag{12.9}
\]

derivatives of \(\varphi\) at amplitude order \(k\). Under that **assumed
one-source closure**, \(C^{12}\) supports \(k\le7\).

But the proof of Lemma 7.1 expands aggregate adjoints of source-marked fields,
which creates at least a second source derivative by (12.6). The maximum
then rises to at least \(k+6\), and recursive adjoint reduction can raise it
further. Therefore the stated \(k\le7\) cutoff is not justified for the
actual marked-adjoint proof. The syntactic assertion that product and chain
differentiation create no mark outside the finite set overlooks the
Malliavin derivative introduced by (4.3).

There are also two minor textual defects: (5.3) contains the literal word
“alpha” in place of \(\alpha\), and Section 6 repeats “The elementary
family.” These do not affect the mathematical verdict.

### 12.5 Verdict on Lemma 7.1

\[
 \boxed{\text{Lemma 7.1 is not proved.}}
 \tag{12.10}
\]

In particular, its claimed consequence (7.4) must remain open. A repair must
do one of two things:

1. construct an all-source-order analytic scale and prove a controlled loss
   under (12.2); or
2. prove a direct, intrinsic \(L^p\) estimate for aggregate adjoints on the
   exact reachable marked core, without recursively invoking another
   Malliavin derivative.

Either repair would be the substantial new OMFP theorem sought by the
near-identity program. The finite-Fourier restriction makes all local
derivatives explicit but does not provide either repair.
