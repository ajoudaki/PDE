# Finite memory selects a function through the geometry of its learning path

29 September 2026. Continuation of the intrinsic finite-closure investigation.
This synthesis is about the autonomous residual-activity-clock model in
MODEL.md, with zero initial readout, finite q, tanh, and the actual fixed
Gaussian matrix actions and transposes. Theorems below use no dense-reference
approximation, population independence or width limit. They are internally
derived results, not promoted book material or novelty claims.

The stronger organizing principle is this: **fitting constrains the final
training-feature directions; the evolving memory also selects a function in
directions invisible to those constraints.** Temporal history determines part
of that selection. Low memory order already supports nonlinear selection;
higher orders change how temporal correlations enter it. The shared clock
also creates a specific path-dependent deformation of the test function.

The results establish these mechanisms, not that the selected test function
is statistically good for every task. Unknown target behavior outside the
observed inputs is not specified by the training equations alone.

## 1. An exact split of the whole learned function

At any time let h(x) be the last hidden feature, H=[h(x_1),...,h(x_m)],
G=H^TH/n and k(x)=H^Th(x)/n. Let p be the current vector of training
predictions and P_H the orthogonal projector onto the columns of H. Define
u=(I-P_H)w. Then, with the Moore--Penrose inverse,

\[
 f(x)=k(x)^TG^\dagger p+\frac{u^Th(x)}n.                  \tag{1}
\]

Proof: p=H^Tw/n and P_H=HG^\dagger H^T/n, so P_Hw=HG^\dagger p;
substitute w=P_Hw+u. This works even when G is singular.

At a converged interpolating endpoint p=y. The first term is precisely the
prediction of the minimum-Euclidean-norm readout that fits the labels with
these final features. The second term vanishes on every training input,
since H^Tu=0, but need not vanish elsewhere. It is not determined by the
labels and final training features. The exact extra readout norm is

\[
 \|w\|^2/n=p^TG^\dagger p+\|u\|^2/n.                    \tag{2}
\]

The closure's readout equation identifies the source of u. At time T,

\[
 u_T=-\frac2m\sum_a\int_0^T
 r_a(t)(I-P_{H_T})h_t(x_a)\,dt.                         \tag{3}
\]

Because P_(H_T)^perp annihilates h_T(x_a), the integrand is equivalently
the projected displacement of the old feature from its final value.
Credit accumulated along directions outside the final training-feature
span can therefore survive after every training error disappears.

For tanh this is a statement about the entire input space, with the exact
uniform bound

\[
 \sup_{x\in\mathbb R^d}
 |f_T(x)-k_T(x)^TG_T^\dagger p_T|
 \le\|u_T\|/\sqrt n.                                   \tag{4}
\]

This is not merely an algebraically permissible phenomenon. The full proof
in FINAL_FUNCTION_ROUTE.md constructs converged, canonically initialized
two-hidden-layer closures with one sample, width two, and every fixed finite
q, for which u_infinity is nonzero and changes a genuine test prediction.
The construction persists on an open set of Gaussian initializations. It
requires sufficiently small fixed labels on that set; it is not a claim of
generic all-label fitting. Hence zero readout initialization does not force
a minimum-readout-norm solution in the final feature map.

This separates two sources of function selection: the final features define
a learned geometry, while the readout also retains a contribution from the
path by which that geometry was reached. Equation (1) is not a claim that
every feature-learning effect is specific to moment closure.

## 2. What a test input retrieves from temporal memory

For a hidden layer at time T, let v be a current test feature and let
c_a(xi)=h_a(xi)^Tv/n be its similarity to sample a's historical feature,
including the prescribed prefix. Let P_q project scalar functions on the
activity interval onto the first q Legendre modes. Then exactly

\[
 (W_\ell-W_\ell^0)v
 =-\frac2m\sum_a\int_0^\tau b_a(\xi)
                         (P_qc_a)(\xi)\,d\xi.          \tag{5}
\]

Substitute the moment integrals and use the finite projection kernel to
obtain (5). Thus q controls how much *temporal variation of similarity to
the current test input* is used to retrieve error credit. At q=1 only its
mean is used; additional modes retain changing trends of similarity.
The current feature v is itself learned through all preceding layers, so
this is not projection onto a fixed collection of input functions.

## 3. Label magnitude selects progress along a common learning path

For multiple samples, write e_a=r_a/rho on intervals of nonzero residual.
Dividing the state equations by rho makes the clock tau the time variable.
Only the normalized vector e enters the backward/write sources. Residual
magnitude determines physical speed; residual direction determines those
sources along the activity path.

For one sample, before fitting a positive target, e=-1. The resulting
augmented-state path is independent of the positive label's magnitude.
With s=2(tau-1), write F(s,x) for its whole-input predictor. A positive
label y selects the first s_y with F(s_y,x_0)=y, if this level exists and
is reached in physical time. Negative labels give the same hidden path
with reversed readout. This is exact at every finite q and depth under
the prescribed zero readout.

