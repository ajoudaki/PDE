# Asymmetric endpoint traces remove depth from the logarithmic exponent

2026-10-04. Post-exchange **internally checked proof refinement**. This is
not an independent promotion review or established-book result.
No experiment, Git mutation or manuscript edit was performed.

The complete reconstruction in DEPTH_INDEPENDENT_EXPONENT_CHECK.md passed
at report SHA-256
`1a4270394c39740b8d0eb65bad7adee47ca4e45056f3116830a69c27b6fe82bd`.
It checked the frozen derivation at SHA-256
`5da4e4593a040c82a8b12b2c63dea334cf65a3d4dd7e1dc0d48921102adf2932`.
The coordinator read the complete derivation and check and separately
reconstructed the endpoint norms and interpolation. The dated status
update preserves the proof below; its candidate-stage wording records
the frozen submission. The named prior lemmas remain inherited internal
research inputs, not independently promoted theorems.

The independent first candidate remains frozen in
`DEPTH_EXPONENT_ROUTE.md`, SHA-256
`e95e6875478cacc80fd62ae57cdcfff8e8e173570ba78f5057abec8e519bf2c6`.
It sharpened the common radius to `log(en)^(-L/2)`. After that freeze,
the coordinator proposed the asymmetric Schatten estimate in Section 3.
This note reconstructs its endpoint bounds and consequences. The
derivative interpolation in Section 5 was then developed and exchanged;
the coordinator independently checked its exponent calculation.
No other route finding was used.

The complete assigned sources are `DEEP_COMPLEX_SOURCE.md`,
`DEEP_ACTIVATION_EXTENSION.md`, `DATASET_SOURCE_CONSTANTS.md`,
`LABEL_SEPARATE_BUDGETS.md`, `WHOLE_QUERY_RESPONSE_SOURCE.md` and
`SAMPLE_COUNT_REFINEMENT.md`. Prior-study insertion proofs and the
separate quadratic-runtime proof were outside this scope and were not
read. The local insertion and runtime theorems explicitly stated in the
assigned sources remain inherited inputs, rather than new independent
proofs in this note.

## 1. Precise improvement and unchanged reference

Fix input dimension `d>=2`, hidden depth `L>=2` and sample count `m`.
Use the canonical Gaussian width-`n` network at every hidden layer,
zero initial readout, loss `m^-1 sum_a(f_a-y_a)^2` and mobilities
`(n,1,...,1,n)`. For `v=x/sqrt(d)` on the unit sphere, the forward pass is

\[
z^{(1)}(v)=Av,\quad z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),
\quad h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\quad
f(v)=w^\top h^{(L)}(v)/n.
\tag{1}
\]

The middle recurrence is for `ell>=2`. Entries of `A(0)` are independent
`N(0,1)`, entries of hidden `W(0)` are independent `N(0,1/n)`, and all
blocks are independent. The activations are real on the real axis and
bounded and holomorphic on one fixed horizontal strip. Define

\[
r_a=f(v_a)-y_a,\quad k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
\quad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Training in physical time is exactly

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad \dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
\quad \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{2}
\]

Let `Q^(0)_{ab}=v_a^T v_b` and
`Q^(ell)_{ab}=E[phi_ell(Z_a)phi_ell(Z_b)]` for
`Z~N(0,Q^(ell-1))`. Set

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\quad
\lambda=\min(1,\gamma/m),\quad
Y=\|y\|_2/\sqrt m,\quad S=C_0Y/\lambda,\quad
\ell_n=\log(en),\quad q_n=\ell_n+\log(e/\lambda).
\]

Keep `0<Y<=c lambda`, equivalent to the requested `Y<=c gamma/m`
when the gap cap is inactive. Fixed structural factors relating these
conventions can be absorbed in `c` for bounded activations. Constants
below depend on fixed `d,L` and activation-strip bounds; depth is
removed only from the power of `log n`, not from those constants.
Zero labels give the separate stationary zero prediction.

**Conclusion.** On the refined high-probability event proved below,
the joint complex domain can use

\[
                   r_n=c\ell_n^{-1/2},\qquad
                   T=C\lambda^{-1}\ell_n,                \tag{3}
\]

for both time and every sphere angle. Thus the actual source families

\[
h^{(\ell)}(t,\theta),\quad W_0^{(\ell)}h^{(\ell-1)}(t,\theta),
\quad\delta^{(\ell)}(t,\theta),\quad
W_0^{(\ell+1)\top}\delta^{(\ell+1)}(t,\theta)
\tag{4}
\]

