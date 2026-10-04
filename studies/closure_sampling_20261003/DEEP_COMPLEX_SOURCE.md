# Deep complex sources from two-direction neuron insertion

2026-10-03. Internally checked post-exchange source proof.
This is not an independent promotion review and not established book material.
The original candidate was frozen at SHA-256
`8cb98569299501b6620c76b5186e4ee2fb74093d2ac3f8183717677b10723db4`.
Its complete reconstruction passed in
[DEEP_COMPLEX_SOURCE_CHECK.md](DEEP_COMPLEX_SOURCE_CHECK.md), SHA-256
`b91d5730d35baf7a2c1ee544fd8c3bdca134ca0680e535eec850205770b88015`.
The present status update makes explicit the fixed query anchor and the
forward applications of incoming-row adjoint probes requested by that
check. It preserves the derivation and its historical provenance.
The first separate attempt was frozen in `DEPTH_COMPRESSION_ROUTE.md`
at SHA-256 `d5728df96ae2dc711d2aa89fbdb0590a9d1fbd6c45d48b2441b080af0f4fdf96`
before the present source inputs were read. Its three positive propositions
remain useful, but its missing-positive-time assessment predates the
user-authorized prior deep insertion theorem.

New scientific inputs read completely are
`../dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`
(SHA-256 `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`),
`DEPTH_INSERTION_CHECK.md`, and `DEPTH_CAVITY_PROBABILITY_CHECK.md`
in that same directory, and this study's `GENERAL_WEIGHTED_COMPARISON.md`.
The supervisor supplied the proposed complex-contour extension and the
forward-response and angular trace ideas. The derivation below reconstructs
those ideas and identifies all new interfaces to the prior insertion proof.
No experiment, trained-path coefficient input, manuscript edit, or Git
operation is used.

## 1. Statement and notation

Fix hidden depth `L`, sample count `m`, and input dimension `d`. Use the
canonical Gaussian width-`n` model, zero readout, tanh in every layer,
loss `m^{-1} sum_a(f_a-y_a)^2`, and mobilities `(n,1,...,1,n)`.
The training vectors are `v_a=x_a/sqrt(d)`. Assume fixed bounded data
and a fixed positive limiting initialized readout-feature Gram. Orthogonal
inputs `v_a=e_a`, `m<=d`, satisfy this assumption by the elementary
layerwise Gaussian argument in the first depth note. Write
`Y=(m^{-1} sum_a y_a^2)^{1/2}` and `S=2Y/kappa`, where `kappa>0`
is a common small-label fitting rate for the full model and fixed-size
rectangular cavities. Take `0<Y<=Y_*`; zero labels are stationary.

For a normalized query `v=x/sqrt(d)`, the forward pass is

\[
 z^{(1)}(v)=Av,\quad h^{(1)}(v)=\tanh z^{(1)}(v),\qquad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\quad
 h^{(\ell)}(v)=\tanh z^{(\ell)}(v),\qquad
 f(v)=w^\top h^{(L)}(v)/n.
 \tag{1}
\]

Set `r_a=f(v_a)-y_a`, `k_a^(L)=w`, and

\[
 \delta_a^{(\ell)}=\tanh'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \qquad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}
 \quad(\ell<L).
 \tag{2}
\]

Use Euclidean mobility coordinates
`Theta=(A,H^(2),...,H^(L),w)`, `H^(ell)=sqrt(n) W^(ell)`, and
`F_a=n f(v_a)`. Then the exact physical equation is

\[
 \dot\Theta=-\frac2m\sum_a r_a\nabla_\Theta F_a.
 \tag{3}
\]

In complex formulas, gradients and transposes are algebraic, with no
conjugation. Norms and singular values are the usual complex norms.

Parametrize the unit sphere by the usual `(d-1)` trigonometric angles
`theta`: `v_1=cos theta_1`, `v_2=sin theta_1 cos theta_2`, and so on,
with `v_d=prod_{j<d} sin theta_j`. This covers the sphere and is periodic
in every real angle. On a fixed small product strip, this map and every
fixed number of its derivatives are bounded by constants depending on `d`.
When `d=1`, use the two queries `v=+1,-1` and omit angular notation.
All source and response families also include the finite training inputs
separately if any are outside the normalized sphere; their fixed norms
only change constants, and they have no angular variables.

Put `ell_n=log(en)` and choose a fixed sufficiently large `C_T`. The
internally checked source theorem is that, with probability tending to one, the actual
source functions

\[
 h^{(\ell)}(t,v(\theta)),\quad
 W_0^{(\ell)}h^{(\ell-1)}(t,v(\theta)),\quad
 \delta_a^{(\ell)}(t),\quad
 W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}(t)
 \tag{4}
