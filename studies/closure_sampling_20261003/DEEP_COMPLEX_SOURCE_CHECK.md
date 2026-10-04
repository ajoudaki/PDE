# Complete reconstruction of the deep complex-source candidate

2026-10-03. Internal collaborative reconstruction, not an independent
promotion review. The complete checked source is DEEP_COMPLEX_SOURCE.md,
SHA-256
8cb98569299501b6620c76b5186e4ee2fb74093d2ac3f8183717677b10723db4.
Before relying on the prior insertion argument, I read its complete source
DEPTH_CAVITY_ROUTE.md at
e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478,
the complete DEPTH_INSERTION_CHECK.md at
77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977,
and the complete DEPTH_CAVITY_PROBABILITY_CHECK.md at
e8ec625d60753186ee5a74e67458e1f048c7edc313dc0155de54cf193e307993.
Only the bounded-activation insertion theorem is used; references to further
unbounded-activation results in the ends of those checks are not inputs.
I also reconstructed the complete GENERAL_WEIGHTED_COMPARISON.md separately.
No provisional verdict was exchanged with the depth author before this
report was frozen.

**Verdict: the tanh complex-source theorem is supported by a complete
reconstruction.** The new observable insertion argument needs the explicit
response source terms written below; with them, its Gaussian events,
nonlinear remainders, endpoint traces, and stopping-domain transfers close.
There is no extra response at the layer being estimated on the right side
of the new trace recursion. The real-carrier theorem alone would not prove
this conclusion. The proof uses the stronger complex insertion and
triangular response argument.

Two harmless clarifications should accompany the source. First, an
initialized query anchor can be any fixed point of the query sphere; a
training input need not belong to that sphere. Second, the enlarged Gaussian
probe event can explicitly include forward applications of the incoming-row
adjoint probes, as described in Section 4 below. These are bounded linear
Gaussian maps and do not change its exponent or hypotheses.

## 1. Exact equations, norm scales, and the complex physical tube

Write \(\Theta=(A,H^{(2)},\ldots,H^{(L)},w)\),
\(H^{(\ell)}=\sqrt n W^{(\ell)}\), and \(F_a=w^\top h_a^{(L)}=nf_a\).
The squared mean loss has Euclidean mobility-coordinate equation

\[
 \dot\Theta=-\frac2m\sum_a r_a\nabla F_a,\qquad r_a=f_a-y_a.
 \tag{C1}
\]

For example the \(H^{(\ell)}\) block of \(\nabla F_a\) is
\(\delta_a^{(\ell)}h_a^{(\ell-1)\top}/\sqrt n\). Thus (C1)
gives the original hidden-matrix coefficient \(2/(mn)\), while the
first-weight and readout coefficients are \(2/m\). The residual derivative
is \(\dot r=-(2/m)Kr\) with the algebraic tangent Gram. On complex
strips no positive definiteness is used, but its norm stays bounded:
each pairing in K is bounded by the forward and backward RMS bounds.

For a hidden query map, \(D_\Theta z^{(\ell)}\) has operator norm C.
At one step its matrix variation is \(U_H h/\sqrt n\); bounded feature
RMS makes its norm at most \(C\|U_H\|_F\). The hidden part of
\(\nabla F_b\) has norm \(CS\sqrt n\); its readout part does not
change any hidden query. Hence the directional query responses R,Q have
RMS CS. Angular responses have RMS C, since their first-layer source
is \(A\partial_\theta v\), followed by bounded gates and operators.

Real fitting is independent of complex continuation and holds for each
autonomous cavity with its own residual. Along a short vertical segment
from a real time, the bounded complex K gives
\(|r(t+is)|\le e^{C|s|}|r(t)|\). Integrating the parameter equations
then improves enlarged operator/readout caps for small S. This proves the
source's (15). A short negative-real segment is treated in the same way
from time zero. The total absolute residual activity on every
real-then-vertical contour is at most CS. No bound is integrated against
the long physical length \(C_T\log(en)\) unless its integrand already
has an inverse power of n.

The stopped carrier budget implies \(M_n\le CS\log(en)\) for every
fixed B and sufficiently large n. Differentiating backward gates gives

\[
 \frac{\|\dot\delta_a^{(\ell)}\|_2}{\sqrt n}
 \le C|r|(1+SM_n).
 \tag{C2}
\]

Here a changed gate multiplies one carrier maximum; its forward derivative
has RMS \(CS|r|\). An already estimated backward derivative propagates
only through bounded gates/operators. This verifies the source's (16).

## 2. Forward-response derivatives and Schatten endpoints

Put \(Z^{(p)}U=D_\Theta z^{(p)}[U]\) and \(V=\nabla F_b\).
Direct differentiation gives

\[
 R_b^{(1)}(v)=\delta_b^{(1)}(v_b^\top v),\qquad
 R_b^{(p)}(v)
 =\delta_b^{(p)}
     \frac{h_b^{(p-1)\top}h^{(p-1)}(v)}n
       +W^{(p)}Q_b^{(p-1)}(v).
 \tag{C3}
\]

