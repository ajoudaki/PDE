# Independent reconstruction of the two-input complex source theorem

2026-10-03. Scoped independent mathematical audit, performed after freezing
the separate label-series route. Only the neutral audit assignment, the
complete candidate and newly authorized supporting source below, and the
already assigned one-input inverse-strip proof were used. No other check
report, experiment, other study, or trained trajectory was read or produced.
The candidate and supporting source were not modified.

The complete frozen inputs checked were:

- TWO_INPUT_COMPLEX_SOURCE.md, 527 lines, SHA-256
  96ce9f5f1966b66082977664efcaa191d137ca646802f9d0984239bb7c4bacf9.
- TWO_INPUT_STABLE_GEOMETRY.md, 415 lines, SHA-256
  93040bef724cfef765aa26d961c996297e13d67b31dcbc3fc51876ac1212c820.
- COMPLEX_ACTIVITY_ROUTE.md, SHA-256
  3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4.
  Its complete proof had already been read; this audit uses its explicit
  inverse-coordinate construction, not its one-input probability theorem.

Canonical notation and its neural-network reference, rigorous-proof
instructions, and the conjecture adversarial-audit instructions were applied.

**Verdict: PASS for the stated two-input source theorem and for the
initialization-only small-source-space consequence at the requested
\(n^{-1/2}\) accuracy.** I found no substantive gap in the real autonomous
cavity comparison, the short vertical complex comparison, the conditioning
of the stopped Gaussian sources, or the query top-gate argument. The
Chebyshev construction also has the asserted retained dimension and coefficient
provenance. Two minor presentation defects are identified in Section 8.
This verdict is an internal scoped reconstruction, not an independent
promotion review of a complete final compression theorem.

## 1. Normalizations and the deterministic comparison

The model has \(A_0\) entries of variance one, \(W_0\) entries of variance
\(1/n\), and \(w_0=0\), independently. For training inputs
\(\sqrt2e_1,\sqrt2e_2\), let \(a_a=Ae_a\),
\(h_a=\tanh a_a\), \(z_a=Wh_a\), \(g_a=\tanh z_a\),
\(\delta_a=w\odot\operatorname{sech}^2z_a\), \(k_a=W^\top\delta_a\),
and \(c_a=y_a-w^\top g_a/n\). The mean unhalved square loss is
\(\tfrac12\sum_a(f_a-y_a)^2\). The factors in candidate equation (1)
therefore agree with mobilities \((n,1,n)\).

