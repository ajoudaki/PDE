# Exact adaptive transcripts and uniform scalar laws

2026-10-06. Scoped continuation of the unseen-query decoder study.
Internal theoretical results; no experiments and no promotion.

Every finite, predictable, two-orientation Gaussian matrix program has an
exact representation by coordinate functions of independent Gaussian row
packets and a finite array of realized scalar coefficients. The coefficients
need not converge to population values for a uniform empirical law to apply.
This avoids an unnecessary independence claim after conditioning on those
coefficients. It does **not** yet give a compact autonomous decoder: acquiring
the coefficients and extending them to a late query are separate tasks.

The exact representation, a quantitative elementary uniform law, and the
conditioning cost of small retained innovations are proved below. A final
section states precisely what a sufficiently accurate online source
implementation would have to supply. No future coefficient table, dense
matrix access, or exact integration oracle is supplied by the results here.

## Scope and provenance

This file is written at the supervisor's explicit request in the current
study. It does not modify the frozen `GROWING_PROGRAM_STABILITY.md` or
`HESSIAN_RESPONSE_CLOSURE.md`. The current shared `AGENTS.md`, process skills,
and the maintained notation contract were read in the preceding scoped
continuation and remain current. The required custom canonical-notation
skill was permission-denied; the supplied presentation instructions and
`docs/notation.qmd` continue to apply.

Scientific inputs are the completely read current-study
`POPULATION_DECODER.md`, the explicitly authorized and completely read
`integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md` and
`GENERAL_TRAJECTORY_LOWER_BRIDGE.md`, and the relevant complete sections of
`docs/02-gaussian-reuse.qmd` recorded in the first frozen note. Section 5.4
of the maintained book was reread for this derivation. Its conditional
matrix identity is reproved in the needed form here. No other study or
external specialized theorem is imported. The supervisor's proposed finite
causal time discretization and augmented compact source implementation are
research directions, not assumed theorems in this file.

The original contract remains the nonlinear trained network, the original
fixed label/gap allowance, a query supplied only after training, the whole
sphere, the whole physical trajectory and endpoint, and an absolute
polylogarithmic bound on retained state **and peak decoding workspace**.
The results here concern finite causal transcripts inside a possible proof
of that contract, not a substitute target.

## 1. Finite causal programs

Let \(M_1,\ldots,M_b\) be independent standard Gaussian

\[
 M_\ell\in\mathbb R^{n\times n},\qquad W_\ell=M_\ell/\sqrt n.
                                                               \tag{1}
\]

Here \(b\) is fixed; \(b=L-1\) for the initialized hidden mixers. The
program makes at most \(R\) calls of the forms \(W_\ell q\) and

\[
 W_\ell^Tc.                                                    \tag{2}
\]

The matrix label, orientation, and vector argument of the next call are
measurable with respect to an external initial sigma-field and all earlier
calls. The external field is independent of the matrices. Between calls,
the program may apply prescribed coordinatewise maps and form scalar
reductions. Its initial vector fields are coordinate functions of packets

\[
 \xi_i,\qquad 1\le i\le n,                                    \tag{3}
\]

which are independent and identically distributed, independent of the
matrices. Deterministic coordinate marks \(t_i\) are also allowed. For
example, the \(d\) Gaussian entries of an initial input-layer row belong
to \(\xi_i\). A deterministic vector with unequal entries is encoded in
the marks, not incorrectly declared identically distributed.

The finite row-evaluation schema contains \(S\) arithmetic or prescribed
scalar-function nodes. Scalar reductions and their scalar transforms
contribute \(P_0\) scalar values to the transcript. These counts are
explicit inputs. No bound depending only on the number of matrix calls is
claimed for a program allowed to insert arbitrarily many scalar reductions.

## 2. Exact conditioning in both orientations

For one fixed matrix, collect the previous forward queries and their
answers, and the previous reverse queries and their answers, as

