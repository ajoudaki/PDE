# Reconstruction of the short causal dense-training program

2026-10-06. Scoped internal mathematical check, not promotion or a decoder
theorem. No experiment or candidate-file edit.

## 1. Frozen input and verdict

The complete checked candidate is `SHORT_CAUSAL_TRAINING_PROGRAM.md`,
SHA-256
`28ed9b8ec6da166e037560c51de4edfdc41c63e9d4a8212992ddc236a5777eef`.

The substantive reduction reconstructs. Its positive endpoint quadrature
weights yield amplification $\exp(2\lambda T)$, without an extra
interpolation-norm factor. The normalized complex parameter derivative
bound is also valid from the supplied source RMS bounds. Thus the claimed
absolute logarithmic exponent for the number of initialized matrix calls
survives the full proof.

Two exact bookkeeping corrections are needed:

1. Choose the ordinary patch length $h=1/(16\lambda K)$, or impose a
   matching lower bound. The displayed condition merely $0<h\le
   1/(16\lambda K)$ does not imply the asserted upper bound on the
   number of patches.
2. If $J$ node Picard iterations are followed by constructing the path
   from $F(U^{(J)})$, the exact field-evaluation count is $HK(J+1)$,
   not $HKJ$. Alternatively adjust the final-iteration convention.
   Neither correction changes the logarithmic exponent.

For arbitrary fixed inverse-polynomial accuracy, the analytic input should
explicitly cite `ANALYTIC_TAIL_EXTENSION.md`, not just the bridge whose
first stated horizon is $32(\gamma/m)^{-1}\log(en)$. That extension was
explicitly authorized and read completely during this check. It supplies
the same complex-time bounds over every finite horizon, on the same
initialization event, after its stated eventual deterministic width
conditions. This is not an additional label restriction.

The carrier clip must precede multiplication by the activation derivative,
as in the already authorized recomputation note's equation (6). The
candidate's reference to that definition suffices; displaying it locally
would make the construction unambiguous. Clipping only the resulting
backward response would not prove the Lipschitz estimate.

Subject to these corrections and the inherited source event, this is a
valid exact-real, finite causal approximation theorem for the dense flow.
It does not reduce initialization information or establish a compact
Gaussian replacement.

## 2. Source estimates and complex displacement bounds

Use $v_a\in S^{d-1}$, residuals $r_a=f_n(v_a)-y_a$, and
$\rho=\|r\|_2/\sqrt m$. Write $\|z\|_{2,n}=\|z\|_2/\sqrt n$.
The network, mobilities and normalization are those in candidate Section 1
and recomputation equations (1)–(2). Its displacement norm is

\[
 \|u\|=\|A-A_0\|_F/\sqrt n
       +\sum_{\ell=2}^L\|W^\ell-W_0^\ell\|_F
       +\|w\|_{2,n}.
\]

Let $H_\ell$ and $D_\ell$ be fixed complex bounds for the feature and
backward-response RMS norms, respectively, on the supplied time domain.
In the bridge they are $H_\ell$ and $S\tau_\ell$ from equations
(5)–(6). The physical gradient formulas give, for complex time as well,

\[
 \frac{\|\dot A\|_F}{\sqrt n}\le2\rho D_1,
 \qquad
 \|\dot W^\ell\|_F\le2\rho D_\ell H_{\ell-1},
 \qquad
 \|\dot w\|_{2,n}\le2\rho H_L.
 \tag{1}
\]

Indeed $m^{-1}\sum_a|r_a|\le\rho$, and for complex vectors
$b,h$ the algebraic outer product still obeys
$\|bh^T/n\|_F=\|b\|_{2,n}\|h\|_{2,n}$. Norm estimates use
absolute values, not positivity of a complex residual Gram.

On the real trajectory, integration of (1) and the inherited integrable
residual bound prove the fixed displacement radius required by the
candidate. On the complex domain, bridge Section 8 bounds $\rho(z)$
by $2Y$. Consequently

\[
 \|u'(z)\|\le4Y
   \left(D_1+\sum_{\ell=2}^LD_\ell H_{\ell-1}+H_L\right).
 \tag{2}
\]

There is no width factor in (2). The state and its derivative are
holomorphic because the finite-dimensional original ODE is holomorphic
inside the supplied activation strip; the clipping extension is not being
continued holomorphically.

Bridge equations (23), (30) and (32) supply the training-coordinate
maximum, radius $r_t=c_t/\sqrt{\log(en)}$, and safe strip margin on
its initial horizon. The complete analytic-tail extension, Sections 2–3,
continues the original ODE near all later real anchors in one fixed small
parameter ball around the last source time. Its equations (7)–(8) keep
the solution strictly inside that ball, and preserve the same feature,
response and initialized-image RMS bounds. Thus (2) applies near every
patch of any required horizon $T=C_a\log(en)$. Its Section 4 also
supplies the all-time real carrier maximum with the stated factor two.

