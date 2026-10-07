# Independent reconstruction of the noisy two-orientation row law

2026-10-06. Scoped independent check of a finite-program partial theorem.
No experiments, candidate edits, other-study reading, or Git operations.

Audited input: the complete 658-line
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`, SHA-256

`0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac`.

The complete preceding version, hash
`f0f2888fd2d66ac6bec48db6efa2e0686e0a36059d88cee06ad1307b9ca1b8d8`,
was also read. The final version changes inline mathematical delimiters
only; its complete mathematical argument was reread before this check
was frozen.

**Verdict: the exact posterior/innovation representation and its gapped
small-matrix construction pass this reconstruction.** The finite-program
sensitivity conclusion is conditional on the stated intermediate-range
and primitive-sensitivity bounds; RMS control alone is not such a
coordinatewise bound. The global PSD extension is valid. The uniform
passive-query innovation cap requested by the supervisor can be proved
deterministically from whitening, without treating query innovations as
Gaussian after the entire initialized matrix is fixed.

This check does not prove the physical-time approximation, its perturbation
amplification, the bounded row-instruction interface, or a late-query
decoder. It records exactly what the candidate supplies to those tasks.

## 1. Model and adaptive likelihood

Fix one initialized matrix $W=M/\sqrt n$, where $M$ has independent
standard Gaussian entries. Each observed action is either
$Wv+\sigma\xi$ or $W^Tu+\sigma\zeta$, with fresh independent standard
Gaussian noise and $0<\sigma\leq1$. Put $\delta=\sigma^2$.
The observable history includes initial external fields independent of
the matrices, prior query choices, and prior noisy answers. It does not
include the individual raw noise vectors separately.

For the fixed matrix, arrange previous queries and answers as

\[
 Y=WV+\sigma\Xi,\qquad X=W^TU+\sigma Z,
\]

with $V,Y\in\mathbb R^{n\times r}$ and
$U,X\in\mathbb R^{n\times s}$. After the observable history is fixed,
all four arrays are fixed. The conditional likelihood is the product
of the chronological answer densities. Its dependence on $M$ is

\[
 \exp\left[-\frac1{2\delta}
  \left(\|Y-MV/\sqrt n\|_F^2+
        \|X-M^TU/\sqrt n\|_F^2\right)\right].
\tag{1}
\]

Adaptive query dependence introduces no derivative or extra factor:
each query in a chronological conditional density is a known function
of the preceding observed prefix. The same reasoning handles predictable
matrix-label choices and stopping rules, with unused innovation slots
padded independently if a deterministic upper call count is desired.

For several initialized matrices, the fixed-history likelihood (1)
factors by matrix label. Its independent Gaussian prior does also.
Consequently the initialized matrices are conditionally independent
given the complete observable history and external field. Interlacing
their adaptive calls does not invalidate this factorization.

Revealing the raw answer noise would invalidate (1) as a posterior
given that larger information: subtracting it reveals a noiseless
matrix action. The candidate correctly excludes that enlargement.

## 2. Posterior mean and covariance

Expanding (1) and adding the prior quadratic form gives the precision
operator on $M$,

\[
 \mathcal P(B)=B+(UU^TB+BVV^T)/(n\delta).
\tag{2}
\]

It is self-adjoint in the Frobenius pairing and dominates the identity.
Set $A=UU^T/n$, $B_0=VV^T/n$. The mean of $W$ therefore solves

\[
 \delta\overline W+A\overline W+\overline W B_0
                         =(YV^T+UX^T)/n,
\tag{3}
\]

and the centered $W$ covariance operator is
$\delta n^{-1}(\delta I+\mathcal L_A+\mathcal R_{B_0})^{-1}$.
In product eigenbases of $A$ and $B_0$, its independent centered
coordinates have variances $\delta/[n(\delta+a_i+b_j)]$.
This confirms both the normalization and the covariance floor of the
precision operator used in the candidate.

Write the small moments

\[
 Q=V^TV/n,\quad K=U^TU/n,\quad H=U^TY/n,\quad J=X^TV/n.
\]

The last two matrices have the same shape but are not equal for noisy
observations. Put $C=(\delta I+Q)^{-1}$,
$D=(\delta I+K)^{-1}$, and define $E$ by

\[
 (\delta I+K)E+EQ=-HC-DJ.
\tag{4}
\]

The inverse Sylvester operator has Frobenius norm at most $\delta^{-1}$.
Applying the left side of (3) to
$YCV^T/n$, $UDX^T/n$, and $UEV^T/n$ gives, respectively,

\[
 YV^T/n+UHC V^T/n,\quad
 UX^T/n+UDJ V^T/n,\quad
 U[(\delta I+K)E+EQ]V^T/n.
\]

The extra terms cancel by (4), proving

\[
 \overline W=YCV^T/n+UDX^T/n+UEV^T/n.
\tag{5}
\]

For a new forward query $q$, define
$v=V^Tq/n$, $x=X^Tq/n$. Then
$\overline Wq=Y(Cv)+U(Dx+Ev)$.
For a reverse query $c$, define $u=U^Tc/n$, $y=Y^Tc/n$.
Then $\overline W^Tc=V(Cy+E^Tu)+X(Du)$.
These identities use no inverse of a possibly singular history Gram.

## 3. Conditional answer covariance and its square root

For the forward query put $d=\|q\|_2^2/n$ and

\[
 f(a)=\frac{\delta}{\delta+a}
       \left[d-v^T((\delta+a)I+Q)^{-1}v\right],\qquad a\geq0.
\tag{6}
\]

In a target eigendirection of $A$ with eigenvalue $a$, the posterior
variance of $Wq$ is
$\delta q^T((\delta+a)I+B_0)^{-1}q/n$.
Multiplication verifies

\[
 (cI+VV^T/n)^{-1}
 =c^{-1}[I-V(cI+Q)^{-1}V^T/n],\qquad c>0,
\]

which converts this variance to (6). The new independent answer noise
therefore makes the full answer covariance

\[
 \Gamma_q=\delta I+f(A)\succeq\delta I.
\tag{7}
\]

The resolvent representation also gives
$0\leq f(a)\leq d$ and
$-d/\delta\leq f'(a)\leq0$: differentiate the positive resolvent
and use $\delta d/(\delta+a)^2\leq d/\delta$.
The reverse covariance is the same calculation with the source and
target histories exchanged.

Let $f_0=f(0)=d-v^TCv$ and $\beta=\delta+f_0$. Define

\[
 h(a)=\frac{-f_0+\delta v^TC((\delta+a)I+Q)^{-1}v}{\delta+a}.
\tag{8}
\]

The resolvent subtraction
$C-((\delta+a)I+Q)^{-1}
 =aC((\delta+a)I+Q)^{-1}$ gives
$f(a)-f_0=ah(a)$, including the continuous value at zero. Hence

\[
 T(a)=\frac{h(a)}{\sqrt{\delta+f(a)}+\sqrt\beta}
\]

is well defined and bounded even at zero. Singular-vector decomposition
of $U/\sqrt n$ now proves

\[
 \Gamma_q^{1/2}=\sqrt\beta I+UT(K)U^T/n.
\tag{9}
\]

On a nonzero squared singular value $a$, the right side has eigenvalue
$\sqrt\beta+aT(a)=\sqrt{\delta+f(a)}$; off the range of $U$
it has eigenvalue $\sqrt\beta$. This proves that (9) is the positive
square root. Rank deficiency of $U$ is harmless.

The candidate's small-matrix realization also checks. With
$\mathcal B=\delta I+K\otimes I+I\otimes Q$ and
$R_v=I\otimes v$, $R_{Cv}=I\otimes(Cv)$, diagonalizing $K$ only
shows that

\[
 R_v^T\mathcal B^{-1}R_v,\qquad
 R_{Cv}^T\mathcal B^{-1}R_v
\]

are the symmetric functions of $K$ whose scalar values are respectively
$v^T((\delta+a)I+Q)^{-1}v$ and
$v^TC((\delta+a)I+Q)^{-1}v$. Thus its formulas for $f(K)$ and
$h(K)$ are exact. They commute, so the final product forming $T(K)$
is symmetric. Every resolvent/Sylvester inverse has gap $\delta$,
the square-root argument has gap $\delta$, and the last inverse has
gap $2\sigma$. The largest matrix dimension is $rs$.

If $r=0$, the direct formulas are
$f(a)=\delta d/(\delta+a)$ and $h(a)=-d/(\delta+a)$.
If $s=0$, no low-rank correction is needed. Both empty histories give
the expected first-answer covariance $(d+\delta)I$.

## 4. Exact joint innovations, not just conditional marginals

For fresh independent $g\sim N(0,I_n)$, put $t=U^Tg/n$. Equations
(5) and (9) produce the next observed answer exactly as

\[
 Y(Cv)+U(Dx+Ev+T(K)t)+\sqrt\beta\,g.
\tag{10}
\]

Conversely, on the original noisy probability space define

\[
 g=\Gamma_q^{-1/2}(y-\overline Wq).
\tag{11}
\]

Conditional on the observable past, (11) is standard Gaussian and its
conditional law does not depend on that past. Earlier innovations are
measurable functions of earlier observed answers and that history.
Iterated conditional expectation therefore factors every finite product
of bounded functions of the innovations into the product of their
Gaussian expectations. This proves their joint independence, including
across matrix labels.

One may place the complete initial row packets in the external initial
sigma-field: they are independent of the matrices and noises, and the
queries still use only their prescribed functions. The same argument
then proves independence of all innovations from the initial packets.
When those packets are iid across rows, the augmented packets containing
their components and $g_{1,i},\ldots,g_{R,i}$ are indeed iid across $i$.

This does not make the innovations independent of the full initialized
matrix. Nor does it make rows independent conditional on empirical
summaries. Both distinctions matter for subsequent decoder proofs.

The inverse-square-root formula in the candidate is also correct:
rationalizing $a^{-1}(\lambda(a)^{-1/2}-\beta^{-1/2})$, with
$\lambda(a)=\delta+f(a)$, yields its coefficient
$-h(a)/[\sqrt\beta\sqrt{\lambda(a)}
(\sqrt\beta+\sqrt{\lambda(a)})]$.

### Identical-row interface

Optional neuron-dependent deterministic marks do not destroy the iid
law of the random packets themselves. They can, however, make the
row functions non-identical. An expectation factorization is then a
product of row-dependent characteristic functions, not one common
characteristic function to the $n$th power. A deterministic mark array
would additionally need counted storage or a counted coordinate
evaluator. This is an interface qualification, not a defect in the
candidate's joint innovation law. The standard network's constant
marks and iid first-layer Gaussian rows fit the identical-row interface.

## 5. Bounds and quantitative sensitivity

Suppose all old query/answer fields and the new query have RMS at most
$B\geq1$. With at most $R$ past calls, Cauchy--Schwarz gives

\[
 \|Q\|,\|K\|\leq RB^2,\quad
 \|H\|_F,\|J\|_F\leq RB^2,\quad
 \|v\|,\|x\|\leq\sqrt R B^2.
\tag{12}
\]

Equations (4)--(6) imply

\[
 \|C\|,\|D\|\leq\delta^{-1},\qquad
 \|E\|_F\leq2RB^2\delta^{-2}.
\tag{13}
\]

Since $h(a)$ is the divided difference of $f$ and
$|f'|\leq B^2/\delta$,
$\|h(K)\|\leq B^2/\delta$ and
$\|T(K)\|\leq B^2/(2\sigma^3)$.
If $g$ has RMS at most $G$, then $\|t\|\leq\sqrt R BG$.
These reproduce the coefficient bounds in the candidate, including the
extra innovation coefficient bound
$\sqrt R B^3G/(2\sigma^3)$.

For positive matrices with spectra above $a>0$, the inverse difference
identity gives the Frobenius Lipschitz constant $a^{-2}$.
For the square root, put $X=A^{1/2}-B^{1/2}$ and use

\[
 A^{1/2}X+XB^{1/2}=A-B.
\]

Separate orthonormal eigenbases on the two sides show that the inverse
Sylvester operator has norm at most $(2\sqrt a)^{-1}$, with no
commutativity assumption on $A,B$. Subtracting two Sylvester equations
similarly controls their solutions by the right-side difference plus
the coefficient difference times the bounded old solution.

Apply these identities to the finite operation graph giving
$C,D,E,\mathcal B^{-1},f(K),h(K),T(K)$. Each graph has a constant
number of matrix operations; its dimensions are polynomial in $R$.
Tensoring by an identity costs at most a $\sqrt R$ Frobenius factor.
All intermediate amplitudes and inverse gaps are polynomial in
$R,B,G,\sigma^{-1}$. Successive product differences therefore give

\[
 L_{\rm call}\leq
 [C(R+1)(B+G+1)(1+\sigma^{-1})]^C
\tag{14}
\]

for an absolute exponent. This is a polynomial one-call bound, not
an iteration over the entire history hidden inside the exponent.

For the complete finite row/scalar graph, suppose there are $N$ primitive
operations, all intermediate coordinate amplitudes are at most $A_*$,
and their local Lipschitz constants, including (14), are at most $L_*$.
A conservative recursive subtraction gives total sensitivity at most
$[C N(1+A_*)(1+L_*)]^{C N}$. Thus its logarithm is polynomial in
the graph size and the logarithms of these bounds. This verifies the
candidate's global sensitivity conclusion under its explicitly stated
range and primitive-sensitivity hypotheses.

The phrase “RMS at most $B$” alone does not bound coordinatewise
multiplication by a carrier by $B$; an individual coordinate can be
$\sqrt n B$. Such a coordinate cap must be included among $A_*$,
or absorbed by enlarging the amplitude parameter. Its logarithm can
still be polylogarithmic. The candidate does not prove an unqualified
global row sensitivity from RMS estimates alone.

## 6. PSD extension and its limits

For a source layer, the current named-field Gram includes the block
for $(V,X,q)$; for a target layer it includes $(U,Y,g)$ as needed.
Symmetrization, projection to the PSD cone, and radial projection of
that PSD matrix onto a Frobenius ball give a globally bounded,
Frobenius-nonexpansive map. The radial projection remains PSD. Both
projections fix a genuine Gram already inside the cap.

A natural cap is the number of named fields times the square of their
largest RMS bound, since the PSD Gram's Frobenius norm is at most its
trace. This choice is polynomial in the displayed field bounds and
call count. Arbitrarily enlarging a cap must instead be included in
the quantitative parameter list.

Take all moments from these projected complete layer Grams. Then
$K,Q$ are PSD and
$\begin{pmatrix}Q&v\\v^T&d\end{pmatrix}$ is PSD. Every such block
has a Gram realization in some finite Euclidean space. The resolvent
variance calculation in Section 3 applies to that realization and
proves $f(a)\geq0$ for every $a\geq0$. Its dimension need not be the
original width $n$; only this positivity assertion is used off-domain.
All inverse and square-root gaps consequently survive, and (14)
remains polynomial after enlarging the amplitude bounds to cover the
chosen Gram cap.

There is no need to impose $H=J$. They belong to different noisy
cross-moment blocks and that equality is generally false.

These assertions establish a bounded Lipschitz extension of the
coefficient formulas, not its agreement with arbitrary modified
trajectories. Agreement requires every input cap to be inactive on
the particular coupled program being compared. The candidate states
this requirement correctly.

Small-matrix spectral operations here do not reintroduce a width-$n$
oracle. For finite-precision use, their implementations still count.
All matrices have polynomial-in-history dimension and can be stored.
Positive-part projection and square root can, for example, be
approximated uniformly on a supplied bounded spectral interval by
scalar polynomials and evaluated by finite matrix arithmetic. Fine
accuracy can require large degree, but the degree counter and scalar
precision have logarithmic dependence on that degree. The square root
and inverse arguments in the coefficient formulas are gapped; PSD
projection itself is nonexpansive and does not require an eigenvector
selection to be continuous. This supplies a viable counted numerical
interface, while a concrete implementation/error budget remains part
of the invoking evaluator theorem.

## 7. Uniform passive-query innovation cap after fixing the full matrix

This is the main additional route check requested by the supervisor.
It does not use conditional Gaussian tail bounds for a fixed full matrix.

Suppose $\|W\|_{\rm op}\leq K_W$, all past query/answer fields and
the new query have RMS at most $B$, and the new raw oracle noise has
RMS at most $G_{\rm raw}$. From (12)--(13),

\[
 \frac{\|\overline Wq\|_2}{\sqrt n}
 \leq2RB^3\sigma^{-2}+2R^2B^5\sigma^{-4}
 \leq4(R+1)^2B^5\sigma^{-4}.
\tag{15}
\]

For example, the $Y(Cv)$ term is at most
$\sqrt R B\cdot\sqrt R B^2\delta^{-1}$ in RMS; the two $U$
terms give the remaining two bounds. The raw observed answer obeys
$\|y\|_2/\sqrt n\leq K_W B+\sigma G_{\rm raw}$.
Since (7) implies $\|\Gamma_q^{-1/2}\|_{\rm op}\leq\sigma^{-1}$,
the original-space innovation (11) satisfies deterministically

\[
 \|g\|_\infty\leq\|g\|_2
 \leq\sqrt n\left[
  K_W B\sigma^{-1}+G_{\rm raw}
              +4(R+1)^2B^5\sigma^{-5}\right].
\tag{16}
\]

The same proof works for a reverse call, because
$\|W^T\|_{\rm op}=\|W\|_{\rm op}$. The bound remains true after
the initialized matrix and complete training noise tape have been
fixed. It uses only actual Gram consistency, RMS bounds, the raw
answer, and the deliberate covariance floor.

For a simultaneous sphere statement, couple the evaluation at every
input using a common finite raw-noise packet for each passive-query
call. If the forward query program has uniform RMS bounds and this
finite packet has the stated RMS bound, (16) holds for every input.
No union over an uncountable family of independent noises is valid
or required. For each individually fixed input, this coupling still
has the correct fresh-noise conditional law for its own chronology.
It is suitable for proving a uniform observable comparison; it is not
a claim that the query innovations are jointly iid as the input varies.

The cap in (16) is much larger than $\sqrt{\log n}$. Nevertheless
its logarithm is bounded by

\[
 O\bigl(\log n+\log(R+1)+\log(B+1)+\log(K_W+1)
                    +\log(G_{\rm raw}+1)+\log\sigma^{-1}\bigr).
\tag{17}
\]

It is therefore admissible for a row evaluator whose cost and
stability depend polynomially on logarithmic amplitude bounds.
Clipping every innovation coordinate at a cap strictly above (16)
leaves all these coupled passive-query executions unchanged. By
contrast, a $\sqrt{\log n}$ cap justified by claiming Gaussian
typicality conditional on the full $W$ would be unsupported.

The uniform RMS premise in this paragraph is a remaining physical
bridge input. For bounded-depth forward queries it can be propagated
from physical operator/RMS bounds and a common finite raw-noise packet;
the candidate alone is a generic finite-program theorem and does not
prove that particular network estimate.

## 8. Conclusion and precise handoff

The candidate's finite-width representation is exact for predictable
noisy matrix calls in both orientations. Its innovation packets are
jointly iid before conditioning on summaries, the posterior coefficients
have explicit noise-dependent gaps, and the PSD extension removes
off-manifold algebraic singularities without assuming a history Gram gap.
Its small-matrix sensitivity mechanism is valid with counted range and
primitive-sensitivity bounds.

The additional deterministic cap (16) resolves the specific proposed
uniform-query clipping issue, subject to uniform physical RMS bounds
and the stated common-noise coupling. It does not identify an iid
query-innovation law conditional on the entire trained matrix.

Remaining handoff obligations are quantitative approximation of the
physical finite program by the noisy and scalar-regularized program,
global coordinate/intermediate caps, an identical-row or separately
counted deterministic-mark interface, and finite-precision evaluation
where a bit theorem is desired. No complete decoder theorem is inferred
from this scoped PASS.

This reconstruction used only the complete assigned candidate and the
supervisor's uniform-cap question. No linked route notes were read.
The required rigorous-math and conjecture-audit process was applied;
the previously reported canonical-skill access restriction is unchanged.
