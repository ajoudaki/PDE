# Independent audit of the two-sample short response lemma

Date: 2026-09-06.

## Verdict

The estimates (3)–(5) pass the mathematical audit for the displayed scalar law, with its stated frozen-coefficient, distinct-source-slot derivative convention. The raw-coordinate argument includes the cross-input gates; the induction closes without using the current bottom response prematurely; all displayed numerical constants and both pointwise Gaussian envelopes check out. No experiment or additional mathematical source was used.

Three repairs are required to make the note fully precise:

1. Lines 119–122 incorrectly say that both deltas vanish **as formal expressions**. The middle delta vanishes almost surely at time zero, but its formal derivative in its zero-variance reverse-source direction is nonzero. The base case remains true; its justification must be corrected.
2. Lines 75–96 do not explicitly specify the finite-width initialization and complete finite realization to which identification is asserted. The Gaussian dependency is conditional on those hypotheses. Identification is justified for the normalized independent Gaussian realization specified below; this setup should be stated in the candidate. This is a specification gap in the finite-scheme assertion, not a failure of the scalar estimates or a missing regularity argument.
3. Lines 315–317 have a sign error for the permitted same-label choice $y_1=y_2=-1$. The positive derivative is that of the label-aligned readout. The auxiliary quantity $g$ also needs a definition if that scope remark is retained.

I found no substantive obstruction to applying dependency Section 3 once the finite realization is specified. In particular, the two backward clips and the bounded-readout extension suffice for its actual coordinate-map hypotheses. No full-theorem, clipping-removal, or opposite-label continuation result is being certified here.

## Sources and exact fingerprints

The candidate was read in full, lines 1–332. Its SHA-256 is:

```text
1122f36422ffb4f75e555978653afeac7ad9c6217c8a9c354b40ada9e3cf6a08
/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md
```

The Gaussian dependency has SHA-256:

```text
bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e
/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md
```

This agrees with the hash declared by the candidate. The mathematical dependency inspected was Section 3, lines 258–476, together with preceding lines 18–62 and 165–212 as needed for matrix normalization, initialization conventions, activation bounds, the operator-norm event, and the stated Wasserstein convergence criterion. No mathematical material after Section 3 was read. Exact hashes of these newline-preserving excerpts are:

```text
950273bdf1d6186ffd4b4b7c2524ad0449278912f3d4914934c61f65efaa4bec  lines 258–476
6f62c82709aa984a3469279f9eab41f162891588f72de78b23a85d0934ddb50a  lines 18–62
f89529e9c3b33a14b8601a6f6a4eb2ff3358cb326ad6acb6b8f785e5584f5244  lines 165–212
```

The mandatory procedural skill was read directly and completely:

```text
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
/etc/codex/skills/solve-math-rigorously/SKILL.md
```

No prior review, other research, thread history, agent, or experiment was consulted. The candidate was not edited.

## 1. Source indexing, response law, and finite-program identification

Write $\langle u,v\rangle_n=n^{-1}u^Tv$. The finite realization sufficient for the identification assertion is the following:

- The neuron root tuples $(z^{(1)}_{0,i1},z^{(1)}_{0,i2})$, $1\le i\le n$, are iid centered Gaussian with covariance $C$.
- $W^{(2)}_0,W^{(3)}_0$ have independent $N(0,1/n)$ entries and are independent of each other and of those root tuples.
- $W^{(4)}_0=0$ exactly.
- All forward actions use the current matrices; reverse queries are $q^{(2)}_{ka}=(W^{(3)}_k)^T\delta^{(3)}_{ka}$ and $q^{(1)}_{ka}=(W^{(2)}_k)^T\delta^{(2)}_{ka}$. The readout, gates, clips, bottom update with $C_{ab}$, and matrix updates are precisely the finite vector versions of candidate (1) and lines 77–78, with simultaneous Euler updates after processing both samples.

