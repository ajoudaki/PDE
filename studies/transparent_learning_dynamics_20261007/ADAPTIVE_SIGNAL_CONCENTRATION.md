# Uniform empirical control of adaptive Gaussian signal programs

2026-10-07. Lead derivation in the transparent-dynamics study. This is a
concentration bridge for the proposed causal Gaussian/response route, not an
all-time neural comparison theorem. Scientific inputs are elementary Gaussian
conditioning and the model already fixed in this study. No literature or other
study is used in this note.

The useful point is precise: adaptively chosen coefficients need not destroy
an empirical Gaussian law of large numbers. A uniform bound over the entire
finite coefficient class applies to the selected coefficients, however they
were computed. The separate issue of **stability when empirical moments are
replaced by population moments remains open**. In particular this result does
not license Gaussian independence of adapted matrix actions.

## 1. A finite-class bound with all parameters visible

Let \(g_1,\ldots,g_n\) be independent standard Gaussian vectors in
\(\mathbb R^r\), where \(r\ge1\). A coefficient vector \(\theta\) ranges
over \([-B,B]^s\), with \(B\ge1\). Consider \(J\) measurable scalar observables
\(F^j_\theta(g)\), each bounded in absolute value by \(M\ge1\), for
every coefficient and every Gaussian argument. For a prescribed truncation
radius \(R\), suppose

