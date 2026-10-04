# Internal check of the finite Gaussian complex-activity strip

2026-10-03. Complete independent reconstruction of Sections 1–8 of
COMPLEX_ACTIVITY_ROUTE.md, source SHA-256
d2b5f9be450435ec4e65242c6e9fa774653c8d9a601344d7f871c47cb8b753d4.
This is an internal collaborative proof check, not a promotion review.
The assigned source and required mathematical instructions were the inputs
to this check. No other new route file was read, and no source edit,
experiment, or Git operation was performed.

**Verdict: PASS for the stated training-source strip theorem.** The exact
first-coordinate transform removes the carrier-dependent multiplier from
the finite-difference estimate. The singleton cavity comparisons, their
common-prefix continuation, conditional Gaussian grids on each cavity's own
stopped domain, and the final cap bootstrap reconstruct. I found no
counterstep in the claimed one-input finite-width theorem. This verdict
does not extend the theorem to passive queries, multiple training inputs,
or a complete compression construction.

## 1. Exact equations and the inverse strip

For the training direction \(e_1\), the source uses
\[
 h=\tanh a,\quad z=Wh,\quad
 \delta=w\odot\operatorname{sech}^2z,\quad k=W^\top\delta,
\]
with activity equations
\[
 a'=\operatorname{sech}^2a\odot k,\qquad
 W'=\delta h^\top/n,\qquad w'=\tanh z.
\]
These are the exact dense equations after
\(ds/dt=2(y-f)\). All complex transposes are algebraic transposes.

