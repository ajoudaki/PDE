# Adversarial audit

## A. Exact coefficient versus interval coefficient

The instability theorem never claims super-`t^5` growth for the literal
coefficient `[h^5] Delta_t`.  The universal Euler chronology cancels its
degree-five temporal part, so that coefficient has degree at most four.
The scalar theorem evaluates `h=rho/t` after a number of steps growing with
`t`; it is an all-orders, nonlocal effect.

## B. Tail probability versus tail amplitude

The lower event has probability `exp(-O(t^2))`.  This is included in
(2.13).  Its amplitude has logarithm `Theta(4^t)`, so the probability loss
does not invalidate the expectation lower bound.

## C. Signed expectation

The proof does not replace `|E X|` by `E|X|`.  Positivity of the activation
makes `a_r` monotone.  All states with `a_N>=0` contribute nonnegatively;
the entire negative part is bounded explicitly by (2.11).  This is why a
positive linearly growing base was used instead of `x+lambda sin(x^p)`.

## D. Coarse/fine cancellation

The schedules are not bounded separately by the same crude envelope.  The
fine schedule has the lower bound `exp(c4^t-O(t^2))`; the coarse schedule
has the upper bound `exp(Ct3^t)`.  Their growth scales are strictly
separated because `4/3>1`.

## E. Regularity

The triangular phase is continuous and differentiable almost everywhere,
not `C^1`.  This is enough for the scalar recursion with Gaussian initial
data, but it does not meet a bounded-derivative or `C^12` activation class.
It does meet the literal at-most-linear growth hypothesis.  A smooth
periodic replacement must cross derivative zero; proving that iterates do
not concentrate in those transition phases requires a new
anti-concentration lemma.  No such lemma is silently assumed here.

## F. Full two-hidden-layer quantifier

The theorem is deliberately labelled scalar.  Equation (3.1) exhibits the
exact reused-matrix term that blocks transfer to `L=2`.  Treating it as
fresh independent Gaussian noise would be invalid.  Therefore this study
does not refute the finite-output `L=2` OMFP claim.

## G. Natural polynomial-phase sine candidates

For

\[
 \phi(x)=\{x+\lambda\sin(x^p)\}/
 \|G+\lambda\sin(G^p)\|_2,
\]

one has `|phi'|<=C(1+|x|^(p-1))`, so every fixed finite scalar
and OMFP source DAG has finite polynomial moments.  The preregistered
Monte Carlo scan shows severe non-uniform integrability for `p=5`: the
sample mean is controlled by one or two observations while the 99.9%
trimmed mean stays small.  This is consistent with the rare-tail mechanism
but cannot determine the expectation.  Unlike the triangular phase,
`cos(x^p)` has zeros, so (2.6) fails.  A proof would require a quantitative
anti-concentration result simultaneously along all adaptive phases.  No
such result is presently established.

## Verdict

The unrestricted phrase “linearly bounded growth” is too weak to imply
uniform Euler stability: a rigorous scalar counterexample exists and an
even simpler smooth activation can make the first or second mean-field Gram
infinite.  For the actual finite-output `q=1,L=2` OMFP network, however,
the super-`t^5` counterexample remains open because of the signed aggregate
reused response in (3.1).  Presenting the scalar theorem as the requested
network theorem would fail the audit.

