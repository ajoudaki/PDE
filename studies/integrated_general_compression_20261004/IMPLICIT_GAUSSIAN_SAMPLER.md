# Exact adaptive sampling of an implicit Gaussian matrix

Status: candidate proof, pending independent audit. This is a finite-dimensional
construction in an exact-real arithmetic model. It is not a width limit, a
numerical-stability theorem, or a promoted result in the maintained book.

Scientific input scope: the supervisor's assignment, `docs/notation.qmd`, and
Sections 1–2 of `docs/02-gaussian-reuse.qmd`. No other study or prior discussion
was consulted. The requested canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` could not be
read because access was denied; no accessible replacement was found in the
available skill roots. The fallback uses the supplied presentation requirements
and the maintained notation contract. The rigorous-math skill was read and
applied. No statistical, training, or numerical experiments were run.

## 1. Statement and computational model

Fix an integer width $n\geq1$, a finite set of layer indices
$\mathcal I$, and deterministic nonnegative query budgets
$k_\ell$, $\ell\in\mathcal I$. In the dense reference model,

\[
 W^{(\ell)}\in\mathbb R^{n\times n},\qquad
 W^{(\ell)}_{ij}\ \text{are jointly independent }N(0,1/n)
 \quad(\ell\in\mathcal I, 1\leq i,j\leq n).
\]

Let $\xi$ denote all independent randomness used by the querying algorithm;
it is independent of these matrices. At each step the algorithm either stops
or chooses, measurably from $\xi$ and the global past transcript, a layer,
a direction of multiplication, and a finite vector in $\mathbb R^n$. The
reply is $W^{(\ell)}v$ for a forward query or
$(W^{(\ell)})^T u$ for a transpose query. The transcript includes query
choices and replies. There are at most $k_\ell$ queries to layer $\ell$,
including zero, repeated, and linearly dependent queries. The stopping time is
at most $\sum_\ell k_\ell$. No observation of a reference matrix outside this
interface is allowed.

The sampler below receives the queries, draws fresh standard Gaussian scalar
variables as needed, and returns replies. Its Gaussian draws are independent
of $\xi$; its private random tape is not an extra observation made available
to the querying algorithm.

**Theorem.** For every such querying algorithm, the sampler has exactly the
same joint law of $\xi$, queries, replies, stopping time, and every measurable
quantity computed from them as the dense reference model. On an extension of
the sampler's probability space, matrices $\widehat W^{(\ell)}$ can be
defined so that:

1. Their entries are jointly independent $N(0,1/n)$, independently of
   $\xi$.
2. Every reply actually returned by the sampler equals the corresponding
   product with $\widehat W^{(\ell)}$, simultaneously and almost surely.
3. The joint law including these matrices is the dense reference joint law.

This completion is only a proof coupling. The sampler does not initialize a
dense reference matrix or evaluate the dense Gaussian remainder in that
coupling. Its stored matrix information consists only of query bases and their
answers, as described below.

For a layer receiving $k\geq0$ queries, the following bounds hold. Here a
scalar addition, subtraction, multiplication, division, or square root costs
one arithmetic operation; generating one exact standard Gaussian scalar costs
one Gaussian draw. One exact real scalar or integer/address occupies one word.
These are idealized real-arithmetic and Gaussian-generation primitives, not
claims about finite-bit implementations.

\[
\begin{aligned}
\text{arithmetic operations}
 &\leq 4nk^2+6nk+2,\\
\text{Gaussian draws}
 &\leq n\min\{k,2n-1\}\leq nk,\\
\text{sampler words}
 &\leq 2n\min\{k,2n\}+8n+5\min\{k,2n\}+64.
\end{aligned}
\]

There are at most $k$ zero tests and $k$ further rank comparisons. These bounds exclude the querying algorithm's
own work and storage, including any transcript it elects to retain. They include
one current query/reply workspace. For $k\geq1$, they are $O(nk^2)$ arithmetic
and $O(nk)$ words. The two initialization arithmetic operations can be shared
between all layers of the same width. In particular, globally the arithmetic
bound is

\[
 2+\sum_{\ell\in\mathcal I}(4n k_\ell^2+6n k_\ell),
\]

and the Gaussian-draw bounds add across layers. A sum of the displayed per-layer
memory bounds is a valid global bound; the vector workspace can also be shared.
When all query budgets are zero the sampler need not allocate vector workspace.

The budgets may depend arbitrarily on $n$. There is no asymptotic assertion
and no assumption that the input vectors are well conditioned.

The proof maintains the conditional Gaussian law after every query. An
orthogonal split isolates the newly observed Gaussian vector from the
unobserved matrix remainder. This proves the answer kernels, preserves the
conditional product law across layers, and supplies the stopped completion
coupling.

## 2. Stored state and the online algorithm

Suppress the layer superscript while describing one layer. The sampler stores
four matrices, initially with zero columns:

\[
 V,Y\in\mathbb R^{n\times p},\qquad
 U,R\in\mathbb R^{n\times q}.
\]

The columns of $V$ form an orthonormal basis of the span of the forward
query vectors seen so far; the columns of $U$ form an orthonormal basis of
the span of the transpose query vectors seen so far. The stored answers have
the meaning $Y=WV$, $R=W^T U$. This meaning will be supplied by the
coupling proof; an actual $W$ is not an input to the algorithm. The state
always satisfies

\[
 V^T V=I_p,\qquad U^T U=I_q,\qquad U^T Y=R^T V.
\tag{1}
\]

Empty matrix products are zero. Precompute $\sigma=1/\sqrt n$. Every
normalization and every zero test below is exact. In particular, a small
positive norm is not rounded to zero.

### Forward query $v\in\mathbb R^n$

Using the old state, compute

\[
 a=V^T v,\qquad v_\perp=v-Va,\qquad
 \alpha=\sqrt{v_\perp^T v_\perp}.
\]

If $\alpha=0$, return $Ya$, leave the state unchanged, and draw no
randomness. Otherwise compute

\[
 e=v_\perp/\alpha,\qquad b=R^T e.
\]

If $q<n$, draw $g\in\mathbb R^n$ with independent $N(0,1)$ coordinates
and set

\[
 h=Ub+\sigma\{g-U(U^Tg)\}.
\tag{2}
\]

If $q=n$, set $h=Ub$ without drawing $g$. Return

\[
 Ya+\alpha h,
\tag{3}
\]

then append the column pair $(e,h)$ to $(V,Y)$. The returned expression
uses the old $V,Y$ and old coefficient $a$. The order of appending and
returning can be reversed in an implementation that preserves those values.

### Transpose query $u\in\mathbb R^n$

Using the old state, compute

\[
 b=U^T u,\qquad u_\perp=u-Ub,\qquad
 \beta=\sqrt{u_\perp^T u_\perp}.
\]

If $\beta=0$, return $Rb$, leave the state unchanged, and draw no
randomness. Otherwise compute

\[
 f=u_\perp/\beta,\qquad a=Y^T f.
\]

If $p<n$, draw fresh $g\in\mathbb R^n$ with independent $N(0,1)$
coordinates and set

\[
 h=Va+\sigma\{g-V(V^Tg)\}.
\tag{4}
\]

If $p=n$, set $h=Va$ without drawing $g$. Return

\[
 Rb+\beta h,
\tag{5}
\]

then append $(f,h)$ to $(U,R)$.

For multiple layers, retain a separate quadruple $(V,Y,U,R)$ per layer and
apply the corresponding rule to the chosen layer. All fresh $g$'s, across
all times and layers, are independent. The algorithm forms only matrix-vector
products with the stored columns. In particular, neither an $n\times n$
projector nor the conditional-mean matrix used in the proof is formed.

## 3. Elementary Gaussian splitting used in the proof

The needed Gaussian fact can be verified directly. If
$Z\in\mathbb R^d$ has independent $N(0,\tau^2)$ coordinates and
$A,B$ are deterministic linear maps with $AB^T=0$, then $AZ$ and
$BZ$ are independent centered Gaussian vectors. Indeed their joint
characteristic function at $(s,t)$ is

\[
 \mathbb E e^{i(s^TAZ+t^TBZ)}
 =\exp\!\left(-\frac{\tau^2}{2}
       \|A^T s+B^Tt\|_2^2\right).
\]

The cross term is $2s^TAB^Tt=0$, so this factors as the product of the
two marginal characteristic functions. This proves independence even when
either covariance is singular. Applying this to the vector of matrix entries
justifies every orthogonal Gaussian split below. No nonsingular covariance or
matrix inverse is needed.

For fixed state satisfying (1), define, for proof purposes only,

\[
 P=VV^T,\qquad Q=UU^T,\qquad
 M=YV^T+UR^T(I-P).
\tag{6}
\]

The compatibility identity in (1) implies

\[
 MV=Y,\qquad
 M^TU=VY^TU+(I-P)R=PR+(I-P)R=R.
\tag{7}
\]

The matrices preserving homogeneous versions of these observations are
exactly

\[
 \{A:AV=0, A^TU=0\}
 =\{(I-Q)B(I-P):B\in\mathbb R^{n\times n}\}.
\tag{8}
\]

For the forward inclusion, $AV=0$ implies $AP=0$, and $A^TU=0$
implies $QA=0$. For the reverse inclusion use $(I-P)V=0$ and
$(I-Q)U=0$. Each summand of $M$ in (6) is Frobenius-orthogonal to
the space in (8): the first has right support in $\operatorname{span}(V)$,
and the second has left support in $\operatorname{span}(U)$.

Thus the candidate conditional matrix law at this state is

\[
 W=M+(I-Q)G(I-P),
 \qquad G_{ij}\ \text{independent }N(0,1/n).
\tag{9}
\]

The induction below proves (9) as a conditional-law identity after adaptive
queries. It does not infer adaptive conditioning merely by treating random
query directions as fixed in an unconditional formula.

## 4. One query updates the conditional law exactly

Assume (9) holds conditional on the full past. Once that past and the
independent querying randomness are conditioned on, the next query direction
and selected layer are fixed.

For a forward query, the algorithm's orthogonal decomposition is
$v=Va+\alpha e$ when $\alpha>0$. If $\alpha=0$, (7) gives the
deterministic answer $Ya$; receiving that answer conveys no additional
information. If $\alpha>0$, then $\|e\|_2=1$, $Pe=0$, and

\[
 We=UR^T e+(I-Q)Ge.
\tag{10}
\]

The coordinates of $Ge$ are independent $N(0,1/n)$: distinct coordinates
use independent rows of $G$, and the variance in each row is
$\|e\|_2^2/n=1/n$. Consequently (2) has exactly the conditional law of
$We$, and (3) has that of $Wv$. If $q=n$, $Q=I$, so the random
term is identically zero and skipping it preserves the law.

It remains to verify that the remaining randomness has the claimed form
after the new answer. Let

\[
 P'=P+ee^T,\qquad
 E=(I-Q)Ge,\qquad
 D=(I-Q)G(I-P').
\]

The remainder in (9) splits as

\[
 (I-Q)G(I-P)=Ee^T+D.
\tag{11}
\]

The random vector $E$ and matrix $D$ are independent. One direct
covariance calculation is

\[
 \operatorname{Cov}(E_i,D_{ab})
 =\frac1n(I-Q)_{ia}\bigl[e^T(I-P')\bigr]_b=0,
\]

because $P'e=e$. They are jointly Gaussian linear functions of the entries
of $G$, so the characteristic-function argument in Section 3 proves the
asserted independence, including all singular cases. The covariance and mean
of $D$ are those of $(I-Q)G'(I-P')$ for fresh iid
$G'_{ij}\sim N(0,1/n)$.

Observing the reply is equivalent to observing $h=We$, since
$h=(Wv-Ya)/\alpha$ and $\alpha>0$. By (10) this specifies
$E=h-UR^T e$ while leaving $D$ independent and unchanged in law.
The new stored columns satisfy $U^Th=R^Te$, since the noise is annihilated
by $U^T$. Hence (1) remains valid. The new mean computed by (6) is

\[
\begin{aligned}
 M'&=YV^T+he^T+UR^T(I-P-ee^T)\\
   &=M+(h-UR^Te)e^T=M+Ee^T.
\end{aligned}
\]

Together with (11), this is exactly the updated kernel
$M'+(I-Q)G'(I-P')$.

For a transpose query with $\beta=0$, (7) gives the deterministic answer
$Rb$. With $\beta>0$, $Qf=0$ and $\|f\|_2=1$, so

\[
 W^Tf=VY^Tf+(I-P)G^Tf.
\tag{12}
\]

Thus (4) is its conditional law. Put

\[
 Q'=Q+ff^T,\qquad
 E=(I-P)G^Tf,\qquad D=(I-Q')G(I-P).
\]

Then $(I-Q)G(I-P)=fE^T+D$, and

\[
 \operatorname{Cov}(E_i,D_{ab})
 =\frac1n(I-P)_{ib}\bigl[f^T(I-Q')\bigr]_a=0.
\]

The same characteristic-function argument shows that $E$ and $D$ are
independent. The observed column $h=W^Tf$ specifies
$E=h-VY^Tf$, while $D$ keeps the law of
$(I-Q')G'(I-P)$. Compatibility is preserved because $V^Th=Y^Tf$.
Expanding the new formula (6), with $U'=[U\ f]$, $R'=[R\ h]$, gives

\[
 M'=M+fh^T(I-P).
\]

Compatibility yields $Ph=VY^Tf$, so
$h^T(I-P)=(h-VY^Tf)^T=E^T$. Therefore $M'=M+fE^T$, precisely
the updated conditional mean. When $p=n$, $P=I$ and the random term
in (12) vanishes. This completes the one-query proof in both directions.

## 5. Arbitrary interleaving, stopping, and completion

Let the full past sigma-field include $\xi$ and all queries and replies
up to the current global step. The induction invariant in the dense model is:
conditional on this sigma-field, the matrices in different layers are
independent, with layer $\ell$ having kernel

\[
 M_\ell+(I-Q_\ell)G_\ell(I-P_\ell),
\tag{13}
\]

where the $G_\ell$'s in this conditional representation are mutually
independent iid Gaussian matrices. At time zero, all stored lists are empty,
$M_\ell=P_\ell=Q_\ell=0$, and (13) is the assumed initialization law.

At a subsequent step, the query choice is measurable from the conditioned
past. It therefore reveals no extra information once that past is fixed.
Only the selected matrix determines the next answer. The one-query calculation
in Section 4 gives its answer law and posterior kernel. The conditional
product structure in (13) implies that all other matrix kernels are unchanged:
the joint conditional law before the answer is the product of the selected
matrix/answer law and the other matrix laws. Conditioning that product on the
answer changes only the selected factor. This proves the induction invariant.

These calculations can equivalently be read as conditional-expectation
identities for bounded measurable test functions; they do not require giving
positive probability to any particular real-valued transcript.

The sampler uses exactly the answer transition kernel just derived, at every
history. Its initial independent randomness $\xi$ has the same law as in
the dense model. Induction over the finite maximal number of queries therefore
gives equality of the complete transcript laws. Querying another layer using
an earlier reply causes no difficulty: conditional on the global past the new
query is already determined. It is the remaining matrices that are
conditionally independent; the outputs themselves need not be independent.

Stopping adds no further conditioning beyond the transcript: whether the
algorithm stops at the current step is measurable from that transcript and
$\xi$. Formally, for a bounded stopping time $T$, partition by the finitely
many events $\{T=t\}$. On each such event the fixed-time conditional identity
already proved applies, with the state at time $t$. Summing those identities
proves (13) at time $T$. Alternatively, make stopping absorbing and pad the
remaining global steps with no observations.

To construct the stated coupling, run the sampler through its stopping time,
then on an extended probability space take independent matrices
$G_\ell$, independent also of the entire sampler run, with iid
$N(0,1/n)$ entries. Define mathematically

\[
 \widehat W^{(\ell)}
 =M_\ell+(I-Q_\ell)G_\ell(I-P_\ell)
\tag{14}
\]

using the final stored states. The conditional law in (14) is exactly the
dense model's conditional law given the same stopped transcript and $\xi$.
Integrating this kernel against the identical transcript laws shows equality
of the full joint laws, including $\xi$ and all completed matrices. In
particular, their unconditional entries are jointly independent
$N(0,1/n)$, and the completed matrices are independent of $\xi$.

Equation (7) and the projected remainder imply
$\widehat W^{(\ell)}V_\ell=Y_\ell$ and
$(\widehat W^{(\ell)})^TU_\ell=R_\ell$. Every earlier forward query is
in the span of the final $V_\ell$, with its returned reply equal to the same
linear combination of stored columns of $Y_\ell$; the new independent
column is appended when that query is processed. Later appends preserve all
previous columns and relations. The transpose argument uses $U_\ell,R_\ell$.
Thus all earlier replies are simultaneously products with the single completed
matrix for their layer. This is pathwise equality on the constructed coupling,
not only a separate marginal-law assertion for each answer.

Construction (14) is not part of the online algorithm or its operation count.
Even if the algorithm later resumes querying, it can continue from the stored
quadruples with fresh Gaussian vectors: the same conditional kernel gives the
correct continuation law. One must not first realize an independent completion
and then claim that unrelated fresh sampler draws reproduce that particular
completion; pathwise agreement requires the joint coupling just established.

## 6. Cost calculation

At a local query to one layer, let $p,q$ be the old basis sizes. A length-
$n$ dot product costs at most $2n$ arithmetic operations. Therefore a
product by an $n\times p$ matrix or its transpose costs at most $2np$.
The following count assumes a new forward direction and allows all displayed
operations even when an empty or full span would permit skipping some.

| Computation | Arithmetic bound |
| --- | ---: |
| $a=V^Tv,\ v_\perp=v-Va$ | $4np+n$ |
| $\alpha=\sqrt{v_\perp^Tv_\perp}$ | $2n+1$ |
| $e=v_\perp/\alpha$ | $n$ |
| $b=R^Te$ | $2nq$ |
| $g-U(U^Tg)$ | $4nq+n$ |
| $h=Ub+\sigma\{g-U(U^Tg)\}$ after the projected vector is ready | $2nq+2n$ |
| reply $Ya+\alpha h$ | $2np+2n$ |

The sum is $6np+8nq+9n+1\leq8n(p+q)+10n$, since $n\geq1$.
A dependent forward query costs at most $6np+3n+1$, which is smaller.
The transpose bound exchanges $p$ and $q$ and has the same upper bound
$8n(p+q)+10n$. There is one zero test per query and at most one further
rank comparison. Vector copying and
bookkeeping take $O(n+p+q)$ word accesses per query, so also preserve the
stated asymptotic work bound if word accesses are charged separately.

Before the $j$-th local query, $p+q\leq j-1$. Summing gives

\[
 \sum_{j=1}^k \{8n(j-1)+10n\}
 =4nk(k-1)+10nk=4nk^2+6nk.
\]

Computing $\sigma=1/\sqrt n$ uses one square root and one division. This
proves the claimed arithmetic bound. No inverse, linear solve, Gram-matrix
eigenvalue bound, or condition-number assumption occurs in this calculation.

Every nonzero new query direction increases exactly one of $p,q$ by one.
Both remain at most $n$. Gaussian vectors are needed only until one of the
two ranks first reaches $n$; thereafter queries enlarging the other side
have deterministic new columns. Immediately before that first full rank, both
ranks are at most $n-1$, so at most $2n-1$ enlargements can draw a Gaussian
vector. If neither rank reaches $n$, there are at most $2n-2$ enlargements.
There are also at most $k$ enlargements in total. Each drawing enlargement
uses $n$ scalar draws, proving $n\min\{k,2n-1\}$.

The four stored matrices contain $2n(p+q)$ scalar words. Store their columns
as linked lists of separate vectors with $2(p+q)$ next-column addresses;
this allows append
without holding a second full copy of the state. Eight length-$n$ scratch
vectors and $3(p+q)$ coefficient words are a conservative workspace bound:
one needs only the current vector/residual, a Gaussian vector, a new answer,
an output, temporary matrix-vector storage, and the three coefficient lists
$a,b,U^Tg$ (or their transpose counterparts). Sixty-four additional scalar or
integer/address words suffice for the scale, norms, loop indices, dimensions,
and list roots in an ordinary implementation. Newly retained column vectors
are charged to the stored matrices. Thus

\[
 2n(p+q)+8n+5(p+q)+64
 \leq 2n\min\{k,2n\}+8n+5\min\{k,2n\}+64.
\]

This is a bound for the sampler state, not for arbitrary client-side storage
or for the imaginary dense matrices in the proof. When $k$ is comparable to
$n$, the bound is itself quadratic in $n$; the theorem makes no stronger
compression claim in that regime. For example, querying all $n$ standard
basis vectors forwards returns the entire matrix, and the retained $Y$ then
equals that matrix. Thus “implicit” specifies how reference randomness is
generated and queried; it cannot mean that an unrestricted oracle transcript
never reveals the whole matrix. A requirement of subquadratic storage must
also constrain the query budget, for example $k=o(n)$.

## 7. Exact scope and limitations

The construction samples a new reference matrix implicitly with the correct
joint iid law. It does not receive a previously realized concrete matrix or
the seed of a specified dense-entry generator, and it does not reproduce
products for such a supplied realization. Equality in law and the existence
of the coupling (14) do not supply that additional service. To serve a fixed
matrix or a prescribed seed-to-matrix map would require a separate input model
and algorithm; no complexity bound for it follows here.

The theorem does permit exact finite-$n$ distributional reasoning for any
algorithm using the specified oracle, including nonlinear or discontinuous
adaptive choices and data-dependent stopping within the budgets. It preserves
the forward/transpose response terms, the dependence between reused products,
and independence of the *unconditional* layer matrices. It makes no claim of
coordinate independence for reused outputs.

Exact zero tests and normalizations are part of the mathematical algorithm.
Near-dependent directions can cause finite-precision difficulties. Replacing
zero tests by tolerances or ordinary orthogonalization by an approximate
implementation requires a separate error analysis. Likewise, exact real words
and exact Gaussian draws are primitives of the stated cost model, not hidden
claims that infinitely precise numbers fit in fixed-bit machine words.

Finally, this sampler result by itself proves no stability, training-time,
width-limit, mean-field, state-evolution, or approximation theorem. Such uses
must supply their own query budgets and additional mathematical arguments.
