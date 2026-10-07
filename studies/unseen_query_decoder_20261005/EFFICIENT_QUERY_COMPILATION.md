# Offline compilation of unseen-input responses

2026-10-06. Independent scoped theory route. No experiment, maintained-source
change, or Git mutation. The result below is a conditional compilation theorem
and two precise obstructions to generic compilation arguments. It does **not**
establish efficient decoding for the original nonlinear model.

The decisive missing fact is a small-circuit approximation theorem for the
current-state response as a function of an unseen input. Unlimited preprocessing
can find and certify such circuits if they exist with the stated bounds. The
existing storage/workspace theorem, analyticity alone, and the low-rank training
source do not establish their existence.

## 1. Scope, sources, and target

The complete scientific inputs read for this route were:

* `CURRENT_STATE_DECODER_CANDIDATE.md`;
* `FOURIER_ROW_PROGRAM_EVALUATION.md`;
* `SHORT_CAUSAL_TRAINING_PROGRAM.md`;
* `PREPROCESSING_AND_QUERY_COST.md`.

No other route output, review, study history, or older finite-panel source was
read. The inherited dense certificates are accepted only as stated in those
inputs; this route does not independently audit them. The required rigorous-math
and conjecture-investigation skills, including the research-contract and
adversarial-audit references, were read. Reading
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
`Permission denied`; the assignment's explicit fallback and the mathematical
communication requirements in `AGENTS.md` were applied.

Use the original depth-\(L\), width-\(n\) nonlinear network, the original
strip-analytic activations, Gaussian initialization, zero readout, mean-square
loss, mobilities \((n,1,\ldots,1,n)\), spanning training inputs
\(x_a\in\mathbb R^d\), full original labels, and supplied small-label and
feature-Gram conditions. Let \(f_n(t,x)\) be its dense predictor, and let
\(b_n(\delta)\) be the inherited whole-sphere, whole-trajectory dense
comparison certificate. The desired efficient theorem retains the guarantee

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\mathrm{compact}}(t,x)-f_n(t,x)|
 \leq 2b_n(\delta/32)+1/n
\]

with the current theorem's probability qualifications. It must additionally
evaluate a new input in a fixed-degree polynomial in the retained description
length and requested logarithmic precision. Retained storage and peak query
workspace must remain \(C[\log(en)]^k\), with \(k\) independent of
\(d,m,L\). Fixed-problem constants and sufficient width may depend on those
parameters. Dense preprocessing may be expensive. The endpoint remains an
explicit terminal flag. The zero-label case is already solved by the zero
predictor and is not the issue here.

The primitive-time formulation counts calls to the original activation
primitives. A bit-time conclusion additionally needs polynomial-*time*
precision interfaces for those primitives and fixed data. The existing
polynomial-*space* interface does not imply that stronger condition.

## 2. A constructive sufficient condition for fast posterior decoding

Fix a completed training prefix of length \(j\), its retained rounded value
\(c\), and one physical-time patch. Write \(s\in[0,1]\) for its normalized
time coordinate. Let \(U_c(x,s)\) denote the passive-query scalar output under
the fixed-prefix posterior law of Section 8 of the Fourier evaluator. The
posterior law is held fixed when \(x,s\) vary. For transition width
\(\sigma>0\), define the increasing threshold ramp

\[
 r_{a,\sigma}(u)=
 \begin{cases}
 0,&u\leq a-\sigma,\\
 (u-a+\sigma)/(2\sigma),&a-\sigma<u<a+\sigma,\\
 1,&u\geq a+\sigma,
 \end{cases}
 \qquad
 H_c(x,s,a)=\mathbb E[r_{a,\sigma}(U_c(x,s))\mid C=c].
\]

Choose the same \(\sigma\leq1/(4n)\) and bounded threshold range as the
current decoder. The Fourier theorem gives a numerical evaluator of \(H_c\)
to any prescribed accuracy on a certified positive-density state. Its work
can be enormous; its storage is bounded by a fixed-degree polynomial in its
description and logarithmic numerical parameters.

Let \(\mathcal P\) be the sum of those description lengths, summary counts,
row dimensions, \(\log(en)\), and required logarithmic bounds and precision.
In the current construction \(\mathcal P\leq C[\log(en)]^{k_0}\) for an
absolute \(k_0\). This notation counts descriptions and numerical certificates;
it does not make an integration oracle a unit-cost instruction.

