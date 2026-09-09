# Adversarial re-audit of the two-step ladder ledger

## Verdict

`TWO_STEP_LADDER_LEDGER.md` does **not** yet prove a counterexample for the
actual `q=1,L=2` width-first network, nor even a complete theorem for the
infinite-block two-step OMFP DAG.  It identifies a sharper candidate and the
exact finite response ledger, but three bridges remain unproved.  Any theorem
language in Sections 1, 9, or 10 of that draft is superseded by this audit.

Accordingly, Section 4 of
`../temporary_linear_growth_uniform_counterexample/FINAL_AUDITED_STATUS.md`
is accurate: the finite-output `L=2` question remains open.

## 1. What is rigorous

The following parts survive the audit.

1. The exact finite-width identity

   \[
   z_i^+=n^{-1/2}W_iH^++h a_i\phi'(z_i)n^{-1}H\cdot H^+
   \]

   is correct and isolates the reused term.
2. The exact two-step OMFP node list (5.1)--(5.13) is complete: it includes
   `K_01`, `K_11`, `sigma_10`, `sigma_11`, `rho_20`, and `rho_21`.
3. The scale choice

   \[
   t=e^R,\quad h=t^{-1},\quad S=t,
   \quad L_0=t^2,\quad L_1=e^S,
   \quad T=L_1/t
   \]

   has the advertised transported-tail separation:

   \[
   L_0^qe^{-R^2/2}\to0,qquad
   L_1^qe^{-cS^2}\to0,qquad
   e^{-R^2/2}T\to\infty.
   \]
4. A locally finite smooth activation can contain the proposed asymmetric
   oscillatory shells while remaining positive and linearly bounded, and all
   of its *initialization-Gaussian* derivative moments can be finite.
5. The ordinary fresh lower-field power count is favorable.  Even including a
   reset fraction `delta`, its scale relative to the direct second amplifier is
   bounded by a quantity of the form

   \[
   t^C p^a\delta^{-C}\to0
   \quad(p=e^{-R^2/2},\ a>0).
   \]

These facts make the two-step ladder a serious candidate.  They do not close
the reused-adjoint or signed-output proof.

## 2. First unproved bridge: adaptive lower response

The claims

\[
 Q_{02}=Q_{12}=Q_{22}=1+o(1),qquad
 \rho_{20}=o(h),\quad\rho_{21}=o(h)
\]

in (8.4)--(8.5) were justified only by a scale ledger.  A proof needs the
conditional density of `b_1` given the active lower source history, including
its nonzero response shift and its correlation with `u_1`.  In particular,
the term

\[
 h^2\mathbb E[
 \phi'(u_2)\phi'(u_0)\phi''(u_1)b_1]
\]

was bounded by quoting a reciprocal landing-density factor, but no density
lemma with constants was proved.  Nor was every reset and cutoff contribution
enumerated.  The informal estimate (8.6) is therefore not a proof of
`rho_20=o(h)`.

There is also a minor bookkeeping defect: the powers of `delta` in (7.5)--(7.6)
depend on whether one uses a supremum or a period-average bound for the reset.
The Gaussian factor would beat any fixed corrected power, but the inequality
as written was not derived with one consistent norm.

## 3. Second unproved bridge: the signed terminal expectation

The favorable event does give a positive candidate contribution of scale
`pT`.  The statement that the whole negative part is `o(pT)` is not proved.
The five-case list in Section 9 omits a quantitative conditional estimate for
rows which:

- start in a reset transition with small `|A|`;
- acquire a large reused Gaussian/response shift;
- or reach the terminal plateau through a cutoff ramp rather than a core
  phase.

Because the terminal value itself is `T`, even a probability of order `p`
with an uncontrolled sign can cancel the favorable contribution.  Geometry of
the scalar center map is insufficient; the fresh and response fields have
unbounded support.  A sign-safe integral estimate for every such route is
still required.

## 4. Third unproved bridge: infinite-block width-first identification

Section 10 asserted that every node of a finite-block two-step network is a
globally Lipschitz function of the initialization and therefore has a
sub-Gaussian tail.  This is not established and is generally false in that
form: reused matrix products can produce finite Gaussian chaoses with
sub-Weibull, rather than sub-Gaussian, tails.  Consequently a future block
whose slope is `exp(S)` is not automatically negligible under every earlier
adaptive query.

A valid diagonal construction would have to do one of the following.

1. Prove an explicit tail exponent for every truncated node and choose the
   future slope growth strictly below that exponent while retaining the
   transported gain; or
2. place future oscillatory supports in sets of small measure for every one of
   the finitely many earlier adaptive laws and prove that the large derivative
   weights remain uniformly integrable.

Neither was done.  Initialization Gaussian moment finiteness, (4.4), is not a
replacement for this adaptive uniform-integrability theorem.

## 5. Final status

The finite two-step route improves the research state in two ways:

- it shows that an all-time Markov corridor is not logically necessary; a
  two-scale moving-tail ladder could already destroy continuity of
  `F_2(h)-F_1(2h)` at `h=0`;
- it reduces the full-network task to a finite response-density lemma, a
  signed bad-route estimate, and an infinite-block truncation theorem.

But those are still mathematical proof obligations.  The correct status is

\[
 \boxed{\text{promising two-step counterexample candidate, not proved}.}
\]

