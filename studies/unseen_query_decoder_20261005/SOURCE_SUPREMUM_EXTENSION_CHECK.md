# Independent reconstruction of the source-supremum extension

2026-10-06. Scoped mathematical audit of the complete frozen
`SOURCE_SUPREMUM_EXTENSION.md`. No candidate edits, experiments,
external-source import, promotion, or Git operation.

**Verdict:** the stated finite-horizon, whole-sphere scalar response
theorem passes this reconstruction under its explicitly inherited source
and dense good-pair events. No additional passive-query backward estimate,
history-covariance gap, or interpolating good parameter path is needed.
The displayed logarithmic exponent $2+d/4$ is correct for the chosen
ambient sphere cover. The theorem remains a bound for the raw divergence
defect, not a compact computation of its derivative trace or a proof of
the full decoder.

The conclusion concerns $s,t\leq T=32(m/\gamma)\log(en)$. It makes
no fitted-endpoint derivative assertion. The final observation about
growing Taylor truncation orders applies to partial sums of these same
analytically normalized source expansions; it does not independently
validate a different growing training program.

## 1. Frozen inputs and audit boundary

Candidate SHA-256:

`8623e2d8adaf3b730274dd704fcbd44533a67fe67d47e18ce38701b7d6cb6a6f`

The complete additional integrated sources were read:

