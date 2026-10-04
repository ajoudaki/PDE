# Scalar aggregate route: exact cross-Gram dynamics and a nonlinear fiber obstruction

Frozen independent route, 2026-09-30. Author: scoped agent
`/root/scalar_aggregate`. No other route or study was read. This is theoretical
research, not a promotion candidate. The formulas and counterexamples below are
proved by direct finite-dimensional differentiation; they have received the
author's algebraic check, not independent review. No training experiment ran.

## Scope and outcome

The target is the README's actual two-hidden-layer tanh q=1 dynamics, with
correlated finite data, moving features, fixed Gaussian mixer and its true
transpose. The desired final result remains an autonomous, restartable scalar
approximation of loss with moving state `S(epsilon)=o(epsilon^-2)`, ideally at
all equal physical times. This route supplies neither that approximation nor
an impossibility theorem for it.

It supplies three concrete results useful before attempting such a closure:

1. An exact low-order residual/loss equation, separating a positive Gram
   contribution from two signed memory contributions. Positive semidefiniteness
   of the whole residual generator is not an identity of q=1.
2. A scalar, Gram-computable dissipation certificate which retains the actual
   memory contributions instead of removing them by projection.
3. A counterexample to autonomous closure using pairwise Grams of the listed
   lower fields `(h,k,ell)` and upper fields `(g,d,v,w)`, even augmented by
   arbitrary compatible linear words in the fixed mixer and its
   transpose. Two states with the same source and the same such aggregates
   have different loss third derivatives. The missing source is explicitly a
   fourth/sixth coordinate moment, not an unexplained abstract remainder.

The counterexamples concern valid *current states* of the q=1 vector field.
They are not asserted reachable from the README's zero-readout Gaussian
initialization. Therefore they reject a universal Gram identity, not a
reachable-state approximation theorem or a population limit. Establishing a
small missing-moment error on that initialized reachable set is the decisive
unresolved step.

Inputs read: study README in full; `paper/main.tex` lines 179--383, containing
the setting and complete learning-speed-clock reconstruction; current
AGENTS/RESEARCH_WORKFLOW; investigate-conjectures and solve-math-rigorously
skills and applicable contract/audit/orchestration references. No external
scientific theorem is used. Manuscript SHA256:
`fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605`.
README snapshot SHA256:
`f3f9cf90b8cb7cd19e714ed3055753fd792a9833554b70e3f03af7692cdf2f14`.

## 1. Exact aggregate identities

All vector inner products below are normalized by width:
`<p,q> = p^T q/n`. For operators, write
`p tensor q = p q^T/n`. For a sum of these normalized rank-one operators use
the ordinary Frobenius Hilbert norm, so that

\[
 \langle p\otimes q,u\otimes z\rangle_{\rm HS}
 =\langle p,u\rangle\langle q,z\rangle.
\]

This convention gives the same operator action as the README. Set

\[
 C_{ab}=x_a^Tx_b/d,\quad s_a=1-h_a^2,\quad j_a=1-g_a^2,
 \quad d_a=w\odot j_a,\quad \ell_a=s_a\odot B^Td_a.
\]

The squares and products inside vectors are coordinatewise. Retain the scalar
arrays

\[
\begin{aligned}
 H_{ab}&=\langle h_a,h_b\rangle,&
 K_{ab}&=\langle k_a,h_b\rangle,&
 G_{ab}&=\langle g_a,g_b\rangle,\\
 D_{ab}&=\langle d_a,d_b\rangle,&
 E_{ab}&=\langle\ell_a,\ell_b\rangle,&
 V_{ab}&=\langle d_a,v_b\rangle.
\end{aligned}
\]

In particular `K` and `V` are cross-Grams, not symmetric Gram matrices. Direct
differentiation of the q=1 reconstruction gives

\[
 \dot B=-\frac2m\sum_b r_b d_b\otimes k_b
       +\frac{\rho}{m\tau}\sum_b v_b\otimes(h_b-k_b),
 \qquad
 \dot h_a=-\frac2m\sum_b r_b C_{ab}s_a\odot\ell_b.
 \tag{1}
\]