\[
 V=[q_1\ \cdots\ q_r],\quad Y=WV,\qquad
 U=[c_1\ \cdots\ c_s],\quad D=W^TU.                            \tag{4}
\]

Only calls made before the current one are included. Set

\[
 Q=V^TV/n,\quad K=U^TU/n,\quad
 H=U^TY/n=D^TV/n.                                              \tag{5}
\]

Empty blocks are omitted, and every inverse below means the
Moore--Penrose inverse when needed. Write \(P_V=VQ^\dagger V^T/n\)
and \(P_U=UK^\dagger U^T/n\). These are orthogonal projectors even
when columns are dependent.

### 2.1 Conditional matrix remainder

Conditionally on the entire revealed past,

\[
 M=P_UM+MP_V-P_UMP_V+P_U^\perp\widetilde M P_V^\perp,           \tag{6}
\]

where \(\widetilde M\) is a fresh standard Gaussian matrix. Across
matrix labels the residual matrices are conditionally independent.

For completeness, suppose (6) holds before a forward call. Decompose its
argument as \(q_*=P_Vq_*+q_\perp\). If \(q_\perp\ne0\), put

\[
 e=q_\perp/\|q_\perp\|_2.
\]

Given the past, \(e\) is deterministic, and
\(\widetilde M ee^T\) and \(\widetilde M(I-ee^T)\) are independent
Gaussian projections. The answer reveals only
\(P_U^\perp\widetilde M e\). Its unobserved \(P_U\)-component is
irrelevant to the old residual, and the residual acting on
\(\operatorname{span}(V,q_*)^\perp\) remains fresh. If
\(q_\perp=0\), nothing is revealed. The transpose case exchanges
left and right projections. This proves (6) inductively under arbitrary
predictable interlacing of all matrix labels. Adaptation through other
matrices does not alter this argument.

### 2.2 New forward call

For \(q_*\), define

\[
 q=V^Tq_*/n,\qquad v=D^Tq_*/n,\qquad
 \tau_q^2=\|q_*\|_2^2/n-q^TQ^\dagger q.                       \tag{7}
\]

Then, on a common extension of the probability space,

\[
 Wq_*=YQ^\dagger q+
       UK^\dagger(v-HQ^\dagger q)+\tau_qP_U^\perp g,            \tag{8}
\]

where \(g\) is conditionally \(N(0,I_n)\), independent of the
past. Indeed, the known forward projection contributes \(YQ^\dagger q\);
the projection of the remaining answer onto \(\operatorname{span}(U)\)
is fixed by \(U^TWq_*=D^Tq_*\). The remaining covariance from (6) is
\(\tau_q^2P_U^\perp\).

The exact coordinate form is especially useful. With

\[
 \alpha=Q^\dagger q,\quad t=U^Tg/n,\quad
 \beta=K^\dagger(v-H\alpha-\tau_qt),
\]

equation (8) becomes

\[
 (Wq_*)_i=\sum_{a=1}^rY_{ia}\alpha_a+
           \sum_{a=1}^sU_{ia}\beta_a+\tau_qg_i.                \tag{9}
\]

The coefficients in (9) are shared across row indices. In particular,
the projection of the fresh Gaussian is not silently thrown away: its
coefficient \(-\tau_qK^\dagger t\) is retained.

### 2.3 New reverse call

For a reverse argument \(c_*\), define

\[
 k=U^Tc_*/n,\quad \omega=Y^Tc_*/n,\quad
 \tau_c^2=\|c_*\|_2^2/n-k^TK^\dagger k.                       \tag{10}
\]

The transposed identity is

\[
 W^Tc_*=DK^\dagger k+
         VQ^\dagger(\omega-H^TK^\dagger k)
            +\tau_cP_V^\perp g.                               \tag{11}
\]

Equivalently, with

\[
 \widetilde\alpha=K^\dagger k,\quad
 \widetilde t=V^Tg/n,\quad
 \widetilde\beta=Q^\dagger
   (\omega-H^T\widetilde\alpha-\tau_c\widetilde t),
\]

we have