are jointly holomorphic near the closed time rectangle
`-r_n<=Re t<=T+r_n`, `|Im t|<=r_n`, and product strip
`|Im theta_j|<=r_n`. Here the backward fields in (4) are evaluated at
each passive query using the same current parameters; they do not add
new forces to (2). Each coordinate is bounded by `C sqrt(n)`.

At coordinate tolerance `n^-1`, the time degree, degree in each angle,
and layer-space dimension can consequently be chosen as

\[
p\le C\lambda^{-1}\ell_n^{3/2}q_n,\qquad
J\le C\ell_n^{1/2}q_n,\qquad
R\le C\lambda^{-1}\ell_n^{(d+2)/2}q_n^d.
\tag{5}
\]

The inherited quadratic runtime then has total retained size

\[
\mathrm{size}\le
C\lambda^{-2}\ell_n^{d+2}q_n^{2d}+Cm(d+1)
\le C\lambda^{-2}\ell_n^{3d+2}+Cm(d+1),                 \tag{6}
\]

where the last bound uses `log(e/lambda)<=ell_n`. In uncapped notation
the leading prefactor is `C m^2/gamma^2`. The old exponent was
`2d(L+5)+2`; the first candidate gave `dL+2d+2`; (6) gives `3d+2`.
For `d=L=2` these are respectively `30`, `10` and `8`.

All constants, probability quantifiers and label assumptions have the
same fixed-dataset meaning as before. The source refit leaves the
reference (1)--(2), the reduced autonomous optimizer, its own-residual
identity, initialization-only preprocessing, physical clock and all-time
whole-sphere `C_data/sqrt(n)` error conclusion unchanged. Its error
prefactor is still the previously derived one; no improvement to that
prefactor is claimed here.

## 2. Endpoint Hilbert--Schmidt bounds do not hide coordinate maxima

For a vector `u`, write
`||u||_{p,n}=(n^-1 sum_i |u_i|^p)^(1/p)`. For a matrix or rectangular
map `M`, write `||M||_{p,n}=n^(-1/p)||M||_{S_p}`, using singular values.
In particular `||M||_{2,n}=||M||_F/sqrt(n)`. Matrix transposes in the
analytic equations are algebraic; these norm estimates use the usual
complex norms.

In mobility coordinates
`Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)` and with `F_b=nf(v_b)`,
define the forward response and angular derivative by

\[
R_b^{(p)}=D_\Theta z^{(p)}(v)\nabla_\Theta F_b,\quad
Q_b^{(p)}=D_\Theta h^{(p)}(v)\nabla_\Theta F_b,
\quad J_j^{(p)}=\partial_{\theta_j}z^{(p)}(v).
\tag{7}
\]

On a pole-safe physical tube, bounded complex gates and bounded hidden
operator norms give

\[
\|D_\Theta z^{(p)}\|_{\rm op}
+\|D_\Theta h^{(p)}\|_{\rm op}\le C,\qquad
\|R_b^{(p)}\|_{2,n}+\|Q_b^{(p)}\|_{2,n}\le CS,
\quad\|J_j^{(p)}\|_{2,n}\le C.                          \tag{8}
\]

These are the RMS and operator bounds already established in the source;
they use neither a coordinate response cap nor a pole-free parameter
segment outside the stopped tube.

The inherited Hessian decomposition expresses `D_Theta^2 F_b` as a
fixed number of bounded-map contractions of single carrier diagonals,
plus bounded-operator terms of rank `O(n)`. Carrier RMS is `CS`, so

\[
                         \|D_\Theta^2F_b\|_{2,n}\le C.  \tag{9}
\]

This also follows immediately from the explicit bounds (6) in
`LABEL_SEPARATE_BUDGETS.md`; it is not an operator-norm bound.

To verify the endpoint `D_Theta Q_b^(p)`, differentiate its defining
formula exactly:

\[
D_\Theta Q_b^{(p)}
=D_\Theta h^{(p)}D_\Theta^2F_b
 +D_\Theta^2h^{(p)}[\,\cdot\,,\nabla_\Theta F_b].        \tag{10}
\]

The first term has bounded normalized Hilbert--Schmidt norm by (8)--(9).
For the second, hold `V=grad F_b` fixed while differentiating the
forward pass. The scalar gate produces

\[
\operatorname{diag}(\phi_p''(z^{(p)})\odot R_b^{(p)})
                       D_\Theta z^{(p)}.
\]

