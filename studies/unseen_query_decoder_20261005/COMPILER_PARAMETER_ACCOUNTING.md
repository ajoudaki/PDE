# Parameter accounting for the physical-program compiler

2026-10-06. Scoped author audit of the existing unseen-query construction.
The initial input scope for Sections 1--7 was `QUADRATIC_RESOURCE_RESULT.md`,
`EXPLICIT_COMPILER_EXPONENT.md`, `QUADRATIC_INITIALIZATION.md`,
`RECALIBRATION_FREE_MOMENTS.md`, and `SHORT_SEED_PRIOR_BLOCKS.md`.
All five were read completely. No other study, maintained scientific source,
prior review, experiment, or Git operation was used. After that audit was
written, the supervisor explicitly authorized the complete additional input
`PHYSICAL_PARAMETER_ACCOUNTING.md` for the numerical-certificate closure in
Section 8; that file was then read completely. This note is an internal
derivation under their physical and numerical interfaces, not an independent
review of those interfaces or a promotion.

The downstream construction admits an explicit polynomial accounting in the
physical program size, input dimension, and logarithmic numerical
certificates. The counted polynomial is large. The existing construction
does not supply a fourth-degree parameter bound. In particular, the literal
dense cofactor matrix implementation already performs more than fourth-degree
work in the physical program size. This is an implementation limitation, not
a lower bound for every possible decoder.

The useful output is the unsubstituted resource formulas below. They retain
every parameter factor instead of moving it into a sufficiently-large-width
condition. Converting them into bounds in training-set size, the initial
Gram gap, labels, and activation parameters requires the separate physical
program and conditioning certificates specified in Section 7.

## 1. Counts, precision, and finite inputs

Use the source notation: \(n\) is dense width, \(d\) is input dimension,
and \(D\) is Gaussian **packet** dimension. These are different quantities.
Let \(R\ge2\) bound the actual number of physical fields, matrix calls,
field evaluations, training examples, and layers. This is a counted size,
not a symbol that may be multiplied by an unreported problem-dependent
constant. Let \(P\) be the actual number of retained scalar summaries,
\(Q\) the number of vector/scalar moment calls in one query, and \(r_h\)
the maximum number of history marks in a vector moment. Work on the
nontrivial branch with \(P,Q\ge1\); the zero-predictor branch is separate.
The schedules in the
assigned sources give, with absolute numerical constants,

\[
 P\le cR^2,\qquad D\le d+cR,\qquad
 Q\le cR^2,\qquad r_h\le cR.
 \tag{1}
\]

The constants in (1) mean fixed instruction-template overheads; physical
parameters must already be represented by actual counts or certificates.
If a different program does not meet (1), use its actual \(P,D,Q,r_h\) in
the formulas instead.

Let \(N\) count the shared scalar/coefficient graph instructions and let
\(r_m\) bound the dimension of a numerical matrix macro. The compiler's
explicit schedule, including its deliberately padded matrix products, gives

\[
 N\le c(R^7+Rd),\qquad r_m\le cR^2.
 \tag{2}
\]

The extra \(Rd\) expands first-layer input contractions which were
fixed-dimensional in the original accounting. Each of at most \(cR\)
such evaluations contracts at most \(d\) coordinates. A one-time training
input Gram calculation, if used, costs an additional
\(O(m^2d)\) scalar operations, where \(m\le R\). It is not a hidden
constant in (2). Literal fixed-data values must also be encoded and counted.
The query whitening extension uses at most \(cR^4\) added instructions
and therefore fits (2).

Supply a finite numerical certificate consisting of:

- a bound \(U\ge2\) on the magnitudes/norms of all exact operands of
  the capped source and query graphs, including fixed numerical literals;
- a floor \(a\in(0,1]\) for every mathematical gapped inverse or root,
  and every positive scalar denominator used by projections;
- bounds on primitive Lipschitz constants on their permitted argument boxes;
- a certified Gaussian coordinate cap \(G_{\max}\), context-coordinate
  ranges, the matrix-noise level \(\sigma\), and the buffered-Gram ridge
  \(\tau\).

An ungapped positive-part macro is nonexpansive; its internally introduced
numerical gap is charged to requested precision rather than assumed here.
Define the logarithmic certificate size

\[
 \chi=2+\lceil\log_2 U\rceil+\lceil\log_2 a^{-1}\rceil
       +\lceil\log_2(1+L_{\rm prim})\rceil
       +\lceil\log_2(N+r_m+D+2)\rceil.
 \tag{3}
\]

Enlarge \(U\) to cover context ranges and the fixed normalization factors.
Here \(L_{\rm prim}\) bounds the Lipschitz constants of the activation,
derivative, and other supplied scalar primitives actually used. Norm
conversions, multiplication, inversion, square roots, PSD projections, and
the primitive interfaces then have a common local Lipschitz bound \(L_0\)
with \(\log_2(1+L_0)\le c\chi\). For example, inverse and root
differences have factors at most \(a^{-2}\) and \((2\sqrt a)^{-1}\)
in Frobenius norm; entry/Frobenius conversions cost at most \(r_m\).
An inverse square root has factor at most \(a^{-3/2}/2\), also covered.

Topological induction through the cached graph gives

\[
 \log_2(1+\Lambda)\le cN\chi,\qquad
 \log_2\operatorname{Lip}_{\rm seq}\le cPN\chi.
 \tag{4}
\]

The first is row sensitivity at a fixed numerical history. The second is
the full capped sequential moment recursion. They are bounds for exact
mathematical circuits, not continuity claims for rounded medians or branch
decisions.

If a row output requires \(p\) bits of absolute accuracy and its ordinary
inputs have at most \(p\) bits after accounting for integer parts, put

\[
 H(p)=2+p+cN\chi.
 \tag{5}
\]

Use local arithmetic precision \(cH(p)\). The explicit rational matrix
implementation in `EXPLICIT_COMPILER_EXPONENT.md`, Sections 5--6, yields