These hypotheses are compatible with the candidate. However, a scalar root pair and a matrix-update formula alone do not state the finite initialization. In particular, the dependency's preceding single-sample model has a nonzero random finite-width readout initialization. That initialization must not be silently substituted for the exactly zero initialization of this lemma.

Unrolling the hidden matrices gives, exactly at finite width,

\[
W^{(\ell)}_k h^{(\ell-1)}_{ka}
=W^{(\ell)}_0h^{(\ell-1)}_{ka}
+\frac\Delta2\sum_{r<k,b}y_b\delta^{(\ell)}_{rb}
  \langle h^{(\ell-1)}_{rb},h^{(\ell-1)}_{ka}\rangle_n,
\]

\[
(W^{(\ell)}_k)^T\delta^{(\ell)}_{ka}
=(W^{(\ell)}_0)^T\delta^{(\ell)}_{ka}
+\frac\Delta2\sum_{r<k,b}y_b h^{(\ell-1)}_{rb}
  \langle\delta^{(\ell)}_{rb},\delta^{(\ell)}_{ka}\rangle_n.
\]

Thus both learned coefficients have the factor $(\Delta/2)y_b$, with the label on the historical update sample $b$. There is no extra $C_{ab}$ in these learned hidden-matrix coefficients. $C$ enters the bottom dynamics and the resulting input moments.

For each time, process both bottom fields, both layer-2 forward calls, both layer-3 forward calls, both layer-3 reverse calls, and then both layer-2 reverse calls. This is an admissible ordering of the simultaneous Euler scheme. Dependency (3.5) then gives:

| Matrix direction | Source | Input determining its uncentered covariance | Opposite-direction response slots |
| --- | --- | --- | --- |
| $W^{(2)}_0$, forward | $\xi^{(2)}_{ka}$ | $H^{(1)}_{ka}$ | $\zeta^{(1)}_{rb}$, $r<k$ |
| $W^{(2)}_0$, reverse | $\zeta^{(1)}_{ka}$ | $\delta^{(2)}_{ka}$ | $\xi^{(2)}_{rb}$, $r\le k$ |
| $W^{(3)}_0$, forward | $\xi^{(3)}_{ka}$ | $H^{(2)}_{ka}$ | $\zeta^{(2)}_{rb}$, $r<k$ |
| $W^{(3)}_0$, reverse | $\zeta^{(2)}_{ka}$ | $\delta^{(3)}_{ka}$ | $\xi^{(3)}_{rb}$, $r\le k$ |

The initially reused matrix therefore contributes exactly the expected derivatives in (2). Forward responses are strictly past. Reverse responses include the current forward block, whereas learned reverse terms remain strictly past. Full sample/time covariances, uncentered second moments, and independence between the four oriented source groups agree with dependency Section 3.3. No independence between two samples within a group is required.

Here is the check of the substantive finite-program premises, rather than merely an invocation of the dependency:

| Dependency premise | Verification for the specified finite realization |
| --- | --- |
| Fixed finite instruction sequence | At fixed $M,\Delta,R_1,R_2$, at most $8(M+1)$ initial-matrix calls are needed. No width-dependent number of calls is used. |
| Independent normalized Gaussian matrices | Supplied by the explicit initialization above; the candidate should state it. |
| Iid root tuples, independent of matrices, with finite moments | The two samples form one Gaussian tuple per bottom neuron. Singular $C$ is allowed. The other populations can have deterministic roots. |
| No unauthorized coordinate mixing between populations | Gates and sample combinations are local within a neuron population. Hidden-layer mixing uses matrix actions. Learned terms use the explicitly allowed scalar contractions. |
| $C^1$, globally Lipschitz coordinate maps with bounded first derivatives | Verified below using both clips and a bounded readout extension. Constants may depend on the fixed caps and program. |
| Deterministic contractions before empirical restoration | All learned coefficients are moments of already available $H$'s or deltas. Current contractions are formed only after their inputs exist. |
| Stability on restoring empirical contractions | $H$, both deltas, and the readout are bounded at fixed caps. Inner products are continuous quadratic-growth tests under the dependency's joint $\mathcal W_2$ convergence. A finite induction, using the initial-matrix operator-norm event, restores the contractions. |
| Singular input Grams | Dependency Section 3.4 supplies fresh input perturbations, fixed-program stability, convergence of bounded formal derivatives, and removal of those perturbations. No inverse-limit or nonsingularity assumption is needed. |
| Correct derivative convention | Keep coefficients and source covariance parameters fixed and retain distinct source slots. The correction to the base-time wording below is necessary to state this consistently. |