Since \(Q_b^{(p)}=D_\Theta h^{(p)}V\),

\[
 DQ_b^{(p)}
 =Dh^{(p)}D^2F_b+D^2h^{(p)}[\,\cdot\,,V].
 \tag{C4}
\]

The second term expands as

\[
 D^2h^{(p)}[U,V]
 =\phi''(z^{(p)})(Z^{(p)}U)R_b^{(p)}
       +\phi'(z^{(p)})D^2z^{(p)}[U,V],
 \tag{C5}
\]

\[
 D^2z^{(p)}[U,V]
 =\frac{U_{H^{(p)}}}{\sqrt n}Q_b^{(p-1)}
  +\frac{V_{H^{(p)}}}{\sqrt n}Dh^{(p-1)}[U]
  +W^{(p)}D^2h^{(p-1)}[U,V].
 \tag{C6}
\]

The matrix \(V_{H^{(p)}}/\sqrt n\) equals
\(\delta_b^{(p)}h_b^{(p-1)\top}/n\), whose operator norm is CS.
The other mixed term in (C6) has operator norm
\(\|Q_b^{(p-1)}\|_2/\sqrt n\le CS\). Both maps have rank at most n.
The curvature term in (C5) factors through the diagonal of \(R_b^{(p)}\).
Consequently its normalized Schatten-2 norm is bounded by its RMS CS,
and its higher Schatten norm by its stopped coordinate cap. There is no
response \(R_b^{(p+1)}\) in (C4)--(C6).

The prior explicit Hessian formula decomposes \(D^2F_b\) into bounded
rank-O(n) terms and bounded-map contractions of single carrier diagonals.
It applies with algebraic transposes on the safe complex strip; singular
value estimates use ordinary complex norms. The budget bounds the diagonal
Schatten-u norms by \(CSu(2B)^{1/u}\), while the Schatten-2 estimate
uses deterministic carrier RMS. Multiplying by \(Dh^{(p)}\) preserves
these bounds. This proves precisely

\[
 \|DQ_b^{(p)}\|_{2,n}\le C,\qquad
 \|DQ_b^{(p)}\|_{u,n}
 \le C[1+A_p+Su(2B)^{1/u}],\quad u\ge2.
 \tag{C7}
\]

For \(q=\partial_{\theta_j}h^{(p)}\), replace R in the curvature
term by J. Its mixed first-layer source is \(U_A\partial_{\theta_j}v\),
and subsequent mixed matrix terms are
\(U_H\partial_{\theta_j}h^{(p-1)}/\sqrt n\), with operator norm C.
Thus \(\|Dq\|_{2,n}\le C\) and
\(\|Dq\|_{u,n}\le C(1+A_p)\). These constants do not come from an
assumed coordinate bound on a future layer.

## 3. Complex local insertion and its control event

For an interior deletion at layer j, conditional on retained initialization
the initialized outgoing columns x and incoming rows y are independent
real Gaussians with covariance \(I/n\). The exact retained equation is

\[
 \dot\Theta=-\frac2m\sum_a r_a
       [\nabla F_a(\Theta,e)+C_a(\Theta)^\top q_a],
 \quad C_a=D_\Theta h_a^{(j-1)},
 \tag{C8}
\]

with \(e_a=\sum_i x_i a_{a,i}+\zeta_a\) and
\(q_a=\sum_i y_i b_{a,i}+\chi_a\). The observation defining r uses e
and no added \(q^\top h\). The learned column and row bounds come from
integrating their actual gradient coordinates; they are respectively
\(CS^2/\sqrt n\) and \(CSM_n/\sqrt n\). Their source remainders are
\(n^{-1/2}\) times a fixed logarithmic power.

The zero-source variational operator is

\[
 DF_0=-\mathsf L\mathsf L^\top
          -\frac2m\sum_a r_aD^2F_a,\qquad
 \mathsf L=\sqrt{\frac2{mn}}[\nabla F_a]_a.
 \tag{C9}
\]

On the positive real part of the contour the first propagator is
contractive. On its vertical or negative-real part its generator has norm C,
so its norm is bounded by the exponential of C times that short length.
In a Dyson term the intervening propagator intervals partition the same
contour. Their total noncontractive length is at most \(Cr_n\); their
product therefore costs one \(e^{Cr_n}\), irrespective of the number
of Hessian insertions. The residual-Hessian operator norm is
\(C(1+M_n)\) and the contour residual mass is CS. Thus
\(\|J(t,s)\|\le e^{Cr_n+CS(1+M_n)}\le n^{1/1000}\)
with a fixed small label threshold, independently of deletion count.