\]

(with the natural layer ranges) are jointly holomorphic on a neighborhood
of the closed domain

\[
 -r_n\le\Re t\le C_T\ell_n+r_n,\qquad |\Im t|\le r_n,
 \qquad |\Im\theta_j|\le r_n,
 \qquad r_n=c\ell_n^{-(L+4)},
 \tag{5}
\]

and their coordinate magnitudes are at most `C ell_n^{L+2}` there.
The activation sources are bounded by a fixed constant. Constants may
depend on fixed depth/data/Gram margins and small label threshold, but
not on width or elapsed physical time.

The proof does not use the first-layer inverse transformation or require
nonvanishing activation derivatives. Tanh supplies the bounded
holomorphic gates on a fixed strip. A corresponding theorem for other
strip-holomorphic bounded activations would require their own initial
Gram assumption; no such additional theorem is asserted here.

## 2. New forward objects and exact derivative structure

For a query `v` and a driving training sample `b`, define vectors

\[
 R_b^{(\ell)}(v)=D_\Theta z^{(\ell)}(v)\nabla_\Theta F_b,
 \qquad
 Q_b^{(\ell)}(v)=D_\Theta h^{(\ell)}(v)\nabla_\Theta F_b
                =\tanh'(z^{(\ell)}(v))\odot R_b^{(\ell)}(v).
 \tag{6}
\]

These are residual-free directional responses, not velocities. In fact
`dot z^(ell)(v)=-(2/m) sum_b r_b R_b^(ell)(v)`. Direct substitution
of the block gradients into the forward derivative gives

\[
 R_b^{(1)}(v)=\delta_b^{(1)}(v_b^\top v),
\]
\[
 R_b^{(\ell)}(v)=
 \delta_b^{(\ell)}\frac{h_b^{(\ell-1)\top}h^{(\ell-1)}(v)}n
       +W^{(\ell)}Q_b^{(\ell-1)}(v),\qquad \ell\ge2.
 \tag{7}
\]

Also set `J_j^(ell)(v(theta))=partial_{theta_j} z^(ell)(v(theta))`.
Then

\[
 J_j^{(1)}=A\partial_{\theta_j}v,\qquad
 J_j^{(\ell)}=W^{(\ell)}\partial_{\theta_j}h^{(\ell-1)},
 \qquad
 \partial_{\theta_j}h^{(\ell-1)}
       =\tanh'(z^{(\ell-1)})\odot J_j^{(\ell-1)}.
 \tag{8}
\]

On a pole-safe operator tube, forward parameter derivatives have bounded
operator norm in the mobility coordinates. Their hidden-gradient argument
in (6) has Euclidean norm `CS sqrt(n)`; the readout-gradient block does
not affect a hidden preactivation. Consequently

\[
 \|R_b^{(\ell)}(v)\|_2/\sqrt n+
 \|Q_b^{(\ell)}(v)\|_2/\sqrt n\le CS,
 \qquad \|J_j^{(\ell)}(v)\|_2/\sqrt n\le C.
 \tag{9}
\]

The angular estimate uses `||A||_F/sqrt(n)<=C`. These are RMS bounds,
not coordinate assertions.

The exact derivative needed at the row-insertion endpoint is

\[
 D_\Theta Q_b^{(p)}
  =D_\Theta h^{(p)}D_\Theta^2F_b
      +D_\Theta^2h^{(p)}[\,\cdot\,,\nabla_\Theta F_b].
 \tag{10}
\]

To see its structure without suppressing a large term, hold
`V=grad F_b` fixed and differentiate the forward recursion twice. Writing
`Z^(p)U=D z^(p)[U]`, one obtains

\[
 D^2h^{(p)}[U,V]
 =\tanh''(z^{(p)})\odot(Z^{(p)}U)\odot R_b^{(p)}
      +\tanh'(z^{(p)})\odot D^2z^{(p)}[U,V],
\]
\[
 D^2z^{(p)}[U,V]
 =\frac{U_{H^{(p)}}}{\sqrt n}Q_b^{(p-1)}
 +\frac{V_{H^{(p)}}}{\sqrt n}D h^{(p-1)}[U]
 +W^{(p)}D^2h^{(p-1)}[U,V],
\]
\[
 V_{H^{(p)}}/\sqrt n
       =\delta_b^{(p)}h_b^{(p-1)\top}/n.
 \tag{11}
\]

At the first layer `D^2 z^(1)=0`. Thus the second term in (10)
contains only diagonals of forward responses at levels at most `p`,
plus mixed weight terms of bounded operator norm and rank `O_L(n)`.
It contains no forward response at level `p+1`.

