# Independent reconstruction of the local matching theorem

Date: 2026-10-10. Verdict: the mathematical matching result passes this
scoped reconstruction. Two editorial corrections are requested below.
No scientific correction, new assumption, experiment, changed closure, or
promotion is needed for the theorem as precisely scoped here. This is an
internal reconstruction, not an independent promotion review.

## Frozen inputs and coverage

The following three scientific inputs were read completely, including
their proofs, scope qualifications, counts, and final limitations:

| Input | Lines | SHA-256 |
| --- | ---: | --- |
| `MATCHING_RESULT.md` | 392 | `18b7c9b6d0dbc753f57757f78c1c07cbd178fc80203e380e86a124a50b314be7` |
| `UPPER_LOCAL_GEOMETRIC.md` | 471 | `e174c084b16cd5aa6b8b5bf940c663a348056fa7dfa40bae71ee1b23ec758485` |
| `WORST_CASE_RESULT.md` | 536 | `d4044343dcd031df298dba5af42d512e5e72b925edcb79edf0392828b4020f09` |

No check reports, study README/history, other studies, chats, maintained
book, or code were read. Required canonical-notation instructions and their
neural-network reference, rigorous-mathematics instructions, and the
conjecture skill with its research-contract and adversarial-audit references
were read. No experiments or Git operations were performed. This report is
the only file written by this checker.

The external papers linked by the source were not fetched under the
three-file input boundary. The Gaussian Lipschitz concentration statement
used in the lower theorem is stated and its application checked below.
Claims classifying identity activation under another paper's assumptions
are not needed for this self-contained, explicitly identity-activation
matching theorem and are not separately source-verified here.

## Exact result checked

For deterministic data \(v_a\in\mathbb R^d\),
\(\|v_a\|_2\le1\), \(|y_a|\le1\), use

\[
f_n(t,v)=c(t)^\top W(t)B(t)v,\qquad
\mathcal L=\frac1{2m}\sum_a(f_n(t,v_a)-y_a)^2,
\]

with \(B\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), \(c\in\mathbb R^n\),
Euclidean/Frobenius gradient flow, independent initial entries of
\(B_0,W_0\) distributed as \(N(0,1/n)\), and \(c_0=0\).
Both hidden activations are identity. The coordinate changes
\(B=W^{(1)}/\sqrt n\), \(c=u/\sqrt n\) give exactly the original
mobilities \((n,1,n)\): the coordinate and gradient factors each contribute
\(1/\sqrt n\), canceling mobility \(n\).

The ordered tensors are \(K_1=f_n\) and
\(K_{r+1}(\ldots,v)=DK_r[V(v)]\), where

\[
V(v)=(W^\top cv^\top,\ c(Bv)^\top,\ WBv).
\]

Order \(q\) retains the original initialized arrays through rank \(q\),
freezes rank \(q\), and drives lower ranks with its own residual. Queries
are passive first slots. All comparisons use physical time
\(0\le t\le T=2^{-15}\). Let \(E_n(q)\) denote the supremum of the
compression error over this interval and the entire unit input sphere,
and let \(D_n\) denote the corresponding difference between two independent
dense initializations.

For \(n\ge4\), \(1\le d\le n\), the candidate proves

\[
q_n=\left\lceil\frac{\log(2^{37}n^3)}{\log1024}\right\rceil,
\qquad
\Pr\{E_n(q_n)\le D_n/n\}
\ge1-4e/\sqrt n-4e^{-c_*n},
\quad c_*=4-\tfrac32\log9>0.
\]

Solutions exist on the asserted good event. The probability estimate is
for each deterministic dataset, including datasets varying with width;
it is not a simultaneous small-ball estimate over datasets chosen after
seeing initialization.

For the specified hard data with fixed \(0<\eta\le1\),
\(4\mid m\), \(4\le m\le\sqrt n\), \(d=m+1\), this upper and the
reconstructed lower imply optimal retained literal storage
\(\exp[\Theta_\eta(\log m\log n)]\), for each fixed success probability
\(p\in(0,1)\) and fixed positive comparison factor. They do not assert
probability-one finite-order success.