These are inherited internally checked scientific inputs. The present
check reconstructs their use and the rank-one estimates (1)–(2); it does
not independently reprove the source's probabilistic insertion theorem.

## 3. Global real extension and prediction sensitivity

Project learned displacements blockwise onto fixed balls strictly containing
their actual ranges. Each projection is nonexpansive in its normalized
Hilbert norm, and their product is nonexpansive in the displayed sum norm.
For hidden matrices,
$\|W_0^\ell+P\Delta W^\ell\|_{\rm op}
\le\|W_0^\ell\|_{\rm op}+\|P\Delta W^\ell\|_F$.
This is the reason a full spectral matrix function is unnecessary here.
The projected first matrix has a bounded Frobenius RMS norm, and the
projected readout has bounded RMS norm.

For clarity the protected backward recursion, with projected parameters
denoted by bars, is

\[
 \widehat\delta_a^L
   =\phi_L'(\bar z_a^L)\odot\operatorname{clip}_M(\bar w),
 \qquad
 \widehat\delta_a^\ell
   =\phi_\ell'(\bar z_a^\ell)\odot
     \operatorname{clip}_M((\bar W^{\ell+1})^T
                              \widehat\delta_a^{\ell+1}),
 \tag{3}
\]

where $M=C\sqrt{\log(en)}$. Real coordinate clipping is
nonexpansive, vanishes at zero, and cannot increase the RMS norm. Hence
forward and backward RMS norms are bounded uniformly for every projected
state, even though the clip's coordinate bound grows with width.

Forward subtraction first gives
$\|\Delta z^\ell\|_{2,n}+\|\Delta h^\ell\|_{2,n}
\le C\|\Delta u\|$. In a backward product, subtraction separates
the changed carrier and the changed gate. The latter has RMS norm at most
$\sup|\phi_\ell''|M\|\Delta z^\ell\|_{2,n}$. The former
propagates the upper response difference with a fixed operator coefficient,
plus a parameter difference times a bounded reference RMS norm. Downward
induction therefore gives $C(1+M)\|\Delta u\|$, not $CM^L\|\Delta u\|$.
Residual clipping has Lipschitz constant one. Rank-one subtraction in
(1) proves

\[
 \sup_u\|F(u)\|\le C,
 \qquad \operatorname{Lip}(F)\le C(1+M)=:\lambda.
 \tag{4}
\]

The order in (3) matters. For example, with $\phi(z)=\sin z$,
clipping $\phi'(z)v$ only after multiplication leaves derivative $-v$
at $z=\pi/2$, where the unclipped response is zero. Large $v$ is not
controlled by such an output clip.

The chosen projections and clips are inactive on the real good trajectory,
so its equation is exactly $u'=F(u)$. For a new unit query $v$, forward
subtraction and the final normalized inner product give

\[
 \sup_{\|v\|=1}|f(u,v)-f(\widetilde u,v)|
 \le C\|u-\widetilde u\|.
 \tag{5}
\]

This is deterministic over the entire sphere and introduces no query net.
Optional training-preactivation clips preserve (4) if placed consistently
in the forward and backward evaluations and chosen inactive on the true
training trajectory. They are unnecessary for this short-program proof.
Smooth caps may be preferable for a later Gaussian-derivative evaluator,
but no such later result is used here.

## 4. Interpolation and endpoint positivity

Take the candidate's $K$ Chebyshev-root nodes on $[0,1]$. Discrete cosine
orthogonality gives $\|a_0\|\le\max_j\|b_j\|$ and
$\|a_k\|\le2\max_j\|b_j\|$ for $1\le k<K$. Since the
Chebyshev polynomials have absolute value at most one on the real interval,

\[
 \|I_Kb\|_\infty\le(2K-1)\max_j\|b_j\|.
 \tag{6}
\]

Integrating their even terms gives precisely candidate equation (6),
with weights

\[
 \omega_j=K^{-1}\left[1-2\sum_{k=1}^{\lfloor(K-1)/2\rfloor}
             \frac{\cos(2k\theta_j)}{4k^2-1}\right].
\]

For an empty sum the bracket is one. Otherwise
$\sum_{k=1}^r2/(4k^2-1)=1-1/(2r+1)$ proves each bracket is
at least $1/(2r+1)>0$. Exactness for constants gives
$\sum_j\omega_j=1$. Thus the endpoint integral has norm at most
the maximum norm of the nodal data, unlike the crude interior bound (6).

