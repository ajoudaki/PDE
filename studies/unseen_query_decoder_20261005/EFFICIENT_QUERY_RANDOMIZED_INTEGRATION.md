# Retained random cubature and conditioning identities

2026-10-06. Bounded new theory route, without experiments or Git operations.
The new positive result is a finite-seed random cubature lemma with one event
covering every actual training prefix, sphere input and physical-time patch.
Its memory exponent is independent of input dimension and network depth.
Under additional range and stability bounds its query time is polynomial in
width \(n\). The user has confirmed that query time must be polynomial in
the compact description and requested logarithmic precision. The sampled
construction is therefore a scoped weaker lemma, not an accepted fallback.
The actual neural application also remains conditional.

An additional identity-preserving control-variate construction repairs the
redundant-mean counterexample in the information note. Its applicability to
the actual passive query requires quantitative bounds on the remaining row
functions and their propagation, which are not presently supplied.

## 1. Inputs, model, and computational target

The newly assigned source `EFFICIENT_QUERY_INFORMATION.md` was read in full,
470 lines, with SHA-256

```text
f8dad05300032801a45d47161127c99d3718eefbf61262e5c7be92c9037129a0
```

The previous fully read sources remain the current-state decoder candidate,
Fourier evaluator, short causal training program, preprocessing/query-cost
note, and the two small-matrix notes from the bounded numerical check. No
other studies or route reports were accessed for this continuation. The
required proof/research skills and the previously authorized fallback for
the unreadable canonical-notation skill remain in force.

The target remains the original full-label nonlinear network, Gaussian
initialization, zero readout, original gradient-flow scaling, admissible
spanning data and small-label condition. The predictor is compared on the
whole sphere \(\|x\|=\sqrt d\), through every time and the fitted endpoint,
with the inherited dense-variability certificate \(b_n\). No test input is
known at training time. A query cannot access dense roots or run the training
scalar recursion again. All retained random bits and all workspace count.
The confirmed runtime target is polynomial in the compact description, not
polynomial in the original width \(n\) or comparable to a dense forward pass.

The new seed is drawn independently of the training source and retained.
Conditional on this finite seed, the resulting query map is deterministic.
The probability statement is over the source and this additional seed. There
is no fresh query-specific success event. This is a change in the construction
of the decoder, not a claim that fresh randomness at each query would suffice
for the original simultaneous guarantee.

Primitive-time statements count the original activation calls. Bit-time
statements additionally require polynomial-time activation and input precision
interfaces; the earlier polynomial-space assumption alone does not imply this.

## 2. A finite-seed uniform Gaussian cubature lemma

Let \(\mu=N(0,I_D)\). Conditional on a fixed complete training tape, consider
finitely many row-function families

\[
 h_\ell(z;\theta),\qquad 1\leq\ell\leq J_0,
 \qquad \theta\in\Theta.
\]

The index \(\ell\) may include the acquired training prefix, physical-time
patch, and passive-query instruction. The parameter set \(\Theta\) contains
the sphere coordinate and a bounded patch-time coordinate; a bounded threshold
coordinate may also be included. Assume uniform bounds

