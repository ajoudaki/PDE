# Normalized ReLU under one-sample loss GD: compact-time audit

## Verdict

For the same width-first `q=1`, two-hidden-layer network, normalized ReLU
does not presently have a proved compact-time discrete-to-continuous OMFP
theorem.  Positive homogeneity gives strong compact-time energy and norm
bounds, derived below, but it does not close either of the two missing
bridges:

1. the actual finite-width network has not been identified at every fixed
   nonzero mesh with an indicator-valued reused-matrix OMFP state; and
2. even inside a proposed hard-gate state, attracting top-gate switches
   prevent a classical ODE with any fixed value of `phi'(0)` from being the
   global limiting object.  A mesh limit, if it exists, needs an additional
   Filippov/occupation-measure state and a uniqueness theorem for that
   augmented dynamics.

Thus the classical fixed-derivative ReLU gradient flow can fail to continue,
whereas convergence of the width-first discrete losses to a generalized
mesh-selected flow remains open rather than refuted.

## 1. Exact loss dynamics and homogeneity identities

Let

\[
 \phi(x)=\sqrt2\,x_+.
\]

In the population notation put

\[
 X=\phi(u),\quad Z=GX,\quad Y=\phi(Z),
\]

\[
 B=A\phi'(Z),\quad Q=G^*B,\quad D=\phi'(u)Q,
\]

and

\[
 f=\langle A,Y\rangle,\qquad r=1-f,
 \qquad \ell={1\over2}r^2.
\]

The learned connector is `G=Gamma+q`, where the immutable pointed Gaussian
action satisfies `||Gamma||_op<=2`.  Half-MSE gradient flow, wherever a
classical selection exists, is

\[
 \dot A=rY,\qquad \dot u=rD,\qquad
 \dot q=r(B\otimes X).                                  \tag{1.1}
\]

The raw tangent kernel is

\[
 K=\|Y\|_2^2+\|D\|_2^2+\|B\|_2^2\|X\|_2^2.             \tag{1.2}
\]

Direct differentiation gives

\[
 \dot f=rK,\qquad \dot r=-rK,
 \qquad \dot\ell=-r^2K.                                \tag{1.3}
\]

These identities use only first derivatives away from gates.  They extend
along an absolutely continuous selected trajectory only if that trajectory
exists, `q` remains trace class, and the ReLU chain rule is valid for the
selection.  Those are conditional hypotheses here, not an already proved
hard-indicator population theorem.
Starting from the width-limit initialization `f(0)=0`,

\[
 r(t)=\exp\{-\int_0^tK(s)\,ds\}\in(0,1],
 \qquad 0\le f(t)<1.                                    \tag{1.4}
\]