Set
\[
 F(\alpha)=\alpha/2+\sinh(2\alpha)/4,\qquad u=F(a),\qquad
 H=\sqrt nW.
\]
Since \(F'(\alpha)=\cosh^2\alpha\), the chain rule cancels the first gate
and gives
\[
 u'=W^\top\delta,\quad
 H'=\delta\sigma(u)^\top/\sqrt n,\quad
 w'=\tanh(H\sigma(u)/\sqrt n),\quad
 \sigma=\tanh\circ F^{-1}.
\]
There is no approximation or changed optimizer in this substitution.

For \(|\operatorname{Im}\alpha|<\pi/4\),
\(\operatorname{Re}F'(\alpha)\ge1/2\). Integrating \(F'\) on the line
segment between distinct points proves injectivity, because the quotient
of the corresponding \(F\) difference by their difference has strictly
positive real part.

Writing \(\alpha=x+iv\) gives
\[
 \operatorname{Re}F(\alpha)
   =x/2+\sinh(2x)\cos(2v)/4,\qquad
 \operatorname{Im}F(\alpha)
   =v/2+\cosh(2x)\sin(2v)/4.
\]
The real part has the sign of \(x\) and magnitude at least \(|x|/2\).
On \(v=\pm\pi/4\), the imaginary part has magnitude at least
\(\pi/8+1/4>1/4\). Continue the real inverse along a vertical segment
inside \(|\operatorname{Im}u|<1/4\). A finite target bounds \(x\);
the preceding boundary formula prevents reaching \(|v|=\pi/4\);
and \(F'\ne0\) prevents a local inverse singularity. Thus the entire
stated horizontal \(u\)-strip belongs to the image, and its inverse branch
is holomorphic.

On the corresponding \(a\)-strip,
\[
 |\tanh a|^2
  =\frac{\cosh(2\operatorname{Re}a)-\cos(2\operatorname{Im}a)}
          {\cosh(2\operatorname{Re}a)+\cos(2\operatorname{Im}a)}
 \le1,\qquad |\operatorname{sech}^2a|\le2.
\]
Consequently \(\sigma\) is uniformly bounded on the entire \(u\)-strip,
even when the real initial \(u=F(a_0)\) is large. Fixed-radius Cauchy
disks bound all required fixed-order derivatives on the smaller strip.
In particular
\((F^{-1})'=\operatorname{sech}^2a\) and
\(\sigma'=\operatorname{sech}^4a\) are correct.

## 2. Deterministic bounds and the Euclidean finite difference

All retained dimensions are at most \(n\), and every normalization remains
\(n\). On the stopped pole domain, \(h,g\), and their gates have fixed
coordinate bounds. A radial activity segment has length at most \(2T\)
once \(r_n\le T/4\). Integration therefore gives
\[
 \|w\|_\infty+\|\delta\|_\infty\le CT,\quad
 \|W-W_0\|_{\rm op}\le CT^2,\quad
 \|W\|_{\rm op}\le K+CT^2.
\]
The rank-one estimate is
\(\|\delta h^\top/n\|_{\rm op}
 \le(\|\delta\|_2/\sqrt n)(\|h\|_2/\sqrt n)\).
It uses complex norms but does not require a conjugate transpose in the
underlying dynamics.

The derivatives
\[
 h'=\sigma'(u)\odot k,\quad
 z'=W'h+Wh',\quad
 \delta'=\operatorname{sech}^2z\odot w'
                 +(w\odot\tanh''z)\odot z'
\]
and \(k'=W'^\top\delta+W^\top\delta'\) yield all RMS bounds in (13).
If \(\|k\|_\infty\le M_c\), then
\[
 \|k^{\odot2}\|_2\le M_c\|k\|_2
\]
gives the stated \(h''\) bound \(C(1+TM_c)\sqrt n\).

For a full retained state and a cavity state define
\[
 D=\|\Delta u\|_2+\|\Delta H\|_F+\|\Delta w\|_2.
\]
The scalar strips are convex, so bounded scalar derivatives give finite
differences between the actual endpoint \(u,z\) coordinates. This does not
require pole safety of a line segment in parameter space. With external
top input \(e\),
\[
 \|\Delta h\|_2\le CD,\qquad
 \|\Delta z\|_2\le CD+\|e\|_2,\qquad
 \|\Delta\delta\|_2\le CD+CT\|e\|_2.
\]
The normalization in the middle inequality is essential:
\[
 \|(\Delta H)h^c/\sqrt n\|_2\le C\|\Delta H\|_F.
\]

For the transformed first equation,
\[
 \|\Delta(W^\top\delta)\|_2
 \le \|W\|_{\rm op}\|\Delta\delta\|_2
       +\|\Delta H\|_F\|\delta^c\|_2/\sqrt n.
\]
For the middle equation, subtract the normalized outer products:
\[
 \|\Delta(\delta h^\top/\sqrt n)\|_F
 \le C\|\Delta\delta\|_2+CT\|\Delta h\|_2.
\]
The readout equation costs \(C\|\Delta z\|_2\). Adding an external source
\(q\) to \(u'\) proves
\[
 \|\Delta u'\|_2+\|\Delta H'\|_F+\|\Delta w'\|_2
 \le CD+C\|e\|_2+\|q\|_2.
\]
The constant is independent of \(\|k\|_\infty\). This is the central
improvement over a direct calculation in the original \(a\) coordinates.

Along a complex radial segment \(s=\tau s_*\), \(0\le\tau\le1\), each
ODE derivative acquires a factor \(s_*\), whose modulus is at most \(2T\).
Ordinary real Gronwall for the norms along this segment therefore applies.

## 3. Column and row deletion bounds

For a deleted lower neuron, let \(x_i=W_{0,:,i}\). The deleted column
satisfies
\[
 \|W_{:,i}-x_i\|_2\le CT^2/\sqrt n,\qquad
 \|W_{:,i}-x_i\|_\infty\le CT^2/n.
\]
Thus its external top input \(e=W_{:,i}h_i\) has norm \(O(1)\), and its
coordinate maximum has the extra small entry factor recorded in (18).
The retained finite difference starts at zero and has forcing \(O(1)\)
over length \(O(T)\), giving \(D_i\le CT\). Substitution yields
\(\|\delta-\delta^{-i}\|_2\le CT\).

The retained carrier difference is bounded by
\[
 \|(W_{:,-i}-W^{-i})^\top\delta\|_2
 +\|(W^{-i})^\top(\delta-\delta^{-i})\|_2\le CT.
\]
For its first term, the factor \(1/\sqrt n\) in
\(W_{:,-i}-W^{-i}=\Delta H/\sqrt n\) cancels the \(O(T\sqrt n)\)
top-response norm. For the deleted coordinate,
\[
 |k_i-x_i^\top\delta^{-i}|
 \le\|x_i\|_2\|\delta-\delta^{-i}\|_2
  +\|W_{:,i}-x_i\|_2\|\delta\|_2
 \le CT.
\]
The comparison asserts no Gaussian law for the actual \(k_i\).
It also gives the \(u\)-coordinate difference \(CT\). For the top
preactivation use its retained difference plus the coordinate bound on
\(e\), giving precisely (21).

For a deleted upper neuron, let \(x_j^\top=W_{0,j,:}\). Its trained row
increment has norm \(CT^2/\sqrt n\). The extra lower source
\[
 q=W_{j,:}^\top\delta_j
\]
has norm \(CT\), so Gronwall now gives \(D_j\le CT^2\), with no
external top input in the retained system. The carrier difference includes
the deleted contribution \(q\), hence is \(CT\), rather than \(CT^2\).

If \(\|k^{-j}\|_\infty\le M_c\), then
\[
 \|h'-(h^{-j})'\|_2
 \le C\|k-k^{-j}\|_2+
       C M_c\|u-u^{-j}\|_2
 \le C(T+T^2M_c).
\]
Finally
\[
 z_j'=\delta_j h^\top h/n+x_j^\top h'
                  +(W_{j,:}-x_j^\top)h'.
\]
The first term is \(CT\); the trained-row term is \(CT^3\). Replacing
\(h'\) in the initial-row pairing by the cavity derivative costs
\(C(T+T^2M_c)\). This proves (24), including the \(T^2M_c\) feedback
term needed later.

All these comparisons use only a deleted row or column norm bound and the
two solutions' common pole-safe domain. They do not require independence
of the actual deleted-neuron history.

## 4. Stops, conditional independence, and continuation

The full pole caps are \(b\), its carrier and forward-derivative caps are
\(M=L=AT\sqrt{\ell_n}\), and each cavity has pole caps \(2b\) and
carrier cap \(2M\), with no forward-derivative cap.

These stopped solutions start locally: initial \(u,z\) are real and
\(k(0)=z'(0)=0\). Before a cap is reached, \(u'=k\), the rank-one middle
equation, and bounded readout velocity bound every state coordinate on a
scaled rectangle. For a fixed finite initialization and width these are
finite bounds, even though the real initial \(F(a_0)\) can be large.
The fixed pole margins place the state in a compact subset of the
holomorphic vector-field domain.

The continuation step can be made explicit. On a bounded cap domain, the
state's time derivative has a finite bound; this makes the state
Lipschitz along segments of the convex scaled rectangle. It therefore has
limits at boundary points. Local holomorphic Picard solutions at these
limits extend it, and local uniqueness makes the extensions agree on
overlaps. A finite cover of a compact boundary supplies extension beyond
a strictly safe scaled rectangle. This justifies using closed stop domains
and excludes a separate finite-state singularity before a displayed cap.

Now suppose a cavity's stop scale were no greater than the full stop
scale. On their common prefix, the already proved deletion estimates give
\[
 |\operatorname{Im}u^c|\le b+CT,\qquad
 |\operatorname{Im}z^c|\le b+CT+C\max|W_{0,ij}|+CT^2/n,
\]
and \(\max|k^c|\le M+CT\).
Choose \(T_0\) small and then width large, as in the source. These bounds
are strictly below \(2b,2b,2M\). Taking the limit to the cavity's alleged
stop and applying the preceding continuation argument gives a
contradiction. Thus every cavity survives through the full stopped domain.
There is no use of that survival before the common-prefix comparison.

For the Gaussian step, condition on the full real \(a_0\) and the matrix
entries retained by one cavity. Its solution, its own stop scale
\(\lambda_c\), and its stopped-domain values are functions of these data.
The omitted row or column remains an independent
\(N(0,I_n/n)\) vector. Stops and curve evaluations are measurable: local
finite-dimensional ODE dependence is continuous before the cap, and cap
suprema can be evaluated over a countable dense set, followed by monotone
continuation. If the retained operator norm exceeds \(K\), setting the
reference curve to zero is a measurable convention.

The full stop does not enter this conditioning. The operator event used
later to transfer cavity survival is intersected with the resulting
unconditional good events, rather than conditioned upon in a Gaussian tail.

## 5. Conditional grids and their probability bound

For a column cavity use \(v=\delta^{-i}\); for a row cavity use
\(v=(h^{-j})'\). On each cavity's complete own stopped domain,
\[
 \sup_s\|v(s)\|_2/\sqrt n\le CT,\qquad
 \sup_s\|v'(s)\|_2/\sqrt n\le C(1+2TM).
\]
For the row cavity, the second estimate uses its actual carrier cap
\(2M\) in the \(h''\) estimate. It does not require a bound on its
maximum forward derivative.

At any fixed stopped-domain evaluation, the real and imaginary parts of
\(x^\top v\) are centered real Gaussians with variances at most
\(\|v\|_2^2/n\le C^2T^2\). The union of their scalar tails proves (30).

Parameterize by \(s=\lambda_c q\), \(q\in D_n\), and choose a rectangular
grid with spacing comparable to
\[
 \eta_n=Tn^{-3}/(1+2TM).
\]
Its size is at most \(Cn^6(1+2TM)^2\). Both the scale and all evaluated
vectors are fixed under the retained-data conditioning. For a nearby
grid point, the line segment stays inside the stopped rectangle, and
\[
 |x^\top[v(s)-v(s_{\rm grid})]|
 \le \|x\|_2 C\sqrt n(1+2TM)\eta_n
 \le CTn^{-5/2}
\]
when \(\|x\|_2\le K\). No independence is needed for this interpolation
inequality.

Since \(M=AT\sqrt{\ell_n}\) and \(T\le T_0\), the grid size is at most
\(C_A n^6(1+\ell_n)\). Unioning the conditional fixed-point tail over
the grid, then averaging over retained data, is valid. Union over the
\(2n\) singleton cavities requires no independence between cavities.

For clarity about constants, the total failure is bounded by
\[
 C_A n^7(1+\ell_n)\exp(-c C_G^2\ell_n),
 \qquad \ell_n=\log(en/\varepsilon).
\]
A sufficiently large fixed \(C_G\) makes the exponent dominate the
polynomial power of \(n\). Choose \(A\) afterward as a fixed multiple of
\(C_G\); its fixed contribution to \(C_A\) is then absorbed by the
sufficiently-large-width threshold. This realizes the source's specified
constant order without a circular demand on \(A\).

The event \(\|W_0\|_{\rm op}\le K\) has exponentially small failure in
\(n\), by two fixed \(1/4\)-nets and Gaussian tails for their bilinear
forms. Entrywise Gaussian tails give
\(\max|W_{0,ij}|\le C\sqrt{\ell_n/n}\). The operator event supplies all
deleted row and column norm bounds. Intersecting these events with the
unconditional cavity grid events proves (31) on the full stopped domain.

## 6. Closing the four full caps

The Gaussian grid bounds plus deterministic reinsertion give
\[
 \max|k|\le C_G T\sqrt{\ell_n}+CT,\qquad
 \max|z'|\le C_G T\sqrt{\ell_n}+CT+CT^2M.
\]
Take \(A\) large, width large, and then \(T_0\) sufficiently small.
The first two terms are smaller than the appropriate fixed fraction of
\(M=L\). The last term has relative size
\[
 \frac{CT^2M}{L}=CT^2,
\]
so short fixed activity closes it. Both caps consequently improve by a
factor of two.

For a complex point \(s=s_0+i\tau\) in the full scaled rectangle, its
vertical segment starts at a real point and remains in that rectangle.
The solution is real on the real interval by uniqueness and real
initialization. Since \(u'=k\),
\[
 |\operatorname{Im}u_i(s)|\le|\tau|\sup|k_i|,\qquad
 |\operatorname{Im}z_j(s)|\le|\tau|\sup|z_j'|.
\]
The improved derivative caps and \(r_n=c/\sqrt{\ell_n}\) therefore bound
both by \(cAT/2\). Choose \(c\) small enough relative to \(A,T_0,b\);
this improves both pole caps to \(b/2\). All four full caps have strict
margins, so the continuation argument excludes a first stop below scale
one and extends the solution to a neighborhood of the closed final
rectangle.

For the optional coordinate bound, conditional on any real \(a_0\), each
initial \(z_j\) is Gaussian with variance at most one. A union bound gives
\(\|z_0\|_\infty\le C\sqrt{\ell_n}\). Canonical Gaussian \(a_0\) gives
the same bound for its maximum. Integrating \(z'\), and
\(a'=\operatorname{sech}^2a\odot k\), along radial segments proves (6).
The separate probability margins in the source suffice for all these
events.

## 7. What is certified

For one fixed training input and every sufficiently short fixed positive
activity interval, the actual finite Gaussian dense network has the stated
holomorphic rectangle of height \(c/\sqrt{\log(en/\varepsilon)}\), with
uniformly bounded activation coordinates and the stated logarithmic
carrier bounds. Constants \(T_0,c,C\) can be fixed independently of
confidence; only the sufficiently-large-width threshold depends on the
chosen \(T,\varepsilon\).

Every real activity point in the interval has an interior Cauchy disk of
radius comparable to \(r_n\), so the source's derivative bound (34)
follows. Its original first-layer response is
\(\operatorname{sech}^2a\odot k\), whose bound follows from the inverse
strip.

The proof retains the same Gaussian matrix in both orientations and works
with the actual finite trajectory. It does not substitute a Gaussian law
for its adaptive carrier. The conditional law is used only for an omitted
row or column paired with its independent autonomous cavity, and a
deterministic bound reconnects that pairing to the true state.

This certification supplies the training-source regularity input required
by a separate compression proof. Passive-input continuation, two-sided
sampling consistency, reduced-model stability, state-count arithmetic, and
the comparison with any original finite-order closure require their own
arguments. No conclusion about those missing portions is included in this
PASS.

## 8. Subsequent complete check of the circle-query and parity extension

The supervisor subsequently assigned Sections 9–10 of the expanded source,
whose frozen SHA-256 is
3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4.
I read those complete sections and reconstructed their dependence on the
already checked Sections 1–8. **Additional verdict: PASS.** This extends
the present check to the joint complex activity and circle-query theorem
and its symmetric activity rectangle.

For \(d=2\), only the first column \(a(s)\) of the first matrix evolves;
\(\beta=A_0e_2\) is fixed. The query preactivation and its angular
derivative are
\[
 b_\theta=a\cos\theta+\beta\sin\theta,\qquad
 q_\theta=-a\sin\theta+\beta\cos\theta.
\]
On the Gaussian initialization event, both \(a_0,\beta\) have bounded RMS
and coordinate maxima \(C\sqrt{\ell_n}\). Integrating
\(a'=(F^{-1})'(u)k\) gives the same bounds for the full training solution
and each row cavity on its own stopped domain. Integrating the bounded
inverse derivative along the vertical segment from \(\operatorname{Re}u\)
to \(u\) gives \(\|\operatorname{Im}a\|_\infty\le4b\).

For \(\theta=t+i\tau\), expanding sine and cosine therefore gives exactly
(41). Taking \(|\tau|\le c_\theta/\sqrt{\ell_n}\) with sufficiently
small fixed \(c_\theta\) makes every query first preactivation remain
strictly inside \(|\operatorname{Im}b_\theta|<1/4\). This step uses no
query top gate. The fixed first-layer strip controls its gates and their
derivatives uniformly in angle and every relevant cavity.

The coefficient \(B_\theta\) in (42) satisfies
\(|B_\theta|+|\partial_uB_\theta|\le C\): the inverse derivative and its
next derivative are bounded on the \(u\)-strip, and the query first gate
and its next derivative are bounded on the new first-preactivation strip.
The formulas
\[
 \partial_s h_\theta=B_\theta\odot k,\qquad
 \partial_\theta h_\theta=\operatorname{sech}^2b_\theta\odot q_\theta
\]
then give the asserted RMS bounds. In the second-derivative estimates,
\[
 \|k^{\odot2}\|_2/\sqrt n\le 2M\,CT,\qquad
 \|q_\theta^{\odot2}\|_2/\sqrt n
       \le\|q_\theta\|_\infty
                    \|q_\theta\|_2/\sqrt n
       \le C\sqrt{\ell_n}.
\]
Also \(|\partial_\theta B_\theta|\le C(1+|q_\theta|)\).
These identities prove all three estimates in (45), with no hidden
width factor.

For row deletion, \(\|u-u^{-j}\|_2\le CT^2\) implies
\(\|a-a^{-j}\|_2\le CT^2\), by the bounded inverse derivative on the
convex \(u\)-strip. Finite differences of the query first gate can be
estimated between its endpoint preactivations in their convex safe strip.
Together with the already proved carrier difference \(CT\), this gives
\[
 \|\partial_s h_\theta-\partial_s h_\theta^{-j}\|_2
                  \le C(T+T^2M).
\]
For the angular derivative, the difference of \(q_\theta\) costs
\(CT^2\), while the gate difference multiplies a cavity \(q_\theta\)
with coordinate maximum \(C\sqrt{\ell_n}\). This yields precisely
\(CT^2(1+\sqrt{\ell_n})\), as required in (46).

The conditional Gaussian argument remains valid after conditioning also
on \(\beta\). It is independent of every mixer row, and no query affects
the training cavity or its own stop. The reference vectors are
\(\partial_s h_\theta^{-j}\) and
\(\partial_\theta h_\theta^{-j}\); their respective RMS bounds are
\(CT\) and \(C\). A grid in the two real activity coordinates and two
real angular coordinates has cardinality polynomial in \(n,\ell_n\).
All first derivatives of these reference vectors in the grid coordinates
are supplied by (45). At the stated mesh, the pairing interpolation error
is \(O(n^{-5/2})\) on the deleted-row norm event. For every fixed
positive \(T\), it is smaller than the required \(T\)-scaled threshold
at sufficiently large width. Gaussian tails at the two respective scales,
followed by the grid and row unions, prove (47). As in the basic proof,
the own-cavity domain is fixed under conditioning; no adaptive full-network
event is conditioned upon.

Substituting the resulting pairings and the deterministic row-deletion
errors into (48) proves the two query top-preactivation derivative bounds.
For the learned-row terms the factors are
\[
 (CT^2/\sqrt n)(CT\sqrt n)=CT^3,\qquad
 (CT^2/\sqrt n)(C\sqrt n)=CT^2.
\]
The possible \(T^2M\) error is \(CAT^3\sqrt{\ell_n}\), with fixed
\(A\), so it fits the claimed \(CT\sqrt{\ell_n}\) activity bound.
Omitting the trained-row and rank-one update terms gives the same
bounds for \(W_0h_\theta\).

The query top gate is checked only after these derivative bounds have
been proved. Starting at real activity and real angle, integrate first
vertically in activity and then vertically in angle. Both segments stay
in the already established joint domain. Equation (49) follows and is
strictly below a fixed pole margin after reducing \(c,c_\theta\).
Thus applying tanh to the query top preactivation is justified without
circularity. The coordinate bounds follow by integration from the known
initial training preactivation around one real angular period and across
the activity rectangle. Joint holomorphy follows from composition of
holomorphic functions on this pole-free product domain.

Finally, the transformed initial value problem is invariant under
\[
 (u(s),H(s),w(s))\longmapsto
        (u(-s),H(-s),-w(-s)).
\]
The sign in the readout derivative cancels the sign from time reflection,
and the top response changes sign; hence all three equations and initial
conditions agree. Local uniqueness gives the stated parity. The reflected
solutions agree on the connected overlap of their rectangles by the
identity theorem, giving the full symmetric rectangle (51). Query
features and \(W_0h_\theta\) are even, and predictions and training
backward responses are odd.

In particular, the explicit initial-centered conformal approximation in
CANONICAL_SCALAR_AUTONOMY_ROUTE.md is compatible with this geometry: set
its \(S=T\) and its radius parameter to \(r_n/2\). Its required horizontal
range is then \([-T-r_n,T+r_n]\), contained in (51), and its imaginary
range is a strict substrip. This uses the proved parity extension and
does not assume an initial Taylor disk of radius \(T\).