**Conditional compilation proposition.** Suppose the following property holds
uniformly for each prefix, its valid retained state, and its time patch. For a
fixed numerical error budget \(\tau>0\), there exists a circuit \(A_c\) such
that:

1. It uses only the original activation primitives and an explicitly specified
   finite collection of scalar arithmetic and continuous elementary operations.
   Its complete description has at most \(S\) gates and constants of at most
   \(b\) bits each. Its numerical evaluation to the required precision takes
   polynomially many primitive operations and polynomial workspace.
2. Its input is \((x,s,a)\), and
   \(\sup|A_c(x,s,a)-H_c(x,s,a)|\leq\tau/4\) over the entire sphere,
   patch, and threshold interval. All its coefficients are determined from
   the current retained state and permitted fixed data.
3. A certified Lipschitz bound \(L_A\) for every admitted circuit, and a
   bound \(L_H\) for \(H_c\), are available. The quantities
   \(S,b,\log(2+L_A+L_H)\) are bounded by fixed-degree polynomials in
   \(\mathcal P\); the degrees do not depend on \(d,m,L\).

Then a finite deterministic current-state compiler can find a circuit with
uniform error at most \(\tau\), using absolute-polylogarithmic workspace.
The compiler's runtime is unrestricted. Retaining that circuit gives
polynomial-primitive-time median decoding, with absolute-polylogarithmic
retained storage and peak query workspace. Allocating \(\tau\) within the
existing conditional-test error budget preserves the original sphere/time
guarantee, including the fitted endpoint.

**Proof.** The finite gate alphabet, length bound, bounded-bit constants, and
explicit numerical interfaces define a finite enumerable candidate class.
Bounds on valid gates, for example a lower gap for any division, are part of
the class. Enumerate the descriptions sequentially, retaining one candidate.
For each candidate enumerate a finite net of the compact query domain with
mesh at most

\[
 h=\frac{\tau}{4(1+L_A+L_H)}.
\]

A sphere net can be generated without storing it: enumerate a dyadic grid in
the unit cube, discard points with Euclidean norm below \(1/2\), and normalize
the others. If a unit vector is within Euclidean distance \(e\leq1/2\) of
a grid point \(g\), then
\(\|g/\|g\|-v\|\leq2e\). Scaling by \(\sqrt d\), and taking product
grids for time and threshold, gives the required finite net. A mixed-radix
counter and the current point use space polynomial in dimension and
\(\log h^{-1}\), regardless of the number of points.

At each point evaluate the candidate and \(H_c\) with absolute errors at
most \(\tau/16\) each. Use the existing fixed-prefix numerical evaluator
for the latter. Accept a candidate only if every estimated difference is at
most \(\tau/2\). A witness from item 2 is accepted: its estimated difference
is at most \(\tau/4+2\tau/16=3\tau/8\). An accepted candidate has true
net-point error at most \(\tau/2+2\tau/16=5\tau/8\). Lipschitz extension
from the net adds at most \(\tau/4\), giving uniform error below \(\tau\).
Thus enumeration terminates under the stated existence assumption.

The enumeration is finite even on other states. Retain the original density
guard; return the bounded fallback if that guard fails or if the finite
candidate list is exhausted without acceptance. The existence hypothesis
ensures that exhaustion does not occur on the states covered by the proposition.

Only the retained training state, one candidate, the net counters, and one
call's numerical workspace are live. Every item has fixed-degree polynomial
size in \(\mathcal P\). During an actual query, evaluate the accepted
circuit at the thresholds required by the original bracket search. There are
\(O(\log(nB_{\mathrm{out}}))\) steps for bounded output range
\([-B_{\mathrm{out}},B_{\mathrm{out}}]\), and its logarithm is already
counted. Choose the circuit error and its evaluation error within the existing
\(1/16\) conditional-test allowance. The original median proof then applies
unchanged to every query parameter. The terminal state supplies the terminal
patch circuit. No query-time integration or training update is performed.
\(\square\)

The required bound \(L_H\) is compatible with the present clipped query
program when its instructions have the stated parameter Lipschitz bounds.
Couple two queries using the same posterior rows and fresh query marks.
If there are \(q\) passive summaries and their common joint Lipschitz bound
is \(\Lambda\geq1\), their differences satisfy

\[
 e_r\leq\Lambda(\|x-x'\|+|s-s'|+e_{r-1}),\qquad e_0=0.
\]

