# Scoped internal check: nonlinear dense variability and finite-jet remainder

Date: 2026-10-10. Checker: /root/tanh_nth_generic.

This is a bounded same-study internal mathematical check, not an isolated
promotion review and not approval to promote any result into the maintained
book. I read the two assigned files completely, then reread the changed
operator-norm, concentration-reference, and introductory formatting passages.
No experiment, other-study input, archived source, or Git operation was used.

## Frozen checked inputs

- SINE_DENSE_VARIABILITY.md, SHA256
  55a644abbbf9ef1151e8edc01cad62f664462a6710b5e90f9a290d2546a28db0.
- SINE_REMAINDER.md, SHA256
  87698c5dcf3f5db71416cea2f84fe2e93be9cbe73eb16da4a3e0b3ce912877ab.

The initial remainder check used hash
b610b959134191083e43f60b6560f8ba38a0f9bc32188ad6033927f8c113e99e.
After Sections 5--6 were added, I read the entire updated file through
the final displayed conclusion, then read the newly appended Section 7
when it was added. The intermediate Sections 1--6 version had hash
b15e09f083054751ce28bdb0a6a8ec505e3f02dcded245cd3ad4f8dbbff47a69.
The updated hash above is the version covered by this report.

The first file concerns the canonical two-hidden-layer model with
$m=d=2$, orthogonal unit inputs, first activation
$\phi_\varepsilon(z)=z+\varepsilon\sin z$ for fixed
$\varepsilon\in[1/8,1/4]$, identity second activation, Gaussian initialization,
zero readout, mobilities $(n,1,n)$, and fixed labels $(\eta,0)$ with
$0<\eta\le10^{-62}$.

The second file uses the same model, allows $0<\eta\le1$, and proves a
deterministic implication from its explicitly stated initialized-jet event.

The separate Gaussian initialized-jet report was not read in this check.
Its claimed probability and combinatorial proof are not covered by this
verdict. The combined NONLINEAR_RESULT.md was not an input and is not
covered by this verdict.

## Verdict

No blocking mathematical issue was found in either checked version.

The dense report proves its deliberately nonsharp independent-run bound

\[
\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
|f_n(t,v)-\widetilde f_n(t,v)|
=O_{\mathbb P}(n^{-1/64000})
\]

on the unit circle in the stated two-dimensional input space. It does not
claim the sharp root-width rate, arbitrary-dimensional query spheres,
general correlated training inputs, or two tanh activations.

The remainder report correctly proves a width-independent real-time
Taylor remainder conditional on its finite initialized-jet bounds. It does
not require or conclude a common complex-time analytic disk for the actual
dense trajectory. The polynomial state used in its proof is not a new
closure and does not change the original frozen-top NTH.

## Dense-variability calculation

Write $Y=\eta/\sqrt2$. I checked the following constants and implications.

1. The transformed equations are the original metric gradient flow in
   physical time. The real transformed activation derivative lies in
   $[9/16,25/16]$, so its Euclidean Lipschitz constant is dimension
   independent.
2. The initialized feature Gram event follows from fixed-dimensional
   empirical Gaussian-square concentration, with population covariance at
   least $(9/16)I_2$. Errors $1/16$ and $1/8$ leave more than the stated
   $1/4$ final-feature gap. Conditional concentration of the second Gram
   is legitimate because its rows are independent Gaussian vectors once
   the first feature vectors are fixed.
3. On the bootstrap gap $1/8$, the loss normalization gives residual
   decay $e^{-t/16}$ and integrated residual at most $16Y$. The four
   parameter/feature increments
   $240Y$, $19200Y^2$, $11520Y^2$, and $38400Y^2$ follow directly by
   integration.
4. Expanding $Wa_a-W_0a_a(0)$ gives the sharper bound
   $215040Y^2$, so the stated $230000Y^2$ is safe. With initial feature
   norms at most eight, the final Gram change is bounded by
   $32(230000Y^2)+2(230000Y^2)^2<8\cdot10^6Y^2$.
   This closes the bootstrap strictly in the stated label range.
5. For a passive unit query, $\|B\|_{\rm op}<25/4$ and its first feature
   norm is below eight. The tail expansion has leading readout term
   $9600Y e^{-t/16}$ and remaining terms bounded by
   $58118400Y^3e^{-t/16}$. Thus the stated
   $20000Y e^{-t/16}$ tail is safe.
6. The state difference norm uses Frobenius norm only for a difference
   of dense matrices, not for the initial dense matrix itself. The
   prediction and residual difference bounds $15D$ are valid. Expanding
   the three state blocks gives bounds no larger than
   $81D$, $50D$, and $238D$, whose sum is less than $400D$.
7. The initial map from normalized Gaussian coordinates into this
   difference norm has Lipschitz constant at most
   $\sqrt{(4/3)^2+1}=5/3<2$. The passive prediction has Lipschitz
   constant at most forty in state, giving $80e^{400t}$ with respect
   to initialized Gaussian coordinates. The stated time and angle
   Lipschitz bound $20000$ is very conservative but valid.