Its Hilbert--Schmidt norm divided by `sqrt(n)` is at most
`C||R_b^(p)||_{2,n}<=CS`, since right multiplication by a bounded
operator preserves that norm bound. No coordinate maximum is used.
At each hidden matrix, the mixed terms are the maps

\[
U\longmapsto U_{H^{(p)}}Q_b^{(p-1)}/\sqrt n,
\qquad
U\longmapsto
\frac{\delta_b^{(p)}h_b^{(p-1)\top}}n
                          D_\Theta h^{(p-1)}[U],
\tag{11}
\]

plus the previously computed lower mixed derivative multiplied by
`W^(p)`. The first map has squared Hilbert--Schmidt norm exactly
`||Q_b^(p-1)||_2^2` for a width-`n` output: sum its images of the
matrix-coordinate basis. Its normalized norm is at most `CS` by (8).
The second is a bounded operator of rank at most one, using backward
and feature RMS bounds. The inherited lower mixed term is propagated
by a bounded operator. At the first layer `D^2 z^(1)=0`.
Finite induction proves

\[
                      \|D_\Theta Q_b^{(p)}\|_{2,n}\le C. \tag{12}
\]

For an angular source `q=partial_theta h^(p)`, the endpoint derivative
has the same graph with `R_b` replaced by `J_j`. Its diagonal term is
`diag(phi'' J_j)D_Theta z`, bounded by the angular RMS in (8).
The mixed hidden map is
`U_H partial_theta h^(p-1)/sqrt(n)`, with the same Hilbert--Schmidt
identity as (11). The first-layer mixed map is
`U_A partial_theta v`; its squared Hilbert--Schmidt norm is
`n||partial_theta v||_2^2=O(n)`. Induction gives

\[
                           \|D_\Theta q\|_{2,n}\le C.   \tag{13}
\]

All constants in (12)--(13) are independent of the lower-layer coordinate
cap `A_p`. Those caps are still allowed in operator estimates for the
local insertion event, but they are unnecessary in these endpoint norms.

## 3. Asymmetric Hölder in the same-root endpoint trace

The source's only trace term responsible for the depth-dependent cap is

\[
\frac1n\operatorname{tr}
 \{D_\Theta q(t)\,\mathcal J(t,s)\,C_a(s)^\top\},
\quad C_a=D_\Theta h_a^{(p)},                            \tag{14}
\]

where `q` is either `Q_b^(p)` or an angular source, and
`mathcal J` is the cavity variational propagator. The forward derivative
endpoint satisfies `||C_a||_op<=C`, `rank C_a<=n`, and hence
`||C_a||_{2,n}<=C`.

Expand the propagator in residual-Hessian insertions around the source's
negative-Gram base propagator. Along the positive real contour the base
is contractive. The total short vertical and negative-real lengths are
`O(r_n)`, so all intervening base factors together cost at most
`exp(Cr_n)<=C`. This product bound is used once per term, not once per
insertion.

Under the separate sample budget `H_a<=2B`, normalized carrier moments
give, for every real `u>=2`,

\[
\|\mathcal A(s)\|_{u,n}
       \le C[1+Su(2B)^{1/u}],                           \tag{15}
\]

where `mathcal A` is the residual-weighted Hessian normalized by the
absolute residual activity. Triangle inequality proves (15) even when
the Hessian sample index changes from factor to factor. Total contour
activity is `CS`.

For a term with `h>=1` Hessian insertions, apply Schatten Hölder with
exponent `2` to `D_Theta q`, exponent infinity to `C_a`, and exponent
`2h` to each of the `h` Hessians. The reciprocal exponents sum to
`1/2+h/(2h)=1`. All base factors use their operator norm. Normalizing
each finite Schatten norm by `n^(-1/u)` yields precisely the required
`1/n` normalization; the ambient parameter dimension may be `O(n^2)`
without changing this identity. Equations (12)--(15) therefore bound
the integrated term by

\[
\frac{C(CS)^h}{h!}
       [1+2CS h(2B)^{1/(2h)}]^h.                        \tag{16}
\]

The `h=0` term is bounded using both endpoint Hilbert--Schmidt norms
and the bounded base propagator; using an operator norm alone for its
second endpoint would not prove a trace bound.

To check summability of (16), split `(a+b)^h<=2^(h-1)(a^h+b^h)`.
The resulting sum is bounded by a constant times

\[
\sum_{h\ge1}\frac{(CS)^h}{h!}
+\sqrt{2B}\sum_{h\ge1}(CS^2)^h\frac{h^h}{h!}.           \tag{17}
\]