For completeness, if a Banach-space-valued function is holomorphic and
bounded by $C_0$ on a disk of radius twice the interval length about its
midpoint, its Taylor coefficient of order $j$ has norm at most
$C_0(2h)^{-j}$. The real interval has half-length $h/2$, so its
degree-$K-1$ Taylor remainder is at most
$(4C_0/3)4^{-K}$. Using the weaker bound $C2^{-K}$, exactness on
that polynomial and (6) yield interpolation error

\[
 \eta=CK2^{-K}.
 \tag{7}
\]

Cauchy's formula and the triangle inequality work directly in the
finite-dimensional block norm. No dimension factor enters. Apply (7) to
the original holomorphic time function $u'(t)$ from (2), not to the
clipped vector field at arbitrary complex states.

## 5. Complete uniform-in-time error recurrence

Set $\ell_n=\log(en)$, $K=\lceil\ell_n^2\rceil+2$ and $J=K$.
Choose ordinary patch length $h=(16\lambda K)^{-1}$ and shorten only
the final patch. Enlarging the fixed coefficient in $\lambda$ makes the
disk used in Section 4 fit in radius $r_t$ on every patch. The number of
patches is $H=\lceil T/h\rceil=O(\ell_n^{7/2})$ for
$T=C_a\ell_n$.

On a patch of actual length $h_j\le h$, the nodal integral map has
contraction factor
$q_j\le h_j\lambda(2K-1)\le1/8$. Let $U^*$ be its fixed point,
$V$ the exact trajectory nodes, and $e$ the starting-state error.
The exact nodes have map defect at most $e+h_j\eta$. Therefore

\[
 \|U^*-V\|_{\max}\le\frac{e+h_j\eta}{1-q_j}
                          \le2(e+h_j\eta).
 \tag{8}
\]

Starting from the constant node array $b$, boundedness in (4) gives
$\|U^*-b\|_{\max}\le Ch_jK$. After $J$ node iterations,

\[
 \|U^{(J)}-U^*\|_{\max}
       \le Ch_jK8^{-J}\le\zeta:=ChK8^{-J}.
 \tag{9}
\]

Construct the patch path and its endpoint from $F(U^{(J)})$. At the
endpoint positivity of the weights gives

\[
 \begin{aligned}
 e_{\rm new}
 &\le e+h_j\lambda\{2(e+h_j\eta)+\zeta\}+h_j\eta\\
 &=(1+2h_j\lambda)e
       +h_j\eta(1+2h_j\lambda)+h_j\lambda\zeta.
 \end{aligned}
 \tag{10}
\]

Since $h_j\lambda\le1/16$, summing this scalar recurrence and using
$\prod_j(1+2h_j\lambda)\le e^{2\lambda T}$ proves

\[
 \max_j e_j\le CT e^{2\lambda T}(\eta+\lambda\zeta).
 \tag{11}
\]

At an interior point of patch $j$, use (6), (8) and (9) to obtain

\[
 \|\widetilde u(t)-u(t)\|
 \le(1+2q_j)e_j+(1+2q_j)h_j\eta+q_j\zeta.
 \tag{12}
\]

This is uniformly negligible as well. The first term uses (11), the
second is at most $C h\eta$, and the third at most $\zeta/8$.
All three are bounded by a fixed multiple of (11)'s right side for
sufficiently large width; directly keeping the two local terms leads to
the same conclusion. Thus no claim about interior positivity is required.

Here $\lambda T=O(\ell_n^{3/2})$, whereas both $2^{-K}$ and
$8^{-J}$ have logarithm $-c\ell_n^2+O(1)$. Equations (7), (9),
(11) and (12) are therefore smaller than $n^{-a}$ for every fixed
$a>0$ at sufficiently large individual width. Increase an internal
accuracy exponent if needed to absorb fixed constants. The patch endpoint
is the next patch's initial value, so the piecewise path is continuous.
Equation (5) transfers the estimate to all sphere queries simultaneously.

Finally, if the inherited output derivative is bounded by
$C_f e^{-\kappa t}$, its motion from $T$ to any later time, including
infinity, is at most $(C_f/\kappa)e^{-\kappa T}$. Choosing
$T=C_a\ell_n$ with $C_a\kappa>a+1$ and freezing the numerical
endpoint proves the all-physical-time assertion. The analytic-tail source
is what permits this arbitrary fixed horizon coefficient without a new
stochastic event.

## 6. Causality, ranks and operation counts

Each hidden velocity is a sum of $m$ rank-one terms. A current Picard
state is its committed starting displacement plus a linear combination
of the previous iteration's $K$ right sides. It does not contain the
recursively expanded computation tree. At an endpoint only $K$ final
right sides are appended to the committed description. Consequently the
rank-description length of each hidden displacement is at most
$mK(H+1)$, independently of the number of earlier Picard iterations.
Old intermediate vector nodes can remain part of the causal DAG without
being expanded into this rank description.