For angular sources `q=partial_{theta_j}h^(p)`, the analogous exact
mixed recursion replaces `R_b` by `J_j`; its first-layer mixed term is
`U_A partial_{theta_j}v`. The mixed hidden terms are
`U_H partial_theta h^(p-1)/sqrt(n)`. They have bounded operator norm
by (9). Therefore the endpoint derivative contains only angular-response
diagonals at levels at most `p` and bounded-rank bounded terms.

Let `||T||_{u,n}=(n^{-1} tr |T|^u)^{1/u}` be the normalized Schatten
norm, also for rectangular maps. On the carrier budget introduced below,
with all lower response maxima bounded by `A_p`, (10)--(11) and the
prior explicit Hessian formula imply

\[
 \|D Q_b^{(p)}\|_{2,n}\le C,
 \qquad
 \|D Q_b^{(p)}\|_{u,n}
       \le C[1+A_p+Su(2B)^{1/u}],\qquad u\ge2,
 \tag{12}
\]

whereas for an angular source the last bound is `C(1+A_p)` and the
Schatten-2 bound is again constant. For the latter use the RMS angular
bound in (9); for the former use the RMS forward-response bound in (9)
and the RMS backward-carrier bound. The Hessian term in (10) is a
bounded-map multiple of a fixed sum of carrier diagonals and bounded-rank
bounded operators. Schatten ideal inequalities and the finite recursion
(11) give exactly (12). In particular the large endpoint factor is not
silently discarded in a trace.

## 3. Stopped complex domains and physical bounds

Fix `b_0>0` so that tanh and the first four derivatives are bounded on
`|Im z|<=8 b_0`. Choose fixed `eta_0>0` and a budget `B>L`, in the
order specified in Section 8. On scaled copies of (5), stop the full
holomorphic solution at the first of the following events:

1. a training or passive-query preactivation has imaginary part `b_0`;
2. the empirical running complex carrier budget reaches `B`;
3. a forward or angular cap below is reached.

The budget is

\[
 \frac1n\sum_{\ell<L}\sum_i
  \exp\left\{\frac{\eta_0}{S}
       \max_a\sup_{z\text{ in the current time rectangle}}
                         |k_{a,i}^{(\ell)}(z)|\right\}.
 \tag{13}
\]

Query angles do not enter training carriers. The readout is separately
bounded by `CS`. Before (13) stops,

\[
 \max|k|\le M_n:=C S\ell_n.
 \tag{14}
\]

Use forward caps `C_ell S ell_n^{ell+1}` for (6), and angular caps
`C_ell ell_n^{ell+1}` for (8), uniformly over all query angles in their
current product strip. Constants are chosen successively in layer order.
Each fixed-size neuron cavity has its own stopped domain, with carrier
budget `2B`, pole caps `2b_0`, and twice the corresponding response caps.
Its references depend only on retained initialization.

On a common pole-safe prefix, follow the contour from zero along the real
axis to `t_0=Re t`, then vertically to `t`. The real positive portion
has total residual activity `CS` and exponential residual decay by the
independently proved fitting theorem. A short negative real portion has
bounded activity and residual `CY`, by the same normalized speed bootstrap
and the residual equation. On the vertical portion,

\[
 \dot r=-(2/m)K(t)r,\qquad \|K(t)\|_{\rm op}\le C.
\]

The Gram formula is algebraic here and need not be positive, but every
feature and backward RMS is bounded on the stopped operator/readout tube.
Gronwall on the vertical segment gives

\[
 |r(t)|\le CY e^{-\kappa\max(\Re t,0)},\quad
 \|w(t)\|_\infty\le CS,\quad
 \max_{\ell\ge2}\|W^{(\ell)}(t)\|_{\rm op}\le K,
\]
\[
 \|A(t)\|_F/\sqrt n\le C,\qquad
 \max_{a,\ell}\|k_a^{(\ell)}(t)\|_2/\sqrt n\le CS.
 \tag{15}
\]

Start with strict enlarged operator/readout caps. Integrating their
rank-one and readout equations along this short segment improves those
caps for small fixed `S` and large `n`. This establishes (15) without
integrating a complex growth constant for time `T=O(log n)`.

The same substitutions in the differentiated forward/backward equations,
using only (14), give

\[
 \max_{a,\ell}\|\partial_t\delta_a^{(\ell)}(t)\|_2/\sqrt n
       \le C |r(t)|[1+SM_n],
 \tag{16}
\]

and polynomial-in-`ell_n` normalized bounds for the first derivatives
of the source vectors in (6), (8). The latter follow from (10)--(12)
and `||dot Theta||_2<=C sqrt(n)|r|`, with the hidden part of that
speed bounded by `CS sqrt(n)|r|`. No coordinate forward-velocity
bound is inferred from (16).

## 4. Complex extension of the insertion event