Since `h!>=(h/e)^h`, the second series is geometric for sufficiently
small structural `S`. Its value is at most
`C sqrt(B) S^2/(1-CS^2)`, bounded under the existing `S^2B<=c`
condition. Thus (14) is bounded by a structural constant independent of
`A_p`. There is no factor `(1+A_p)`.

The same-root insertion term outside (14) is an integral of
`r_a(s)b_a(s)`, with normalized total residual activity `CS` and
`|b_a|<=CM_n`. Its bound improves from
`CS M_n(1+A_p)` to `CS M_n`. The other direct trace, learned-row,
Gaussian and insertion-error terms in the original equations
(25)--(26) remain unchanged.

## 4. Stopped maximum and response caps close without a depth power

Retain the individual carrier budgets

\[
\mathcal H_a=\frac1n\sum_{\ell<L,i}
 \exp\left\{\frac{\eta_0}{S}\sup_t|k_{a,i}^{(\ell)}(t)|\right\}
                   \le B,                              \tag{18}
\]

where the supremum is over the current stopped complex rectangle. Add
the carrier maximum stop `max|k|<=M_n=C_*S sqrt(ell_n)` and forward
and angular stops of sizes `C_ell S sqrt(ell_n)` and
`C_ell sqrt(ell_n)`. Every cavity has its own doubled budgets and caps;
all references are functions of its retained initialization only.

The maximum-stop argument in the independently frozen first candidate
uses only the existing insertion interface. Explicitly, its singleton
shift is

\[
|k_{a,i}^{(j)}(t)-x_i^\top\delta_a^{(j+1),-i}(t)|
                     \le CS(1+S^2B)+o(1).               \tag{19}
\]

The reference RMS is `CS`. Its stopped derivative has a fixed
polynomial-logarithmic bound even under the original coarse carrier
maximum. Freeze or clamp on its own stopped rectangle. Conditional
Gaussian tails on a mesh of spacing `n^-2`, and off-grid interpolation
using that derivative bound and `||x_i||_2<=C`, give

\[
\sup_{a,j,i,t}|x_i^\top\delta_a^{(j+1),-i}(t)|
                         \le C_G S\sqrt{\ell_n}.        \tag{20}
\]

The mesh cardinality is a fixed power of `n` for all sufficiently large
width, and a sufficiently large Gaussian tail multiplier dominates it.
This argument does not use a bounded Gaussian supremum moment, does not
use empirical-budget removal, and never conditions roots on full
survival. Choose `C_*` with a fixed margin above `C_G` and the shift
constant in (19); this strictly improves the carrier maximum stop.

For every fixed-size cavity, the coordinate-small insertion comparison
transfers the full prefix to its doubled pole, response, carrier-maximum
and separate budget stops. In particular
`H_a^{-I}<=exp(o(1)/S)H_a+O(|I|/n)<2B`.
All inserted controls remain polylogarithmically bounded. The strict
powers of `n` in the enlarged Gaussian insertion event and nonlinear
graph remainders are unchanged. Later fixed-block moment degrees do
not require new Gaussian-maximum constants: those cavities have their
own doubled maximum stops and survive by this transfer.

With the trace factor corrected by Section 3, the response estimates are

\[
\max|R_b^{(p+1)}|
 \le C\{M_n+S\sqrt{\ell_n}+SM_n+S^2M_n\}+o(1),
\]
\[
\max|J_j^{(p+1)}|
 \le C\{\sqrt{\ell_n}+SM_n\}+o(1).                     \tag{21}
\]

They imply at every fixed depth

\[
\max|R_b^{(\ell)}|\le C_\ell S\sqrt{\ell_n},\qquad
\max|J_j^{(\ell)}|\le C_\ell\sqrt{\ell_n}.               \tag{22}
\]

The first-layer response follows from
`R_b^(1)=delta_b^(1)v_b^T v`. The first-layer angular bound follows
from initialized Gaussian row norms and the bound `CS M_n` on each
first-weight row increment. Choosing the layer constants successively
gives strict improvements of all response stops. The trace calculation
never requires the value of a next-layer response to bound its own cap.

For a complex query, move from its real time and real angle vertically
in time and then in the angles. Equation (2), (22), and normalized
residual averaging bound the imaginary preactivation by

\[
C r_n SY\sqrt{\ell_n}+C_d r_n\sqrt{\ell_n}
                         \le Cc(1+SY).                  \tag{23}
\]