ReLU's Euler identity `x phi'(x)=phi(x)` also gives

\[
 \langle A,Y\rangle=f,
\]

\[
 \langle u,D\rangle
 =\langle X,Q\rangle
 =\langle GX,B\rangle
 =\langle Z,A\phi'(Z)\rangle=f.                        \tag{1.5}
\]

Consequently

\[
 {d\over dt}\|A\|_2^2={d\over dt}\|u\|_2^2=2rf\le {1\over2}. \tag{1.6}
\]

At the normalized initialization both squared norms equal one.  On
`[0,T]`, set

\[
 R_T=1+{T\over2}.
\]

Then

\[
 \|A(t)\|_2^2,\ \|u(t)\|_2^2\le R_T.                   \tag{1.7}
\]

Since `||b tensor x||_1=||b||_2||x||_2` and
`||B||_2<=sqrt(2)||A||_2`, `||X||_2<=sqrt(2)||u||_2`,

\[
 \|q(t)\|_1
 \le2\int_0^t\|A(s)\|_2\|u(s)\|_2\,ds
 \le2TR_T.                                             \tag{1.8}
\]

Thus

\[
 \|G(t)\|_{\rm op}\le 2+2TR_T=:g_T.                   \tag{1.9}
\]

Finally,

\[
 \|Y\|_2\le2g_T\|u\|_2,\qquad
 \|D\|_2\le2g_T\|A\|_2,
\]

so

\[
 K(t)\le8g_T^2R_T+4R_T^2.                              \tag{1.10}
\]

Equations (1.4), (1.7)--(1.10) rule out compact-time norm explosion for any
selected continuous trajectory.  They do not prove existence, uniqueness,
or convergence of explicit Euler meshes.

## 2. Loss time does not remove the fixed-step hard-indicator bridge

At finite width one half-MSE step is exactly

\[
 \theta_{k+1}=\theta_k+h r_k g(\theta_k).                \tag{2.1}
\]

At initialization the width-first residual is `r_0=1`; at the next step it
is a deterministic nonzero scalar for all sufficiently small fixed `h`.
Therefore the alternating adaptive queries of the same `W` and `W^T`, their
hard gates, learned rank-one terms, and aggregate response coefficients are
identical to the feature-ascent queries up to scalar step weights.  No query
is removed by passing to loss time.

The fixed-step theorem in
`temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md` assumes

\[
 \phi\in C^2,\qquad \|\phi'\|_\infty+\|\phi''\|_\infty<\infty,
\]

and hence does not apply to ReLU.  The dedicated hard-kink audits
`RELU_LEAKY_BRIDGE_AUDIT.md` and `RELU_LEAKY_ADVERSARIAL_AUDIT.md` leave
open, explicitly:

- adaptive alternating Gaussian conditioning for discontinuous gates;
- non-atomicity of every later queried gate, including singular history
  Grams;
- convergence and uniform integrability of all empirical Grams and terminal
  readouts, including `L^2` self-averaging of the predictor (mean
  convergence alone does not identify the expected squared loss); and
- equality of the regression response DAG with the proposed indicator DAG.

Thus even pointwise fixed-nonzero-mesh identification of the actual hard
ReLU network is not an available theorem in the study.

## 3. The classical continuous vector field has attracting switches

### 3.1 An exact finite-width positive-probability obstruction

The obstruction is already present in the actual width-two network.  Put
`c=sqrt(2)` and, with `n=2`, write

\[
 X_j=\phi(u_j),\quad
 z_i={1\over\sqrt2}\sum_jW_{ij}X_j,\quad
 Y_i=\phi(z_i),\quad
 f={1\over2}\sum_iA_iY_i.
\]

For half-MSE flow, direct differentiation gives

\[
 \dot z_i=rA_i\phi'(z_i)Q_X
 +{r\over2}\sum_{j,k}W_{ij}W_{kj}A_k\phi'(z_k)
                         \phi'(u_j)^2,
 \qquad Q_X={1\over2}\sum_jX_j^2.                    \tag{3.1}
\]

Choose

\[
 u=(1,1),\qquad W_1=(1,-1),\qquad W_2=(2,0),
\]

\[
 A_2={1\over4c},\qquad A_1=-{\lambda\over c},
 \qquad \lambda>{1\over8}.                             \tag{3.2}
\]

Then `X=(c,c)`, `z_1=0`, `z_2=2`, `f=1/4`, `r=3/4`, and
`Q_X=2`.  If `s` denotes the slope used at the first top gate, (3.1)
reduces exactly to

\[
 \dot z_1=r\{4A_1s+2A_2c\}.                            \tag{3.3}
\]

The negative- and positive-side velocities are therefore

\[
 p={3\over8}>0,
 \qquad q={3\over4}\left({1\over2}-4\lambda\right)<0. \tag{3.4}
\]

For a fixed convention `phi'(0)=d`, the contact velocity is

\[
 v_0={3\over4}\left({1\over2}-{4\lambda d\over c}\right). \tag{3.5}
\]

For every fixed real `d`, choose `lambda>1/8` different from the at most one
value that makes (3.5) zero.  Now perturb `W_1` to `(1+delta,-1)` with
`delta>0` sufficiently small.  This gives `z_1=delta>0`, while all bottom
gates and the second top gate remain a fixed positive distance from zero.
The vector field is smooth in this sign cell.  By (3.4) and continuity,
`dot z_1` stays bounded above by a negative constant until `z_1` hits zero,
which occurs in time `O(delta)`.  At the hit, the strict inequalities
`p>0>q`, `r>0`, and `v_0!=0` persist.