For `z_a=B h_a`,

\[
 \dot z_a=-\frac2m\sum_b r_b d_bK_{ba}
 +\frac{\rho}{m\tau}\sum_b v_b(H_{ba}-K_{ba})+B\dot h_a.
 \tag{2}
\]

Since `f_a=<w,g_a>`, the last term contracts with `d_a`, and

\[
 \langle d_a,B(s_a\odot\ell_b)\rangle
 =\langle\ell_a,\ell_b\rangle.
\]

The equality uses the *same* `B^T` as in backpropagation. Thus

\[
 \boxed{\dot r_a=-\frac2m\sum_b r_b
  \{G_{ab}+C_{ab}E_{ab}+D_{ab}K_{ba}\}
  +\frac{\rho}{m\tau}\sum_bV_{ab}(H_{ba}-K_{ba}).}
 \tag{3}
\]

This exact equation already contains only `O(m^2)` scalar coefficients, but
their evolution is not closed. Replacing them by an evaluator that accesses
all neurons would not provide the requested scalar compression.

For example, put

\[
 T_{abc}=\langle s_a\odot\ell_c,h_b\rangle,
 \qquad U_{abc}=\langle k_a,s_b\odot\ell_c\rangle.
\]

Then two low-order equations are

\[
\begin{aligned}
 \dot H_{ab}
 &=-\frac2m\sum_c r_c(C_{ac}T_{abc}+C_{bc}T_{bac}),\\
 \dot K_{ab}
 &=\frac\rho\tau(H_{ab}-K_{ab})
   -\frac2m\sum_c r_c C_{bc}U_{abc}.
\end{aligned}
 \tag{4}
\]

`T` and `U` are not ordinary pairwise Grams of the displayed current fields:
they contain the coordinate multiplier `1-h^2`. The obstruction in Section 4
makes this issue quantitative at the loss level.

## 2. A realizable scalar dissipation certificate

Let `q_a=h_a-k_a` and introduce three finite-rank operators

\[
 X=\sum_a r_a d_a\otimes h_a,\qquad
 Y=\sum_a r_a d_a\otimes q_a,\qquad
 Z=\sum_a v_a\otimes q_a.
\]

Define

\[
 A_r=r^T(G+C\odot E)r\ge0,
 \quad U=\|X\|_{\rm HS},\quad N=\|Y\|_{\rm HS},
 \quad P=\|Z\|_{\rm HS}.
\]

The first inequality needs no imported matrix theorem: `G` is a feature Gram,
and `C odot E` is the Gram of `x_a/sqrt(d) tensor ell_a`. Equation (3) gives
the exact scalar identity

\[
 \boxed{\dot L=-\frac4{m^2}
 \left[A_r+U^2-\langle X,Y\rangle_{\rm HS}
             -\frac\rho{2\tau}\langle X,Z\rangle_{\rm HS}\right].}
 \tag{5}
\]

For clarity, every term is computable from finite scalar contractions, e.g.

\[
\begin{aligned}
 U^2&=\sum_{ab}r_ar_bD_{ab}H_{ab},\\
 N^2&=\sum_{ab}r_ar_bD_{ab}\langle q_a,q_b\rangle,\\
 P^2&=\sum_{ab}\langle v_a,v_b\rangle\langle q_a,q_b\rangle,\\
 \langle X,Y\rangle&=\sum_{ab}r_ar_bD_{ab}\langle h_a,q_b\rangle,\\
 \langle X,Z\rangle&=\sum_{ab}r_aV_{ab}\langle h_a,q_b\rangle.
\end{aligned}
\]

These formulas are scalar identities, not an autonomous method for supplying
the contractions.

**Proposition 1 (conditional dissipation without changing q=1).** If, at a
current state, some `eta` in `[0,1]` obeys

\[
 N+\frac\rho{2\tau}P\le\eta U,
 \tag{6}
\]

then

