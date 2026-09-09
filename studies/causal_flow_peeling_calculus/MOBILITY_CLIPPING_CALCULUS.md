# Mobility--Clipping Completion Calculus

## Claim level

This note records the first successful nonlinear completion mechanism.  It is a reusable collection of typed rules, not a universal Banach algebra.  The rules rigorously close the two-hidden-layer arctangent rung when combined with the fixed-finite-program MFP theorem.  Their depth recursion stops at one explicit missing tail-propagation rule, analyzed below.

## 1. Typed objects

The calculus distinguishes:

- `B`: coordinatewise bounded fields, with a deterministic bound;
- `E`: energy fields in normalized `l^2`;
- `S_xi(C)`: seed-dominated fields satisfying
  \[
  |v_i(t)|\le |\xi_i|+C_T
  \]
  for an iid seed `xi` with a certified tail;
- `O`: operators with a dimension-free operator norm;
- `N`: normalized contractions and rank-one/nuclear morphisms.

The allowed deterministic products are

\[
B\odot E\to E,
\qquad
E\times E\to N,
\qquad
N(E,E)\to O.
\]

There is no `E odot E -> E` rule.

## 2. Mobility flattening

Suppose a coordinate state has the gradient form

\[
\dot u=m(u)q,
\qquad m(u)>0.
\]

Define the mobility coordinate

\[
\Phi(u)=\int_0^u\frac{ds}{m(s)},
\qquad w=\Phi(u).
\tag{1}
\]

Then, exactly,

\[
\dot w=q.
\tag{2}
\]

This rule removes the unstable difference product

\[
[m(u)-m(\widetilde u)]\widetilde q.
\]

It is admissible when `Phi` is a global diffeomorphism and the required forward map expressed in `w` is globally controlled.  For arctangent,

\[
m(u)=\frac1{1+u^2},
\qquad
\Phi(u)=u+\frac{u^3}{3}.
\]

If `psi=Phi^{-1}` and

\[
\chi(w)=\arctan(\psi(w)),
\]

then

\[
0<\psi'(w)=m(\psi(w))\le1,
\qquad
0<\chi'(w)=m(\psi(w))^2\le1,
\]

and `chi` is bounded by `pi/2`.  All derivatives of `psi` and `chi` have polynomial growth, in fact they are bounded after the low orders needed here, so they remain admissible fixed-program unary nodes.

## 3. Seed-tail clipping

Suppose an otherwise bounded network grammar contains

\[
b=v\odot m(z),
\tag{3}
\]

where `m` is bounded and Lipschitz but `v` is an `S_xi(C)` multiplier.  Let `kappa_R` be a smooth one-Lipschitz clipping map equal to the identity on `[-R,R]` and bounded by `R+1`.  Define

\[
b_R=\kappa_R(v)\odot m(z).
\]

For fixed `R`, (3) is a dimension-free Lipschitz operation in normalized energy.  If

\[
\tau_{n,S}(\xi)
=\left[
\frac1n\sum_i(|\xi_i|-S)_+^2
\right]^{1/2},
\]

then seed domination gives

\[
\|v-\kappa_R(v)\|_n
\lesssim \tau_{n,R-C_T}(\xi),
\tag{4}
\]

with an immaterial unit adjustment for smooth clipping.

If the clipped state vector field has Lipschitz constant

\[
L_R\le L_0+L_1R,
\]

then Gronwall gives an unclipping error bounded by

\[
C_Te^{L_RT}\tau_{n,R-C_T}(\xi).
\tag{5}
\]

For a standard Gaussian seed and `p>=2`,

\[
\mathbb E\tau_{n,S}^p
\le
\mathbb E(|Z|-S)_+^p
\le
\frac{2\Gamma(p+1)\varphi(S)}{S^{p+1}}.
\tag{6}
\]

The quadratic Gaussian exponent in (6) beats the linear stability loss in (5), uniformly in width.  Thus the clipped flow converges to the original flow in compact-time `L^p` after `R -> infinity`.

