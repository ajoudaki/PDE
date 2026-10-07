# Label expansion at zero readout: all-time coefficients and an analytic boundary

2026-10-06. Scoped theoretical route. No experiments or promotion.

The zero-label expansion has an all-time triangular structure: every fixed
residual coefficient decays exponentially times a polynomial in time, and
every fixed parameter coefficient converges at the fitted endpoint. The
coefficient recursion has linear nesting depth in the label order. These
facts are proved below for the actual deep-network gradient flow, without
restricting its data geometry or freezing hidden weights.

A quantitative complex-label disk also follows from a specified holomorphic
neighborhood of the initialized feature map. Its constants expose, rather
than remove, the missing width-uniform neighborhood. Finally, a fully explicit
Gaussian integral shows that strip holomorphy, finite Gaussian moments and
zero-readout parity alone do not imply any nonzero label Taylor radius. That
example is not a counterexample to deep-network gradient flow.

The original late-query decoder remains open. In particular, no smaller label
allowance is substituted for the full allowance in the assigned integrated
sources, and no conditional coefficient workspace estimate is called a
complete decoder memory bound.

## 1. Model and normalization

Use the architecture, loss and initialization of
`GENERAL_EXPLICIT_FITTING.md`: fixed depth $L\ge2$, sample count $m$, input
dimension $d$, inputs $v_a=x_a/\sqrt d\in S^{d-1}$, independent Gaussian first
weights and hidden matrices, and zero stored readout. Activations are real on
the real axis, holomorphic on a horizontal strip, with bounded derivative
on that strip. Values may have linear growth. The present finite-network
lemmas are deterministic conditional on an initialized training-feature
Gram with a positive gap. They do not change the iid initialization law.

Write the hidden parameters in their mobility-normalized coordinates as

\[
 u=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)})\in\mathbb R^P,
 \qquad a=W^{(L+1)}/\sqrt n\in\mathbb R^n,
 \qquad b=(y_1,\ldots,y_m)^T/\sqrt m.
\]

Here $P=nd+(L-1)n^2$; the Euclidean norm of $u$ is the direct-sum
Frobenius norm of its blocks. The temporary letter $a$ in this note is the
normalized readout, not a sample index. Define the training feature operator
and the query feature vector by

\[
 V(u)=\left[\frac{h^{(L)}(u,v_j)}{\sqrt{mn}}\right]_{j=1}^m,
 \qquad q_v(u)=\frac{h^{(L)}(u,v)}{\sqrt n}.
\]

Thus $V:\mathbb R^P\to\mathbb R^{n\times m}$,
$f_n(v)=a^Tq_v(u)$, and the normalized residual for labels $\zeta y$ is

\[
 e=V(u)^Ta-\zeta b,\qquad \|b\|_2=Y.
\]

For real $\zeta$, the loss is $\|e\|_2^2$. Its actual physical-time gradient
flow, with mobilities $(n,1,\ldots,1,n)$ in the original coordinates, becomes

\[
 \dot a=-2V(u)e,\qquad \dot u=-2J(u,a)e,
 \qquad u(0)=u_0,\quad a(0)=0,                     \tag{1}
\]

where $J(u,a):\mathbb R^m\to\mathbb R^P$ is defined by

\[
 h^TJ(u,a)c=a^TDV(u)[h]c
 \quad(h\in\mathbb R^P,\ c\in\mathbb R^m).
\]

The complexified system uses these same bilinear transposes, with no complex
conjugates in its vector field. Conjugates are used only for Euclidean norm
estimates. Differentiating the residual gives the exact equation

\[
 \dot e=-2K(u,a)e,\qquad
 K(u,a)=V(u)^TV(u)+J(u,a)^TJ(u,a).                 \tag{2}
\]

Set $V_0=V(u_0)$ and assume

\[
 K_0=V_0^TV_0\succeq gI_m\quad\text{for some }g>0. \tag{3}
\]

On the initialization event in the assigned fitting source, $g=\lambda/2$
is admissible, where $\lambda=\gamma/m$. No other history covariance gap is
required in the lemmas below.

## 2. Every fixed label order has an all-time endpoint

Taylor coefficients here include the factorial denominator:
$u_k(t)=[\zeta^k](u(t,\zeta)-u_0)$,
$a_k(t)=[\zeta^k]a(t,\zeta)$, and
$e_k(t)=[\zeta^k]e(t,\zeta)$. This section first defines them formally;
Section 3 identifies them with the derivatives of the actual trajectory.

