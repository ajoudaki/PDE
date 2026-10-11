# Isolated internal review of the finite-time energy route

11 October 2026. Verdict: **PASS for the deterministic claims in Sections
1–5 and the affine tracking corollary, with the scope stated below.**
This is an internal proof check, not a promotion
review. The unrestricted nonlinear, width-uniform prediction-tracking target
remains open in this argument; neither its truth nor its falsity is established.

## Frozen inputs and review boundary

The complete scientific inputs read were:

- `ENERGY_ROUTE.md`, SHA-256
  `2e3ee1f7a168df71b53ceda53e8e30d58b722821092f918e75f7d557df8394cc`.
- Exactly lines 1–76 of `paper/compact_legendre.tex`, containing the projection
  lemma and its proof. SHA-256 of that exact line slice, including its final
  newline:
  `9ab74f1773cd20be8aaa2b4ea9ae00d9da8dd8947186297ff9e56eec5e9a5d93`.
- Complete `docs/notation.qmd`, SHA-256
  `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.

During this review the author made the requested explicit Gaussian-law and
confidence-range clarification at the start of Section 5. I read that exact
replacement and verified that replacing its three lines by the original
single sentence recovers the original hash above; there were no other
candidate changes. The corrected frozen candidate reviewed by this final
report has SHA-256
`0b51956f9782c02fff67476929f87078c9115af1819a9b25d92a5ecfd082886d`.

The neutral review assignment, current `AGENTS.md`,
`/etc/codex/skills/solve-math-rigorously/SKILL.md`, and
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` together
with its complete `references/neural-response-memory.md` were also read.
No study README, other route, study history, earlier verdict, unassigned
scientific source, external source, experiment, or Git material was consulted.
Only this report was written. No additional scientific dependency was needed
to reconstruct the displayed argument. This checks the displayed closure;
correspondence with portions of the manuscript or code outside the frozen
inputs is outside the review boundary.

The notation in the candidate is retained: $w=W^{(L+1)}$,

\[
 \rho^2=\frac1m\sum_a(f(x_a)-y_a)^2,\qquad
 Y^2=\frac1m\sum_a y_a^2.
\]

The parameter norm has the candidate's first-layer and readout factors

\[
 \|U\|_{\rm par}^2
 =\frac{\|U^{(1)}\|_F^2}{n}
  +\sum_{\ell=2}^L\|U^{(\ell)}\|_F^2
  +\frac{\|U_w\|_2^2}{n}.
\]

This is the mobility metric for the stated loss, rather than an unnormalized
Euclidean parameter metric. Zero stored readout is an explicit assumption;
the conclusion is not silently transferred to a different initialization.

## Exactness, regularity, and sample normalization

The raw equations are locally Lipschitz on $\tau>0$: reconstruction is
smooth in the moment coordinates and $\tau^{-1}$, the forward and backward
maps are locally Lipschitz under the stated hypotheses on $\phi_\ell'$,
and the sample residual norm is locally Lipschitz even at zero. When all
residuals vanish, every raw right-hand side, including the clock and moment
equations, vanishes. Uniqueness for this finite-dimensional ODE therefore
excludes reaching such an equilibrium at a finite regular time from $Y>0$.
For $Y=0$, the prescribed initial state is already an equilibrium.
This justifies clock division on compact regular intervals without adding
division to the algorithm.

For $p_j^A(\xi)=P_j(2\xi/A-1)$, direct polynomial differentiation gives

\[
 \partial_Ap_j^A
 =-\frac1A\left(jp_j^A+\sum_{i<j}(2i+1)p_i^A\right).
\]

Consequently the raw moments in equation (3) equal
\(\int_0^{\tau(t)}h_a(\xi)p_j^{\tau(t)}(\xi)d\xi\) and
\(\int_0^{\tau(t)}b_a(\xi)p_j^{\tau(t)}(\xi)d\xi\), respectively.
Their initial values are exactly the integrals of the stated constant
forward and zero backward prefixes. The physical backward write is
\(\rho b_a=r_a\delta_a\), including its sign and sample residual factor.

Orthogonality gives the reconstructed hidden increment as

\[
 -\frac2{mn}\sum_a\int_0^{\tau(t)}
       (\Pi_q^{\tau(t)}b_a)(\xi)
       (\Pi_q^{\tau(t)}h_a)(\xi)^\top\,d\xi.
\]

For a fixed pair of histories, differentiating the corresponding cross
projection tail gives $e_b(A)e_h(A)^\top$. The interior terms vanish
because derivatives of the projected polynomials remain in the projection
space. Subtracting this derivative from that of
\(\int_0^A b_a h_a^\top\) proves equation (5), with the positive defect
sign and coefficient $2\rho/(mn)$. This is the actual reconstructed
trajectory, not an externally forced substitute.