For the regularity row, the two potentially problematic maps are

\[
f_R(z,q)=\phi'(z)\tau_R(q),\qquad
|\partial_z f_R|\le\frac{2R}{5},\quad
|\partial_q f_R|\le\frac1{10}.
\]

They are globally $C^1$ and Lipschitz. This covers both the raw bottom update and the middle delta. The raw Gaussian bottom coordinate is only added or passed through bounded smooth gates; it is never multiplied as an unbounded coordinate by another unbounded field.

For the top delta, choose a smooth bounded function $\chi$ with bounded derivative that equals $w$ on a neighborhood of $[-aS,aS]$, and use $\chi(w)\phi'(z)$. Its first derivatives are bounded. Since

\[
|W^{(4)}_k|
\le\frac\Delta2\sum_{r<k,b}|H^{(3)}_{rb}|
\le aS,
\]

this extension preserves both values and first derivatives on all attained scalar and finite-program states. Bounded products used as contraction inputs can likewise be extended on their known bounded argument ranges. No bound on $\tau_R''$ is needed: the dependency asks for bounded first derivatives of the coordinate maps, not bounded second derivatives.

The projection, integration-by-parts, and singular-perturbation arguments in dependency Section 3 apply under these verified hypotheses. Their fixed-program constants need not be uniform in $M$ or the caps. The uniform estimates below concern the resulting scalar recursion and do not interchange width and growing-program limits.

## 2. Base case and noncircular construction

The literal claim at candidate lines 119–122 is false for the formal middle expression. At time zero,

\[
W^{(4)}_0\equiv0,\quad \delta^{(3)}_{0a}\equiv0,
\quad B^{(3)}_{0a,0b}=0.
\]

The Gaussian source $\zeta^{(2)}_{0a}$ has zero variance, but the unsimplified formal expressions are

\[
q^{(2)}_{0a}=\zeta^{(2)}_{0a},\qquad
\delta^{(2)}_{0a}
=\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a}).
\]

Consequently

\[
\left.\partial_{\zeta^{(2)}_{0b}}\delta^{(2)}_{0a}
\right|_{\zeta^{(2)}_0=0}
=\mathbf1_{a=b}\phi'(\xi^{(2)}_{0a})>0
\quad\text{when }a=b.
\]

Nevertheless, the derivative used for $B^{(2)}_0$ is a **forward-source** derivative:

\[
\left.\partial_{\xi^{(2)}_{0b}}\delta^{(2)}_{0a}
\right|_{\zeta^{(2)}_0=0}
=\mathbf1_{a=b}\phi''(\xi^{(2)}_{0a})\tau_{R_2}(0)=0.
\]

There is no learned row at time zero, so $U_0=V_0=0$. Also $\zeta^{(1)}_0=0$ almost surely and $q^{(1)}_0=\zeta^{(1)}_0$ formally. Its raw bottom-gate derivative in its own source direction remains $\phi'(G_a)$. This establishes the intended base case without deleting zero-variance source directions.

At step $k\ge1$, a precise causal order is:

\[
\begin{gathered}
H^{(1)}_k\ ;\ (A^{(2)}_k,\xi^{(2)}_k,Z^{(2)}_k,H^{(2)}_k)\ ;\\
(A^{(3)}_k,\xi^{(3)}_k,Z^{(3)}_k,\delta^{(3)}_k)\ ;\\
(B^{(3)}_k,\zeta^{(2)}_k,q^{(2)}_k,\delta^{(2)}_k)\ ;\\
(B^{(2)}_k,\zeta^{(1)}_k,q^{(1)}_k).
\end{gathered}
\]