\[
 \begin{split}
 T_{\rm row}(p)&\le cH(p)^{16}
   +cN\,T_{\rm prim}(cH(p),\chi),\\
 S_{\rm row}(p)&\le cH(p)^6
   +S_{\rm prim}(cH(p),\chi).
 \end{split}
 \tag{6}
\]

The constants in (6) are absolute once the displayed certificate and
interfaces have been supplied. In particular, \(d\), conditioning, and
primitive evaluation costs are not absorbed into them. The argument for
(6) counts matrix dimension \(r_m\), minor bit lengths, exact rational
arithmetic, Newton iteration, and precision resets. Since \(N\) bounds
\(r_m,D\), their numerical-size terms fit \(H(p)\).

The primitive functions are cost interfaces, not unreported constants:
one may write
\(T_{\rm prim}(w,\chi)=T_{\rm act}(w,\chi;B_{\rm eval})
+T_{\rm data}(w;B_{\rm data})\), and likewise for space. Here
\(B_{\rm eval}\) is the finite activation-evaluator description length
and \(B_{\rm data}\) the data encoding length. Taking their sum safely
bounds each primitive call even when a call uses only one interface.
Data precision access includes rational division or other work needed to
produce the requested literals; reading an input encoding alone does not
produce their rounded values for free.

Let \(B_{\rm in}\) be the bit length of the finite problem input and
certificate descriptions. Read and encode them at charged cost. If their
construction takes work \(T_{\rm cert}\), that work is additional.
For safe accounting, add \(B_{\rm in}\) to retained and peak memory when
those inputs remain available to the decoder. Replacing them by rounded
graph literals is possible only after their rounding tolerance is certified;
it removes their retained originals but not their input acquisition cost.
All formulas below display the nonprimitive algorithmic part; primitive
work and workspace are added using (6).
For a query input, separately charge \(T_x(p_{\rm ctx})\) and
\(S_x(p_{\rm ctx})\) to obtain its coordinate words to the required
precision. A finite rational query can use its actual encoding; a real
query needs a stated precision-access interface. The input rounding must
have a proved error at most the chosen mesh, not an uncomputable exact
comparison with a real grid boundary.

## 2. Precision choices without parameter-dependent asymptotic absorption

Here is a direct way to supply the whitening and precision requirements.
Let \(A_0\) bound the raw mean coefficient operator, let \(q_0\) bound
the raw empirical history-Gram norms, let \(B\ge1\) bound the capped
passive features, and let \(\Gamma\ge1\) bound propagation from local
mean/variance errors to the final prediction. For a desired deterministic
numerical allowance \(\epsilon\in(0,1)\), a sufficient ridge choice is

\[
 \tau\le\min\left\{1,
  \frac{\epsilon^2}{100\Gamma^2 A_0^2(q_0+3)},
  \frac{\epsilon\sigma^2}{12\Gamma B^2}\right\}.
 \tag{7}
\]

If \(A_0=0\), omit the second constraint. The buffered-Gram perturbation
is at most \(3\tau\). Thus the mean change is bounded by
\(2A_0\sqrt{3\tau(q_0+3\tau)}\), and the variance change by
\(3\tau B^2/\sigma^2\). Substitution into (7), followed by multiplication
by \(\Gamma\), makes their sum smaller than \(\epsilon\). This avoids
the source addendum's use of a fixed-depth factor being eventually less
than \(\overline X\). The certificate (3) must include the resulting
floor and operand bounds after whitening.

The propagation factor may itself be computed from the nonnegative
two-coordinate recurrence (27) in `RECALIBRATION_FREE_MOMENTS.md`, by
products and sums of its explicit \(2\)-by-\(2\) matrices and the
readout norm. Its full value belongs in an error bound. Its logarithm
belongs in precision accounting. No fixed-depth polynomial is discarded
by increasing \(n\).

Allocate entropy and scalar-noise failure shares \(\alpha,\beta>0\),
and use a fixed conditional probability share \(\rho\in(0,1)\). Put
\(T_\rho=\sqrt{P/(\beta\rho)}\), and let \(T_E\) be the certified
bound on the source scalar-noise marks used in its coupling. Direct
sufficient choices are

\[
 \begin{split}
 \eta&\le\min\left\{
   \frac{\epsilon}{T_E P(1+\Lambda)^{2P+2}},
   \frac{\tau}{16r_hT_\rho}\right\},\\
 \epsilon_{\rm hist}&\le\min\left\{
   \frac{\epsilon}{(1+\Lambda)^{P+1}},
   \frac{\tau}{16r_h(1+L_{\rm pair})}\right\}.
 \end{split}
 \tag{8}
\]

Use a harmless constant in place of \(r_h\) if the history is empty.
Here \(L_{\rm pair}\) is the actual pair-test sensitivity and satisfies
\(\log_2(1+L_{\rm pair})\le cN\chi\). Equation (8) implies the
source coupling and the common-Gram condition
\(r_h[\eta T_\rho+(1+L_{\rm pair})\epsilon_{\rm hist}]\le\tau/8\).
Allocate the remaining \(\tau/8\) or more to numerical matrix error.
The extra factor \((1+\Lambda)^{P+1}\) also allows the complete
subsequent exact query-moment recursion; it does not assume that its
sensitivity equals that of a single row. The cap certificate includes
\(T_E\) and the scalar-noise magnitude bounds used here.

The source/compact-prefix quantization recurrence is

\[
 e_P\le P(1+\Lambda)^P(\Lambda+c_E+1)\kappa,
 \tag{9}
\]

where \(c_E\) bounds the finite scalar-noise and final-rounding factors.
Thus source precision can be selected by the explicit inequality

\[
 p_a\ge\log_2\frac{1}{\epsilon_{\rm hist}}
       +P\log_2(1+\Lambda)
       +\log_2[P(\Lambda+c_E+1)]+\text{integer/coupling bits}.
 \tag{10}
\]

