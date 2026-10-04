# Reconstruction of the second forward-history derivative argument

2026-10-03. Complete collaborative internal reconstruction, not an isolated
promotion review. The checked candidate is `HISTORY_APPROXIMATION_ROUTE.md`
at SHA-256
`bfb51ee447eeb2128d5970ba400eff9964987bcdbc47d38bba21f65dc2e2240f`.

**Mathematical verdict: PASS in the stated two-tanh, small-fixed-label,
zero-readout scope.** The actual order-$p$ residual-RMS closure has
all-time same-realization prediction error $C_\mu n^{-1/2}$ against the
dense width-$n$ network at
$p_n=\lceil n^{1/6}\exp\{a\sqrt{\log(e+n)}\}\rceil$, for sufficiently
large fixed $a$. Replacing original order $q$ by $\min\{q,p_n\}$ gives
the same error scale against that original closure, uniformly in $q$.
The moving count is $n^{7/6+o(1)}$. Both directions of the actual initialized
mixer remain unchanged. No finite-to-population bias is used or omitted.

One presentation correction was requested: the candidate introduced
$\|u\|_n$ for finite RMS, whereas the repository notation contract
requires writing $\|u\|_2/\sqrt n$ explicitly. This does not affect the
mathematical verdict. The reconstruction below uses explicit factors.

The author subsequently applied that notation-only revision. I read its
complete source and exact unified diff against the checked original. The
revised source has SHA-256
`46fc0584660bc45bda7cfeb6e4b6a63151559f79c96005ad3794799048d2477f`.
Every vector RMS and normalized history norm was expanded with the correct
$1/\sqrt n$ factor, and squared norms with $1/n$. The activation is now
defined as $\phi=\tanh$, with its derivatives written $\phi',\phi''$;
this exactly replaces the former gate aliases. The input-scope paragraph
also clarifies that the previous temporal note supplied only a diagnostic,
not a proof premise. No hypothesis, algorithm, estimate, exponent, or
conclusion changed. The full mathematical PASS applies to this revised
version as well; the original hash is retained for provenance.

## 1. Inputs and exact scope

The complete frozen candidate, current manuscript setting and residual-clock
construction, complete `paper/results.tex`, `paper/proof_alltime.tex`, and
`paper/proof_tracking.tex` were read. The authorized prior inputs read
completely were `Q_ORDER_RESULT.md`, `Q_ORDER_POSITIVE_ROUTE.md`,
`Q_ORDER_INSERTION_CHECK.md`, `Q_ORDER_POSITIVE_PROBABILITY_CHECK.md`,
`NONORTHOGONAL_DIRECT_ROUTE.md`, `NONORTHOGONAL_CHECK.md`,
`FINITE_MIXED_MOMENT_ROUTE.md`, and `FINITE_MIXED_MOMENT_CHECK.md`.
These all belong to the explicitly authorized prior study
`studies/dense_cutoff_population_rate_20261001/`. No unrelated study or
unfrozen sibling route was inspected. The canonical-notation skill, its
neural reference, and the rigorous-math skill were applied. No experiment,
manuscript mutation, or Git operation was performed.

The scientific source anchors are

```text
9026935501ce94886d9eee81c6d318d3f45ac2f526597be5de71b0989a959f27  Q_ORDER_POSITIVE_ROUTE.md
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
```

Write $v_a=x_a/\sqrt d$, $\|v_a\|_2=1$. The first weights are
$W^{(1)}\in\mathbb R^{n\times d}$, the hidden mixer is
$W\in\mathbb R^{n\times n}$, and the stored readout is
$w\in\mathbb R^n$. Forward fields, residual, and loss are
\[
z_a^{(1)}=W^{(1)}v_a,\quad h_a^{(1)}=\tanh z_a^{(1)},\quad
z_a^{(2)}=Wh_a^{(1)},\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
f_a=w^\top h_a^{(2)}/n,\quad r_a=f_a-y_a,\quad
\mathcal L=\rho^2=\frac1m\sum_a r_a^2.
\]
The backward response and lower carrier are
\[
\delta_a^{(2)}=w\odot\tanh'(z_a^{(2)}),\qquad
k_a=W^\top\delta_a^{(2)},\qquad
\delta_a^{(1)}=\tanh'(z_a^{(1)})\odot k_a.
\]
The loss and mobilities $(n,1,n)$ give exactly the candidate's equations
(3), including the $2$, $1/m$, and $1/n$ factors. Both systems share
$W_0^{(1)}$ with independent standard Gaussian entries and $W_0$ with
independent variance-$1/n$ Gaussian entries. The readout is exactly zero.

