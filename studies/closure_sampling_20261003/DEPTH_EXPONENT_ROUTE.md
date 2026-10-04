# A square-root-log carrier stop sharpens the depth exponent

2026-10-04. Scoped independent candidate derivation, not an independent
promotion review or established-book result. No experiment, Git mutation,
manuscript edit, or other-file edit was performed.

The complete assigned inputs were `DEEP_COMPLEX_SOURCE.md`,
`DEEP_ACTIVATION_EXTENSION.md`, `DATASET_SOURCE_CONSTANTS.md`,
`LABEL_SEPARATE_BUDGETS.md`, `WHOLE_QUERY_RESPONSE_SOURCE.md`, and
`SAMPLE_COUNT_REFINEMENT.md`. Their references to prior-study insertion
proofs, the runtime proof, and separate check reports were not followed:
those inputs were outside this assignment. Consequently the result below
is a proof refinement conditional on the local insertion and runtime
interfaces stated in these assigned sources; it does not independently
reconstruct the inherited insertion theorem or autonomous optimizer.

The candidate was developed before scientific exchange. Its first,
weaker version used the original logarithmic carrier cap and removed
four spare powers from the common complex radius. The stronger version
below was then communicated to the coordinator. No sibling-route result
was used in the derivation.

## 1. Result and unchanged contract

Fix input dimension `d>=2`, hidden depth `L>=2`, and sample count `m`.
Each layer of the reference has width `n`. For normalized training inputs
`v_a=x_a/sqrt(d)` on the unit sphere, its forward pass is

\[
z^{(1)}(v)=Av,\quad z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),
\quad h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\quad
f(v)=w^\top h^{(L)}(v)/n.
\]

The middle recurrence is for `ell>=2`. Initialization has independent
standard Gaussian entries in `A`, independent `N(0,1/n)` entries in the
hidden matrices, and zero readout. Each activation is real on the real
axis, bounded and holomorphic on a common fixed horizontal strip.
Let `r_a=f(v_a)-y_a` and set

\[
k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
\quad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

The squared mean loss and mobilities `(n,1,...,1,n)` give physical flow

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
\dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
\dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{1}
\]

Define the initialized covariance by `Q^(0)_{ab}=v_a^T v_b` and
`Q^(ell)_{ab}=E[phi_ell(Z_a)phi_ell(Z_b)]` for
`Z~N(0,Q^(ell-1))`. Write

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\quad
\lambda=\min(1,\gamma/m),\quad
Y=\|y\|_2/\sqrt m,\quad S=C_0Y/\lambda,\quad
\ell_n=\log(en).
\]

Keep the existing condition `0<Y<=c lambda`; for the uncapped convention
this is `Y<=c gamma/m`. Structural constants depend only on `d,L` and
activation-strip bounds. All dataset quantities are fixed before the
large-width limit. The zero-label case remains stationary.

**Candidate strengthened source statement.** The common complex radius
may be replaced by

\[
                     r_n=c\ell_n^{-L/2},\qquad
                     T=C\lambda^{-1}\ell_n.             \tag{2}
\]

On the corresponding closed time rectangle and product angle strip,
the same four whole-query source families are jointly holomorphic, with
coordinate magnitudes at most `C sqrt(n)`. The time rectangle is
`-r_n<=Re t<=T+r_n`, `|Im t|<=r_n`; the angle strips are
`|Im theta_j|<=r_n` in the source's sphere parameterization.
As before, a smaller fixed multiplier gives a neighborhood of the closure.

Put `q_n=ell_n+log(e/lambda)`. The ensuing approximation degrees and
layer source dimension are

\[
\begin{aligned}
p&\le C\lambda^{-1}\ell_n^{L/2+1}q_n,\\
J&\le C\ell_n^{L/2}q_n,\\
R&\le C\lambda^{-1}\ell_n^{dL/2+1}q_n^d.
\end{aligned}                                                \tag{3}
\]

Here `p` is the time degree and `J` the degree in each of `d-1` angles.
Conditional on the inherited quadratic-storage runtime bridge, total
retained size is therefore at most