\[
 \dot L\le-\frac4{m^2}[A_r+(1-\eta)U^2]\le0.
 \tag{7}
\]

Proof: Cauchy--Schwarz bounds the two signed terms in (5) by
`U(N+rho P/(2 tau))`. This also covers `U=0`; condition (6) then makes the
entire middle-layer bracket zero. No inverse Gram matrix or division by
`rho` is used.

An alternative certificate uses the *actual signed* scalar bracket in (5)
and is less conservative than (6). A closure could preserve the PSD Gram of
the three operators `(X,Y,Z)` while estimating this bracket. PSD preserves
Cauchy--Schwarz, but does **not** imply that the bracket is nonnegative.
The needed estimate is precisely the sign/size of the lag correlations.

The residual-zero set is an exact equilibrium of every microscopic q=1 state:
all right-hand sides contain either `r` or `rho`. Any candidate aggregate
equations should retain that algebraic property. It alone says nothing about
fitting or approximation before the residual vanishes.

## 3. Why imposing a PSD residual generator changes the model

Writing (3) as

\[
 \dot r=-\frac2m Qr+\rho b,
 \quad Q=G+C\odot E+D\odot K^T,
 \quad b_a=\frac1{m\tau}\sum_bV_{ab}(H_{ba}-K_{ba}),
 \tag{8}
\]

does not give a PSD `Q`. Nor can the drift `rho b` simply be dropped. For
`rho>0`, one representation of the entire generator is

\[
 \dot r=-\frac2m\left(Q-\frac12bu^T\right)r,
 \qquad u=r/\rho,\quad u^Tu=m.
 \tag{9}
\]

This representation is nonunique and its symmetric part need not be PSD.
At `rho=0`, (3), not (9), is the nonsingular definition.

Here is an exact loss-increasing q=1 current state. Take width `n=1`, two
samples, labels `(1,1)`, and any linearly independent normalized inputs so
that the two first-layer preactivations can be prescribed. They may have any
correlation strictly between `-1` and `1`. Set

\[
 W_0=1,\quad h=(1/2,1/4),\quad k=(-1/2,-1/4),
 \quad v=(4,0),\quad w=1,\quad\tau=4.
\]

The first-layer weights are chosen to realize `atanh(h)` on the two inputs.
The reconstructed scalar mixer is

\[
 B=1+\frac12(4(-1/2)+0)=0.
\]

Therefore `g=f=ell=0`, `d_a=1`, `r_a=-1`, `rho=1`, and `hdot=wdot=0`.
Equation (1) gives

\[
 \dot B=(-1/2-1/4)+\frac18[4(1)+0]=-1/4.
\]

Consequently `fdot=(-1/8,-1/16)` and

\[
 \dot L=-\dot f_1-\dot f_2=3/16>0.\tag{10}
\]

All ordinary Gram matrices of this state are PSD because they are actual
Grams. The construction also persists under small changes of the source and
state, with the reconstructed mixer and loss derivative varying continuously.
Thus a universal PSD projection would replace an allowed q=1 vector field.

**Reachability limitation.** This is not a claim that the initialized q=1
trajectory visits this state, or that loss increases with positive
probability under the specified initialization. To impose PSD only on the
initialized reachable set, one must prove a property of that set, such as
(6); neither Gram realizability nor the zero-residual equilibrium proves it.

## 4. Same-source Gram fibers can have different loss jets

The following counterexample keeps the true mixer and transpose and allows
nondegenerate correlated data. It identifies the missing scalar moments.

Fix `m` normalized inputs whose input Gram `C` is positive definite; in
particular `m<=d`. Fix any binary label vector `y`, possibly containing both
signs. Define

\[
 \beta=\frac{y^TCy}{m^2}>0.
\]

At a current state choose an invertible real mixer `W_0`, a nonzero first-layer
vector `h` with all coordinates in `(-1,1)`, and put

\[
 H=\langle h,h\rangle,\quad
 w=W_0^{-T}h,\quad v=-W_0h/H,
 \quad h_a=k_a=y_a h,\quad v_a=y_a v.
 \tag{11}
\]