For fixed deterministic complex control functions the linear retained
variation is still a linear map of the real roots. Its operator norm,
including all polynomial-logarithmic endpoint factors, is at most
\(n^{1/200}\) for sufficiently large n. Each coordinate then has
variance \(O(n^{-1+1/100})\). Splitting real and imaginary parts gives
tails \(\exp(-c n^{0.79})\) at threshold \(n^{-1/10}\).
Complex quadratic forms are centered at \(\operatorname{tr}R/n\);
independent-root bilinear forms are centered at zero. Apply the real
Gaussian-square bound to the real and imaginary symmetric parts to obtain
the same exponent. Gaussian input dimension is O(rn) for fixed deletion
count r, so the Euclidean image is at most \(n^{1/100}\) with the
required overwhelming probability despite the O(n²) parameter dimension.

Here is a concrete domain parameterization for the control-net statement.
For a terminal point \(t_0+is\), concatenate the real segment from zero
to \(t_0\) and its vertical segment. Parameterize each by arclength and
pad the resulting control to one interval of length \(C\log(en)\), by
constant extension after the terminal point. Its Lipschitz constant is at
most \(\sqrt n\) times a fixed logarithmic power. A value mesh of size
\(n^{-1/8}\) and a time mesh of that size divided by the Lipschitz
constant yield log covering number
\(n^{5/8}\operatorname{polylog}(n)\). Real and imaginary parts only
multiply fixed constants.

Terminal anchors, heights and real/imaginary angles range over a
fixed-dimensional parameter set. On the stopped safe tube, derivatives of
the coefficient maps and propagators with respect to those parameters
are bounded by a fixed power of n: recursively differentiate their explicit
matrix/gate formulas, use the fixed number of layers, the polynomial-log
caps and \(\|J\|\le n^{1/1000}\). At a contour corner, compare the
two integral pieces and their endpoint lengths separately. Thus a grid of
mesh \(n^{-K}\) for fixed sufficiently large K controls interpolation and
has polynomial size. This contributes only O(log n) to log entropy.
It does not create a net over two-dimensional control functions.

The control interpolation error is
\(n^{-1/8+1/200}\operatorname{polylog}(n)=o(n^{-1/10})\).
The net entropy exponent 0.625 is strictly below 0.79. Gaussian estimates
therefore hold uniformly over controls, terminals and angles, on the
cavity's own domain determined only by its retained initialization.
Actual root-dependent controls can then be substituted pathwise.

## 4. Explicit enlarged observable sources and nonlinear remainders

The extra observables do not feed back into (C8). First reconstruct the
complex version of the original state insertion proof. Put
\(a=1/100\), \(b=1/10\), and split the state difference into its
Gaussian linear variation V and nonlinear remainder U, with
\(\|U\|\le u=n^{-1/25}\). All linear forward/backward coordinate
variations have maximum \(n^{-b}\) and Euclidean norm at most \(n^a\).
For two such coordinate increments, their nonlinear product is bounded by

\[
 C(n^{a-b}+n^{-b}u+u^2).
 \tag{C10}
\]

Mixed matrix variations have the additional \(n^{-1/2}\), giving
\(n^{-1/2}(n^{2a}+n^au+u^2)\). These are algebraic product estimates
and apply equally to complex coordinates. Bounded gate derivatives on the
larger strip supply the Taylor formulas. The independent incoming-row
adjoint probe has coordinate maximum \(n^{-b}\) and bounded Euclidean
norm. Subtracting its lower recursion along the joining segment gives
\(C[n^{-b}(n^a+u)+n^{-1/2}(n^a+u)]\). Its Hessian bound therefore
leaves the reverse nonlinear power \(n^{2a-b}=n^{-0.08}\).

The adaptive residual is retained. Its scalar Taylor remainder is
\(n^{-1}\operatorname{polylog}(n)(n^{2a}+n^au+u^2)\);
after multiplication by the \(\sqrt n\)-sized gradient it remains
\(n^{2a-1/2}\operatorname{polylog}(n)\).
Terms weighted by r integrate against CS; the other small terms integrate
over O(log n). Propagation costs \(n^{1/1000}\). At the proposed
remainder cap every resulting power is \(o(n^{-1/25})\).
Forward expansion on the parameter joining segment keeps its preactivation
coordinates within o(1) of the pole-safe reference; this validates the
larger strip used for Taylor expansion rather than assuming it.

For completeness, the new direct response sources can be written exactly.
If the deleted layer j lies below an observed layer p, let
\(\Phi_v(\Theta,e_v)\) denote the retained query feature map there.
The omitted outgoing preactivation is
\(e_v=\sum_i W_{:,i}^{(j+1)}h_i^{(j)}(v)\). Its directional
derivative along the full training gradient is

\[
 D e_v[\nabla F_b]
 =\sum_i W_{:,i}^{(j+1)}Q_{b,i}^{(j)}(v)
 +\frac{\delta_b^{(j+1)}}n
                   \sum_i h_{b,i}^{(j)}h_i^{(j)}(v).
 \tag{C11}
\]

The second term has Euclidean norm \(CS/\sqrt n\) for fixed deletion
count. The first is \(\sum_i x_iQ_{b,i}^{(j)}(v)\) plus a permitted
\(n^{-1/2}\operatorname{polylog}(n)\) remainder. The exact retained
query response is