The prior real insertion proof is used with the following explicit
modifications; these are necessary for this proof, not consequences
of a real carrier maximum alone.

Delete a fixed number of neurons in one layer. Let `x_i` be their
initialized outgoing columns and `y_i` their initialized incoming rows,
transposed. Conditional on the retained initialization these vectors are
independent real `N(0,I/n)` roots. The retained equation, with forward
sources `e_a` and reverse sources `q_a`, is exactly

\[
 \dot\Theta=-\frac2m\sum_a r_a\left[
   \nabla_\Theta F_a(\Theta,e)
      +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right],
\]
\[
 e_a=\sum_i x_i a_{a,i}+\zeta_a,\qquad
 q_a=\sum_i y_i b_{a,i}+\chi_a.
 \tag{17}
\]

The reverse term is omitted for `j=1`. Its residual is the forward
residual and contains no artificial `q^T h` observation. Actual controls
are `a_{a,i}=h_{a,i}^(j)` and `b_{a,i}=delta_{a,i}^(j)`.
Along each real-plus-vertical contour their amplitudes are respectively
bounded and `O(M_n)`; their Lipschitz constants are at most
`sqrt(n) polylog(n)`, by (15)--(16). Learned-row/column remainders obey
`||zeta||+||chi||<=n^{-1/2} polylog(n)` exactly as in the real proof.
All these estimates allow complex scalar controls.

The cavity variational equation has the same algebraic split

\[
 D F_0=-\mathsf L\mathsf L^\top
               -\frac2m\sum_a r_aD^2F_a.
 \tag{18}
\]

On the positive real portion, the first propagator is contractive.
On the vertical portion its generator has bounded operator norm, so
its norm is at most `exp(C r_n)`; the short negative-real portion has
the same bound. Products of intervening propagators in a Dyson term
have total non-real/backwards length at most `C r_n`, giving one
factor `exp(C r_n)`, rather than one uncontrolled factor per insertion.
The residual-Hessian operator bound and total contour residual activity
`CS` give `||J||<=n^{1/1000}` after the same fixed small-label choice
as in the prior proof.

For each deterministic complex control on one contour, all linear
variations are complex linear maps of the real omitted roots. Splitting
real and imaginary parts proves the same coordinate Gaussian tail at
`n^{-1/10}` as in the real proof. Complex quadratic pairings are centered
at `tr R/n`; independent-root cross terms are centered at zero. Applying
the real Gaussian-square estimate to real and imaginary parts gives the
same exponent `n^{0.79}`, up to constants. The one-dimensional contour
control net still has log cardinality `n^{5/8} polylog(n)` at accuracy
`n^{-1/8}`. Complex controls double a fixed number of real coordinates.
A polynomial grid of real anchors, terminal heights and query angles
adds only `O(log n)` to log cardinality. Stopped first derivatives of
all coefficient maps are bounded by a fixed power of `n` times a
polylogarithm, so polynomial grid refinement suffices. The anchor grid
does not turn the control net into a two-dimensional function class.

Include in this event the linear variations of training carriers,
preactivations, passive-query preactivations, (6), (8), and the lower
incoming-row adjoint probes. Include also the forward applications
`D_Theta z^(q)(v) C_a^T y` and `D_Theta h^(q)(v) C_a^T y` at every
relevant lower layer, where `C_a=D_Theta h_a^(j-1)` and `y` is the
omitted incoming-row root at deleted layer `j`. Conditional on retained
initialization and fixed controls, these are bounded linear maps of that
same Gaussian root. They have the same coordinate and Euclidean tail
bounds, and add only finitely many observable families to the existing
parameter grids. Equations (10)--(12) give polynomial-log
operator bounds for the extra observable derivatives. Their coordinate
Gaussian images are therefore at most `n^{-1/10}`, and their Euclidean
norms at most `n^{1/100}`, on the same event after enlargement of fixed
constants. If a deletion occurs below a passive observable, its direct
forward observable source is `x_i` times its deleted activation, forward
response, or angular derivative. These scalar quantities are permitted
controls with the displayed polylogarithmic caps. The missing rank-one
weight-gradient pairing contributes `n^{-1/2} polylog(n)` in Euclidean
norm. If the deletion occurs above a passive forward response, its direct
reverse observable source is a bounded lower derivative map applied to
`y_i b_i`. Thus all additional first variations are linear root maps;
actual root-dependent coefficients are substituted only after the uniform
control event is established.

The nonlinear insertion proof keeps its power margins. Write the state
difference as the linear variation plus a remainder of norm `u`, and put
`a=1/100`, `b=1/10`. For forward, backward, forward-response and angular
coordinates, a scalar Taylor remainder has the bound