Near initialization, the level exists for every sufficiently small label
when h_0^L(x_0) is nonzero. The training slope is
alpha=||h_0^L(x_0)||^2/n>0, so it remains positive on a small activity
interval. The physical clock s'=2(y-F(s,x_0)) approaches its level
exponentially. Therefore the path description actually gives a converged
terminal network there. The threshold can depend on the realization and q.

This reformulates one-sample learning as function-path selection:

\[
 f_\infty^y(x)=F(s_y,x).                               \tag{6}
\]

It does not assert that F reaches all label levels. At general Gaussian
width, a proof controlling its global history-alignment terms remains open.

## 4. The first nonlinear feature feedback is favorable for fitting

There is an arbitrary-depth identity behind the initial motion. Let theta
collect the hidden weights, let M be their canonical mobility (n for the
first layer, one for middle layers), and define

\[
 V(\theta)=\frac{\|h_\theta^L(x_0)\|^2}{2n}.
\]

On the universal positive-label path,

\[
 \theta(s)=\theta_0+\frac{s^2}{2}M\nabla V(\theta_0)+O(s^4),
\]
\[
 F(s,x_0)=\alpha s+\beta s^3+O(s^5),\qquad
 \beta=\frac23\nabla V(\theta_0)^TM\nabla V(\theta_0).    \tag{7}
\]

The proof in ACTIVITY_AND_FUNCTION.md differentiates the actual moment
equations. Zero readout first gives w(s)=s h_0^L+O(s^3). Its backward
signal produces the hidden acceleration M grad V, and integrating the
resulting feature change in the readout supplies the factor 2/3.

For tanh and the Gaussian initialization, beta is strictly positive almost
surely for every nonzero input and fixed finite depth. In particular the
last-hidden gradient is a nonzero outer product. The first representation
change strengthens the training response per unit accumulated activity,
even though individual weights and feature coordinates have mixed signs.
The positivity is a sum-of-squares identity, not a positive-matrix assumption.

This does not imply that all later representation changes help, that a
larger training response means smaller test risk, or that greater depth
improves the rate. It identifies the first nonlinear feedback loop with
no frozen-feature substitution.

For two hidden layers the terminal function can be made more explicit:

\[
 f_\infty^{(q)}(x;y)
 =A(x)y+C(x)y^3+E(x)y^5+q^2J(x)y|y|^5+O_K(|y|^7).       \tag{8}
\]

A(x)=h_0(x_0)^Th_0(x)/||h_0(x_0)||^2 is the exact frozen-hidden-feature
interpolant coefficient. The coefficients C,E,J are derived in
DIRECT_LEARNING_ROUTE.md and independent of fixed q. In particular:

- nonlinear feature learning changes the final test function at cubic order;
- every finite q, including q=1, already carries that effect;
- changing q first changes this expansion at degree six;
- these changes vanish at the training point, whose fitted value is y.

The report proves C and J nonzero almost surely at a fixed test input 2x_0.
For d>=2, the same statement holds at a fixed same-radius input with angle
pi/3 to x_0. Thus these are actual off-training shape changes, not merely
different training speeds or extrapolation outside the training radius.

The remainder is uniform on each compact input set, at fixed n,q and
initializer. The expansion is not uniform in growing q and is not a
recommendation to prefer a smaller q at finite labels. Its q^2 term also
shows that the label-to-function map from fresh initialization is generically
C5 but not C6 at zero for this clock and prefix convention. This particular
nonanalyticity belongs to the finite closure and should not be transferred
to another optimizer without proof.

## 5. One shared clock produces one leading off-training deformation

At every finite state, the whole-function velocity has the exact form

\[
 \dot f(x)=-\frac2m\sum_a K_q(x,a)r_a+\rho V_q(x).       \tag{9}
\]

Both fields are explicit functions of the current responses and moments.
K_q contains current backward similarities paired with the projected
forward endpoints. V_q is the transport of stored backward memory against
the mismatch of the current and remembered forward endpoint. The complete
formulas and normalization are in INTRINSIC_GEOMETRY_ROUTE.md. At a fixed
state, reversing all residuals reverses the first term and leaves the
second unchanged, since the activity clock advances for either sign.

Consider a fitted state, retain its full memory, and perturb its training
labels by eta. The precise local hypothesis is strict instantaneous residual
contraction: with A=(2/m)K_q(train,train), v=V_q(train),

\[
 \min_{\|z\|=1}
 \left[z^T\frac{A+A^T}{2}z-rac{|v^Tz|}{\sqrt m}\right]>0.     \tag{10}
\]

This condition implies a genuine local return theorem: small perturbations
fit exponentially, state travel is O(||eta||), and the extra clock advance
Delta tau is bounded above and below by positive constants times ||eta||.
It is a sufficient local condition, not an assumed property of every fit.