\[
 D_\Theta\Phi_v
       [\nabla F_b(\Theta,e_b)+C_b^\top q_b]
       +D_{e_v}\Phi_v\,D e_v[\nabla F_b].
 \tag{C12}
\]

All derivatives in (C12) hold their external source arguments fixed.
This identity includes the direct deleted-parameter contribution, the
reverse retained-gradient contribution, and the direct forward response.
If j lies above the observed layer, the external query terms disappear
and only the retained-gradient reverse source remains. If j is the observed
layer, restrict the query output to retained coordinates and apply the same
identity below/above as appropriate. At j=1 no incoming reverse source is
needed. This covers every layer relation required by the simultaneous stops.

For an angular derivative, the corresponding direct external source is
\(\sum_i x_i\partial_\theta h_i^{(j)}(v)\), plus the small learned
column correction. There is no gradient-dependent direct reverse
observable term. These scalar deleted response controls have the prescribed
polynomial-log caps; differentiating their finite recursions bounds their
contour Lipschitz constants by \(\sqrt n\operatorname{polylog}(n)\).

Linearizing (C12) gives bounded/polylogarithmic deterministic maps of x
and y for fixed controls. The additional Gaussian event may explicitly
include \(Z_v^{(q)}C_b^\top y\) and
\(Dh_v^{(q)}C_b^\top y\) at every relevant lower level. These are
bounded linear maps of y and hence obey the same coordinate and Euclidean
bounds; their number and parameter sets are already covered by the nets.
This supplies the forward applications of the lower adjoint probes.

