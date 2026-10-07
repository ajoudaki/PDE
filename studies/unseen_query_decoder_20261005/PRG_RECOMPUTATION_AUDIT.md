# Repeated initialization access and space-bounded pseudorandomness

2026-10-06. Scoped theoretical continuation. Internal conditional reduction
and access-pattern audit; no experiments, promotion, or Git operations.

The conditional dense evaluator does not yet yield a short-seed decoder.
Its relevant missing property is a small **random-input visit count** or
a generator theorem for its actual repeated-read tests, not a smaller
integration stack. There is a legitimate intermediate route: the
Impagliazzo--Nisan--Wigderson generator permits bounded repeated access,
and a polylogarithmic-visit reformulation would have a polylogarithmic
seed. No such reformulation is supplied by the present recursive evaluator.

A new precise positive reduction is proved below. A generator fooling
one family of repeated-read comparison tests would suffice for the
whole-sphere, all-physical-time prediction bound. The tests use a fixed
dense reference only in the proof; the decoder need not retain that
reference. This reduction avoids amplifying an unspecified $o(1)$ dense
failure probability by a growing query net. The required generator
guarantee remains an explicit additional assumption.

## 1. Finite random input and counted evaluator

Use the fixed neural-network problem, physical normalization, label
allowance, and activation/data computation interfaces of
`RECOMPUTATION_SPACE.md`. Put $\ell_n=\log(en)$. There are

\[
 D_n=nd+(L-1)n^2
\tag{1}
\]

independent initialized Gaussian coordinates before the zero readout.
The conditional evaluator uses $S_n=O(\ell_n^C)$ working bits, with an
absolute exponent $C$ depending at most on the activation-evaluation
exponent. It repeatedly requests the same initial coordinates. Its
finite precision and loop counters are included in $S_n$.

One can first replace the Gaussian input by a finite bit string without
claiming compression. For example, encode each coordinate by $p_n$ fair
bits, apply the midpoint Gaussian quantile map, cap it at a known
$R_n=C_0\sqrt{\ell_n}$, and round it to the common coordinate grid.
Take $p_n=O(\ell_n^3)$. To justify the finite-law replacement, couple
the midpoint uniform grid to a uniform variable with error $2^{-p_n}$.
Outside the Gaussian tails beyond $R_n$, the inverse-CDF derivative is
at most $C e^{R_n^2/2}$, so the coordinate error is at most
$C e^{R_n^2/2}2^{-p_n}$ plus the grid-rounding error. A union over (1),
with $C_0$ sufficiently large, makes the cap failure $o(1)$. The
global extension's initial-condition amplification is
$e^{O(\ell_n^{3/2})}$; hence these errors remain negligible at every
fixed inverse-polynomial target accuracy. Gaussian CDF evaluation and
bisection on this capped interval have elementary finite-precision,
polylog-space implementations; they do not store a quantile table.

Write

\[
 N_n=D_n p_n=n^2\ell_n^{O(1)},\qquad
 \Gamma_n:\{0,1\}^{N_n}\longrightarrow\mathbb R^{D_n}
\tag{2}
\]

for this deterministic coordinatewise map. A coordinate of $\Gamma_n$
can be computed from its corresponding $p_n$ input bits in polylog
space. Those bits must have their original values on every request.

For a bit string $u$, let $g_n(u;t,v)$ be the exact projected predictor
of the globally controlled extended flow initialized at $\Gamma_n(u)$,
with time capped at $T=O(\ell_n)$. It is defined for every $u$, not only
Gaussian-good inputs. The extension gives uniform bounds

\[
 |g_n(u;t,v)|\leq C_1,\qquad
 |g_n(u;t,v)-g_n(u;s,z)|
       \leq C_1(|t-s|+\|v-z\|_2)
\tag{3}
\]

for $s,t\in[0,T]$ and $v,z$ on the sphere, or its fixed slightly
larger input ball. The time inequality follows by combining the bounded
parameter speed with the projected predictor's parameter Lipschitz
bound. The spatial inequality is the forward subtraction with uniformly
capped physical operators. For $t\geq T$, define $g_n(u;t,v)=g_n(u;T,v)$.

The streamed solver computes a value $\widehat g_n$ with
$\sup_{t,v}|\widehat g_n-g_n|\leq n^{-a}$ for any fixed $a$, in
$S_n$ working bits, for every capped finite root. The inherited good
event is needed only to identify $g_n$ with the original dense flow,
not to run its globally controlled numerical algorithm.