The coordinate \(u_a=\Psi(a_a)\), where
\(\Psi(a)=a/2+\sinh(2a)/4\), satisfies
\(\dot u_a=c_ak_a\). The one-input inverse proof applies here independently
to both first-layer columns: \(\Psi^{-1}\) is holomorphic for
\(|\operatorname{Im}u|<1/4\), its derivative is
\(\operatorname{sech}^2(\Psi^{-1}u)\), and
\(\sigma'=(\operatorname{sech}^2\circ\Psi^{-1})^2\) for
\(\sigma=\tanh\circ\Psi^{-1}\). This verifies both the transformed
equations and the lower term in candidate equation (12).

I reconstructed the general lemma in stable-geometry Section 1. For the two
curves there, write \(q=x-\bar x\) and
\(p(t)=\int_0^t(c-\bar c)\,ds\). Their difference satisfies

\[
 q=V(x)p-\int_0^t DV(x)\dot x\,p\,ds
        +\int_0^t[V(x)-V(\bar x)]\bar c\,ds-\int_0^te\,ds.
\]

If \(D=\sup_{s\le t}\|q(s)\|\) and \(P=\sup_{s\le t}|p(s)|\), the
hypotheses give

\[
 \sup_{s\le t}\|q(s)-V_0p(s)\|
 \le C S(P+D)+\epsilon.
\]

The observation difference, including the sign of its added discrepancy,
is

\[
 \dot p=-L_0q-[N(x)-N(\bar x)]-d
       =-K_0p+\zeta,\qquad
 |\zeta|\le CS(P+D)+C\epsilon.
\]

Since \(K_0\) is symmetric with gap \(\gamma>0\), convolution with
\(e^{-K_0t}\) has \(L^\infty\)-operator norm at most \(1/\gamma\).
Absorbing \(CS D\) and then \(CS P\) proves the claimed bound, uniformly
in the terminal time. This argument controls the signed primitive \(p\);
it does not assert an unsupported \(L^1\) estimate for \(c-\bar c\).

For positive neuron masses, the state norm and weighted adjoint in
stable-geometry Section 2 have the correct scalings. In particular

\[
 \|\delta h^\top D_1\|_{\rm HS}
       =\|\delta\|_{D_2}\|h\|_{D_1}.
\]

On the small-activity tube, \(\|w\|_\infty=O(S)\),
\(\|B-B_0\|_{\rm HS}=O(S^2)\), and
\(\sum_a\|u_a-u_{a,0}\|_{D_1}=O(S^2)\). Consequently
\(\|V_a-V_{a,0}\|=O(S)\) and \(\|DV_a\|=O(1)\).
For the potentially delicate lower block, differentiating
\(B^*\delta_a\) gives \((dB)^*\delta_a+B^*d\delta_a\), with

\[
 d\delta_a=\operatorname{sech}^2z_a\odot dw
          +w\odot\tanh''z_a\odot dz_a.
\]

There is no diagonal carrier multiplier in this differential. The observation
remainder \(N_a=w^\top D_2(g_a-g_{a,0})\) has derivative \(O(S^2)\)
in \(w\) and \(O(S)\) in the hidden blocks. All estimates are uniform in
the smallest positive neuron mass. The real tube used here is convex:
the displacement and operator bounds are norm bounds, and the readout bound
is an infinity-norm bound.

## 2. Real fitting and genuine autonomous cavities

The residual matrix in stable-geometry equation (10) is the sum of the
readout Gram, a Gram of the rank-one hidden updates, and a nonnegative
diagonal first-layer term. Orthogonality of the two inputs is essential
for that last diagonal form. The readout Gram changes by \(O(S^2)\);
therefore its initial gap survives at sufficiently small fixed label norm
\(Y=|y|\). The residual norm then decays exponentially and has total
integral \(O(Y)\). This closes the activity bootstrap, gives real global
existence, and gives the fitted limit and uniformly Lipschitz real-circle
prediction tails.

The initial Gaussian Gram event in candidate Section 2 is justified. The
first empirical covariance concentrates near \(qI_2\) with
\(q=\mathbb E\tanh^2Z>0\). Conditional independence of upper rows and
continuity of the Gaussian covariance-to-tanh-Gram map then give an upper
Gram near \(gI_2\), with \(g>0\). All observed products are bounded, so
exponential concentration applies at both layers. The separate Gaussian
operator, coordinate-maximum, and first-layer RMS events are compatible.

For a lower deletion, the omitted column contributes
\(e_a^z=W_{:,i}h_{a,i}\), of ordinary Euclidean norm \(O(1)\), to the
retained full top preactivation. Thus its residual-free vector-field error
in the normalized state norm is \(O(n^{-1/2})\); its integrated actual
velocity error is \(O(Yn^{-1/2})\). Its prediction discrepancy is
\(O(Yn^{-1/2})\). The deterministic comparison lemma applies using the
cavity's own observation map and its own initial readout Gram.

For an upper deletion, the additional lower velocity has ordinary norm
\(O(Y|c|)\), hence normalized norm \(O(Y|c|n^{-1/2})\). Its missing
prediction is \(w_jg_{a,j}/n=O(Y/n)\). The resulting normalized state
comparison is \(O(Y^2n^{-1/2}+Y/n)\).

Multiplying by \(\sqrt n\), with the matrix represented as
\(H=\sqrt nW\), gives precisely the two bounds in candidate equation (9).
The cavity Gram losses are \(O(n^{-1/2})\) for lower deletion and \(O(n^{-1})\)
for upper deletion. This works uniformly over all singletons on the same
initialized operator event.

These cavities really are autonomous and are independent of the omitted
Gaussian column or row. Their residuals have not been copied from the full
model. The small negative real-time extension only has fixed length; the
same transformed finite differences give \(O(Y)\) ordinary state comparison
there. No long backward-time stability is used.

## 3. Short vertical comparisons and feedback scaling

On a stopped pole-safe complex domain, all algebraic transposes in the
equations are retained, while inequalities use ordinary complex norms.
Candidate equation (12) obeys \(\|K(t)\|_{\rm op}\le C\) on the operator
and readout tubes. Positivity of complex \(K\) is neither true in general
nor needed: on the vertical path from \(t_0=\operatorname{Re}t\),

\[
 |c(t)|\le e^{C|\operatorname{Im}t|}|c(t_0)|.
\]

The real anchor supplies exponential decay in \(t_0\). Integrating the
equations vertically gives readout increments \(O(r_0|c(t_0)|)\),
matrix increments \(O(r_0Y|c(t_0)|)\), and normalized read-in increments
of the same latter order. Choosing fixed \(r_0\) and \(Y_*\) small closes
the readout and operator caps. This proves candidate equations (10)--(11)
without a factor \(e^{CT}\).

The learned entry bound \(CY^2/n\), and the corresponding row/column
norm bound \(CY^2/\sqrt n\), follow directly by integrating the actual
rank-one update along the real anchor path and then vertically. Only the
integral of the residual is used.

The feedback scaling in candidate equation (14) is correct. For a lower
deletion, with ordinary state difference \(D_c\),

\[
 \|z_a-z_a^c\|_2\le CD_c+\|e_a^z\|_2,\qquad
 |f_a-f_a^c|\le C(D_c+Y\|e_a^z\|_2)/\sqrt n.
\]

For an upper deletion add \(CY/n\) for the omitted output coordinate.
The residual-free full field has ordinary norm \(O(\sqrt n)\), so its
multiplication by the output difference costs
\(CD_c+CY\|e_a^z\|_2+CY/\sqrt n\). Fixed-residual differences cost
\(C|c|D_c+C|c|\|e_a^z\|_2\), with upper-row forcing \(O(Y|c|)\).
The real anchor difference is already \(O(Y)\); Gronwall over vertical
length at most \(r_0\) therefore gives \(D_c=O(Y)\), uniformly in the
real anchor and in \(T\).

The argument uses scalar finite differences along segments joining safe
endpoint preactivations. These segments stay in their scalar strips. It
does not require the parameter-space segment between the two complex
states to have pole-safe preactivations.

The reinsertion estimates follow at the same scale. For example,

\[
 k_{a,i}-\xi_i^\top\delta_a^{-i}
 =\xi_i^\top(\delta_a-\delta_a^{-i})
   +(W_{:,i}-\xi_i)^\top\delta_a,
\]

where \(\|\delta_a-\delta_a^{-i}\|_2=O(Y)\), including the direct
column input. The two terms are \(O(Y)\) and \(O(Y^3)\).
The upper comparison additionally includes
\(W_{j,:}^\top\delta_{a,j}=O(Y)\).
For pole transfer, the lower direct input costs only
\(C\max|W_{0,ji}|+CY^2/n\) coordinatewise, rather than its \(O(1)\)
Euclidean norm. This verifies candidate equations (16)--(17).

## 4. Stops, Gaussian conditioning, and cap closure

The full stop uses poles \(b\), lower-carrier cap
\(M=AY\sqrt\ell\), and forward-response cap \(L=AY\sqrt\ell\), with
\(\ell=\log(en/\eta)\). Each singleton uses its own pole caps \(2b\),
carrier cap \(2M\), and its own stop scale. It does not need a forward
response cap for the following estimates.

On any common prefix the deterministic differences imply cavity poles
less than \(b+CY+C\sqrt{\ell/n}<2b\) and cavity carriers less than
\(M+CY<2M\), after the stated choices. Thus a cavity cannot stop before
the full solution. This is a valid strict-margin continuation argument;
cavity survival is not assumed when proving the comparison.

The source \(q_a=\sigma'(u_a)\odot k_a\) is residual-free and satisfies
\(\dot h_a=c_aq_a\), even when \(c_a=0\). For a row cavity,

\[
 \|q_a-q_a^{-j}\|_2
 \le C\|k_a-k_a^{-j}\|_2
       +C(2M)\|u_a-u_a^{-j}\|_2
 \le C(Y+YM).
\]

Reinsertion then proves candidate equation (20). On each cavity's own
stopped domain, both independent source choices
\(\delta_a^{-i}\) and \(q_a^{-j}\) have RMS at most \(CY\).
Differentiation gives RMS at most \(CY(1+YM)\) for their time
derivatives; the only quadratic carrier product is bounded by the carrier
maximum times its RMS.

Conditional on \(A_0\) and retained initialization, the cavity, its stop
scale, and its gridded source values are deterministic. The omitted
Gaussian vector stays \(N(0,I_n/n)\). The Gaussian tail thus applies to
each reference pairing, although it does not apply directly to the full
adaptive carrier. Setting the reference to zero on a failed retained
operator/Gram event is legitimate. For query uses one also works
conditionally on the good \(A_0\) event; that event is independent of the
omitted matrix row.

A grid in the deterministic rectangle coordinates, mapped by the
retained-initialization-dependent stop scale, needs only polynomially many
points. Its mesh in candidate Section 4 gives interpolation error
\(CYn^{-5/2}\) on the initialized operator event. The logarithm of the
total count, including all cavities and both samples, is \(O_B(\ell)\).
The Gaussian estimates can therefore be intersected afterward with the
full operator/Gram event. No conditioning on a full-network stopping
event occurs.

The cap improvement reads

\[
 \max|k_a|\le C_GY\sqrt\ell+CY,\qquad
 \max|Wq_a|\le C_GY\sqrt\ell+CY+CYM.
\]

Choose the Gaussian threshold, then \(A\), then \(Y_*\). The feedback
ratio \(CYM/L=CY\) is small independently of width. The dependence of
grid constants on the fixed \(A\) affects only the eventual width
threshold. Equation (25) now gives
\(\max|\dot u_a|+\max|\dot z_a|\le CY^2\sqrt\ell\).
Vertical integration over \(r=c/\sqrt\ell\) closes the pole caps.
The usual finite-dimensional holomorphic continuation is applicable:
at each fixed width the state remains bounded before a stop, all gates
have a fixed distance from their poles, and local solutions are unique.
Strict margins continue the solution past a putative terminal scale.

## 5. Passive circle queries and paired source bounds

The same training bounds hold on each row cavity's own stopped domain.
Integrating \(\dot a_a=c_a(\Psi^{-1})'(u_a)k_a\) along the real
anchor path and vertically gives

\[
 \|a_1\|_2/\sqrt n+\|a_2\|_2/\sqrt n\le C,\qquad
 \max|a_{a,i}|\le C\sqrt\ell,\qquad
 \max|\operatorname{Im}a_{a,i}|\le4b.
\]

For complex angle, these estimates keep
\(b_\theta=a_1\cos\theta+a_2\sin\theta\) in a fixed safe first-layer
strip when \(|\operatorname{Im}\theta|\le c_\theta/\sqrt\ell\).
This is established before applying the upper query tanh.

The residual-free query vectors in candidate equation (27) are the exact
coefficients of \(c_a\) in \(\dot h_\theta\). Their RMS is \(CY\),
whereas the RMS of \(\partial_\theta h_\theta\) is bounded independently
of \(Y\). Differentiating these formulas yields equation (28). For
example the potentially largest factor in
\(\partial_\theta^2h_\theta\) is the square of the angular
preactivation derivative; its RMS is bounded by its coordinate maximum
\(C\sqrt\ell\) times its bounded RMS. The time derivatives similarly use
the carrier maximum \(2M\) times its RMS.

Row differences in the query responses cost \(C(Y+YM)\). In the
angular derivative difference, a first-gate difference multiplies a
cavity angular preactivation of maximum \(C\sqrt\ell\), giving
\(CY(1+\sqrt\ell)\). All inverse-coordinate derivatives used in these
finite differences are bounded on the proved strips.

The four-real-coordinate Gaussian grids use the row cavity's own stopped
time domain times a fixed angular strip. Their sizes are still polynomial
in \(n,T,\ell\), and their source RMS bounds give pairings
\(CY\sqrt\ell\) and \(C\sqrt\ell\). The reinsertion errors are of those
orders or smaller. Consequently both matrix orientations needed for
forward sources satisfy candidate equations (30)--(31).

At a real time and real angle, the upper query preactivation is real.
Integrating first vertically in time and then vertically in angle gives
imaginary part at most \(CY^2c+Cc_\theta<1/4\). Thus the top query
tanh is only applied after its pole margin has been proved. The bound on
\(W_0h_\theta\) follows by moving from an initial training angle around
one real angular period and then along real time; the time integral is
controlled by \(\int|c|\le CY\), rather than by \(T\).

Finally, candidate equation (32) is the exact integrated learned-matrix
identity. Its coordinatewise bound is \(CY^3\), using a bounded forward
coordinate, two response RMS bounds \(CY\), and residual integral \(CY\).
Subtracting this from the proved \(k_a\) bound controls
\(W_0^\top\delta_a\). The entire paired source list therefore has the
claimed coordinate bound on the joint complex rectangle. No query
quantity feeds back into training.

## 6. Initial jets to a small Chebyshev space

I separately reconstructed stable-geometry Section 4. This construction is
valid under its explicit rectangle hypothesis and does not use trained
snapshots.

With its notation \(v=\pi T/(8r)\), \(b=\tanh v\),
\(\alpha=\tanh(v+\pi/4)\), \(\eta=b/\alpha\), the map

\[
 z(\xi)=\frac T2+\frac{2r}{\pi}
       \log\frac{1+\alpha(\xi-\eta)/(1-\eta\xi)}
                     {1-\alpha(\xi-\eta)/(1-\eta\xi)}
\]

maps the unit disk strictly into the required time rectangle.
Indeed its imaginary part has absolute value below \(r\), and its
displacement from \(T/2\) in the real direction is less than
\((4r/\pi)\operatorname{artanh}\alpha=T/2+r\).
At \(\xi=0\), the logarithm equals \(-2v\), so \(z(0)=0\).
The real inverse maps \([0,T]\) to
\([0,\xi_*]\), where \(\xi_*=2\eta/(1+\eta^2)<1\).
The displayed difference formula for \(\alpha-b\) yields
\(1-\xi_*\ge c e^{-CT/r}\).

For a bounded source \(R\), the Taylor coefficient of \(R(z(\xi),\theta)\)
is the stated finite sum of \(\partial_t^kR(0,\theta)\), \(k\le j\).
Cauchy's estimate bounds every such coefficient by \(M\). The chosen
finite order \(J\) makes the tail at every real time at most
\(\epsilon/[4(p+1)]\), uniformly also for complex angle. This use of
a potentially enormous \(J\) is genuine analytic continuation from the
initial germ.

Chebyshev--Lobatto interpolation is then applied to computed approximations
at its nodes. These values are finite combinations of initialized
derivatives, not observed values of a trained path. Each discrete cosine
coefficient changes by at most twice the nodal perturbation, so total
interpolant error from this replacement is at most \(\epsilon/2\).
The Bernstein ellipse with parameter \(\exp(cr/T)\) lies inside the time
rectangle for a sufficiently small fixed \(c\). Its geometric Chebyshev
tail, including Lobatto aliasing, gives the stated
\(CM(T/r)e^{-cpr/T}\) bound.

For real time the resulting polynomial remains bounded by \(M+C\epsilon\)
on the angular strip. Fourier coefficient decay and equispaced-grid
aliasing therefore justify the final trigonometric interpolation. All
operations are fixed scalar linear maps, so paired sources \(R,W_0R\)
produce paired coefficient vectors \(v,W_0v\), and the same holds for the
transpose pair. It is essential that the candidate supplies bounds for
both sources in each pair; the construction has not inferred an image
error from the source error alone.

At \(T=B\ell\), \(r,r_\theta\asymp\ell^{-1/2}\),
\(M=O(\sqrt\ell)\), and \(\epsilon\asymp n^{-1/2}\), the orders are

\[
 p=O(\ell^{5/2}),\qquad L=O(\ell^{3/2}),
 \qquad (p+1)(2L+1)=O(\ell^4).
\]

Thus \(O(\ell^4)\) ordinary vector coefficients are retained per source.
Only a fixed number of sources is needed. Matching their products by
positive cubature requires \(O(\ell^8)\) nodes per layer, and the
fully stored small dense matrix has \(O(\ell^{16})\) entries.

The intermediate derivative order may be
\(\exp(O(\ell^{3/2}))\) times a logarithmic factor. It is discarded,
together with its scalar combination table and full-width intermediate
arrays, after forming the final coefficient vectors and selected model.
Under the audit's stated contract allowing unrestricted exact-real setup
and counting retained training/evaluation state, that is legitimate.
It gives no efficient preprocessing, bounded workspace during setup, or
finite-precision guarantee.

## 7. Scope of the accepted conclusion

The reconstruction establishes the high-probability complex source rectangle
through \(T=B\log(en/\eta)\), at fixed sufficiently small nonzero labels
with arbitrary component signs, for the actual finite dense model and its
whole-circle query sources. It also establishes the initialization-only
construction of the stated small retained source spaces on that rectangle.

The real fitting estimates give tails after \(T\), including at the fitted
endpoint. A final \(C/\sqrt n\) reduced-model theorem still has to choose
\(B\) large enough for those tails and verify the paired-cubature defect
and same-physical-time own-feedback comparison for the constructed small
model. Those final construction details are outside the frozen complex
source candidate and are not accepted merely by this source audit.

## 8. Objections and disposition

| Item | Severity and disposition |
|---|---|
| Complex residual matrix is not positive semidefinite | Closed. Only its bounded norm is used on a short vertical segment anchored at a real exponentially fitting solution. |
| Autonomous cavities have different residual controls | Closed. The real signed-primitive comparison includes those differences; the vertical comparison includes the \(O(\sqrt n)\) field times \(O(n^{-1/2})\) output difference. |
| Gaussian conditioning could use full adaptive data | Closed. Every reference and its stop scale use retained initialization only; full events are intersected afterward. |
| Cavity stop might occur before the full stop | Closed by the explicit common-prefix strict-margin argument. |
| Query tanh could be evaluated before its poles are controlled | Closed. Gaussian bounds use first-layer query functions, then derivatives of the unevaluated upper preactivation control its imaginary part. |
| Initial-jet construction could conceal trained snapshots | Closed. The nodal values used for interpolation are finite evaluated initial-jet sums with a proved remainder. |
| Small retained dimension might conceal large stored setup data | Closed under the specified retained-state contract; setup storage and cost are explicitly unbounded and discarded. |
| General approximation lemma states its logarithmic order bounds for every \(\epsilon>0\) | Minor formal issue. For arbitrarily large \(\epsilon\) the printed logarithms can be negative. Restrict to \(0<\epsilon\le M\), or replace them by positive logarithms such as \(\log(e+\cdot)\). The intended \(\epsilon\asymp n^{-1/2}\) regime is unaffected. |
| Candidate query formulas contain “quad” and “operatorname” without their TeX backslashes | Typographical only, in Section 5 equation (27) and the next displayed inline formula. The intended \(\quad\) and \(\operatorname{sech}^2\) are unambiguous. |

No mathematical source was repaired during this audit. The two minor
corrections above do not alter the source theorem or its application at the
requested accuracy.

## 9. Final-source confirmation

The revised TWO_INPUT_COMPLEX_SOURCE.md was checked at SHA-256
a048017ae0f87d7efb4ce845a89a26e7cd93879e5b441c5107945d561a68f60e.
The PASS verdict applies to this revision.

I verified the changed status passages, restored TeX backslashes in the
query formulas, and explicit conditioning on the good initial \(A_0\)
RMS and coordinate-maximum event for the row-query Gaussian argument.
That event uses only retained data for a row cavity, so setting a query
reference to zero off the event preserves independence of the omitted row.
No additional probabilistic or dynamical assumption has been introduced.

As a completeness check on the revision, reversing exactly these announced
edits in memory reproduced the original audited file hash
96ce9f5f1966b66082977664efcaa191d137ca646802f9d0984239bb7c4bacf9.
Thus no unreviewed changes elsewhere in the source are hidden in the new
hash. Neither source version was modified by this audit.

The supporting stable-geometry source was still at its original audited
hash when this confirmation was appended. Its general large-\(\epsilon\)
wording issue remains minor and does not affect the accepted target
accuracy; confirmation of its promised restriction is recorded separately
when that revision is available.

## 10. Final supporting-source confirmation

The revised TWO_INPUT_STABLE_GEOMETRY.md was checked at SHA-256
708182a1b52269a76ac03ecc08b8436f39fe20c7173272df5d022f9c42b29068.
The PASS verdict applies to its deterministic comparison, fitting/cavity
lemmas, and initial-jet approximation construction at this revision.

Section 4 now explicitly restricts the approximation tolerance to
\(0<\epsilon\le M\). With \(T/r\ge1\) and \(r_\theta\le1\), choosing the
displayed absolute constant at least \(e\) makes both logarithms positive.
This resolves the only mathematical wording defect identified in Section 8;
the intended \(\epsilon\asymp n^{-1/2}\) application is unchanged.

The other edits update the complexity and completion paragraphs to point
to the now-reconstructed source theorem and the separately checked final
construction. They preserve the distinction between internal checks and
promotion, add no hypotheses to the lemmas, and change no label-sign or
fixed-label quantifier. The final construction and its other review were
not imported into this scoped source audit.

Reversing exactly the tolerance restriction and those status paragraphs
in memory reproduced the original audited stable-geometry hash
93040bef724cfef765aa26d961c996297e13d67b31dcbc3fc51876ac1212c820.
Thus the rest of the supporting proof is unchanged. Both minor defects
listed in Section 8 are resolved in the confirmed final sources.