Choosing the structural multiplier `c` in (3) sufficiently small makes
(23) less than half the pole margin. A fixed strict margin suffices.
These estimates are taken on stopped prefixes and use lower query gates
before excluding the possible next query pole, as in the existing
augmented insertion proof.

## 5. Carrier moments sharpen the complex-time derivative

The original coarse derivative bound
`||dot delta_a||_{2,n}<=C rho(1+SM_n)` would give a complex correction
of constant size at radius (3), with an unwanted growing Gaussian
entropy factor. This is repaired by interpolation, without a new
probabilistic moment theorem.

Here `rho(t)=||r(t)||_2/sqrt(m)`. On the stopped complex domain, (2),
bounded physical operators, (8), and (22) give

\[
\|\dot z_a^{(\ell)}\|_{2,n}\le C\rho S,\qquad
\|\dot z_a^{(\ell)}\|_\infty\le C\rho S\sqrt{\ell_n}.
\tag{24}
\]

The first estimate can also be obtained by differentiating the forward
pass: `||dot A||_F/sqrt(n)<=C rho S`,
`||dot W^(ell)||_op<=C rho S`, and bounded gates propagate these
normalized RMS bounds. The second uses the exact identity
`dot z=-(2/m)sum_b r_b R_b` and
`m^-1 sum_b|r_b|<=rho`.

For any real `u>=4`, (18) implies the deterministic moment estimate

\[
                  \|k_a^{(\ell)}\|_{u,n}
                         \le CSu(2B)^{1/u}.             \tag{25}
\]

Indeed `x^u<=(u/e)^u exp(x)` applied to `eta_0|k|/S` proves it.
Let `v=2u/(u-2)`, so `1/u+1/v=1/2`. Interpolating the two bounds
in (24), using
`||b||_{v,n}<=||b||_infty^(1-2/v)||b||_{2,n}^(2/v)`, gives

\[
\|\dot z_a^{(\ell)}\|_{v,n}
                    \le C\rho S\ell_n^{1/u}.
\]

Hölder in the normalized counting measure therefore yields

\[
\|k_a^{(\ell)}\odot\dot z_a^{(\ell)}\|_{2,n}
              \le C\rho S^2u(2B\ell_n)^{1/u}.           \tag{26}
\]

Choose `u=max(4,log(2B ell_n))`. Then the last exponential factor is
bounded. Since `B` is fixed and structural, enlarging the width threshold
gives

\[
\|k_a^{(\ell)}\odot\dot z_a^{(\ell)}\|_{2,n}
                    \le C\rho S^2\log(e+\ell_n).        \tag{27}
\]

This use of a growing real exponent is purely a deterministic consequence
of a stopped exponential budget. It is not a growing-deletion estimate
and does not change the fixed-moment order of limits later.

Differentiate the actual backward recursion:

\[
\dot\delta_a^{(\ell)}
=\phi_\ell''(z_a^{(\ell)})\odot\dot z_a^{(\ell)}
                              \odot k_a^{(\ell)}
 +\phi_\ell'(z_a^{(\ell)})\odot\dot k_a^{(\ell)},
\]
\[
\dot k_a^{(\ell)}
=\dot W^{(\ell+1)\top}\delta_a^{(\ell+1)}
 +W^{(\ell+1)\top}\dot\delta_a^{(\ell+1)},\qquad
\dot k_a^{(L)}=\dot w.                                 \tag{28}
\]

The first term in the second line has normalized RMS at most
`C rho S^2`, using `||dot W||_op<=C rho S` and
`||delta||_{2,n}<=CS`. The terminal bound is
`||dot w||_{2,n}<=C rho`. Use (27), bounded gate derivatives and
bounded mixer operators in downward induction through (28). This gives

\[
\max_{a,\ell}\|\dot\delta_a^{(\ell)}(t)\|_{2,n}
             \le C\rho(t)[1+S^2\log(e+\ell_n)].         \tag{29}
\]

## 6. Complex Gaussian moments and budget removal

On the short vertical contour, the normalized residual Gram has bounded
operator norm, so the inherited real decay gives
`rho(t+is)<=CY exp(-kappa max(t,0))`, with `kappa~lambda`.
For `z=t+is` set `t_+=max(t,0)` and anchor the real reference at `t_+`.
If `t<0`, first traverse the short negative-real segment from zero to
`t`, then the vertical segment; their combined length is at most `2r_n`.
Thus the real reference always belongs to the existing nonnegative-time
Gaussian theorem. Using `Y/S<=C lambda<=C`, integration of (29) gives
the normalized complex correction radius