Each new covariance block is an uncentered Gram matrix of already constructed inputs and is positive semidefinite. It consistently extends the previous covariance block, including in singular cases. Thus covariance selection does not introduce an implicit equation for the current responses.

The bottom estimate for $A^{(2)}_k$ uses only $U_r,V_r$ with $r<k$. The middle estimates for $A^{(3)}_k$ and $E^{(2)}_k$ use only $V_r$ with $r<k$. The top estimate then gives $V_k$. Only after that are $q^{(2)}_k$ and $U_k$ bounded. The sharper historical bound $Q_*$ is available because previous completed steps established $V_r\le V_*$, not just $V_r\le1$. There is no bootstrap circularity.

## 3. Raw bottom derivative, including cross-input gates

The activation constants themselves are valid: $\phi'(z)=1/[10(1+z^2)]$ and $\phi''(z)=-z/[5(1+z^2)^2]$ give $0<\phi'\le1/10$ and $|\phi''|\le1/5$. The dependency's bound $\pi<10/3$, together with $|\arctan z|<\pi/2$, gives $5/6<\phi(z)<7/6$. All correlation dependence below uses the positive semidefiniteness of $C$ and $\frac12\sum_c|C_{ac}y_c|\le1$. This covers $\rho=1$ and $\rho=-1$, both label signs, and both label modes without inverting $C$.

Fix a source slot $\zeta^{(1)}_{sb}$, and write $d$ for its formal derivative. Direct differentiation, before taking any maximum, gives

