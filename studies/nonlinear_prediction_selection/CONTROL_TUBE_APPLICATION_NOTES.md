# Application checks for the frozen control-tube theorem

Author assistance, 2026-09-12. This is not an independent review.
The frozen CONTINUATION_CONTROL_TUBE.md and ROUTE_CONTINUATION.md
are unchanged. The coordinator authorized this endpoint-interface
check and a full read of FINITE_CAPTURE.md. No other route was
read; no Git operation or experiment was performed.

The principal conclusions are:

1. The control-tube theorem does give a uniform short append from
   the fitted population endpoint, by approximation with complete
   finite reference prefixes. The actual reference tail must be
   included in the control distance.
2. The named-coefficient continuity needed by the reference raw
   anchor is supplied by fixed-graph source differentiation, root
   clipping, and chronological covariance completion. No finite-
   width derivative theorem or forgotten uniform-in-mesh continuity
   assertion is necessary.
3. The finite-GF bridge preserves the actual initial readout,
   common carrier, paired observations, and width-first order.
   One prose step should be made more precise: passage of the
   small readout through a fixed graph uses the oracle cutoff
   induction, not merely finite-dimensional continuity on a raw
   ball. A precise reconstruction is given below.

## 1. The endpoint is approached, never reached at finite physical time

Use the notation CT1–CT4 from the frozen theorem. Let
\[
 \ell_*^{\rm tail}(b)
 =\int_b^\infty\sum_j|a_{*,j}(t)|\,dt
 =s_\dagger-s_*(b)\longrightarrow0.
 \tag{A1}
\]
The reference controls are
\(a_*=(e_*,-e_*,0,\ldots,0)\), not a control that stops at a
large finite b. They approach their endpoint only as
\(b\to\infty\). The actual population state
\(\theta_*(b)\) converges strongly in the raw metric to
\(\theta_\dagger\) on the same initialized carrier.

Fix any finite list of added directions and any deterministic
append control \(d=(d_1,\ldots,d_J)\), supported on
\([0,H]\), with
\[
 \int_0^H\sum_j|d_j(v)|\,dv\le\ell_0.
 \tag{A2}
\]
The physical duration H is arbitrary. For each finite b define
one control from the original initialization by
\[
 a^{b,d}(t)=
 \begin{cases}
  a_*(t),&0\le t\le b,\\
  d(t-b),&b<t\le b+H,\\
  0,&t>b+H.
 \end{cases}
 \tag{A3}
\]
Its distance from the complete, untruncated reference is bounded by
\[
 \int_0^\infty\sum_j|a_j^{b,d}(t)-a_{*,j}(t)|\,dt
 \le \ell_0+\ell_*^{\rm tail}(b).
 \tag{A4}
\]
On the append interval use
\(|d_j-a_{*,j}|\le|d_j|+|a_{*,j}|\); afterwards the cost is
the remaining reference tail. Before b the cost is zero.
Thus (A4) accounts for the full reference history exactly.

Choose \(\ell_0<\delta/4\), then choose \(b_0\) so that
\(\ell_*^{\rm tail}(b_0)<\delta/4\), where \(\delta\) is the
frozen control-tube radius. For every \(b\ge b_0\), every H,
and every append satisfying (A2), the source cap and Gaussian
query tails have the same constants. This also leaves strict
room for coefficient perturbations used in approximations.
The physical length \(b+H\) does not enter those constants.

If only the interval \([0,b+H]\) is under consideration, its
control-distance bound is smaller; the zero extension is a
convenient way to make the tail accounting explicit.
No training switch is claimed for the original mixture problem:
(A3) is a comparison construction used to build a reached-state
control class.

## 2. Finite endpoint Euler programs inherit the uniform tails

This passage is slightly stronger than merely taking a limit of
already constructed controlled paths.