\[
\frac{\|\delta_a(t+is)-\delta_a(t_+)\|_2}{S\sqrt n}
 \le Cr_n[1+S^2\log(e+\ell_n)]
 \le D_n:=C\ell_n^{-1/2}\log(e+\ell_n).                 \tag{30}
\]

The two real parameter Lipschitz constants of the bracket are at most
`C log(e+ell_n)` after the same normalization; for the horizontal
derivative one may bound the difference by the sum of the two endpoint
derivative norms where `t>0`, and by the single complex endpoint bound
where `t<0`. Continuity at zero gives the same Lipschitz bound across
the join. Cavity-measurable clamping preserves a fixed multiple
of this bound. The covering number at normalized Gaussian resolution
`epsilon` is therefore at most
`(C lambda^-1 ell_n^C/epsilon)^2`.

For an omitted `N(0,I/n)` root divided by `S`, the correction process
has Gaussian radius `CD_n`. A dyadic net gives mean supremum at most

\[
C D_n\sqrt{\log(C\lambda^{-1}\ell_n^C/D_n)}
 \le C\ell_n^{-1/2}[\log(e+\ell_n)]^{3/2}+o(1)
                              \longrightarrow0          \tag{31}
\]

for fixed positive `lambda`, and tail scale `CD_n`. To see the bound,
at net level `k` sum Gaussian increments of standard deviation
`CD_n 2^-k`; their log cardinality is at most
`C[log(C lambda^-1 ell_n^C/D_n)+k]`. Gaussian tail union bounds and
`sum_k 2^-k sqrt(k)<infinity` give (31) and the stated tail.
Every fixed exponential moment of the correction supremum tends to one.

Combine it by Cauchy--Schwarz with the unchanged real single-sample
Gaussian reference moment. The separate-budget proof then has its same
structural complex moment bound, without taking a maximum over samples
inside that moment. The singleton shift, common-cavity comparison and
fixed-block moment expansion are unchanged. For every fixed integer
moment degree `p`, they give the limiting hit probability bound
`m vartheta^p`, with structural `vartheta<1`. Taking the width limit
first and then the infimum over fixed `p` removes all carrier-budget
stops under the original `S<=c` condition, equivalently `Y<=c lambda`.

The logical dependencies are thus noncircular. Budgets and maximum,
response and pole caps are imposed together. Local insertion transfers
them to doubled cavity caps. The polynomial Gaussian grid and singleton
shift improve the maximum cap without using a supremum moment.
Asymmetric endpoint traces improve response caps; their coordinate
bounds exclude poles and give (24). The still-stopped exponential
budgets yield (25)--(29), which prove the complex Gaussian moment needed
to remove those budgets last. Holomorphic continuation then reaches (3).

## 7. Source approximation and exact scope of the result

On the resulting domain, the whole-query backward recursion has bounded
gates and hidden operator norms. Its RMS is at most `CS`, so its
coordinate maximum is at most `CS sqrt(n)`. Forward features and both
initialized mixer orientations have the same sufficient coordinate
bound `C sqrt(n)`. This is precisely the deduction in
`WHOLE_QUERY_RESPONSE_SOURCE.md`, now using (3).

The logarithm of that magnitude divided by tolerance `n^-1` is
`O(ell_n)`. Time approximation requires degree a constant times
`(T/r_n)q_n`; angle approximation requires a constant times `r_n^-1 q_n`.
Since `T/r_n=C lambda^-1 ell_n^(3/2)`, these are (5).
The coefficient count for each family is
`(p+1)(2J+1)^(d-1)`, giving its stated `R`. There are a fixed number of
whole-query families per layer. Exact initialization vectors add
`O(m+d)`, absorbed as before by `m lambda<=B_phi^2`.

Identical scalar coefficient operations preserve every initialized
matrix-image pair. The existing finite initial-jet continuation procedure
can compute the required coefficient approximations from initialization
and labels. No trained trajectory enters preprocessing. The inherited
quadratic runtime therefore receives exactly its former approximation
and pairing hypotheses at smaller `R`, and its state count gives (6).

This candidate does not establish optimal powers in dimension, efficient
preprocessing, bounded-precision stability, or a growing-depth theorem.
Its originally requested independent audit was specifically the adaptation of the
inherited local stopped-domain insertion interfaces to the enlarged
radius and additional maximum stop, followed by the trace and derivative
arguments above. The complete check linked at the beginning now verifies
that implication from the inherited interfaces. No experiment or formal
machine proof was performed.