## Ordered source bounds and identification of the actual closure

Every expression generated from \(c^\top WBv_0\) is built from matrix
products, transposes, outer products, and scalar/vector pairings. Replacing
one parameter occurrence by the corresponding component of \(V(v_k)\)
adds one parameter leaf and one input slot. After \(k\) replacements there
are at most \(3\cdot4\cdots(k+2)=(k+2)!/2\) terms, each with \(k+3\)
parameter leaves. These are expression trees of norm-bounded operations;
the construction does not introduce a free trace or a dimension factor.
Consequently, on a block-norm bound \(s\),

\[
|K_{k+1}(v_0,\ldots,v_k)|
\le\frac{(k+2)!}{2}s^{k+3}\prod_{i=0}^k\|v_i\|_2.
\]

At \(s=4\) this is exactly the stated
\(32\,4^k(k+2)!\) coefficient bound. Each input occurs linearly.
Readout reflection sends \(K_r\) to \((-1)^rK_r\), so all odd
initialized ranks vanish. An odd frozen top is therefore zero and leaves
the preceding even top constant; the two orders have the same predictions.

Define the fixed data contractions and evolving dense coefficient by

\[
Q=\frac1m\sum_a v_av_a^\top,\qquad
b=\frac1m\sum_a y_av_a,\qquad
w=B^\top W^\top c.
\]

Here \(\|Q\|_{\rm op}\le1\), \(\|b\|_2\le1\), and the exact
physical flow is

\[
\dot B=W^\top c(b-Qw)^\top,\qquad
\dot W=c[B(b-Qw)]^\top,\qquad
\dot c=WB(b-Qw).
\]

For a trial path \(z\), put \(a_z=b-Qz\). Repeated integration gives
the finite prediction map

\[
v^\top\mathcal F_q[z](t)=
\sum_{k=1}^{q-1}\int_{0<s_k<\cdots<s_1<t}
K_{k+1}(v,a_z(s_1),\ldots,a_z(s_k);0)\,ds_k\cdots ds_1.
\]