**Proposition 1.** At every finite width satisfying (3), the formal
coefficients of (1) are uniquely defined on $[0,\infty)$. Hidden coefficients
of odd order and readout/residual coefficients of even order vanish. For
every integer $j\ge0$ there are finite constants, allowed to depend on the
initialized network and on $j$, such that

\[
 \|e_{2j+1}(t)\|_2\le C_j(1+t)^j e^{-2gt},       \tag{4}
\]

\[
 \sup_{t\ge0}\|a_{2j+1}(t)\|_2<\infty,
 \qquad \|\dot a_{2j+1}(t)\|_2
       \le C'_j(1+t)^j e^{-2gt}.                 \tag{5}
\]

For $j\ge1$,

\[
 \sup_{t\ge0}\|u_{2j}(t)\|_2<\infty,
 \qquad \|\dot u_{2j}(t)\|_2
       \le C''_j(1+t)^{j-1}e^{-2gt}.             \tag{6}
\]

Every nonzero parameter coefficient therefore has a finite endpoint. For
any fixed sphere query, its prediction coefficients also have finite
endpoints. At fixed finite width the last assertion is uniform on the query
sphere. There is no assertion that $C_j$ grows geometrically in $j$ uniformly
in width.

**Proof.** Equations (1) are invariant under
$(\zeta,a,e,u)\mapsto(-\zeta,-a,-e,u)$. Uniqueness of the triangular
coefficient construction below gives the asserted parity. Equivalently,
substitute an even hidden series and odd readout and residual series directly
into (1)–(2).

Write $V_p=[\zeta^p]V(u_0+\sum_{k\ge1}\zeta^ku_k)$ and define $J_p,K_p$
by the corresponding substitutions into (1)–(2). Explicitly, for $p\ge1$,

\[
 V_p=\sum_{r=1}^{p}\frac1{r!}
       \sum_{k_1+\cdots+k_r=p\atop k_i\ge1}
       D^rV(u_0)[u_{k_1},\ldots,u_{k_r}].        \tag{7}
\]

All odd $V_p$ and $K_p$ vanish; all even $J_p$ vanish, because $J$ is
linear in the odd readout. In particular $J_0=0$. The exact recurrences are

\[
 \dot u_k=-2\sum_{p+q=k\atop p,q\ge1}J_pe_q,
 \qquad
 \dot e_k=-2K_0e_k-2\sum_{p=1}^{k-1}K_pe_{k-p}, \tag{8}
\]

\[
 \dot a_k=-2V_0e_k-2\sum_{p=1}^{k-1}V_pe_{k-p}. \tag{9}
\]

The initial conditions are $u_k(0)=a_k(0)=0$,
$e_1(0)=-b$, and $e_k(0)=0$ for $k>1$. First compute $e_1,a_1$.
Then, for $j=1,2,\ldots$, compute $u_{2j}$ from already known lower-order
odd coefficients, form $V_{2j},K_{2j}$, compute $e_{2j+1}$, and finally
compute $a_{2j+1}$. This is triangular: $J_{2j-1}$ only uses readout
coefficients up to order $2j-1$ and hidden coefficients up to order $2j-2$.
Although $V_{2j}$ and $K_{2j}$ use $u_{2j}$, that coefficient was just
computed from lower orders.

At order one the formulas are explicit:

\[
 e_1(t)=-e^{-2K_0t}b,\qquad
 a_1(t)=V_0K_0^{-1}(I-e^{-2K_0t})b.             \tag{10}
\]

These prove (4)–(5) for $j=0$. The inverse is legitimate by (3), and
$\|e^{-2K_0t}\|_{\rm op}\le e^{-2gt}$ by diagonalizing the real symmetric
matrix $K_0$.

Inductively suppose the claimed bounds hold below the next order. Every
coefficient of $V$ and $J$ needed for $\dot u_{2j}$ is a finite polynomial
in bounded, previously obtained parameter coefficients, with fixed
derivatives of $V$ at $u_0$. It is therefore bounded in time. Every summand
in $\dot u_{2j}$ has an odd residual factor of order at most $2j-1$.
By (4), its norm is at most a constant times
$(1+t)^{j-1}e^{-2gt}$. This proves the derivative estimate (6); its
integral is finite, so $u_{2j}$ is bounded and converges.

Consequently $K_{2p}$ is bounded for $1\le p\le j$. The forcing of
$e_{2j+1}$ in (8) is bounded by
$C(1+t)^{j-1}e^{-2gt}$. Variation of constants gives

