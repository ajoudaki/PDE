# Isolated adversarial review: RESTART_RESPONSE_WINDOW.md

Verdict: **PASS for the stated local restart lemma**, with the auxiliary
continuation qualifications and editorial corrections specified below.

Audited file: `/tmp/l3-two-sample-Un7kw9/RESTART_RESPONSE_WINDOW.md`.

Length: 753 lines. SHA-256, verified before reading and again before writing
this review:

```text
ee160401e65aab1b8e11848f1c25fd9fbefd15830380369eaba251d7a649e1a3
```

## Scope and dependencies

The audited assertion is the estimate at lines 107–145 for actual canonical,
capped, finite source programs. Its hypotheses include the three random
history-envelope bounds (6) and a primal bound on both the retained prefix
and the proposed continuation. This is not an unconditional continuation,
population-limit existence, or global two-sample theorem. In particular, the
actual signed energy term (40) remains unclosed.

Read `solve-math-rigorously` in full at
`/etc/codex/skills/solve-math-rigorously/SKILL.md`. Mathematical dependencies
consulted were only:

- `CONTRACT.md`, in full.
- `NONLINEAR_RESPONSE_PERTURBATION.md`, the source definitions surrounding
  (6)–(10), and Sections 3–4 for coefficient-prefix moments, derivative
  equations (24), (26), (28), and their envelopes.
- `TWO_SAMPLE_SOURCE_BASELINE.md`, Section 3, to verify the formal source
  covariances, frozen-derivative convention, and causal query order.

The additional reading list inside the candidate was not followed. No
reviews, history, other routes, agents, experiments, or external theorem
sources were used. No existing file was edited. The finite canonical source
representation is taken in the precise sense supplied by the permitted
definitions; its external Gaussian-program identification theorem is not
being independently certified here.

## 1. The retained history supplies the necessary old forcing

The strengthened random history hypothesis has substantive content. It is
not interchangeable with an absolute bound on expected response coefficients.
From (3)–(6), the deterministic old-row bounds (14) follow as written:

\[
 |\mathbb E(GJ)|\le 2\mathbb E|J|,
 \qquad
 \mathbb E[Q^i_k\mathcal H_i(u)]
 \le \|Q^i_k\|_2\|\mathcal H_i(u)\|_2\le Q_*H_*.
\]

The top backward row is bounded by
\(eQ_*H_*+2H_*\), before its learned term. The middle backward row is
bounded by \(eQ_*H_*+4M^0_3H_*\). These arguments require no independence
between a field and its derivative. The learned terms have exactly the
column weights \(h_jc_b\); their block bounds are \(Q_*^2h_j\) forward and
\(SQ_*^2\) for a backward time row.

The future old-column forcing uses the new row of coefficients. In
particular,

\[
 \frac1{h_j}\left|\sum_{r<m}a^2_{kr}D^{2,\zeta}_{r,j}\right|
 \le \frac{A_2}{h_j}\sum_{r<m}h_r|D^{2,\zeta}_{r,j}|
 \le A_2\mathcal H_2(u).
\]

The diagonal \(D^{2,\zeta}_{j,j}=V^2_j\) is correctly present: its bound
is 2, and its single time weight cancels the denominator. It is not treated
as an \(O(h_j)\) derivative. For forward-source rows, zero-padding the old
derivative rows gives

\[
 \sum_{j\le k}|J^{i,\mathrm{old}}_{k,j}|
 \le 1+A_i\sum_{r<m}h_r\sum_{j\le r}|D^{i,\xi}_{r,j}|
 \le 1+A_i\mathcal H_i(u),\qquad i=2,3.
\]

Thus (4) and (5) retain precisely the integrated old backward derivatives
needed here. No old coefficient is frozen to its value in row \(m\), and
no old source is discarded. The full covariance definition in baseline (5)
agrees with candidate (10); adjoining source slots preserves the old
marginal law, including the law of each old envelope.

## 2. The four-stage induction is causal

There is no circular assumption of the future coefficient conclusion (8).
The dependencies needed to estimate a row are as follows.

| Row being estimated | Coefficient rows already available | Current unbounded multiplier needed in its remainder estimate |
| --- | --- | --- |
| \(a^2_k\) | \(b^2_r\), \(r<k\) | None; \(G^1_k\) is bounded by 2 |
| \(a^3_k\) | Current \(a^2_k\), and \(b^3_r\), \(r<k\) | None; \(G^2_k\) is bounded by 2 |
| \(b^3_k\) | Current \(a^3_k\), earlier top forward rows | \(C_k\), already determined from earlier top fields |
| \(b^2_k\) | Current \(a^2_k,b^3_k\), earlier middle rows | \(q^2_k\), available after constructing \(b^3_k\) |