All these inequalities persist on an open neighborhood of the displayed
finite parameter vector.  The iid Gaussian initialization has a strictly
positive density on that neighborhood.  Hence, for every fixed derivative
convention, the actual width-two Gaussian network has a positive-probability
set of regular initial conditions whose classical loss-gradient trajectory
reaches a noncontinuable attracting top gate.

This finite-width fact must not be promoted to a statement that the
width-first population trajectory develops a positive-mass sliding set.
That promotion requires exactly the hard-indicator state-evolution and
uniform gate-crossing theorem which is open in Section 2.

### 3.2 The marked population normal form

The marked top-gate calculation at initialization gives, for general slopes
`(a,b)`, the two normal velocities

\[
 p=\zeta+2bA,\qquad q=\zeta+2aA,
\]

where `A` and `zeta` are independent centered nondegenerate Gaussians.  For
normalized ReLU, `(a,b)=(sqrt(2),0)`, so

\[
 p=\zeta,\qquad q=\zeta+2\sqrt2 A.                       \tag{3.6}
\]

The event

\[
 \{p>0>q\}
 =\{\zeta>0,\ A<-\zeta/(2\sqrt2)\}                      \tag{3.7}
\]

has strictly positive probability.  It is an attracting gate: on the
negative side the normal coordinate moves upward, and on the positive side
it moves downward.  Multiplication by the half-MSE residual `r>0` preserves
both signs.

This is a positive-probability law for the marked normal data conditional
on examining a gate surface.  Since an initialized Gaussian preactivation
equals zero with probability zero, it is not by itself a theorem that the
canonical width-first population trajectory reaches such a surface, much
less that it creates positive mass there.  That hitting statement remains
part of the missing hard-indicator population dynamics.

Freeze the remaining state at such a contact.  The normal equation is

\[
 \dot z=
 \begin{cases}
 p,&z<0,\\
 q,&z>0,\\
 v_0,&z=0,
 \end{cases}                                             \tag{3.8}
\]

where a fixed convention for `phi'(0)` produces one fixed algebraic choice
of `v_0` for the current sources.  Equation (3.8) has an absolutely
continuous continuation from `z(0)=0` only if `v_0=0`.  Indeed, put
`w=|z|` and `c=min(p,-q)>0`.  The function `w` is absolutely continuous and

\[
 w'(t)\le-c
\]

for almost every `t` with `z(t)!=0`.  On the level set `{z=0}`, absolute
continuity gives `z'=0`, hence `w'=0`, almost everywhere.  Integration
therefore yields

\[
 w(t)\le-c\,|\{s\in[0,t]:z(s)\ne0\}|.
\]

The left side is nonnegative, so the displayed set has measure zero for
every `t`, and continuity forces `z` to vanish identically.  This solves
(3.8) only when `v_0=0`.

But `v_0` has the form `zeta+2c_0A` for a fixed derivative convention
`c_0`.  No constant `c_0` makes this vanish on every positive-probability
event (3.7).  This is the finite-dimensional attracting-switch obstruction
recorded as E10 in
`nonlinear_activation_operator_ide/EVIDENCE_LEDGER.md`.