The final term includes \(\log(nD+P)\), the source sampling failure
inverse, amplitude bits, and finite Gaussian-mark precision. It is a
logarithmic term, not a suppressed parameter-dependent constant. With all
shares at fixed fractions of \(\delta\), and the scalar-noise and root
caps included in the certificate, (7)--(10) permit

\[
 p_a\le c\left[PN\chi+\log(n+2)+\log\delta^{-1}
                         +\log\epsilon^{-1}+\chi\right].
 \tag{11}
\]

An analogous choice of context precision satisfies

\[
 p_{\rm ctx}\le c\left[PN\chi+\log\epsilon^{-1}+\chi\right].
 \tag{12}
\]

Choose the constants large enough for the specified accuracy. A
one-half-Hölder variance coordinate doubles the necessary precision, which
does not change these degrees. Bounds (11)--(12) mean that the displayed
right sides are sufficient choices; they are not assertions that an
arbitrarily chosen larger precision must obey the upper bounds.

## 3. Initialization, exact weights, and compact updates

Put \(H_a=H(p_a)\) and

\[
 v_a=p_a+\lceil\log_2(n+1)\rceil
               +\lceil\log_2(P+2)\rceil+2.
 \tag{13}
\]

The streaming selection lemma uses at most \(q\le P+1\) selected
packets. Its weight numerators and denominators have at most
\(c(P+1)v_a\) bits. Its certified selection work and workspace are

\[
 c n(P+2)^8v_a^3,\qquad c(P+2)^3v_a.
 \tag{14}
\]

These are the actual parameters of that lemma, not numerical powers of
\(\log n\). Its bounded determinant representation prevents denominator
growth with the number of insertions.

Source execution and reconstruction of all selection vectors each scan
\(n\) packets at \(P\) stages, so the full initialization work is
bounded by

\[
 W_{\rm init}\le B_{\rm in}+T_{\rm cert}
 +c\left[nP H_a^{16}+n(P+2)^8v_a^3+m^2dH_a^2\right]
 +c nPN\,T_{\rm prim}(cH_a,\chi).
 \tag{15}
\]

The last scalar term charges optional fixed-input Gram preparation with
schoolbook fixed-precision arithmetic. Generating the finite Gaussian
packets fits the first term: there are \(D\) coordinates per packet,
and \(D\le cN\le cH_a\). One can use the source's bounded
Box--Muller construction. Elementary series, rational arithmetic and
rounding evaluate one coordinate in \(O(H_a^{10})\) work, below the
row allowance even after multiplying by \(D\). To verify this deliberately
loose degree, use \(O(H_a)\) series terms; clearing the common factorial
and dyadic denominators gives \(O(H_a^2)\)-bit integers, so reduced
rational arithmetic costs \(O(H_a^6)\) per operation. The bounded number
of series/bisection loops remains below \(O(H_a^{10})\). Coupling bits
and cutoff failure are those already included in (10).

The retained program and panel have the explicit bound

\[
 S_{\rm base}\le B_{\rm in}
 +c\left[((P+1)D+2P)p_a
        +(P+1)^2v_a+N(p_a+\log_2(N+2))\right].
 \tag{16}
\]

The three terms count packets/noises/current summaries, exact rational
weights, and a conservative instruction list with precision-sized literals.
The temporary initialization peak is bounded by

\[
 S_{\rm init}\le S_{\rm base}
       +c\left[nDp_a+(P+2)^3v_a+H_a^6\right]
       +S_{\rm prim}(cH_a,\chi)+S_{\rm cert}.
 \tag{17}
\]

Here \(S_{\rm cert}\) is any extra workspace used to obtain or verify
the input certificates. It is zero only when they are already supplied.

For compact updates, the exact final Cramer representation can retain a
single common denominator \(n\det H\) for all weights. The weighted
sum of dyadic row outputs then uses one denominator, so each product and
accumulator has \(O((P+1)v_a)\) bits. At most \(q\) products plus
one final rounded division cost \(O(q(P+1)^2v_a^2)\) bit operations
per summary. Thus **all** \(P\) acquisition updates have work

\[
 W_{\rm upd}\le c\left[P(P+1)H_a^{16}
                          +P(P+1)^3v_a^2\right]
       +cP(P+1)N\,T_{\rm prim}(cH_a,\chi).
 \tag{18}
\]

The same retained Cramer data already appear in the selection proof; this
does not require small nonzero weights or a well-conditioned selected panel.
If one uses separately reduced denominators instead, the safe product-rule
arithmetic bound is larger. Equation (18) specifies the common-denominator
implementation. Its peak is covered by (16), \(cH_a^6\), and the
single-call primitive workspace.

## 4. Query context, statistical blocks, seed, and full query cost

The source's information bound is explicitly

\[
 K_* =\frac{P}{2\alpha}\log(1+B_F^2/\eta^2),\qquad
 K_+=\max\{K_*,1\},
 \tag{19}
\]

where \(B_F\) caps each acquired scalar integrand. Obtain a certified
dyadic \(\widehat K\in[K_+,2K_+]\), and set

\[
 s=\left\lfloor\frac{n}{128\widehat K}\right\rfloor.
 \tag{20}
\]

For example, \(n\ge512K_+\) is an explicit sufficient condition
that makes the block lemma applicable with at least two rows per block.
This condition is not removed from the theorem by calling the parameters
fixed. On the common source event, vector and scalar sampling errors are
respectively at most
\(cB\sqrt{r_hK_+/n}\) and \(cB^2\sqrt{K_+/n}\), before their
explicit physical propagation factors.

Let \(k\le d+1+cR^2\) be the number of varying query-context coordinates,
including guarded intermediate moments. Let \(A_{\rm ctx}\ge1\)
bound their absolute values, with its logarithm covered by \(\chi\).
At precision \(p_{\rm ctx}\), an upper bound on the logarithm of the
number of all grid contexts, prefixes, and call indices is