Fix a finite append coefficient list
\(\gamma_{kj}\), with total absolute mass at most \(\ell_0\)
and sufficiently small maximal step mass. On the canonical
carrier define its raw Euler recursion from
\(\theta_\dagger\) by
\[
 \Theta_{0}=\theta_\dagger,\qquad
 \Theta_{k+1}=\Theta_k+\sum_j\gamma_{kj}g_{u_j}(\Theta_k).
 \tag{A5}
\]
It is well defined by finitely many continuous raw operations.
Every \(g_u\) is continuous in raw state: the upper gate uses
bounded-multiplier continuity, actual adjunction passes its
query, the lower bounded gate multiplies one fixed \(L^2\)
field after subtraction, and the middle term is an HS rank.
No ambient Lipschitz statement for the lower gate is required.

First replace \(\theta_\dagger\) by \(\theta_*(b)\). For this
fixed append list, continuity of the finitely many updates gives
convergence of all append states to (A5) as \(b\to\infty\).
At a fixed b, replace \(\theta_*(b)\) by a sufficiently fine
reference raw Euler prefix. Those prefixes are the actual
Gaussian finite programs with exact integrated reference
coefficients, and converge strongly to \(\theta_*(b)\).
Attach the same fixed append coefficient list to each prefix.
Another finite continuity induction passes the appended states
to their counterparts starting at \(\theta_*(b)\).

Each combined finite program belongs to the source tube.
To see this without tying the append coefficient mesh to a
physical mesh, realize a step \(\gamma_k\ne0\) on a physical
interval of length \(\sum_j|\gamma_{kj}|\), using constant
controls \(d_j=\gamma_{kj}/\sum_i|\gamma_{ki}|\).
The actual append mass of that interval is exactly its length.
The reference contribution to its common dominating-clock
mass is at most twice that length because \(0<e_*(t)\le1\).
Thus a maximal append mass at most \(h_0/3\) ensures the
frozen theorem's control-mesh threshold; reference prefixes
may be subdivided arbitrarily finely. Zero steps may be omitted.
The full control cost still obeys (A4).

Consequently all combined programs have the same beta-row cap
and the same Gaussian query tails, uniformly in b, the prefix
mesh, and the append mesh. Pass the tails through the two
limits in this explicit order:

1. At fixed finite b and fixed append list, refine the reference
   prefix mesh.
2. At the same fixed append list, let \(b\to\infty\).

For each fixed passive query and append node, the raw states and
their Q fields converge in \(L^2\). Use the 1-Lipschitz soft
tail \(\|(|Q|-R)_+\|_2\) and
\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2\le2\tau_R(Q)
 \tag{A6}
\]
to pass the Gaussian tail estimate with changed constants.
Those constants do not depend on the append list.
Therefore all sufficiently fine Euler programs (A5) from
\(\theta_\dagger\) have uniform passive Gaussian tails.
Their readout supremum and raw norm bounds pass in the same
way; an \(L^2\) limit of fields bounded by a common pointwise
constant has that bound by an almost surely convergent
subsequence.

The named beta-row cap is asserted for the complete-history
finite approximating programs. One need not invent a finite
source list for the endpoint \(\theta_\dagger\), nor assert
coefficientwise convergence across varying prefix partitions.
The limiting endpoint carrier, raw state, actual action and
adjoint, and the Q tails are the objects needed for completion.
All old Gaussian history is retained by the approximation;
none is reset or resampled.

The append coefficients in (A5) may have been computed by a
deterministic population feedback recursion. For the preceding
argument, freeze that finite list while approximating its
initial endpoint. The source theorem is uniform over every
admitted deterministic list, so it does not matter how that
list was chosen. This is a proof step for source bounds, not a
claim that an endpoint or later trajectory is fed to the
original finite-network optimizer.

## 3. Strong endpoint controlled completion

