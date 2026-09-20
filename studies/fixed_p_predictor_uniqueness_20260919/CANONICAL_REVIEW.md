# Informed internal check of canonical order-one feature independence

Reviewer: scoped agent unique_passive_limits, 2026-09-19.

**Verdict: PASS for the stated exact-population, order-one feature theorem and
represented-readout construction.** I found no mathematical correction needed.
There is one nonblocking rendering issue: most inline mathematical expressions
start with an ordinary parenthesis and end with an escaped closing parenthesis,
for example candidate lines 24–29. Repair these delimiters when preparing a
readable edition. I made no candidate edits.

This is an informed scoped internal check, not an isolated promotion review. I
had authored the separately frozen passive-limit route in this same study before
receiving this assignment. The canonical candidate was not available during
that independent route. No other studies, old proof, other agents' reviews,
or external scientific sources were used in this check.

## Exact inputs and coverage

I read every line of the following assigned scientific inputs:

- CANONICAL_FEATURES.md, SHA-256
  b202a5344b2ba5bb845e2a907e3347467a7dc65115c68a155af9d367090b53f3.
- docs/NOTATION.md, SHA-256
  199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b.
- docs/global_nonlinear.md, lines 13161–13786 inclusive, slice SHA-256
  0a00ff65642c57068bc3cbf8dcda5a3024edd8e12213a521168fb4db9b303bb1.

The initial batched read was truncated in its combined output; complete separate
reads of the notation and source ranges 13161–13360, 13361–13560, and
13561–13786 repaired that coverage. The candidate itself was read completely.
Hashes match the frozen assignment and the candidate's recorded dependencies.
HEAD was bcee9782651c34ae1204d37186e5c57e9282b273 and the Git index was empty.
Required proof/research skills and process instructions were already read.
Only this report is written; no experiments, code tests, index changes or
candidate modifications are part of this review.

The source range defines the raw lists, Gaussian core marks, positive ridge,
actual transpose orientation, and contraction directly. H3.CS7 explicitly
specifies the initialization contraction, so checking the present finite-order
feature statement does not require importing a neural-limit theorem or sources
outside the assigned range. I did not audit the source's broader neural-limit
or hierarchy-convergence theorems.

## Contraction, correlation, and ridge normalization

The source gives, at order one, exactly
\[
 \psi_1=(1,h_1,h_2,T_1,T_2)^T,\qquad
 \psi_2=(1,Z_1,Z_2)^T,
\]
with independent lower pairs
$h_i=\tanh g_i$, $T_i=\tanh(\zeta_i+\alpha h_i)$ and separate upper variables
$Z_i=\tanh\xi_i$. The variances are $\operatorname{Var}\zeta_i=\tau$ and
$\operatorname{Var}\xi_i=v$, with $\alpha=1-\tau$. No extra nonconstant words
are present at this order. The scheduled ridge is exactly $1/4096$.

Writing $\gamma=ET_i^2$, $\delta=1-\gamma$ and $\beta=E[h_iT_i]$, the lower
Gram has independent two-by-two blocks
\[
 \begin{pmatrix}v&\beta\\\beta&\gamma\end{pmatrix}
\]
on each $(h_i,T_i)$ pair and a separate constant entry one. Its off-block
entries vanish by independence and centered oddness, not by an assumption that
$h_i$ and $T_i$ are independent. The upper Gram is
$\operatorname{diag}(1,\tau,\tau)$.

Substitution into H3.1 gives
\[
 C_{Z_j,h_i}=\alpha v\,\mathbf1_{i=j},\qquad
 C_{Z_j,T_i}=(\alpha\beta+\tau\delta)\mathbf1_{i=j}.
\]
Indeed $E\partial_{\xi_i}Z_j=\alpha\mathbf1_{i=j}$,
$E[Z_iZ_j]=\tau\mathbf1_{i=j}$, and
$E\partial_{\zeta_j}T_i=\delta\mathbf1_{i=j}$. All constant row/column
entries are zero. Thus the response term $\tau\delta$ is retained.