\[
C\lambda^{-2}\ell_n^{dL+2}q_n^{2d}+Cm(d+1)
\le C\lambda^{-2}\ell_n^{dL+2d+2}+Cm(d+1),                \tag{4}
\]

where the last inequality assumes `log(e/lambda)<=ell_n`.
Thus the uncapped version has prefactor `C m^2/gamma^2`, exactly as
before. In the example `d=L=2`, the logarithmic storage exponent changes
from `30` to `10`. This is not an optimality assertion.

The source-space change leaves the existing autonomous equations,
initialization-only preprocessing, own-residual property, physical clock,
whole-sphere error norm and all-time `C_data/sqrt(n)` comparison unchanged.
The quantitative comparison constant remains the one in the existing
quadratic runtime; no sharper error prefactor is asserted here.

## 2. An additional proof stop, before budget removal

Retain the separate sample budgets from `LABEL_SEPARATE_BUDGETS.md`:

\[
\mathcal H_a=\frac1n\sum_{\ell<L,i}
 \exp\left\{\frac{\eta_0}{S}
       \sup_{t\text{ in the current rectangle}}
                           |k_{a,i}^{(\ell)}(t)|\right\}\le B.
\tag{5}
\]

Here `eta_0>0` and `B>L` are fixed structural constants, chosen in the
same order as in that proof. Add the running maximum stop

\[
           \max_{a,\ell<L,i,t}|k_{a,i}^{(\ell)}(t)|
                 \le C_*S\sqrt{\ell_n}.                 \tag{6}
\]

The top carrier `w` already has coordinate bound `CS`.
Every cavity has its own budget `2B`, doubled pole caps, doubled response
caps, and twice the maximum cap in (6). All these stops are proof devices.
No equation in (1) is modified.

The inherited local insertion theorem continues to apply on common
stopped prefixes. Its proof uses bounded physical RMS/operator tubes,
fixed small total activity, carrier diagonal maxima at most a fixed
polylogarithm, polynomial-logarithmic response caps, and inverse
polynomial-logarithmic contour widths. All remain true here. Gaussian
control nets and graph Taylor remainders retain their strict powers of
`n`; replacing fixed logarithmic exponents cannot defeat these powers.
The holomorphic gate arguments stay within the same prescribed pole
stops until those stops are excluded below.

In particular the source's singleton backward insertion estimate is

\[
\sup_{a,t}|k_{a,i}^{(j)}(t)
       -x_i^\top\delta_a^{(j+1),-i}(t)|
                    \le CS(1+S^2B)+o(1),                \tag{7}
\]

where `x_i~N(0,I/n)` is independent of the singleton cavity and the
cavity uses its own residual. This estimate holds while the full stops
remain unhit. Its trace-series proof uses (5), not a pre-existing
Gaussian supremum moment on the enlarged complex domain.

The same local insertion comparison gives retained-coordinate difference
`o(1)` for every fixed-size cavity. Hence (5) transfers as
`H_a^{-I}<=exp(o(1)/S)H_a+O(|I|/n)<2B`, and (6) transfers to its
doubled cavity cap. Pole and response stops transfer in the same way.
For fixed positive `S`, none of these doubled cavity caps can be hit
before the corresponding full prefix ends. This gives cavity survival;
it does not condition a Gaussian law on full survival.

## 3. A polynomial grid improves the new maximum stop

The Gaussian bound needed to improve (6) is weaker than the bounded
exponential-moment estimate needed later to remove (5).

Freeze each singleton reference on its own stopped rectangle, using the
cavity-measurable clamping convention of the source. Conditional on its
retained initialization,

\[
\|\delta_a^{-i}(t)\|_2/\sqrt n\le CS.
\tag{8}
\]

The stopped derivative estimate in the source, valid also with the new
maximum cap, gives

\[
\|\partial_t\delta_a^{-i}(t)\|_2/\sqrt n
       \le C\rho(t)(1+SM_n),\quad
M_n=2C_*S\sqrt{\ell_n},\quad
\rho(t)=\|r(t)\|_2/\sqrt m\le CY.                       \tag{9}
\]