Let \(d\) be a fixed integrable append control of mass at most
\(\ell_0\). Parametrize by its own total variation; its control
interval has length at most \(\ell_0\), and the sum of the
absolute control densities is at most one.
Use (A5) with exact integrated coefficients on finer control
partitions and the integral interpolation CT46.
Section 2 supplies Gaussian tails uniformly in these programs.

For two append partitions, the one-reference cutoff comparison
gives
\[
 \sup_s d_{\rm raw}(\Theta^\pi(s),\Theta^{\pi'}(s))
 \le Ce^{C(1+R)\ell_0}
       \{(1+R)(|\pi|+|\pi'|)+e^{-cR^2}\}.
 \tag{A7}
\]
All constants depend only on the endpoint control neighborhood.
First send both mesh sizes to zero at fixed R, then let
\(R\to\infty\). The paths are Cauchy in the complete raw path
space. Continuity of the \(g_u\), their common bounds, and
integrability of the controls pass the integral equations to
a strong absolutely continuous solution from
\(\theta_\dagger\). Positive-part convergence passes the tails.
Uniqueness against any competing strong solution uses the
constructed solution as the sole tail-bearing reference in
(A7), with zero initial discrepancy.

There is an equivalent actual-prefix construction. Let
\(\Psi_b\) be the post-b portion of the controlled path (A3)
written on the fixed append control clock. Its initial state
is \(\theta_*(b)\), and it has the same uniform tails.
For \(b,b'\ge b_0\),
\[
 \sup_s d_{\rm raw}(\Psi_b(s),\Psi_{b'}(s))
 \le Ce^{C(1+R)\ell_0}
   \{d_{\rm raw}(\theta_*(b),\theta_*(b'))+e^{-cR^2}\}.
 \tag{A8}
\]
The initial discrepancy tends to zero on the original common
carrier. Taking \(b,b'\to\infty\) at fixed R and then removing
R gives the same endpoint-controlled solution, by uniqueness.
This proves independence of the prefix approximation.

For constrained feedback Euler, the uniform source and tail
input is now available. The remaining construction must check
the feedback coefficient continuity and the comparison modulus
on the stopped region where its anchor Gram inverse exists.
That additional step is not replaced by (A7), which compares
fixed equal controls. In particular, a positive Gram bound is
an input to the constrained feedback application, not an
assumption in the source-tube theorem.

## 4. Named-coefficient continuity in the reference raw anchor

The reference anchor CT21–CT25 uses three different limits.
Their order matters:

- At a fixed clock Euler graph and nonzero fresh forcing,
  width tends to infinity.
- At that fixed graph the forcing tends to zero, after
  establishing continuity of its named coefficient.
- Only after a mesh-uniform coefficient bound has been
  proved is the clock/raw Euler mesh refined.

There is no assertion that zero-forcing continuity is uniform
over a growing graph. The finite pulse norm bound is uniform
in the mesh, which is the property used to obtain the final cap.

For the first limit, smoothly clip the Gaussian first roots
and use an inactive smooth readout clip equal to identity on
a neighborhood of the deterministic readout interval.
The clock coordinate map \(J(X,g)\) obeys
\[
 J_X=\phi'(J),\qquad
 J_g=\frac{\phi'(J)}{\phi'(g)}.
 \tag{A9}
\]
After clipping g both derivatives are bounded at each fixed
clip level. The passive first feature is
\(\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), whose source-relevant
X derivatives are bounded independently of the root clip.
Thus the contained finite Gaussian program and its source rule
apply to the clipped forced and unforced graphs.

At any fixed graph, all named source derivatives have a finite
deterministic envelope while previous selected coefficients
remain in a compact set. This follows inductively:
the lower clock feature derivatives are bounded, the upper
tanh derivatives are bounded, the readout is bounded by total
feature length, and each action answer is its source plus a
finite linear combination with fixed coefficients.
Root derivatives are never taken in this induction.

Now remove the root clip chronologically. Earlier second
moments converge, so the next finite covariance matrix
converges. Its nonnegative square root converges even at rank
loss, by bounded subsequences and uniqueness of a nonnegative
square root. Couple on a common finite standard Gaussian list.
Node values and source derivatives converge in probability.
The deterministic derivative envelope gives uniform
integrability of derivatives, so their expectations converge.
The same argument is uniform over forcing amplitudes in a
fixed compact interval at this fixed graph. In particular it
proves coefficient continuity at zero forcing.
This is the complete continuity mechanism used by
C.4.5.2.R5–R7, not continuity of a pseudoinverse.

The fresh root z remains independent of all centered source
groups in the scalar construction. The latter's selected
covariances may depend on forcing amplitude q, but are
deterministic and frozen under differentiation. The only
local root insertion is \({\rm slot}+qz\), so
\[
 \partial_zV^q=q\,\partial_{\rm slot}V^q,\qquad
 \mathbb E[zV^q]=q\,\mathbb E[\partial_{\rm slot}V^q].
 \tag{A10}
\]
This validates the source extraction even for a zero-variance
or duplicated source slot. The unforced value law alone would
not determine such a transverse derivative.

For the raw-to-clock step, transformed raw variables
\(F(w)\) are an analysis device, not extra instructions to
which the at-most-linear value theorem is applied.
At a fixed raw graph each \(w\) has a linear envelope in the
finite Gaussian root/source list; its named derivatives have
polynomial envelopes. Multiplication by \(F'(w)=\cosh^2w\)
therefore has finite moments at that fixed graph.
The uniform defect estimate CT23 is stronger: after cancellation
its only exponential is \(e^{2h|b|}\), with a capped Gaussian
query b. CT28–CT29 give its required fixed moments uniformly
over all prefixes under the temporary cap.
The direct injection step has size \(h_s\), so dividing its
defect by \(|\bar\gamma_p|=h_s/2\) leaves \(O(h_s)\).
All later defect sums use
\(\sum_kh_k^2\le L_*h_{\max}\).

The source comparison CT24–CT25 then uses only:
bounded clock gates, the deterministic clock-pulse envelope,
the raw/clock raw-state difference, D-row coefficient
differences, and the summed normalized defect.
The current alpha is obtained before current beta; its
right side uses only old raw Q rows. Thus the cap bootstrap
does not assume its current conclusion.

I find no omitted named-coefficient continuity dependency in
this reconstruction. The canonical proof packet should retain
the complete contained III.F source/regularization proof and
C.4.5.2's clipping/forcing proof, since naming their theorems
without these bodies would conceal precisely the delicate step.
No all-orders jet theorem or uniform derivative convergence of
finite GF is needed for this anchor.

## 5. Check of FINITE_CAPTURE.md

The following parts reconstruct as stated:

- The finite metric is the normalized row/readout metric plus
  ordinary middle Frobenius increment norm. The initialized
  Gaussian middle action is controlled in operator norm.
- The actual readout has standard deviation \(1/n\);
  its maximum and normalized second moment vanish in
  probability. It is retained in both actual flow and proxy.
- Finite GF energy controls displacement on each fixed finite
  \(T\), and the pointwise readout derivative is bounded by
  \(2\sqrt{\mathcal L_n(0)}\). This gives the finite ball and
  permits continuation without assuming finite query tails.
- The reference proxy alone carries tails. Its Gaussian
  tails beat \(e^{C_TR}\) for every separately fixed
  \(T=\tau_0/\epsilon<\infty\).
- A finite union of reference and mixture proxy programs uses
  the same initialized arrays. It identifies their paired
  hidden contractions, with no finite-width endpoint.
- Width is taken at fixed positive epsilon and fixed
  population law before epsilon tends to zero. Constants and
  widths may depend on epsilon. The bridge does not claim
  otherwise.

One sentence needs a more precise mathematical reading. Bare
finite-dimensional continuity on each width's bounded initial
event does not by itself show that the small initial readout
perturbation remains small uniformly as width grows. The
continuity constants could depend on width, and the lower
gate multiplies an unbounded Q field.
The intended statement is valid by the following fixed-graph
cutoff induction.

First form the finite oracle with zero readout root using the
fixed population residuals and contractions. The fixed-program
theorem identifies every finite tuple and its second moments.
Add the actual initial readout to the proxy parameters.
At a recomputed upper backward field, use
\[
 c\phi'(Z)-\bar c\phi'(\bar Z)
 =(c-\bar c)\phi'(Z)
        +\bar c[\phi'(Z)-\phi'(\bar Z)].
 \tag{A11}
\]
The oracle readout is pointwise bounded at a fixed program,
and the additive initial readout tends to zero in supremum
and RMS. Actual adjunction then bounds the Q discrepancy
in RMS using the initialized operator bound and the finite
rank expansion.
At a lower backward field, use for its fixed oracle Q
\[
 \|[\phi'(z)-\phi'(\bar z)]\bar Q\|_{n,2}
 \le2R\|z-\bar z\|_{n,2}+2\tau_{R,n}(\bar Q).
 \tag{A12}
\]
At fixed R, first take width to infinity. The oracle tail
converges by continuous soft-cutoff second moments. Then
remove R. Every rank update and scalar contraction passes by
the ordinary two-factor RMS inequality.
Induction over the finite graph proves the additive-readout
and recomputation errors vanish. This is exactly the
C.4.7.5 mechanism cited by FINITE_CAPTURE.md, and supplies the
uniformity that ordinary finite-dimensional continuity alone
would not supply.

There are two equivalent precise proxy conventions:

1. Recompute finite fields and scalar contractions exactly
   at each proxy update, freezing only the population
   residual coefficients. Then the assigned velocity differs
   from its actual GF field only through those scalar
   prediction/residual errors.
2. Freeze all population contractions as well, obtaining a
   deterministic-coefficient oracle and finite-rank proxy.
   Then the error called \(\zeta_{n,h}\) should include the
   full assigned-versus-recomputed velocity discrepancy,
   not just the update-input prediction discrepancies.

In the second convention all components of that enlarged
\(\zeta_{n,h}\) tend to zero by (A11)–(A12) and the finite-rank
contraction induction. The comparison estimate and limit order
are unchanged. FINITE_CAPTURE.md is valid under its natural
first convention, or with this explicit enlargement under
the second convention. I found no substantive readout,
common-carrier, or width-order obstruction.

After receiving this check, the coordinator reported that
FINITE_CAPTURE.md had been corrected to include the explicit
fixed-oracle cutoff induction for the vanishing readout.
This report preserves the concrete correction and the exact
pre-correction input hash. No further audit of the changed file
was requested or performed.

## 6. Frozen inputs and remaining interface

Read in full for this author check:
FINITE_CAPTURE.md and the already authored frozen control-tube
module. The required probability and source dependencies had
been read in full in the first round, with exact line coverage
recorded in ROUTE_CONTINUATION.md. No further scientific
material was imported in this round.

| File | SHA-256 at this check |
|---|---|
| FINITE_CAPTURE.md | 1223b79d23d04ea17f9cbff6996e02822c433523c2f918903ac060c560179616 |
| CONTINUATION_CONTROL_TUBE.md | 175492fdd14a51395187cb586f2aa63b634bd688a01cbd84f3a9a043efd06cbc |
| ROUTE_CONTINUATION.md | 7f33067ed4715f53fb1f14d39a9a7b07865178519c4bdef0a344048104225a13 |

The remaining central step is the feedback construction and
selection argument: show the actual mixture's stopped controls
stay inside the tube, construct the constrained endpoint
feedback flow using its inherited tails and a positive anchor
Gram, and prove its relation to the original initialized
mixture flow. The source theorem and endpoint passage do not
claim those conclusions by themselves.