\[
 (W^Tc_*)_i=\sum_{a=1}^sD_{ia}\widetilde\alpha_a+
            \sum_{a=1}^rV_{ia}\widetilde\beta_a+\tau_cg_i.
                                                               \tag{12}
\]

Using only (9) and ignoring (12) would erase precisely the reverse
responses at issue in the nonlinear decoder problem.

### 2.4 Independent full innovations, including a coupling to the original matrices

The projected innovation in (8) can be completed without changing the
original action. If \(\tau_q>0\), let \(\eta\) denote the original
answer minus its conditional mean in (8), and take an additional
independent \(\zeta\sim N(0,I_n)\). Define

\[
 g=\eta/\tau_q+P_U\zeta.                                     \tag{13}
\]

Given the past, the first term has covariance \(P_U^\perp\), the
second has covariance \(P_U\), and they are independent. Consequently
\(g\mid\text{past}\sim N(0,I_n)\), and \(P_U^\perp g=\eta/\tau_q\).
If \(\tau_q=0\), an entirely fresh unused \(g\) may be inserted.
For a reverse call replace \(P_U\) by \(P_V\).

Including previous completion variables in the past preserves (6): they
reveal only independent auxiliary Gaussian variables beyond the actual
matrix answers. Iterating conditional independence shows that all full
innovations \(g_1,\ldots,g_R\) are jointly independent standard Gaussian
vectors and independent of the initial packets. Therefore

\[
 Z_i=(\xi_i,g_{1,i},\ldots,g_{R,i}),\qquad 1\le i\le n,          \tag{14}
\]

are independent and identically distributed row packets. This is an
unconditional statement. The \(Z_i\) are generally **not** independent
after conditioning on all realized coefficients.

## 3. Exact row representation

**Finite-transcript proposition.** Under Section 1, there is a scalar
array \(c\) of length

\[
 P\le P_0+C R^2                                                \tag{15}
\]

and fixed coordinate functions \(F_a\), one for each named vector node,
such that the entire original transcript is represented exactly by

\[
 X_{a,i}=F_a(t_i,Z_i;c).                                       \tag{16}
\]

Here \(c\) contains the scalar reductions, and the realized action
coefficients in (9) and (12). It is allowed to be an arbitrary function
of the complete row array. A finite set of possible call schemas may be
handled by also recording the realized schema. For a fixed schema the
functions \(F_a\) are deterministic.

**Proof.** Initial nodes have the prescribed form. A coordinatewise map
or scalar-coefficient arithmetic operation preserves the form. At a
matrix call use (9) or (12), append its at most \(R+1\) scalar
coefficients and one fresh component of \(Z_i\), and apply induction.
There are at most \(R\) such calls, giving (15). Equations (6)--(13)
provide a joint realization with the original matrices, rather than
merely a sequence of unmatched marginal laws. \(\square\)

The proposition is independent of a population limit and has no
smallest-eigenvalue hypothesis. Without quantitative control on the
coefficient range and coordinate functions, however, it is only an exact
representation theorem. It does not by itself imply a useful empirical
law or an implementation with small memory.

## 4. Uniform laws allow fully adaptive realized coefficients

Let \(Z_1,\ldots,Z_n\) be independent packets as in (14). Let

\[
 f_j(t,z;c),\quad 1\le j\le J,\quad c\in[-A,A]^P,
                                                               \tag{17}
\]

be deterministic functions. Assume \(A,L\ge1\), and uniformly in
the marks, packets, indices, and coefficients,