8. The same-constant Lipschitz extension is legitimate on the entire
   Gaussian coordinate space. Its values on the initialization event
   agree with the actual prediction; its Gaussian mean cancels between
   two independent copies.
9. At $T=(\log n)/4000$, the concentration Lipschitz constant is
   $80n^{1/10}$. Taking threshold $n^{-1/4}$ gives exponent
   $n^{3/10}/12800$, which dominates the
   $O((1+\log n)n^{1/2})$ time-angle grid size. Interpolation gives the
   short-horizon $O(n^{-1/4})$ bound.
10. Comparing each later-time prediction to its value at $T$ through its
    fitted endpoint costs at most $80000Y e^{-T/16}$ for the pair.
    Since $e^{-T/16}=n^{-1/64000}$, the all-time conclusion follows,
    including the limiting endpoint.

The initial draft's two-sided $1/4$-net explanation did not itself prove
operator norm at most four: its straightforward union-bound exponent is
insufficient. This nonessential explanation has been removed. The checked
version instead applies the stated Gaussian operator-norm tail directly.
The supervisor separately verified the exact external references:
Vershynin's Proposition 5.34 and Corollary 5.35 in arXiv:1011.3027.
I checked the rescaling and hypotheses in this application, not a fresh
complete reading of that external source.

Malformed inline math openings in the initial draft were also corrected;
the affected introductory and cited passages were reread.

## Finite-jet remainder calculation

The deterministic lemma assumes normalized Euclidean/Frobenius state
coefficients through order $R$ are bounded by $M$, and also assumes the
unnormalized transformed first-coordinate coefficients are bounded by
$M$ in maximum norm. This second bound is essential, is explicitly
stated, and is not inferred from an Euclidean bound.

I checked each step of the proof.

1. For every real transformed scalar center, the inverse-coordinate ODE
   $z'=1+\varepsilon\cos z$ is a contraction on the complex-time disk
   of radius $1/16$, with state radius $1/4$. On that state disk its
   vector field is below two and its derivative below $1/3$. The
   claimed contraction factor $1/48$ and scalar increment bound
   $|H(\tau+s)-H(\tau)|\le4|s|$ are valid uniformly in the center and
   in the stated activation interval.
2. For the finite state polynomial $P_R$ and
   $\rho=(D_*M)^{-1}$, $D_*\ge256$, both normalized state increments
   and raw transformed coordinate increments are at most $2/D_*$.
   This puts every scalar composition inside its uniform complex
   disk. Applying the increment estimate coordinatewise preserves the
   Euclidean norm and introduces no factor $\sqrt n$.
3. The composed vector field $\mathcal F_n(P_R)$ is consequently
   bounded and holomorphic in the relevant product norm, uniformly
   in $n,R,M$. The matrix component is an outer product, hence is
   bounded in Frobenius norm even though the fixed $W_0$ need only
   be bounded in operator norm.
4. Finite chain-rule matching makes $P_R'$ and
   $\mathcal F_n(P_R)$ agree through degree $R-1$. Cauchy's
   coefficient estimate and a geometric tail therefore yield the
   defect $2C_0\rho^{-R}t^R$ for $0\le t\le\rho/2$.
   This does not assume convergence of the true infinite Taylor
   series.
5. The actual real flow exists in a fixed norm ball for a
   width-independent interval by the stopped-velocity argument.
   Increasing $D_*$ if necessary puts the comparison interval inside
   it. Real Lipschitz stability then gives
   $2C_0e^{Lt}\rho^{-R}t^{R+1}/(R+1)$ for the state difference.
6. The prediction on $P_R$ is separately holomorphic and bounded.
   Its coefficients through degree $R$ are the true initialized
   prediction coefficients. Its own Cauchy tail, combined with the
   real state estimate, gives
   $C(D_*M)^{R+1}t^{R+1}$ with constants independent of $n,R,M$.
7. The final comparison with the original hierarchy is explicitly
   conditional on the correct own-residual unmatched-jet identity and
   on the hierarchy remainder. Taking the minimum time in the report
   gives $|f_1-\widehat f_1^{(q)}|\ge L_j\tau^j/2$ by an ordinary
   triangle inequality; no source-clock identification is used.

### Added Sections 5--6: interface with the separately checked jet event

The later sections correctly convert the stated order-specific
initialized-jet event into dense and original-NTH remainder bounds. This
part of my check uses the initialized-jet event as a separate input; it
does not certify the underlying forest proof, which the supervisor and
the remainder author report checking independently.

The additional initial norm event permits $L_0=8$: the two transformed
initial vectors have combined norm at most $16/3$, and the two-sided
$1/4$-net at bilinear threshold four now gives an operator threshold
eight, with exponent $(2\log9-8)n<0$. Unlike the removed
operator-threshold-four argument in the initial dense report, this
net calculation has a valid exponent.