\[
dZ^{(1)}_{ja}
=\frac\Delta2\sum_{r<j,c}C_{ac}y_c
\left[
\phi''(Z^{(1)}_{rc})\tau_{R_1}(q^{(1)}_{rc})dZ^{(1)}_{rc}
+\phi'(Z^{(1)}_{rc})\tau'_{R_1}(q^{(1)}_{rc})
\left(\mathbf1_{(r,c)=(s,b)}
+\sum_{v\le r,e}B^{(2)}_{rc,ve}\phi'(Z^{(1)}_{ve})dZ^{(1)}_{ve}\right)
\right].
\]

Both the differentiated gate at sample $c$ and every cross-sample gate in the return through $B^{(2)}$ are present.

Before time $s+1$ the variation is zero. Its direct injection has size at most $\Delta/20$. With

\[
D_r=\max_{v\le r,c}|dZ^{(1)}_{vc}|,
\qquad \frac12\sum_c|C_{ac}y_c|\le1,
\]

the remaining terms are bounded by

\[
\Delta\sum_{r<j}
\left(\frac{\max_c|q^{(1)}_{rc}|}{5}+\frac{U_r}{100}\right)D_r.
\]

The product-form discrete Gronwall bound, starting at the injection, followed by the outer factor $\phi'\le1/10$, proves

\[
|\partial_{\zeta^{(1)}_{sb}}H^{(1)}_{ja}|
\le\frac\Delta{200}E^{(1)}_j.
\]

Thus the coefficient in (6) is correct. There is no replacement of a raw derivative by a natural-coordinate derivative.

For past times,

\[
\|q^{(2)}_{ra}\|_2\le\frac{aS}{10}+a
\le\frac{161}{120}=Q_0,
\quad \operatorname{sd}(\zeta^{(1)}_{ra})\le\frac{Q_0}{10},
\quad \max_a|q^{(1)}_{ra}|\le\max_a|\zeta^{(1)}_{ra}|+a.
\]

For a two-component centered Gaussian vector with component variances at most $v$, the needed bound is

\[
\mathbb E e^{\lambda\max_a|G_a|}
\le\sum_{a=1}^2\mathbb E e^{\lambda|G_a|}
\le4e^{\lambda^2v/2},\qquad\lambda\ge0.
\]

The factor four accounts for two samples and two signs. No independence between samples is used. For $j\ge1$, apply convexity to the average over the $j$ time slots with exponent coefficient $j\Delta/5\le S/5$. This is time Jensen, not a union over time, so no factor depending on $M$ is missing. The $j=0$ case is immediate.

It follows that

\[
\mathbb E E^{(1)}_j
\le4\exp\left\{\frac{73}{200}
+\frac9{200}\left(\frac{161}{1200}\right)^2\right\}
<4e^{2/5}<6.
\]

Hence

\[
|A^{(2)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{50}\right)
=\frac\Delta2\frac{1279}{900}
<\frac\Delta2\frac32.
\]

## 4. Middle derivative rows and reverse-source injection

Let $R_{ja}$ be the total absolute $\xi^{(2)}$-derivative row of $Z^{(2)}_{ja}$, and set $R_j=\max_aR_{ja}$. There is one direct source entry in that row, namely $(j,a)$, so its direct contribution is one. It is not two and it is not the number of all past source slots.

Because the other source slots, all deterministic coefficients, and the covariance parameters are held fixed during a formal variation,

\[
|d\delta^{(2)}_{ra}|
\le\frac{|q^{(2)}_{ra}|}{5}|dZ^{(2)}_{ra}|
+\frac1{100}\sum_{v\le r,b}|B^{(3)}_{ra,vb}|\,|dZ^{(2)}_{vb}|.
\]

The response row includes both sample indices and its current-time entries. Summing over forward-source slots and then the two update samples gives

\[
R_j\le1+A\Delta\sum_{r<j}
\left(\frac{\max_a|q^{(2)}_{ra}|}{5}+\frac{V_r}{100}\right)
\max_{v\le r}R_v.
\]

The two update samples turn $A\Delta/2$ into $A\Delta$. This proves (10).

For one reverse source $\zeta^{(2)}_{sb}$, $Z^{(2)}_s$ has no current reverse-source dependence. Only $\delta^{(2)}_{sb}$ has the direct injection, of size at most $1/10$. Its first forward contribution has size at most $A\Delta/20$. The same propagation bound, with the final activation derivative, gives (11), including its coefficient $A\Delta/200$.

The two-sample Gaussian maximum and time Jensen now give, for every $p\ge1$,

\[
\mathbb E(E^{(2)}_j)^p
\le4\exp\left\{
pAS\left(\frac a5+\frac1{100}\right)
+\frac12\left(\frac{pAS}{5}\right)^2\left(\frac{aS}{10}\right)^2
\right\}
\le4\exp\left\{\frac{219p}{400}+\frac{3969p^2}{1280000}\right\}.
\]

In particular,

\[
\mathbb E E^{(2)}_j<8,\qquad
\|E^{(2)}_j\|_2
\le2\exp\left\{\frac{219}{400}+\frac{7938}{1280000}\right\}
<\frac72.
\]

Thus

\[
|A^{(3)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{25}\right)
=\frac\Delta2\frac{1333}{900}
<\frac\Delta2\frac32.
\]

The strict coefficient margin is $17/900$, as asserted. Taking a maximum of the absolute derivative rows before expectation does not lose an additional sample factor: the deterministic response row satisfies

\[
\max_a\sum_{s,b}|\mathbb E D_{a,sb}|
\le\max_a\mathbb E\sum_{s,b}|D_{a,sb}|
\le\mathbb E\max_a\sum_{s,b}|D_{a,sb}|.
\]

## 5. Top row, current middle row, and exact endpoint constants

For the top forward-source derivative rows $T_j$, differentiating the readout explicitly gives

\[
\max_a\sum_{s\le j,b}
|\partial_{\xi^{(3)}_{sb}}\delta^{(3)}_{ja}|
\le\frac\Delta{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
\le\frac{73}{300}S\max_{v\le j}T_v.
\]

Here the two readout samples exactly cancel the denominator two in its update. The first term carries two factors $1/10$, one from differentiating the past activation and one from the current top gate.

The strictly past forward recursion then yields

\[
\max_{v\le j}T_v
\le\exp\{A(73/300)S^2\}
\le e^{657/800}<\frac52.
\]

Each learned top covariance has magnitude at most $(aS/10)^2$. There are two sample slots per past time, each weighted by $\Delta/2$. Thus

\[
V_k\le\frac{73}{300}S\frac52+\frac{a^2S^3}{100}
\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}=V_*<1.
\]

Minkowski's inequality, without any source/shift independence assumption, now gives

\[
\|q^{(2)}_{ka}\|_2\le\frac{aS}{10}+aV_*
\le\frac7{40}+\frac76\frac{3067}{3200}
=\frac{24829}{19200}=Q_*.
\]

This holds at all previous completed steps as well. Retaining the full current return in $q^{(2)}_k$, the current middle derivative row is bounded by

\[
\sum_{s\le k,b}
|\partial_{\xi^{(2)}_{sb}}\delta^{(2)}_{ka}|
\le\left(\frac{|q^{(2)}_{ka}|}{5}+\frac{V_k}{100}\right)E^{(2)}_k.
\]

Cauchy–Schwarz applies even though $q^{(2)}_k$ and $E^{(2)}_k$ are dependent. The learned bottom covariance row contributes at most

\[
\frac\Delta2\sum_{r<k,b}
\|\delta^{(2)}_{ka}\|_2\|\delta^{(2)}_{rb}\|_2
\le\frac{S}{100}Q_*^2\le\frac3{200}Q_*^2.
\]

Consequently

\[
U_k\le\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}<1.
\]

