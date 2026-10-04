# Fixed-threshold route: what a cap does and does not establish

This is a scoped theoretical analysis of the current paper's two-hidden-layer,
order-one response closure. Inputs were the current `paper/main.tex` setting
and order-one equations, `paper/results.tex` all-time statement, and the shared
notation contract. No other study, experiment, or prior lower bound is used.

The principal target is an all-time, fixed-confidence
`O_P(n^{-1/2})` predictor error between the clipped finite system and its own
clipped population limit. Comparison with the original unclipped population is
a separate question. The threshold analysis below neither proves nor disproves
the principal rate. It does prove useful coefficient bounds, an exact
post-gate Lipschitz property, and the failure of a deterministic argument that
would infer lower-layer inactivity from upper-layer inactivity.

## Exact system and bounds

Write `g(z)=sech²(z)` and `C_M(u)=max(-M,min(M,u))`, coordinatewise. With
`u_a=Ax_a/sqrt(d)`, `h_a=tanh(u_a)`, `z_a=B h_a`, and `H_a=tanh(z_a)`, the
normalized order-one state is

\[
B=W_0+\frac1{mn}\sum_a v_a k_a^T,\qquad
f_a=\frac1n w^T H_a,\qquad r_a=f_a-y_a,\qquad
\rho=\left(\frac1m\sum_a r_a^2\right)^{1/2}.
\]

The recursive clipped responses and their updates are

\[
d_a=C_M(w\odot g(z_a)),\qquad
\ell_a=C_M(g(u_a)\odot B^T d_a),
\]
\[
\dot A=-\frac2m\sum_a r_a\ell_a x_a^T/\sqrt d,
\quad \dot w=-\frac2m\sum_a r_aH_a,
\quad \dot v_a=-2r_a d_a,
\quad \dot k_a=\frac\rho\tau(h_a-k_a),
\quad \dot\tau=\rho.
\]

Initialization is the canonical independent Gaussian `A_0,W_0`, with
`w=v_a=0`, `k_a=h_a(0)`, and `tau=1`. The sign and normalization of `v,k`
are obtained from the paper's raw moments by `v=-2 bar(delta)` and
`k=bar(h)/tau`.

Let `S(t)=integral_0^t rho(s) ds`, so `tau=1+S`. On every solution interval,

\[
\|w(t)\|_\infty\le2S(t),\quad
\|k_a(t)\|_\infty\le1,\quad
\|d_a(t)\|_\infty\le D_M(S(t)),\qquad D_M(s)=\min(M,2s).
\tag{1}
\]

Indeed, `m^{-1} sum_a |r_a| <= rho` and `|H_ai|<=1` bound the readout
velocity by `2rho`. Solving the key equation gives
`tau k_a=h_a(0)+integral rho h_a`, whose numerator is coordinatewise bounded
by `tau`. The response bound then uses `0<g<=1` and clipping contraction.
Consequently,

\[
\frac1m\sum_a\|v_a(t)\|_\infty
\le 2\int_0^{S(t)}D_M(s)\,ds\le 2S(t)^2.
\tag{2}
\]

The first inequality follows by integrating
`||dot v_a||_infty <= 2 |r_a| D_M(S)` and averaging in `a` before using
`m^{-1} sum |r_a|<=rho`. In particular, the rank-one Frobenius identity gives

\[
\|B(t)-W_0\|_F
\le\frac1m\sum_a
 \frac{\|v_a\|_2}{\sqrt n}\frac{\|k_a\|_2}{\sqrt n}
\le2S(t)^2.
\tag{3}
\]

The learned part of the lower carrier has the coordinate bound

\[
\|(B-W_0)^Td_b\|_\infty
\le 2D_M(S)\int_0^S D_M(s)\,ds
\le\min(2M^2S,4S^3).
\tag{4}
\]

For example, each summand in coordinate `j` is
`k_aj(v_a^T d_b)/(mn)`; apply `|k_aj|<=1`,
`|v_a^T d_b|/n<=||v_a||_infty D_M(S)`, and (2).
Equation (4) leaves the initial-matrix action `W_0^T d_b` entirely present.