Full row rank of the input matrix lets a first-layer matrix `A` realize
`atanh(h_a)` for every sample. The reconstructed mixer is

\[
 B=W_0+v\otimes h=W_0(I-P_h),
 \quad P_h=h h^T/(nH).
\]

It obeys `Bh=0`, `B^Tw=0`, and hence

\[
 g_a=0,\quad d_a=w,\quad\ell_a=0,\quad f_a=0,
 \quad r=-y,\quad\rho=1,\quad\langle w,v\rangle=-1.
 \tag{12}
\]

Take `tau>1` arbitrary. This is a valid finite q=1 current state, with finite
coordinates and exactly the prescribed model equations.

Let `P,Q` be orthogonal transformations on the second and first neuron
spaces satisfying

\[
 P W_0=W_0 Q.\tag{13}
\]

Use the same fixed `W_0`, replace `h,k` by `Qh,Qk` and `w,v` by `Pw,Pv`, and
reconstruct `A` from the new first-layer values. Then `B` is replaced by
`P B Q^T`. Provided the new coordinates of `h` remain in `(-1,1)`, equations
(11)--(12) remain valid. All pairwise Grams of the lower fields
`(h_a,k_a,ell_a)` and upper fields `(g_a,d_a,v_a,w)` are unchanged. This
dictionary does not include arbitrary additional coordinatewise gates or
fixed test vectors.

More strongly, every pairwise contraction obtained by appending any finite
linear word of `W_0` and `W_0^T` to these typed fields is unchanged: (13) and
its transpose move `P,Q` through each word, and the final orthogonal factors
cancel in the inner product. The same statement holds if `B,B^T` are also
allowed linear letters. This is a same-source symmetry, not resampling the
mixer or replacing its transpose by independent Gaussian noise.

The coordinate nonlinearity is not equivariant under a general `Q`. For
example, at the state (11),

\[
 \dot\ell_a=2W(1-h^2)\odot h,
 \quad W=\langle w,w\rangle,
\]

and hence

\[
 \frac d{dt}\langle h_a,\ell_b\rangle
 =2y_a W\,[H-\langle h^2,h^2\rangle].\tag{14}
\]

`H,W` are invariant under the paired rotation; the fourth coordinate moment
need not be. Thus even the enlarged full typed Gram itself need not have a
single-valued autonomous derivative.

The loss obstruction is stronger than this derivative of an auxiliary
observable. Define

\[
 S=\langle h^2,(1-h^2)^2\rangle,
 \quad M_4=\langle w^2,w^2\rangle,
 \quad a=2WH,
 \quad F(t)=\frac1m\sum_a y_a f_a(t).
\]

At (11)--(12), direct q=1 differentiation gives

\[
 f'_a=y_a a,\qquad f''_a=-y_a a^2,
\]

and