The exact arithmetic behind the last value is

\[
Q_*^2=\frac{616479241}{368640000},\qquad
\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
=\frac{1802437}{1920000},
\]

\[
\frac{1802437\cdot38400+1849437723}{73728000000}
=\frac{71063018523}{73728000000},\qquad
\frac{97}{100}-\frac{71063018523}{73728000000}
=\frac{453141477}{73728000000}>0.
\]

The strict elementary exponential comparisons used throughout can all be certified without numerical approximation. The exponential series gives

\[
e<\frac{163}{60}+\frac7{4320}
=\frac{11743}{4320}<\frac{68}{25}<\frac{11}{4}<3.
\]

The tail bound here uses $1/6!$ times a geometric series of ratio $1/7$. Then:

- $e^{2/5}<3/2$, because $121/16=242/32<243/32=(3/2)^5$.
- The bottom exponent is $105353289/288000000<2/5$.
- The middle $p=1$ exponent is $704769/1280000<3/5$, and $3^3<2^5$ proves $e^{3/5}<2$.
- The exponent after taking the $p=2$ square root is $354369/640000$, and $5/9-354369/640000=10679/5760000>0$.
- For $e^{5/9}<7/4$, the candidate's integer comparison is correct:
  $68^5 4^9=381139961249792<394078193359375=25^5 7^9$.
- $657/800<5/6$, and $3^5 2^6=15552<15625=5^6$ proves $e^{5/6}<5/2$.

All constants in (6)–(16) are therefore consistent. The argument uses neither a lower bound on $\Delta$ nor a small-mesh assumption. For $M=0$, the response rows vanish, the forward-coefficient claim is vacuous, and both query exponential moments equal one.

## 6. Both actual-query Gaussian envelopes

For each individual time and sample, both layers have the representation

\[
q^{(j)}_{ka}=\zeta^{(j)}_{ka}+\beta^{(j)}_{ka},
\qquad |\beta^{(j)}_{ka}|\le a,
\]

because the corresponding deterministic absolute response row is less than one and each activation is bounded by $a$. The two variance bounds are separately justified:

\[
\operatorname{Var}(\zeta^{(2)}_{ka})
=\mathbb E(\delta^{(3)}_{ka})^2
\le\left(\frac7{40}\right)^2,
\]

