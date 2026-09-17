# Post-freeze algebra check: regular potential and reflection contrast gain

2026-09-16. Scope: the two additions requested by the supervisor. I read
`antipodal_upgrade_check.md` for the exact normalized coefficient
involutions. This is an author-side algebra check, not a fresh isolated
review. No research branch, experiment, or edit to a frozen file was made.

**Conclusion:** both additions are correct under the stated hypotheses.
The first gives a current-state potential regular at zero readout. The
second proves strict initial hidden-gradient activity for every actual
signed-permutation reflection with positive initialized contrast,
including the diagonal reflections, without any independence assertion
after a change of coefficient basis.

## 1. Regular current-state potential

Use the already checked scalar flow and notation

\[
 F=\langle c,U(h)\rangle,\quad q=\|c\|^2,\quad
 C=\|U\|^2,\quad K=\|\operatorname{grad}F\|^2,
 \qquad F_s=K,\quad q_s=2F.
\]

Assume the previously proved initialized-path estimate C>=C_0>0.
Then K>=C_0 and F^2<=qC<=qK. Define, using the fixed initialized number
C_0,

\[
                 \Phi(X)=\frac{1+q(X)}{C_0+F(X)^2}.
\]

Direct differentiation gives

\[
 \begin{aligned}
 \Phi_s
 &=\frac{2F(C_0+F^2)-2F(1+q)K}{(C_0+F^2)^2}\\
 &=-\frac{2F\{(qK-F^2)+(K-C_0)\}}{(C_0+F^2)^2}\le0.
 \end{aligned}                                               \tag{1}
\]

The inequality holds along the reached feature trajectory, where F>=0.
Both bracketed terms are nonnegative. Equivalently their sum is

\[
 (qC-F^2)+(1+q)\|\operatorname{grad}_hF\|^2+(C-C_0)\ge0.
\]

The denominator is everywhere at least C_0, so Phi has no readout-origin
singularity and Phi(X_0)=1/C_0. It is differentiable in the characteristic
state class; only q and the already used differentiable prediction
functional F enter it.

For labels +A,-A, the physical clock is s_t=2(A-F), and therefore

\[
 \Phi_t=-\frac{4F(A-F)\{(qK-F^2)+(K-C_0)\}}
                       {(C_0+F^2)^2}\le0.              \tag{2}
\]

Here the physical solution has 0<=F<A at finite time, as already proved.
No monotonicity claim for arbitrary ambient states with F<0 or F>A is
implied. Also, this regular potential uses the previously established
barrier C>=C_0; its sign calculation does not by itself replace the proof
of that barrier. With that dependency stated, the addition is valid.

## 2. A coefficient variation for any actual reflection symmetry

Let O_1,O_2 be the actual normalized coefficient transformations induced
by a signed-permutation input reflection. The checked initialization
symmetry has

\[
 O_\ell^TO_\ell=I,\qquad O_\ell^2=I.
\]

Consequently O_ell^T=O_ell. At a fixed state of the corresponding
symmetry, with the lower state held fixed,

\[
 a_-=O_1a_+,\qquad M=O_2MO_1,
 \qquad MO_1=O_2M.
\]

Writing the fixed upper mark column as b_2, the two preactivations are

\[
 z_+=b_2^TMa_+,\qquad
 z_-=b_2^TMa_-=b_2^TO_2Ma_+.
\]

Let P_-=(I-O_2)/2, an orthogonal projection, and take the allowed
coefficient variation

\[
                         \delta M=P_-M.
\]

It even preserves the matrix symmetry subspace, since
O_2(delta M)O_1=delta M. Indeed O_2 P_-=-P_- and
P_-O_2=-P_-. Holding the lower state fixed gives

\[
 \delta z_+=b_2^TP_-Ma_+=\frac{z_+-z_-}{2},
\]
\[
 \delta z_-=b_2^TP_-MO_1a_+
           =b_2^TP_-O_2Ma_+=-\delta z_+.                 \tag{3}
\]

For U=(phi(z_+)-phi(z_-))/2 and C=E_2U^2, equation (3) yields

\[
 \delta C
 =E_2\!\left[U\frac{z_+-z_-}{2}
                   \{\phi'(z_+)+\phi'(z_-)\}\right].   \tag{4}
\]

There is no missing factor of two: delta U equals
delta z_+(phi'(z_+)+phi'(z_-))/2, and delta C=2E U delta U.

For phi=tanh, U has the sign of z_+-z_-, and both derivatives in braces
are strictly positive at finite preactivations. Thus the integrand in
(4) is nonnegative everywhere and positive wherever U!=0. If C_0>0 at
initialization, that event has positive probability, giving

\[
               \delta C(X_0)>0,
 \qquad       \operatorname{grad}_h C(h_0)\ne0.         \tag{5}
\]

Bounded marks and finite initialized M justify differentiation and
integration. The physical Frobenius metric is unchanged; delta M is an
ordinary coefficient variation in that same metric.

## Consequence and scope

Equation (5) is exactly the premise used in the checked strict-gain
addendum: h_s=(s/2)grad_h C(h_0)+o(s), so the singular normalized ratio
q/F^2 decreases strictly on an initial interval and stays nonincreasing
thereafter. Its fitting endpoint therefore satisfies C_infty>C_0.
Replacing the coordinate-axis row scaling by (3) extends that argument
to the diagonal signed-permutation reflections as requested.

This computation needs only the actual orthogonal involutions and
positive initialized contrast. It does not diagonalize a mark law or
assume independence of transformed marks. It also supplies no new
symmetry for a generic rotated pair: O_1 and O_2 must arise from the
verified dictionary symmetry.