\[
 \|e_{2j+1}(t)\|_2
 \le C e^{-2gt}\int_0^t(1+s)^{j-1}\,ds
 \le (C/j)(1+t)^j e^{-2gt}.                    \tag{11}
\]

Equation (9) then proves (5); its derivative is integrable. This closes
the induction, with no horizon in the constants.

For the query coefficient use the finite Taylor expansion of
$a^Tq_v(u)$. Every term is a product of convergent parameter coefficients
and a derivative of $q_v$ at $u_0$. At finite width these derivatives are
continuous in $v$; the compact sphere makes their finitely many required
norms uniformly bounded. Products and sums therefore converge uniformly.
This proves the final assertion. It does not estimate those derivative
bounds uniformly as $n\to\infty$. $\square$

The mechanism in (11) is training-residual damping. It prevents an undamped
polynomial drift of the parameter coefficients. It does not control their
growth as the order tends to infinity.

## 3. A quantitative all-time complex-label theorem

The next lemma specifies the analytic neighborhood that a successful
population proof would need to replace by a width-uniform object.

**Proposition 2.** Suppose $V$ is holomorphic on the complex Euclidean ball
$\|u-u_0\|_2<R$ and, throughout that ball,

\[
 \|V(u)\|_{\rm op}\le M,\qquad
 \|DV(u)[h]\|_{\rm op}\le B\|h\|_2,\qquad M,B\ge1. \tag{12}
\]

Assume (3), and define the absolute label-radius bound

\[
 q_* =\min\left\{
       \frac{g\sqrt R}{\sqrt{8BM}},
       \frac{g^{3/2}}{8BM}\right\}.             \tag{13}
\]

For every complex $\zeta$ with $q=|\zeta|Y<q_*$, equations (1) have a
solution for all physical times, and

\[
 \|e(t)\|_2\le q e^{-gt},\qquad
 \|a(t)\|_2\le \frac{2Mq}{g},\qquad
 \|u(t)-u_0\|_2\le\frac{4BMq^2}{g^2}<R/2.     \tag{14}
\]

The entire path and its endpoint are holomorphic in $\zeta$ on
$|\zeta|<q_*/Y$ when $Y>0$, with bounds uniform in time. For $Y=0$ the
path is exactly stationary. If $q_v$ is holomorphic and uniformly bounded
on the same ball for all sphere queries, the assertion also holds for
$f_n(t,v)=a(t)^Tq_v(u(t))$, uniformly in time and in $v$.

**Proof.** From the definition of $J$ and (12),
$\|J(u,a)\|_{\rm op}\le B\|a\|_2$. For as long as
$\|K-K_0\|_{\rm op}<g/2$ and $u$ remains in its analytic ball,

\[
 \frac{d}{dt}\|e\|_2^2
 =-4\operatorname{Re}(e^*Ke)
 \le-2g\|e\|_2^2.
\]

Here $e^*$ is the conjugate transpose in the norm identity; the matrix
$K$ in the holomorphic vector field still uses ordinary transposes.
Consequently $\|e(t)\|_2\le q e^{-gt}$ and
$\int_0^\infty\|e\|_2\le q/g$ on the stopped interval. Integrating
(1) gives the other bounds in (14). Integration of (12) along the segment
from $u_0$ to $u$ gives
$\|V-V_0\|_{\rm op}\le B\|u-u_0\|_2$. Therefore

\[
 \begin{aligned}
 \|K-K_0\|_{\rm op}
 &\le 2MB\|u-u_0\|_2+B^2\|a\|_2^2\\
 &\le\frac{12B^2M^2q^2}{g^2}<\frac{3g}{16}.
 \end{aligned}                                                     \tag{15}
\]

The first entry in (13) gives $\|u-u_0\|_2<R/2$; the second gives the
strict improvement (15) of the kernel stop. The solution cannot reach
either boundary. In finite dimension it remains in a compact subset of
the vector field's domain, so it extends through every finite time.
Both parameter velocities are integrable by (14), proving endpoint
existence. Their tails are bounded by constants times $e^{-gt}$, uniformly
for labels in any closed smaller disk.

For completeness, local analytic dependence follows by Picard iteration:
on a sufficiently short time interval the integral form of (1) is a
contraction on a closed parameter ball, and each iterate is holomorphic
in the label. The uniform contraction limit is holomorphic by its Cauchy
integral formula. Concatenating finitely many such intervals proves this
for every finite time. The uniform exponential endpoint tail allows the
same Cauchy formula to pass to the limit $t\to\infty$. It also identifies
the formal coefficients in Section 2 with actual Taylor coefficients,
including the endpoint coefficients.