\[
 L_{\rm ctx}=k[p_{\rm ctx}+\lceil\log_2(2A_{\rm ctx}+2)\rceil+2]
                   +\lceil\log_2((P+1)(Q+1))\rceil.
 \tag{21}
\]

These contexts are not stored or searched. Choose an odd block count
\(J\) with

\[
 J\le c[1+L_{\rm ctx}+\log_2((r_h+1)/\delta_{\rm q})]
 \tag{22}
\]

and a sufficiently large absolute constant so the coordinate-median
failures union bound. The numerical and PRG failure shares can be assigned
the same order with

\[
 F=1+L_{\rm ctx}+\log_2((r_h+1)/\delta_{\rm q}).
 \tag{23}
\]

Here \(\delta_{\rm q}\) is the total query-seed failure allocation.
Thus each fixed-context PRG test is required to have additive error at most
\(2^{-cF}\). Let \(N_b=Js\) be the number of row blocks in one
moment estimator and let \(E=\lceil\log_2(N_b+2)\rceil\).

For the finite Gaussian quantile sampler take

\[
 T^2\ge2\log\frac{16\,2^{L_{\rm ctx}}J sD}{\delta_{\rm q}},
 \qquad
 b_{\rm uni}\log2\ge T^2/2+
                 \log(C\Lambda/\epsilon_G).
 \tag{24}
\]

Choose \(\epsilon_G\) below its allocated row error and count it in
precision. The certificate must satisfy \(T\le G_{\max}\), or the
root cap and its consequent operand/sensitivity bounds must be enlarged
before applying these formulas. This explicit compatibility check replaces
the fixed-parameter assertion that the sampling cutoff eventually fits
inside the existing cap.

The CDF/quantile computation in the short-seed source has polynomial cost:
with \(O(v)\) Taylor terms and \(O(v)\) bisection steps, where
\(v\) bounds \(T^2\), requested precision, and argument bit length,
the same common-denominator calculation as above gives
\(O(v^{10})\) work and \(O(v^6)\) space per coordinate. A sufficient
whole-row query precision therefore is

\[
 p_q\le c\left[F+\log(nD+2)+\log\epsilon^{-1}+N\chi+\chi\right],
 \qquad H_q=H(p_q).
 \tag{25}
\]

It includes uniform bits, Gaussian evaluation, row output and accumulator
precision; enlarge the constant for the chosen numerical margin.
The sampler for \(D\) coordinates fits the \(H_q^{16}\) row
allowance. This is a sufficient precision schedule, conditional on (24)
and the supplied certificate, not an independent proof of the physical
good event.

Between successive rows, the following many bits suffice for one fixed
context's test:

\[
 S_{\rm between}\le
 c\left[(J(r_h+1)+P+k+R^4)H_q+E\right].
 \tag{26}
\]

The \(R^4\) term permits cached dense coefficient arrays. The much
larger row-evaluation scratch is discarded after every row and does not
enter this finite-state count. Fixed source instructions and data may be
hardwired in each proof test; their actual retained bits are still counted
in (16).

Using precisely the block-generator interface stated and sourced in
`SHORT_SEED_PRIOR_BLOCKS.md`, take the generator block length

\[
 A_{\rm rng}=c[S_{\rm between}+D H_q+E+F].
 \tag{27}
\]

One seed has at most \(cA_{\rm rng}E\) bits. Generating one row's block
by the stated Toeplitz-hash recursion costs at most
\(cA_{\rm rng}^2E\) bit operations. Restarting that seed for another
context is the source's separate fixed-context test, with its finite union
bound; it does not invoke a repeated-read PRG theorem.

Consequently a full unseen-input query satisfies

\[
 \begin{split}
 W_{\rm query}\le{}&T_x(p_{\rm ctx})
 +cQJs\left[H_q^{16}+A_{\rm rng}^2E
                        +N T_{\rm prim}(cH_q,\chi)\right]\\
 &+cQ(r_h+1)J\log_2(J+2)H_q
   +c(R^4+k+P)H_q^{16},
 \end{split}
 \tag{28}
\]

where the second line permits median sorting, context preparation, and
coefficient assembly. The following memory bounds count all live state:

\[
 \begin{split}
 S_{\rm retained}&\le S_{\rm base}+cA_{\rm rng}E,\\
 S_{\rm query\ peak}&\le S_{\rm base}
  +c[A_{\rm rng}E+S_{\rm between}+H_q^6]
  +S_{\rm prim}(cH_q,\chi)+S_x(p_{\rm ctx}).
 \end{split}
 \tag{29}
\]

The preparation term in (28) can be made smaller, but it cannot silently
disappear when \(s\) is small. These formulas retain \(s\) itself;
replacing it by \(n\) is a valid looser bound, unlike replacing a
parameter-dependent multiplicative factor by a width threshold.

## 5. One explicit coarse polynomial envelope

For a compact substitutable envelope, set

\[
 M=2+R+d,\qquad
 \Theta=2+\chi+\log_2(n+2)+\log_2(M+2)
                   +\log_2\delta^{-1}+\log_2\epsilon^{-1}.
 \tag{30}
\]

Assume the cap/conditioning certificate and (24) hold, allocate fixed
fractions of \(\delta\) to the finitely many failure categories, and
select the precisions just described. Equations (1)--(12) and (21)--(27)
give the following explicit estimates:

\[
 \begin{array}{c|c}
 \text{quantity}&\text{upper bound}\\ \hline
 P,k&cM^2\\
 D,r_h&cM\\
 N&cM^7\\
 p_a,H_a,p_{\rm ctx},v_a&cM^9\Theta\\
 L_{\rm ctx},J,p_q,H_q&cM^{11}\Theta\\
 S_{\rm base}-B_{\rm in}&cM^{16}\Theta\\
 S_{\rm between},A_{\rm rng}&cM^{23}\Theta^2\\
 E&c\Theta
 \end{array}
 \tag{31}
\]