Even the former cap `CS ell_n` would suffice in this step: it gives a
fixed polynomial-logarithmic Lipschitz bound. Thus there is no dependence
here on having already proved the stronger maximum conclusion.

For each deterministic point in the clamped reference rectangle, the
real and imaginary parts of `x_i^T delta_a^{-i}(t)` are centered real
Gaussians of variance at most `CS^2`, by (8). Cover the containing time
rectangle by a mesh of spacing `n^-2`. Its cardinality is at most a
fixed power of `n` for all sufficiently large `n`, since `T` is a fixed
multiple of `lambda^-1 ell_n`. On the event `||x_i||_2<=C`, (9) makes
the off-grid pairing error `o(S)`. A Gaussian tail and a union over this
grid, all neurons, layers and the fixed `m` samples yield

\[
\max_{a,j,i,t}|x_i^\top\delta_a^{(j+1),-i}(t)|
                     \le C_GS\sqrt{\ell_n}              \tag{10}
\]

with probability tending to one. More explicitly, each grid tail at
threshold `K S sqrt(ell_n)` is at most `C exp(-cK^2 ell_n)`;
choosing fixed `K` above the grid's polynomial exponent makes their sum
vanish. Fixed factors involving `m,lambda` enter the width threshold.
Clamping is cavity measurable, so this calculation never treats an
adaptive full-network vector as independent of its initialized root.

Choose `S` with `S^2B<=c` as in the existing budget proof and choose
`C_*>2C_G`, enlarged for the structural constant in (7). Equations
(7) and (10) strictly improve (6) for sufficiently large width.
Only singleton references are used in this Gaussian union. There is no
need for a maximum constant growing with the later fixed-block moment
degree: all fixed-block cavities have (6) as their own doubled stop,
and their survival through the full prefix follows from insertion.

## 4. Sharper triangular response caps and exclusion of poles

In mobility coordinates `Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)`
and with `F_b=n f(v_b)`, define the same source observables as before:

\[
R_b^{(\ell)}(v)=D_\Theta z^{(\ell)}(v)\nabla_\Theta F_b,
\quad Q_b^{(\ell)}=\phi_\ell'(z^{(\ell)})\odot R_b^{(\ell)},
\quad J_j^{(\ell)}=\partial_{\theta_j}z^{(\ell)}.
\]

They satisfy the exact recursions