Thus, **conditionally on a proved activity estimate** `S(infty)<=S_*`,
every `M>=2S_*` makes the top clip inactive for all coordinates and all time.
For example, a separately proved bound `rho(t)<=Y exp(-lambda t)` gives
the explicit threshold `M>=2Y/lambda`. This statement is deterministic on
the event where the activity estimate holds. It does not assert that the
lower clip is inactive.

## Why the post-gate clip helps a stability proof

The scalar map

\[
F_M(z,p)=C_M(g(z)p)
\]

obeys the exact global estimate

\[
|F_M(z,p)-F_M(\widetilde z,\widetilde p)|
\le |p-\widetilde p|+2M|z-\widetilde z|.
\tag{5}
\]

Clipping is 1-Lipschitz and `g<=1`, proving the first-variable-in-`p`
bound. For fixed finite `p`, the function of `z` is locally absolutely
continuous. Where the clip is unsaturated its derivative is `g'(z)p`, and

\[
|g'(z)p|=2|\tanh z|\,|g(z)p|\le2M.
\]

Where it is saturated its derivative is zero almost everywhere. Integrating
this derivative proves the `z` bound, including intervals crossing a
saturation boundary. This proof also covers `p=0` and `M=0`.

The estimate is special to clipping the product after the tanh gate (or to
other gates with an analogous bounded logarithmic derivative). It is not
obtained by declaring the unclipped carrier coordinate bounded. It supplies a
dimension-independent nonlinear stability constant, but does not by itself
quantify the Gaussian-reuse sampling error over continuous or infinite time.

## Canonical Gaussian lower tangent has unbounded support

Take one normalized datum `m=d=1`, `x=1`, and `y!=0`. Let
`a_i=A_{0,i}`, `h_i=tanh(a_i)`, `z=W_0h`, and

\[
\psi(z)=\tanh(z)g(z).
\]

For every fixed finite width and every `M>0`, all clips are locally the
identity at the initial state: both clipped inputs initially vanish and there
are finitely many coordinates. Differentiating at zero yields

\[
\dot w(0)=2y\tanh z,\qquad \dot d(0)=2y\psi(z),
\]
\[
\dot\ell_i(0)=2y g(a_i)[W_0^T\psi(W_0h)]_i,
\qquad
\ddot A_i(0)=4y^2g(a_i)[W_0^T\psi(W_0h)]_i.
\tag{6}
\]

These identities hold for the clipped and unclipped order-one systems.
The initial first-layer and hidden-matrix velocities vanish, so no missing
initial forward-velocity term occurs when differentiating the gates.

Here is a direct derivation of the limiting empirical law in (6), without
an imported Gaussian-reuse theorem. Set `q_n=||h||_2²/n` and let `P_h` be
orthogonal projection onto the orthogonal complement of `h`. Conditional on
`h`, the rows of `W_0` admit the Gaussian decomposition

\[
W_0=\frac{zh^T}{\|h\|_2^2}+R,
\]

where `z_i` are independent `N(0,q_n)`, and the rows of `R` are independent
`N(0,P_h/n)` and independent of `z`. Thus, conditionally on `h,z`,

\[
W_0^T\psi(z)\ \overset{law}=\ \alpha_nh+\sigma_nP_hG,
\quad
\alpha_n=\frac{n^{-1}\sum_i z_i\psi(z_i)}{q_n},\quad
\sigma_n^2=\frac1n\sum_i\psi(z_i)^2,
\tag{7}
\]

with `G` an independent standard Gaussian vector. The conditional variances
of the displayed empirical averages tend to zero: `psi` is bounded,
`z psi(z)` has uniformly bounded second moment when `q_n` is bounded, and
`q_n` converges in probability to

\[
q=\mathbb E\tanh^2(A)>0,\qquad A\sim N(0,1).
\]

Continuity of the corresponding Gaussian integrals then gives

\[
\alpha_n\longrightarrow\alpha
 =\frac{\mathbb E[Z_q\psi(Z_q)]}{q},\qquad
\sigma_n^2\longrightarrow\sigma^2
 =\mathbb E\psi(Z_q)^2>0,
\quad Z_q\sim N(0,q).
\]