For example, the last persistent-state exponent is
\(11+1+11=23\): \(J\) block means, \(r_h\) coordinates, and
\(H_q\) bits per coordinate. The source precision exponent is
\(2+7=9\); the context count adds at most two more powers. These
calculations do not use a parameter-dependent lower bound on \(n\).

Substitution into (15)--(18) and (28)--(29), with \(s\le n\), yields
the nonprimitive algorithmic bounds

\[
 \begin{array}{c|c}
 \text{resource}&\text{upper bound, besides supplied-input/certificate costs}\\ \hline
 \text{retained bits}&cM^{23}\Theta^3\\
 \text{post-initialization peak bits}&cM^{66}\Theta^6\\
 \text{initialization work}&cnM^{146}\Theta^{16}\\
 \text{temporary initialization bits}&c[nM^{10}\Theta+M^{54}\Theta^6]\\
 \text{all acquisition-update work}&cM^{148}\Theta^{16}\\
 \text{one query's work}&cnM^{189}\Theta^{17}.
 \end{array}
 \tag{32}
\]

The query row-stream degree is \(13+176=189\): \(QJ\) contributes
degree \(13\) and \(H_q^{16}\) contributes degree \(176\).
The independent coefficient-preparation term
\((R^4+k+P)H_q^{16}\) in (28) has degree at most \(180\), also
covered by (32) for \(n\ge1\). No claim of optimized polynomial
degree or a replacement for the checked logarithmic-exponent theorem is
made.

For the primitive calls, add at most

\[
 \begin{split}
 &cnM^9\,T_{\rm prim}(cM^9\Theta,\chi)
                  &&\text{during initialization},\\
 &cM^{11}\,T_{\rm prim}(cM^9\Theta,\chi)
                  &&\text{for all updates},\\
 &cnM^{20}\Theta\,T_{\rm prim}(cM^{11}\Theta,\chi)
                  &&\text{during query row streaming},
 \end{split}
 \tag{33}
\]

and the actual coefficient-preparation primitive calls if they are not
shared with a row evaluation. A safe additional allowance is
\(cM^{11}T_{\rm prim}(cM^{11}\Theta,\chi)\), which is already
dominated by the last bound in (33). Add the largest single-call primitive
workspace to the corresponding memory bound. Input acquisition,
certificate generation/verification, retained input descriptions, and query
coordinate acquisition remain the additive terms specified in Sections 1,
3, and 4.

If the physical program and logarithmic numerical certificates are
polynomial in the scientific parameters and the primitive interfaces have
uniform polynomial bit cost, (32)--(33) establish polynomial downstream
resources. They do not establish small polynomial degree. In particular,
substituting \(R\le A\Psi^u\) retains powers of \(A\) and
\(\Psi\) in (15)--(33); it does not justify replacing them by a
larger \(n_0\) and reporting a parameter-free prefactor.

## 6. Why a degree-four conclusion is not available here

Several distinct assertions must be separated.

First, the proof currently counts graph size \(R^7\), history precision
\(R^9\chi\), and selection work \(n(P+2)^8v_a^3\). The last is
as large as \(nR^{16}v_a^3\) when \(P\asymp R^2\). These are
upper bounds; their size alone is not a mathematical lower bound.

Second, a literal implementation of the specified dense matrix schedule
does have work above fourth degree in \(R\). At a two-orientation
history with \(\Theta(R)\) forward and reverse observations, the
Kronecker system has dimension \(r_m=\Theta(R^2)\). Materializing
it already writes \(\Theta(R^4)\) entries. A prescribed dense cubic
matrix multiplication at that dimension executes \(\Theta(R^6)\)
scalar operations. The explicitly given cofactor inverse evaluates
\(\Theta(r_m^2)\) determinants, each by cubic dense elimination,
and therefore executes \(\Theta(r_m^5)=\Theta(R^{10})\)
rational-operation slots on a full-size instance, before bit costs or
Newton steps. This is a statement about these enumerated loops. It is
not a claim that Kronecker inverses intrinsically require those costs.

Third, the graph-sensitivity precision \(PN\chi\) is a sufficient
worst-case stability bound, not an unavoidable precision lower bound.
Sharper physical conditioning, sharing coefficient work across rows,
structured Sylvester solvers, fast inverse algorithms, better selection,
and a different query estimator could improve the result. None of those
improvements is established by the current resource theorem.

Fourth, there are unavoidable input costs independent of these loose
algorithms. An explicitly supplied \(m\)-by-\(d\) dataset with
\(b_{\rm data}\) bits per entry has \(\Omega(md b_{\rm data})\)
input-description bits. A supplied dense root of
\(\Theta(Ln^2+dn)\) entries at \(b\) bits per entry has that size
times \(b\); reading it is not \(O(Ln^2+dn)\) bit work when \(b\)
grows. The construction instead generates its own fresh source law, as
the initialization note expressly requires. A general query presented as
\(d\) finite coordinate words also incurs their input cost. None of
these elementary observations proves a fourth-degree lower bound in
\(m\), gap inverse, or label size for the full model class.

## 7. Missing upstream certificates and exact claim boundary

The following must be supplied before replacing the fixed-problem result by
a parameter-uniform theorem about the original nonlinear network:

1. A counted \(R\), including physical time horizon, patch count,
   collocation degree, Picard count, example/layer loops, and added passive
   query fields, with explicit dependence on \(m,d,L\), the initial gap,
   labels, activation constants, target accuracy, and confidence.
2. Explicit physical good-event thresholds and constants: operator/RMS and
   coordinate caps; the raw \(A_0,q_0,B\) bounds; \(\sigma\); and
   the propagation factor \(\Gamma\). These determine (7), \(a,U\),
   and \(\chi\). A symbol \(C_*\) allowed arbitrary problem dependence
   is not this certificate.
3. Verified, finitely encoded noise and precision choices meeting (8),
   (10), (19)--(20), and sampler-cap compatibility (24). In particular,
   the explicit condition \(n\ge512K_+\) remains a condition, not a
   hidden removal of the \(K_+\) dependence.
4. A parameter-explicit dense/physical error bound and a comparison of the
   propagated sampling/rank-correction errors with the requested dense
   certificate. The argument that a positive fixed-label factor eventually
   dominates every logarithmic remainder does not give a uniform bound as
   labels approach zero. Zero labels may have their separate exact-zero
   branch, but nearby nonzero labels still require the actual inequalities.
5. A computational input model. Arbitrary real data have no finite bit
   encoding. Strip analyticity does not imply a computable activation,
   much less a uniform polynomial evaluator. For instance,
   \(\phi(x)=x+c\) with noncomputable real \(c\) is entire and has
   globally bounded derivative, but has no effective precision evaluator.
   The source's primitive model is legitimate as a stated model;
   it cannot be silently upgraded to fully charged bit complexity.

For polynomial dependence, it suffices to bound the relevant *logarithmic*
caps and inverse floors polynomially; the amplitudes themselves may be
exponential. Conversely, small \(R\) alone does not control the bit
length of supplied data, the precision of a tiny gap, primitive evaluation,
or the physical correctness threshold.

The established result of this audit is the conditional downstream
accounting (15)--(29), with the coarse polynomial envelope (32)--(33).
The source-to-physical-network certificates and the desired low-degree
scientific-parameter bounds are not proved by this audit.

Required process skills: `solve-math-rigorously` and
`investigate-conjectures`, including the adversarial-audit and evidence
references, were read. The repository-required custom notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
was permission denied even on an escalated read; no equivalent was found
in the readable skill roots. The repository's explicit notation rules were
applied directly, preserving \(d\) for input dimension and \(D\) for
packet dimension. No claim is made to have read the inaccessible skill or
its linked neural-network reference.

## 8. Authorized follow-up: a parameter-explicit numerical certificate

This section uses the subsequently authorized
`PHYSICAL_PARAMETER_ACCOUNTING.md`. It closes the *numerical resource*
certificate using that note's physical count and matrix-noise precision.
It does not make its inherited stochastic source event effective, nor
replace the smaller physical stability constants in the statistical
accuracy proof by the very large numerical upper bound used below.

Write \(r=m/\gamma\), let \(\beta\ge10\) be the activation bound
in that note, and retain the full original intersection of label allowances.
In particular \(16Yr\le1\), where \(Y=\|y\|_2/\sqrt m>0\).
Fix the desired normalized deterministic
accuracy exponent \(a_0\ge1\). To expose both dataset size and confidence,
enlarge the physical note's logarithmic factor to

\[
 Z=(a_0+1)\log\!\left(
   \frac{e n(m+d+2)\beta^{100L}(1+r)}{\delta}\right).
 \tag{34}
\]

For a fixed choice of \(a_0\), the extra factor is an absolute constant.
The physical note supplies the explicit upper bounds

\[
 R\le c\left[d+\beta^{300L}mL(1+r)^3Z^6\right],\qquad
 b_\sigma\le c\beta^{100L}(1+r)Z^2,
 \quad \sigma=2^{-b_\sigma}.
 \tag{35}
\]

The first bound includes the training and appended passive-field counts.
Its numerical accuracy choices pay for \(\operatorname{Lip}(F)T\)
directly. The old assignment \(b_\sigma\asymp\log^2 n\), with an
unreported parameter-dependent sufficient width, is not used here.

### 8.1 Remove small-label denominators from actual row instructions

It is insufficient to write \(\bar u=u/Y\) while retaining every
physical projection formula unchanged. Implement the factorization at
the field level. Write physical learned displacements and readout as
\(Y\bar D\) and \(Y\bar a\); write the residual and backward
response as \(Y\bar e\) and \(Y\bar b\). Then

\[
 \bar f=\langle\bar a,h\rangle_n,\qquad
 \bar e=\bar f-y/Y.
 \tag{36}
\]

Here \(\langle\cdot,\cdot\rangle_n\) denotes the source's normalized
readout pairing. Project the vector \(\bar e\) onto its RMS-unit ball.
Normalized backward propagation starts at \(\bar a\); its carrier
clip is the physical clip divided analytically by \(Y\), namely
\(32K_{\rm src}r\sqrt{\log(en)}\). The initialized Gaussian matrices
act on these normalized queries, with answer-noise level \(\sigma\)
in those coordinates. Physical backward noises are obtained by the final
multiplication by \(Y\). Thus no noisy physical quantity is divided by
an arbitrarily small label scale.

In normalized time \(\tau=t/r\), a hidden/first-layer normalized
gradient has coefficient \(rY\) multiplying
\(\bar e\bar b h\), whereas a normalized readout gradient has
coefficient \(r\) multiplying \(\bar e h\), with the original data
average and mobility normalizations. The inequalities \(rY\le1/16\)
and \(Y\le\beta^{3L}\) are supplied by the physical note. The only
input normalization requiring precision access is \(y/Y\); its
coordinate magnitudes are at most \(\sqrt m\), and its actual finite
input/evaluation cost remains charged through \(T_{\rm data}\).

There is also a bounded implementation of normalized displacement
projection. First project \(\bar D\) onto the normalized Frobenius ball
of radius \(4(1+r)\). If \(q\) is its resulting squared normalized
norm, multiply it by

\[
       \frac{1}{\sqrt{\max\{1,4Y^2q\}}}.
 \tag{37}
\]

The first operation ensures \(\|\bar D\|\le4(1+r)\); the second
ensures \(\|Y\bar D\|\le1/2\). Both fix the true trajectory:
the physical note bounds its normalized path length by \(2\sqrt r\)
and its physical learned displacement by \(1/4\).
The new scalar denominator in (37) is at least one. This avoids either
materializing the potentially huge radius \(1/(2Y)\) or introducing
its reciprocal into numerical conditioning. Both radial projections are
nonexpansive in the normalized state. Their composition only reduces the
numerical state domain used in the physical extension.

For normalized readout use its radius \(16rH_L\), replacing \(H_L\)
by the explicit upper envelope \(\beta^{3L}\) if necessary. This
retains the same \(\beta^{O(L)}\) physical bounds. The physical note
also gives \(\lambda\le H^2\le\beta^{6L}\), so
\(r\ge\beta^{-6L}\); an inverse power of this readout radius costs
only \(O(L\log\beta)\) bits. It does not introduce \(\log(1/Y)\).
All nonlinear activations continue to receive the original physical
preactivations. Their normalization is not a change of network dynamics.

These are explicit implementation choices for the normalized physical
extension. They preserve its projection identities on the true trajectory,
its field-count order, and its operator bounds. Its answer-noise comparison
uses noise in these normalized field coordinates; the powers of \(Y\)
are multiplied back only where the physical field requires them. This is
the normalized-noise interpretation needed for (35), rather than an
assertion that a fixed physical backward noise can be divided by \(Y\)
at no cost.

### 8.2 Raw caps and ridge precision

The physical note's recurrences give envelopes
\(\beta^{O(L)}(1+r)^{O(1)}\) for normalized physical RMS fields,
coefficients, and carrier clips, with the displayed square-root logarithm.
For an intentionally loose explicit envelope use

\[
 C_{\rm phys}=\beta^{1000L}(1+r)^{10}(1+Z)^{10},
 \qquad
 X=2^{\left\lceil\log_2\!\left[
 c_0(2+n+R+d+C_{\rm phys}^{2}+\sigma^{-1})\right]\right\rceil},
 \tag{38}
\]

where \(c_0\) is a sufficiently large absolute numerical constant.
The physical estimates used here have powers at most \(100L\),
and the normalization just described adds only fixed powers of \(1+r\)
and \(\beta^L\); hence this envelope has slack. In particular,
each capped principal row coordinate is at most
\(C_{\rm phys}\sqrt n\le X\), and the physical-Gram norm is
at most \(R C_{\rm phys}^2\le X^2\).

The innovation bound also retains \(C_{\rm phys}\) explicitly. For
one initialized hidden mixer \(W\), its normalized entries have prior
law \(\operatorname{vec}W\sim N(0,n^{-1}I)\). At an exact predictable
matrix-observation prefix, let \(\mathcal A\) be the linear map sending
\(\operatorname{vec}W\) to the stacked forward and reverse matrix
actions, and let \(b_{\rm obs}\) be the corresponding stacked noisy
answers. Gaussian likelihoods with answer-noise variance \(\sigma^2\)
give the conditional mean

\[
 \operatorname{vec}\overline W
  =(nI+\sigma^{-2}\mathcal A^*\mathcal A)^{-1}
                       \sigma^{-2}\mathcal A^*b_{\rm obs}.
 \tag{38a}
\]

The queries are fixed when evaluating that prefix likelihood; their
predictable choice introduces no additional likelihood factor. This is
conditioning on the observed matrix transcript, not on private acquisition
data or on a physical good event. The following norm inequalities hold
pointwise at prefixes satisfying the certified physical bounds.
There are at most \(R\) answers, each of Euclidean norm at most
\(\sqrt n C_{\rm phys}\), so
\(\|b_{\rm obs}\|_2\le\sqrt{nR}C_{\rm phys}\).
For each singular value \(s\ge0\) of \(\mathcal A\),

\[
 \frac{s}{n\sigma^2+s^2}\le\frac{1}{2\sigma\sqrt n},
 \qquad
 \|\overline W\|_F\le\frac{\sqrt R C_{\rm phys}}{2\sigma}.
 \tag{38b}
\]

The scalar inequality follows from
\((s-\sigma\sqrt n)^2\ge0\); singular-value decomposition then
proves the operator bound used in (38b).
At the next call, its answer covariance \(\Gamma\) has
\(\Gamma\succeq\sigma^2I\). Thus its whitened innovation
\(g=\Gamma^{-1/2}(y-\overline Wq)\), for
\(\|q\|_{2,n},\|y\|_{2,n}\le C_{\rm phys}\), satisfies

\[
 \|g\|_{2,n}\le\frac{C_{\rm phys}}{\sigma}
             +\frac{\sqrt R C_{\rm phys}^2}{2\sigma^2},
 \qquad
 \max_i|g_i|\le\sqrt n\left[
 \frac{C_{\rm phys}}{\sigma}
             +\frac{\sqrt R C_{\rm phys}^2}{2\sigma^2}\right]
 \le cX^4.
 \tag{38c}
\]

The last step uses individually
\(n,R,C_{\rm phys}^2,\sigma^{-1}\le X\). Therefore the chosen
innovation-root cap \(X^9\) remains valid without treating
\(C_{\rm phys}\) as a fixed constant. Physical/innovation cross
moments obey the same cap by the RMS Cauchy--Schwarz inequality. These
are bounds on the exact source event; the explicit caps define the
bounded numerical extension outside it.

Learned-list coefficients acquire at most one factor \(r\) or \(rY\),
also at most \(X\). Repeating the degree checks in Sections 3--4 of
`EXPLICIT_COMPILER_EXPONENT.md` with these bounds preserves the loose
raw operand cap \(X^{100}\). In particular, the raw query coefficient
and history-Gram bounds may be taken as

\[
 A_0\le X^{102},\qquad q_0\le X^{202}.
 \tag{39}
\]

A valid supplied small passive-feature cap can be intersected with the
deterministic physical coordinate bound; this only reduces its cap and
preserves its identity on the physical event. Thus its numerical magnitude
may be assumed \(1\le B\le X^{100}\). This operation bounds the
*size* of that supplied cap. It does not independently construct the much
sharper passive-feature certificate used for statistical root-width error.

No unquantified physical mean-mixer constant is needed to select ridge
precision. For \(0<\tau\le1\), the buffered empirical Gram has norm
at most \(q_0+3\). Therefore its transformed mean coefficient obeys

\[
 \|A\|\le A_0(q_0+3)\le2X^{304}.
 \tag{40}
\]

This estimate is independent of \(\tau^{-1}\). Use this deliberately
large bound in the two-coordinate recurrence (27) of the moment note,
and use \(a_1,a_2\le c\beta^2\le X^2\), \(B\le X^{100}\).
The square allows for composing the activation with a smooth value cap:
its second derivative contains the square of the first activation
derivative. This leaves the following numerical power estimates unchanged.
Its matrix row sums are at most \(X^{412}\), after increasing \(c_0\).
The normalized readout coefficient is bounded by \(X^{203}\).
Products and sums through \(L\) layers are consequently bounded by

\[
                   \Gamma_{\rm num}=X^{512(L+2)}.
 \tag{41}
\]

Take normalized deterministic allowance \(\epsilon=n^{-a_0}\), and
choose the dyadic ridge

\[
 c_\tau=2048(L+2)+2a_0+2048,
 \qquad \tau=X^{-c_\tau}.
 \tag{42}
\]

It satisfies (7). For example, the first denominator in (7) has total
power at most \(1024(L+2)+406\), besides an absolute constant, while
\(\epsilon^{-2}\le X^{2a_0}\). The variance constraint has smaller
power \(512(L+2)+202+a_0\), since \(\sigma^{-1}\le X\).
Thus all numerical mean/variance perturbations after (41) fit the assigned
allowance, without a width-dependent absorption of their coefficients.

Whitened marks have cap at most \(X^{101+c_\tau/2}\); their products,
row accumulators, and coefficient matrices have cap \(X^{c(L+a_0+1)}\).
Their inverse/root floors and local Lipschitz constants have logarithmic
size at most \(c(L+a_0+1)\log X\). Consequently the certificate (3)
can be supplied with

\[
 \chi\le c(L+a_0+1)\log_2X,
 \qquad
 \Theta\le c\beta^{200L}(1+r)Z^2.
 \tag{43}
\]

To check the last inequality, (35), (38), and the enlarged logarithm
(34) give \(\log X\le c\beta^{100L}(1+r)Z^2\).
Also \(L\le\beta^L\), \(a_0\) is fixed, and the extra logarithms
in (30) are bounded by \(cZ\). There is no suppressed \(\log m\),
\(\log d\), \(\log\delta^{-1}\), or \(\log Y^{-1}\) in (43).

The bound (41) is used **only** for negligible deterministic errors and
precision. Substituting it into the statistical root-width error would
give a much weaker estimate. That statistical argument still uses the
inherited physical mean-mixer, passive-feature, and whole-source events.

### 8.3 Gaussian cutoff compatibility and final substitution

The Gaussian cutoff check can also be made finite and explicit. Equations
(24), (31), and (43) require
\(T^2\le cM^{11}\Theta\) for a sufficient choice of cutoff.
Since \(M\le cX\), \(L\le R\le X\), and
\(\Theta\le c[(L+a_0+1)\log X+Z]\), while
\(X\ge C_{\rm phys}^2\ge(1+Z)^{20}\), one has
\(\Theta\le cX^2\) for fixed \(a_0\).
Thus the required squared cutoff is at most \(cX^{13}\).
Choose the absolute \(c_0\) in (38) large enough that
\(cX^{13}\le X^{18}\). The source innovation-root cap
\(G_{\max}=X^9\) then satisfies \(T\le G_{\max}\) for every
admissible numerical instance. No sufficiently-large-
\(n\) qualification is used for this cap comparison.

Because \(d\le m\), (35) gives
\(M\le c\beta^{301L}m(1+r)^3Z^6\). Combining this with (43) in
(32) yields a shared, intentionally loose envelope:

\[
 \begin{array}{c|c}
 \text{resource}&\text{nonprimitive bound}\\ \hline
 \text{retained bits}
   &c\beta^{65000L}m^{23}(1+r)^{72}Z^{144}\\
 \text{post-initialization peak bits}
   &c\beta^{65000L}m^{66}(1+r)^{204}Z^{408}\\
 \text{initialization work}
   &c\beta^{65000L}n m^{146}(1+r)^{454}Z^{908}\\
 \text{all update work}
   &c\beta^{65000L}m^{148}(1+r)^{460}Z^{920}\\
 \text{one query's work}
   &c\beta^{65000L}n m^{189}(1+r)^{584}Z^{1168}\\
 \text{temporary initialization bits}
   &c\beta^{65000L}
       [n m^{10}(1+r)^{31}Z^{62}
                   +m^{54}(1+r)^{168}Z^{336}].
 \end{array}
 \tag{44}
\]

For verification, a term \(M^u\Theta^v\) contributes powers
\(m^u(1+r)^{3u+v}Z^{6u+2v}\) and activation exponent
\((301u+200v)L\). The largest such exponent in (44) is
\((301\cdot189+200\cdot17)L=60289L\), below the shared 65000.
The additive data/certificate/query-input costs and evaluator terms in
(33) remain additional. Rounding \(md\) training-data values to the
used finite precision fits these memory bounds when their evaluator and
original encoding costs are charged separately; it does not make
arbitrary exact real data finite.

Equation (44) is a conditional resource theorem for the specified capped,
normalized finite-program interfaces. The inherited scientific source
event and its width restrictions, the explicit sampling condition (20),
and comparison of the statistical remainder with \(3b_n\) are separate
accuracy obligations. Their thresholds remain as stated in their sources;
this appendix neither makes them polynomial nor removes them. In
particular it proves no useful crossover with dense cost and no parameter
degree at most four for the unseen-query decoder.
