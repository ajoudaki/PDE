# Internal check of the single-input dynamics route

Checked 2026-09-20. Frozen input: complete `ROUTE_DYNAMICS.md`, SHA-256
`f84da8b5a840079a239ae8b2ffd4c12359f8abab08f27d831e0534f2ac2fa755`.
The complete file was read after the dictionary route was written. This is a
scoped internal proof check, not a promotion review or independent authorship
of the combined rate theorem. No route file was edited.

Conclusion: the all-physical-time transfer and the constants in equations
(15)-(29) pass this internal check. No blocking mathematical error was found.
The route correctly leaves quantitative H3 source production to a separate
lemma. Its all-time claim concerns closure order, not a uniform all-time
finite-neural-width theorem.

## Checks that could have invalidated the upgrade

1. **Physical clocks near fitting.** A finite-feature-interval comparison need
   not by itself control arbitrarily long physical time. Here the remedy is
   valid: the exact feature training function has derivative at least m_*>0
   throughout [0,S], even beyond its own fitting endpoint. Therefore the
   subtraction at the two clocks gives a *negative* term
   -2m_*|s_N-s|. This yields the uniform bound epsilon/m_* without multiplying
   it by physical time. The use of b(s_N) is legitimate because the exact
   feature flow is defined past its endpoint. At a zero clock difference,
   its upper right norm derivative is bounded by 2epsilon, so no division by
   the clock difference is hidden.

2. **Lower bound on the training feature slope.** The c-norm argument was
   rederived. Since c_s=h and the hidden velocity is J*c, differentiation
   gives c_ss=JJ*c; there is no missing derivative-of-J term because h,
   rather than J*c, is differentiated. For g=||c||>0,

       g''=[||h||^2-(g')^2+||J*c||^2]/g >=0.

   Cauchy-Schwarz gives |g'|<=||h||. The initialization expansion gives
   g'(0+)=sqrt(m_*), so g>=s sqrt(m_*) prevents a later zero and extends
   convexity to all positive s. Hence ||h||>=sqrt(m_*) and b_s>=m_* globally.
   This does not assume hidden linearity, small motion, or trained Gaussian
   answers. The argument remains valid for the closure only in its specified
   row-L2 plus *matrix-coefficient Frobenius* hidden metric; the route uses
   exactly that metric.

3. **Ridge filters and the gradient metric.** The closure middle derivative
   is U2*(delta) times U1*(H) transpose in coefficient space. Its pushforward
   is Q2(delta tensor H)Q1. The Gram contractions are positive contractions,
   not orthogonal projections; neither idempotence nor an HS-gradient
   interpretation of this filtered increment is used. The fitting identity
   uses ||M_s||F^2, which is the correct term. Its norm dominates the HS
   increment speed as needed for the uniform raw bounds.

4. **Linear stability constants.** Let dX,dK,dc denote component distances
   and D=dX+dK+dc. With B>=2,

       ||Z_N-Z|| <= B dX+dK+rho <= B D+rho,
       ||delta_N-delta|| <= (1+2SB)D+2S rho.

   Thus the apparent absence of a separate '+1' in the forward coefficient
   is correct: the K and X errors are separate summands of D. Adding the
   three derivative bounds gives precisely

       C_D=2B+1+2S(B^2+B+1),
       C_rho=2S(B+1)+3.

   This validates the displayed E_S and P_S, with zero initial transformed
   error. Both action orientations are included among the three source
   defects; the initial action is never assumed close in operator norm.

5. **Passive whole-circle observations.** Since w=(j(X,g1),g2), the fixed
   second Gaussian coordinate cancels in comparisons, and
   ||w_N-w||2<=||X_N-X||2. For every unit u, the prediction's raw gradient
   block norms are bounded by BS,S,1, as are the exact training feature
   velocity block norms. Their Hilbert product pairing is at most
   V_S^2=1+S^2(B^2+1). This verifies the uniform passive time modulus and
   therefore the factor 1+V_S^2/m_* in the same-physical-time estimate.

6. **Fitting endpoint inclusion.** The squared-norm difference at time zero
   is at most 2||(B_N-A0)tanh g1||2, because both upper hidden fields are
   bounded by one in L2 and tanh is 1-Lipschitz. With rho<=1/100 and
   m_*>1/5, m_N>9/50, hence its endpoint is below 50/9<6. The exact endpoint
   is below 5. This proves the clock estimate's endpoint premise rather
   than assuming it.

7. **Numerical constants and factor of two.** At S=6 the stated values are

       B=20,
       C_D=41+12(400+20+1)=5093,
       C_rho=12*21+3=255,
       V_S^2=1+36*401=14437,
       1+5 V_S^2=72186.

   Thus equations (28)-(29) have the correct constants. The normalized
   one-atom datum uses the unhalved squared loss, so its physical residual
   factor is 2(1-f). Its initial feature kernel is m_*, not the opposite-
   label two-atom reference's m_*/2.

## Maintained dependency verification

The relevant B.1 theorem, scalar-coordinate proof, global existence argument,
and initialized-action/width identification portion were read. Its one-input
Gram hypothesis, activation regularity assumptions, and vanishing stored
readout regime apply here. Its displacement formulation specifically avoids
requiring a square-integrable F(g). The transformed argument in the route is
consistent with that maintained result and preserves its physical loss factor.

The complete rational certificate in C.4.5.1 part 5 was read, along with the
definition q=E tanh^2 G, v=E tanh^2(sqrt(q)G), m=v/2. The certificate proves
q>0.39 and a lower bound for v exceeding 1/5, via a conservative input
scale 0.624 whose square is below 0.39. Thus m_*=v>1/5 is the right single-
input deduction. This was a source check; the rational program was not rerun.

## Scope of the conclusion

The route proves a valid all-time stability mechanism once rho_N(6) is
quantitatively small. Its qualitative strong-projection argument alone does
not assign a numerical order. That distinction is explicit in the frozen
file, and the dictionary route must supply its own audited quantitative
source estimate before a combined unconditional order-to-error theorem is
asserted. The displayed endpoint and whole-circle claims do not assert
operator-norm recovery of A0, practical constants, monotone finite-order
errors, finite-dimensional exact closure, or all-time uniform neural-width
convergence.
