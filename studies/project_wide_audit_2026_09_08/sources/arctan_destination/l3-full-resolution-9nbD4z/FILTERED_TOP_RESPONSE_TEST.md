# Filtered top response: one structural elimination test

Status: **NO_CANONICAL_PROGRESS. Unverified candidate pending independent review.**

The single test is to eliminate the learned top matrix and the readout
before taking responses, and then ask whether supplied-middle-path top
stability controls the response returned through the actual middle path.
It does not close this argument. The exact response contains that returned
path in both orientations of the learned memory. In the frozen-coefficient
formalism, the same issue is an additional causal response operator inside
the top resolvent, not an additional bounded external input. No bound for
that resolvent, its expected coefficients, or the resulting middle-query
tails on every finite feature horizon is proved here.

This is a failure of the tested inference, not a counterexample to the
canonical theorem. The local response bootstrap is accepted at its stated
conditional scope and is not extended or reproved. Neither rank nor the
fixed-clipping stability bridge is reproved. The interacting-oracle
distribution reduction is not tested or assumed proved here.

The required skill and the following three files were read in full. Their
SHA-256 hashes at the time of reading were:

- `CAUSAL_FILTERED_QUERY_RANK.md`:
  `7406ffb9c24e8359e7e188c70eb3863ff5aeb9179df3d7bba92103b98aedcfd1`.
- `FILTERED_QUERY_CLIPPED_STABILITY.md`:
  `cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b`.
- `LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md`:
  `2a999c88df03e0344fe53f58c9d73e8ae4c6b4b79a860b531700060444fdbf47`.

`INTEGRATED_INITIAL_QUERY_COMPRESSION.md` was also read in full to check
the memory conventions. No experiments, external source theorems, agents,
or repository edits were used. Only this candidate file was written.

## 1. Exact finite filtered response, with the readout retained

Use the recursion (17)--(22a) of the rank note. Write
\(p=\eta/\varepsilon\in(0,1]\), \(T=N\eta\), and
\(c=\pi/2\). All finite vectors have ordinary Euclidean norms;
normalizing factors are displayed. Finite transposes are \(T\).
Any population adjoint would be denoted by \(*\); no population operator
is constructed in this note.

The canonical seeds remain mutually independent, with independent entries
\[
 z^{(1)}_{0,i}\sim N(0,1),\qquad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\qquad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).                         \tag{1}
