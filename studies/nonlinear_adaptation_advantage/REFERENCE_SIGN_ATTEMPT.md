# Reference-specific sign attempt

**Outcome: no sign proved.** On the actually reached two-anchor reference,
the disputed numerator has a five-term decomposition involving task/reference
cross-pairings and two explicit tanh curvature terms. The reference's positive
readout acceleration does not make those cross-pairings positive or bound them
by the required energy. The available absolute estimates provably do not
yield a coefficient below one. The endpoint cubic has an equally explicit
task-versus-reference-history representation with no established sign.

This is a bounded analytic attempt on the unchanged family (G1)–(G3) from
`ROUTE_GEOMETRY.md`. It introduces no family and performs no experiment.
The symmetric residual below is solely the previously authorized diagnostic;
it is not a proposed target constructed around the trained predictor.

## 1. Use the actual reference history

Retain the exact first-row and middle hidden state `x_h=(w,K)`, actual
initialized action and adjoint, and upper feature `H_u(x_h)`. Define

\[
h(x_h)=\frac{H_{e_1}(x_h)-H_{e_2}(x_h)}2,
\quad B(x_h,c)=\langle c,h(x_h)\rangle,
\quad J=Dh.
\]

Here `Dh` denotes the strong hidden directional map of C.4.5.1 R2. The
actual reference feature clock obeys

\[
c_s=h(x_h(s)),\qquad (x_h)_s=J(s)^*c(s),\qquad
c_{ss}=J(s)J(s)^*c(s),\qquad
B_s=\|h(s)\|^2+\|J(s)^*c(s)\|^2\ge m_0=1/10. \tag{R1}
\]

Its initial readout is the limiting zero readout, and therefore the actual
reached endpoint satisfies the history identity

\[
c_\dagger=\int_0^{s_\dagger}h(s)\,ds,
\qquad B(\theta_\dagger)=1,\qquad 0<s_\dagger\le10. \tag{R2}
\]

These statements are used for the actual reference, not imposed at an
arbitrary tanh state. The retained finite random readout and original-start
physical interpretation remain those of the contract.

At the endpoint fix the actual residual `r=F_*-q`, density `p`, and effective
signed force measure

\[
\mu=r p\rho-\sum_a\beta_a\delta_{e_a},\qquad
\beta=M^{-1}G^*\int r(u)g(u)p(u)d\rho(u).
\]

For scalar differentiation hold this measure fixed, and put

\[
k(x_h)=\int H_u(x_h)d\mu(u),\quad U=Dk,\quad
b=\nabla\langle c,k\rangle=(U^*c,k),\quad
g_B=(J^*c,h). \tag{R3}
\]

The `b` here is exactly the fully projected task force, because the signed
anchor subtraction is part of `mu`. In particular none of the following
expressions discards the first row, changes the actual adjoint, or makes a
readout-only comparison.

For hidden directions `v,z`, define the scalar bilinear form
`L_mu(v,z)` as the second hidden derivative of `<c,k(x_h)>`, with `c` fixed.
Define `L_B` similarly for `<c,h(x_h)>`. These are scalar paired derivatives,
not asserted second derivatives of an L2-valued feature map. They exist for
the directions below by the L4 row and bounded-readout conditions proved in
the frozen reports. Their exact integrands are the hidden terms of (G12).

## 2. The actual reference numerator has five terms

Let

\[
N_\mu=H_\mu[b,g_B]+H_B[b,b], \tag{R4}
\]

the numerator in the pure-symmetric readout identity (B11) of the preceding
follow-up. Expanding the readout-linear scalar functions in (R3) gives

\[
\begin{aligned}
N_\mu={}&\langle U^*k,J^*c\rangle
       +\langle U^*h,U^*c\rangle
       +2\langle J^*k,U^*c\rangle\\
 &+L_\mu(U^*c,J^*c)+L_B(U^*c,U^*c). \tag{R5}
\end{aligned}
\]

For verification, the mixed Hessian of `<c,k(x_h)>` on directions
`(v,a)` and `(z,d)` is
`<a,Uz>+<d,Uv>+L_mu(v,z)`. Substitute `(v,a)=(U*c,k)` and
`(z,d)=(J*c,h)`. The Hessian of `<c,h>` on `b,b` is
`2<k,J U*c>+L_B(U*c,U*c)`. Actual adjunction gives (R5).

This formula isolates what reference reachability adds. For example, its
second term is exactly

\[
\langle U_\dagger^*h_\dagger,U_\dagger^*c_\dagger\rangle
=\int_0^{s_\dagger}
 \langle U_\dagger^*h_\dagger,U_\dagger^*h(s)\rangle\,ds. \tag{R6}
\]