The sample normalization is correct throughout. Writing

\[
 u_a=r_a/\rho,\qquad \frac1m\sum_a u_a^2=1,
\]

one has, from a uniform per-sample response bound,

\[
 \frac1{mn}\sum_a\|b_a\|_2^2
 =\frac1m\sum_a u_a^2\frac{\|\delta_a\|_2^2}{n}
 \le B_\ell^2.
\]

An individual $u_a$ can be as large as $\sqrt m$; none of the aggregate
estimates needs the incorrect bound $\lvert u_a\rvert\le1$.
In particular,

\[
 \|\mathcal E_\ell/\rho\|_F
 \le2\left(\frac1{mn}\sum_a\|e_{b,a}\|_2^2\right)^{1/2}
       \left(\frac1{mn}\sum_a\|e_{h,a}\|_2^2\right)^{1/2}.
\]

The growing-interval identity has no missing normalization factor. Integrating
the last inequality in clock time and using the two tail-growth identities
proves equation (8).

## Projection dependency and endpoint attacks

The eigenvalue argument yields equation (7) for histories with square
integrable derivative. At a fixed regular interval and fixed finite $n,q$,
the forward histories have this regularity: physical states are continuously
differentiable, the clock has positive derivative, and the constant prefix
joins continuously. Thus using the estimate to obtain a uniform derivative
bound does not assume that uniform bound beforehand. The energy route does
not require the backward derivative estimate at this stage.

I checked both endpoint constants from the supplied lemma. Integration by
parts gives

\[
 e_g(A)=\frac12\int_0^A(p_q^A+p_{q-1}^A)g'(\xi)\,d\xi,
\]

because $p_q^A(0)+p_{q-1}^A(0)=0$. The multiplier's squared norm is

\[
 \frac A4\left(\frac1{2q+1}+\frac1{2q-1}\right)
 =\frac{Aq}{4q^2-1}\le\frac A{3q};
\]

the inequality includes $q=1$, where equality holds.