\[
 C\{n^{a-b}+n^{-b}u+u^2\},
 \tag{19}
\]

because the linear coordinate maximum is `n^{-b}` and its Euclidean
norm is `n^a`. Matrix cross terms have the additional `n^{-1/2}`.
A reference carrier or a reference forward/angular response multiplies
these errors by at most a polylogarithm. The exact mixed recursions
(10)--(11) show that differentiating a response introduces only the
bounded third gate derivative, these stopped diagonals, and the same
matrix cross terms. For angular sources the first mixed input derivative
has bounded coefficients and obeys (19). This gives the extra observable
remainders with the same power margins as the original backward ones.

The reverse source requires the independent incoming-row probe estimate:
its reference coordinates are `n^{-b}`, and its Euclidean norm is bounded.
Changing the lower state by `n^a+u` changes that probe in Euclidean norm
by `C[n^{-b}(n^a+u)+n^{-1/2}(n^a+u)]`. Its second-derivative estimate
therefore gives the prior reverse error `n^{2a-b}`, plus the corresponding
mixed terms. Scalar residual Taylor errors still carry `1/n`, and their
product with the `sqrt(n)` gradient gives `n^{2a-1/2}`. They are not
replaced by a forced residual. After integration over contour activity
`CS`, or length `O(log n)` for unweighted small terms, and propagation
by `n^{1/1000}`, the largest powers at `u<=n^{-1/25}` are strictly
smaller than this remainder cap. This closes the same nonlinear estimate.

These expansions also justify the joining strips: the linear and remainder
preactivation coordinate changes tend to zero, so all connecting arguments
remain within the larger fixed strip `|Im z|<8b_0` while either endpoint
has its prescribed pole cap. No safe parameter-space segment is assumed
without this forward expansion.

Consequently, uniformly on common stopped prefixes, every retained
carrier, training/query preactivation, and extra response coordinate
differs from its cavity counterpart by `o(1)`, for example
`C_r n^{-1/30}` after absorbing logarithms. The ordinary Euclidean
response differences are at most `C_r n^{1/100}`. Failure is
superpolynomially small and can be unioned over every set of each fixed
deletion count. This is the precise extension of the prior local insertion
interface used in the following sections.

## 5. Endpoint traces for the new forward responses

Consider singleton deletion at layer `p+1`. The lower query activation
`h^(p)(v)` itself has no direct dependence on its omitted incoming row
`y` or outgoing column `x`. Write `C_a=DTheta h^(p)(v_a)` for a
training lower derivative and `C_v=DTheta h^(p)(v)` for a query.
At the zero-source cavity define `Q=C_v grad F_b`.

The actual full lower response satisfies the exact retained identity

\[
 Q_{\rm full}=C_v(\Theta)\left[
       \nabla F_b(\Theta,e)+C_b(\Theta)^\top q_b\right].
 \tag{20}
\]

Linearizing at the zero-source cavity gives

\[
 Q_{\rm full}-Q^0
   =(D Q^0)V+C_v B_b^\top e_b+C_vC_b^\top y\,b_b
        +o_{\ell^2}(1),
 \tag{21}
\]

where `B_b=DTheta delta_b^(p+2)` is the external-forward response
endpoint when `p+1<L`, and the natural top-layer derivative is used
at the last hidden layer. The last term records the direct reverse
observable source. The state first variation `V` has the prior formula
with forward forcing `(P_a+Q_a)x a_a` and reverse forcing
`-(2/m)r_a C_a^T y b_a`. The symbol `Q_a` in this one sentence is
the prior external forcing matrix, not the vector `Q` in (20).
At the last hidden layer there is no outgoing root and no external
forward source. The omitted readout coordinate instead gives the exact
prediction offset `d_a=w_i h_{a,i}^{(L)}/n`. If `r_a^0` denotes the
retained forward residual at the current retained state, the retained
velocity is exactly

\[
 -\frac2m\sum_a(r_a^0+d_a)
       [\nabla F_a^0+C_a^\top q_a].
 \tag{21a}
\]

Here `q_a=W_{i,:}^{(L)T} delta_{a,i}^{(L)}` and
`|delta_{a,i}^{(L)}|<=CS`. The additional offset force has Euclidean
norm at most `CS/sqrt(n)`, since `|d_a|<=CS/n` and
`||grad F_a^0||<=C sqrt(n)`. Its product with the reverse probe is
at most `CS^2/n`. Integrating over the contour costs only `O(log n)`,
and the weak variational amplification leaves both terms within the
previous insertion remainder. Thus (21) applies with its forward-source
term absent and with only the independent incoming root `y`. The direct
reverse term and trace (22)--(23) remain, with the sharper amplitude
`CS` in place of `M_n`. This is an autonomous top-neuron cavity; no
full-network residual is used to define its reference.