- `UNBOUNDED_COMPRESSOR_BRIDGE.md`, SHA-256
  `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.
- `ANALYTIC_TAIL_EXTENSION.md`, SHA-256
  `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349`.

The standing authorized dense source is
`GENERAL_DENSE_COMPARISON.md`, SHA-256
`ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`;
its complete contents and good-pair specialization had already been
read and checked. The response-extension/divergence lemma was reconstructed
independently in the preceding assigned audit. Its current note hash is
`fc5aeaaf56dc9c4e55f71eb40e81ed6fcede8c21f1eab715617654e60d66deea`.

No linked earlier study, other route note, or archived book material was
opened. The integrated source's Gaussian insertion theorem is an inherited
input, not independently proved in this check. The all-time analytic-tail
note was read completely as authorized, but no late-time derivative-trace
claim is required by the candidate's proof.

## 2. The common complex domain is supplied by the source

Write $\ell_n=\log(en)$, and let $\mathcal E_n$ be the intersection of the
source and real-comparison good events. For the unchanged fixed problem,
$\mathbb P(\mathcal E_n^c)=o(1)$. The source's equations (23), (30)–(32)
supply, on this same event:

\[
 r_t=c_t\ell_n^{-1/2},\qquad r_x=c_x\ell_n^{-1/2},
\]

a complex time rectangle around $[0,T]$, the intrinsic complex sphere
tube, a holomorphic neighborhood of their closed product, fixed operator
and RMS bounds, and preactivation imaginary parts at most $a/4$.
Here $a$ is the activation strip width and $c_t,c_x>0$ are fixed-problem
constants. Crucially, source (23) bounds the actual **complex training**
carriers by $C\sqrt{\ell_n}$ on the time rectangle. Its scope is not
limited to real time. The source's stopping and continuation argument
retains that maximum when the full event is concluded.

Source (31) also supplies $\|r\|_2/\sqrt m\leq2Y$ along the short
complex paths from real anchors. Every point needed by a shrunken patch
is reached by the same deterministic choice of anchor and contour for
all roots, with total contour length at most $2r_t$.

The theorem retains the existing intersection of source, dense-fitting,
and compact-fitting label allowances. No inference that a weaker label
allowance implies the source event is made or needed.

## 3. Complex root Lipschitz control from two actual good paths

For two parameter states define their distance by

\[
 D=\|A-\widetilde A\|_F/\sqrt n
     +\sum_{j=2}^L\|W^{(j)}-\widetilde W^{(j)}\|_F
     +\|w-\widetilde w\|_2/\sqrt n.
\]

At real anchors the inherited good-pair comparison gives

\[
 D\leq Cn^{-1/2}e^{C\sqrt{\ell_n}}\|G-\widetilde G\|_2.
\tag{A}
\]

The following comparison applies directly to the two actual complex
states on $\mathcal E_n$. In a forward layer,

\[
 W h-\widetilde W\widetilde h
   =(W-\widetilde W)\widetilde h
           +W(h-\widetilde h).
\]

The first term is controlled by the Frobenius parameter difference and
reference feature RMS; the second by the operator cap and the lower
feature difference. Both scalar preactivations lie in the safe strip.
Their straight scalar segment also lies there, so integrating $\phi'$
along that segment bounds the activation difference. Induction therefore
gives feature and preactivation RMS differences at most $CD$.

For a training backward layer, split

\[
 \phi'(z)\odot k-\phi'(\widetilde z)\odot\widetilde k
   =[\phi'(z)-\phi'(\widetilde z)]\odot\widetilde k
       +\phi'(z)\odot(k-\widetilde k).
\]

The first term has RMS at most $C\sqrt{\ell_n}D$, using the bounded
second derivative and the reference training-carrier maximum. Splitting
$W^T\delta-\widetilde W^T\widetilde\delta$ controls the second
term by a parameter difference times a fixed response RMS, plus the
upper backward difference times a fixed operator bound. At the top,
the carrier difference is the readout difference. Thus downward
induction gives

\[
 \|\delta-\widetilde\delta\|_2/\sqrt n
       \leq C(1+\sqrt{\ell_n})D.
\tag{B}
\]

The changed-gate contributions are added over the fixed depth. No
additional power of $\sqrt{\ell_n}$ is multiplied at each layer.

Prediction and normalized residual differences are at most $CD$.
Subtracting each rank-one parameter velocity, using the complex residual
bound $2Y$, gives

\[
 \|F(\theta)-F(\widetilde\theta)\|_{\mathrm{par}}
        \leq C(1+\sqrt{\ell_n})D.
\tag{C}
\]

The complex rank-one identity
$\|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)$ and the
normalizations of the first and readout blocks give exactly this norm.
Complex transposes cause no change in operator norms. All subtractions
use endpoint bounds on two actual states. They never evaluate the
network on the straight segment between its parameter states.

Parametrize the common short complex contour by arc length. Its tangent
has modulus one, so the integral inequality from (C) has the same
coefficient as an ordinary real-parameter Gronwall inequality. The factor
is at most

\[
 \exp\{2Cr_t(1+\sqrt{\ell_n})\}=O_{\rm problem}(1).
\]

This proves (A) throughout the required complex time domain.

For a complex query, its norm is at most two and both forward
preactivation sequences remain in the safe strip. The same forward
subtraction yields unnormalized query-feature Lipschitz constant
$Ce^{C\sqrt{\ell_n}}$. Training features and readout obey that bound;
training backward fields obey it with the additional factor
$1+\sqrt{\ell_n}$ from (B). Their vector norms are at most $B\sqrt n$
with fixed $B$.

Initialized matrix images also have these bounds. Indeed

\[
 W_0u-\widetilde W_0\widetilde u
       =W_0(u-\widetilde u)
           +(W_0-\widetilde W_0)\widetilde u,
\]

and the second term is at most
$\|G-\widetilde G\|_2\|\widetilde u\|_2/\sqrt n
\leq B\|G-\widetilde G\|_2$. The first term uses the initialized
operator bound. The same calculation applies to a transposed initialized
image. None of these arguments requires a passive-query backward
coordinate maximum.

## 4. Holomorphic charts and the number of patches

For real unit $u$, let the columns of $V$ form a real orthonormal tangent
frame. The candidate chart is

\[
 v_u(z)=(u+Vz)(1+z^Tz)^{-1/2}.
\]

If $\|z\|_2\leq1/4$, then $|z^Tz|\leq1/16$. The square-root
branch is holomorphic, the derivative is bounded by an absolute
constant, and $v_u(z)^Tv_u(z)=1$. On a polydisk of radius
$\rho=c r_x/\sqrt d$, choose the numerical $c$ small enough. Its
image has norm at most two. Also $v_u(\operatorname{Re}z)$ is real,
so integration along the imaginary segment gives

\[
 \|\operatorname{Im}v_u(z)\|_2
 \leq C\|\operatorname{Im}z\|_2
 \leq C\sqrt{d-1}\rho\leq r_x\leq\sinh r_x.
\]

Thus the entire outer polydisk maps into the supplied intrinsic tube.

Choose a sphere net with ambient Euclidean mesh $\rho/8$. Disjoint
ambient balls give at most $(1+C/\rho)^d\leq C_d r_x^{-d}$ points.
If a real unit $v$ is close to its center $u$, then
$u^Tv=1-\|u-v\|^2/2$ is bounded below and its chart coordinate is
$z=V^Tv/(u^Tv)$. It lies in the smaller chart polydisk. Hence these
smaller neighborhoods cover the sphere. For $d=1$, the two real points
need no chart coordinate and satisfy the stated looser bound as well.

Outer time disks of a fixed fraction of $r_t$ centered in $[0,T]$
fit in the source rectangle, including at its endpoints. Their
half-radius disks cover $[0,T]$ with $C(1+T/r_t)$ centers. For two
independent time variables and the sphere charts, the number of patches
is at most

\[
 N_n\leq C(1+T/r_t)^2r_x^{-d}
      \leq C\ell_n^{3+d/2}.
\tag{D}
\]

The ambient $d$ in this bound is deliberate. A sharper intrinsic cover
is unnecessary to prove the candidate's exponent.

## 5. Coefficientwise extension preserves the required root derivatives

On each product patch there are $k=d+1$ complex coordinates: two times
and $d-1$ query-chart variables. Expand each vector source in a Taylor
series and multiply each coefficient by its outer multi-radius power.
Cauchy's formula expresses every such coefficient as an average of
source values on the outer torus, multiplied by a unit-modulus factor.
The same formula for a difference of two roots shows that every weighted
coefficient has

\[
 \|u_\alpha(G)\|_2\leq B\sqrt n,
 \quad
 \|u_\alpha(G)-u_\alpha(\widetilde G)\|_2
     \leq A_n\|G-\widetilde G\|_2,
\]

\[
 A_n=C(1+\sqrt{\ell_n})e^{C\sqrt{\ell_n}}.
\tag{E}
\]

The bound is independent of coefficient order. Variables unused by a
source have zero original coefficients.

Extend every vector coefficient separately from $\mathcal E_n$, regarding
$\mathbb C^n$ as $\mathbb R^{2n}$, and project onto its radius
$B\sqrt n$ ball. The vector extension lemma preserves (E). Its
Jacobian has real rank at most $2n$, giving
$\|D_Gu_\alpha\|_{\rm HS}^2\leq2nA_n^2$ almost everywhere.
Extending the tensor product directly as an $n^2$-component vector
would not give this dimension count; the candidate correctly extends
the two vector factors separately.

For each pair of extended coefficients $C_\alpha,H_\beta$, define
$U_{ij}=C_{\alpha,i}H_{\beta,j}/n^{3/2}$. The complex version of
the Gaussian divergence identity is obtained by conjugating the
second factor in its second moment, or by applying its real version
to real and imaginary parts. It gives

\[
 \mathbb E|\delta(U)|^2
       \leq\mathbb E\|U\|_2^2
                 +\mathbb E\|D_MU\|_{\rm HS}^2
       \leq\frac{B^4+8B^2A_n^2}{n}.
\tag{F}
\]

This confirms the harmless complex-dimension constant in the
candidate's $CB(B+A_n)/\sqrt n$ bound.

For a good root, the actual finite-dimensional ODE and forward maps
have smooth dependence on nearby real initial conditions throughout a
safe compact complex patch. This follows from local analytic dependence
and the positive strip/state margins, applied on a finite cover of that
compact domain. No uniform lower bound on the size of this root
neighborhood is required. Differentiation of a coefficient under its
finite Cauchy contour is therefore legitimate. Its root derivative is
the corresponding coefficient of the total root derivative of the
actual source.

Weak derivative locality identifies each extended coefficient's root
derivative with this original one almost everywhere on $\mathcal E_n$. There
are only countably many coefficients, matrix-coordinate derivatives,
and coefficient pairs at each width, and finitely many patches. Their
exceptional sets have one common null union. The resulting coefficient
identities therefore hold simultaneously, not merely separately at
each real time or query.

## 6. The supremum bound and its logarithmic exponent

On a smaller patch every normalized variable has modulus at most
$1/2$. Bilinearity of the matrix pairing and of the total derivative
of a product expands the raw defect into coefficient-pair divergences.
Define its auxiliary absolute envelope by

\[
 Z_j=\sum_{\alpha,\beta\in\mathbb N^k}
        2^{-|\alpha|-|\beta|}\,
               |\delta(U_{j,\alpha,\beta})|.
\]

Using (F) and Minkowski gives

\[
 \|Z_j\|_{L^2}
       \leq\frac{CB(B+A_n)}{\sqrt n}
           \left(\sum_{\alpha\in\mathbb N^k}
                         2^{-|\alpha|}\right)^2
       =\frac{CB(B+A_n)}{\sqrt n}\,2^{2k}.
\tag{G}
\]

The sum of these weighted $L^2$ norms is finite. In particular the
absolute series is finite almost surely, converges uniformly on the
smaller closed polydisk, and its tails tend to zero in the supremum
$L^2$ norm. On $\mathcal E_n$ outside the common null set, its non-absolute
series is the actual analytic defect, because both value and root
derivative coefficients agree. This justifies summing before taking
the supremum over the continuum of real times and queries.

There is no need for independence between patches or coefficients.
Pointwise $\max_j Z_j^2\leq\sum_j Z_j^2$, so (D) and (G) imply

\[
 \mathbb P\left\{\mathcal E_n\cap
       \left[\sup_{s,t\leq T,\,v\in S^{d-1}}|E_n(s,t,v)|
           >\frac{C\sqrt{N_n}\,B(B+A_n)}{\sqrt{n\delta}}
       \right]\right\}\leq\delta.
\]

Here $E_n(s,t,v)$ is the scalar defect defined in candidate (1).
Since $B$ is fixed and
$1+\sqrt{\ell_n}\leq2\sqrt{\ell_n}$,

\[
 \sqrt{N_n}\,B(B+A_n)
 \leq C\ell_n^{3/2+d/4}\sqrt{\ell_n}
                          e^{C\sqrt{\ell_n}}
 =C\ell_n^{2+d/4}e^{C\sqrt{\ell_n}}.
\]

Adding the inherited good-event failure proves exactly the claimed
$1-\delta-o(1)$ guarantee. No new probability cost is introduced by
the coefficientwise localization. The same envelope controls Taylor
partial sums at any order on the smaller patches; this is the precise
scope of the growing-order observation.

## 7. Disposition and remaining distinction

No mathematical correction is required for the frozen candidate's
theorem. The actual two-state complex comparison, the countable root
derivative locality, and the analytic cover each supply the necessary
bridge rather than assuming it.

This closes the previously conditional supremum transfer for the
specified training and forward-query source pairs. It does not provide
an algorithm for their total response traces, a controlled law for
arbitrary adaptive Stein test fields, a stable growing covariance
factorization, or an autonomous compact decoder. The theorem's scope
excludes passive-query backward vectors and fitted-endpoint derivative
traces; the proof respects both exclusions.

Previously read rigorous-math and conjecture-audit instructions were
applied. The canonical-notation skill remained unavailable under the
reported permission denial; the maintained notation contract and the
supplied presentation requirements were used directly.