For the query conclusion, bounded holomorphy on the radius-$R$ hidden
ball supplies a uniform derivative bound on the radius-$R/2$ ball: apply
the one-variable Cauchy formula in each unit direction with radius below
$R/2$. The exponential parameter tails then give uniform query tails,
and the same Cauchy argument applies. $\square$

In particular, for any $1<r<q_*/Y$, if $F_r$ bounds the prediction on the
label circle $|\zeta|=r$, Cauchy's formula and the geometric series give

\[
 \sup_{t\in[0,\infty],v}
 \left|f_n(t,v;1)-\sum_{k=0}^K[\zeta^k]f_n(t,v;\zeta)\right|
 \le \frac{F_r\,r^{-K-1}}{1-r^{-1}}.             \tag{16}
\]

This is a proved full-time tail estimate when its displayed neighborhood
and radius hypotheses hold. The crucial condition is $q_*>Y$, not merely
real-label fitting.

### A concrete finite-width analytic neighborhood

The hypotheses of Proposition 2 are not empty for the actual deep network.
Here is an explicit construction showing their finite-width limitation.
Suppose the initialized first-matrix RMS operator norm and all hidden
matrix operator norms are at most eight, and all initialized sphere-feature
RMS norms are at most $H_0$. Let the activation strip have width
$a_{\rm strip}>0$ and full-strip derivative bound $s\ge1$. Define

\[
 C_1=1,\qquad C_\ell=H_0+9sC_{\ell-1}\ (2\le\ell\le L),
 \quad C_* =\max_\ell C_\ell,
 \quad R_n=\min\{1,a_{\rm strip}/(4\sqrt n C_*)\}. \tag{17}
\]

For $\|u-u_0\|_2<R_n$, layerwise subtraction yields
$\|z^{(\ell)}(u,v)-z^{(\ell)}(u_0,v)\|_2/\sqrt n
\le C_\ell\|u-u_0\|_2$. Indeed the first-layer bound is exactly the
normalization of $u$; the next-layer difference is bounded by the changed
mixer times the initialized feature plus the current mixer times the
changed feature. The current mixer norm is at most nine. Applying this
induction along each radial segment proves that every preactivation stays
within imaginary distance $a_{\rm strip}/4$; hence the derivative bound
used in the induction is valid. This also proves holomorphy on the ball.

The current feature RMS norm is at most $H_0+sC_*$. Put
$M=\max\{1,H_0+sC_*\}$,
$D_1=1$, $D_\ell=M+9sD_{\ell-1}$, and
$B=\max\{1,s\max_\ell D_\ell\}$. Differentiating the forward recursion
gives (12) with these width-independent $M,B$. The sample normalization
in $V$ ensures that the columnwise bound also bounds its operator norm;
the same argument applies to its derivative. The query maps have the same
uniform feature bound.

Thus Proposition 2 proves a sufficient label disk whose radius is bounded
below by a constant times $n^{-1/4}/Y$ on this event. The first condition
in (13), through $R_n$, is the shrinking term. This rough neighborhood
does not improve the finer shrinking-domain estimates identified in the
assigned dense-comparison report. Its contribution here is a complete
all-time continuation and coefficient argument, not a width-uniform disk.
For fixed nonzero $Y$, it does not justify evaluating the series at
$\zeta=1$ as $n\to\infty$.

## 4. Gaussian coefficient integrals need not form a convergent series

**Proposition 3.** There is an activation obeying the required strip class
and having unbounded values, and an explicit odd Gaussian-averaged function
of a real label multiplier, which is smooth but has label Taylor radius
zero. The hidden perturbation is even and quadratic in the label.

Fix $c>0$, let $G,H$ be independent real standard Gaussians, and set

\[
 \phi(z)=z+\frac{\sinh c}{\cosh c-\cos z},
 \qquad P(\zeta)=\zeta\,\mathbb E\phi(G+\zeta^2H^2)
 \quad(\zeta\in\mathbb R).                      \tag{18}
\]

The activation is real on the real axis. Its only nonreal poles are at
$2\pi k\pm ic$; on the smaller strip $|\operatorname{Im}z|<c/2$ its
periodic part and first derivative are bounded. One can verify this directly
by periodicity and compactness of one closed period in that smaller strip,
whose denominator has no zero. Its linear term makes its values unbounded.
All its real derivatives of any fixed positive order are bounded.

**Proof of zero radius.** The elementary geometric-series identity is