For the kernel bound, the supplied transformed Legendre equation gives
\(\partial_\theta(v^2+v'^2/a_k)=-a_k'v'^2/a_k^2\ge0\) on
\((0,\pi/2)\). Its midpoint energy is at most $4/k$, by the displayed
even and odd midpoint values and central-binomial estimate. Hence

\[
 |\partial_\theta P_k(\cos\theta)|
 \le3\sqrt k(\sin\theta)^{-1/2}
     +2k^{-1/2}(\sin\theta)^{-3/2}.
\]

On $[1/k,\pi/2]$ the integral is at most $3\pi\sqrt k+8$.
On $[0,1/k]$, the separate bound
\(\lvert P_k'\rvert\le k(k+1)/2\) gives an integral at most
\((k+1)/(4k)\le1/2\). Reflection yields at most
\(17+6\pi\sqrt k\le36\sqrt k\). Therefore the kernel has $L^1$
norm at most $36\sqrt q$, so the quoted $64\sqrt q$ is valid.
The $q=1$ averaging kernel also satisfies the assertion directly.
These arguments hold for aggregate sample vectors viewed as one Hilbert
space, so their use introduces no sample-count or width factor.

## Readout energy, continuation, and loss variation

The decisive readout identity checks algebraically:

\[
 \frac d{dt}\frac{\|w\|_2^2}{n}
 =-4\langle r,f\rangle_m
 =2Y^2-2\rho^2-2\|f\|_m^2
 =Y^2-4\|f-y/2\|_m^2.
\]

Its last expression gives $\|w(t)\|_2/\sqrt n\le Y\sqrt t$.
Integrating the middle expression and using the nonnegative readout norm
gives $\int_0^t\rho^2\le Y^2t$, and Cauchy–Schwarz then gives
\(\int_0^t\rho\le Yt\). No bound on activation values or on the magnitude
of a fixed label is used. Dense gradient flow has
\(d\rho_D^2/dt=-\|F\|_{\rm par}^2\), so its path displacement is at most

\[
 \int_0^t\|F\|_{\rm par}
 \le\sqrt{t\int_0^t\|F\|_{\rm par}^2}\le Y\sqrt t.
\]

For fixed finite width this bounds every parameter on finite intervals and
proves dense continuation.

Inside the stopped ball $R=Y\sqrt T+1$, each hidden operator norm is at
most $K_0+R$, since an increment's operator norm is bounded by its Frobenius
norm. The first matrix, readout, feature, response, residual, and clock bounds
in (13) follow with exactly their displayed normalizations. The inequality
\(\lvert\phi_\ell(u)\rvert\le b_\ell+s_\ell\lvert u\rvert\) is sufficient;
unbounded values are allowed, but unbounded first derivatives are not.

The apparent circularity in the forward clock-energy argument resolves as
follows. Polynomial endpoint evaluation has operator norm $q/\sqrt A$,
because its squared norm is $q^2/A$. Applied to the bounded aggregate
backward history, this gives an endpoint error at most $(q+1)B_\ell$.
The tail-growth identity and equation (7) then give

\[
 \int_1^{\tau(t)}\|\mathcal E_\ell/\rho\|_F^2\,d\xi
 \le4(q+1)^2B_\ell^2D_{h^{(\ell-1)}}
 \le A_c^2\frac{q+1}{q}B_\ell^2Z_{\ell-1}
 \le2A_c^2B_\ell^2Z_{\ell-1}.
\]

Thus only the preceding forward layer's derivative energy occurs.
Differentiating $h^{(\ell)}=\phi_\ell(W^{(\ell)}h^{(\ell-1)})$
splits into the canonical weight velocity, defect velocity, and propagated
previous-layer derivative. Their squared integral bounds are respectively

\[
 4S B_\ell^2H_{\ell-1}^4,\qquad
 2A_c^2B_\ell^2H_{\ell-1}^2Z_{\ell-1},\qquad
 K_R^2Z_{\ell-1}.
\]

The factor $3s_\ell^2$ proves (14). For the first layer,
\(\|(W^{(1)})'\|_F/\sqrt n\le2B_1\), giving its stated initial step.
No backward gate was differentiated in obtaining this recursion.

The zero backward prefix gives $D_b\le SB_\ell^2$. Combining this with
the forward tail and cross-tail estimate produces exactly $C_E$ in (16).
The bound $M$ in (17) follows by applying sample Cauchy–Schwarz separately
to the canonical blocks and then summing their squared mobility norms.

Since $D\mathcal L[U]=-\langle F,U\rangle_{\rm par}$, the sign and all
factors in (18) are correct. It yields

\[
 \int_0^t\|F\|_{\rm par}^2\,ds\le Y^2+MC_E/q,
\]

and hence (20). At the stated $q_0$, the two added terms in (20) are
each at most $1/4$: the displacement remains below $Y\sqrt T+1/2<R$.
This is a strict stopping margin. If $C_E=0$, the accumulated defect is
zero and $q_0=1$ is consistent.

The maximal-existence alternative is also excluded. At fixed $n,q$, each
individual backward history has norm at most $\sqrt{mn}B_\ell$, despite
the absence of an a priori positive lower bound for $\rho$ at a putative
endpoint. Forward histories, $\tau\le A_c$, and all their raw moments
are bounded by their integral formulas and $\lvert p_j\rvert\le1$.
Together with $\tau\ge1$, this confines the finite raw state to a compact
subset of the ODE domain; the locally Lipschitz ODE therefore continues.

Finally, taking the positive part of (18) gives (22) without a sign
assumption on the defect. This is total positive variation of closure loss,
not closeness to dense loss, monotonicity, or eventual fitting.

## Gaussian event and quantifiers

The corrected frozen note explicitly assumes $0<\delta<1$, independent
first-matrix entries with law $N(0,1)$, independent hidden-matrix entries
with law $N(0,1/n)$, and mutually independent matrices. The initial readout
is $w_0=0$. Independence across layers is unnecessary for the union bound,
but is compatible with the proof. Entry variances alone would not imply
the Gaussian bilinear-form calculation; the clarification removes that
possible ambiguity.

Markov's inequality gives the stated first-matrix bound with failure at most
\(\delta/2\). Two $1/4$-nets of size at most $9^n$ give

\[
 \|W\|_{\rm op}\le2\max_{u,v\text{ in the nets}}|u^\top Wv|.
\]

Each bilinear form has variance $1/n$, so (23) follows. Substituting (24)
gives a hidden-layer failure probability at most

\[
 2\left(\frac{\delta}{4(L-1)}\right)^n
 \le\frac{\delta}{2(L-1)}\qquad(n\ge1).
\]

Consequently, for every fixed width $n\ge1$, an initialization event of
probability at least $1-\delta$ supports all $q\ge q_0$ simultaneously.
The same deterministic constants and $q_0$ apply at every width. There is
no union over $q$, hidden $n$-dependent remainder, or claim about one
event covering infinitely many separately sampled widths. The theorem is
for each fixed finite horizon $T$, with $q_0$ allowed to depend on $T$;
it does not prove that one fixed $q$ works for all time.

## Affine tracking and the nonlinear boundary

The affine corollary closes both missing estimates. To verify the first,
let $D=\|\theta-\vartheta\|_{\rm par}$ for two states in the stated
bounded parameter region. For $\phi_\ell(u)=a_\ell u+c_\ell$, forward
subtraction gives

\[
 \sup_{\|v\|=1}\frac{\|h_\theta^{(1)}-h_\vartheta^{(1)}\|_2}{\sqrt n}
 \le|a_1|D,
\]

and each later difference is at most $\lvert a_\ell\rvert$ times
the sum of the preceding difference multiplied by $K_R$ and $H_{\ell-1}D$.
Backward subtraction has the corresponding recursion with $B_{\ell+1}D$
and starts from $\lvert a_L\rvert\|w_\theta-w_\vartheta\|_2/\sqrt n$.
All gates are constant. These recursions, the readout formula, and subtraction
of each rank-one velocity give (28) with no width factor.

For the second estimate, the endpoint bounds above give

\[
 \|\mathcal E_\ell\|_F
 \le130\rho B_\ell\sqrt{A_cZ_{\ell-1}^*/3},
\]

and consequently $\|\dot\theta\|_{\rm par}\le C\rho$.
This particular estimate also holds for the nonlinear class. For every
training sample, differentiation of its prediction gives

\[
 |Df_a[U]|
 \le\left(B_1^2+\sum_{\ell=2}^L B_\ell^2H_{\ell-1}^2+H_L^2\right)^{1/2}
       \|U\|_{\rm par}.
\]

It follows that $\|\dot r\|_m\le C\rho$,
\(\lvert\dot\rho\rvert\le C\rho\), and
\(\|\partial_t(r/\rho)\|_m\le2C\). Thus (29) is valid for fixed

\[
 Y>0,\qquad Y e^{-CT}\le\rho(t)\le Y e^{CT}.
\]

For affine gates, differentiating the backward recursion uses bounded
operators and the already bounded matrix velocities, giving a uniform
per-sample response derivative bound $C\rho$. The aggregate physical
derivative of $b_a=(r_a/\rho)\delta_a$ is therefore bounded by $C+C\rho$.
Changing variables $d\xi=\rho\,dt$ gives

\[
 \frac1{mn}\sum_a\int_1^{\tau(T)}\|b_a'(\xi)\|_2^2d\xi
 =\int_0^T\frac{(mn)^{-1}\sum_a\|\dot b_a(t)\|_2^2}{\rho(t)}dt
 <\infty,
\]

uniformly in $n,q$. Zero initial readout makes the backward prefix
continuous, so no jump invalidates the projection derivative estimate.
The bound may depend on the fixed positive $Y$; $Y=0$ is stationary.

The two derivative-controlled tails now give accumulated defect at most

\[
 \frac{A_c^2}{2q(q+1)}
 \sum_{\ell=2}^L\sqrt{Z_{b,\ell}Z_{\ell-1}^*},
\]

where $Z_{b,\ell}$ denotes the finite backward derivative energy just
bounded. Applying (28) to the integral equations gives a parameter
difference at most this quantity times $e^{C_FT}$. The forward difference
recursion is uniform over the unit input sphere, proving (31)–(32).

The corollary's scope is the normalized-input, zero-readout setup of Section
1, arbitrary fixed labels and affine layer coefficients, every fixed finite
$T$, and $q\ge q_0(T,Y,A_0,K_0,\{b_\ell,s_\ell\})$. When random
initialization is used, it holds on the stated Gaussian confidence event.
The phrase “arbitrary finite data” should be read within that setup; a version
allowing unnormalized inputs would need the corresponding fixed input-radius
factors. The note does not establish continuation for all small orders or a
single order valid for unbounded time.

For nonlinear gates, equations (25) and (26) expose a real missing estimate:
two RMS bounds do not control the RMS of their coordinatewise product.
The example $u=v=\sqrt n e_1$ verifies that limitation but is not a
counterexample to the Gaussian theorem. For each fixed width, local
Lipschitz continuity on the bounded parameter region and the $L^1$ defect
do give tracking as $q\to\infty$; the resulting Lipschitz constant may
depend on width.

The bracket in (27) is correct with the convention
\([X_a,X_b]=DX_bX_a-DX_aX_b\). A nonzero bracket prevents transforming
all those fields into constant fields by a single smooth coordinate map;
it says nothing decisive about other stability methods. Finally, the
conditional tail-splitting estimate would produce the stated Osgood modulus:
\(\int_0 de/[e\sqrt{\log(1/e)}]=\infty\). The required evolving tail bound
is not provided by the current energy bounds, so the note appropriately
does not claim that this conditional mechanism proves nonlinear tracking.

No substantive mathematical error was found in the frozen claims. The
Gaussian law and confidence range are now explicit. The affine corollary
inherits the normalized-input and sufficiently-large-order conditions stated
above. The valid energy argument does not establish the still-missing
nonlinear prediction theorem.