For $R_\ell=G_\ell+\eta I=L_\ell L_\ell^T$, substituting
$b_\ell=L_\ell^{-1}\psi_\ell$ and $D=L_2^{-1}CL_1^{-T}$ yields
\[
 b_2^TD L_1^{-1}E_1[\psi_1\tanh(g\cdot u)]
 =\psi_2^TR_2^{-1}CR_1^{-1}E_1[\psi_1\tanh(g\cdot u)].
\]
Both inverse Gram factors and the right transpose are therefore correct.
Multiplying the two-by-two inverse gives exactly the candidate's coefficients
\[
 \Delta=(v+\eta)(\gamma+\eta)-\beta^2,\quad
 A=\frac{\alpha v(\gamma+\eta)-\beta(\alpha\beta+\tau\delta)}{\Delta},
 \quad
 B=\frac{\alpha\eta\beta+\tau\delta(v+\eta)}{\Delta}.
\]
The remaining upper factor is $1/(\tau+\eta)$.

Conditioning on the lower Gaussian pair first gives
$E[T_i\mid g]=m(\alpha\tanh g_i)$, where
$m(s)=E_\zeta\tanh(\zeta+s)$. Since $u\in S^1$, the conditional residual
in $g\cdot u$ has variance $1-u_i^2$. This recovers exactly
\[
 H_0(u)=\tanh\big(F(u_1)Z_1+F(u_2)Z_2\big)
\]
with the candidate's $F$. The reduction does not replace the correlated marks
by independent features.

## Reconstruction of the delicate sign estimate

This is the main potential failure point, since $A$ has not been shown positive.
The candidate correctly avoids using its sign.

First, scalar Gaussian integration by parts gives
$1-v=E[G\tanh G]>E[\tanh^2G]=v$. The strict inequality holds off $G=0$
because $|G|>|\tanh G|$. Thus $0<v<1/2$.
Pointwise comparison at $\sqrt vG$ gives $0<\tau<v$, so $1/2<\alpha<1$.
For $\xi\sim N(0,v)$, integration by parts and Cauchy–Schwarz give
\[
 E[\xi\tanh\xi]=v\alpha,\qquad \alpha^2v\le\tau. \tag{R1}
\]
Bounded derivatives and Gaussian tails justify these integrations.

Since $m$ is odd and $0<m'(s)\le1$, conditioning on $h=\tanh G$ yields
\[
 0<\beta=E[h\,m(\alpha h)]\le\alpha v. \tag{R2}
\]
Put $s_0=1+2\tau$ and
$\lambda=s_0^{-1/2}\exp(-\alpha^2/s_0)$.
Integrating $\tanh z\le z$ for $z\ge0$ and using evenness gives
$\operatorname{sech}^2z\ge e^{-z^2}$. Completing a Gaussian square,
then applying Jensen to $e^{-x}$, therefore gives
\[
 J(s):=m'(s)\ge s_0^{-1/2}e^{-s^2/s_0}\ge\lambda
 \quad(|s|\le\alpha),\qquad
 \delta\ge s_0^{-1/2}e^{-\alpha^2v/s_0}. \tag{R3}
\]

I checked both ranges in the candidate's proof that $\delta+\lambda>1$:

1. If $1/2<\alpha\le3/4$, then $3/2\le s_0<2$,
   $\alpha^2/s_0\le3/8$, and $\alpha^2v/s_0<3/16$.
   Thus
   \[
   \delta+\lambda\ge
   (e^{-3/16}+e^{-3/8})/\sqrt2
   \ge23/(16\sqrt2)>1.
   \]
   The last inequality is the exact integer comparison $529>512$.