\[
\operatorname{Var}(\zeta^{(1)}_{ka})
=\mathbb E(\delta^{(2)}_{ka})^2
\le\left(\frac{Q_*}{10}\right)^2
<\left(\frac7{40}\right)^2.
\]

The last strict inequality follows already from $24829<33600$, equivalently $Q_*<7/4$. The pointwise inequality $q^2\le2\zeta^2+2a^2$ does not require independence of the shift and source. For a centered Gaussian with variance $\sigma^2<4$, direct integration gives

\[
\mathbb E e^{\zeta^2/8}=(1-\sigma^2/4)^{-1/2}.
\]

It follows for **both** reverse layers that

\[
\mathbb E e^{(q^{(j)}_{ka})^2/16}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]

Indeed, $49/288<1/5$, $e^{1/5}\le\sum_{m\ge0}(1/5)^m=5/4$, and

\[
(1-49/6400)^{-1/2}=\frac{80}{\sqrt{6351}}<\frac43.
\]

The displayed upper bound is therefore less than $5/3$, which is stronger than required. This also gives the separate pointwise tail bounds

\[
\mathbb P(|q^{(j)}_{ka}|>t)\le2e^{-t^2/16},\qquad t\ge0,
\]

with the harmless replacement of a strict bound by a weak one. No claim about a maximum over all times is established or needed here. A simultaneous maximum over multiple samples or layers would require its own union factor; the candidate does not assert such an envelope.

## 7. Required candidate repairs

**R1 — Correct the formal-zero statement, lines 119–122.** Replace it with the following substance:

> At time zero, $\delta^{(3)}_0\equiv0$, hence $B^{(3)}_0=0$ and $\zeta^{(2)}_0=0$ almost surely. Keep the formal expressions $q^{(2)}_0=\zeta^{(2)}_0$ and $\delta^{(2)}_0=\phi'(\xi^{(2)}_0)\tau_{R_2}(\zeta^{(2)}_0)$. Their forward-source derivatives vanish on the attained Gaussian law, so $B^{(2)}_0=0$, and $U_0=V_0=0$. Neither this step nor later differentiation deletes a zero-variance source slot.

This is a necessary consistency correction, not a change to the numerical induction.

**R2 — State the finite realization, before lines 75–96.** Add the iid two-sample Gaussian neuron initialization with covariance $C$, the two independent initial matrices with iid $N(0,1/n)$ entries, independence of matrices and roots, exactly zero readout, and the finite forward/reverse definitions with simultaneous updates. State identification for this fixed-$M,\Delta,R_1,R_2$ program. The existing Lipschitz-extension argument is valid; the explicit bounds in Section 1 of this review can be included if a fully spelled-out application is desired. There is no need to introduce a new theorem uniform in the number of queries.

**R3 — Fix or remove the auxiliary same-label remark, lines 315–321.** For common label $y\in\{-1,1\}$, the literal readout derivative is

\[
\frac{dW^{(4)}}{ds}=\frac y2(H^{(3)}_1+H^{(3)}_2).
\]

Thus $d(yW^{(4)})/ds\ge m$, whereas $dW^{(4)}/ds\le-m$ for $y=-1$. If retaining the conditional hitting-time remark, define $f_a=\mathbb E[W^{(4)}H^{(3)}_a]$ and $g=y(f_1+f_2)/2$. Under the explicitly deferred gradient-flow premises, its readout contribution to the label-mode kernel is

\[
\mathbb E\left[\left(\frac{H^{(3)}_1+H^{(3)}_2}{2}\right)^2\right]\ge m^2,
\]

so $g(0)=0$ and $g'\ge m^2$ would give the stated bound $1/m^2=36/25<3/2$. This corrects the sign and notation; it does not supply the deferred existence, clipping-removal, symmetry, or physical-clock arguments.

No other repair to the short scalar response estimates was found. The explicitly deferred full-theorem obligations are outside this audit and are not grounds for rejecting this short feature-interval lemma.
