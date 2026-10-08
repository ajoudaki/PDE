# Actual neural finite-history laws without clipping or rank assumptions

2026-10-07. Lead derivation continuing the exact two-sided Gaussian query
route. This proves a fixed finite-program result for actual neural operations,
not just a globally Lipschitz clipped proxy. It does not establish a width
rate, continuous-time limit, finite-memory closure, or all-time error.

The useful observation is that backpropagation's problematic product is a
bounded activation-derivative gate times a backward field. In a comparison,
the large multiplier can be taken from the reference simulator only. Uniform
integrability of that simulator suffices; higher empirical moments of the
actual network need not be assumed.

## 1. Fixed finite neural-program class

There are finitely many neuron populations of size \(n\), finitely many
independent matrices with iid \(N(0,1/n)\) entries between specified
populations, and Gaussian row roots independent of these matrices. Each
population's roots are iid rows of a fixed-dimensional Gaussian vector.
Coordinates within a row may be correlated, including singular covariance.
Program length, root dimensions, and scalar functions are fixed as
\(n\to\infty\).

Allowed operations, in a prescribed order, are:

1. A matrix or transpose query to an initialized Gaussian matrix.
2. A coordinatewise globally Lipschitz scalar function, possibly with nonzero
   intercept and hence at most linear growth.
3. A gated product \(u_i a(v_i)\), with \(a\) bounded and globally Lipschitz.
4. Finite linear combinations of row fields using shared scalar coefficients.
   Coefficients are continuous functions of earlier empirical inner products
   and fixed data, finite on a neighborhood of their limiting arguments.
5. An empirical inner product \(n^{-1}u^\top v\).

The original program does not divide by unprotected empirical history Grams.
Their inverses occur only in the proof's Gaussian conditioning. Matrices may
be reused in either orientation. No operation selects a special neuron.
Every scalar instruction defines finite values on the finite-width inputs
where it is executed. A formula defined only near its limiting argument may
be given any finite measurable extension outside that neighborhood; the proof
uses the extension with probability tending to zero. Actual Euler scalar
operations are globally polynomial and need no such extension.