The nonlinear response estimates now follow directly from (C3), not from
an unproved abstract smoothness assertion. Expand its scalar forward
pairing: a first variation is \(O(n^{a-1/2})\), a two-increment
remainder is \(O(n^{2a-1})\). Multiplication by the unperturbed
response of Euclidean norm \(CS\sqrt n\) gives
\(CS n^{2a-1/2}\); multiplication of a first pairing variation by a
changed response gives the same allowed power. The recursion
\(Q=\phi'(z)R\) uses (C10) for changed gates and changed R, while
unperturbed R has only a polynomial-log maximum. The angular recursion
\(\partial_\theta h=\phi'(z)J\) has exactly these same product types.
Matrix cross terms keep \(1/\sqrt n\).

In (C12), the remaining delicate term is the change of
\(D\Phi_v C_b^\top y\). Subtract it into the change of \(C_b^\top y\)
(the prior reverse-probe estimate) and the change of \(D\Phi_v\) applied
to the reference probe. For the latter, (C5)--(C6) with the probe as
second argument gives a changed preactivation times a reference forward
probe of coordinate maximum \(n^{-b}\), and matrix terms carrying
\(1/\sqrt n\). It is at most a logarithmic multiple of
\(n^{a-b}+n^{2a-b}+u^2\). This is why including the forward probe
maps in the Gaussian event is sufficient.

Thus every enlarged observable has the same strict power margin as the
state insertion proof. Retained coordinate differences are
\(O_r(n^{-1/30})\), and the Euclidean response differences are
\(O_r(n^{1/100})\), uniformly on common stopped prefixes. No hypothesis
on a compressed network or on a trained response beyond the declared stops
enters this calculation.

## 5. Top-layer deletion and the new endpoint trace

When deleting a last hidden neuron, there is no outgoing Gaussian root.
Its incoming row y is independent of the retained initialization. The
missing prediction is \(d_a=w_i h_{a,i}^{(L)}/n\), so the exact retained
velocity is

\[
 -\frac2m\sum_a(r_a^0+d_a)
              [\nabla F_a^0+C_a^\top q_a].
 \tag{C13}
\]

Here \(|d_a|\le CS/n\), \(\|\nabla F_a^0\|\le C\sqrt n\), and
\(\|q_a\|\le CS\). The two offset terms have norms \(CS/\sqrt n\)
and \(CS^2/n\). Integrating for O(log n) and applying the weak propagator
keeps them inside the insertion remainder. Dropping the product
\(d_aC_a^\top q_a\) would be algebraically wrong; (C13) and the source
include it. The reference cavity is autonomous.

For deletion at layer \(p+1\), the lower map \(h^{(p)}(v)\) has no
direct external forward query argument. Set \(C_v=Dh^{(p)}(v)\)
and \(Q^0=C_v\nabla F_b^0\). Its first variation is precisely

\[
 (DQ^0)V+C_vB_b^\top e_b+C_vC_b^\top y b_b,
 \tag{C14}
\]

with the forward term absent at the last layer. Pairing with y makes all
x-y terms centered. The direct y-y trace is
\(b_b\operatorname{tr}(C_vC_b^\top)/n=O(M_n)\).
Both derivative maps have bounded norm and rank at most n. The remaining
same-root trace is

\[
 -\frac2m\sum_a\int r_a(s)b_a(s)
    \frac{\operatorname{tr}
          [DQ^0(t)J(t,s)C_a(s)^\top]}n\,ds.
 \tag{C15}
\]

Expand J around the base propagator in (C9). At h residual-Hessian
insertions there are h+2 Schatten factors. Their normalized exponents
sum to one, canceling the factor 1/n despite the O(n²) parameter space.
By (C7), the bound is a constant times

\[
 \frac{(CS)^h}{h!}
 [1+A_p+S(h+2)(2B)^{1/(h+2)}]
 [1+S(h+2)(2B)^{1/(h+2)}]^h.
 \tag{C16}
\]

The h=0 term instead uses the uniform Schatten-2 endpoint bounds.
For h>=1 expand the two bracket contributions into bounded and
budget-dependent parts. The inequality
\((h+2)^{h+2}/h!\le C^{h+1}(h+2)^2\) bounds the latter by a
convergent geometric-polynomial series for sufficiently small fixed S.
For fixed B the whole sum is \(C(1+A_p)\); the smallness threshold
does not depend on \(A_p\). The one noncontractive base cost is
\(e^{Cr_n}\). Exterior integration in (C15) costs \(CSM_n\).

The initialized Gaussian row source has standard deviation CS and
uniform maximum \(CS\sqrt{\log(en)}\) after a polynomial query/time grid.
The learned-row correction has size \(CSM_n/\sqrt n\) paired with
a vector of norm \(CS\sqrt n\), hence \(CS^2M_n\).
Equation (C3) also has its direct term bounded by \(CM_n\).
This reconstructs the source's (25). For an angular source Dq replaces
DQ, its Gaussian RMS is C, and it has no direct reverse observable term;
the same trace gives (26).

The first-layer R maximum is \(CS\log(en)\). The first-layer angular
maximum is \(C[\sqrt{\log(en)}+S M_n]\). Inductively the right sides
at level p+1 involve only level-p maxima. Choosing successive fixed layer
constants yields strict margins under
\(C_\ell S\log(en)^{\ell+1}\) and
\(C_\ell\log(en)^{\ell+1}\). No self-dependent response maximum
has been hidden inside the endpoint estimate.

## 6. Cavity survival and removal of the nonbudget stops

Apply the insertion result only on each common full/cavity prefix.
Retained carrier differences \(o(1)\) imply
the cavity budget is at most \(e^{o(1)/S}B+O(r/n)<2B\).
The preactivation and response coordinate differences are also o(1),
so a cavity cannot reach its doubled pole or response cap first.
This proves survival without conditioning Gaussian roots on full survival.

All references required by the preceding Gaussian/trace estimates now
exist throughout the full prefix, so the triangular recursions improve
the full response caps. At a complex point start from real time and
real angles and integrate first in imaginary time, then in each imaginary
angle. With the source's radius \(r_n=c\log(en)^{-(L+4)}\), the
resulting imaginary preactivation increment is at most

\[
 C(SY+1)r_n\log(en)^{L+1}
     =C(SY+1)\log(en)^{-3}.
 \tag{C17}
\]

The time derivative is the residual sum of R; the angular derivative is J.
At the next layer these derivative estimates use only lower query gates
and training backward responses. Thus this proof does not presume the
next query gate is safe. Finite off-sphere training inputs are separate
passive cases of the same estimates. All pole and response caps have
strict margins. Only the exponential carrier budget remains to be removed.

## 7. Complex-domain Gaussian moments and budget closure

For a cavity on its own stopped rectangle, separate its backward source
into its value on the real axis and its short vertical increment. The real
part has the previously proved activity modulus
\[
 \|\delta(t)-\delta(s)\|_2/(S\sqrt n)\le C\sqrt{v},
 \tag{C18}
\]
where v is residual activity divided by S, provided
\(S^2\log(e+B)\le1\). A short negative-real interval satisfies the
same proof using absolute activity, or is included with the small
nonpositive/vertical increment. This does not change its B-independent
Gaussian exponential-moment bound.

By (C2), the normalized vertical increment has radius
\(D_n=Cr_n\log(en)\) and two real parameter Lipschitz constants
at most \(C\log(en)\). Define the complete coefficient reference on a
fixed containing rectangle by clamping its real and imaginary coordinates
to its own stopped rectangle. On the actual rectangle the map is unchanged;
clamping is 1-Lipschitz and cavity measurable. Subtract the correspondingly
clamped real-axis value. Its Gaussian covering number is bounded by
\((C\log(en)^C/\epsilon)^2\) at normalized resolution epsilon.
Dyadic increments from its small radius therefore sum to expected supremum
\[
 CS D_n\sqrt{\log(C\log(en)^C/D_n)}=o(S).
 \tag{C19}
\]

At level k the increment radius is \(SD_n2^{-k}\), and the logarithm
of its cardinality is at most a constant times
\(\log(C\log(en)^C/D_n)+k\); summing these Gaussian maxima proves
(C19) directly. Gaussian tails have scale \(SD_n\), so every fixed
exponential moment of that increment divided by S is uniformly bounded
and tends to one. Combining it with the real part by Cauchy--Schwarz
proves the stated \(\mathcal L_*(\lambda)\), independent of B after
the fixed smallness choices. Width thresholds may depend on the fixed B,
S and lambda, which is compatible with the subsequent order of limits.

For singleton/common-cavity differences, project the entire clamped
coefficient difference onto the ball of radius \(C_r n^{1/100}\).
Both references omit the relevant outgoing root, so the projected
coefficient is independent of that root. On the successful full prefix
projection is inactive. Its normalized Gaussian radius is
\(C_r n^{-1/2+1/100}\); its parameter Lipschitz constant is only
polynomial-logarithmic after normalization. A polynomial grid and Gaussian
tails at \(n^{-1/10}\) give exponent \(n^{0.78}\). This establishes
the same vanishing common-cavity pairing as in the prior real proof on
the entire complex prefix, without a root-dependent projection rule.

The old backward singleton trace uses two derivative-of-response endpoints,
both with their carrier diagonals retained. Its complex Dyson expansion
has the same h+2 factor count, now with the harmless \(e^{Cr_n}\)
base factor. Its budget-dependent series starts at \(S^4B\) before
the exterior residual integral. The direct external trace uses carrier RMS;
the incoming/outgoing term remains centered; the adaptive residual rank-one
term is \(n^{-1+o(1)}\operatorname{polylog}(n)\).
Hence the singleton shift is \(CS(1+S^2B)+o(1)\), with a constant
independent of any later moment degree. No forward-response cap appears
in this shift's constant.

Expand a layer budget's p-th moment at fixed p. Distinct tuples use their
common cavity; after pathwise domination remove the full-event indicators
and condition on that cavity. Its outgoing roots are independent. The
moment base is
\(\mathcal L_*(\eta_0)e^{C\eta_0(1+S^2B)}\), independent of p.
Collision tuples have only \(O_p(n^{p-1})\) choices and finite
fixed-multiplicity moments. Failed insertion events contribute o(1) because
the stopped full budget is bounded by B. Minkowski handles the fixed number
of layers without claiming layer independence.

Choose B first, then the fixed label threshold S small as in the source.
The moment ratio is strictly below one. For every fixed p the limsup
budget-hit probability is bounded by that ratio to the power p. Taking
the width limit first and then the infimum over fixed integers p removes
the budget stop. There is no growing-deletion assumption.

## 8. Continuation, magnitudes, and exact scope of the check

At scale zero carriers and R vanish; the real initial query angles have
safe gates. Initial angular Gaussian estimates can be constructed layer
by layer: conditional on preceding layers, the relevant row action is
Gaussian with bounded variance because its source angular derivative has
bounded RMS. Crude polynomial bounds on second angular derivatives suffice
for a polynomial grid. This supplies the initial strict response margins.
All fixed-size cavities inherit strict initial Gram/operator margins, by
the same rectangular deletion estimate as in the prior proof.

Local holomorphic ODE contraction gives the initial neighborhood. The
physical bounds and finite-dimensional coordinate bounds exclude finite
escape before a declared cap. The strict cap margins patch the local
solutions through the full closed domain and to a neighborhood of it.
This validates joint holomorphy in time and query angles for the actual
network, with its own residuals.

For source magnitudes, choose a fixed sphere anchor, for example \(e_1\).
Its initialized preactivations have maximum \(C\sqrt{\log(en)}\):
at each hidden layer conditional Gaussian rows have bounded variance,
because activations are bounded. The anchor need not be a training input.
Integrate the proved time derivative against total residual activity CS
and the angular derivatives over bounded real angular paths. This gives
the claimed polynomial-log coordinate bound for each query preactivation.
Finite training inputs have their own initialized anchor values.

The learned forward-matrix correction is an integral of a bounded
activation pairing times a response coordinate bounded by \(CS\log(en)\);
its size is \(CS^2\log(en)\). The transpose correction pairs two
backward responses in RMS and has size \(CS^3\). Thus both orientations
of the initialized source inherit the claimed magnitudes. Gates remain
bounded on the verified strip.

This proves the stated finite-depth tanh source theorem with radius
\(c\log(en)^{-(L+4)}\), magnitude \(C\log(en)^{L+2}\), logarithmic
physical horizon, finite fixed data and a positive initial Gram, on events
of probability tending to one. It proves no merely-smooth activation theorem.
The initialization-only interpolation, cubature, and autonomous weighted
comparison are separate subsequent steps. Their required source regularity
is supplied here; their storage and error conclusions still require those
constructions to be applied explicitly.

## 9. Complete reconstruction of the activation supplement

After the preceding report was frozen at
9004cc9ebc64a576243d2cfc15de8ce08fe640e5dad71b45d76f52d071fd8502,
the supervisor assigned the complete DEEP_ACTIVATION_EXTENSION.md.
I read and reconstructed its final version, SHA-256
2e772fff3b7074c8cd9f5cadf158b6cc39decb42c66eee43f381a5c15b1b22e0.
Its augmented-graph calculation independently supplies the explicit
source/remainder interface reconstructed in Sections 3--5 above.

**Supplement verdict: PASS.** The deep source result extends to fixed
layer-dependent activations that are bounded and holomorphic on a fixed
complex strip and real on the real axis, with the stated positive initial
Gram assumption. No sign or nonvanishing condition on their real slopes is
needed. Its every-layer feature certificate is valid with the additional
nonconstant-activation and orthogonal-input assumptions, in the precise
finite-width sense stated by the source.

### 9.1 Activation replacement and the augmented graph

On the half-width strip, a disk of radius a/4 remains strictly inside the
given holomorphic strip. Cauchy's integral formula therefore bounds the
j-th derivative by \(j!B_\phi(4/a)^j\), in particular for j through
four. These bounds supply real fitting, the complex local ODE, finite
differences, and all derivatives used in Gaussian grids and Taylor
remainders. The empirical Gaussian forward initialization uses bounded
feature values, without their mean being zero. Rectangular deletion is
essential when an activation has a nonzero value at zero; both source
proofs use that deletion.

Inspecting the reconstructed steps above, the only scalar activation
operations are evaluation and differentiation through this fixed finite
order, on a safe strip. The Hessian decomposition has one carrier diagonal
per curvature term regardless of slope sign. The real residual kernel is
a gradient Gram and remains nonnegative with arbitrary real slopes. The
complex estimates use absolute values. The source recursions and endpoint
traces never divide by an activation derivative. Thus no tanh identity,
oddness, monotonicity, inverse coordinate, or global injectivity is required.
The data Gram is assumed explicitly until its separate criterion is proved.

The supplement's graph order is acyclic: all forwards, all training
backwards, then forward directional responses and angular responses.
Its perturbation lemma can be checked operation by operation:

- A scalar gate remainder uses
  \(\|v^2\|_2\le\|v\|_\infty\|v\|_2\),
  \(\|v u_0\|_2\le\|v\|_\infty\|u_0\|_2\), and
  \(\|u_0^2\|_2\le\|u_0\|_2^2\).
  These give \(n^{\alpha-\beta},n^{-\beta}u,u^2\) up to
  polynomial-logarithmic factors.
- A coordinate product has those same three terms. A reference carrier,
  R or J multiplying a prior remainder costs only its declared
  polynomial-logarithmic maximum.
- A hidden matrix or transpose cross term has
  \(n^{-1/2}(n^{2\alpha}+n^\alpha u+u^2)\). The denominator comes
  from the mobility coordinate H and is present in both orientations.
- A normalized pairing has a pure quadratic error divided by n.
  Multiplication by an unperturbed response of norm \(CS\sqrt n\)
  leaves precisely the preceding \(n^{-1/2}\) scale. A previously
  controlled feature remainder contributes its Euclidean norm divided
  by \(\sqrt n\), and the same response factor cancels that denominator.

These rules prove its equation (8) by finite induction. Products with a
previous remainder do not introduce \(n^\alpha u\) without an inverse
width or small coordinate factor. The first variation from U has norm at
most a polynomial-logarithmic factor times u, as follows by differentiating
the same graph with fixed controls. Coordinate-small forward increments
keep the joining scalar arguments inside the larger strip.

The direct deleted-neuron response source in its equation (13) agrees
exactly with (C11): the missing WQ coordinate and the missing normalized
feature-pairing summand are both present. The latter has Euclidean norm
\(CS/\sqrt n\). The angular source has no pairing summand. Below the
deleted layer, the true backward source q enters before the R recursion,
so its reverse effect is included. These first variations are linear
Gaussian root maps with controls held fixed. Their finite collection fits
the original one-dimensional contour control net; the finite-dimensional
angle grid changes only polynomial cardinalities.

The top-neuron identity includes both offset terms in (C13), and its
estimates are unchanged. This confirms that the graph lemma applies to
the actual full/cavity comparison, rather than only to nearby parameter
states with omitted direct sources.

The supplement's weaker residual remainder estimate is also sufficient.
Since \(f=w^\top h^{(L)}/n\), its pure scalar remainder is bounded by
\(CE_n(u)/\sqrt n\) plus the normalized two-increment product.
Multiplying by a reference gradient of norm \(C\sqrt n\) gives
at most a polynomial-logarithmic multiple of \(E_n(u)\).
The first residual variation times the first gradient variation retains
\(n^{-1/2}\). Even without an exterior residual factor, integration costs
only O(log n). The independent-row reverse-probe calculation gives
\(n^{2\alpha-\beta}\). At \(u=n^{-0.04}\), the worst powers are
\(-0.08\), strictly below \(-0.04\) after the \(n^{0.001}\)
propagator loss. Thus the nonlinear state remainder and all augmented
coordinate comparisons close.

### 9.2 Initialized Gram and the scope of nonmonotone examples

For linearly independent normalized training vectors, their Gaussian
preactivation covariance is positive definite. A nonconstant continuous
activation preserves positive definiteness of the feature second-moment
matrix under a full-support Gaussian: a null quadratic form would give
\(\sum_a c_a\phi(z_a)=0\) everywhere by continuity; varying one
coordinate at a time forces every coefficient to vanish.
Induction applies this fact at all layers. Bounded activations give
convergence of empirical covariances through conditional bounded-variable
concentration and continuity in covariance. Thus the initial Gram condition
is automatic in that subcase.

The sine example satisfies the actual complex hypothesis:
\(|\sin(x+iy)|^2=\sin^2x+\sinh^2y\le\cosh^2a\) on the strip.
Its derivative zeros and changes of sign therefore furnish a valid example
beyond monotone saturating activations. This is a substantive consequence
of avoiding the earlier first-coordinate inverse, not an assumption that
the inverse also works for sine.

### 9.3 Every-layer feature identity and preservation

At zero readout, every hidden velocity is zero and
\[
 v=\dot w(0)=\frac2m\sum_a y_a h_a^{(L)}(0).
 \tag{C20}
\]
The Gram gap and \(y\ne0\) give \(v\ne0\). For nonconstant
holomorphic activations, the real zero set of each activation and each
derivative is discrete unless the respective function is identically zero.
For the derivative the latter would imply a constant activation and is
excluded. Conditional Gaussian rows have positive variance whenever the
preceding feature vector is nonzero. Starting at a nonzero orthogonal
input, induction therefore shows that all finitely many initialized
slopes are nonzero almost surely. The square Gaussian hidden matrices
are invertible almost surely as their determinant is a nonzero polynomial
in independent continuously distributed entries.

With \(p_a^{(\ell)}=\dot k_a^{(\ell)}(0)\) and
\(d_a^{(\ell)}=\dot\delta_a^{(\ell)}(0)\), the downward products in
the supplement consequently map v to nonzero \(d_a^{(1)}\).
Let \(c_a=2y_a/m\) at initialization. Orthogonality makes
\(\ddot A e_a=c_a d_a^{(1)}\); at least one such column is nonzero.
For hidden matrices,
\(\ddot W^{(\ell)}=n^{-1}\sum_a c_a d_a^{(\ell)}
 h_a^{(\ell-1)\top}\).

Pair the second derivative of the layer-ell forward feature with
\(c_a p_a^{(\ell)}/n\) and sum over a. The direct matrix term is
the Frobenius pairing of \(\ddot W^{(\ell)}\) with its defining
rank-one sum, hence its squared norm. Moving the other term through
the initialized transpose produces precisely the same pairing one layer
below, since \(W_0^{(\ell)\top}d_a^{(\ell)}=p_a^{(\ell-1)}\).
The base term is
\(\sum_a c_a d_a^{(1)\top}\ddot A e_a/n=\|\ddot A\|_F^2/n\).
This proves the strictly positive identity in its equation (22) with all
normalization factors unchanged.

Adding the finite initialized vectors \(d_a^{(\ell)}\) and their
paired reverse images to the cubature spaces preserves the entire
initialized downward recursion, including v. Inclusion of
\(d_a^{(1)}\) preserves the norm of each nonzero \(\ddot A\) column.
The weighted adjoint transfers each layer pairing exactly; its direct
matrix term is the squared weighted Hilbert--Schmidt norm. Hence the
selected network satisfies the strictly positive weighted identity (23).
It need not have square or invertible selected hidden matrices.

The resulting conclusion is exact nonzero hidden feature motion at each
finite width. It does not prove a width-independent displacement or
acceleration lower bound at arbitrary depth. The previously separate
two-hidden-layer RMS certificates have stronger scope on that narrower
architecture and should not be silently identified with this certificate.

## 10. Confirmation of the final clarified source versions

I read both complete revised files and verified their exact filesystem hashes:

- DEEP_COMPLEX_SOURCE.md:
  7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2.
- DEEP_ACTIVATION_EXTENSION.md:
  b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141.

Their mathematical hypotheses, source radius and magnitude, probability
quantifiers, augmented remainder bounds, activation class, and feature
certificate are unchanged from the versions reconstructed above. The new
explicit forward applications of incoming-row adjoint probes are precisely
the bounded Gaussian maps already justified in Section 4 of this check.
The new fixed sphere anchor resolves the harmless wording issue recorded
above without requiring a training input on the sphere.

The remaining revisions record internal-check status, historical hashes
and provenance. The source now points to GENERAL_ANALYTIC_COMPRESSION.md
for the final assembly with the separately checked deterministic comparison.
That pointer does not enlarge this report's source-proof verdict; the
coordinator assigns the assembly its own check. No independent promotion
status or width-independent deep feature-displacement lower bound is added.
The final clarified source and activation-extension versions retain the
PASS conclusions and scope recorded here.