At the prescribed zero-readout initialization, V_q=0 and K_q is just the
initial last-feature Gram. If that Gram is positive definite on the training
set, (10) proves multi-input interpolation for sufficiently small labels
at every fixed finite q,n and depth. This deterministic local corollary has
a realization-dependent threshold, not a width-uniform one.

Write a(x)=(2/m)K_q(x,train). Eliminating the integrated training residuals
from (9) gives

\[
 \Delta f_\infty(x)
 =a(x)A^{-1}\eta+D(x)\Delta\tau+O_K(\|\eta\|^2),
 \quad D(x)=V_q(x)-a(x)A^{-1}v.                       \tag{11}
\]

Here D(x_a)=0 at every training sample. All leading nonlinear dependence
on a small label change lies in this *one function*, regardless of depth,
width, sample count or finite order. The amplitude is the additional shared
learning activity. This one-function statement is about local response
around a fitted memory state, not the dimension of all learned functions.

The derivation is short: integrate the training equation to obtain
eta=-A integral r dt+v Delta tau+O(||eta||^2); integrate the test equation;
then eliminate integral r dt. Contraction bounds state travel and make
freezing the coefficients an O(||eta||^2) operation.

This has a concrete consequence. Fit y, then y+eta, then y again, preserving
the accumulated memory at each endpoint. All training predictions return
exactly to their original values, whereas

\[
 f_{\rm cycle}(x)-f_*(x)
 =D(x)(\Delta\tau_{\rm out}+\Delta\tau_{\rm back})
       +O_K(\|\eta\|^2).                              \tag{12}
\]

If D(x) is nonzero, the test function changes at first order in the size of
the label excursion. The clock contributions add rather than cancel. This
is history dependence of the actual predictor, not just of internal moments.

The report proves a canonically reachable example: two scalar tanh hidden
layers, one input, positive Gaussian first/middle initial weights, small
fixed positive label, and each fixed finite q. At the unseen input x=2,
D is strictly negative. The construction holds on a positive-probability
Gaussian set with a common fixed label. Thus the mechanism is not just an
arbitrary-state possibility. Its prevalence and magnitude at large width
remain open, and there is no assertion that the induced drift improves risk.

From fresh initialization the label map in (8) is C5 at zero; from an
already fitted memory with D nonzero, the relearning map in (11) has a
first-order kink. These are different protocols, not conflicting claims.

## 6. Finite activity produces a well-defined whole-input endpoint

For any finite width, order, depth and dataset, if
S_infinity=integral_0^infinity rho(t)dt is finite, then the entire tanh
closure state converges, all training residuals vanish, and its predictors
converge uniformly on every compact input set. They also converge in
L2(mu) for every input probability measure mu. This statement is conditional
on finite activity; general-data finite activity is not proved here.

The proof uses finite total variation in activity time, not a mesh of passive
test samples. Bounded activations first bound the readout by 2S_infinity.
Moment projection energies bound each learned matrix; descending backward
bounds control the remaining layers. Raw coordinate velocities are then
bounded by constants times rho, giving Cauchy limits. Continuity gives a
limiting residual, which integrability forces to zero. Bounded outputs and
compact-uniform convergence give L2(mu) for every mu.

There is also an explicit spatial Lipschitz bound from a fixed activity
budget with no q or n factor, conditional on bounded initial operator norms.
Its depth recursion and constants appear in ACTIVITY_AND_FUNCTION.md. This
does not give an unknown-target test-risk bound or prove bounded activity
for unrestricted labels.

## Current scientific conclusion

The equations now support more than the idea of paired memory. They describe
how learning selects an entire function: representation change modifies the
geometry in which examples interact, accumulated credit leaves an additional
off-training component, and the common clock can transport that component
even along label cycles that leave the final training constraints unchanged.

The exact identities and local theorems make these statements testable and
mathematical. They do not yet establish general all-label fitting or beneficial
generalization. Those questions now require control of the sign and task
alignment of the induced function deformation, rather than treating all
feature motion as automatically useful.

The source proofs are in [FINAL_FUNCTION_ROUTE.md](FINAL_FUNCTION_ROUTE.md),
[DIRECT_LEARNING_ROUTE.md](DIRECT_LEARNING_ROUTE.md),
[INTRINSIC_GEOMETRY_ROUTE.md](INTRINSIC_GEOMETRY_ROUTE.md) and
[ACTIVITY_AND_FUNCTION.md](ACTIVITY_AND_FUNCTION.md). The parent
read them completely. The function route checked the learning route's
sixth-order expansion, and the learning route checked the arbitrary-depth
positive cubic identity. Thirty deterministic static algebra checks passed
with maximum discrepancy 1.71e-13 at tolerance 1e-9; the checks concern exact
identities, not empirical learning performance. No training experiments,
paper edits, external novelty claim or Git operation were performed.