A fixed finite Euler computation of the canonical network belongs to this
class when implemented by the exact history identities in
FINITE_RESPONSE_MEMORY.md. Forward activations satisfy operation 2.
Backpropagation uses operation 3 with \(a=\phi'\). The stipulated bounded
strip derivative bounds \(\phi'\) and, by Cauchy's formula, \(\phi''\) on
the real line. Predictions, deficits and rank-memory coefficients use
operations 4--5. First-layer initial panel values are Gaussian row roots
with the fixed input Gram as covariance.

## 2. The theorem

Every fixed program in Section 1 has a deterministic scalar history law in
each population, constructed below. For the joint vector of its row fields:

- Empirical averages of every bounded Lipschitz test converge in probability
  to the corresponding expectation under that law.
- All empirical second and cross moments converge in probability.
- Every acquired scalar coefficient and output converges to the value obtained
  from those laws by the prescribed continuous operations.

There is no history-Gram gap assumption, clipping, nonzero-label condition,
or additional fitting condition. The scalar history laws have all moments.
The claim does not assert convergence of higher moments of the original
program.

For fixed finite Euler evolution this identifies actual nonlinear feature
and backward kernels, including passive panel inputs, with a definite aggregate
law. It does not interchange the width limit with increasing step count,
decreasing step size, or infinite time.

## 3. Scalar-law construction

At each initialized matrix keep retained forward queries \(H\) and answers
\(F\), and reverse queries \(D\) and answers \(B\). In the scalar laws,
\(H,B\) live in the input population, and \(F,D\) in the output population.
Histories start empty. Nonmatrix operations are evaluated in the scalar
laws, replacing empirical inner products by expectations.

For a forward query \(u\), put
\[
a=(\mathbb E HH^\top)^{-1}\mathbb E[Hu],
\qquad u_\perp=u-H^\top a.
\]
Empty history omits that term. If \(\mathbb E u_\perp^2=0\), return
\(F^\top a\) without retaining the query. Otherwise return
\[
b=(\mathbb E DD^\top)^{-1}\mathbb E[B u_\perp],
\qquad
g=F^\top a+D^\top b+\sqrt{\mathbb E u_\perp^2}\,Z,
\qquad Z\sim N(0,1),
\tag{1}
\]
where \(Z\) is independent of all earlier output-population fields, and retain
\(u,g\). The reverse rule exchanges the histories and populations. Expectations
always use their stated population; unrelated neuron populations are not paired.

The limiting laws determine a deterministic retain/omit schedule. Each
retained query increases its history's \(L^2\) dimension, so retained Grams
are positive definite, without any quantitative eigenvalue bound. At every
finite stage all scalar coefficients are finite and all fields have all moments:
allowed operations have polynomial growth and fresh innovations are Gaussian.
This recursively defines the law and the retention schedule.

## 4. A simulator revealing only retained queries

Construct all matrices and roots on one probability space. A modified
finite-\(n\) simulator uses the same nonmatrix operations as the original
program but follows the deterministic schedule above. At a retained query it
requests the actual matrix action. At an omitted forward query it returns
\(F_n a\), using retained finite-\(n\) answers and the deterministic limiting
coefficient \(a\). It does not query the omitted input. Reverse queries are
symmetric. Neither the original program's additional queries nor their answers
are revealed in the simulator transcript.

This simulator has joint empirical convergence for every continuous
polynomial-growth test, including all moments. Here is the induction.

The Gaussian root case is the iid law of large numbers. Nonmatrix operations
preserve convergence by composition and polynomial growth. For a converging
scalar coefficient, localize it to a compact neighborhood of its limit, use
uniform continuity on a bounded row cube, and bound the complement with a
higher empirical moment. This justifies coefficient substitution without a
global coefficient cap.

At a retained query, exact adaptive Gaussian conditioning gives the finite
version of (1), except that the fresh Gaussian vector is projected off the
opposite query span. The empirical retained Grams converge to positive definite
limits; their inverses and regression coefficients converge in probability.
The exact formula uses pseudoinverses if a finite Gram is singular; that event
has probability tending to zero.

The projection of a fresh Gaussian \(\xi\) onto a retained opposite stack
\(D_n\) is \(D_n e_n\), with
\[
e_n=(D_n^\top D_n)^{-1}D_n^\top\xi.
\]
Conditionally on the past its coefficient covariance is
\((D_n^\top D_n)^{-1}=O_{\mathbb P}(n^{-1})\), so \(e_n\to0\) in probability.
All empirical moments of \(D_n e_n\) vanish because those of \(D_n\) are
bounded in probability. Empty opposite history omits this projection.

After dropping that term and substituting convergent coefficients, the answer
has form (1) with iid fresh \(Z_i\). For a continuous polynomial-growth test
\(\psi(v,z)\), conditional variance of its average is bounded, after coefficient
localization, by
\[
\frac{C}{n^2}\sum_i(1+\|v_i\|^{2k})=O_{\mathbb P}(n^{-1})
\]
for some fixed \(k\). Its conditional mean is the empirical average of the
continuous polynomial-growth function \(\mathbb E_Z\psi(v,Z)\).
Gaussian moments supply its envelope; dominated convergence on bounded
\(v\)-sets supplies continuity. The induction hypothesis identifies this mean.
Truncation on bounded row sets plus a higher empirical moment controls the
vanishing projection and coefficient substitutions. An omitted query is just
a finite linear combination, for which induction is immediate.

This proves all stated simulator moment limits. Exact conditioning is
applicable because its retained queries are predictable from its own earlier
transcript, roots and deterministic omission coefficients.

## 5. One-sided comparison of an unbounded gated product

Write \(\|u\|_{2,n}^2=n^{-1}\sum_i u_i^2\). Suppose corresponding fields
\(u_n,\widetilde u_n\) and \(v_n,\widetilde v_n\) differ by
\(o_{\mathbb P}(1)\) in this norm. Suppose the reference field has uniformly
integrable empirical squares in probability: for every \(\epsilon>0\),
\[
\lim_{R\to\infty}\limsup_{n\to\infty}
\mathbb P\left\{\frac1n\sum_i|\widetilde u_{n,i}|^2
\mathbf1_{\{|\widetilde u_{n,i}|>R\}}>\epsilon\right\}=0.
\tag{2}
\]
For bounded Lipschitz \(a\),
\[
\|u_n a(v_n)-\widetilde u_n a(\widetilde v_n)\|_{2,n}
\longrightarrow0
\quad\hbox{in probability}.
\tag{3}
\]
Indeed the norm on the left is at most
\[
\begin{aligned}
&\|a\|_\infty\|u_n-\widetilde u_n\|_{2,n}
+R\,\operatorname{Lip}(a)\|v_n-\widetilde v_n\|_{2,n}\\
&\hspace{2em}
+2\|a\|_\infty
\|\widetilde u_n\mathbf1_{\{|\widetilde u_n|>R\}}\|_{2,n}.
\end{aligned}
\tag{4}
\]
First let \(n\to\infty\) at fixed \(R\), then \(R\to\infty\).
The simulator satisfies (2), for example by its fourth empirical moment
convergence and \(u^2\mathbf1_{|u|>R}\le u^4/R^2\).
No higher moment of the original field was used.

## 6. Original/simulator coupling

For the finite set of initialized Gaussian matrices,
\[
\max_G\|G\|_{\rm op}=O_{\mathbb P}(1).
\tag{5}
\]
A direct bound suffices: each sphere has a \(1/4\)-net with at most \(9^n\)
points, by the disjoint-ball volume argument. Approximating a maximizing
bilinear pair gives \(\|G\|_{\rm op}\le2\max_{\rm net}|v^\top Gu|\).
Every fixed bilinear form is \(N(0,1/n)\), hence
\[
\mathbb P\{\|G\|_{\rm op}>8\}
\le2\,9^{2n}e^{-8n}\longrightarrow0.
\]
A finite union proves (5).

Induct through the original and simulator programs on the same matrices and
roots. Initially their fields agree. Assume prior corresponding fields differ
by \(o_{\mathbb P}(1)\) in normalized Euclidean norm. Their norms are bounded
in probability because the simulator's are. Inner products then differ by
\(o_{\mathbb P}(1)\) after subtracting the two factors and applying
Cauchy--Schwarz. Continuous scalar coefficients converge to the same finite
limits. Finite linear combinations, Lipschitz row functions, and the gated
products in Section 5 consequently preserve the comparison.

A retained matrix answer differs by \(G(u_n-\widetilde u_n)\), or its
transpose version, whose norm vanishes by (5). At an omitted forward call,
\[
Gu_n-F_n a
=G(u_n-\widetilde u_n)+G(\widetilde u_n-H_n a).
\tag{6}
\]
The first term vanishes as before. The simulator's joint second-moment
convergence shows that the squared norm of the second input tends to
\(\mathbb E(u-H^\top a)^2=0\), exactly the omission criterion.
Its image therefore vanishes by (5). Reverse calls are identical.

This proves normalized Euclidean agreement for all fields of the fixed
program. Bounded Lipschitz empirical tests transfer by Cauchy--Schwarz,
and second/cross moments transfer by the two-factor estimate. The simulator
limits therefore prove every assertion in Section 2.

## 7. What this resolves, and what it does not

Zero-readout rank singularities and unbounded activation values do not
prevent a qualitative fixed-history aggregate law for the actual canonical
network. The law includes the cross-direction Gaussian response term (1);
discarding it still gives the wrong model.

However, retained limiting gaps can deteriorate with program length. The
proof gives no estimate uniform in that length, and the two-limit argument
(4) gives no width rate. Neither \(n^{-1/2}\) accuracy nor logarithmic memory
follows from this qualitative theorem. Quantitative weak stability and
continuous/all-time closure remain separate, unresolved obligations.

The complete proof and actual-Euler membership passed the scoped internal
check in UNCLIPPED_HISTORY_AUDIT.md. This version incorporates its
finite-program well-definedness convention. Its recorded source hash refers
to the preceding version; no quantitative conclusion is added by that check.