For the first two rows one uses (22) with the unnecessary current multiplier
omitted, as explicitly permitted at lines 364–366. One must not use a bound
on \(q^1_k\) to construct \(a^2_k\), or on \(q^2_k\) to construct
\(a^3_k\). Neither is needed. The future integrals and exponentials in
those stages involve only \(Q^i_r\) with \(r<k\).

The moment argument also respects this table: moment estimates are applied
only to the coordinate instructions already available at a stage. A
simultaneous assertion of moments for every current field would be
premature, but is not necessary for the proof. The permitted dependency
explicitly gives this incomplete-prefix version at lines 322–326.

The varying old-forcing rows cause no problem for finite iteration. Their
absolute values have one common random bound \(4\kappa\mathcal H_i(u)\),
even though the rows themselves vary with \(k\). Taking an increasing
majorant therefore bounds the derivative maxima and their remainders.
The feedback coefficients are dominated by
\(\kappa(1+eQ^i_r)\); substituting the resulting exponential bound into
the remainder gives (24).

The exact current returns are also retained. At the top,
\(\partial_{\xi^3_k}Z^3_k=I\) and
\(\partial_{\xi^3_k}C_k=0\), so the diagonal output is \(L^3_k\).
In the middle the same identity derivative contributes both \(L^2_k\)
and \(V^2_kb^3_{kk}G^2_k\). Their expectations are exactly (11), because
\(b^3_{kk}\) is diagonal. These terms are bounded in the leading forcing
terms of (34)–(35), not assigned an erroneous factor \(d\).

Consequently (32)–(35) have the claimed half-unit margin when
\(d\le(2K)^{-1}\). Induction through these stages and then through the
mesh nodes closes the actual rows. No continuity argument in a growing
coefficient dimension is needed.

## 3. The unbounded products use only one old envelope

The primal estimates are sufficient for the stated \(Q_*\). For example,
\(|\phi_e(z)|\le |z|+1+\pi/2\) and
\(|\mathcal D_{e,R}(z,q)|\le2|q|\). With the assumed matrix actions,
these give the listed forward and backward bounds. The source variances
are second moments of these fields, so they too are controlled. Under
deterministic coefficient bounds the causal moment iteration gives
\(\|Q^i_r\|_p\le L_*\sqrt p\), without a random maximum over source
times. The very loose constant (19) covers its forcing and feedback terms.

Put \(W_k=\sum_{m\le r<k}h_r(1+Q^i_r)\). Minkowski gives
\(\|W_k\|_6\le d(1+\sqrt6L_*)\). The square-exponential expansion and
weighted convexity argument in (21) are valid with arbitrary time
correlations. For an old envelope \(F\), Hölder gives exactly

\[
 \mathbb E[F E^i_k(1+Q^i_k)W_k]
 \le \|F\|_2\|E^i_k\|_6\|1+Q^i_k\|_6\|W_k\|_6,
 \qquad \frac12+\frac16+\frac16+\frac16=1.
\]

Every remainder used in closing a coefficient row contains only one factor
\(F\). The leading current products \(Q_k(1+A_iF)\) instead use
Cauchy–Schwarz and the primal \(L^2\) bound. Thus no hidden higher old
moment is needed in the local closure. The constant (31) dominates these
estimates: the largest displayed output factor is covered by
\(100\kappa^3\), and \((1+\sqrt6L_*)^2\le6(1+L_*)^2\).

## 4. The new history bound does not misuse the old \(L^2\) bound

One could not infer an \(L^2\) bound on \(F E_k\) from \(F\in L^2\)
alone. The candidate does not make that inference. After the coefficient
induction closes, it returns to the full-origin formal derivative equations.
This is essential and valid for the actual canonical programs in scope.

Here is an explicit check of the resulting history majorant. On a bounded
coefficient prefix ending at time \(t\le S\), write

\[
 W_i(t)=\sum_{r<n}h_rQ^i_r,
 \qquad
 \mathcal E_i(t)=\exp\{\kappa t+\kappa eW_i(t)\},
 \qquad t=s_n.
\]

The full-origin bottom transpose bound is \(2h_j\mathcal E_1(t)\).
The middle transpose bound is \(2Ah_j\mathcal E_2(t)\), and its
forward-source row is bounded by \(\mathcal E_2(t)\). At the top, the
sum of the forward-source and readout row norms has forcing 1 and feedback
at most \(2A+2+eAQ^3_r\), hence is bounded by \(\mathcal E_3(t)\).

For the middle accumulated transpose term, the diagonal contributes at
most 2 and the strictly later terms give

\[
 \max_{j<n}\frac1{h_j}\sum_{r<n}h_r|D^{2,\zeta}_{r,j}|
 \le 2+2A\mathcal E_2(t)\bigl(eW_2(t)+4MS\bigr).
\]