\[
 \frac{\sinh c}{\cosh c-\cos z}
 =1+2\sum_{k\ge1}e^{-ck}\cos(kz).              \tag{19}
\]

For real $z$ this series and each fixed-order differentiated series converge
absolutely and uniformly. The characteristic function of a real standard
Gaussian gives $\mathbb E\cos(kG)=e^{-k^2/2}$ and
$\mathbb E\sin(kG)=0$. This identity follows, for example, by integrating
the Gaussian density by parts: its characteristic function $\chi$ obeys
$\chi'(k)=-k\chi(k)$ and $\chi(0)=1$. Independence and (19) give

\[
 P(\zeta)=\zeta+\zeta^3
       +2\zeta\sum_{k\ge1}e^{-ck-k^2/2}
                         \mathbb E\cos(k\zeta^2H^2).              \tag{20}
\]

Every fixed real derivative under the expectation is justified by a
polynomial in $|H|$ times a bounded derivative of the periodic activation.
The Gaussian has every such moment. Equation (20) is therefore smooth,
and for $r\ge1$ its coefficient of $\zeta^{4r+1}$ is exactly

\[
 A_r=2(-1)^r\frac{\mathbb EH^{4r}}{(2r)!}
                 \sum_{k\ge1}e^{-ck-k^2/2}k^{2r}.                \tag{21}
\]

All terms in its magnitude have the same sign, so there is no cancellation.
Gaussian integration by parts gives
$\mathbb EH^{4r}=(4r)!/(2^{2r}(2r)!)$. Since the central binomial
coefficient is the largest among the $4r+1$ coefficients in
$(1+1)^{4r}$,

\[
 \frac{\mathbb EH^{4r}}{(2r)!}
 =\frac{\binom{4r}{2r}}{2^{2r}}
 \ge\frac{2^{2r}}{4r+1}.                       \tag{22}
\]

For $r\ge2$, choose $k=\lfloor\sqrt{2r}\rfloor$ in (21). Then
$k\ge\sqrt{r/2}$, $k^2/2\le r$, and $ck\le c\sqrt{2r}$, so

\[
 |A_r|\ge\frac{2}{4r+1}
             (2r)^r e^{-r-c\sqrt{2r}}.         \tag{23}
\]

Its $(4r+1)$-st root tends to infinity. A power series with a positive
radius has bounded coefficient roots, as follows immediately from the
Cauchy coefficient estimate on any smaller circle. Thus $P$ cannot be
holomorphic on any complex neighborhood of zero and its Taylor series has
radius zero. $\square$

This example has a bounded real prediction envelope on each bounded label
interval and explicit finite Gaussian integrals at every coefficient order.
Replacing $\zeta^2$ in (18) by $(1-e^{-t})\zeta^2$ and its leading factor
by $(1-e^{-t})\zeta$ gives a family with an endpoint and exponentially
decaying time derivatives; the same zero-radius argument applies at every
$t>0$. These elementary properties cannot by themselves certify (16).

The example is deliberately not asserted to satisfy (1). It falsifies the
intermediate implication “strip-analytic nonlinearities plus Gaussian
coefficient formulas imply a fixed label disk.” A proof for the actual
deep flow must use additional structure of its trained Gaussian fields.
This witness does not falsify the existence of an absolute-polylog decoder,
nor the possibility of an asymptotic series with a useful finite optimal
truncation, nor a more general approximation by analytic continuation.

## 5. What the recursive memory count does and does not prove

There is a precise small-stack property in (7)–(9). Expand sums and tensor
contractions term by term. Compute $u_{2j}$ using lower-order coefficients,
then $K_{2j}$, then the convolution defining $e_{2j+1}$, then $a_{2j+1}$.
Along any recursive call chain the label order decreases after at most a
fixed number of these stages. A coefficient of a composition in (7) has
at most $k$ factors at order $k$, and a partition $k_1+\cdots+k_r=k$ can
be enumerated with at most $k$ integer registers. The same applies to the
multilinear derivative of $V$ occurring in $J$.

Consequently the time/coefficient recursion has $O(k)$ nested frames and
$O(k^2)$ simultaneously stored scalar values, indices and partial sums,
when all vector coordinates and tensor contractions are streamed. A
deterministic quadrature with $N$ nodes at each one-dimensional time integral
needs one loop counter per active integral; it does not require retaining
all its sampled values. The index bits are
$O(k^2(\log(P+n+m+k)+\log N))$, before numeric precision and leaf-evaluator
workspace. Using an error allocation over the full finite recursion gives
a finite deterministic quadrature for each fixed coefficient and time;
unlimited work permits recomputation of every discarded child value.

