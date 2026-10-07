# Scoped check of moment-preserving population substitutions

2026-10-06. Independent reconstruction of Sections 1--5 of
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md`. The information interface already
proved in `EFFICIENT_QUERY_INFORMATION.md` is taken as given, as directed;
this is not a fresh review of that information note.

The checked mathematical claims are correct. The centered
sub-Gaussian formula in candidate equation (22) is
\(\log\int\exp\{\lambda[R-\int R\,d\mu]\}\,d\mu
\le\lambda^2\sigma_R^2/2\). The first version read had a typesetting
error in that formula; the author corrected it, and the complete corrected
note was reread. The final checked hash is recorded below.

The conclusions here concern posterior noise control, the finite entropy
dual, uniqueness of the minimizing row law, multiplier rounding, and the
fixed-test control-variate estimate. They do not validate the physical
forcing lemma in Section 6 or an efficient neural decoder.

## 1. Inputs and fixed interface

The complete synthesis note was read, including the sections outside the
verdict's scope. No linked source, other new route output, external source,
experiment, or Git operation was used. The previously read research and
proof instructions and the supervisor's explicit canonical-notation
fallback were applied. Only this assigned report was written.

The inherited interface consists of iid row packets of law \(\mu\),
independent standard Gaussian scalar noises, bounded chronological row
tests, and

\[
 C_r=\frac1n\sum_iF_r(Z_i;C_{<r})+\eta E_r,
 \qquad |F_r|\le B,
 \qquad H=\frac P2\log(1+B^2/\eta^2).
\]

On its stated common event, every prefix posterior \(\pi_c\) satisfies
\(D(\pi_c\Vert\mu^{\otimes n})\le H/\alpha\), and its common
row marginal has entropy at most \(h=H/(\alpha n)\). The conditional
empirical-average inequality from that interface is also assumed. These
are the only prior mathematical conclusions needed for the present
Sections 1--5 reconstruction.

## 2. Posterior noise and strict feasible slack

Let \(S_E=\sum_{r=1}^PE_r^2\). Since
\(\mathbb E S_E=P\), the finite process

\[
 M_j=\mathbb E[S_E\mid C_{\le j}]
\]

is a nonnegative martingale of mean \(P\). On each event where its
first crossing of \(P/\beta\) occurs at index \(j\), the
conditional expectation of its terminal value equals \(M_j\).
Summing these disjoint events bounds the crossing probability by
\(\beta\). This proves the simultaneous posterior bound in
candidate equation (4); independence of the noises after conditioning
is not used or asserted.

At prefix length \(j\), every earlier scalar \(C_r\) is known. Taking
conditional expectations of its defining update gives

\[
 \int F_r(z;c_{<r})\,\pi_c^1(dz)-c_r
                                 =-\eta\mathbb E[E_r\mid c].
\]

Exchangeability identifies the conditional empirical average with the
one-row expectation. Conditional Cauchy--Schwarz then gives
\(|\mathbb E[E_r\mid c]|\le\sqrt{\mathbb E[S_E\mid c]}
\le T\), where \(T=\sqrt{P/\beta}\). Intersecting with the
information event costs at most \(\alpha+\beta\) total failure.

Thus \(\pi_c^1\), of entropy at most \(h\), lies within
\(\eta T\) of the center of each retained moment constraint. The
optimization box has radius \(2\eta T\), so its slack is at least
\(\eta T>0\) in each coordinate. This is a verified feasible slack;
linear dependence between the moment functions does not invalidate it.
For an empty prefix the optimization is simply minimized by \(\mu\).

## 3. Finite dual attainment and a unique minimizing density

For fixed prefix \(c\), abbreviate the retained test vector by
\(F(z)\), and define the finite functions

\[
 \psi(\lambda)=\log\int e^{\lambda^TF}\,d\mu,
 \qquad J(\lambda)=\lambda^Tc-2\eta T\|\lambda\|_1-\psi(\lambda).
\]

The bound \(|F_r|\le B\) permits differentiation under the integral
at every finite \(\lambda\); on a compact multiplier set a constant
times \(e^{B\|\lambda\|_1}\) dominates the relevant integrands.
Consequently \(\nabla\psi\) is the moment vector of the exponential
tilt \(\nu_\lambda\).

Applying the entropy inequality to the feasible posterior marginal gives

\[
 \psi(\lambda)
 \ge\lambda^T\int F\,d\pi_c^1-D(\pi_c^1\Vert\mu),
 \qquad
 J(\lambda)\le h-\eta T\|\lambda\|_1.                     \tag{1}
\]

This proves coercivity directly: \(J\) is continuous and tends to
minus infinity as \(\|\lambda\|_1\) tends to infinity. It therefore
attains a finite maximum. Since \(J(0)=0\), every maximizer obeys

\[
 \|\lambda_*\|_1\le h/(\eta T).                            \tag{2}
\]

No separation theorem requiring full-dimensional moment support, and no
covariance inverse, is needed for this step.

At a nonzero coordinate of \(\lambda_*\), its ordinary coordinate
derivative must vanish. At a zero coordinate, the two one-sided
derivatives have the required opposite signs. Together these conditions
give a vector \(s\) such that

\[
 |s_r|\le1,\qquad s_r=\operatorname{sign}(\lambda_{*,r})
       \text{ if }\lambda_{*,r}\ne0,
 \qquad \int F\,d\nu_{\lambda_*}=c-2\eta T s.               \tag{3}
\]

Hence the tilted law is feasible. Its relative entropy is finite and
equals

\[
 D(\nu_{\lambda_*}\Vert\mu)
 =\lambda_*^T\int F\,d\nu_{\lambda_*}-\psi(\lambda_*)
 =J(\lambda_*),                                             \tag{4}
\]

because \(\lambda_*^Ts=\|\lambda_*\|_1\). For any other feasible
law, the entropy inequality and the moment box give

\[
 D(\nu\Vert\mu)
 \ge\lambda_*^T\int F\,d\nu-\psi(\lambda_*)
 \ge J(\lambda_*).
\]

This proves primal attainment and dual equality constructively. Comparing
with \(\pi_c^1\) bounds the minimum by \(h\). All minimizers have
finite entropy and thus densities relative to \(\mu\). If two such
densities differed on a set of positive \(\mu\)-measure, strict
convexity of \(u\log u\) would give their feasible midpoint strictly
smaller entropy. The minimizing density is therefore unique. This does
not imply uniqueness or good conditioning of the multiplier vector.

## 4. Rounding and finite description length

Let \(\Delta=\|\widetilde\lambda-\lambda_*\|_1\). Pointwise,
the change in the unnormalized exponent is at most \(B\Delta\).
Integrating its exponential upper and lower bounds gives

\[
 |\psi(\widetilde\lambda)-\psi(\lambda_*)|\le B\Delta,
 \qquad
 \left|\log\frac{d\nu_{\widetilde\lambda}}{d\nu_*}\right|
                                                   \le2B\Delta.
\]

The likelihood-ratio bound implies the candidate's conservative estimate
\(\|\nu_{\widetilde\lambda}-\nu_*\|_{\rm TV}
\le e^{2B\Delta}-1\). For \(|G|\le B_G\), the expectation
error is at most \(2B_G(e^{2B\Delta}-1)\).

If \(0<\varepsilon\le1\) and
\(\Delta\le\varepsilon/[8B\max\{1,B_G\}]\), then
\(x=2B\Delta\le1/4\). Since \(e^x-1\le2x\) on this
interval, that expectation error is at most
\(8BB_G\Delta\le\varepsilon\). The displayed numerical
constant is therefore sufficient.

Taking \(B_G=B\) and \(\varepsilon=\eta T\le1\) proves
the claimed extra \(\eta T\) tolerance for each retained moment.
The exact tilt was in the radius-\(2\eta T\) box, so the rounded
one lies in the radius-\(3\eta T\) box. Rounding each multiplier
coordinate to error \(\Delta/j\) gives the desired total
\(\ell^1\) error for \(j\ge1\).

For completeness, a signed scalar with magnitude bounded by
\(h/(\eta T)\) and grid spacing comparable to \(\Delta/j\)
requires

\[
 O\!\left(1+\log(1+h/(\eta T))
                    +\log(1+j)+\log_+(1/\Delta)\right)
\]

bits. Substituting the smaller of the two permitted rounding tolerances
gives candidate equation (17), up to an absolute constant multiplying
the entire bound. The two powers of \(B\) in the retained-moment
tolerance are covered by that constant. The absolute-polylogarithmic
conclusion requires the stated logarithmic bounds on \(B\), \(B_G\),
\(1/\eta\), and the requested accuracy, with fixed confidence
parameters; it is not a bound for arbitrary tests with uncounted ranges.

This argument rounds multipliers for a fixed ideal prefix and row circuit.
It proves neither stability when that prefix itself is rounded nor an
algorithm for finding a multiplier or evaluating its normalization.
The candidate explicitly leaves those issues unresolved.

## 5. Reusing moments and estimating only the residual

For a fixed prefix and query, the coefficients \(a\) and row function
\(G\) must be determined without additional access to the hidden row
array. They may depend on the prefix; no unconditional statistical
independence from that prefix's data is required. Put

\[
 R=G-a^TF,
 \qquad d_G=a^Tc+\int R\,d\mu.
\]

If the oscillation of \(R\) is at most \(2B_R\), subtracting its
range midpoint gives a function bounded in absolute value by \(B_R\)
and leaves its empirical-minus-prior discrepancy unchanged. The inherited
entropy estimate therefore supplies candidate equation (19).

The exact update identities yield, on the posterior of rows and noises,

\[
 \frac1n\sum_iG(Z_i)-d_G
 =\frac1n\sum_iR(Z_i)-\int R\,d\mu-\eta a^TE_{\le j}.      \tag{5}
\]

For the last term,

\[
 \mathbb E[|a^TE_{\le j}|\mid c]
 \le\|a\|_2\sqrt{\mathbb E[\|E_{\le j}\|_2^2\mid c]}
 \le T\|a\|_2.
\]

This proves the stated conditional estimate

\[
 \mathbb E\left[\left|\frac1n\sum_iG(Z_i)-d_G\right|\middle|c\right]
 \le B_R\sqrt{\frac{2(H/\alpha+\log2)}n}+\eta T\|a\|_2.     \tag{6}
\]

In particular, there is no missing \(\sqrt j\) factor: the posterior
bound already controls the squared norm of the entire noise vector.
Large reuse coefficients enter the original-noise term, not the sampling
range term. The common information and noise event makes (6) valid for
every fixed query test and coefficient choice at every prefix without a
union over queries.

The sub-Gaussian variant is also correct. Its assumption is explicitly
on all real exponential moments of \(R-\int R\,d\mu\), rather
than its variance alone. Under the independent prior, the average of
\(n\) copies has variance proxy \(\sigma_R^2/n\). Bounding the
exponential of its absolute discrepancy by the sum of the positive and
negative exponentials adds \(\log2\) to the entropy estimate.
Optimizing its positive exponent parameter gives (6) with \(B_R\)
replaced by \(\sigma_R\). If the residual is unbounded, truncating
the absolute discrepancy before the entropy inequality and passing
monotonically to the limit justifies the finite posterior expectation.

Fresh independent passive-query row coordinates preserve the inherited
entropy bound after the prescribed augmentation. A fresh scalar Gaussian
noise contributes at most \(\eta\), since its absolute first moment
is at most one. These additions have exactly the costs stated in the
candidate.

## 6. Counterexample repair and the adaptive-query boundary

For the redundant mean, choosing \(G=F\) and \(a=1\) gives
\(R=0\), \(d_G=C\), and a decoded value
\(\tanh((d_G-C)/\sigma)=0\). The exact noisy output satisfies

\[
 \mathbb E[|U|\mid C]
 \le\frac\eta\sigma\bigl(\mathbb E[|E|\mid C]
                                      +\mathbb E|E'|\bigr)
 \le\sigma(T+1)
\]

when \(\eta=\sigma^2\). This reconstructs candidate equation
(23) and proves the claimed repair of that specific example.

For a scalar Lipschitz output map, multiplying (6) and the optional fresh
noise cost by its Lipschitz constant is valid. Markov's inequality gives
a conditional interval with any prescribed failure probability \(p\)
by increasing its radius by \(1/p\). To intersect this with a posterior
center interval of mass \(5/8\), choose \(p<5/8\), for example
\(p=1/8\). This is the probability margin imported from the previous
center transfer. The sufficient scale condition (24) is correct with
fixed confidence factors and bounds uniform over the desired prefixes
and query/time pairs.

The note correctly excludes a further step that would otherwise be
invalid: in a multistep query, a later row function depending on previous
random query summaries is not a fixed function of the training prefix.
Equation (6) cannot be applied to it merely by plugging in the random
summaries. A new information, uniformity, or propagation argument is
needed. Nothing in dual attainment or multiplier rounding proves that
argument, or efficient deterministic evaluation of the residual
integrals.

## 7. Verdict boundary and checked version

The five assigned groups of claims reconstruct under the inherited
information interface. The only correction identified in the initial
version is the already reported typesetting of the centered integral in
(22), not a change to its mathematical assumption or conclusion.

The tilt is a uniquely defined feasible density with a finite multiplier
description; it is not a proved efficient computation. The control-variate
bound applies to fixed tests and explicitly charges reuse noise; it is
not a bound for the full adaptive neural query program. No conclusion on
the physical-forcing lemma or the full neural decoder is given here.

Checked final candidate SHA-256:
`e7440281bdb14a8d87efc89e2c429e6ca24bc8c99f92587a1559246b4f3f8838`.