The accumulated middle forward-source row is at most
\(\mathcal E_2(t)(eW_2(t)+4MS)\); the corresponding top bound is
\(\mathcal E_3(t)(eW_3(t)+2S)\). These bounds imply, with ample room in
the stated \(\kappa\),

\[
 \mathcal H_i(t)
 \le 10\kappa^2(1+S+W_i(t))\mathcal E_i(t).
\]

Since \(\|W_i(t)\|_4\le2SL_*\), the same exponential calculation as
(21), with total duration at most \(S\), gives finite moments of this
majorant of every fixed order. In particular, its \(L^2\) bound is
dominated by (36). Higher moments are therefore derived from the canonical
equations and the now-proved deterministic coefficient bounds. They are
not additional hypotheses about arbitrary old random variables.

All arguments use actual positive step weights. The transpose denominator
is cancelled by the same source slot's step; no ratio of neighboring steps
is introduced. Derivative maxima are bounded pathwise by an increasing
integral exponential, while source moments use maxima of deterministic
norms. There is no random Gaussian maximum or source-count factor. The
terminal zero-step convention is never used as a denominator.

## 5. Nonaccumulation and the unclosed energy term

With common primal and history bounds on the continuations under
consideration, the displayed constants give a common positive admissible
window length. With maximum mesh step below half that length, the stated
covering count follows by taking windows of length between half and all
of the admissible length, except for the last remainder. This is a
conditional statement about this estimate.

In contrast, the recursive certificate (37) gives no lower bound forcing
\(\sum_i d_i=\infty\). Even though all higher response moments exist on
each bounded-coefficient prefix, their bounds depend on the coefficient
bounds and thus on the history certificate. This does not propagate that
certificate without finite-time blow-up.

The energy identity (39) is exact after the direct forcing time. The
contribution involving \(L^1_k\) is exactly (40), whose absolute majorant
is (41). Cauchy–Schwarz requires a fourth response moment as in (42);
the Euler square term requires the additional weighted second moment
shown at line 699. Their finiteness is distinct from a uniform estimate
that would close continuation.

The Gaussian example (43) is correct: exponential tilting gives
\(\mathbb EV_n^2=1\) and \(\mathbb E[GV_n^2]=2n\). It disproves a
general weighted-energy bound based only on multiplier tails and response
\(L^2\) size. It is not a constructed canonical network response, and
the candidate correctly does not present it as one. No favorable sign or
canonical cancellation has been established.

## 6. Corrections and qualifications

The following qualifications are needed to use the auxiliary continuation
paragraph literally. They do not change the passed local lemma, which
already assumes the primal bound on its entire retained and future prefix.

1. **Retained primal bound in lines 590–598.** A bound \(B_0\) at the
   reached state alone does not bound earlier retained primal sizes by
   \(2B_0\). If \(B_{\rm past}\) bounds that retained prefix, apply the
   lemma with \(B=\max\{B_{\rm past},2B_0\}\), or explicitly choose
   \(B_0\ge B_{\rm past}\). The direct first-exit estimate on the new
   interval is otherwise valid.

2. **Exact length in the prefix-only reading of lines 606–618.** The
   length \(d_*(\bar B,\bar H,S)\) applies when the candidate continuation
   also has primal bound \(\bar B\). If only the prefixes before a putative
   terminal time are known to have that bound, invoking the local primal
   argument instead gives the common sufficient length

   \[
    \delta=\min\left\{d_*(2\bar B,\bar H,S),
                 \frac{\bar B}{100(2\bar B)^3}\right\}>0.
   \]

   Use this length for that interpretation of nonaccumulation. The same
   covering argument applies with \(\delta\) on a horizon where its
   uniform hypotheses are supplied. Refinement must also stay within the
   mesh family for which those uniform hypotheses hold; a refined mesh is
   not the same already-controlled trajectory.

There are also two mathematical wording fixes and two rendering fixes:

- At lines 668–670 replace “the nonlinear part” by “the contribution of
  \(L^1_k\).” The memory term also depends on the nonlinear activation
  through \(V,G\) and the coefficients; (40) isolates the specified
  multiplier contribution, not every dependence on \(e\).
- At lines 736–737 refer to the capped multiplier
  \(g'(Z)\tau_R(q)\), or explicitly qualify \(g'(Z)q\) as its uncut
  version. The permitted clip assumptions do not impose monotonicity.
- In (12), change the two literal `quad` strings to `\quad`.
- At line 558, remove the stray backslash before the closing math delimiter.

No change is needed to the local history hypothesis, the four-stage
coefficient closure, the cap-independent moment argument, or the endpoint
history bound. The pass includes singular source covariances and
\(\rho=-1\): formal derivatives retain their named slots, and the proof
uses \(|P|\le1\) and \(\|P\|_{\rm op}\le1\), with no inverse Gram
matrix or cross-population pairing.