## 2. What the verified generator theorems actually cover

Nisan's original generator is formulated for finite-state machines
receiving successive random blocks. Section 2.1 models the state between
blocks and does not provide repeatable access to discarded blocks.
Thus evaluating its output coordinate from a seed is computationally
possible, but this does not enlarge its class of fooled tests.
[Nisan, original paper, Section 2.1](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).

There is a stronger relevant theorem. For an $S$-space computation whose
random-input head moves along a line and visits each input cell at most
$v$ times, the INW communication construction gives seed length

\[
 s=O\!\left(\log N\,[vS+\log(N/\varepsilon)]\right).
\tag{4}
\]

Here fixed read-only ordinary inputs are permitted. To obtain (4), use
one processor per random-tape cell. Each head crossing transfers the
$O(S)$-bit machine state; each processor communicates $O(vS)$ bits.
The line has constant separator width, so INW Theorem 2 gives (4).
Its Theorem 3 states the constant-$v$ specialization. The paper also
states polylog-space evaluation of its generators.
[INW, original paper, Theorems 2--3 and Section 4](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/INW94/proc.pdf).

Consequently, with $N=N_n$, $S=\ell_n^{O(1)}$, and
$\log\varepsilon^{-1}=\ell_n^{O(1)}$, a proof of
$v=\ell_n^{O(1)}$ would supply a legitimate absolute-polylog seed and
coordinate evaluator. Visits count cells crossed during travel to a
requested index, not just cells whose bits are used. A direct random
jump interface therefore needs a separate line-traversal analysis.

For comparison, the verified Gurjar--Volk read-$k$ theorem allows an
arbitrary known oblivious reading sequence, but its seed guarantee is

\[
 O\!\left(e^{k^2}N^{1-1/2^{k-1}}\log N
                  [\log(N/\varepsilon)+k\log W]\right),
 \qquad k\geq2,
\tag{5}
\]