The projection correction is negligible in empirical RMS, since conditional
on `h`,

\[
\frac1n\|(I-P_h)G\|_2^2
=\frac{(h^TG)^2}{n\|h\|_2^2}\ \overset{law}=\ \frac{G_0^2}{n}.
\]

Apply the ordinary independent-coordinate law of large numbers to `(a_i,G_i)`
and use the preceding RMS error to transfer bounded Lipschitz empirical tests.
The empirical law of `dot ell_i(0)` therefore converges in probability to

\[
\Xi=2y g(A)\{\alpha\tanh A+\sigma G\},
\qquad A,G\text{ independent }N(0,1).
\tag{8}
\]

Given every finite `A`, this is a Gaussian variable of strictly positive
variance because `y!=0`, `g(A)>0`, and `sigma>0`. It has positive mass outside
every finite interval. Its unconditional law is continuous, so weak empirical
convergence also gives, for each finite `R`,

\[
\frac1n\#\{i:|\dot\ell_i(0)|>R\}
\longrightarrow\mathbb P(|\Xi|>R)>0.
\tag{9}
\]

In particular, the maximum initial lower-response time derivative escapes
every fixed deterministic bound in probability. A positive cap preserves
nontrivial initial hidden learning, including the unbounded tangent law; it
does not replace the model by frozen features.

**Logical limit of this result.** An unbounded initial derivative does not
prove unbounded response coordinates at a fixed positive time. For example,
`M tanh(tG/M)` has an unbounded derivative at zero but is always bounded by
`M`. Consequently, (8) is not a proof that the actual population clipping
tail is nonzero at a specified time, nor a lower bound on clipping bias, nor
a counterexample to the principal width-rate question.

## A deterministic lower-activation example, with its probability limit stated

Even bounded matrix operator norm and arbitrarily short total activity cannot
give a universal deterministic inactive lower cap. The following construction
shows this while keeping the exact nonlinear order-one equations. It is not a
typical-Gaussian lower bound.

Fix `a,z_*,c,y>0`, let `h_*=tanh(a)`, and set the initial first weights to
`a_1=0`, `a_j=a` for `j>=2`. Let every row of `W_0` equal `b^T`, with

\[
b_1=\frac c{\sqrt n},\qquad
b_j=\frac{z_*}{(n-1)h_*}\quad(j\ge2).
\]

Then `W_0h=z_* 1` and

\[
\|W_0\|_{op}^2
=c^2+\frac{n z_*^2}{(n-1)h_*^2},
\]

uniformly bounded in `n`. By permutation symmetry every top coordinate,
readout coordinate, and value coordinate remains equal, and there are only
two first-layer coordinate types. At times `t=u/sqrt(n)`, uniformly on any
fixed finite interval of `u`, the clipped equations give

\[
w_i(t)=\frac{2y\tanh(z_*)u}{\sqrt n}+O(n^{-1}),\quad
d_i(t)=\frac{2y\psi(z_*)u}{\sqrt n}+O(n^{-1}),
\]
\[
A_1(t)=O(n^{-1/2}),\quad A_j(t)-a=O(n^{-1})\ (j\ge2),
\quad v_i(t)=O(n^{-1}),\quad z_i(t)-z_*=O(n^{-1}).
\tag{10}
\]

To verify these orders, bounded clipped first-layer velocity first bounds
`A_1(t)` by `O(t)`. The other lower carriers have size `O(d_i)` because
`n b_j=O(1)` for `j>=2`, giving their `O(t²)` displacement. The top readout
velocity is bounded; hence `w,d=O(t)` and `v=O(t²)`. The first-coordinate
contribution to `W_0 h(t)-W_0h(0)` is `O(t/sqrt(n))`; the sum of the other
contributions and the learned matrix contribution are `O(t²)`. These bounds
close a short-time bootstrap with constants uniform for bounded `u`.
Substitution into the readout equation yields its displayed leading term,
and then the leading term for `d`. The top clip is inactive for sufficiently
large `n` because `M` is fixed and positive.