The order is correct: the first appended source index is associated with
the latest integration time. The scalar ordered integral satisfies
\(I'_{a_1\ldots a_k}(t)=u_{a_1}(t)I_{a_2\ldots a_k}(t)\), where
\(u_a=(y_a-v_a^\top z)/m\). Thus differentiating the source's
reconstruction of every retained rank gives precisely its original
rank equation. Rank \(q\) has only its constant term. At a fixed point,
rank one equals \(v^\top z\), making the residual the closure's own
residual. Polynomial ODE uniqueness identifies these reconstructed arrays
with the original finite NTH, not merely a prediction surrogate.

On a radius-one parameter ball around an admissible initial state, block
norms are at most five, the residual vector has norm at most \(126\),
and block velocities have norm at most \(3150\). Since \(3150T<1\),
a first-exit argument gives dense existence and boundedness on the interval.
The source bound for \(K_2\) gives

\[
\|w(t)\|_2\le\|b\|_2(e^{1875t}-1)<\|b\|_2
\]

when \(b\ne0\). In the dense ordered expansion, all external source
vectors are fixed while the innermost tensor is integrated. No derivative
of a residual is introduced. The \(N\)-fold remainder is bounded by

\[
\frac{125}{2}(N+1)(N+2)(10\|b\|_2T)^N,
\]

because \(s^{N+3}=5^{N+3}\), the source vectors have norm at most
\(2\|b\|_2\), and the simplex contributes \(T^N/N!\). It tends to
zero uniformly, proving \(w=\mathcal F_\infty[w]\). This checks the
essential identification with the dense physical trajectory.

## Uniform contraction, parity, and the error constant

On the continuous-path ball \(\|z\|_\infty\le\|b\|_2\), set
\(x=8T=1/4096\). The map norm and its Lipschitz constant satisfy

\[
\|\mathcal F_q[z]\|_\infty
\le64\|b\|_2[(1-x)^{-3}-1]<\|b\|_2/16,
\qquad
L\le96x(1-x)^{-4}<1/32.
\]

The first factor follows from
\(\sum_{k\ge0}(k+1)(k+2)x^k=2(1-x)^{-3}\).
For the second, telescope over the \(k\) source slots: one slot has
norm bounded by the path difference, and the other \(k-1\) slots have
norm at most \(2\|b\|_2\). This produces the stated factor \(16\),
not a factor involving \(m\) or \(d\). Both strict bounds follow from
\((1-x)^{-4}<4/3\). Hence contraction is uniform even as \(b\to0\).

The first potentially nonzero omitted index is
\(j=2\lfloor q/2\rfloor+1\). For \(z_0=x\|b\|_2\), the tail is at
most

\[
32(j+1)(j+2)z_0^j\frac{1+z_0}{(1-z_0)^3}.
\]

Indeed, after putting \(k=j+\ell\), the polynomial factor is at most
\((j+1)(j+2)(\ell+1)^2\). Dividing by \(1-L\) costs less than an
additional factor two. The whole-sphere norm equals the Euclidean norm
of the prediction-coefficient difference, with no dimension factor.
Since \((j+1)(j+2)\le4^j\), \(j\ge q\), and
\(\|b\|_2^j\le\|b\|_2\), the result is exactly

\[
E_n(q)\le64\|b\|_2\,1024^{-q}.
\]

If \(b=0\), the dense initial state is an equilibrium. The finite
reconstruction at \(z=0\) also has every contracted source contribution
zero; uniqueness makes it stationary. Thus \(E_n(q)=D_n=0\), without
division by zero and without a nonzero-label-mean assumption.

## Complex disk and actual dense-discrepancy lower bound

The complex extension retains ordinary transposes. Complex operator norm
is invariant under transpose, and all polynomial expressions remain
holomorphic. In the maximum block norm, a unit variation changes
\(w=B^\top W^\top c\) by at most \(75\). Each velocity derivative is
therefore bounded by
\(5\cdot126+5\cdot126+25\cdot75=3135\).
The Picard map on the closed disk of radius \(R_0=1/4096\) maps the
radius-one path ball into itself and contracts, since both
\(3150R_0\) and \(3135R_0\) are less than one. Uniform iteration gives
a holomorphic solution in the disk's interior and continuity on its
closure. The circles used for Cauchy's formula are strictly interior.

The prediction derivative has three terms each bounded by \(5^4\)
times the residual-vector norm. Radial integration therefore gives

\[
\|w(t)\|_2\le\|b\|_2(e^{1875|t|}-1)<\|b\|_2
\quad (|t|\le R_0),
\]

using \(1875/4096<\log2\). This verifies that the complex estimate
retains the small factor \(\|b\|_2\).

For \(b\ne0\), let \(v_*=b/\|b\|_2\) and
\(g(t)=f_n(t,v_*)-\widetilde f_n(t,v_*)\). On the pair's norm event,
\(|g|\le2\|b\|_2\) on the disk. With \(R=1/8192\), a circle of
radius \(R/2=2^{-14}\) about any \(t\in[0,R/4]\) lies in that disk.
Consequently,

\[
|g''(t)|\le2!\,(2\|b\|_2)/(2^{-14})^2
=2^{30}\|b\|_2.
\]

At zero readout,

\[
f_n'(0,v_*)=\|b\|_2H,\qquad H=\|W_0B_0v_*\|_2^2.
\]

Because \(v_*\) is deterministic, \(A=\|B_0v_*\|_2^2\) has law
\(\chi_n^2/n\); conditionally on the full vector \(B_0v_*\), the ratio
\(H/A\) has this same law, independent of that vector. Thus \(H\) is
the product of two independent normalized chi-square variables.

For their density \(p\), the maximizer is \(a_0=1-2/n\ge1/2\).
On \([a_0,a_0+n^{-1/2}]\),
\((\log p)'(a_0)=0\) and \((\log p)''\ge-2n\), so
\(p\ge e^{-1}p(a_0)\). Integrating over this interval proves
\(\|p\|_\infty\le e\sqrt n\). The gamma-density integration gives
\(\mathbb E[A^{-1}]=n/(n-2)\le2\). The product density is therefore
bounded by \(2e\sqrt n\), as is the density of the difference of two
independent products. In particular,

\[
\Pr\{|H-\widetilde H|\le1/n\}\le4e/\sqrt n.
\]

This estimate is unconditional; intersecting afterward with the matrix
norm event introduces no invalid conditioning. The norm event for one
matrix follows from a \(1/4\) net, the threshold-three chi-square tail,
and \(d\le n\): its failure is at most
\(\exp[-(4-\tfrac32\log9)n]\). Four matrices give
\(4e^{-c_*n}\) for the pair.

On the intersection, \(|g'(0)|\ge\|b\|_2/n\). Taylor's integral
remainder at the deterministic time \(t_n=1/(2^{30}n)\le T\) gives

\[
D_n\ge|g(t_n)|
\ge\frac{\|b\|_2}{2^{30}n^2}
-\frac{\|b\|_2}{2^{31}n^2}
=\frac{\|b\|_2}{2^{31}n^2}.
\]

This is a bound on the actual realized discrepancy. Combining it with
the error upper bound cancels \(\|b\|_2\) and gives
\(E_n(q)/D_n\le2^{37}n^2 1024^{-q}\). The declared \(q_n\) gives
at most \(1/n\); it is at least two throughout \(n\ge4\).
All probability and power-of-two constants in this chain check.

## Reconstruction of the lower bound used in the match

The hard data have \(v_a=(e_0+e_a)/\sqrt2\), signs of mean \(1/2\),
and \(y_a=\eta s_a\). Their Gram is
\((I+\mathbf1\mathbf1^\top)/2\), and
\(\bar v=m^{-1}\sum_a s_av_a\) has squared norm
\(1/8+1/(2m)\). Thus its direction is a unit passive query and
\(\lambda=\|\bar v\|_2\ge2^{-3/2}\). The matrix norm and source-norm
event in the source has exponential probability; the latter follows by
taking each of the two independent chi-square norm ratios at least \(3/4\).

For \(j=2\lfloor q/2\rfloor+1\), the signed-mean discrepancy has
zero derivatives below \(j\) and

\[
g^{(j)}(0)=\eta^jK_{j+1}(\bar v,\ldots,\bar v;0).
\]

One may see the feedback cancellation directly from the ordered
representation: the omitted tail first occurs at degree \(j\), and its
leading term uses only the initial control. The difference of controls in
the retained map is proportional to the output difference and acquires
one extra time integration, so cannot change that leading coefficient.
Equivalently, in differentiated rank equations, differentiated-residual
terms contain lower-order prediction differences, all zero. Thus the
own-residual feedback is accounted for.

For source ascent, put \(h=Bv_*\) in this paragraph only. Rescaling the
source time by \(\tau=\lambda s\) gives
\(h'=W^\top c\), \(W'=ch^\top\), \(c'=Wh\). The preserved quantities
\(WW^\top-cc^\top=W_0W_0^\top\) and
\(\|h\|^2-\|c\|^2=\|h_0\|^2\) imply

\[
c''=(\|h_0\|^2I+W_0W_0^\top)c+2\|c\|^2c.
\]

After diagonalization and sign choices, the initial velocity and every
Taylor coefficient are nonnegative. Setting
\(A=\|h_0\|^2\), \(H=\|W_0h_0\|^2\), coefficientwise induction
compares this solution with \(c'(0)u\), where
\(u''=Au+2Hu^3\), \(u(0)=0,u'(0)=1\). On the event \(A,H\ge1/2\),
this dominates \(2\tan(\tau/2)\): that comparison function satisfies
\(u''=u/2+u^3/8\), whose nonnegative coefficients are smaller.
The tangent recurrence gives the further coefficientwise lower bound
\(\tau/(1-\tau^2/12)\).

Since the source output is \(c^\top c'\), its coefficient at
\(j=2k+1\) is at least \(H(k+1)^2 12^{-k}\ge8^{-j}\).
Restoring the output factor \(\lambda\) and time factor \(\lambda^j\)
gives \(K_{j+1}(\bar v,\ldots,\bar v;0)\ge j!64^{-j}\).
These comparisons hold at every order on a single initialization event.

The finite closures have a common holomorphic disk by their ordered maps:
on the unit prediction ball at radius \(1/4096\), the norm sum is less
than \(0.38\), and the Lipschitz sum is less than \(0.2\). The dense
Picard argument above supplies the same disk. Their signed difference is
bounded by two on the smaller closed disk \(R=1/8192\).

The derivative-to-real-interval transfer also checks. For a degree-\(N\)
polynomial, its Chebyshev coefficients have magnitude at most twice its
interval norm; the endpoint derivative formula and the affine interval
map give

\[
|P^{(j)}(0)|\le\frac{2N}{j!}
\left(\frac{8N^2}{R}\right)^j\|P\|_{[0,R/4]}.
\]

The Taylor tail of a disk-bounded-by-two function is at most
\((2/3)4^{-N}\) there. Writing \(\rho=\eta/64\),
\(\theta=\rho R/8=\eta/2^{22}\),
\(\kappa=16[1+\log(1/\theta)+\log(8/3)]\), and
\(N=\lceil\kappa j\rceil\), the source's logarithmic estimate makes
the tail at most half the polynomial lower bound. Using
\(j!\ge(j/e)^j\), \(N\le2\kappa j\), and \(j\le2^j\) then gives

\[
\|g\|_{[0,R/4]}\ge
\frac1{8\kappa}
\left(\frac{\theta}{8e^2\kappa^2}\right)^j.
\]

This reproduces exactly \(A_\eta e^{-C_\eta j}\). Dividing the signed
mean by \(\lambda\le1\) transfers the lower to the actual passive
query. Thus the all-order lower does not rest on an unproved Taylor-tail
noncancellation assumption.

For completeness, the dense discrepancy upper used by that lower has the
right topology and dimension dependence. With block norms at most five,
the coefficient vector is \(25\)-Lipschitz in the sum of the two
Frobenius and one vector differences. Each flow block is
\(1255\)-Lipschitz in this same sum, giving Gronwall factor
\(e^{3765T}\). Since only the two matrix blocks vary initially, the
stated scalar initialization Lipschitz constant
\(L_T=50e^{4000T}\) is conservative and valid.

The Gaussian concentration theorem needed is: if \(X\) has independent
\(N(0,1/n)\) coordinates and \(F\) is a global \(L\)-Lipschitz real
function, then
\(\Pr(|F(X)-\mathbb EF(X)|\ge s)\le2e^{-ns^2/(2L^2)}\).
A scalar Lipschitz extension from the norm-good initialization set meets
these hypotheses. The same deterministic extension for each independent
copy has the same mean, so the difference tail at threshold \(2s\) is
at most \(4e^{-ns^2/(2L_T^2)}\). Equality with the original observables
is restored on the common good event.

A \(1/2\) sphere net has at most \(5^d\) points and costs a factor two
in the linear sphere supremum. A time grid of mesh at most \(1/n\)
costs \(500000/n\) for the difference of two coefficient vectors, each
\(250000\)-Lipschitz in time. The resulting bound is
\(D_n\le4s+500000/n\), with the stated union-bound choice of \(s\).
Taking \(d=m+1\) and failure target \(1/n\) yields
\(D_n\le C\sqrt{(m+\log(en))/n}\), as required.

Finally, for \(r_n=n/(m+\log(en))\), all orders
\(q\le(4C_\eta)^{-1}\log r_n\) satisfy a compression-error lower
\(A_\eta e^{-C_\eta}r_n^{-1/4}\), whereas the dense discrepancy upper
is \(Cr_n^{-1/2}\). Their ratio diverges uniformly over those orders.
This is the correctly directed use of concentration for a necessary
budget; the sufficient budget above instead used anti-concentration.

## Storage, quantifiers, and surviving boundaries

There are \(m+d\) retained first slots and \(m\) choices for every
driving slot. Thus the exact counts are

\[
N_{\rm moving}=(m+d)\sum_{r=1}^{q-1}m^{r-1},\qquad
N_{\rm frozen}=(m+d)m^{q-1}.
\]

For \(m\ge2\), these give precisely the three bounds in the matching
candidate. For \(m=1\), the separate counts
\((1+d)(q-1)\) and \(1+d\) are correct. First-slot linearity makes
\(f_{n,q}(t,v)=\sum_i v_i f_{n,q}(t,e_i)\) an exact decoder from the
passive coordinate outputs; an infinite query collection is not hidden.
The proof's data contraction is an analytical identity, not an alternative
retained state replacing the specified literal arrays.

For \(d=m+1,m\ge4\), the total is at most \(5m^q\), plus the
optional \(md+m\) data storage. With \(q_n=O(\log n)\), this proves
the sufficient exponential-in-\(\log m\log n\) count. The lower permits
removing an initialized zero odd top and still charges at least
\(m^{q-1}\) literal retained entries, or \(m^{q-2}\) moving entries.
Subtracting one or two from the necessary order changes only constants
once \(n\) is sufficiently large.

Uniformly for \(4\le m\le\sqrt n\), eventually
\(m+\log(en)\le2\sqrt n\), while this denominator is at least one.
Therefore \(\log[n/(m+\log(en))]\) lies between
\(\frac12\log n-\log2\) and \(\log n\), establishing the matching
logarithmic exponent uniformly in the stated range. The lower at one
passive query also lower-bounds the whole-sphere error. Its common
all-order event excludes initialization-dependent order selection under
a deterministic insufficient budget, not only a preselected order.

No unaccounted dense trajectory, future observation, noncausal residual,
restart rule, or additional evolving state is used. The counts explicitly
exclude coefficient-generation work, initialization peak memory, numerical
integration, and precision. They are real-coordinate counts of literal
tensors, not an information-theoretic lower bound on structured encodings.

The theorem is a complete local result for the specified deep-linear,
zero-readout, canonical-metric class. It does not resolve a universal
nonlinear-activation upper, every fixed longer interval, all-time accuracy,
or a lower bound against factored tensor storage. Fixed label magnitude is
essential to the displayed hard-family exponent; imposing
\(\eta=O(1/m)\) changes its constant and its asymptotic consequence.

## Requested editorial corrections

1. In `MATCHING_RESULT.md`, the phrase “any prescribed fixed positive
   success probability” should explicitly read \(p\in(0,1)\). The
   proved probability tends to one; that alone does not prove a
   probability-one requirement. This clarifies the intended quantifier
   without changing the proof or its asymptotic constants.
2. In `WORST_CASE_RESULT.md`, equation (7), the displayed numerator has
   an actual form-feed byte before `rac`, rather than the literal TeX
   backslash in `\frac`. Replace it by `\frac`. The intended unit query
   is unambiguous from its denominator, norm identity, and subsequent
   uses; this is a rendering correction only.

The supervisor was informed of both issues before any author edit. This
report evaluates the frozen hashes above; source hashes must be updated
or the corrections explicitly recorded if those two edits are applied.

## Author resolution after the frozen review

Both requested editorial corrections were applied. The theorem and proof
status lines were also changed from awaiting reconstruction to internally
checked, with links to this report. No estimate, argument, or hypothesis was
otherwise changed. The resulting source hashes are:

- `MATCHING_RESULT.md`:
  `74cc2f091e4106bbd12d9ecb51ff5049f2b889e613647b148b83188dd76c63f4`.
- `UPPER_LOCAL_GEOMETRIC.md`:
  `6cbdc29a429fb7e27d9688f6a6951a5751e62cd8bf490ff8560b9ff786de9733`.
- `WORST_CASE_RESULT.md`:
  `8b4f03bd580adbc078a1f9bb6030101954cb0341e987a22bfcd904d7e7815e50`.

This author addendum records the narrow post-review edits; it does not
alter the reviewer's verdict or replace a promotion review.