Pair (21) with the omitted incoming row `y`. Every `x-y` bilinear
form is centered. The direct term has mean

\[
 b_b\,\operatorname{tr}(C_vC_b^\top)/n=O(M_n),
 \tag{22}
\]

because both derivative maps have bounded operator norm and rank `O(n)`.
The only nontrivial additional same-root mean is

\[
 -\frac2m\sum_a\int r_a(s)b_a(s)
      \frac1n\operatorname{tr}\{D Q^0(t)J(t,s)C_a(s)^\top\}\,ds.
 \tag{23}
\]

Assume the lower forward-response cap is `A_p`. The normalized trace
in (23) is at most `C(1+A_p)`. Here is the estimate. Expand `J` in
residual-Hessian insertions around (18)'s bounded base propagator. The
term with `h` insertions has two endpoint factors and `h` Hessian factors.
Normalized Schatten Holder at exponent `h+2`, (12), and the carrier
budget bound give a multiple of

\[
 \frac{(CS)^h}{h!}
 [1+A_p+S(h+2)(2B)^{1/(h+2)}]
 [1+S(h+2)(2B)^{1/(h+2)}]^h.
 \tag{24}
\]

There is one harmless total factor `exp(Cr_n)` from the base propagators.
For `h=0`, the two normalized Schatten-2 endpoint bounds give a constant.
For `h>=1`, split the powers into the bounded and budget-dependent parts;
`(h+2)^{h+2}/h!<=C^{h+1}(h+2)^2`. The resulting series is bounded
by `C(1+A_p)` for fixed `B` and sufficiently small `S`. The choice
is independent of `A_p`, since that factor is outside the series.
The exterior integral in (23) has `int |r|<=CS` and `|b_a|<=CM_n`.
Thus (23) is at most `CSM_n(1+A_p)`.

The learned incoming row has Euclidean increment at most
`CSM_n/sqrt(n)`. Pairing it with a forward-response source of RMS
`CS` costs `CS^2 M_n`. The Gaussian linear source `y^T Q^0` has
conditional standard deviation at most `CS`. A polynomial time/angle
grid, using (16) and (10), gives its uniform bound `CS sqrt(ell_n)`.
The quadratic fluctuations and nonlinear remainder are `o(1)` by the
uniform insertion event. Equation (7) also has the direct rank-one
term bounded by `CM_n`. Hence the next-layer response satisfies

\[
 \max|R_b^{(p+1)}|
 \le C\{M_n+S\sqrt{\ell_n}
                    +SM_n(1+A_p)+S^2M_n\}+o(1).
 \tag{25}
\]

This is triangular: no level-`p+1` response occurs on the right.
Since `M_n=O(S ell_n)`, choosing the fixed layer constants sufficiently
large proves strict margins under the caps `C_ell S ell_n^{ell+1}`.

For the angular source `q=partial_theta h^(p)(v)`, (21) has only the
state derivative `Dq V`; it has no direct reverse observable term because
it contains no training gradient. Its same-root trace is (23) with `DQ`
replaced by `Dq`, bounded by `C(1+A_p)` from the angular counterpart of
(12). Its Gaussian source has standard deviation at most `C`, and its
learned-row correction is at most `CSM_n`. Therefore

\[
 \max|J_j^{(p+1)}|
 \le C\{\sqrt{\ell_n}+SM_n(1+A_p)
                                      +SM_n\}+o(1).
 \tag{26}
\]

The first-layer angular maximum is at most `C ell_n`: initialized row
coordinates are `O(sqrt(ell_n))`, and the first-weight increment is
bounded coordinatewise by `CSM_n` using (3). Upward induction in (26)
gives strict margins under `C_ell ell_n^{ell+1}`. The real initialized
angular bounds can also be obtained before any dynamics by independent
Gaussian rows and polynomial query grids; they provide the starting
strict margins at time zero.

## 6. Cavity survival and removal of pole/response caps

Apply insertion comparisons only on the common prefix of the full and
cavity stopped domains. The retained carrier differences are `o(1)`,
so their running exponential budgets satisfy

\[
 H^{-I}\le e^{o(1)/S}H+O(|I|/n)<2B
 \tag{27}
\]

while the full budget is at most `B`. Query and training preactivation
coordinate differences are `o(1)`, so a cavity pole cannot reach `2b_0`
while the corresponding full preactivation is at most `b_0`. The extra
response differences are likewise `o(1)`, so doubled cavity response
caps cannot be hit first. This establishes cavity survival through the
full prefix without conditioning any Gaussian law on full survival.