It is a pairing of the endpoint and earlier reference feature increments
after a task-specific operator. It is not a square. The first and third
terms of (R5) are two different task/reference operator cross-pairings.
The remaining two are explicit scalar tanh curvature integrals. The positive
operator `J(s)J(s)*` in (R1) does not identify any of them with a nonnegative
quantity, or give the upper bound needed for coercivity.

There is an exact way to expose the history discrepancy in (R6). Integrating
`h_s=J J*c` by parts in (R2) yields

\[
c_\dagger=s_\dagger h_\dagger
               -\int_0^{s_\dagger}s J(s)J(s)^*c(s)\,ds.
\]

Consequently (R6) is

\[
s_\dagger\|U_\dagger^*h_\dagger\|^2
-\int_0^{s_\dagger}s\,
 \langle U_\dagger^*h_\dagger,
         U_\dagger^*J(s)J(s)^*c(s)\rangle\,ds. \tag{R7}
\]

The second integral is of the same reference history as the positive term;
it has neither an independently small factor nor a proved favorable sign.
All differentiations and integrations here use only the strong second
readout derivative already established in C.4.5.1; no third derivative or
new Taylor radius is assumed.

The exact reference balance can therefore replace an unknown endpoint
readout by its actual history, but this replacement does not close a sign
estimate. A new statement controlling the task-weighted cross-time
correlations in (R6)–(R7) would be substantive additional information.

## 3. Why the established absolute estimates cannot certify coercivity

This subsection checks the available quantitative route, rather than merely
noting that (R5) contains terms of both signs. Use the reference constants

\[
C=\sqrt{10},\quad M=2+\sqrt{10},\quad H=10,
\quad L_h=\sqrt{1+M^2},\quad L_0^2=1+C^2 L_h^2,
\quad q_4\ge\sup_u\|Q_\dagger(u)\|_4.
\]

Write `S=||mu||TV`, `R_0=||r||p`, and `k_A=lambda_min(M_dagger)>0`.
The actual endpoint estimates give

\[
\|U\|\le S L_h,\quad \|J\|\le L_h,\quad
\|k\|\le S,\quad \|h\|\le1,
\quad S\le S_0R_0,
\quad S_0=1+\sqrt2L_0/\sqrt{k_A}. \tag{R8}
\]

For a hidden direction `v`, let
`Z_v=v_K H1+A[phi'(w.u)(v_w.u)]`. Then
`||Z_v||2<=L_h||v||h`. Subtracting the two hidden differentiations in (G12)
and using `|phi''|<=2` yields

\[
|L_\mu(v,z)|\le S\left[
(2H L_h^2+C)\|v\|_h\|z\|_h
                +2MC\|v_w\|_4\|z_w\|_4\right]. \tag{R9}
\]

The upper curvature product uses the bounded readout and two L2 vectors.
The mixed middle/row terms are bounded by
`C(||v_K||||z_w||2+||z_K||||v_w||2)<=C||v||h||z||h`.
The remaining lower curvature term uses actual adjunction and the two L4
row directions. Thus (R9) makes no unproved Lp estimate for the action.
For `L_B`, replace the total variation factor by one.

From (R3) and the actual gradient formula,

\[
\|U^*c\|_h\le S L_h C,\quad
\|J^*c\|_h\le L_h C,\quad
\|(U^*c)_w\|_4\le S q_4,\quad
\|(J^*c)_w\|_4\le q_4.
\]

Apply these estimates to each of the five terms in (R5). The first three
cost at most `4S² L_h² C`; the two curvature terms together cost at most
`2S²(2H L_h²+C)L_h² C²+4S²MC q_4²`. Hence

\[
|N_\mu|\le S^2 C_{\rm abs},\quad
C_{\rm abs}=4L_h^2C+2(2H L_h^2+C)L_h^2C^2+4MCq_4^2. \tag{R10}
\]

Define `lambda=||b||²/R_0²`, which is positive on the full fixed G family
by its proved nonstationarity and full-gradient injectivity. It is at most
`L_0²`. Equations (R1), (R8), and (R10) only certify

\[
\frac{|N_\mu|}{B_s\|b\|^2}
\le\frac{S_0^2 C_{\rm abs}}{m_0\lambda}. \tag{R11}
\]

This particular bound is necessarily larger than one even under the most
favorable `S_0>=1` and `lambda<=L_0²`:

\[
\frac{S_0^2 C_{\rm abs}}{m_0\lambda}
\ge\frac{4L_h^2C}{(1+10L_h^2)/10}
=\frac{4C}{1+1/(10L_h^2)}>\frac{120}{11}>1. \tag{R12}
\]