For $D=\sum_\alpha c_\alpha a_\alpha b_\alpha^T/n$,

\[
 \|D\|_F^2=\sum_{\alpha,\beta}c_\alpha c_\beta
       \frac{a_\alpha^Ta_\beta}{n}
       \frac{b_\alpha^Tb_\beta}{n},\qquad
 Dv=\sum_\alpha c_\alpha a_\alpha
                              \frac{b_\alpha^Tv}{n}.
 \tag{13}
\]

The analogous first-weight formula has fixed training inputs on the
right; the readout is a vector sum. The ball projection multiplies each
description by one scalar. Thus norms, projected actions and transposed
actions require only scalar empirical inner products and linear
combinations of existing vectors. The initialized parts still require
the actual $A_0,W_0^\ell$ calls.

With the path convention used in Section 5 there are $HK(J+1)$ field
evaluations. Each uses $O(mL)$ initialized matrix/transpose calls and
creates $O(mL)$ principal vector arrays, treating a finite linear
combination as one vector instruction. Thus the number of those calls
and arrays is $O(mLHK(J+1))=O(\ell_n^{15/2})$ for a fixed problem.
If linear combinations are expanded into binary additions, the vector
and scalar instruction counts receive only another fixed polynomial
factor from the rank bound; no exponent depends on $L,m,d$.

All required Gram entries of generated arrays are at most the square of
their polynomial count. Evaluating (13) at all nodes remains polynomial
in this count and the rank-description length. A late query adds the
stated forward initialized calls and contractions with the stored learned
factors. These observations validate the absolute-power scalar-instruction
claim as well as the looser $C\ell_n^8$ Gaussian-call bound.

The instructions are exact-real here. Width-$n$ vectors and initialized
dense matrices remain indispensable inputs to this construction. The
number of matrix calls is not a total information count, and no finite-bit
activation, data, time or query interface is supplied by this theorem.
Those distinctions are correctly explicit in the candidate.

## 7. Provenance and claim level

The complete frozen candidate was read. Previously authorized complete
inputs remained unchanged at these hashes:

- `RECOMPUTATION_SPACE.md`:
  `74adb390a71c76ef21831ac76005288d6827fdc8db072dc271b2c0ea32f2dba3`.
- `GENERAL_DENSE_COMPARISON.md`:
  `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`.
- `GENERAL_EXPLICIT_FITTING.md`:
  `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6`.
- `COMPACT_FULL_LABEL_RANGE.md`:
  `90aeb1a3aba585aab27f0b46cb23ad7391614abbc64272dccf16ab25fb80b071`.

After the supervisor explicitly expanded this check's source scope, the
following integrated notes were read completely, including their final
sections and corrections:

- `UNBOUNDED_COMPRESSOR_BRIDGE.md`:
  `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.
- `ANALYTIC_TAIL_EXTENSION.md`:
  `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349`.

No linked prior studies, unassigned notes, other reviewers' reports,
experiments or external sources were accessed. The maintained notation
and already-read rigorous-proof workflow were applied. The custom
canonical-notation skill remains inaccessible, so the explicitly directed
minimal-notation and maintained-notation fallback was used.

This is a supervised separate reconstruction: the supervisor supplied the
candidate and clarified the intended pre-gate carrier clips and source
scope. The checker independently reconstructed the interpolation weights,
endpoint recurrence, complex rank-one estimates and transcript counts.
It is not a fresh isolated promotion review. Only this assigned check was
created; no candidate, maintained file or Git index was changed.

Final claim: the short causal approximation reduction is mathematically
supported after the two bookkeeping repairs, with the all-time analytic
source identified explicitly. Compact initialization, growing-program
Gaussian identification, passive-query stability and total compact
decoder workspace remain separate unresolved obligations.

## 8. Corrected-version verification

The corrective candidate, SHA-256
`0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5`,
was inspected on 2026-10-06. Equation (8) now fixes the ordinary patch
length exactly. Section 5 and equation (14) count $HK(J+1)$ evaluations,
including construction of the final patch path. Section 2 explicitly
places every backward-carrier clip before its gate. Section 1 cites the
analytic-tail extension and states its role in permitting an
accuracy-dependent horizon coefficient.

These changes resolve every corrective qualification in Section 1 above.
The reconstructed exact-real short-program theorem is validated at this
version, conditional on its explicitly inherited good-event inputs.
Its $C\log(en)^8$ initialized-call bound and all-time, whole-sphere
numerical approximation hold as stated. This verification does not change
the unresolved compact-initialization, law-identification or total-bit
claims recorded in Sections 6–7.
