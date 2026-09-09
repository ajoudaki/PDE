**CLEAN.** Theorem SD, its explicit constant, the sharpness assertion, and the restricted dyadic consequence are mathematically justified under the stated assumptions. I found no required correction. The proof does not need Section 8 or any other mathematical source beyond the supplied files and elementary calculus/Gaussian integration.

The audit covered every line of `shallow.md`, `NOTATION.md`, and `INPUTS.json`. All input files remained unchanged.

**Read and hash ledger**

The candidate directory was `/tmp/pde_assembly2_shallow_r1`. The complete input ledger is:

| File | Lines read | Bytes before/after | Verification |
|---|---:|---:|---|
| `shallow.md` | 1–551 | 17,318 / 17,318 | SHA-256, bytes, and lines match `INPUTS.json` before and after |
| `NOTATION.md` | 1–98 | 5,110 / 5,110 | SHA-256, bytes, and lines match `INPUTS.json` before and after |
| `INPUTS.json` | 1–12 | 286 / 286 | SHA-256 unchanged; manifest contains no self-hash |

The following SHA-256 values were obtained identically before and after the mathematical audit:

```text
shallow.md
4321fc6bf9fdddedccb752072f3326134d514edbdd576c328923432e4345efd9

NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b

INPUTS.json
0da4173c89588799ec10b57eb170a31998b68a74402c54f5e812c18a926a46e1
```

I personally read the following procedural instructions completely:

| Instruction file | Lines | Bytes |
|---|---:|---:|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 115 | 7,593 |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 185 | 11,286 |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | 99 | 5,946 |
| `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md` | 157 | 5,518 |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 121 | 6,010 |

Their recorded SHA-256 values, in the same order, were:

```text
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de
7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e
9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e
8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501
```

One combined display truncated part of `shallow.md`; subsequent untruncated reads covered lines 1–240 and 238–551. `NOTATION.md` and `INPUTS.json` were also displayed completely. Thus the audit did not rely on truncated coverage.

No checkout, studies, other packet, task history, prior verdict, or external source was inspected. No delegation, numerical experiment, symbolic computation, or file modification was performed. Tool use was confined to reading files and obtaining line counts, byte counts, and hashes.

**Model, notation, and scope**

The candidate specifies the necessary contract:

| Item | Exact scope |
|---|---|
| Architecture/data | One hidden layer, one sample, scalar input, \(x_1=1\) |
| Initialization | All stored \(a_i^0,u_i^0\) independent \(N(0,1)\) |
| Activation | Real \(C^{12}\), normalized by \(E\phi(G)^2=1\), with the finite displayed growth/derivative bound \(M\) |
| Updates | Simultaneous explicit Euler feature-ascent updates (SD1) |
| Mobilities | Both blocks have mobility \(n\) |
| Observable | \(n^{-1}\sum_i a_i\phi(u_i)\), and its population expectation |
| Metric | Absolute scalar error; ordinary Euclidean-induced derivative norms |
| Step estimate | Every integer \(k\ge1\), every real \(|h|\le(16Mk)^{-1}\) |
| Width statement | Exact equality of expectations at every finite width, for fixed finite \(N,h\) |
| Dyadic limit | Uniform convergence of expected terminal outputs along \(N=2^p\), on \([-S,S]\), \(0<S\le2c_\phi\) |
| Physical training | No identification with physical loss-GD steps or their continuous-time limit |

The order-one readout initialization is explicitly distinguished from the small-readout convention in `NOTATION.md`. The scalar \(h\), population coordinates, auxiliary two-dimensional state, and scalar envelopes are typed sufficiently to avoid a substantive notation conflict.

