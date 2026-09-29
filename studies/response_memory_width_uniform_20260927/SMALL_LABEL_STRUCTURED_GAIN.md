# Structured forcing, tangent curvature, and the missing Gaussian step

Scoped analytic investigation, 28 September 2026. Inputs were
`SMALL_LABEL_ENERGY.md`, `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`, and the canonical
network, old-clock equations and projection-error identities in
`paper/main.tex`. The `solve-math-rigorously` skill was applied. No other
study, external source, experiment, or Git operation was used.

**Outcome.** There is no completed width-uniform comparison theorem here.
The calculation below identifies a specific obstruction to replacing the
missing carrier estimate by a one-sided energy or normal/tangent argument.
Even with bounded hidden operator norm, arbitrarily small fixed labels,
bounded initial readout coordinates, and a fixed positive readout Gram,
the canonical vector field has tangent expansion of order
`sqrt(n) Y^2`. Moreover, the original old-clock forcing generates a
nonzero perturbation in precisely the exceptional neuron coordinate.
This is a deterministic obstruction to the proposed proof shortcut,
**not a counterexample to the Gaussian-initialization theorem**. The
example's coherent initialized matrix is not typical Gaussian data.

## 1. Exact comparison energy

Use the mobility inner product and the sample RMS inner product from the
two input notes. Thus the adjoint of the output Jacobian is understood
between these two Hilbert spaces, and the dense field is `F=-2J* r`.
For two states `theta` and `theta_hat`, put `e=theta_hat-theta`,
`q=f(theta_hat)-f(theta)`, and

\[
 B=f(\widehat\theta)-f(\theta)-J(\theta)e,
 \qquad
 \widehat B=f(\theta)-f(\widehat\theta)+J(\widehat\theta)e.
\]

For the actual closure defect `E`, direct inner-product expansion gives

\[
 \frac12\frac{d}{dt}\|e\|_{\rm mob}^2
 =-2\|q\|_m^2
   -2\langle B,r\rangle_m
   -2\langle\widehat B,\widehat r\rangle_m
   +\langle e,E\rangle_{\rm mob}.
 \tag{1}
\]

Indeed, `J(theta)e=q-B`, whereas
`J(theta_hat)e=q+B_hat`; substitute these identities into
`-2< J(theta_hat)e,r_hat>+2<J(theta)e,r>`.
The negative prediction term therefore coexists with two output
linearization remainders. It does not give a sign to either remainder.

For one sample, let `v` be any parameter direction, and let
`z'_ell,h'_ell` denote its first directional forward variations. Write
`c_L=w` and `c_ell=W_(ell+1)^T delta_(ell+1)` for lower layers. Twice
differentiating the forward recursion yields the exact identity