\[
R_b^{(1)}=\delta_b^{(1)}v_b^\top v,\qquad
R_b^{(p+1)}=\delta_b^{(p+1)}
 \frac{h_b^{(p)\top}h^{(p)}(v)}n+W^{(p+1)}Q_b^{(p)},
\]
\[
J_j^{(1)}=A\partial_{\theta_j}v,\qquad
J_j^{(p+1)}=W^{(p+1)}
 [\phi_p'(z^{(p)})\odot J_j^{(p)}].
\tag{11}
\]

Use the inherited endpoint-trace estimates, equations (25)--(26) of
`DEEP_COMPLEX_SOURCE.md`. If `A_p` denotes the applicable lower response
maximum, they state on common stopped prefixes

\[
\max|R_b^{(p+1)}|
 \le C\{M_n+S\sqrt{\ell_n}+SM_n(1+A_p)+S^2M_n\}+o(1),
\]
\[
\max|J_j^{(p+1)}|
 \le C\{\sqrt{\ell_n}+SM_n(1+A_p)+SM_n\}+o(1).
\tag{12}
\]

Their trace factors involve only lower-layer response diagonals. The
single carrier maximum `M_n` comes from the omitted reverse-source
amplitude and learned incoming row; it can be replaced by (6) without
changing the trace proof or its normalized sample sums.

The first line of (11) gives `max|R_b^(1)|<=CS sqrt(ell_n)`.
For the angular start, the initialized first-weight row norms are
`O(sqrt(ell_n))`, while (1), total activity `CS`, and (6) give
`max_i ||A_i(t)-A_i(0)||<=CS M_n`. The derivatives of the fixed sphere
map are bounded on a fixed small product strip. Hence
`max|J_j^(1)|<=C sqrt(ell_n)`.

Substitute `M_n=C_*S sqrt(ell_n)` into (12). Upward induction, choosing
the fixed layer constants successively, gives strict improvements under
the proposed caps

\[
\max|R_b^{(\ell)}|\le C_\ell S\ell_n^{\ell/2},\qquad
\max|J_j^{(\ell)}|\le C_\ell\ell_n^{\ell/2}.             \tag{13}
\]

For example the only potentially highest-degree term in the first
recurrence is `S M_n A_p`; if
`A_p=C_pS ell_n^(p/2)`, it equals
`C_* C_p S^3 ell_n^((p+1)/2)`, below the next cap after choosing its
constant. The angular induction has the same logarithmic power.
No smallness of `S sqrt(ell_n)` is required.

At a complex point first move from its real time and real query angle
vertically in time, then in each angle. Since
`dot z=-(2/m)sum_b r_b R_b`, (13) bounds the imaginary preactivation by

\[
C r_n SY\ell_n^{L/2}+C_d r_n\ell_n^{L/2}
                  \le Cc(1+SY).                         \tag{14}
\]

Here (2) was used. Under the unchanged small-label condition, `S` and
`SY` are structurally bounded. Choose `c` in (2) sufficiently small to
put (14) strictly inside half the prescribed pole margin. The finite
layer constants may depend on `L`, as already allowed. Thus a vanishing
pole margin is unnecessary; a fixed strict margin suffices. The response
estimate for each layer is obtained from lower query gates and training
responses before excluding that layer's possible query pole, exactly
as in the original triangular argument.

## 5. The empirical budgets still close on the larger rectangle

The only remaining stop is (5). Its real Gaussian reference moment is
the unchanged single-sample estimate from `LABEL_SEPARATE_BUDGETS.md`.
For the complex correction, (9) and `Y/S<=C lambda<=C` give

\[
\frac{\|\delta_a(t+is)-\delta_a(t)\|_2}{S\sqrt n}
 \le Cr_n(1+S^2\sqrt{\ell_n})
 \le D_n:=C\ell_n^{-(L-1)/2}.                            \tag{15}
\]

This is the normalized Gaussian radius of the bracket. Its two real
parameter Lipschitz constants are bounded by `C sqrt(ell_n)` using
(9); clamping at the cavity's own stop preserves that order. A covering
number at normalized Gaussian resolution `epsilon` is bounded by
`(C lambda^-1 ell_n^C/epsilon)^2`.

For completeness, a dyadic net starting at radius `D_n` has increments
with Gaussian standard deviation at most `C D_n 2^-k`. The number of
increments at level `k` has logarithm at most
`C[log(C lambda^-1 ell_n^C/D_n)+k]`. Gaussian tails and a union bound
over levels, followed by summation of `2^-k sqrt(k)`, bound the mean
supremum by

\[
C D_n\sqrt{\log(C\lambda^{-1}\ell_n^C/D_n)}=o(1),        \tag{16}
\]

and give a tail with scale `C D_n`. The convergence uses `L>=2` and
fixed positive `lambda`; in particular it holds for `L=2`.
Integrating that tail shows that each fixed exponential moment of the
complex correction tends to one. The real/imaginary Gaussian split
changes constants only.

Applying Cauchy--Schwarz for one sample therefore gives the same bounded
single-sample complex exponential moment as before, independent of `m`
and the later moment degree. The fixed-block moment argument in
`LABEL_SEPARATE_BUDGETS.md` then gives
`limsup P{any full budget hits B}<=m vartheta^p` for every fixed
integer `p`, with structural `vartheta<1`. Take width to infinity
first, then the infimum over fixed `p`.

This removes the remaining stop without a stronger label condition.
The logical order is: impose the extra maximum stop; obtain Gaussian
grid control; exclude that maximum stop and the triangular response and
pole stops; use the improved stopped derivative to close empirical
moments. The Gaussian grid step does not use the empirical moment
conclusion. Cavity references carry their own stops throughout.

Local holomorphic existence, bounded physical parameters and the strict
stop margins give continuation to the full rectangle. The augmented
insertion graph uses bounded holomorphic derivatives and no divisions
by activation slopes, so the activation extension remains valid.

## 6. Approximation count and inherited runtime

The whole-query backward induction in `WHOLE_QUERY_RESPONSE_SOURCE.md`
applies on the enlarged pole-safe domain: `||W^(ell)||_op<=C`,
`||w||_2<=CS sqrt(n)`, and bounded complex activation derivatives give
`||delta^(ell)(t,theta)||_2<=CS sqrt(n)`. Initialized matrix images
obey the same bound. Thus each coordinate of every required source is
bounded by `C sqrt(n)` on (2); a new polylogarithmic query-carrier
maximum is unnecessary.

At coordinate tolerance `epsilon=n^-1`, the approximation tail numerator
is `log(C sqrt(n)/epsilon)=O(ell_n)`. The time-strip tail is bounded by
`C sqrt(n)(T/r_n)exp(-c p r_n/T)` and the angular tail by a fixed
power of `r_n^-1` times `C sqrt(n)exp(-c J r_n)`. Their prefactors'
logarithms are `O(q_n)`. Hence (3)'s degrees follow from
`T/r_n=C lambda^-1 ell_n^(L/2+1)` and
`r_n^-1=C ell_n^(L/2)`.

There are a fixed number of whole-query families per layer. Their
coefficient count is at most `C(p+1)(2J+1)^(d-1)`, giving (3)'s `R`.
The exact initialized vectors add `O(m+d)`, absorbed by the existing
trace bound `m lambda<=B_phi^2`. Applying identical scalar interpolation
operations to each initialized matrix-image pair retains the exact
paired relation needed by the bridge.

The enlarged radius permits the same finite initialization-jet
preprocessing already used in the source theorem. Neither future trained
snapshots nor a residual history are supplied. The runtime bridge's
`O(R^2)` count then gives (4); its approximation input is still
`epsilon=n^-1`. Its real training-carrier estimate and stability proof
are unchanged, so its all-time error conclusion follows with its
existing dataset-dependent prefactor and width threshold.

## 7. Audited limits and route status

The first, simpler candidate is independently useful: with the original
`M_n=CS ell_n`, the actual first-layer caps are `CS ell_n` and
`C ell_n`. Induction gives `ell_n^ell`, not `ell_n^(ell+1)`, and
`r_n=c ell_n^-L` has a strict pole margin. For `L>=2`, its complex
correction `r_n ell_n` tends to zero. This already gives dimension
exponent `d(L+1)+1`, replacing `d(L+5)+1` without the extra maximum
stop. It is superseded here by the stronger square-root-log version.

The stronger route is a **candidate proof refinement**. Its remaining
independent reconstruction should focus on the exact transfer of the new
carrier-maximum stop through the inherited local insertion interface,
the cavity-measurable rectangular clamping used by the Gaussian grid,
and the order of the maximum, pole, response and budget improvements.
Those are the interfaces on which an apparent circular proof would
fail. The derivation above states how each is used; the original
prior-study proof and runtime implementation were not independently
available in this scoped assignment.

No assertion of depth-independent exponents is established. In (12),
the term `S M_n A_p` still multiplies a lower-layer coordinate cap by
`sqrt(ell_n)` at each layer. Eliminating that remaining depth loss would
require a stronger endpoint-trace estimate, for example suitable
empirical response moments replacing `A_p`; the assigned sources supply
such moments only for training carriers. A smaller arbitrary contour
step or ordinary piecewise time approximation does not remove this
factor: the latter trades degree for the number of pieces and retains
the order `(T/r_n) log(1/epsilon)`.

The powers in (4) are therefore sufficient powers for this construction,
not lower bounds on the storage needed by any autonomous representation.
They do not settle growing-depth, growing-dimension, growing-sample,
bounded-precision, or practical preprocessing questions.