Consequently
\(e_q\leq q\Lambda(1+\Lambda)^q(\|x-x'\|+|s-s'|)\).
The ramp contributes \((2\sigma)^{-1}\) and the same bound for threshold
changes. These estimates hold pointwise in the latent rows, so averaging
under the fixed posterior adds no reciprocal-density factor. Their logarithms
have the required size. Any output map not already included as a summary must
have its own counted bound.

This proposition isolates circuit *existence*, rather than efficient circuit
discovery, as the remaining question. Its existence assumption is substantial
and currently unproved for the actual response family. It is a sufficient
criterion for the posterior-median construction, not a necessary condition for
every possible fast decoder.

Compilation must occur after the relevant prefix has been acquired, using
that prefix alone. One may discard its predecessor's circuit. Precomputing
and retaining all future prefix-specific circuits from the completed source
would encode unacquired future information and is not authorized by this
proposition. Alternatively a compiler could construct a universal circuit
whose inputs include \(c\), but existence of that stronger circuit is also
unproved. Expensive compilation at a state transition is a separate cost from
the fast query assertion; it is not claimed to be fast online training.

## 3. Why full moment compilation loses the absolute exponent

There is an elementary lower bound on a common candidate representation.
Let \(\mu\) be a probability measure on \(\mathbb R^s\), with moments through
degree \(2K\), whose density is positive on a nonempty open set. Suppose
nodes \(z_1,\ldots,z_q\) and weights integrate every polynomial of total
degree at most \(2K\) exactly. Then

\[
 q\geq\binom{s+K}{K}.
\]

To prove this, the polynomials of total degree at most \(K\) form a vector
space of dimension \(\binom{s+K}{K}\), counted by their monomials. If the
number of nodes were smaller, the linear conditions \(p(z_i)=0\) would
have a nonzero polynomial solution. The node rule would give zero for
\(p^2\). Its true integral is positive: a nonzero polynomial cannot vanish
on a nonempty open set, and its square is positive on some open subset of
the positive-density set. This contradicts exactness. Positivity of the
weights is not even needed for this argument.

For fixed latent dimension \(s\) and degree \(K\) of order \(\log n\),
this lower bound is of order \((\log n)^s\). Thus the scheme “retain all
moments or a universal node rule through logarithmic polynomial degree”
cannot obtain a logarithmic exponent independent of dimension. The row
dimension in the present construction is \(d+O(R)\), with growing training
program size \(R\), so indiscriminately treating all row coordinates makes
the count worse.

This is a lower bound for that exact universal cubature requirement. It is
not a lower bound for approximating the specific neural response, for
approximate quadrature with additional structure, or for arithmetic circuits.
For example, a closed-form Gaussian integral can bypass a node rule entirely.
The source-selected \(P+1\) packets preserve the \(P\) realized training
integrands, not every polynomial or every future query integrand. Their
training exactness therefore supplies no missing uniform query theorem.

## 4. Analyticity alone does not provide uniform succinct compilation

The following direct counting argument states the limitation precisely.
Fix a positive strip width \(\rho\) and \(s\) periodic real variables
\(\theta\in[0,2\pi]^s\). There are uniformly strip-bounded real analytic
functions for which any *uniform finite-bit representation of this class*
at accuracy \(\varepsilon\) needs order
\((\log\varepsilon^{-1})^s\) bits. The claim concerns a common analytic
class bound; it is not a trained-network lower bound or a lower bound for
each individual analytic function.

For an integer \(K\geq1\), take the \(M=K^s\) frequency vectors
\(\alpha\in\{1,\ldots,K\}^s\), set
\(a=e^{-2\rho sK}/M\), and independently choose signs
\(\epsilon_\alpha\in\{-1,1\}\). Define

\[
 F_\epsilon(\theta)
   =a\sum_{\alpha\in\{1,\ldots,K\}^s}
          \epsilon_\alpha\cos(\alpha\cdot\theta).
\]

On the complex strip \(|\operatorname{Im}\theta_i|<\rho\), the absolute
value of every cosine is at most \(e^{\rho sK}\), so
\(|F_\epsilon|\leq e^{-\rho sK}\leq1\). These are therefore uniformly
bounded analytic functions on one fixed strip. Their fixed-order real
derivatives are uniformly bounded as well, since exponential decay controls
every fixed power of \(K\).