\[
 \boxed{F'''=a^3+32H^2W
    +\beta\left(24W^2-\frac{4W}{\tau}\right)S
    -32H^3M_4.}\tag{15}
\]

Here the derivatives are in physical time. In particular the `tau^-1` term
records the actual q=1 memory clock, and cannot be omitted.

To verify (15) without suppressing a nontrivial differentiation, set
`c_a=(Cy)_a/m`. At the state, the first nonzero derivatives are

\[
\begin{aligned}
 w'&=h'_a=k'_a=d'_a=0,&
 B'&=2w\otimes h,\\
 g'_a&=2y_aH w,&
 \ell'_a&=2W(1-h^2)\odot h,\\
 w''&=4H w,&
 h''_a&=4Wc_a(1-h^2)^2\odot h,\\
 k''_a&=0,&
 k'''_a&=h''_a/\tau,\\
 d''_a&=4H w-8H^2w^3.
\end{aligned}
\]

It is economical to differentiate (3) twice. At this state,

\[
\begin{aligned}
 G''_{ab}&=8y_ay_bH^2W,& E''_{ab}&=8W^2S,\\
 D''_{ab}&=8HW-16H^2M_4,&
 K''_{ba}&=4W y_b c_aS,\\
 (H_{ba}-K_{ba})''&=4W y_a c_bS.&
\end{aligned}
\]

The first derivatives of `G,E,D,K,H-K` vanish. Although
`V'_ab=2y_bW`, it gives no contribution because `H-K` and its first derivative
vanish. Inserting the displayed second derivatives in (3),
using `sum_a y_a c_a/m=beta` and `V_ab=-y_b`, gives (15), including the term
`a^3` from the second residual derivative. Finally

\[
 L'''=-2F'''-6a^3,\tag{16}
\]

because `f(0)=0`, `f'_a=y_a a`, and `f''_a=-y_a a^2` at the current time.

### An explicit paired rotation with unequal loss derivatives

For width two take

\[
 Q=P=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \quad W_0=2I+Q,\quad h=\alpha(1,0)^T.
 \tag{17}
\]

This source is invertible, has distinct singular values `3,1`, and satisfies
(13). The two hidden vectors are `h` and
`Qh=alpha(1,1)^T/sqrt(2)`, both admissible for sufficiently small positive
`alpha`. Both have `H=alpha^2/2`, and

\[
 W=\frac{5-2\sqrt2}{18}\alpha^2>0.
\]

Using a prime here only to denote the *rotated state*,

\[
 S'-S=\frac{\alpha^4}{2}-\frac{3\alpha^6}{8}.
\]

Also `M_4'-M_4=O(alpha^4)`. Thus (15) gives the explicit small-amplitude
separation

\[
 F'''_{\rm rotated}-F'''_{\rm original}
 =-\frac{2\beta W}{\tau}\alpha^4+O(\alpha^8)
 =-\frac{\beta(5-2\sqrt2)}{9\tau}\alpha^6+O(\alpha^8),
 \tag{18}
\]

which is nonzero for all sufficiently small `alpha>0`. The omitted terms
are finite polynomials in `alpha`; `beta,tau` are fixed. The loss derivatives
therefore differ by (16), despite equal current predictions and all the
specified scalar Grams.

This example is not confined to a single measure-zero choice of Gaussian
mixer: because its singular values are distinct, locally one can choose
continuous singular vectors and take the paired sign transformations
`P=U diag(1,-1)U^T`, `Q=V diag(1,-1)V^T`. They satisfy (13). At a fixed small
`alpha`, the strict inequality in (18), and the bound on both hidden vectors,
persist in a neighborhood of (17). A width-two Gaussian mixer has a positive
density on that neighborhood. This says only that the *source algebra*
counterexample is robust. The constructed current states still need not be
reachable from the specified random initialization.

For every larger finite width one can embed the two-dimensional construction
as a block with extra distinct nonzero singular values and zero extra entries
in `h`, and then perturb. The normalization changes constants but not the
nonzero leading term. This is not a lower bound uniform in Gaussian
probability or a population-limit obstruction.

**Proposition 2 (scoped Gram nonclosure).** On a state class containing the
two states above, no deterministic autonomous ODE initialized only from the
fixed source, data, and all such current typed linear-word pairwise Grams can
reproduce the loss curve for both states. Its initialized scalar state is
identical for the two targets, hence its prediction is identical; equations
(15)--(18) show that the actual curves differ. This conclusion holds even
if the purported closure stores these Gram arrays through a PSD factorization.

More quantitatively, write the nonzero loss-third-derivative difference as
`delta`. Both targets have equal loss derivatives through order two. Smooth
local ODE theory applies around `r=-y`, where `rho>0`, so Taylor's formula
gives a time `t_0>0` such that

\[
 |L_1(t)-L_2(t)|\ge\frac{|\delta|}{12}t^3
 \qquad(0<t<t_0).
\]

Any common predicted loss has error at least `|delta| t^3/24` on one of the
two states. This bound is for that aggregate encoding on this current-state
class. It is not a no-go theorem for enriched moments, a special initialized
trajectory, or the full admissible approximation class.

## 5. Consequences for a finite closure mechanism

A concrete realizability-oriented attempt would evolve the typed Grams of
`h,k,ell` on the first neuron space and `g,d,v,w` on the second, plus the
tensor Gram of `X,Y,Z`, retaining the exact residual equation (3) and the
residual-zero factors. The moving scalar count is initially `O(m^2)`. Using
Gram factors can preserve PSD and the Cauchy--Schwarz constraints used in
Proposition 1. It does not solve the following two distinct problems:

* The PSD cone does not encode the required identities between a coordinate
  and its tanh or its squared derivative. Section 4 exhibits different
  coordinatewise moments within the same PSD Gram fiber.
* The source terms in (4), and derivatives of the tensor Gram, require those
  missing moments as well as applications of the same fixed mixer and
  transpose. Arbitrary Gaussian completion or refactorization chooses one
  completion without an error bound for the actual q=1 completion.

The first necessary enrichment is explicit: the family in (11) requires
`<h^4>`, `<h^6>` and `<w^4>` (or equivalent contractions) to remove the loss
jet ambiguity. Their derivatives create further coordinate multipliers and
mixed forward/backward contractions. No statement here says that this
hierarchy cannot be approximated. The unresolved estimate must control the
**collective omitted contribution on the initialized reachable set**, not
merely ensure that retained Grams are PSD or individual entries are bounded.

A precise remaining approximation obligation for this route is:

> Construct, from the Gaussian source law and finite data only, a nested
> scalar moment family and computable autonomous closure maps. Prove that
> the errors they produce in (3)--(4) and their additional retained equations
> are uniformly small on the relevant initialized q=1 trajectories, with a
> quantified rate in the number of retained scalars. Establish enough
> stability to turn that source error into loss accuracy at equal physical
> times. The rate and stability constants must yield `S(epsilon)=o(epsilon^-2)`.

This is not claimed proved or made easier merely by restating it. The new
information from this route is exactly where its lowest-order source first
escapes and why positivity supplies no replacement for it. A promising
reopening would require a reachable-state estimate for the omitted
coordinate moments or their *loss-weighted* contribution; an arbitrary
ambient Gram ball is already insufficient by Proposition 2.

## 6. Computability, costs, and claim status

At finite width every displayed coefficient is computable from the actual
state and fixed source by sums, products, tanh and true transpose actions.
This is not the required compressed coefficient provenance: direct
evaluation stores `O(nm)` moving fields and `O(n^2)` fixed mixer entries and
uses `O(n^2 m)` work for dense mixer actions. The scalar diagnostic arrays
cost `O(m^2)` storage but can cost `O(nm^2)` to form, in addition to those
matrix actions. Factorizing the scalar Grams only changes that diagnostic
representation. It does not eliminate the moving neuron fields needed to
evaluate their derivatives.

A population use of the identities would replace inner products by
expectations on the stated population spaces with the specified operator
and its adjoint. It additionally requires existence and convergence of
that population q=1 system. No population identification, rate, all-time
bound, scalar coefficient evaluator, or matching root-width error estimate
is proved in this route.

| Claim | Mathematical status | Check status / limit |
|---|---|---|
| Equations (1)--(5), (8)--(9) | Exact at finite width | Direct derivation and author algebra check |
| Proposition 1 | Proved conditional dissipation certificate | Requires its actual lag bound, not assumed generally |
| Equation (10) | Exact current-state loss-increase example | Reachability from target initialization unproved |
| Equations (14)--(18), Proposition 2 | Proved current-state Gram obstruction | Same-source, true-adjoint, nonlinear; no initialized/population no-go |
| PSD Gram completion as approximation | Unproved candidate | Missing source estimate is decisive |
| `S(epsilon)=o(epsilon^-2)` | Open | No moving/fixed cost claim satisfying target |

The route is **frozen with a sharp obstruction to its lowest-order witness**.
It should not be broadened into universal nonclosure, or called a successful
finite approximation. No changes to maintained material or Git writes were
made.