This is a proved count for the recurrence, not for its derivative-tensor
leaves. At finite width the latter involve the initialized matrices. Keeping
them would require $\Theta(n^2)$ data and violate the decoder target. In a
population route they would instead have to be reduced to explicit Gaussian
integrals, with a number of jointly required Gaussian variables bounded by a
fixed polynomial in $k$. Neither that bound nor the required quantitative
growing-order width comparison follows from (7). A deterministic product
quadrature for an integral in $D_k$ Gaussian coordinates would itself use
$O(D_k)$ counters and coordinates, plus the integrand evaluator's stack.
Thus a proved $D_k\le Ck^p$ and polynomial-space integrand evaluator would
combine with this recurrence count; an unspecified Gaussian integral is not
one stored scalar.

All these counts concern a deterministic query function. Reusing fixed
quadrature rules and tolerances defines one function of $v$, so repeated
queries need not introduce fresh randomness. Establishing a uniform error
bound for that function is a separate requirement and is not supplied by
the memory count.

## 6. Frozen result, provenance and next implication

The route proves (4)–(6), the explicit all-time holomorphy theorem
(12)–(16), the finite-width neighborhood (17), the zero-radius Gaussian
counterexample (18)–(23), and the recurrence-stack count in Section 5.
The first two apply to the actual deep-network feature-learning flow at
each finite width. The Gaussian example concerns only a proposed analytic
inference, with its narrower scope stated above. All proofs are explicit;
they have been algebraically reconstructed by the route author but have
not received an independent review.

The absent implication is specific: replace the finite-width hidden ball
in (17) by a population construction that gives a summable approximation
at the full original labels, together with quantitative growing-order width
errors and polynomial Gaussian-leaf workspace. A fixed complex disk would
suffice via (16); Proposition 3 shows why it requires a network-specific
argument. Proposition 1 is also compatible with factorial coefficient
growth, so it cannot itself establish that disk.

The target remains the supervisor's all-sphere, all-physical-time and fitted
endpoint late-query problem with absolute-polylog retained plus live memory,
at the dense-variability near-root error envelope. No initialization-dependent
full array, future trajectory, spatial coefficient table, fresh-query
randomization, or narrower label interval has been inserted into a claimed
solution.

Scientific inputs read: `docs/index.qmd` and `docs/notation.qmd` completely;
the assigned `POPULATION_DECODER.md` Section 10 as a route locator (the
adjacent Section 9 conclusion and provenance lines were incidentally visible
in the requested range); and the three specifically authorized integrated
sources `GENERAL_DENSE_COMPARISON.md`, `GENERAL_EXPLICIT_FITTING.md`, and
`COMPACT_FULL_LABEL_RANGE.md` completely. Links from those sources were not
followed. No other study, archive, repository history, experiment or external
scientific source was used. The supervisor supplied the exact integrated
paths after the initial lookup in the current study returned missing files.

Process inputs: the complete `solve-math-rigorously` and
`investigate-conjectures` skills, with the latter's research-contract,
adversarial-audit and proof-search-orchestration references; Part 1 of the
shared workflow; and the supplied shared task instructions. The required
custom canonical-notation skill returned `Permission denied`; a filename
search in accessible skill roots found no copy before the supervisor
instructed use of the explicit user requirements and maintained notation
contract. Its neural-network reference was not accessible. This is a
disclosed fallback, not a claim that the unavailable instructions were read.

The initial scientific route was scoped independently. The supervisor's
subsequent message emphasized absolute-polylog live memory, the allowance of
large decoding work, and the need for one consistent all-query function.
No other route's scientific findings were supplied before this candidate.

Source hashes at writing:

| Input | SHA-256 |
|---|---|
| `docs/index.qmd` | `f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| current-study `POPULATION_DECODER.md` | `9d7ac82eed17036686cef3d679022a8df4404e78212e87e5df83d0503733f54d` |
| integrated `GENERAL_DENSE_COMPARISON.md` | `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9` |
| integrated `GENERAL_EXPLICIT_FITTING.md` | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| integrated `COMPACT_FULL_LABEL_RANGE.md` | `90aeb1a3aba585aab27f0b46cb23ad7391614abbc64272dccf16ab25fb80b071` |

HEAD before this assigned-file write was
`3834145d910202a84824d943fe7d7f65714d96f2`; the shared index was empty.
The route edited only this report and performed no Git index mutation.