\[
 |f_j(t,z;c)|\le B,\qquad
 |f_j(t,z;c)-f_j(t,z;c')|\le L\|c-c'\|_\infty.                 \tag{18}
\]

Define the deterministic moment functional

\[
 \mu_j(c)=\frac1n\sum_{i=1}^n
             \mathbb E f_j(t_i,Z;c),                          \tag{19}
\]

where \(Z\) is an independent packet with the common law. The marks
need not have any limiting empirical distribution.

**Uniform-law proposition.** For \(0<\delta<1\), with probability
at least \(1-\delta\), simultaneously for every \(c\in[-A,A]^P\)
and \(1\le j\le J\),

\[
 \left|\frac1n\sum_i f_j(t_i,Z_i;c)-\mu_j(c)\right|
 \le \frac2n+
 B\sqrt{\frac2n\left[
     P\log(2+2ALn)+\log\frac{2J}{\delta}\right]}.
                                                               \tag{20}
\]

**Proof.** Cover the coefficient box in sup norm by a grid of mesh
\((Ln)^{-1}\). Its cardinality is at most
\((2+2ALn)^P\). For a fixed grid point and \(j\), the summands are
independent, even with unequal marks. For centered variables in an
interval of length \(2B\), convexity of the exponential gives
\(\mathbb E e^{\theta(X-\mathbb EX)}\le e^{\theta^2B^2/2}\).
Multiplication of these bounds and optimization in \(\theta\) give

\[
 \mathbb P\left\{\left|\frac1n\sum_iX_i-
          \frac1n\sum_i\mathbb EX_i\right|>u\right\}
       \le2e^{-nu^2/(2B^2)}.
\]

A union bound gives the square-root term in (20) at every grid point.
Moving to a nearest point changes each empirical and expected average
by at most \(1/n\), proving (20). \(\square\)

For clarity, the elementary exponential bound used here follows by
rescaling to \(X\in[0,1]\): convexity first bounds the exponential
moment by that of a Bernoulli variable with mean \(\mathbb EX\).
The second derivative of its centered log moment generating function is
a Bernoulli variance, at most \(1/4\). Its value and first derivative
vanish at zero, yielding the bound after two integrations.

Taking \(c=c(Z_1,\ldots,Z_n)\) in this one simultaneous event is
valid. There is no conditional-iid assertion and no union bound over
possible values of the random coefficient array. If a finite family of
schemas is needed, its cardinality multiplies \(J\) in (20).

In particular, if

\[
 P+\log A+\log L+B+\log J=\operatorname{polylog}(n),            \tag{21}
\]

then (20) has root-\(n\) error times an absolute polylogarithm, at
any fixed polynomially small failure probability. The exponent is the
one supplied by the actual counts, not an assertion that it is five.
An additional factor \(e^{C\sqrt{\log n}}\) in \(B\) is likewise
compatible with the target scale.

### 4.1 Clipping is part of the theorem, not an omitted tail argument

The exact row functions in (16) are not automatically bounded or
globally Lipschitz in their coefficients. One valid application of (20)
has the following explicit steps.

1. Restrict the realized coefficients to a deterministic box on a proved
   good event.
2. Clip independent Gaussian components at
   \(T=\sqrt{2\log(2nR/\delta_0)}\). For the \(nR\) newly added
   Gaussian entries, the union bound shows that this changes none of
   them except with probability at most \(\delta_0\). Initial Gaussian
   packets add their own finite number of components to this count.
   For other initial packet laws, a separate tail bound is required.
3. Insert deterministic clips into intermediate row nodes, large enough
   to leave the realized good transcript unchanged. This makes the
   coefficient-indexed class well defined even at inconsistent or
   nonphysical coefficient arrays.
4. Clip each final moment integrand to the value \(B\) actually proved
   sufficient for the desired event. A product of two bounded fields
   needs the product bound; its bound is not that of either factor.

For a finite arithmetic row graph with \(S\) nodes, coefficient bound
\(A\), intermediate amplitude bound \(H\), and primitive scalar
Lipschitz constants at most \(D\), elementary induction bounds its
coefficient Lipschitz constant by

\[
 L\le [C S(1+A+H+D)]^{C S}.                                   \tag{22}
\]

For example, subtraction adds the two previous Lipschitz constants;
multiplication of two \(H\)-bounded nodes multiplies their sum by
\(H\); multiplication by a coefficient bounded by \(A\) adds a
term at most \(H\) and multiplies the old constant by \(A\);
and a prescribed scalar map multiplies it by \(D\). Clipping is
one-Lipschitz. Applying these rules successively proves (22), with a
larger absolute constant if multi-input sums are individual nodes.

Matrix inverses, square roots of empirical variances, and small
denominators need not occur inside this row graph: their already
realized values are coefficient slots. Thus their lack of a global
coefficient derivative is not silently ignored in (22).

If \(S\), \(\log A\), \(\log H\), and \(\log D\) are
polylogarithmic, so is \(\log L\). However, (20) depends on the
final amplitude \(B\), not only its logarithm. An exponentially large
intermediate clipping radius is harmless for the covering-number log;
an exponentially large final moment bound generally is not. In
particular, a normalized nearly dependent history direction can have
coordinates as large as \(\sqrt n\). Its required moment class must
be checked separately; it cannot be declared polylogarithmically
bounded from its RMS normalization alone.

## 5. Tiny retained pivots: entropy is easier than stability

For this section retain linearly independent history columns only.
Suppose each retained forward column satisfies
\(\|v_j\|_2/\sqrt n\le B_0\), and its RMS distance from the span
of earlier retained columns is at least \(\tau>0\). Take a thin QR
factorization

\[
 V/\sqrt n=ET,
 \quad E^TE=I_r,\quad T\text{ upper triangular}.
\]

The diagonal entries of \(T\) are at least \(\tau\), and all its
entries have absolute value at most \(B_0\). Write \(T=D_0(I+N_0)\)
with \(N_0\) strictly upper triangular. Then
\(\|N_0\|_{\rm op}\le rB_0/\tau\), and nilpotence gives

\[
 T^{-1}=\left[\sum_{k=0}^{r-1}(-N_0)^k\right]D_0^{-1}.
\]

Consequently

\[
 \|T^{-1}\|_{\rm op}
 \le \frac r\tau\max\{1,rB_0/\tau\}^{r-1},\qquad
 \|Q^{-1}\|_{\rm op}\le
 \frac{r^2}{\tau^2}\max\{1,rB_0/\tau\}^{2r-2}.                \tag{23}
\]

The identical bound applies to reverse histories. This is deliberately
crude but has the useful logarithmic size

\[
 \log(1+\|Q^{-1}\|+\|K^{-1}\|)
 \le C R\,[1+\log(R+1)+\log(B_0+1)+\log(1/\tau)].              \tag{24}
\]

Assume also that all mixer operator norms are at most \(K_0\), all
queries have RMS at most \(B_0\), and fresh innovations have RMS at
most \(G_0\). Each action then has RMS at most \(K_0B_0\). Every
entry of the ordinary Gram and cross-Gram vectors in (7)--(12) is
bounded by a product of these RMS bounds. Equations (9), (12), and
(23) therefore imply a deterministic box bound on every action
coefficient with

\[
 \log A\le C R\,[1+\log(R+1)+\log(B_0+K_0+G_0+1)
                              +\log(1/\tau)].                 \tag{25}
\]

Thus choosing \(R=\operatorname{polylog}(n)\) and
\(\tau=\exp[-\operatorname{polylog}(n)]\) is consistent with the
entropy requirement \(\log A=\operatorname{polylog}(n)\).
This statement does **not** say that perturbing input moments by
root-\(n\) is stable under those inverses.

### 5.1 Discarding a tiny new direction changes the program

For an actual argument \(q_*\), if
\(\|P_V^\perp q_*\|_2/\sqrt n\le\tau\), then

\[
 \|Wq_*-WP_Vq_*\|_2/\sqrt n\le\|W\|_{\rm op}\tau.           \tag{26}
\]

Replacing this action by the known linear combination of old forward
answers has the stated one-call error. It is not an exact Gaussian
reveal of the unprojected argument. A modified program must record only
the projected argument as the argument whose action was revealed;
discarded residual actions may not be used for later conditioning.
The same rule applies in reverse. Propagation of (26) through the full
physical approximation is an additional estimate.

There need not be a gap between an actual pivot and a chosen threshold.
An approximate implementation can avoid assuming such a gap by using
a buffer: if its error in squared residual norm is at most
\(\tau^2/4\), retain only when its estimate exceeds \(2\tau^2\).
Every retained direction then has true residual norm at least
\(\sqrt{7/4}\tau\), and every discarded one has true residual norm
at most \(3\tau/2\). This supplies conditioning or a controlled
discard error in either case. It does not claim that an exact and an
approximate algorithm follow the same retention schema.

## 6. A conditional online scalar-update lemma

The distinction between representation and implementation can be made
quantitative. Suppose a fixed retained schema with at most \(R\) calls
is processed in causal order. At a forward call, the genuinely new
scalar inputs required by (7)--(9) are

\[
 V^Tq_*/n,\quad D^Tq_*/n,\quad \|q_*\|_2^2/n,
 \quad U^Tg/n,                                                \tag{27}
\]

in addition to stored old Grams and coefficients. The reverse list
exchanges \(V,Y\) with \(U,D\) as in (10)--(12). Updating the old
Gram tables needs finitely many further pairings of the new query and
answer with old columns, again at most \(C R\) scalars per call.

If all values in these lists are supplied with absolute error at most
\(\varepsilon\), all exact retained innovation norms are at least
\(\tau\), and all exact Gram inverses are at most \(A_0\), then
the action-coefficient update is locally Lipschitz, with a constant
bounded by a fixed polynomial in

\[
 R,\quad B_0+K_0+G_0+1,\quad A_0,\quad 1/\tau.                \tag{28}
\]

Here local means that the errors are small enough to keep the
perturbed Gram eigenvalues above half their original smallest positive
eigenvalue and the perturbed squared innovation above \(\tau^2/2\).
This qualification is verified, rather than assumed, by taking
\(\varepsilon\) sufficiently small relative to the displayed bounds.

To prove the claim, for a positive Gram \(Q\) and perturbation \(E\)
with \(\|Q^{-1}\|\|E\|\le1/2\), the resolvent identity gives

\[
 \|(Q+E)^{-1}-Q^{-1}\|
 \le2\|Q^{-1}\|^2\|E\|.                                    \tag{29}
\]

Entrywise scalar errors imply an operator error at most \(R\) times
their maximum. Products and sums in (7)--(12) have polynomial
Lipschitz bounds in the bounded factors. Finally, for \(x,y\ge
\tau^2/2\),

\[
 |\sqrt x-\sqrt y|\le |x-y|/(\sqrt2\tau).                    \tag{30}
\]

Combining (29)--(30) proves (28). The number of factors and sums in one
call is polynomial in \(R\), so no unmentioned dependence on \(n\)
appears.

More generally, suppose the supplied moment update at each call is
itself Lipschitz in all previously retained scalar state, with
constant at most \(L_0\), and has an additional error at most
\(\varepsilon\). Induction through \(R\) calls bounds the final
state error by

\[
 \varepsilon R(1+L_*)^R,                                    \tag{31}
\]

where \(L_*\) is a fixed polynomial in (28) and \(L_0\). One first
chooses \(\varepsilon\) so that this bound stays within the local
neighborhood required above; then the same induction justifies its
use at every step. If

\[
 R+\log A_0+\log L_0+\log(1/\tau)
       +\log(B_0+K_0+G_0+1)=\operatorname{polylog}(n),            \tag{32}
\]

the amplification in (31) is \(\exp[\operatorname{polylog}(n)]\).
Source accuracy \(\varepsilon=\exp[-\log(n)^C]\), for a sufficiently
large fixed \(C\), can absorb this factor and any prescribed inverse
polynomial target. This is the reason that allowing a larger absolute
memory exponent can help a high-accuracy source implementation.

Crucially, (31) requires actual high-accuracy moment inputs, or a proved
high-accuracy source model providing them. Substituting the root-\(n\)
uniform law (20) for those inputs does not satisfy this requirement:
an exponentially ill-conditioned inverse can amplify that error.
Nor does the exact row representation provide the assumed \(L_0\)
for a closed, autonomous moment update by itself.

## 7. What is and is not an autonomous compressed past

The following items are compatible with compressed past summaries.

* After processing each causal call, retain its realized scalar
  coefficients and update the Gram tables. There are \(O(P_0+R^2)\)
  scalars and at most \(O(S)\) finite row instructions. This records
  the past; it is not a table of future coefficient values.
* A coordinate evaluator can replay its **finite row instruction
  graph** for one innovation packet using \(O(S+P)\) workspace, or
  less by recomputation. It does not retain the \(n\) physical rows.
* Finite quadrature over the \(O(R)\)-dimensional packet can be streamed
  one quadrature point at a time, with workspace polynomial in the
  packet dimension and instruction count. A valid decoder must specify
  its quadrature and error control. Equation (19) is a mathematical
  expectation, not a free exact-integration operation.

The following steps do not follow from those observations.

**Acquiring the next coefficient.** Once the \(n\) original row
packets have been discarded, evaluating a row function at a newly
generated packet does not recover its original empirical averages in
(27). Keeping only past coefficient values does not supply those new
averages. A compact source dynamics must genuinely compute or
approximate them; its existence cannot be inferred from (16).

**Completing and representing innovations.** Formula (13) is an exact
probabilistic construction. To implement it from a compact source,
one must approximate the actual initialized action, subtract its
known conditional mean, divide by the retained innovation norm, and
add the projected independent probe. A proposed augmentation by
innovation/action source pairs must include these operations and
the probe storage in its own autonomous construction. The factor
\(1/\tau\) belongs in its accuracy budget. Dense access needed to
evaluate (13) is not licensed by the representation theorem.

**Filtration preservation.** A source compiler might inspect more
initialized-matrix information than the base causal program. Its
approximate coefficients must not then be inserted into the conditioning
sigma-field while claiming the original residual law (6). One legitimate
proof pattern is to analyze the exact causal transcript and its exact
coefficients first, and afterward compare the decoder using approximate
coefficients on a separate deterministic accuracy event. A different
pattern needs a new conditional-law proof for its enlarged information.

**Late-query coefficients.** A training transcript does not contain
the empirical cross-moments of an unseen nonlinear query with all old
queries and answers. Appending that query in (8) is exact but requires
new values in (7). Replacing them by the expectations (19) invokes a
root-\(n\) error before the history inverse. Equations (24)--(25)
control the logarithm of the inverse for entropy purposes, not this
perturbation. An output-energy estimate, a direct weak passive-query
argument, or a separate high-accuracy query-source implementation is
still required. The old full forward/backward physical history is not
an allowed way to obtain it.

**All queries at once.** For every fixed appended query, Sections 2--4
give an exact coupling and its uniform coefficient event. Different
queries have a correlated residual Gaussian process; their fresh
innovation arrays cannot simply be declared identical. A proof-only
sphere net can use individual-query probability bounds, provided an
actual decoder modulus in the input is also proved. If that modulus
is \(\exp[\operatorname{polylog}(n)]\) and \(d\) is fixed, the
logarithm of the net cardinality remains polylogarithmic and is
compatible with (20). Discontinuous retention rules require separate
control. The proof net must not be appended as a stored query panel.

**No compact iid-root seed has been established.** The exact packets
in (14) contain \(nR\) independent Gaussian entries. Storing them is
not polylogarithmic. Replacing them by a short pseudorandom seed or
limited-independence construction changes the initialization/coupling
law and needs its own proof. Encoding the full array in the digits of
one real number is outside the finite-information contract.

The concrete advance is therefore an exact adaptive representation
plus a uniform law that tolerates data-dependent coefficients, and an
explicit high-accuracy budget for causal scalar updates. The remaining
decoder obligations are autonomous source acquisition, stability of
the passive late-query scalar law, and an all-query/all-time counted
evaluation. None is asserted solved by this note.