The strict inequality uses `C>3` and `L_h²>1`. Thus the known absolute
reference estimates cannot certify
`N_mu <= (1-eta) B_s ||b||²` with any positive `eta`. This is a statement
about the displayed proof bounds, not a lower bound on the actual ratio.
The actual numerator could be negative or substantially smaller; deciding
that requires signed information beyond (R1) and the source-norm bounds.

There is also a short exact check of the logical gap in using readout
convexity alone. Consider, solely as a test of that inference, the readout
equation `c''=diag(0,1)c`, with `c(0)=0,c'(0)=(1,1)`. Then
`c(s)=(s,sinh s)` and `c'(s)=(1,cosh s)`. For fixed `s>0` choose

\[
\frac1{\cosh s}<a<\frac{s}{\sinh s},\qquad v=(1,-a).
\]

The interval is nonempty because `tanh s<s`, proved by integrating
`sech² t<1` from zero. Nevertheless
`(v dot c(s))(v dot c'(s))<0`. So even a constant positive semidefinite
readout acceleration operator does not force a nonnegative task-projected
cross-pairing. This is not a tanh state, not an E₀ counterexample, and not
a replacement for (R5): it verifies exactly why positivity in (R1) alone
cannot justify the missing inference in (R6).

## 4. The actual endpoint cubic has a reference-history form

Readout linearity also gives the exact actual-neural cubic

\[
\mathcal C_p(r)
=2\langle U^*k,U^*c_\dagger\rangle
                         +L_\mu(U^*c_\dagger,U^*c_\dagger). \tag{R13}
\]

Indeed `C_p(r)=H_mu[b,b]`, as proved in (G13)–(G14), and (R3) supplies its
two readout/hidden cross terms and its fixed-readout hidden Hessian. Inserting
the actual reference history (R2) makes its first term

\[
2\int_0^{s_\dagger}
       \langle U_\dagger^*k_\dagger,U_\dagger^*h(s)\rangle\,ds. \tag{R14}
\]

The second term is an explicitly signed tanh curvature integral with the
same effective task and anchor weights. Neither term is a square or is
controlled by the scalar fact `B(theta_dagger)=1`. The task field `k` differs
from both the readout `c` and the anchor feature contrast `h`; setting any
two of them equal would change the scientific object.

For the pure symmetric diagnostic the cubic cancellation follows from the
actual reference symmetry, not from a sign in (R13). On G's uniform-density
slice, the actual residual still has its antisymmetric baseline
`r_A=F_*-q_0` plus the antisymmetric coefficient perturbations. The exact
decomposition remains
`C_1(r_A+r_S)=c(r_A,r_A,r_A)+3c(r_A,r_S,r_S)`.
Equations (R13)–(R14) do not give the sign of either term. Small target
coefficient radius does not make the fixed baseline negligible. General
allowed density perturbations also remove the exact symmetry cancellation.

Thus this attempt reaches a concrete certificate target for the supervisor:
the signed full-family contractions in (R13), or the five terms in (R5) if
the proposed readout coercivity is pursued. It does not establish a favorable
margin on a single witness, on the whole box, or on its robustness neighborhood.

## 5. Scope, checks, and terminal status

The actual-reference identities used here are C.4.5.1 R2–R19, together with
the complete C.4.9–C.4.10 source/gradient/projection facts already read in
the original route. No additional scientific file or other route was read.
The two prior frozen reports remain unchanged:

* `ROUTE_GEOMETRY.md` — SHA-256
  `e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04`;
* `GEOMETRY_SIGN_FOLLOWUP.md` — SHA-256
  `7400b12eb9655a24f8ba23af2fd41b60733947ca5fc184850d2629eafd980719`.

At this attempt's startup the contract, workflow, and
`docs/global_nonlinear.md` hashes were unchanged from the original route's
source manifest. The metadata-only HEAD was
`88172930b86b57f302ae53d0ae28c8bcc33838e4`; the shared index was empty.
Only this assigned file was written. No Git mutation or experiment occurred.

Author checks: expand the scalar readout-linear Hessian in two ways to verify
all five terms in (R5); substitute the exact history integral to obtain
(R6)–(R7); verify each factor norm and the mixed row/middle inequality in
(R9); verify the lower bound on the *bound* in (R12), without confusing it
with the unknown actual ratio; and recover the original cubic by (R13).
No higher population derivative or independent review is claimed.

The specific coercivity cannot be deduced from the presently proved
reference readout balance, fitting level, and absolute source estimates by
these arguments. A stronger neural relation among the actual task/reference
operators could still exist; it has not been proved or disproved. The
smallest unresolved signed quantities are explicitly (R5) and (R13), with
their task/reference-history form (R6),(R14). E₀ remains unresolved.