The Gaussian source grids and the trace estimates (25)--(26) then improve
every full forward and angular cap, in layer order. For a complex point,
start from its real time and real query angle, then move vertically in
time and in each angular coordinate. Equations (6), (25), and (26) give

\[
 \max_{\ell,i}|\Im z_i^{(\ell)}(t,v(\theta))|
 \le C S Y r_n\ell_n^{L+1}+C_d r_n\ell_n^{L+1}
 \le C(1+SY)\ell_n^{-3}.
 \tag{28}
\]

This is strictly smaller than `b_0/2` for large width (or with a smaller
fixed `c`). The training case is included among the query bounds.
The estimates are obtained before applying the gate at the next query
layer: all traces for that layer use only lower query gates and training
responses. Thus no query pole estimate is assumed to prove itself.

All full response and pole caps now have strict margins. Only the full
empirical carrier budget remains as a possible obstruction.

## 7. Complex Gaussian references with a uniform exponential moment

For each cavity on its own stopped complex domain, the real reference
`delta(t)` has the prior cutoff activity modulus and conditional Gaussian
supremum bound, with constants independent of `B` once
`S^2 log(e+B)<=1`. To handle the complex part write

\[
 \delta(t+is)=\delta(t)+[\delta(t+is)-\delta(t)].
 \tag{29}
\]

After division by `S sqrt(n)`, the bracket has norm at most

\[
 D_n=C r_n\ell_n,
 \tag{30}
\]

by (16), uniformly over its stopped domain. Its two real parameter
Lipschitz constants, using the difference of two time derivatives for
the horizontal one, are at most `C ell_n`. Extend parameterization to
a fixed containing rectangle by freezing/clamping at its own stopping
scale; this choice is cavity measurable and changes only fixed constants.
Equivalently use the scaled-domain parameterization from the two-input
complex proof. If the retained initialization event fails, use the zero
reference.

The conditional Gaussian pairing of (29)'s bracket with an omitted
`N(0,I/n)` root has radius at most `C S D_n` and covering numbers
at resolution `S epsilon` bounded by `(C ell_n^C/epsilon)^2`.
A dyadic net starting at radius `D_n` therefore has mean supremum

\[
 C S D_n\sqrt{\log(C\ell_n^C/D_n)}=o(S)
 \tag{31}
\]

and Gaussian tail scale `S D_n`. This follows by summing at level `k`
the increment standard deviation `CSD_n 2^{-k}` times the square root
of the logarithm of the net cardinality. The same real/imaginary split
handles complex source values. In particular every fixed exponential
moment of this supremum divided by `S` is uniformly bounded and tends
to one. Combining with the real reference through Cauchy--Schwarz proves

\[
 E\left[\exp\left\{\lambda\max_a\sup_z
       |x_i^\top\delta_a^{-I}(z)|/S\right\}\mid\text{cavity}\right]
       \le\mathcal L_*(\lambda),
 \tag{32}
\]

where `mathcal L_*` is finite and independent of the budget and fixed
deletion count, after sufficiently large width. The width threshold may
depend on fixed `B,S,lambda`. This order is sufficient for the moment
argument; it does not require a uniform threshold over growing moments.

For comparison of singleton and fixed-block references, project their
entire cavity-measurable frozen complex difference onto the Euclidean
ball of radius `C_r n^{1/100}`. It stays independent of the particular
omitted outgoing root and agrees with the actual difference on the
successful prefix. The normalized Gaussian radius tends to zero.
A polynomial two-parameter grid is enough here: (16) gives polynomial-log
Lipschitz constants before projection, projection is nonexpansive, and
Gaussian tails at threshold `n^{-1/10}` have exponent `n^{0.78}`.
The union over the polynomial grid and all fixed-size sets remains
superpolynomially small. Thus the projected pairings are `o(1)` uniformly,
the complex analogue of the prior common-cavity estimate.

## 8. Removal of the carrier budget

The singleton backward insertion shift extends unchanged along the
contours:

\[
 |k_{a,i}^{(j)}(z)-x_i^\top\delta_a^{(j+1),-i}(z)|
                   \le CS(1+S^2B)+o(1).
 \tag{33}
\]

Its proof is the prior two-endpoint Hessian trace series with (18)'s
base factors. Those factors cost only `exp(Cr_n)`. Both endpoints retain
their carrier diagonals. The term with `h` Hessian insertions has
Schatten exponent `h+2`, exactly as in the prior proof; the budget-dependent
series starts at `S^4 B` before its exterior residual integral. The
incoming/outgoing cross term remains centered because the two real roots
are independent. Direct forward traces use carrier RMS. Rank-one residual
adaptation terms remain `n^{-1+o(1)} polylog(n)` after contour integration.
This accounts for every term in (33).