\[
\sup_{g\in[-R,R]^r}
|F^j_\theta(g)-F^j_{\theta'}(g)|
\le L\|\theta-\theta'\|_\infty,
\qquad L\ge1,
\tag{1}
\]

for every \(j\). These are explicit boundedness and coefficient-regularity
hypotheses, not consequences claimed here for unmodified neural trajectories.

For \(0<\delta<1\), choose

\[
R=\sqrt{2\log(4nr/\delta)}.
\]

Then with probability at least \(1-\delta\), simultaneously for every
\(j\) and every \(\theta\),

\[
\left|\frac1n\sum_{i=1}^nF^j_\theta(g_i)
-\mathbb E F^j_\theta(g)\right|
\le
M\sqrt{\frac2n
\left[s\log(1+2BnL)+\log(4J/\delta)\right]}
+\frac{2+M\delta}{n}.
\tag{2}
\]

The value \(L\) in (2) must be a bound valid on the displayed cube at
this chosen \(R\). It may depend on \(R\).

### Proof

Clip each Gaussian coordinate to \([-R,R]\), writing \(g^R\) for the
result. A union bound and the elementary normal tail inequality give

\[
\mathbb P\{g_i\ne g_i^R\text{ for some }i\}
\le2nr e^{-R^2/2}=\delta/2.
\tag{3}
\]

The same coupling for one Gaussian vector gives, uniformly in coefficients,

\[
|\mathbb EF^j_\theta(g)-\mathbb EF^j_\theta(g^R)|
\le 2M\mathbb P\{g\ne g^R\}
\le4Mr e^{-R^2/2}=M\delta/n.
\tag{4}
\]

Take an infinity-norm net of the coefficient cube with radius
\(1/(nL)\). It can be chosen with at most
\((1+2BnL)^s\) points: subdivide each interval into pieces of length at
most \(2/(nL)\) and use their centers. For each net point and each
observable, the centered sample mean on clipped Gaussians obeys

\[
\mathbb P\left\{
\left|\frac1n\sum_iF^j_\theta(g_i^R)
-\mathbb EF^j_\theta(g^R)\right|>t\right\}
\le2\exp\left(-\frac{nt^2}{2M^2}\right).
\tag{5}
\]

For completeness, (5) follows by the exponential-moment argument for a
bounded variable of interval length \(2M\). If \(X\) lies in an interval
of length \(2M\), the logarithmic moment-generating function of
\(X-\mathbb EX\) has zero value and slope at zero, and its second
derivative is the variance under an exponential tilt. Every tilted variable
still lies in that same interval, whose variance is at most \(M^2\), since
\(\operatorname{Var}(X)\le\mathbb E(X-\text{midpoint})^2\le M^2\).
Integrating twice yields
\(\mathbb E e^{t(X-\mathbb EX)}\le e^{t^2M^2/2}\).
Multiply these bounds for independent samples, optimize the exponential
Markov inequality, and apply it to both signs.

Taking the union bound in (5) over the net and the \(J\) observables
proves the square-root term in (2) except with failure \(\delta/2\).
Moving from a coefficient to its net point changes the sample mean and
the expectation by at most \(1/n\) each, by (1). Add these two errors
and (4), and intersect with (3). This proves (2). \(\square\)

## 2. Why coefficient adaptivity is allowed

On the event of (2), substitute any coefficient selection
\(\theta=\widehat\theta(g_1,\ldots,g_n,\text{other random data})\)
whose value belongs to the coefficient cube. No independence between that
selection and the sample is needed: the event already holds for every
coefficient value. Arbitrarily correlated selections for different
observables are also covered.

This is a same-coefficient comparison. It bounds

\[
\frac1n\sum_iF_{\widehat\theta}^j(g_i)
-\mathbb EF_{\widehat\theta}^j(g),
\]

where the expectation treats the realized \(\widehat\theta\) as a fixed
argument. It does not identify this population value with the output of a
separately evolved population model, whose coefficient trajectory would
generally be different. Proving that second comparison requires stability.

## 3. Scalar signal circuits have logarithmic entropy cost

Here is a sufficient concrete class for (1). Consider a fixed acyclic
program with at most \(p\ge1\) scalar operations, acting on the Gaussian
inputs and on coefficients in \([-B,B]^s\). Every internal node is clipped
to \([-A,A]\), where \(A\ge\max(1,M,R)\). An operation is either:

- An affine combination of at most \(p\) previous nodes, with coefficients
  of absolute value at most \(B\), followed by a scalar function whose
  Lipschitz constant is at most \(a\ge1\), then clipping.
- A product of two previous nodes, followed by clipping.

The final observable is also clipped to \([-M,M]\). Coefficients may be
reused; constant coefficients need not be counted in \(s\). Several outputs
of the same program can serve as the \(J\) observables. Assume the complete
grammar and clipping levels are fixed before seeing the Gaussian sample.
Every variable affine weight and bias is a coordinate of \(\theta\);
the scalar gate functions are fixed. A nonlinear parameterization of a
weight must instead be counted as additional controlled gates. Coefficients
enter as edge weights or biases, not as unclipped ordinary input nodes.

Set, only for this bound,

\[
C_0=4(p+1)(B+1)(A+1)(a+1).
\]

The program has coefficient Lipschitz bound

\[
L\le C_0^{p+1}.
\tag{6}
\]

To prove this, put \(h=\|\theta-\theta'\|_\infty\). Gaussian-input
nodes agree in the comparison. If all previous node differences are at most
\(C_0^k h\), the affine-input difference is at most
\(pB C_0^k h+(pA+1)h\). Applying the scalar Lipschitz constant and clipping
makes it at most \(C_0^{k+1}h\). A product difference is at most
\(2A C_0^k h\), also bounded by \(C_0^{k+1}h\). Clipping is
1-Lipschitz. Induction proves (6), with one spare factor for the final output.

Substitution in (2) uses

\[
\log(1+2BnL)
\le\log(1+2Bn)+(p+1)\log C_0.
\tag{7}
\]

Thus even a large coefficient sensitivity costs its **logarithm** in the
uniform empirical bound. For \(s\le(p+1)^2\), the leading complexity
inside the square root is polynomial in the program length, rather than
exponential in that length. A polylogarithmic program, polylogarithmic output
bound and coefficient/internal-node bounds whose logarithms are
polylogarithmic in \(n\) give an explicit
\(n^{-1/2}\operatorname{polylog}n\) same-coefficient empirical error.
Here \(\log a\), \(\log J\), and \(\log(1/\delta)\) must also be
polylogarithmic, or fixed in the stated limit.
The logarithmic powers still depend on those stated program bounds; no
dimension-independent exponent is asserted.

The real analytic activation class is compatible with this grammar because
\(\phi\) is Lipschitz on the real line, and its strip derivative bound
also bounds the higher derivative needed for a \(\phi'\) gate on any
strictly narrower strip. This observation supplies a possible value of
\(a\); it does not prove that clipping leaves a particular neural program
unchanged. That is a separate localization requirement.

## 4. Application boundary for Gaussian matrix queries

For a coordinatewise signal program implementing the correct sequential
simulation of Gaussian matrix actions, a new response can
be generated from a fresh independent Gaussian vector, earlier response
vectors, and coefficients determined by earlier empirical pairings. At the
level of a single neuron population, after finitely many queries every
response coordinate is therefore a function of that coordinate's independent
Gaussian innovations and globally shared adaptive coefficients. The bound
above can control the resulting empirical pairings uniformly over those
coefficients if the exact query program has been placed in the bounded
grammar.

There are three distinct obligations before this can imply a transparent
population dynamics theorem:

1. **Correct conditioning.** Forward and transpose queries share the same
   initialized matrix. The causal regression/self-interaction term must be
   retained; replacing every new action by independent Gaussian noise is wrong.
2. **Localization and rank handling.** A valid neural construction must give
   coefficient/node bounds or a controlled truncation. Nearly dependent query
   histories can make naive Gram inverses large. Finite coefficient sensitivity
   alone is harmless for (2), but is not harmless for dynamical propagation.
   Truncation needs population-tail control as well as equality on the sampled
   coordinates: agreement at all \(n\) samples with high probability does not
   imply a small change of Gaussian expectation. The independent audit gives
   a short repeated-squaring circuit demonstrating that distinction.
3. **Weak-observable stability.** Replacing every empirical moment by a
   population moment changes later coefficients and feature laws. One needs a
   comparison at prediction/response level, preferably with residual-weighted
   stability and no exploding physical-horizon Gronwall factor.

The third obligation is not solved by uniform concentration. For example,
an arbitrarily ill-conditioned inverse Gram can amplify an entrywise-small
moment defect. A positive-part covariance square root can also give a
strong coupling error of the square root of that defect, even when smooth
weak observables have a better rate. A claim at dense variability must prove
the required weak stability, not silently infer it from (2).

## 5. Research-state consequence

This lemma removes one specific objection to an aggregate causal Gaussian
route: adaptation of the moment coefficients alone need not preclude the
correct empirical fluctuation scale for a polylogarithmic transcript. It
does not remove the need for a correct law, finite-state closure, all-time
stability, or an error budget that controls the desired observables.

The current exact polar theorem remains unchanged. This is a new bridge toward
a genuinely aggregate alternative, not a supersession of that theorem or a
claim that the full research goal has been achieved.

An independent internal check is recorded in ADAPTIVE_SIGNAL_AUDIT.md.
Its core concentration and adaptivity checks passed. The present version
incorporates its coefficient-grammar, confidence-rate and population-tail
qualifications; the audit's recorded hash identifies the preceding version.