The unclipped input to the *lower* clip at coordinate one is therefore

\[
g(A_1(t))[B(t)^Td(t)]_1
=2cy\psi(z_*)u+O(n^{-1/2}).
\tag{11}
\]

For any fixed positive `M`, choose
`u>M/(2cy psi(z_*))`. Then (11) exceeds `M` for all sufficiently large `n`,
while `S(t)=O(n^{-1/2})`. The lower cap activates despite bounded initial
operator norm and vanishing elapsed activity. This is a genuine activation
statement, unlike merely inspecting the initial tangent.

The canonical Gaussian initialization has positive density on every finite
Euclidean neighborhood of these finite-dimensional initial states. Continuous
dependence of the clipped ODE, using (5), makes strict activation persist in
a sufficiently small neighborhood. Thus activation has positive probability
at each such finite width. **No width-uniform lower bound on that probability
is proved**; the neighborhoods may be extremely improbable. The construction
therefore rules out an all-realizations deterministic inactivity argument,
not a high-probability inactive-cap theorem for Gaussian initialization.

## Target and confidence distinctions

If a population comparison for fixed `M` were established, its triangle
decomposition would be

\[
\|f_n^M-f^\infty\|
\le\|f_n^M-f_\infty^M\|+\|f_\infty^M-f^\infty\|.
\]

The first term is the requested sampling/width problem. The second is a
possible deterministic clipping bias relative to an unclipped target. For
fixed `M`, a proved positive second term would obstruct convergence to that
unclipped target; it would say nothing against a root-width rate for the first
term. The present route establishes neither positivity nor vanishing of this
population bias. It also does not turn the paper's dense-population order
error into a width rate for a fixed order-one clipped population.

Here `E_n=O_P(n^{-1/2})` means that for each fixed confidence loss `delta>0`
there are finite `C_delta` and `N_delta` with

\[
\mathbb P\{E_n>C_\delta/\sqrt n\}\le\delta\qquad(n\ge N_\delta).
\]

It is not the stronger claim that one finite `C` gives probability tending
to one. A nondegenerate Gaussian limit for `sqrt(n) E_n` would be compatible
with the former and incompatible with the latter. Confidence factors such as
`sqrt(log(1/delta))` are compatible with root-width scaling at fixed confidence.

Finally, `M=0` makes `d=ell=v=0` and freezes both hidden layers. This is an
exact easier model and is not a witness for the intended positive-threshold
feature-learning claim. The identities (6) show the distinction for every
positive `M` without assuming an all-time rate.

## Conclusion of this bounded route

Proved: top inactivity from total activity, bounded learned lower-carrier
correction, post-gate joint Lipschitz continuity, the canonical unbounded
initial lower-tangent law, and an exact deterministic example of lower-cap
activation with bounded operator norm and arbitrarily short activity.

Open here: a unique clipped population construction with the required
all-time quantitative Gaussian-reuse estimate, the proposed root-width
predictor rate, and any nonzero population bias at fixed positive `M`.
The decisive remaining input is a quantitative sampling/source estimate;
the threshold and stability bounds alone cannot supply it.

## Subsequent internal cross-check exposure

After freezing the independent threshold analysis above, the coordinator
explicitly authorized reading the complete same-study
`FITTING_AND_THRESHOLD.md`. I checked its exact constants
`D=K_0+2`, `C_h=8+4X²D²`,
`s_*=min(1,sqrt(lambda/(4C_h)))`, and `Y<=lambda s_*/2`.
The displayed bounds imply
`dot rho<=(-2lambda+4C_h S²)rho<=-lambda rho` before the stop,
and `S<=Y/lambda<=s_*/2` excludes that stop. Its `8S rho` bound on
`||dot B||_F`, the convergence of every finite-width state block, and the
inactive top threshold `2Y/lambda` are valid as written. In particular,
`M=1` makes the top clip inactive because `2Y/lambda<=s_*<=1`.
No correction was required. This is an internal cross-check after exposure,
not an independent promotion review or a proof of the width rate.