\[
 |h_\ell|\leq B,
 \qquad |h_\ell(z;\theta)-h_\ell(z';\theta)|
             \leq L_z\|z-z'\|_\infty,
 \qquad |h_\ell(z;\theta)-h_\ell(z;\theta')|
             \leq L_\theta\|\theta-\theta'\|,
\]

where \(B,L_z,L_\theta\geq1\). Let \(0<u,\beta\leq1/4\).
Suppose a finite net of \(\Theta\) of mesh
\(h=u/(8L_\theta)\) has cardinality at most \(M_\Theta\).
This is a proof-only net and is not retained. For a sphere times a fixed
number of bounded intervals,

\[
 \log M_\Theta
 \leq C(d+c)\log\!\left(2+
       \frac{C(d+1)L_\theta(1+\text{parameter range})}{u}\right),
\]

where \(c\) is the number of interval coordinates. A cube grid followed by
normalization of points near the unit sphere proves such a bound: if
\(\|g-v\|\leq e\leq1/2\) and \(\|v\|=1\), then
\(\|g/\|g\|-v\|\leq2e\).

Choose an even integer

\[
 k\geq2,\qquad 2J_0M_\Theta4^{-k}\leq\beta,
 \qquad Q\geq256kB^2u^{-2}.
 \tag{1}
\]

There is an explicitly specified retained random seed of polynomial length
in

\[
 D+k+\log Q+\log B+\log L_z+\log u^{-1}
 \tag{2}
\]

which generates \(Q\) row points sequentially. With probability at least
\(1-\beta\), their numerically evaluated empirical averages approximate
\(\int h_\ell(z;\theta)\,\mu(dz)\) to error at most \(u\),
simultaneously for every \(\ell\) and every \(\theta\). The per-query
time is \(Q\) times a polynomial in (2), the function-description size
and logarithmic numerical precision. Peak workspace, including the seed,
is polynomial in these logarithmic parameters, not in \(Q\).

### 2.1 Finite Gaussian approximation

Choose \(A\) to be the smallest integer at least one satisfying
\(A^2\geq2\log(32DB/u)\). Clipping a Gaussian vector to
\([-A,A]^D\) changes every displayed expectation by at most \(u/8\):
the exceptional probability is at most \(2D e^{-A^2/2}\), and the
function difference is bounded by \(2B\).

Let \(U\) be uniform on \([0,1]\), and let \(q_A(U)\) be the Gaussian
quantile clipped to \([-A,A]\). On its nonconstant interval its derivative
is at most \(\sqrt{2\pi}e^{A^2/2}\), and the same global Lipschitz bound
holds across its two constant pieces. Replacing \(U\) by a midpoint of a
\(2^{-b}\)-grid and evaluating \(q_A\) to error \(\zeta\) changes a
coupled row coordinate by at most

\[
 \sqrt{2\pi}e^{A^2/2}2^{-b}+\zeta.
\]

Choose this at most \(u/(8L_z)\). The finite row law \(\nu\), generated
from \(Db\) uniform bits, then has expectation bias at most \(u/4\) for
every function in the family. The required \(b\) and output precision are
polynomial in the logarithms in (2).

This quantile routine need not be an oracle. On \([-A,A]\), integrate the
Taylor series for \(e^{-t^2/2}\), with the explicitly bounded remainder,
to evaluate the Gaussian CDF; a degree polynomial in \(A^2\) and requested
bits suffices. For example the exponential remainder is bounded by
\(e^{A^2/2}(A^2/2)^{N+1}/(N+1)!\); taking
\(N\geq C(A^2+b_{\rm work}+1)^2\) makes it smaller than the required
dyadic error. Bisection using the lower density
\((2\pi)^{-1/2}e^{-A^2/2}\) then evaluates the clipped inverse to the
chosen error. If the CDF comparison is uncertain within its numerical
tolerance, that density bound directly certifies the required position
error. Endpoint clipping is handled by the same tolerance rule. One can avoid
a normalizing-constant oracle by computing the CDF as a ratio of integrals of
\(e^{-t^2/2}\), truncating both at \(\pm T\) with \(T^2\) linear in
the requested precision plus a safety margin. The Gaussian tail bounds its
truncation error, and the denominator is bounded below by its integral over
\([-1,1]\), which exceeds one. Both bounded-interval integrals use the same
Taylor procedure. Scalar square roots use the counted numerical routine.
Thus this step has polynomial arithmetic and bit cost in the parameters
just specified, without adding an exact Gaussian-quantile primitive.

### 2.2 The retained seed and its exact independence property

Take \(w=\max\{Db,\lceil\log_2(Q+1)\rceil\}\).
Retain an irreducible binary polynomial of degree \(w\), defining the
field \(\mathbb F_{2^w}\), and retain \(k\) independent uniform field
elements \(a_0,\ldots,a_{k-1}\). For distinct field elements indexed by
\(i=1,\ldots,Q\), compute

\[
 V_i=\sum_{j=0}^{k-1}a_j i^j.
 \tag{3}
\]

Any at most \(k\) of these values are independent and uniform: the
corresponding evaluation map has full row rank by the nonzero Vandermonde
determinant, so each possible output has equally many coefficient preimages.
Use the first \(Db\) bits of \(V_i\) as the independent uniform coordinate
bits in Section 2.1. The resulting finite Gaussian rows are exactly
\(k\)-wise independent with common law \(\nu\).

The field polynomial and coefficients use at most \((k+1)w+1\) bits;
the random part is exactly \(kw\) bits. Field
evaluation by Horner's rule uses \(O(k)\) polynomial multiplications and
reductions, each with polynomial bit cost in \(w\). Only the current index,
row, function workspace and accumulator are live.

Existence and construction of the field polynomial do not require an assumed
pseudorandom-generator theorem. One may search all monic binary degree-\(w\)
polynomials and test divisibility by every nonconstant monic polynomial of
degree at most \(w/2\). Candidate/divisor counters and polynomial long
division use \(O(w^2)\) workspace and unrestricted preprocessing
time. Existence follows directly by taking a splitting field of
\(X^{2^w}-X\): its roots are closed under addition, multiplication and
nonzero inversion, and its derivative is one, so they form a field of
exactly \(2^w\) elements. Splitting fields can be obtained by successively
adjoining roots of irreducible factors. An element of degree less than \(w\)
has degree dividing \(w\), hence at most \(w/2\); elements of degree
\(e\) are roots of \(X^{2^e}-X\), so there are at most \(2^e\) of them.
The sum over \(1\leq e\leq w/2\) is smaller than \(2^w\) for
\(w\geq2\). Thus an element of degree \(w\) exists and its minimal
polynomial is the required irreducible polynomial. The case \(w=1\) is
immediate. None of this large search is repeated at query time.

### 2.3 Concentration, one event, and numerical storage

At a fixed net point and function, center the bounded row values by their
\(\nu\)-expectation. Their average's \(k\)-th moment equals that of
fully independent rows, because its expansion uses at most \(k\) distinct
indices. For independent values in \([-B,B]\), the centered log moment
generating function gives
\(\Pr(|\overline h-\mathbb E_\nu h|>t)
 \leq2\exp[-Qt^2/(2B^2)]\).
The elementary proof differentiates the log moment generating function
twice and bounds each tilted variance by \(B^2\). Integrating the tail
for the even moment \(k\) yields

\[
 \mathbb E|\overline h-\mathbb E_\nu h|^k
 \leq2\left(\frac{kB^2}{Q}\right)^{k/2}.
\]

Markov's inequality and (1) give failure at most \(2\cdot4^{-k}\)
for deviation \(u/4\). A union over the \(J_0M_\Theta\) net tests
costs at most \(\beta\). Both the empirical and exact expectations are
\(L_\theta\)-Lipschitz, so passage from the net adds at most \(u/4\).
The Gaussian-discretization bias adds at most \(u/4\). Function evaluation
and accumulation can share the remaining \(u/4\) budget.

Weighted summation stores one accumulator. A precision including
\(\log Q+\log u^{-1}\) controls total rounding from its \(Q\) updates.
Neither the net nor a list of row points is retained. Conditional on any
training tape satisfying the uniform parameter bounds, the seed succeeds
with probability at least \(1-\beta\). Averaging that statement over the
training source proves one joint event. The same seed can therefore be
chosen independently at initialization, and its uniform success includes
inputs chosen adaptively after inspecting earlier answers.

## 3. Consequences for a population passive-query program

The information note defines, at current prefix \(c\),

\[
 d_r=\int G_r(z;c,d_{<r};x,s)\,\mu(dz),\qquad 1\leq r\leq q.
 \tag{4}
\]

The exact functions
\(h_r(z;x,s)=G_r(z;c,d_{<r}(x,s);x,s)\) do not depend on the cubature
seed. Apply Section 2 to these functions for every actual prefix and patch.
It is unnecessary to take a net over every possible acquired \(c\): first
condition on the complete actual training tape. The parameter Lipschitz
bounds follow by propagation through the deterministic recursion whenever
the supplied instruction bounds give them. Their logarithms may be large,
but only those logarithms enter seed length.

Suppose the empirical evaluation at perturbed summary arguments has common
Lipschitz constant \(\Lambda\geq1\), and the final output is
\(L\)-Lipschitz. On the single cubature event, subtraction at the exact
arguments in (4) gives

\[
 e_r\leq(1+\Lambda)e_{r-1}+u,
 \qquad |\widehat d_{\rm out}-d_{\rm out}|
       \leq A_{
          \rm out}u,
 \qquad A_{\rm out}=(1+L)q(1+\Lambda)^q.
 \tag{5}
\]

Here \(e_r\) is the largest summary error through step \(r\).
Reusing one seed at the adaptively computed summary arguments causes no
independence error: the concentration event was applied to the deterministic
exact arguments, and the other difference is controlled pointwise by the
Lipschitz estimate.

For desired output error \(\epsilon\), choose
\(u=\epsilon/A_{\rm out}\). Up to fixed factors, the sufficient number
of streamed rows is

\[
 Q=O\!\left(k B^2 A_{\rm out}^2\epsilon^{-2}\right),
 \qquad k=O\!\left(1+\log(J_0M_\Theta/\beta)\right).
 \tag{6}
\]

If \(\log B,\log A_{\rm out},D\), the instruction count and all
logarithmic precisions are absolute powers of \(\log n\), the retained
seed and workspace remain absolute-polylogarithmic. If additionally
\(BA_{\rm out}\) and \(\epsilon^{-1}\) are polynomial in \(n\),
the query time is polynomial in \(n\). The current generic certificates
permit \(BA_{\rm out}=\exp[\operatorname{polylog}(n)]\); therefore even
this polynomial-\(n\) conclusion requires an additional bound.

At accuracy comparable to \(b_n\), ordinary bounded-row sampling can
require order \(n\), up to the inherited subpolynomial and logarithmic
factors, even when the amplification and range are polylogarithmic.
Equation (6) is an upper bound for this witness, not a lower bound for every
decoder. It does not establish polynomial time in the compact description.

Most importantly, accurate numerical evaluation of (4) does not justify
replacing the posterior query by (4). The information note's separate
statistical stability condition remains necessary for this route. Random
cubature solves an integration problem only after a valid target integral
has been identified.

## 4. Conditioning identities as control variates

The preceding statistical issue has a useful exact refinement. At prefix
\(c\), suppose a passive row instruction admits the identity

\[
 G_r(z;c,u;x,s)
   =\sum_{\ell\leq j}\alpha_{r\ell}(c,u;x,s)
                  F_\ell(z;c_{<\ell})
       +R_r(z;c,u;x,s).
 \tag{7}
\]

All functions and coefficients here must be explicitly computable from the
current retained description. The coefficient sum is bounded by
\(\sum_\ell|\alpha_{r\ell}|\leq A_F\), and suppose
\(|R_r|\leq B_R\). No equality of population and observed training means
is assumed. The actual noisy history gives the exact identity

\[
 \frac1n\sum_iG_r(Z_i;c,u;x,s)
 =\sum_\ell\alpha_{r\ell}c_\ell
   +\frac1n\sum_iR_r(Z_i;c,u;x,s)
   -\eta\sum_\ell\alpha_{r\ell}E_\ell.
 \tag{8}
\]

Define the anchored population query recursively by

\[
 d_r=\sum_\ell\alpha_{r\ell}(c,d_{<r};x,s)c_\ell
          +\int R_r(z;c,d_{<r};x,s)\,\mu(dz).
 \tag{9}
\]

The retained training means are therefore reused in exact identities;
only the residual is integrated under the prior. This neither updates the
training history nor conditions on the private selected packet panel.
Although private noise marks appear in the proof of (8), they are not inputs
to (9).

Here is a precise posterior transfer bound. Let \(H\) be the information
budget in the assigned note, and take its all-prefix entropy event
\(K_j(c)\leq H/\alpha\). Choose positive failure budgets
\(\rho_R,\rho_E,\rho_q\). The same entropy inequality applied to the
\(q\) residual functions at the deterministic arguments in (9) gives

\[
 a_R=B_R\sqrt{\frac2n\left[
          \log(2q)+\frac{H/\alpha+\log2}{\rho_R}\right]}.
 \tag{10}
\]

With conditional probability at least \(1-\rho_R\), all residual empirical
means are within \(a_R\) of their prior expectations, for every fixed
query on that same training event. Uniform constants make this assertion
valid for every query parameter without adding training exceptional sets.

The historical-noise term is also controllable at all prefixes. Let
\(\mathcal E=\{\max_{\ell\leq P}|E_\ell|\leq T\}\). Its prior
failure is at most \(2P e^{-T^2/2}\). The process
\(\Pr(\mathcal E^c\mid C_{\leq j})\) is a nonnegative martingale.
Its elementary first-crossing inequality implies that, outside a training
event of probability at most \(2P e^{-T^2/2}/\rho_E\), every prefix
posterior assigns probability at most \(\rho_E\) to \(\mathcal E^c\).
For example choose \(T^2\geq2\log(2P/(\alpha_E\rho_E))\).
Fresh scalar query noises of scale \(\eta_q\) are bounded by \(T_q\)
with conditional failure at most \(2q e^{-T_q^2/2}\leq\rho_q\).

If the original empirical query drift is \(\Lambda_G\)-Lipschitz in
its summary prefix and the output is \(L\)-Lipschitz, subtract its
recursion from (9), using (8) at the deterministic arguments. This gives

\[
 |U_c(x,s)-d_{\rm out}(c,x,s)|
 \leq (1+L)q(1+\Lambda_G)^q
            [a_R+\eta A_F T+\eta_qT_q]
 =:\Delta
 \tag{11}
\]

with conditional failure at most \(\rho_R+\rho_E+\rho_q\), at every
prefix on the stated common training events. All added events and constants
have been displayed; no assumption of independent posterior rows is used.

Combine (11) with the original posterior-center mass of \(5/8\). If its
failure budget is below \(5/8\), the two posterior output intervals
overlap. The anchored deterministic output is then within
\(2b_n+\epsilon_{\rm bridge}+\Delta\) of the dense predictor. Random
cubature of the residual in (9), using a valid Lipschitz bound for the
anchored recursion, adds its uniform numerical error \(\epsilon\).
This yields one sphere/time event after allocating the entropy, noise,
original-source, and seed failure budgets. It preserves an \(O(b_n)\)
scale only when \(\Delta+\epsilon=O(b_n)\); it does not automatically
retain the exact old coefficient \(2b_n+1/n\).

For the information note's example, \(F_1(z)=\operatorname{clip}_{[-1,1]}z\)
and the query reuses exactly that mean. Take \(\alpha_{11}=1\) and
\(R_1=0\). Formula (9) returns \(d_1=c_1\), so its output
\(\tanh((d_1-c_1)/\sigma)\) is exactly zero. The remaining error is
controlled by \(\eta/\sigma\) times historical and fresh scalar noises.
Thus the dangerous \(1/\sigma\) amplification no longer acts on an
independent empirical fluctuation. No cubature samples are needed in this
special case. This verifies the utility of preserving the conditioning
identity, without claiming that every nonlinear query has such a small
residual representation.

For the actual neural model, no bound on \(B_R\), \(A_F\), or the
relevant propagation after such a decomposition has been established in
the assigned sources. Taking all \(\alpha\) equal to zero recovers the
existing population substitution and its unresolved bound. The exact
algebra (7) is consequently a concrete next proof target, not a completed
neural decoder.

## 5. Why matching a posterior mean need not stabilize importance weights

A solvable Gaussian diagnostic distinguishes identity-preserving conditioning
from a product tilt. This diagnostic uses an unbounded Gaussian row function;
it is not asserted to be the bounded neural row circuit.

Let \(Z_i\) be independent standard Gaussians and observe
\(C=n^{-1}\sum_iZ_i+\eta E\). Given \(C=c\), the row-vector posterior
is Gaussian with common mean \(m=c/(1+n\eta^2)\). In the unit direction
\(n^{-1/2}(1,\ldots,1)\), its variance is

\[
 v=\frac{n\eta^2}{1+n\eta^2};
\]

all orthogonal variances remain one. These formulas follow by completing
the square in the prior density times
\(\exp[-(c-n^{-1}\sum_i z_i)^2/(2\eta^2)]\).

The product proposal \(\nu=N(m,1)^{\otimes n}\) matches the posterior
mean exactly. In the collective direction its centered variance remains
one. The normalized posterior importance weight is
\(w(t)=v^{-1/2}\exp[-(1/v-1)t^2/2]\), where \(t\sim N(0,1)\)
under \(\nu\). Direct Gaussian integration gives

\[
 \mathbb E_\nu w^2=\frac1{\sqrt{v(2-v)}},
 \qquad D(\pi\Vert\nu)=\tfrac12(v-1-\log v).
 \tag{12}
\]

For \(\eta\sqrt n\ll1\), the second moment is of order
\((\eta\sqrt n)^{-1}\), while the entropy is only of order
\(\log(1/(\eta\sqrt n))\). The permitted scale
\(\eta=\exp[-\log^2(en)]\) makes the former superpolynomial in \(n\)
and the latter polylogarithmic. Small information and a correctly matched
mean therefore do not, by themselves, bound ordinary importance-sampling
variance.

This example is not an impossibility result: the collective Gaussian
coordinate can be sampled with its correct variance directly. That repair
uses its exact conditional structure. For the nonlinear row program, an
analogous stable conditional sampler or residual identity must be constructed
and counted; a proposed low-information product tilt does not establish it.

## 6. Relation to the Fourier integral and final status

The finite-seed lemma could approximate a single-row characteristic function
uniformly over its frequency/query box. Its finite-law empirical estimator
is unbiased for that finite-law characteristic function. Raising it to the
\(n\)-th power, projecting it to the unit disk, and taking a ratio are not
unbiased operations. The existing deterministic absolute-error estimates
remain necessary for those steps.

More seriously, the Fourier numerator requires a row error small enough to
absorb its integration volume, the factor \(n\), and the posterior-density
lower bound. Those logarithms are polynomial in the compact parameters,
but their reciprocals can be \(\exp[\operatorname{polylog}(n)]\).
The sample count proportional to squared reciprocal accuracy can therefore
be superpolynomial in \(n\). The outer frequency/query grid would also
remain. Randomizing only the Gaussian row integral does not solve these
two problems or produce a stable unbiased posterior test.

The useful weaker conclusion is precise: bounded and sufficiently stable
population or anchored-residual queries admit a finite retained seed,
absolute-polylogarithmic workspace, polynomial-\(n\) query time under
the displayed additional bounds, and one event for every input and time.
No pseudorandom-generator oracle or retained sample table is needed.
This is a scoped weaker lemma and is not an accepted fallback for the
confirmed target. Polynomial time in the compact description is still
unproved. For the
actual neural model, the unresolved bridge is an identity-preserving
conditional representation with quantitative residual and propagation
bounds; low information alone does not supply it.

Status: conditional author derivations; the confirmed runtime target remains
unresolved by this lemma.
The previous current-state decoder theorem and its original guarantees
are unchanged. No full efficient-decoder theorem is claimed.