For the shallow output,
\[
\partial_{a_i}f_{n,1}=\frac{\phi(u_i)}n,\qquad
\partial_{u_i}f_{n,1}=\frac{a_i\phi'(u_i)}n.
\]
Multiplication by mobility \(n\) gives precisely (SD1). No width factor is missing.

The backpropagation convention in `NOTATION.md`, lines 31–42, follows by differentiating its network definition. With the stated squared loss, one sample, and label one, the scalar factor relating loss descent to feature ascent is
\[
-2r=2(1-f),
\]
as stated. This relation is a continuous-flow clock relation and does not convert a finite loss-GD update into a fixed feature step.

The arctangent primitive statements have the stated calculus basis: the relevant derivatives are \(1+z^2\) and \(10(1+z^2)\), respectively reciprocal to the corresponding activation derivatives. The warning about finite Euler updates is valid because nonlinear coordinate changes introduce higher-order increments.

The population pairing, rank-one representative \(uv^T/n\), ordinary finite norms, and distinctions between finite collections of function fields and finite-dimensional scalar states are consistent. General remarks about other population operators are not used as premises of this shallow theorem.

**Independent check of width identification and state growth — (SD13)–(SD14)**

Writing \(R(z)=1+|a|+|u|\), the update gives
\[
\begin{aligned}
R(E_{\alpha h}z)
&\le R(z)+\alpha|h|
 \bigl(|\phi(u)|+|a|\,|\phi'(u)|\bigr)\\
&\le (1+\alpha M|h|)R(z).
\end{aligned}
\]
Consequently,
\[
|\psi(E_h^Nz_0)|
\le M(1+M|h|)^{2N}R(z_0)^2.
\]
This is Gaussian-integrable for every fixed finite \(N,h\).

Each neuron depends only on its own initial pair, so different neurons remain independent and identically distributed. The two coordinates within a pair need not remain independent; the proof does not assume that they do. Linearity of expectation therefore gives
\[
E f_{n,1}^N(h)=F_{N,1}(h)
\]
at every width.

This is an exact expectation identity. The candidate does not incorrectly promote it to a random-output convergence theorem.

**Independent check of the transported defect — (SD15)–(SD17)**

Direct subtraction yields
\[
E_h(E_hz)-E_{2h}z
=h\bigl(g(z+hg(z))-g(z)\bigr)
=h^2\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau.
\]
Thus (SD15) is exact for either sign of \(h\), including its continuous definition at zero.

To check the telescoping order, define
\[
H_q=\psi(B_h^q C_h^{k-q}z).
\]
Then, with \(x_q=C_h^{k-1-q}z\) and \(v_q=\psi\circ B_h^q\),
\[
H_q-H_{q+1}
=v_q(C_hx_q)-v_q(B_hx_q).
\]
Applying the fundamental theorem of calculus along the segment from \(C_hx_q\) to \(B_hx_q\) gives the negative sign in (SD16). Summing over \(q=0,\ldots,k-1\) gives exactly
\[
\psi(C_h^kz)-\psi(B_h^kz)=h^2Q_k(h,z).
\]

There is no commutation assumption, missing transport factor, or substitution of a local defect for its propagated effect. The interpolation identity
\[
C_hx+\tau h^2b_h(x)=(1-\tau)C_hx+\tau B_hx
\]
is also exact.

**Independent check of every constant recursion — (SD5)–(SD12), (SD18)–(SD27)**

The radius and amplification identity are correct:
\[
c=\frac1{16M},\qquad \Lambda=12MR,\qquad
4c\Lambda=3R,\qquad P=e^{3R}.
\]

The endpoint paths use at most \(4k\) Euler coefficient units. Convexity of \(R\) controls their interpolation, after which at most \(2k\) additional fine steps occur. Hence
\[
R(z)\le e^{6M|h|k}R(z_0)
\le e^{3/8}R(z_0)<2R(z_0).
\]
This argument does not treat the interpolation as an Euler step.

For \(q\ge1\), evaluation of \(D^qg\) on unit directions contains a first-coordinate term bounded by \(M\), a second-coordinate term bounded by \(M|a|\), and \(q\) second-coordinate terms bounded by \(M\). Therefore the displayed \(6MR(z)\) bound is valid through \(q=4\). For \(D^j\psi\), the analogous count gives \(5MR(z)\) through \(j=4\), with the first derivative using the growth bound for \(\phi\). The \(q=0\) bound follows directly from \(g\). All required derivatives are consequently bounded by \(\Lambda\) along the relevant paths.

I checked the recursions as follows:

| Recursion | Independent verification |
|---|---|
| \(X_1\), (SD6) | At most \(4k\) coefficient units contribute source \(\Lambda\), with amplification \(P\), giving \(4P\Lambda k\) |
| \(X_2\), (SD6) | The normalized source sum is \(8\Lambda X_1+4c\Lambda X_1^2\) |
| \(X_3\), (SD6) | The normalized source sum is \(12\Lambda(X_1^2+X_2)+4c\Lambda(X_1^3+3X_1X_2)\) |
| \(\mathcal G_j\), (SD7) | These are the chain-rule bounds through order three, with coefficients \(1\), \(1,1\), and \(1,3,1\) |
| \(\mathcal B_j\), (SD7) | Leibniz differentiation of \(Dg(\cdot)[g(\cdot)]\) gives exactly the displayed binomial convolution |
| \(\mathcal Z_j\), (SD8) | Differentiating \(h^2b_h(x_q)\) gives coefficients \(1,2j,j(j-1)\); normalization by \(k^j\) gives the stated upper bound |
| \(T_j\), (SD9) | Repeating the path estimates for at most \(2k\) fine steps gives source coefficients \(2,4,6\), and \(2c\), with initial contributions \(\mathcal Z_j\) |
| \(\mathcal H_j\), (SD10) | The same composition formulas apply to \(Dg\) and \(D\psi\) along the post-interpolation path |
| \(V_0\), (SD11) | Tangent propagation of the initial direction costs at most \(P\), giving \(P\mathcal B_0\) |
| \(V_j\), (SD11) | The differentiated tangent recurrence gives exactly the \(2c\) and \(2j\) sums displayed |
| \(\mathcal C_M\), (SD11) | Leibniz differentiation of \(D\psi(z)[\omega]\), followed by the \(k\) defect summands, gives the stated factor \(6\mathcal C_M(R)k^4\) |

Two potentially delicate normalizations merit explicit confirmation.

First,
\[
\partial_h^j(h^2b_h)
=h^2b_h^{(j)}+2jh\,b_h^{(j-1)}
+j(j-1)b_h^{(j-2)}.
\]
Using \(\|b_h^{(r)}\|\le\mathcal B_r k^r\), the three contributions after division by \(k^j\) are bounded respectively by
\[
\frac{c^2}{k^2}\mathcal B_j,\qquad
\frac{2jc}{k^2}\mathcal B_{j-1},\qquad
\frac{j(j-1)}{k^2}\mathcal B_{j-2}.
\]
Dropping \(k^{-2}\le1\) proves the deliberately loose (SD8), including \(j=1\).

Second, in the tangent recurrence, the first source sum contains \(h\) and derivatives whose normalized product scales like \(k^j\). Summing at most \(2k\) steps gives \(2c\). The second sum has derivative product \(k^{j-1}\); its \(j\) prefactor and at most \(2k\) steps give \(2j\). Thus no derivative of the transported initial direction is omitted.

All recursions are finite, nonnegative, and acyclic. The \(V_j\) recursion uses only lower \(V\)-indices. Their dependence is exclusively on \(M\), the integration variable \(R\), and fixed arithmetic operations. No trained trajectory or unknown regularity modulus enters the constant.

**Gaussian integrability and all expectation interchanges**

Every envelope is a finite polynomial in \(c,\Lambda,P\). Since \(c\le1\), \(\Lambda=12MR\), and \(P=e^{3R}\), each is bounded by
\[
C(1+R)^d e^{\lambda R}
\]
for finite constants depending only on \(M\) and the finite recursion.

For the two independent Gaussian marks,
\[
R=1+|a_0|+|u_0|,
\]
this is integrable. Polynomial factors can be separated using
\[
1+|a_0|+|u_0|
\le(1+|a_0|)(1+|u_0|),
\]
and each resulting one-dimensional integral is finite because
\[
\lambda|x|-\frac{x^2}{2}\le-\frac{x^2}{4}
\]
outside a bounded interval.

This proves:

- \(B_\phi^{\rm sh}<\infty\).
- Integrability of the activation expression defining \(J_\phi\).
- Integrable bounds for \(Q_k\) and its first three step derivatives, uniform over \(|h|\le c/k\) for each fixed \(k\).
- Integrable bounds permitting the fixed-\(N\) cubic derivatives of the observable to be averaged.
- Continuity of each fixed expected terminal-output function.

The differentiation argument has the necessary hypotheses: the finite recursions are sufficiently smooth, and difference quotients are bounded using the fundamental theorem of calculus and the next derivative envelope. The successive expectation interchanges are therefore justified.

Although the candidate names dominated convergence, its use here can also be verified directly by truncating the Gaussian marks to a compact rectangle, using uniform continuity there, and bounding the complementary tails by the displayed integrable envelope. No specialized external theorem is a missing dependency.

The assumed \(C^{12}\) regularity is more than the argument needs; it is sufficient and causes no gap.

**Parity, remainder, and cubic coefficient — (SD29)–(SD36)**

Let \(S(a,u)=(-a,u)\). The Euler recursion satisfies
\[
E_{-h}(Sz)=S(E_hz),
\qquad \psi(Sz)=-\psi(z).
\]
The initial Gaussian law is invariant under \(S\), so \(F_{N,1}\) and \(D_k\) are odd for arbitrary admissible \(\phi\). No parity assumption on \(\phi\) is needed.

Since
\[
D_k(h)=h^2\overline Q_k(h)
\]
and \(\overline Q_k\) is \(C^3\), it is odd, including at zero. Thus
\[
\overline Q_k(0)=\overline Q_k''(0)=0.
\]
The integral Taylor identity in (SD30) gives
\[
\left|\overline Q_k(h)-h\overline Q_k'(0)\right|
\le \frac{|h|^3}{6}\sup_{|v|\le|h|}
|\overline Q_k'''(v)|
\le B_\phi^{\rm sh}k^4|h|^3.
\]
Multiplication by \(h^2\) gives precisely the claimed fifth-order remainder. The argument handles negative \(h\) by orientation reversal and \(h=0\) directly.

For the coefficient, independent differentiation at zero gives
\[
z_N'=Ng,\qquad z_N''=N(N-1)b,
\]
and
\[
z_N'''=N(N-1)(N-2)c_1+
\frac{N(N-1)(2N-1)}2c_2.
\]
Indeed, the third-derivative increment at step \(j\) is
\[
3j(j-1)c_1+3j^2c_2.
\]
This verifies both finite sums in (SD31).

Writing the symmetric Hessian as \(Dg=D^2\psi\) gives
\[
D\psi[c_1]=g^T(Dg)^2g=\|Dg[g]\|^2,
\]
\[
D^2\psi[g,b]=\|b\|^2,\qquad
D\psi[c_2]=D^3\psi[g,g,g].
\]
The observable chain rule then yields
\[
F_{N,1}^{(3)}(0)
=\left(2N^3-\frac32N^2+\frac12N\right)\mathsf S
 +(4N^3-6N^2+2N)\mathsf H,
\]
which equals (SD33).

At initialization,
\[
Dg[g]=
\bigl(a_0p^2,\ \phi(u_0)p+a_0^2pq\bigr),
\]
so Gaussian integration gives
\[
\mathsf H=
E\!\left[\phi'^4+\phi^2\phi'^2
+2\phi\phi'^2\phi''+3\phi'^2\phi''^2\right].
\]
Likewise,
\[
D^3\psi[g,g,g]
=3a_0^2\phi p^2q+a_0^4p^3\phi''',
\]
and hence
\[
\mathsf S=3E[\phi\phi'^2\phi''+\phi'^3\phi'''].
\]
Thus \(\mathsf S+4\mathsf H\) has exactly the five coefficients displayed in \(J_\phi\), including \(11=3+8\).

Finally,
\[
8F_{k,1}^{(3)}(0)-F_{2k,1}^{(3)}(0)
=-3k(2k-1)(\mathsf S+4\mathsf H).
\]
Division by \(6\) proves
\[
\overline Q_k'(0)=-\frac{k(2k-1)}2J_\phi.
\]
The sign and normalization in (SD4) are correct.

**Sharpness and boundary cases — (SD37)–(SD38)**

For \(\phi\equiv\pm1\), normalization holds, \(U_j=u_0\), and
\[
F_{N,1}(h)=Nh.
\]
All terms in \(J_\phi\) vanish, and the discrepancy is exactly zero.

For \(\phi(z)=z\), the activation satisfies (SD2) with \(M=1\). In coordinates
\[
v=(a+u)/\sqrt2,\qquad w=(a-u)/\sqrt2,
\]
one step multiplies \(v,w\) by \(1+h,1-h\). Since \(au=(v^2-w^2)/2\) and both initial variances equal one,
\[
F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2.
\]
This verifies (SD37), \(J_\phi=8\), and cubic discrepancy coefficient \(-4k(2k-1)\).

The fifth-order coefficient is
\[
32\binom{2k}{5}-\binom{4k}{5}
=-\frac43k(k-1)(2k-1)(8k-9).
\]
Its leading term is \(-\frac{64}{3}k^4\).

If an estimate with \(Ck^p|h|^5\), \(p<4\), held for this single activation with \(C\) independent of \(k\), taking \(h\to0\) at each fixed \(k\) would bound that coefficient by \(Ck^p\), a contradiction as \(k\to\infty\). The shrinking radius does not obstruct this argument.

Therefore the exponent \(4\) is sharp over the activation class. This does not assert that every activation attains that growth, or that the displayed constant is optimal.

**Dyadic consequence — (SD39)–(SD40)**

The substitution \(h=s/(2k)\) is admissible whenever \(|s|\le S\le2c_\phi\). The cubic contribution satisfies
\[
\frac{k(2k-1)}2|J_\phi|
\left|\frac{s}{2k}\right|^3
=\frac{(2k-1)|J_\phi||s|^3}{16k^2}
\le\frac{|J_\phi|S^3}{8k},
\]
and the remainder becomes
\[
B_\phi^{\rm sh}k^4
\left|\frac{s}{2k}\right|^5
\le\frac{B_\phi^{\rm sh}S^5}{32k}.
\]
This proves (SD39).

With
\[
A=\frac{|J_\phi|S^3}{8}
+\frac{B_\phi^{\rm sh}S^5}{32},
\]
telescoping gives, for integers \(q>p\ge0\),
\[
\sup_{|s|\le S}|G_{2^q}(s)-G_{2^p}(s)|
\le A\sum_{j=p}^{q-1}2^{-j}
\le 2^{1-p}A.
\]
Pointwise completeness produces the limit, and the same bound proves uniform convergence and exactly (SD40). Continuity passes to the uniform limit.

The candidate correctly restricts this conclusion to the dyadic sequence of expected terminal outputs.

**Claim and adversarial-check ledger**

| Claim or possible obstruction | Finding |
|---|---|
| Exact finite-width expectation identification | Proved by coordinatewise recursion and integrability |
| Wrong coarse/fine order or sign | Ruled out by explicit hybrid telescoping |
| Interpolation improperly treated as Euler | Ruled out; convexity is used separately |
| Omitted derivative of the transported direction | Ruled out by the full differentiated tangent recurrence |
| Missing power of \(k\) in constants | None found; all source sums and normalizations checked |
| Gaussian tail growth invalidating interchange | Ruled out by polynomial-times-linear-exponential envelopes |
| Parity requiring odd activation | Ruled out; symmetry is in the initial readout |
| Cubic coefficient or Gaussian contraction error | None found; independently reproduced |
| Nonuniform constant hidden in sharpness argument | None; the linear activation is one fixed admissible witness |
| Dyadic estimate promoted to arbitrary partitions | No such promotion occurs |
| Section 8 or another library result used as a premise | No such dependency occurs |

**Required corrections**

None.

**Precise limitations**

This verdict establishes the stated theorem and consequence, with their displayed constants and scopes. It does not establish:

- convergence in probability or almost surely of finite-width outputs;
- a joint growing-width/growing-step-count theorem;
- convergence along every integer \(N\), arbitrary partitions, or a partition-independent flow;
- hidden-state convergence, a restartable limiting state, or an ODE identification;
- physical loss-GD convergence, long-time validity, or results for reused inter-hidden-layer matrices;
- the substantive comparison with the unavailable Section 8;
- any unspecified theorem concerning the broader library mentioned in `NOTATION.md`.

The review is a complete manual mathematical audit of the permitted packet, not a machine-checked formal proof. All three input files have identical before-and-after hashes.