\[
 D^2f[v,v]=\frac2n v_w^T h'_L
 +\frac1n\sum_{\ell=1}^L
       c_\ell^T\bigl[\phi''(z_\ell)\odot(z'_\ell)^2\bigr]
 +\frac2n\sum_{\ell=2}^L
       \delta_\ell^T v_{W_\ell}h'_{\ell-1}.
 \tag{2}
\]

Here the first-layer second preactivation variation is zero, while
`z''_ell=2v_(W_ell)h'_(ell-1)+W_ell h''_(ell-1)` for later layers.
Repeated substitution of this last equality proves (2), with the
backward recursion collecting the coefficients of each gate term.
The problematic term in the previous energy note is exactly the
initialized part of `c_ell` in (2), in second-variation form.

## 2. An explicit tangent direction with unbounded expansion

Take `m=d=1`, input `x=1`, and `L=2`. Fix

\[
 p=\tfrac12,\quad q=\tfrac9{10},\quad s=\tfrac45,
 \qquad A=1-p^2=\tfrac34,\quad Q=1-q^2=\tfrac{19}{100},
 \quad D=1-s^2=\tfrac9{25},\quad c=\operatorname{arctanh}s.
\]

For `n>=2`, define the orthonormal vectors

\[
 u=\frac{\boldsymbol1}{\sqrt n},\qquad
 v=\frac{(0,1,\ldots,1)^T}{\sqrt{n-1}},
 \qquad
 b_n=\frac{c\sqrt n+p}{q\sqrt{n-1}},\qquad g=e_1+b_nv.
\]

Choose the initial parameters

\[
 W_1=(-\operatorname{arctanh}p,
             \operatorname{arctanh}q,\ldots,
             \operatorname{arctanh}q)^T,
 \quad W_2=ug^T,\quad w=\omega\boldsymbol1,
 \quad y=(s+\tfrac12)\omega,
 \tag{3}
\]

where `omega>0` is arbitrarily small and independent of width. Then

\[
 h_1=(-p,q,\ldots,q)^T,\quad z_2=c\boldsymbol1,
 \quad h_2=s\boldsymbol1,\quad r=-\omega/2,
 \quad \Gamma_w=s^2.
 \tag{4}
\]

The definition of `b_n` verifies `g^T h_1=c sqrt(n)`, proving the
middle equality. All hidden operator norms are bounded uniformly in
`n`; the normalized initial first-layer norm is bounded too. The
readout satisfies `||w||_infty=omega` and
`||w||_2/sqrt(n)=omega<=Y=(s+1/2)omega`. Consequently these states
meet the deterministic small-label assumptions in the input notes,
after decreasing `omega` by a width-independent amount if necessary.

At (3), consider the direction

\[
 a_{W_1}=\sqrt n\,e_1,\qquad a_{W_2}=0,
 \qquad a_w=-\frac{\omega D A}{s}\boldsymbol1.
 \tag{5}
\]

Its hidden forward variations are
`h'_1=A sqrt(n)e_1`, `z'_2=A boldsymbol1`, and
`h'_2=DA boldsymbol1`. Thus

\[
 J a=\omega DA+s\left(-\omega DA/s\right)=0,
 \qquad
 \|a\|_{\rm mob}^2=1+(\omega DA/s)^2.
 \tag{6}
\]

This is a genuine tangent direction to the prediction level set, with
uniformly bounded norm. Since
`c_1=W_2^T delta_2=omega D sqrt(n)g` and
`phi''(-arctanh(p))=2pA`, formula (2) gives

\[
 D^2f[a,a]
   =2pA\omega D\sqrt n
       +\omega\phi''(c)A^2
       -\frac{2\omega D^2A^2}{s}.
 \tag{7}
\]

The three terms are respectively the first-layer gate, top-layer gate,
and readout cross term. For `L=r^2`,

\[
 D^2\mathcal L[a,a]=2(Ja)^2+2rD^2f[a,a]
   =-2pAD\omega^2\sqrt n+O(\omega^2).
\]

Because `DF` is the negative mobility Hessian of the loss,

\[
 \frac{\langle a,DF\,a\rangle_{\rm mob}}
      {\|a\|_{\rm mob}^2}
 =\frac{2pAD\omega^2\sqrt n+O(\omega^2)}
        {1+(\omega DA/s)^2}.
 \tag{8}
\]

Hence positive readout Gram and small fixed labels do not imply a
dimension-free one-sided Lipschitz constant, even on prediction-tangent
directions. The normal Gauss--Newton term vanishes exactly in (6).
This statement concerns instantaneous expansion; it alone says nothing
about its duration or the integrated gain of the actual comparison.

## 3. The old-clock defect reaches the exceptional coordinate

It would be insufficient to object that the direction (5) is an
arbitrary perturbation. At order `P=1`, the actual defect has a concrete
first nonzero derivative that reaches the same coordinate after one
application of the linearized field.

At `t=0`, the forward endpoint error is zero and the backward prefix
is zero. Since the order-one forward projected endpoint is its clock
average, differentiating it initially gives zero. Therefore the exact
defect identity from the manuscript gives

\[
 E_2(0)=0,\qquad
 e_2:=\dot E_2(0)=\frac{2r}{n}\delta_2\dot h_1^T.
 \tag{9}
\]

Let `D_1=diag(A,Q,...,Q)`. Equations (3)--(4) give

\[
 \dot h_1=\omega^2D\sqrt n\,D_1^2g,
 \qquad e_2=-\omega^4D^2u(D_1^2g)^T.
 \tag{10}
\]

Thus the structured forcing has uniformly bounded Frobenius norm
`O(omega^4)` and rank one. Put `e=(0,e_2,0)` and `V=DF(theta_0)e`.
If `C_h=(D_1^2g)^T h_1`, direct differentiation of
`F_1=-2r D_1 W_2^T delta_2` gives

\[
 V_{W_1,1}
 =\omega^6 A\left[-D^3\sqrt n\,A^2
                 +(2D^4-D^2\phi''(c))C_h\right].
 \tag{11}
\]

For verification, the three necessary directional changes are

\[
 e_2h_1=-\omega^4D^2 C_hu,\qquad
 Dr[e]=-\omega^5D^3C_h/\sqrt n,
\]
\[
 e_2^T\delta_2+W_2^T D\delta_2[e]
 =-\omega^5\left[D^3\sqrt n\,D_1^2g
                +D^2\phi''(c)C_hg\right].
\]

Substitution into
`DF_1[e]=-2 Dr[e] delta_1-2r D_1 D(W_2^T delta_2)[e]`
proves (11). Moreover

\[
 \frac{C_h}{\sqrt n}\longrightarrow cQ^2,
 \qquad
 \frac{V_{W_1,1}}{\omega^6\sqrt n}
 \longrightarrow AD^3[-A^2+2(D+s)cQ^2]\ne0.
 \tag{12}
\]

Indeed, the bracket is approximately `-0.4705`. All other
first-layer coordinates of `V` are `O(omega^6)`, its hidden matrix
block is `O(omega^6)` in Frobenius norm, and its readout is a constant
vector with entries `O(omega^5)`. These claims also follow from the
three displayed variations and the canonical flow equations; the
constants are independent of width.

For the actual closure-minus-dense parameter discrepancy `eta(t)`,
smoothness at the nonzero initial residual and `E_1=0` imply

\[
 \eta(0)=\dot\eta(0)=0,\quad \ddot\eta(0)=e,
 \qquad
 \eta_{W_1}(t)=\tfrac16V_{W_1}t^3+O_n(t^4).
 \tag{13}
\]

The remainder is only asserted at each fixed width. In particular,
the leading first-layer discrepancy is nonzero in the exceptional
neuron, with its natural normalized size independent of width.

For a precise normal/tangent interpretation, subtract from `V` the
readout-only vector whose entries are `(JV)/s`. Call the resulting
direction `T`. Then `JT=0`, `T_(W_1)=V_(W_1)` and
`T_(W_2)=V_(W_2)`. Its norm is bounded independently of width.
The first gate term in (2) for `T` is a positive constant times
`sqrt(n) omega^13`; all other terms stay bounded in width. To check
the latter, the other first-layer coordinates are bounded, the
corresponding carriers are bounded, `z'_2` has bounded coordinates
(all upper-layer quantities are multiples of `boldsymbol1` or
rank-one matrices with left vector `u`), and the remaining terms in
(2) obey Cauchy--Schwarz. Thus this tangent component of a direction
generated by the structured forcing also has an unbounded positive
one-sided gain for fixed `omega`.

This last construction uses a readout right inverse to split normal
and tangent directions. It does not assert that `T` itself is an
actual parameter discrepancy or that it is an orthogonal projection.
The exact trajectory statement is (13).

## 4. What remains necessary

Equations (8) and (13) exclude two shortcuts: a uniform tangent
Hessian bound from Gram coercivity, and an assumption that the
old-clock product defect never excites a large-carrier coordinate.
They do not exclude cancellation over time, a better state-dependent
comparison metric, or a Gaussian estimate for the actual reachable
directions.

A scalar uncoupled equation illustrates why instantaneous expansion
is not the final question. If `dot z=a(t) phi'(z)` with externally
fixed `a(t)`, its homogeneous linearized solution obeys exactly

\[
 v(t)=v(0)\frac{\phi'(z(t))}{\phi'(z(0))}.
 \tag{14}
\]

Differentiate the ratio to verify (14); tanh has strictly positive
derivative at every finite point. Large instantaneous curvature can
therefore have a short duration. For the network, however, the
coefficient itself changes with the other neurons, samples and
layers, and the first-layer preactivation derivative contains the
sample input Gram. The uncoupled cancellation does not give an
integrated bound for that coupled linearized system.

The Gaussian task still needs a proved estimate for these coupled,
trained carrier-weighted directions, or an exact metric cancellation
that handles their coupling and the actual defect. None of the
identities here gives the missing estimate (24) or (25) of
`SMALL_LABEL_ENERGY.md`. No independence of trained responses from
initialized matrices, no normality of the defect, and no favorable
sign of the residual-weighted gate curvature may be inserted at this
step.