Now repeat the fixed-block empirical moment expansion, replacing real
suprema by complex-domain suprema. The moment references satisfy (32);
the common-cavity comparison after (32) makes the product use independent
outgoing roots conditionally on one cavity. Collision tuples have only
`O_p(n^{p-1})` choices and their fixed multiplicity exponential moments
are finite. For every fixed integer `p`, the layerwise moment bound has
base

\[
 D(B,S)=\mathcal L_*(\eta_0)e^{C\eta_0(1+S^2B)},
 \tag{34}
\]

independent of `p`. The failed insertion event contributes `o(1)` since
the stopped full budget is bounded. Summing over the fixed number of
layers by Minkowski gives base `(L-1)D(B,S)`.

Choose `B>4(L-1) mathcal L_*(eta_0)e^{C eta_0}` first and then
choose the label threshold so that `S^2 log(e+B)<=1`, all local and
trace smallness conditions hold, and `e^{C eta_0 S^2B}<=2`.
These choices are independent of moment degree and width. Markov gives,
for every fixed `p`, a limiting probability for hitting the full budget
at most `[(L-1)D(B,S)/B]^p`. First take the width limit at fixed `p`,
then the infimum over integers `p`; the hit probability tends to zero.
There is no growing-deletion theorem in this argument.

Initialization conditions transfer to every fixed-size cavity with strict
margins as in the prior proof. At complex-domain scale zero the time is
zero, all carriers vanish, all real query gates are pole-free, and the
initial angular Gaussian events give strict starting caps. Local
holomorphic existence and uniqueness supply the initial neighborhood.
Bounds (15), all strict cap margins, and finite-dimensional continuation
exclude any earlier loss of existence. Thus the stopped domain reaches
(5); strict margins also give a neighborhood of its closure.

## 9. Source magnitudes, construction consequences, and audit boundary

After removal of the stops, gate coordinates are bounded. Carrier and
backward-response coordinates are `O(S ell_n)` by the budget.
Choose any fixed normalized sphere anchor, for example `v=e_1`; it need
not be a training input. Its initialized preactivations are
`O(sqrt(ell_n))` by layerwise conditional Gaussian row bounds. Integrate
the forward coordinate derivative bounds along real activity and bounded
real angular paths from this anchor. Finite training inputs outside the
sphere have their own initialized values and require no angular path.
Equations (25)--(26) then give
`max |z^(ell)(t,v(theta))|<=C ell_n^{L+2}` on (5).
The learned-matrix identity gives

\[
 [(W^{(\ell)}(t)-W_0^{(\ell)})h^{(\ell-1)}(t,v)]_i
 =-\frac2m\sum_a\int r_a(s)\delta_{a,i}^{(\ell)}(s)
 \frac{h_a^{(\ell-1)}(s)^\top h^{(\ell-1)}(t,v)}n\,ds.
\]

Bounded gates, response-coordinate cap and total contour residual
activity make this `O(S^2 ell_n)`. Therefore the forward initialized
source in (4) has the asserted bound. The reverse initialized source
uses the same integral transposed: its coordinate correction is bounded
by `CS^3`, since its two response factors require only RMS estimates.
This proves the displayed source magnitude claim. Sections 4--8 and their
augmented observable interfaces were completely reconstructed in the
linked internal check.

An inverse polynomial-logarithmic radius, polynomial-logarithmic magnitude,
and a horizon `O(log n)` give polynomial-logarithmic tensor polynomial
source spaces. The initial-jet analytic continuation construction from
the two-input note applies to time; periodic analytic interpolation applies
to the fixed `d-1` angular variables. The source tolerance may be
`n^{-1/2} exp[-D sqrt(log n)]/log n` without changing this conclusion,
because its logarithm is `O(log n)`. Paired initialized matrix actions
are preserved by using identical scalar coefficient operations. Combined
with `GENERAL_WEIGHTED_COMPARISON.md` and the explicit construction in
`GENERAL_ANALYTIC_COMPRESSION.md`, this supplies the requested
all-sphere, all-time `C/sqrt(n)` neuron compression with polynomial-log
TOTAL post-setup storage. No trained snapshots or residual forcing enter
that construction.

The frozen candidate explicitly reserved judgment on the enlarged
passive-observable insertion interface in Section 4, including the top
residual offset (21a), the uniform complex-domain control/net
parameterization, and transfer of all simultaneous query pole and response
caps. The complete reconstruction in the linked check now verifies those
interfaces and the triangular trace mechanism. Its Section 9 also checks
the bounded-strip-holomorphic activation extension in
`DEEP_ACTIVATION_EXTENSION.md`. A real backward maximum alone would not
establish these interfaces. The result is internally checked research;
it has not undergone an independent promotion review or been promoted
into the maintained book or manuscript.