The candidate assumes the feature-Gram gap initially, then uses the exact
compatible signed-data quotient proved in the authorized positive route.
For fixed compatible sphere data the gap and positive label threshold
are geometry dependent. No uniformity over colliding input geometries,
incompatible signed duplicates, arbitrary depth, or large labels is asserted.

## 2. The algorithm is fully autonomous and unchanged

For order $p$, the evolved state is $W^{(1)},w,\tau$ and
$\bar h_{a,j}^{(1)},\bar\delta_{a,j}^{(2)}\in\mathbb R^n$ for
$a\le m$, $0\le j<p$. The clock satisfies $\dot\tau=\rho$,
$\tau(0)=1$, and the initialized mixer is retained exactly. The
candidate's moment ODEs and reconstruction are precisely the original
Legendre equations with this order. Sources are evaluated in its own
reconstructed network. The first-layer/readout equations are unchanged.

The history formula uses $c_a=r_a/\rho$ only in the proof. The autonomous
ODE uses $r_a\delta_a^{(2)}$ and $\rho h_a^{(1)}$ and does not divide by
$\rho$. The stored initial forward mode is the initialized first feature;
all other memories start at zero. The unit prefix therefore has constant
forward history and zero backward history. For $Y=0$ every state is
stationary; for $Y>0$ the fitting theorem gives $\rho>0$ at every finite
physical time, so all intermediate changes of variables are legitimate.

All-order existence, fitting, bounded operator/readout norms, and physical
speed bounds precede the approximation argument. The candidate does not
assume its desired discrepancy estimate in order to establish existence.
The physical hidden-matrix velocity includes the closure defect, and the
manuscript bounds this full velocity. That point is needed below.

Differentiating the exact reconstruction gives the candidate's defect (8).
The growing-domain projection-energy identity, followed by
Cauchy--Schwarz in the clock, yields
\[
\int_0^t\|E_2(s)\|_F\,ds
\le\frac2{mn}\sum_a
\|(I-\Pi_p^A)b_a^{(2)}\|_{L^2(0,A;\mathbb R^n)}
\|(I-\Pi_p^A)h_a^{(1)}\|_{L^2(0,A;\mathbb R^n)},
\quad A=\tau(t),\quad b_a^{(2)}=c_a\delta_a^{(2)}.
\tag{C1}
\]
Thus the source being estimated is total absolute velocity error, which
is the quantity actually used by damping.

## 3. Spectral estimate and the prefix interface