This is stronger than an informal “tail truncation”: it records the exact competition between the stability loss and the tail exponent.

## 4. Persistent-source finite-history expansion

Write a trained edge as

\[
G(t)=\Gamma+H(t),
\qquad
\dot H=b\otimes_nx.
\]

At Euler times `t_j=jh`, exactly

\[
H_j=h\sum_{s<j}b_s\otimes_nx_s,
\]

and therefore

\[
G_jx_j
=\Gamma x_j
+h\sum_{s<j}b_s\langle x_s,x_j\rangle_n,
\tag{7}
\]

\[
G_j^*b_j
=\Gamma^*b_j
+h\sum_{s<j}x_s\langle b_s,b_j\rangle_n.
\tag{8}
\]

Equations (7)--(8) are a finite causal program using one persistent source and its exact transpose.  They do not freshen the matrix and require no inverse Gram matrix.

For every fixed clip `R` and step count `N`, MFP's fixed-program theorem evaluates this history, including all response corrections.

## 5. Lipschitz finite-program completion rule

Let `X_R` be a clipped flow in a width-dependent Banach state space.  On a localization event, suppose

\[
\|F_R(X)-F_R(\widetilde X)\|\le L_R\|X-\widetilde X\|,
\qquad
\|F_R(X)\|\le M_R,
\]

with constants independent of width.  The Euler interpolation with `N` steps then satisfies

\[
\sup_{t\le T}\|X_R(t)-X_{R,N}(t)\|
\le
\frac{M_RT}{2N}(e^{L_RT}-1).
\tag{9}
\]

Fixed `(R,N)` is evaluated by MFP.  First take width to infinity, then `N -> infinity`, then remove `R` using (5)--(6), and finally remove the localization.  The resulting character is unique because two candidate limits can be compared through the same clipped Euler approximants.

The order is important.  No theorem constant is required to be uniform in a growing program length.

## 6. Autonomous limiting state

For every fixed `(R,N)`, retain the joint typed character of:

- the immutable source and its transpose orientation;
- the current `A,w,H` fields;
- the derived forward/backward fields;
- every closed observable needed by the predictor and kernel.

The uniform completion makes these characters Cauchy.  Their projective limit is a positive character on the completed typed algebra.  Current fields plus the fixed source generator form the state.  The full query history is not retained: equations (7)--(8) are an implementation of a finite step, while the completed learned operator `H(t)` is a current morphism.

Restarting from a current character and applying the same clipped Euler approximation gives the same limit as continuing from zero, because this equality holds at finite width and the approximation is uniform.  Hence the state is autonomous and satisfies the semigroup law.

This state is infinite-dimensional but has finitely many types and computably convergent approximations, satisfying the program contract.

## 7. Why the rule is depth-sensitive

At `L=2`, the only unbounded multiplier in a gate product after mobility flattening is the top readout:

\[
b_2=A\odot\phi'(z_2).
\]

It is seed-dominated because `A'=phi(z_2)` is bounded.  Rule (3)--(6) applies directly.

At `L=3`, the hidden backpropagated product is

\[
b_2=r_2\odot\phi'(z_2),
\qquad
r_2=G_2^*b_3.
\]

The multiplier `r_2` is not seed-dominated by a coordinatewise deterministic inequality.  Mobility flattening the bottom `u` does not remove it.  Attempting to flatten the derived `z_2` gives

\[
\frac d{dt}\Phi(z_2)
=\|x_1\|_n^2r_2
+\phi'(z_2)^{-1}G_1\dot x_1,
\]

and the moving-input term acquires the unbounded factor `1+z_2^2`.

Thus the next reusable block must be a **reachable-tail propagation rule**:

> if `b` belongs to the certified network grammar, prove a tail strong enough for `Gamma^*b` and its stability/tangent fields that clipping `r=G^*b` has a vanishing error after the linear-in-`R` stability loss.

This is a real reduction in form: all finite-history Gaussian semantics, time discretization, nonlinear bottom mobility, and deterministic stability are already discharged.  It is not yet a proof of that tail rule.