Two different sign lists differ at some positive frequency \(\alpha\).
The corresponding complex Fourier coefficient of their difference has
magnitude \(a\). A Fourier coefficient, being a normalized integral against
a modulus-one function, is bounded by the real-domain supremum norm.
Thus the \(2^M\) functions are pairwise separated by at least \(a\).
At accuracy \(\varepsilon=a/3\), one decoded function cannot approximate
two members of this family. At least \(2^M\) distinct descriptions are
needed, hence worst-case description length at least \(M-1\) bits.
Finally

\[
 \log\varepsilon^{-1}=2\rho sK+s\log K+\log3=O_{s,\rho}(K),
\]

which proves the stated dimension-dependent lower bound.

A tensor polynomial or Fourier table exhibits the same issue directly.
Analyticity can give logarithmic degree, but the number of independent
coefficients grows as a power of that degree depending on the number of
query variables. Even granting an appropriate spatial complex neighborhood
for the nonlinear decoder, that argument does not supply an absolute power
of \(\log n\). The present sources prove time analyticity where needed;
they do not state a uniform spatial analytic certificate for the posterior
median, which also contains clipping and threshold operations.

The counting argument is deliberately narrower than the target theorem.
It concerns a generic analytic class and common regularity constants.
It neither proves that the constructed functions arise from this fixed
neural-training problem nor defeats arbitrary problem-specific constants.
It explains why “the response is analytic, so compile it” is not a complete
proof. Additional structure of the actual response class is essential.

## 5. What the low-rank training source leaves unresolved

The short causal program supplies learned hidden-matrix displacements of
the form

\[
 D(t)=\sum_{r=1}^{p} c_r(t)a_r b_r^T/n,
 \qquad W(t)=W_0+D(t),
\]

with \(p\) bounded by an absolute power of \(\log n\). Let \(V\) be the
span of the retained right factors \(b_r\), and \(P_V\) its orthogonal
projection. For an arbitrary test feature vector \(h(x)\), the exact action
is

\[
 W(t)h(x)=W_0P_Vh(x)+W_0(I-P_V)h(x)
             +\sum_{r=1}^{p}c_r(t)a_r\langle b_r,h(x)\rangle/n.
\]

The learned term depends on source contractions. The second initialized
term is still a new matrix response unless a further theorem controls or
integrates it. Applying the next nonlinear activation does not preserve
\(V\), and the original assumptions supply no invariant training-feature
span. Spanning inputs in \(\mathbb R^d\) do not remedy this: in general
\(\phi(A\sum_a\alpha_a x_a)\ne\sum_a\alpha_a\phi(Ax_a)\).

The posterior construction integrates these unresolved Gaussian responses
instead of discarding them. Compiling its integrals into a small circuit
would resolve this route. Simply retaining low-rank displacement coefficients
or training Grams does not provide a method to evaluate them at an unseen
input. This identity is not a lower bound: it identifies the term that a
claimed training-basis decoder must approximate, with a uniform error estimate
at the required dense-variability scale.

## 6. Verdict and exact next proof obligation

The current-state denominator can already be cached. A full query table,
generic polynomial-moment rule, or tensor analytic expansion gives no
absolute-exponent improvement. Amortizing their construction across many
queries changes total time accounting, but does not make their retained
tables smaller or bound the first unseen query's runtime. Streamed tables
recover the existing low-space, potentially enormous-time regime.

The new positive conclusion is the conditional compilation proposition:
unrestricted preprocessing removes the need for an efficient algorithm that
*discovers* short response circuits. One still must prove that uniformly
accurate, polynomial-size, stably evaluable circuits exist for the actual
nonlinear current-prefix response functions, with an absolute polynomial
degree. Such a theorem must count coefficients and precision, remain uniform
over the whole input sphere and each time patch, and derive the response
from the original training labels and dynamics. No such theorem follows
from the assigned sources, and this route has not proved it.

Status: elementary conditional compiler argument and representation-specific
obstructions, author derived; no independent reconstruction of this note
has yet been performed. The broad efficient-decoder conjecture remains open.

Input hashes at the read boundary:

```text
9b1e87e3c2e2e74efdf56a40c130c8ff91d74484ab215d6afe03c8ae2c808411  CURRENT_STATE_DECODER_CANDIDATE.md
55dd1adb0234448ac2ec022446fd1c3a4ad7245e26f10deabac614f2ac17b1d1  FOURIER_ROW_PROGRAM_EVALUATION.md
0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5  SHORT_CAUSAL_TRAINING_PROGRAM.md
934ed2e94ecf83f9531d3669960563c28d0e6ea767b72c967c11ffe9b025b061  PREPROCESSING_AND_QUERY_COST.md
```