\]
Here \(W^{(4)}\) is the rescaled readout. The activation is arctangent,
\(h^{(\ell)}=\phi(z^{(\ell)})\), and
\(\phi'(z)=1/(1+z^2)\). The target is 1, the output is
\((W^{(4)})^Th^{(3)}/n\), and the feature clock for the intended
canonical flow is \(ds/dt=-2(f_n-1)\). No residual is included in any
\(\delta^{(\ell)}\). The filtered registers, including their noisy
warmups, are not identified with the exact canonical forward constraints.

At update index \(j\), let \(e_{F,j}^{(3)},e_{T,j}^{(3)}\) be the actual
raw upper oracle errors, including the Gamma terms. Eliminating the top
memory gives exact finite identities
\[
\begin{split}
 W^{(4)}_j&=W^{(4)}_0+\eta\sum_{v<j}h^{(3)}_v,\\
 \delta^{(3)}_j&=W^{(4)}_j\odot\phi'(z^{(3)}_j),\\
 W^{(3)}_j&=W^{(3)}_0+
       \frac\eta n\sum_{r<j}\delta^{(3)}_r(h^{(2)}_r)^T,\\
 z^{(3)}_{j+1}&=(1-p)z^{(3)}_j+p\left[
       W^{(3)}_0h^{(2)}_j+e_{F,j}^{(3)}
       +\eta\sum_{r<j}\delta^{(3)}_r
                      \frac{(h^{(2)}_r)^Th^{(2)}_j}{n}\right],\\
 q^{(2)}_j&=(W^{(3)}_0)^T\delta^{(3)}_j+e_{T,j}^{(3)}
       +\eta\sum_{r<j}h^{(2)}_r
                      \frac{(\delta^{(3)}_r)^T\delta^{(3)}_j}{n}.
\end{split}                                                    \tag{2}
\]
All indices are pre-step; in particular no \(r=j\) matrix update is used.
Equations involving a current oracle output use \(0\le j<N\); the
state and memory identities also hold at \(j=N\).

For differentiation, take a \(C^1\) clipping with
\(|\tau_R|\le\min(|\cdot|,R)\), \(|\tau_R'|\le1\), as in the
local audit. A claim about formal derivatives needs this qualification;
the rank note itself permits nondifferentiable contractions. Fix the
initial seeds and Gamma arrays. Let \(D\) be differentiation in a specified
direction of the direct oracle inputs, through the whole finite recursion.
All induced changes of past queries and oracle errors are included.
Regularized Cholesky factors are smooth, so these derivatives exist for
the stated finite smooth program. This finite pathwise derivative is not
being equated with a scalar Gaussian representation coefficient.

Put \(u_j=Dz^{(3)}_j\). Direct differentiation of the first two lines of
(2), holding \(W^{(4)}_0\) fixed, yields the exact response
\[
 D\delta^{(3)}_j
 =W^{(4)}_j\odot\phi''(z^{(3)}_j)\odot u_j
 +\eta\phi'(z^{(3)}_j)\odot
       \sum_{v<j}\phi'(z^{(3)}_v)\odot u_v.               \tag{3}
\]
The second term is essential: it is the derivative of the learned
readout. In particular the top derivative is not just a bounded diagonal
multiplier acting on the current \(u_j\).

Differentiating the last two lines of (2) gives
\[
 u_{j+1}=(1-p)u_j+p\left[
  \eta\sum_{r<j}(D\delta^{(3)}_r)
                  \frac{(h^{(2)}_r)^Th^{(2)}_j}{n}
  +\mathfrak f_j\right],                                \tag{4}
\]
where the actual forcing is
\[
 \mathfrak f_j=W^{(3)}_jDh^{(2)}_j+De_{F,j}^{(3)}
   +\eta\sum_{r<j}\delta^{(3)}_r
                    \frac{(Dh^{(2)}_r)^Th^{(2)}_j}{n},    \tag{5}
\]
and
\[
\begin{split}
 Dq^{(2)}_j={}&(W^{(3)}_j)^TD\delta^{(3)}_j+De_{T,j}^{(3)}\\
 &+\eta\sum_{r<j}(Dh^{(2)}_r)
                    \frac{(\delta^{(3)}_r)^T\delta^{(3)}_j}{n}\\
 &+\eta\sum_{r<j}h^{(2)}_r
                    \frac{(D\delta^{(3)}_r)^T\delta^{(3)}_j}{n}.
\end{split}                                                    \tag{6}
\]
For example, differentiating the forward learned-memory term produces
three summands. Differentiating its current \(h^{(2)}_j\) combines with
\(W^{(3)}_0Dh^{(2)}_j\) into \(W^{(3)}_jDh^{(2)}_j\);
differentiating its old \(h^{(2)}_r\) gives the last term of (5);
differentiating \(\delta^{(3)}_r\) gives the sum in (4).
In (6), the derivative of the current \(\delta^{(3)}_j\) similarly
combines into the trained transpose. Thus neither orientation of the
old learned memory has been discarded.

To see precisely the input required by supplied-middle-path stability,
set
\(B=\|W^{(4)}_0\|_\infty+cT\) and
\(L=\|W^{(3)}_0\|_{\rm op}+cBT\).
The identities (2) give \(|\delta^{(3)}_{j,i}|\le B\) and
\(\|W^{(3)}_j\|_{\rm op}\le L\). Cauchy--Schwarz applied to (5) gives
\[
 \frac{\|\mathfrak f_j\|_2}{\sqrt n}
 \le L\frac{\|Dh^{(2)}_j\|_2}{\sqrt n}
    +cB\eta\sum_{r<j}\frac{\|Dh^{(2)}_r\|_2}{\sqrt n}
    +\frac{\|De_{F,j}^{(3)}\|_2}{\sqrt n}.                \tag{7}
\]
This identifies the missing input rather than estimating it. A bound on
the supplied activation \(|h^{(2)}|\le c\) is not a bound on
\(Dh^{(2)}\). Applying an input-response bound for (3)--(4) to (7)
therefore leaves the actual middle response to be controlled.

The actual oracle errors in these equations are not frozen. For example,
at upper call \(l=j+2\), the rank note gives exactly
\[
\begin{split}
 De_{T,j}^{(3)}
 &=\sum_{i<l}\left[
  (Ds_i)(\Gamma^TA_\theta)_{il}
   +s_i(\Gamma^TDA_\theta)_{il}\right]+\sigma DU_l,\\
 De_{F,j}^{(3)}
 &=\sum_{i\le l}\left[
  (Dt_i)(\Gamma A_\omega)_{il}
   +t_i(\Gamma DA_\omega)_{il}\right]+\sigma DV_l.
\end{split}                                                    \tag{8}
\]
All arrays here are leading \(l\)-prefixes. Differentiating
\(A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I\) and
\(A_\omega^TA_\omega=\Omega^T\Omega/n+\sigma^2I\) specifies their
upper-triangular derivatives by
\[
\begin{split}
 (DA_\theta)^TA_\theta+A_\theta^TDA_\theta
     &=(D\Theta)^T\Theta+\Theta^TD\Theta,\\
 (DA_\omega)^TA_\omega+A_\omega^TDA_\omega
     &=((D\Omega)^T\Omega+\Omega^TD\Omega)/n.
\end{split}
\]
The derivatives of \(t_i=(\Theta A_\theta^{-1})_i\) and
\(s_i=(\Omega A_\omega^{-1})_i/\sqrt n\) include the inverse-factor
derivative \(D(A^{-1})=-A^{-1}(DA)A^{-1}\). The lower oracle has the
same formulas with its own histories. Bounds on raw errors do not bound
(8). No estimate for (8) is claimed, and no oracle distribution identity
is inferred by differentiating a state-error bound.

## 2. The middle response in (5) retains the full lower feedback

Let \(x^{(1)}=F(z^{(1)})\), \(F(z)=z+z^3/3\). With all initial seeds
fixed, differentiating the actual remaining registers gives
\[
\begin{split}
 Dh^{(1)}_j&=\phi'(z^{(1)}_j)^2\odot Dx^{(1)}_j,\\
 Dh^{(2)}_j&=\phi'(z^{(2)}_j)\odot Dz^{(2)}_j,\\
 D\delta^{(2)}_j
 &=\phi''(z^{(2)}_j)\odot\tau_R(q^{(2)}_j)\odot Dz^{(2)}_j\\
 &\quad+\phi'(z^{(2)}_j)\odot\tau_R'(q^{(2)}_j)\odot Dq^{(2)}_j,\\
 Da^{(2)}_{j+1}&=Da^{(2)}_j+\eta D\delta^{(2)}_j,\\
 DM^{(2)}_{j+1}&=DM^{(2)}_j+
  \frac\eta n\left[(D\delta^{(2)}_j)(h^{(1)}_j)^T
                    +\delta^{(2)}_j(Dh^{(1)}_j)^T\right],\\
 DR^{(1)}_{j+1}&=DR^{(1)}_j+
  \eta\left[(DM^{(2)}_j)^T\delta^{(2)}_j
                      +(M^{(2)}_j)^TD\delta^{(2)}_j\right],\\
 Dx^{(1)}_{j+1}&=(1-p)Dx^{(1)}_j
      +p\left[(W^{(2)}_0)^TDa^{(2)}_j+DR^{(1)}_j+De_{T,j}^{(2)}\right],\\
 Dz^{(2)}_{j+1}&=(1-p)Dz^{(2)}_j
      +p\left[W^{(2)}_jDh^{(1)}_j
                    +(DM^{(2)}_j)h^{(1)}_j+De_{F,j}^{(2)}\right].
\end{split}                                                    \tag{9}
\]
Initially \(Dx^{(1)}_0,Da^{(2)}_0,DM^{(2)}_0,DM^{(3)}_0,DR^{(1)}_0\)
and \(DW^{(4)}_0\) are zero. The exact warmup responses are
\[
 Dz^{(2)}_0=\sigma DV^{(2)}_1,\qquad
 Dz^{(3)}_0=W^{(3)}_0\bigl[\phi'(z^{(2)}_0)\odot Dz^{(2)}_0\bigr]
                         +\sigma DV^{(3)}_1.
\]
In particular the response of the returned lower memory is its full
pre-step derivative, not zero at a later restart. Equations (3)--(9),
with these warmups, form an exact finite variational system. They show
where the top input in (7) is generated.

The retained middle multiplier is
\[
 \phi''(z^{(2)}_j)\odot\tau_R(q^{(2)}_j)\odot Dz^{(2)}_j. \tag{10}
\]
Bounding it by \(2R\|Dz^{(2)}_j\|_2/\sqrt n\) yields a fixed-clipping
estimate; replacing \(R\) with the Euclidean size of \(q^{(2)}_j\)
is not a valid multiplier estimate. This note does not repeat that
already known obstruction as a new result. Its role here is to locate
the response entering both terms involving \(Dh^{(2)}\) in (5).
The special top identities did not remove that input.

## 3. The same test in the frozen-coefficient response convention

This section is conditional algebra, not a distribution reduction.
Grant a finite scalar Gaussian/response description with the convention
of the local audit: deterministic response and covariance coefficients
are held fixed during source differentiation. We derive what the top
filter does to that description. We do not assert that the particular
regularized two-oracle program has the following exact representation;
any additional terms in its eventual representation must also be kept.
The gap identified below remains even in the displayed granted form.
The deterministic coefficients in this granted finite program are
assumed finite; this is not an assertion that they have already been
constructed uniformly on all feature horizons.

Use canonical notation \(z^{(3)},W^{(4)},h^{(2)},h^{(3)}\) also for the
scalar coordinates in this paragraph. They are scalar random variables,
not finite vectors. Write \(\xi^{(3)}_{\mathrm w}\) for the warmup top
forward source, \(\xi^{(3)}_i\) for the forward source at update \(i\),
and \(\zeta^{(2)}_r\) for the middle reverse source. Set
\(h^{(2)}_{\mathrm w}=h^{(2)}_0\). The warmup source has its own formal
coordinate even when its covariance is singular with another source.

In the audit's formal query description the raw upper forward target,
including the trained memory, has the form
\[
 \xi^{(3)}_i+
 \sum_{r<i}\left(\mathcal R_{ir}+\eta\kappa_{ir}\right)
                                      \delta^{(3)}_r,
 \quad
 \mathcal R_{ir}=\mathbb E\frac{\partial h^{(2)}_i}
                                      {\partial\zeta^{(2)}_r},
 \quad
 \kappa_{ir}=\mathbb E[h^{(2)}_ih^{(2)}_r].               \tag{11}
\]
Thus \(\mathcal R\) is the returned formal middle response, not the
learned covariance \(\eta\kappa\). It is not removed by holding the
deterministic coefficients fixed. That convention fixes its value in
the derivative; it does not set the coefficient to zero. The strict
inequality \(r<i\) follows from pre-step query selection; extra zero
coefficients caused by lower filter delays are allowed.

For \(0\le j\le N\), define the filter weights
\[
 P_{j\mathrm w}=(1-p)^j,\qquad
 P_{ji}=\begin{cases}
 p(1-p)^{j-1-i},&0\le i<j,\\
 0,&j\le i<N.
 \end{cases}                                             \tag{12}
\]
At \(p=1\), exponent zero is interpreted as 1. Every row of \(P\)
sums to 1, including row zero. Iterating the top filter exactly gives
\[
 z^{(3)}_j=(P\xi^{(3)})_j+
       \sum_r\bigl(A^{\rm learn}_{jr}+A^{\rm resp}_{jr}\bigr)
                                                  \delta^{(3)}_r,
                                                               \tag{13}
\]
where
\[
 A^{\rm learn}_{jr}=\eta\sum_{r<i<j}P_{ji}\kappa_{ir},
 \qquad
 A^{\rm resp}_{jr}=\sum_{r<i<j}P_{ji}\mathcal R_{ir}.      \tag{14}
\]
Both matrices have row and column indices \(0,\ldots,N\), with empty
sums set to zero, and are strictly lower triangular. The learned part satisfies
\(|A^{\rm learn}_{jr}|\le\eta c^2\), since \(|\kappa_{ir}|\le c^2\)
and the filter weights have total mass at most 1. For the other part
the actual conclusion is only
\[
 \sum_r|A^{\rm resp}_{jr}|
 \le\sum_{i<j}P_{ji}\sum_{r<i}|\mathcal R_{ir}|.          \tag{15}
\]
The filter averages the unknown response row. It supplies no factor
\(\eta\) for that row and no bound for its size. In particular, summing
the factor \(p\) over the filter window gives mass up to 1, not a
vanishing forcing amplitude.

Define the source-response matrices, with the coefficients in (11)
held fixed,
\[
 J_{jv}=\frac{\partial z^{(3)}_j}{\partial\xi^{(3)}_v},
 \qquad H_{jv}=\frac{\partial\delta^{(3)}_j}{\partial\xi^{(3)}_v},
 \quad v\in\{\mathrm w,0,\ldots,N-1\}.
\]
Keep \(W^{(4)}_0\) as the prescribed independent initial seed, not zero.
For a scalar temporal vector \(u\), define the random lower-triangular
linear map
\[
 (\mathcal L u)_j
 =W^{(4)}_j\phi''(z^{(3)}_j)u_j
   +\eta\phi'(z^{(3)}_j)
               \sum_{v<j}\phi'(z^{(3)}_v)u_v.            \tag{16}
\]
This is exactly (3), now on scalar temporal coordinates. Equations
(13) and (16) imply
\[
 J=P+(A^{\rm learn}+A^{\rm resp})H,\qquad H=\mathcal L J. \tag{17}
\]
No Gaussian integration by parts or differentiation of a covariance
square root is used in (17).

To isolate precisely what supplied-middle-path top control could give,
write
\[
 \mathcal K=(I-\mathcal L A^{\rm learn})^{-1}\mathcal L.
\]
The inverse exists for this finite program: its subtracted matrix is
strictly lower triangular, so the inverse is the terminating sum of its
powers. Rearranging (17) gives the exact identities
\[
 H=\mathcal K P+\mathcal K A^{\rm resp}H,
 \qquad
 H=(I-\mathcal K A^{\rm resp})^{-1}\mathcal K P.           \tag{18}
\]
The second inverse is also a terminating finite sum. This establishes
finite algebraic solvability, not any bound uniform in mesh or clipping.
Even granting all-horizon control of the learned-memory top map
\(\mathcal K\), the additional operator
\(\mathcal K A^{\rm resp}\) remains inside the inverse. Treating it as
a prescribed bounded source, or deleting it because the middle path is
bounded, changes (18). This is the precise failure of the tested
supplied-path inference for the formal response.

The canonical identity for the readout has already been fully used in
(16). It does not cancel the second term in (18). For example, its
off-diagonal entries include
\(\eta\phi'(z^{(3)}_j)\phi'(z^{(3)}_v)>0\); the readout derivative
is a returned history, not a negative diagonal correction. Nor is
\(W^{(4)}\phi''(z^{(3)})\) always nonpositive under the stated finite
initialization: \(\phi''(z)=-2z/(1+z^2)^2\), and at warmup
\(W^{(4)}_{0,i}\) is independent of the nonzero almost-surely
\(z^{(3)}_{0,i}\), so their signs disagree with probability \(1/2\).
This sign check does not assert significant growth or failure in the
limit; the initial readout is tiny. It only rules out using an
unproved pointwise negative-sign premise for this elimination.

There is no restart reset in (18). Splitting at a later index retains
the old columns of \(H\), the learned readout in (16), and the old
columns of both matrices in (14). Finite causality alone does not bound
their accumulated coefficients independently of the number of steps.

## 4. Exact missing estimate and the resulting classification

In the same granted scalar description, for \(0\le j<N\) the middle
transpose query is
\[
\begin{split}
 q^{(2)}_j={}&\zeta^{(2)}_j
       +\sum_{v\in\{\mathrm w,0,\ldots,j-1\}}
                        (\mathbb E H_{jv})h^{(2)}_v\\
 &+\eta\sum_{r<j}
          \mathbb E[\delta^{(3)}_j\delta^{(3)}_r]h^{(2)}_r.
\end{split}                                                    \tag{19}
\]
For this pre-step filtered program, the current forward source
\(\xi^{(3)}_j\) has not entered \(\delta^{(3)}_j\); its coefficient
is zero. The warmup coefficient is retained even though it multiplies
the repeated activation \(h^{(2)}_0\). Formula (19) is conditional on
the specified formal description, not a new equality in distribution
for the finite oracle.

The readout identity does directly control the learned covariance part.
For the scalar seed with the variance in (1),
\[
 \bigl(\mathbb E|\delta^{(3)}_j|^2\bigr)^{1/2}
 \le \bigl(\mathbb E|W^{(4)}_0|^2\bigr)^{1/2}+cT
 =n^{-1}+cT.
\]
This uses \(|\delta^{(3)}_j|\le |W^{(4)}_0|+cT\) and the triangle
inequality in probability-space \(L^2\), without any independence after
reuse. Consequently the absolute value of the last line of (19) is at
most \(cT(n^{-1}+cT)^2\). This is the already available readout/learned
memory bound, not a new response estimate.

One sufficient missing estimate is
\[
 \sup_{j\eta\le T}\sum_{v\in\{\mathrm w,0,\ldots,j-1\}}
       |\mathbb E H_{jv}|\le C_T,                         \tag{20}
\]
with \(C_T<\infty\) for every finite \(T\), independent of clipping,
mesh, and filter scale in the prescribed regime. This demands the
response in (18), including \(A^{\rm resp}\). It is not a bound for
\(\mathcal K P\) alone. The middle derivatives defining
\(\mathcal R\) also have to be those of the full program; replacing
the lower memories in (9) by a supplied path is not that derivative.

For clarity about the strength of this obligation, suppose both (19)
and (20) held and its centered Gaussian source had variance at most
\((n^{-1}+cT)^2\), as in the audit's covariance prescription. Then
the entire non-Gaussian shift in (19) would have absolute value at most
\(cC_T+cT(n^{-1}+cT)^2\). The event that \(|q^{(2)}_j|\) exceeds
that value by \(x>0\) is contained in
\(\{|\zeta^{(2)}_j|>x\}\), and hence
\[
 \mathbb P\!\left(|q^{(2)}_j|>
          cC_T+cT(n^{-1}+cT)^2+x\right)
 \le 2\exp\!\left[-\frac{x^2}{2(n^{-1}+cT)^2}\right].     \tag{21}
\]
The Gaussian bound follows from its moment generating function and
Markov's inequality. This implication does not require independence of
the shift and the source, or independence across source times. It is
not a new proved tail bound: (20) is unproved. Any extra oracle source
variance or response terms in a different exact representation would
also need to be included before using (21).

The absolute row bound (20) is a sufficient target, not a claim that
absolute values are necessary. A signed estimate for the actual shift
in (19) could serve instead. This test proves neither. A mere quadratic
bound for that shift would still not supply the stronger uniform tails
needed by the stated continuation program.

The results established here are the finite identities (3)--(9) and,
conditional on the explicit frozen-coefficient program, the filter and
response identities (12)--(18) and the implication (20)--(21). They expose
the retained forcing exactly. No whole generated-space
\(L^\infty\!\to L^p\) or \(L^p\!\to L^p\) claim, fresh-noise
replacement, or independent reused-neuron assertion is used.

**NO_CANONICAL_PROGRESS:** supplied-middle-path top control does not
estimate the returned-middle operator in (18), and this test supplies
no new canonical coefficient, covariance, or tail bound for it. The
all-horizon response remains open. No conclusion about failure of the
canonical theorem follows. Exact uncut population/MF/GF/GD continuation,
including removal of the surrogate modifications, remains the goal.
This bounded test is complete; no follow-up route is started.