The hierarchy's quadratic max-entry majorant is independent of its
number of stored entries. Its Cauchy remainder
$4H_q(4H_q)^{R+1}t^{R+1}$ on $t\le1/(8H_q)$ is valid.

Writing
$b_{n,j}=1+\log(j+1)+\log\log(e^e n)$, the stated state-jet envelope
$\exp[C(j+1)b_{n,j}]$ gives dense and hierarchy Taylor remainders
bounded by $\exp[C(j+1)^2b_{n,j}]t^{j+1}$. The stated shorter time
scale lies in both existence intervals. A sufficiently large constant
in $\tau=\exp[-C'_\eta(j+1)^2b_{n,j}]$ makes the total remainder at
most half the unmatched leading term. The resulting exponent
$C''_\eta(j+1)^3b_{n,j}$ is therefore correct.

The interface with the parameter transfer has the needed quantifiers:

- At $n_k=\lceil e^k\rceil$, all $q\le k$ satisfy
  $j=2\lfloor q/2\rfloor+1\le k+1\le\lfloor\log(en_k)\rfloor$.
  Thus the remainder's simultaneous order range covers the entire
  simultaneous parameter-transfer event.
- The transferred coefficient bound
  $(\eta/16)^j(8e k^4)^{-(j+1)}$ implies the remainder report's
  proposed lower bound
  $\exp[-C_\eta(j+1)(1+\log\log(e^e n_k))]$.
- For almost every single deterministic fixed activation parameter,
  the Remez event has eventual probability at least $1-1/k$.
  Intersecting it with the initialized-jet event of probability
  $1-n_k^{-A}$ is valid. No event simultaneous over a continuum of
  activation parameters is needed.
- The Remez conclusion here is along the geometric width sequence;
  it must not be silently restated as an all-width probability
  assertion. The remainder report explicitly leaves this final
  quantifier assembly to the combined theorem.

### Added Section 7: geometric-envelope sharpening

The geometric version of the deterministic lemma is correct. If the
normalized and raw transformed state coefficient at order $s$ is bounded
by $B^s$, the polynomial state increment on
$|t|\le(D_*B)^{-1}$ is at most
$B|t|/(1-B|t|)\le1/(D_*-1)$. The same scalar complex disks, bounded
composed vector field, finite jet matching, and real stability proof
therefore apply. The resulting dense remainder is
$C(D_*B)^{R+1}t^{R+1}$, rather than one obtained by replacing every
coefficient by the final-order bound.

The stated order-specific initialized event can be put in this geometric
form: for $1\le s\le R$, use $s+1\le2s$ and $s+1\le R+1$ and enlarge
the fixed base/exponent constants. This is a conversion of the separately
supplied event, not a fresh probability argument.

The weighted hierarchy proof preserves the actual closure. With
$X_s=\widehat K_s/B^s$ its equation is exactly

\[
\dot X_s=\frac B2\sum_{b=1}^2X_{s+1}(\cdots,b)
                  (y_b-BX_{1,b}),\qquad \dot X_q=0.
\]

The coefficient recursion is dominated by
$Z'=2B^2Z^2$, $Z(0)=1$. The linear term is bounded by the corresponding
positive quadratic convolution because the majorant's constant
coefficient is one and $B\ge1$. Thus the weighted series converges
and is bounded by two on $|t|\le1/(4B^2)$; the actual prediction
is bounded by $2B$. Its displayed Cauchy remainder
$4B(4B^2)^{R+1}t^{R+1}$ is correct. It remains valid when the Taylor
degree exceeds the hierarchy rank.

These two remainders have a common polynomial base: with $B_0$ denoting
the initialized geometric base, take
$B_{\rm c}=2\max\{C_{\rm d}D_*,16\}B_0^3$.
The summed dense and hierarchy remainder is at most
$(B_{\rm c}t)^{R+1}$ for $t\le B_{\rm c}^{-1}$.
This verifies the interface to the higher-degree real-polynomial
coefficient argument. For its choice $R=2j$ and
$q\le\lfloor k/4\rfloor$, one has
$R\le3q\le3k/4<\lfloor\log(en_k)\rfloor$, so the required initialized
order range is covered.

The earlier quadratic-order remainder bounds are still valid but are
weaker than this new section. This audit found no new gap in the
sharpening. The coefficient-transfer proof itself was authored separately
in NONLINEAR_WITNESS.md and sent to another agent for an independent
same-study check; this paragraph does not present self-review as an
independent check of that proof.

## Consequence and limitations of this check

An independently established short-time NTH lower bound $n^{-o(1)}$,
on even one training input, is asymptotically larger than the checked
dense-pair benchmark $O_{\mathbb P}(n^{-1/64000})$. The two high-probability
events can be intersected without any independence assumption between
the lower-bound event and the dense-pair event.

This check does not establish the Gaussian initialized-jet lemma, the
fixed-parameter Remez lower bound, or their uniform order range. Those
remain separate scientific inputs to the complete combined theorem.
Nor does this internal check establish a two-tanh result, a general-data
two-sided accuracy theorem, or a polynomial-in-width storage lower bound.