For a finite endpoint $A>0$, put $\eta_A(\xi)=\xi(A-\xi)$ and
$\mathcal L_Au=-(\eta_Au')'$. The normalized shifted Legendre mode
$e_j=\sqrt{(2j+1)/A}\,p_j(\xi/A)$ has
$\mathcal L_Ae_j=j(j+1)e_j$. This eigenvalue is independent of $A$;
the two chain-rule factors cancel the two powers of $A$ in the weight.

If $u$ is $C^1$ and piecewise $C^2$ on $[0,A]$, with square-integrable
$\mathcal L_Au$, integration by parts twice gives
\[
\int_0^A\mathcal L_Au\,e_j
=\int_0^A u\,\mathcal L_Ae_j
=j(j+1)\int_0^A u e_j.
\]
The outer boundary terms vanish because $\eta_A$ vanishes there and
$u,u'$ have finite one-sided values. At the interior prefix join, both
the value and first derivative of $u$ match, so the two boundary
contributions cancel. Expanding in the complete orthonormal polynomial
basis and using Bessel then gives
\[
\|(I-\Pi_p^A)u\|_{L^2}
\le\frac{\|\mathcal L_Au\|_{L^2}}{p(p+1)}. \tag{C2}
\]
For vectors, sum the scalar coefficient inequalities over the coordinates;
the constant remains one and carries no dimension factor.

The actual forward history satisfies this domain condition. Its prefix
derivative is zero. On the right of the join, the first-layer equation in
its own residual clock gives a sum proportional to the carriers $k_a$.
At time zero these carriers vanish because $w_0=0$. Thus its derivative
also approaches zero from the right. A jump in the second derivative
is allowed in (C2); it produces no delta function in $\mathcal L_Au$.
The backward history generally lacks this matching first derivative, which
is why the candidate does not apply (C2) to it.

Only finite $t$, hence finite positive residual and a regular finite
interval $[0,\tau(t)]$, is used to justify integration by parts. The
endpoint at infinite physical time is subsequently handled by uniform
estimates. No assumed smooth extension through that endpoint enters.

## 4. Complete reconstruction of the forward regularity bound

Fix one actual order-$p$ closure, suppress hats, and let primes denote
its clock derivatives. Put
$K_p=\sup_{s\ge0,a}\|k_a(s)\|_\infty$.
The physical RMS bound already gives $K_p\le C\sqrt nY<\infty$.
For the fixed input Gram $G_{ab}=v_a^\top v_b$,
\[
(z_a^{(1)})'=-\frac2m\sum_bG_{ab}c_b
           \tanh'(z_b^{(1)})\odot k_b.
\]
Since $|c_b|\le\sqrt m$, bounded slopes give
\[
\frac{\|(z_a^{(1)})'\|_2}{\sqrt n}\le CY,
\qquad \|(z_a^{(1)})'\|_\infty\le CK_p.
\tag{C3}
\]
The exact readout equation and bounded tanh imply
$\|w\|_\infty\le2Y/\kappa$. The full closure velocity bounds imply
\[
\|W'\|_F\le CY,\quad
\frac{\|w'\|_2}{\sqrt n}\le2,\quad
\frac{\|(z_a^{(2)})'\|_2}{\sqrt n}\le CY.
\]
Therefore
\[
(\delta_a^{(2)})'=w'\odot\tanh'(z_a^{(2)})
 +w\odot\tanh''(z_a^{(2)})\odot(z_a^{(2)})',
\quad
k_a'=W'^\top\delta_a^{(2)}+W^\top(\delta_a^{(2)})'
\]
have normalized Euclidean norms bounded by $C$. This calculation uses no
derivative of $E_2$ and no maximum of the top preactivation velocity.

The residual equation gives $\|\dot c\|_2/\sqrt m\le C$, hence
$\|c'\|_2/\sqrt m\le C/\rho$. Differentiate the first-layer clock
equation. Its three terms contain $c_b'k_b$, $(z_b^{(1)})'k_b$,
and $k_b'$. The first costs $CY/\rho$ in RMS; the second costs
$CYK_p$ by multiplying the RMS in (C3) by the carrier maximum; the
third costs $C$. Hence
\[
\frac{\|(z_a^{(1)})''\|_2}{\sqrt n}
\le C(Y/\rho+1+YK_p).
\]
The activation second derivative adds
$\tanh''(z_a^{(1)})\odot((z_a^{(1)})')^2$. Its RMS is at most
$C\|(z_a^{(1)})'\|_\infty\|(z_a^{(1)})'\|_2/\sqrt n
\le CYK_p$. Consequently
\[
\frac{\|(h_a^{(1)})'\|_2}{\sqrt n}\le CY,
\qquad
\frac{\|(h_a^{(1)})''\|_2}{\sqrt n}
\le C(Y/\rho+1+YK_p). \tag{C4}
\]
There is only one power of $K_p$; estimating both factors in the
coordinatewise square by their maxima would incorrectly lose this fact.

At a finite terminal time $t$, $A=\tau(t)\le2$ and, for $s\le t$,
\[
\eta_A(\tau(s))\le A\int_s^\infty\rho(u)du
\le A\rho(s)/\kappa,\qquad |\eta_A'|\le A.
\]
Insert (C4) into $\mathcal L_Ah=-\eta_Ah''-\eta_A'h'$ and use
$d\xi=\rho(s)ds$. The prefix contributes zero, and
\[
\frac1n\|\mathcal L_Ah_a^{(1)}\|_{L^2(0,A;\mathbb R^n)}^2
\le C\int_0^t[Y^2+\rho(s)^2(1+YK_p)^2]\rho(s)ds
\le CY^3(1+YK_p)^2. \tag{C5}
\]
Here $\int\rho\le Y/\kappa$ and
$\int\rho^3\le Y^3/(3\kappa)$. In particular the possibly singular
$c'$ term is canceled by the vanishing Legendre weight before integration.
Combining (C2) and (C5) proves the candidate's improved forward tail
\[
\frac{\|(I-\Pi_p^A)h_a^{(1)}\|_{L^2(0,A;\mathbb R^n)}}{\sqrt n}
\le CY^{3/2}(1+YK_p)p^{-2}. \tag{C6}
\]

## 5. Backward tail and source multiplication

The bound on $(\delta_a^{(2)})'$ proved above gives
$\|\dot\delta_a^{(2)}\|_2/\sqrt n\le C\rho$.
Since $b_a^{(2)}=c_a\delta_a^{(2)}$,
\[
\frac{\|b_a^{(2)}\|_2}{\sqrt n}\le CY,\qquad
\frac{\|\dot b_a^{(2)}\|_2}{\sqrt n}\le C(Y+\rho).
\]
Freeze this history after physical time $T$. Its difference from the
original is bounded in clock $L^2$ by $CY^{3/2}e^{-\kappa T/2}$,
because only the tail clock mass is affected. For the frozen history,
the weighted first derivative energy is bounded by
$CY^2(1+T)$: changing variables contributes $1/\rho$, canceled by
$A-\tau(s)\le\rho(s)/\kappa$. The first-order Legendre estimate
therefore gives
\[
\frac{\|(I-\Pi_p^A)b_a^{(2)}\|_{L^2(0,A;\mathbb R^n)}}{\sqrt n}
\le C\left[\frac{Y\sqrt{1+T}}p+Y^{3/2}e^{-\kappa T/2}\right].
\]
Taking $T=2\log p/\kappa$ gives $CYp^{-1}\sqrt{\log(e+p)}$,
including $p=1$ after increasing the constant. This is uniform in
the actual current endpoint $A$.

Multiply this estimate by (C6) in (C1), and increase finite terminal
times. Monotonicity of the accumulated absolute defect and a uniform
right side give
\[
\epsilon_p:=\int_0^\infty\|E_2(t)\|_Fdt
\le CY^{5/2}(1+YK_p)p^{-3}\sqrt{\log(e+p)}. \tag{C7}
\]
This establishes the additional power of memory order in the actual
autonomous model, rather than in a recorded dense history.

## 6. Same-time comparison and absorption

Let $D_{n,p}$ be the supremum over physical time of the sum of normalized
first-layer Frobenius, hidden Frobenius, and normalized readout Euclidean
differences. It is finite by the already established physical bounds.
Assume a dense carrier maximum $M\ge1$ for both $k_{D,a}$ and $w_D$.

Forward subtraction costs $CD_{n,p}$ in normalized preactivations.
At the top backward response, subtract as
\[
\widehat\delta_a^{(2)}-\delta_{D,a}^{(2)}
=(\widehat w-w_D)\odot\tanh'(\widehat z_a^{(2)})
+w_D\odot[\tanh'(\widehat z_a^{(2)})-\tanh'(z_{D,a}^{(2)})].
\]
The second multiplier is bounded by $2Y/\kappa$, independent of $M$.
Thus the top-response RMS difference is $CD_{n,p}$. Multiplication by
the bounded hidden operator, and the extra term
$(\widehat W-W_D)^\top\delta_{D,a}^{(2)}$, give the same bound for
the carrier difference. Passing from Euclidean RMS to maximum gives
\[
K_p\le M+C\sqrt nD_{n,p}. \tag{C8}
\]
These are comparisons at the same physical time. No equality of residual
clocks is asserted or needed.

The manuscript's one-reference damping estimate has dense tail exactly
zero above $M$. Retaining the integrated residual activity in its exponent
gives $D_{n,p}\le A_M\epsilon_p$ with $A_M=Ce^{CYM}$.
Put $s_p=p^{-3}\sqrt{\log(e+p)}$. Equations (C7)--(C8) imply
\[
D_{n,p}\le CA_MY^{5/2}s_p(1+YM)
          +CA_MY^{7/2}\sqrt n\,s_pD_{n,p}.
\]
Whenever $CA_MY^{7/2}\sqrt n\,s_p\le1/2$, ordinary algebra yields
\[
D_{n,p}\le CA_MY^{5/2}(1+YM)s_p. \tag{C9}
\]
This is a closed absorption argument for a quantity already known finite;
it neither assumes a preliminary small-discrepancy estimate nor uses a
circular fitting bootstrap.

## 7. Probability dependency and order selection

The imported prior theorem supplies, on dense-only events $\Omega_n$
of probability tending to one,
$M_n=1+C_0Y\sqrt{\log(e+n)}$. Its complete proof and the supplied
checks were inspected, not replaced by a population Gaussian assertion.
The chain used here is finite Gaussian deletion/insertion, a uniform
deterministic-control net, the adaptive negative-Gram variational term,
and a finite empirical-budget stop. The Schatten bound uses instantaneous
rank $O(n)$ and leaves the identity part in a contraction; it therefore
does not introduce an ambient $n^2$ factor.

The potentially delicate probability steps have the correct quantifiers:
all fixed-size deletion sets are unioned at superpolynomial failure cost;
cavity references omit the columns on which Gaussian conditioning is
performed; radial projection supplies a deterministic small-variance
reference before conditioning; and the full stopping event is not used
as an independence event. Fixed empirical moment degree is chosen before
width tends to infinity, then increased to remove the budget stop. The
moment base and small-label threshold stay independent of that degree.
The resulting maximum bound extends from a logarithmic physical horizon
to all time by deterministic residual-tail drift. These are precisely
the finite-network inputs required by (C8)--(C9).

For the present consequence, $A_{M_n}\le Ce^{K\sqrt{\log(e+n)}}$.
Choose fixed $a>K/3$ and
\[
p_n=\left\lceil n^{1/6}e^{a\sqrt{\log(e+n)}}\right\rceil.
\]
Then the absorption coefficient is at most
$C\sqrt{\log(e+n)}e^{-(3a-K)\sqrt{\log(e+n)}}$, hence tends to zero.
After multiplication of (C9) by $\sqrt n$, its right side is at most
\[
C(1+\sqrt{\log(e+n)})\sqrt{\log(e+n)}
     e^{-(3a-K)\sqrt{\log(e+n)}},
\]
which is bounded. This proves $D_{n,p_n}\le Cn^{-1/2}$.

Since $s_p$ decreases for $p\ge1$, the same estimate holds
simultaneously for every $p\ge p_n$ on the same dense-only event.
There is no union over order-dependent random events. The confidence
form is therefore valid: for each $\delta>0$, every sufficiently large
width has success probability at least $1-\delta$. Nonzero labels are
fixed before width; a uniform threshold as $Y\downarrow0$ is not claimed.

## 8. Queries, original-order comparison, endpoint, and state accounting

Whole-input subtraction through the actual shared mixer gives
\[
\sup_{t\ge0}|\widehat f_{n,p}(t,x)-f_{n,D}(t,x)|
\le C(1+\|x\|_2/\sqrt d)D_{n,p}.
\]
The majorant is square integrable under each fixed query law with finite
second moment. Squaring, taking the time supremum, and integrating proves
the requested metric with the supremum inside the query integral. Fixed
bounded query sets are covered uniformly. Parameter convergence from finite
activity extends every comparison to the fitted endpoint.

For an original order $q$, run $p=\min\{q,p_n\}$. When $q\le p_n$,
the two ODEs and initial states coincide exactly. When $q>p_n$, both
order $q$ and order $p_n$ satisfy the dense comparison on the same event.
The pointwise triangle inequality followed by the $L^2(\mu)$ triangle
inequality gives at most $2C_\mu n^{-1/2}$. This holds simultaneously
for every integer $q\ge1$. The dense path is solely a proof reference;
neither simulated closure reads it or obtains histories from it.

The moving scalar count is
$2mnp+n(d+1)+1\le2mnp_n+n(d+1)+1=n^{7/6+o(1)}$.
As $5/4-7/6=1/12$, every fixed $0<\epsilon<1/12$ gives the requested
$O(n^{5/4-\epsilon})$ bound at sufficiently large width. The fixed
$n^2$ mixer storage and dense matrix-vector runtime are unchanged.
Both directions of that mixer and the closure's response memories remain
present in its autonomous updates.

There is no sampling or population-limit replacement in the construction.
All approximation bias from lowering memory order is included in (C7)--(C9)
and the same-realization triangle comparison. Thus no unproved numerical
dense-to-population rate is being hidden in the root-width claim.

The count is sufficient, not optimal. The proof does not establish that
$p=O(n^{1/6})$ without its subpolynomial factor suffices, that smaller
orders are impossible, or that the second-derivative argument extends to
general depth. The remaining repository promotion requirements are separate
from this internal mathematical PASS.