Explicit Euler does not stop existing at (3.7); it chatters across the gate
in an `O(h)` layer.  A possible limit is a Filippov sliding rule with a
source-dependent occupation fraction between the two gate sides.  That
fraction is not the value of `phi'(0)` and is visible to
\(B=A\phi'(Z)\), to
the reused adjoint `G^*B`, and therefore to the kernel and future state.

For the frozen scalar normal equation this occupation is explicit.  Once
the Euler iterate enters the invariant strip

\[
 hq<z_k<hp,
\]

the rescaled phase `y_k=z_k/h` obeys

\[
 y_{k+1}=y_k+p\quad(y_k<0),\qquad
 y_{k+1}=y_k+q\quad(y_k>0).                             \tag{3.9}
\]

After identifying the endpoints of `(q,p)`, (3.9) is rotation by `p` on a
circle of length `p-q`.  More explicitly, put

\[
 \alpha={p\over p-q},\qquad x_k={y_k-q\over p-q}\in(0,1).
\]

Then `x_(k+1)={x_k+alpha}` modulo one, and the positive-side indicator is

\[
 I_k=\mathbf1_{\{x_k\ge1-\alpha\}}
     =x_k+\alpha-x_{k+1}.
\]

Therefore

\[
 \left|\sum_{k=0}^{N-1}I_k-N\alpha\right|
 =|x_0-x_N|<1.                                           \tag{3.10}
\]

Every non-boundary orbit consequently has positive-side occupation

\[
 \lambda_+={p\over p-q},qquad
 (1-\lambda_+)p+\lambda_+q=0.                          \tag{3.11}
\]

up to an endpoint-count error bounded independently of the number of
steps.  Hence the frozen scalar Euler scheme converges to `z=0` and its
gate converges only weakly, with occupation (3.11).

This calculation shows both sides of the issue.  A single frozen kink has a
canonical mesh average, so attraction alone does not disprove mesh
convergence.  In the network, however, `p` and `q` evolve through the same
aggregate gate occupations and through `G^*B`; proving that (3.11) remains a
unique, restartable closure is precisely the missing kinetic OMFP theorem.

Moreover, replacing the chattering gate by its scalar mean is not enough.
If `I_h` is the positive-side gate, then weakly one expects

\[
 I_h\rightharpoonup\lambda_+,
 \qquad I_h^2=I_h\rightharpoonup\lambda_+,
\]

whereas the square of the weak mean is `lambda_+^2`.  The update of `q`
and the reused action `G^*B` are linear in `B=A I_h`, but the tangent kernel
contains `||B||_2^2`, `||G^*B||_2^2`, and their response correlations.
Therefore the loss rate itself can see the gate Young measure.  A proof must
transport its required first and second occupation moments; a pointwise
choice of `phi'(0)` or a single averaged gate field loses information.

## 4. Why ordinary Banach-ODE arguments do not repair the gap

The ReLU Nemytskii map is Lipschitz but not Frechet differentiable at a
Gaussian `L^2` field.  Let `U` have a density positive at zero and let

\[
 v_\varepsilon=-2U\,\mathbf1_{\{0<U<\varepsilon\}}.
\]

For the candidate derivative
`Dphi(U)v=sqrt(2) 1_{U>0}v`, put

\[
 m_\varepsilon
 =\mathbb E[U^2\mathbf1_{\{0<U<\varepsilon\}}].
\]

Then

\[
 \|v_\varepsilon\|_2=2\sqrt{m_\varepsilon},
\]

whereas

\[
 \|\phi(U+v_\varepsilon)-\phi(U)-D\phi(U)v_\varepsilon\|_2
 =\sqrt{2m_\varepsilon}.                                \tag{4.1}
\]

The quotient is `1/sqrt(2)`, not zero.  Consequently the classical smooth
Banach-space sewing theorem cannot be applied on the natural `L^2` state.
The energy bounds of Section 1 do not change this local fact.

## 5. Exact theorem still needed

A genuine compact-time theorem for the discrete ReLU losses would need all
of the following, in this order:

1. pointwise fixed-mesh width identification for the hard indicator program
   with the actual reused matrix and adjoint;
2. an augmented population state retaining the gate-side occupation/Young
   measure created by attracting switches;
3. compact-time, partition-uniform tail and response estimates for
   `Q=G^*B` on that augmented state;
4. uniqueness and restartability of the resulting Filippov/kinetic OMFP;
   and
5. a split-mesh estimate with a dyadically summable modulus, followed by
   convergence of the loss readout.

No artifact in the study proves items 1--4 for hard ReLU.  Positive
homogeneity proves the useful a priori bounds (1.4)--(1.10), but it does not
determine the missing occupation field or control the reused-adjoint
response hierarchy.

Accordingly, the endpoint question has the following exact status:

\[
 \begin{array}{c|c}
 \text{classical loss-gradient ODE with fixed }\phi'(0)
   &\text{can be noncontinuable with positive finite-width probability},\\
 \text{width-first discrete endpoint losses as }h\downarrow0
   &\text{open; neither convergence nor mesh dependence is proved}.
 \end{array}
\]

The frozen occupation formula proves that the first row does not imply
failure in the second row.