2. If $3/4\le\alpha<1$, then $\tau\le1/4$, $s_0\le3/2$, and (R1) gives
   $\alpha^2v/s_0\le\tau/(1+2\tau)\le1/6$.
   Hence $\delta\ge(5/6)\sqrt{2/3}>2/3$.
   Also $\alpha^2\le1$ and the increasing function
   $-\tfrac12\log s-1/s$ on $[1,2]$ give $\lambda\ge e^{-1}>1/3$.
   For completeness $e<3$ follows from
   $e=2+\sum_{k\ge2}1/k!<2+\sum_{k\ge2}2^{-(k-1)}=3$.

Next, $h$ and $\zeta$ are centered and orthogonal, with squared norms
$v,\tau$, and Gaussian integration by parts gives $E[T\zeta]=\tau\delta$.
Expanding the square of $T-(\beta/v)h-\delta\zeta$ proves
\[
 \gamma\ge\beta^2/v+\tau\delta^2. \tag{R4}
\]
Writing $N_B=\alpha\eta\beta+\tau\delta(v+\eta)$, direct substitution of
(R4), without dropping a negative term, gives
\[
 \Delta-\delta N_B
 \ge\eta[\beta^2/v+v+\eta-\alpha\beta\delta]>0.
\]
The strict sign follows from (R2),
$\alpha\beta\delta\le\alpha^2v\delta\le v$, and $\eta>0$.
Consequently $0<B<1/\delta$.

Finally the defining row identity gives $A(v+\eta)+B\beta=\alpha v$.
For $|s|\le\alpha$, (R2), $J\le1$, $B\le1/\delta$ and (R3) imply
\[
 \begin{aligned}
 A+\alpha BJ(s)
 &=\frac{\alpha v+B[\alpha(v+\eta)J(s)-\beta]}{v+\eta}\\
 &\ge\frac{\alpha}{v+\eta}
   \{v[1-B(1-J(s))]+\eta BJ(s)\}\\
 &\ge\frac{\alpha v}{(v+\eta)\delta}(\delta+\lambda-1)>0.
 \end{aligned}
\]
This proves $\chi'(g)>0$ for every finite real $g$. The argument is valid
for every fixed positive ridge; it neither takes $\eta\downarrow0$ nor needs
a numerical value of any Gaussian moment.