for width $W$. Already at $k=2$, this certificate contains $\sqrt N$;
substituting (2) does not yield polylogarithmic storage. Equation (5)
is an upper bound supplied by that construction, not a lower bound on
all read-twice generators.
[Gurjar--Volk, Theorem 1.1](https://www.cse.iitk.ac.in/users/rgurjar/papers/prgReadk.pdf).

HashPRG does not silently remove the access condition either. Its formal
Definition 2.4 restricts the tester to streaming over the random string.
Its CountSketch application constructs a separate one-pass finite-state
test for the particular scalar error event, exploiting the sketch's
structure. This is an example of the kind of new reformulation needed
here, not a theorem for arbitrary repeatable random-oracle computations.
[Kacham--Pagh--Thorup--Woodruff, Definition 2.4 and Section 6.1](https://arxiv.org/html/2304.06853v2).

## 3. The current evaluator's access pattern does not pass that gate

Consider even the ordinary coordinate-recursive initialized forward
pass, before Picard iteration or spectral clipping. To compute the
second-layer coordinates it uses

\[
 h_i^{(2)}(v)=\phi_2\!\left(\sum_{j=1}^n
                  W_{ij}^{(2)}\phi_1(A_jv)\right).
\tag{6}
\]

The literal row-by-row streamed schedule recomputes $\phi_1(A_jv)$
for each output row $i$. Each first-layer row is therefore read $n$
times when all second-layer outputs are requested. This is independent
of the fixed depth $L\geq2$ and already exceeds every polylogarithm.
Keeping all first-layer features would remove these rereads at the cost
of $n$ stored scalars. Reversing the loops instead keeps all $n$
second-layer preactivation accumulators, again outside the target.

This count describes the literal recursive implementation. It does not
prove a lower bound for an alternative algorithm computing only the
final scalar prediction. In particular it does not exclude a new
network-specific rearrangement or distributional approximation.

The recursive integration adds another source of repeated access. With
the midpoint implementation in `RECOMPUTATION_SPACE.md`, each Picard
level evaluates many lower-level states. Its certified counts have

\[
 J=O(\ell_n^2),\qquad \log Q=O(\ell_n^3),
 \qquad \log D=O(\ell_n^3),
\tag{7}
\]

where $Q$ is the quadrature count and $D$ the clipping-polynomial degree.
Depth-first evaluation trades these very large trees of repeated source
requests for short stacks. The existing bounds do not bound input visits
by a polylogarithm. They supply at best an exponential-in-polylog upper
bound. Substituting such a visit bound into (4) gives no requested seed
bound. Small stack depth is not a visit-count estimate.

The following elementary memory statement prevents an exact generic
read-once simulation from bypassing this distinction. Suppose $r$
independent input bits have been consumed, all will later be requested
again, and the machine will never revisit their input cells. If the
machine must reproduce their entire values exactly from its retained
state and fixed later inputs, it needs at least $r$ state bits: two
different $r$-bit prefixes cannot lead to the same state. More generally,
with at most $2^S$ states, exact reproduction succeeds with probability
at most $2^{S-r}$ on a uniform prefix, since one state can correctly
reproduce at most one prefix. The conclusion still holds with independent
fresh random bits by conditioning on those later random bits and averaging.

Applied to transcript-preserving replay of (6), this costs at least
the previously consumed independent first-layer root bits, already
$\Omega(n)$. It is not a lower bound for the network's scalar observable;
changing the computation rather than reproducing its coordinate transcript
is exactly the remaining possibility. Replacing repeated roots by fresh
bits changes their equality constraints and is not such a proof.

## 4. Exact conditional transfer from a suitable repeated-read PRG

Here is a sufficient generator interface with all approximation and
uniformity quantifiers exposed. Suppose the dense-comparison source,
finite-root coupling, and capped solver imply, for independent uniform
$U,V\in\{0,1\}^{N_n}$,

\[
 \mathbb P\!\left\{
 \sup_{t\geq0,\ v\in S^{d-1}}
      |g_n(U;t,v)-g_n(V;t,v)|>b_n
                 \right\}\leq\alpha_n,
 \qquad \alpha_n\longrightarrow0,
\tag{8}
\]

where $b_n=n^{-1/2}e^{C\sqrt{\ell_n}}\ell_n^{C'}$ is the inherited
near-root scale after harmless enlargement. Only this error scale and
$\alpha_n=o(1)$ are used; no polynomial rate for $\alpha_n$ is assumed.
For sufficiently large $n$, $b_n\to0$.

Take a computably enumerated sphere/time net of mesh
$\Delta_n=b_n/(100C_1)$ on $[0,T]\times S^{d-1}$. A rational grid
followed by normalization gives at most

\[
 Q_n\leq (C/\Delta_n)^d(1+T/\Delta_n)
       =n^{O_d(1)}
\tag{9}
\]

points and needs only $O_d(\log n)$ counter and coordinate bits at the
working accuracy. A rational constant-factor underestimate of $b_n$
may be used for mesh construction. Its description and the fixed
problem constants count, but the net is not stored as an array.

For each fixed reference string $v_0\in\{0,1\}^{N_n}$, define a
Boolean test $\mathcal B_{v_0}(u)$: stream through this net and accept
if, at any point $q$,

\[
 |\widehat g_n(u;q)-\widehat g_n(v_0;q)|>5b_n/4.
\tag{10}
\]

Use solver accuracy $n^{-a}\leq b_n/100$. A constant-accuracy rational
threshold inside a small interval around $5b_n/4$ gives the same bounds.
The test holds only one net point, two scalar predictions, the reference
input address, and the solver workspace. It therefore uses
$S_n+O_d(\log n)$ bits. It reads $u$ repeatedly as a random-access
input. The reference $v_0$ is an ordinary fixed read-only input, not an
additional random tape. If a time bound is needed, a halting finite-bit
machine with this workspace and polynomial input lengths has at most
$2^{O(S_n+\log n)}$ configurations; alternatively the explicit recursive
loop bounds give an exponential-in-polylog time bound.

Assume an explicit generator

\[
 \mathcal G_n:\{0,1\}^{s_n}\longrightarrow\{0,1\}^{N_n}
\tag{11}
\]

has $s_n=\ell_n^{O(1)}$, a polylog-space coordinate algorithm, and
fools every test (10), uniformly over all fixed references $v_0$, with
error $\varepsilon_n=o(1)$. The exponent and coordinate-evaluation
exponent must be absolute over the fixed network problem, as in the
desired contract. This is the missing assumption; no theorem in
Section 2 has been shown to supply it for the present evaluator.

**Conditional consequence.** Retain a uniform seed $Z$ and decode by
$\widehat g_n(\mathcal G_n(Z);t,v)$. For an independent original
dense Gaussian model, the uniform all-physical-time/sphere difference
is at most $3b_n$ with probability $1-o(1)$, after absorbing numerical,
finite-law, and original-good-event errors. The retained seed plus peak
decoding workspace has absolute-polylog bit count. Training is replayed
during each decoding call; no autonomous replacement flow is asserted.

To prove it, average (8) over the second argument. There exists one
fixed string $v_*$ such that

\[
 \mathbb P_U\{\|g_n(U)-g_n(v_*)\|_\infty>b_n\}
       \leq\alpha_n.
\tag{12}
\]

If the uniform difference is at most $b_n$, the solver errors make
every quantity in (10) at most $1.02b_n$. Thus
$\mathbb P_U\{\mathcal B_{v_*}(U)=1\}\leq\alpha_n$.
The generator assumption gives

\[
 \mathbb P_Z\{\mathcal B_{v_*}(\mathcal G_n(Z))=1\}
       \leq\alpha_n+\varepsilon_n.
\tag{13}
\]

If this test rejects, (3), the mesh radius, and the two solver errors
imply
$\|g_n(\mathcal G_n(Z))-g_n(v_*)\|_\infty<1.3b_n$.
Combine this with (12) and the triangle inequality to get a difference
at most $2.3b_n$ between generated and independent uniform finite-root
models, with failure at most $2\alpha_n+\varepsilon_n$. The finite-root
coupling and dense tail identification give the stated conservative
$3b_n$ bound for the original dense model.

The reference $v_*$ is selected only by an existence argument in the
proof and is never stored in the decoder. The uniform generator guarantee
over fixed references is what makes this legitimate. A generator chosen
specifically by inspecting an uncounted $v_*$ would not satisfy this
contract. Likewise, pointwise fooling followed by a naive union would
yield $Q_n\alpha_n$, which need not vanish. The single streamed test
in (10) is needed to avoid that gap.

For a bounded-visit proof, it is the visit count of this whole comparison
test, not just one prediction call, that must fit (4). Streaming the
$Q_n$ net points sequentially multiplies visits. Thus even a hypothetical
polylog-visit pointwise evaluator would not automatically complete the
whole-sphere reduction via INW; one would additionally need a suitably
strong pointwise dense failure rate, or a low-visit uniform comparison
test. The general repeated-read assumption (11) directly includes (10).

## 5. Why the existing degree audit does not supply (11)

Section 10 of `RECOMPUTATION_SPACE.md` gives a separate algebraic
certificate, not a support-count objection. If each activation is
replaced by a degree-$q$ polynomial, one top feature has total degree
$q+\cdots+q^L$ and can use
$O_d(q^{L-1})$ distinct initialized coordinates in one monomial.
On even the favorable additional coordinate range
$O(\sqrt{\log n})$, the elementary strip approximation to
inverse-polynomial accuracy uses $q=O(\ell_n^{3/2})$. Thus matching
all monomials already asks for a depth-dependent polylogarithmic
independence order at the initial prediction derivative.

A polynomial gradient field of degree $r$ has Picard root-degree
certificate $r^J$. Time Taylor jets improve one patch to degree
$1+K(r-1)$, but $H$ restarts give the compositional certificate
$[1+K(r-1)]^H$. The available $J,H=\ell_n^{O(1)}$ do not make these
polylogarithmic degree bounds. These are limitations of that sufficient
moment-matching construction, not approximation-degree lower bounds.
No estimate presently makes the high-root-support terms collectively
negligible through training, and a bound for polynomial expectations
would still need conversion into the threshold event (10).

## 6. Result of the bounded audit

The ordinary Nisan substitution is unjustified. A legitimate repeated-read
theorem, (4), identifies a sharper sufficient property, but the current
space-saving recomputation schedule lacks it. Known read-$k$ parameters
in (5) do not give the needed seed even under a much more favorable
constant-read certificate. The network-specific degree route also has
no absolute-polylog certificate after learned-time composition.

What is new and positive is the exact reduction (8)--(13): one uniform
comparison-test family, with fully counted polylog workspace and no
stored dense reference, is sufficient to transfer dense-vs-dense accuracy
to a short-seed replay decoder. Constructing a generator for that family,
or proving a stronger low-communication reformulation of it, remains open.
This is not a proof that no such generator exists.

Repository scientific input was confined to the complete current-study
`RECOMPUTATION_SPACE.md` and its already-authorized dense-comparison
interface. Verified external primary statements are linked at their use.
No other study or archived source was opened for this audit. The
conjecture-audit and rigorous-math workflows were applied; the previously
reported canonical-skill access restriction is unchanged.