For $|t|<1$, differentiation under the expectation defining $F$ is justified
on each compact subinterval by bounded $\chi$, bounded tanh derivatives,
and Gaussian first moments. Gaussian integration by parts gives
\[
 (\tau+\eta)F'(t)
 =E[\chi'(G)\operatorname{sech}^2(tG+\sqrt{1-t^2}V)]>0.
\]
The second-derivative term from the $G$ integration cancels exactly with
the $V$ integration term. Bounded convergence supplies endpoint continuity.
Strict interior monotonicity and continuity give strict monotonicity on all
of $[-1,1]$, including endpoint comparisons. Symmetry gives $F(-t)=-F(t)$.
Thus its only zero is zero.

## Independence, augmented query, and readouts

The effective map $r(u)=(F(u_1),F(u_2))$ is injective by coordinatewise strict
monotonicity. It is odd and nonzero on $S^1$. Therefore the candidate's
antipodal-free input condition implies $r_a\ne0$ and $r_a\ne\pm r_b$.
This condition, rather than merely distinct directions in coefficient space,
is exactly what the next argument needs.

The upper $Z$ law has positive density throughout $(-1,1)^2$, since both
Gaussian variances are positive and coordinatewise tanh is a diffeomorphism
onto that square. An $L^2$ relation among the continuous fields is thus an
identity at every point of the square.

I checked the restriction-to-a-line argument against collinear but differently
scaled $r_a$: it still works. A vector $q$ avoiding the finitely many
orthogonal lines of $r_a$, $r_a-r_b$, and $r_a+r_b$ makes all
$s_a=|r_a\cdot q|$ positive and pairwise distinct. The line $tq$ is in the
square for sufficiently small $|t|$. The resulting one-variable finite sum of
tanh functions is real analytic for every real $t$, so its zero interval
extends across the real line by the Taylor-series endpoint argument supplied
in the candidate.

Absorbing signs into the coefficients gives
$\sum e_a\tanh(s_at)=0$ with $0<s_1<\cdots<s_m$.
The limit at infinity gives $\sum e_a=0$. Subtract that constant identity,
multiply by $e^{2s_1t}$, and use
$\tanh(st)-1=-2/(e^{2st}+1)$: the limit is $-2e_1=0$.
Removing that term and repeating proves every coefficient zero. Integer
ratios between the $s_a$ cause no exception. This proves the claimed finite
independence, hence positive definiteness of its Gram matrix. Positive
training weights preserve definiteness by an invertible diagonal congruence.

An augmented query outside all training directions and antipodes satisfies
the identical hypotheses. Its projection residual
\[
 R_*=H_*-\sum_a(K^{-1}k)_aH_a
\]
is nonzero and orthogonal to every training field. Therefore
$\kappa_*=\|R_*\|_2^2=E[R_*H_*]>0$. Substitution verifies the candidate's
readout formula:
\[
 c_t=\sum_a(K^{-1}y)_aH_a+
       \frac{t-k^TK^{-1}y}{\kappa_*}R_*.
\]
It fits every label and gives exactly $t$ at the query. Every coefficient
is finite, and the fields are bounded, so $c_t$ is bounded. No bound uniform
in arbitrary prescribed $t$ is claimed. It remains odd under upper-mark sign
reversal and is admissible as a represented readout. Orthogonality also proves
the stated uniqueness of the minimum-$L^2$-norm interpolant.

## Adversarial scope checks and residual issues

- The theorem concerns the exact Gaussian population. Finite upper-node
  quadrature has finite rank; the candidate explicitly excludes transferring
  its universal finite-set claim to such a rule.
- The claim is fixed order one. It neither assumes rotational invariance of
  the projected kernel nor substitutes a rotationally invariant kernel.
- Repeated or antipodal inputs would invalidate independence; they are
  explicitly excluded. Queries at these directions remain label constrained.
- Positive definiteness for each fixed finite set does not give uniform
  conditioning near collisions. The candidate correctly states this.
- The initial readout is zero. The alternate readouts share the canonical
  initialized hidden state but are not claimed to share the full prescribed
  initialization or to be reached from it.
- The result is a representability theorem, not a statement about noisy
  endpoint distributions, full-network convergence, or multiple solutions
  to deterministic gradient flow. No such bridge is asserted.

There are no unresolved mathematical objections within the assigned theorem.
The malformed inline delimiters are an editorial issue only. This report
supports internal acceptance of the exact stated feature and readout results;
it supplies neither a promotion review nor approval to change established
material.

## Version closure: delimiter-only repair

On 2026-09-19 I read the complete revised CANONICAL_FEATURES.md and independently
verified its current SHA-256:
5eab1371afaca04719bcd78a88c586f33042a008a28bbf1f3a07f0a0f6075b91.

The only changes from the reviewed version are precisely 167 inserted
backslashes before opening-parenthesis math delimiters. To verify this at the
byte level, I preserved the one pre-existing opening delimiter on the weighted
Gram expression, removed the backslash from each of the other 167 opening
delimiters, and hashed the recovered bytes. The result is exactly the original
reviewed SHA-256:
b202a5344b2ba5bb845e2a907e3347467a7dc65115c68a155af9d367090b53f3.
The file-length difference is exactly 167 bytes. No other byte changed.

The revised file has 168 inline and 36 display math-delimiter pairs. A sequential
delimiter check found no unmatched or nested delimiters, and inspection of the
complete revised text confirmed the repaired openings enclose the intended
expressions. The earlier nonblocking rendering issue is closed.

**The mathematical-content PASS applies unchanged to this revised hash.**
The byte comparison proves that all mathematical expressions, assumptions,
arguments, and scope qualifications are preserved. This version closure is
part of the same informed internal check; it does not change its independence
or promotion status. I edited only this review report.
