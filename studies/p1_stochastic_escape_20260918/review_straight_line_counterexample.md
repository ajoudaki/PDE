# Informed internal review of the straight-line counterexample

2026-09-19. Reviewer: the scoped `cubic_order_check` route. This report reviews
the complete frozen 532-line candidate `straight_line_geometry_attempt.md`.

## Corrections and clarifications before the verdict

1. **State the physical input normalization explicitly.** Candidate lines
   29, 66, and 518 describe unit or normalized inputs but never state the
   relation to the physical inputs of the canonical model. Insert after
   equation (1): “The physical samples are x_a=sqrt(3)u_a; consequently
   x_a dot x_a/3=1 and their first-layer arguments are w dot u_a.”
   In the opening claim, “unit inputs” should say “unit normalized input
   directions.” All subsequent calculations use exactly this convention.
   Taking the displayed u_a as physical x_a without that scaling would
   change the claimed canonical preactivations.

2. **Identify (25) as directional, not a Fréchet Hilbert Hessian.** The
   frozen candidate does not explicitly assert a Fréchet state Hessian,
   but its discussion at lines 506--510 should make the stronger distinction
   explicit. Formula (25) is a bounded quadratic form giving every fixed
   direction's coefficient. There is no uniform second-order Fréchet Taylor
   expansion of the loss at this state in the physical L2 topology, and
   hence no Fréchet Hessian there. The direct descent construction proves
   this; a complete verification is given in Section 6 below. The finite
   input-space Hessians of R at e_1 and e_2 are ordinary genuine Hessians.

3. **Complete the noncoercivity justification.** Essential infimum zero
   of the multiplier alone does not, for an arbitrary sum, rule out
   coercivity of an added nonnegative term. In this case the added term is
   a finite sum of squared bounded linear functionals, and noncoercivity
   follows directly from the explicit normalized directions in Section 6.
   This is a short explanatory completion, not an obstruction to the
   counterexample.

**Verdict: the counterexample's mathematical construction and all fixed-line
and nearby-descent claims pass this informed internal check, with the
normalization and differentiability clarifications above.** No failed
interpolation condition, retained-feature cancellation, gradient identity,
or fixed-direction expansion was found. The proof does not rely on its
referenced earlier route. The optional balanced-weight extension supplied
by the supervisor is also valid, as checked separately in Section 7.

## Provenance, coverage, and limits

This is not a fresh isolated review or a promotion review. Earlier in this
same study I derived the collapsed-state cubic criterion and fifth-order
counterexample and then performed an informed internal review of a
no-bad-local-minima proof, including its real-label and sign-class extension.
I retain that prior context. The current review did not read or use the
candidate author's referenced `general_bad_geometry_route.md`, another
reviewer's findings, another study, or any additional scientific source.

The complete current candidate was read, including its provenance, all
proofs, final scope claims, and every correction-sensitive passage. The
canonical model and notation were previously read completely in this
context and have unchanged hashes. Required mathematical/research skills
and current shared instructions were applied. No experiment, computation
of a determinant or data coordinates, external source retrieval, or Git
write was performed. Tool use read the candidate, checked hashes and line
numbers, and inspected path/index metadata. Only this review file is written.

| Scientific input | SHA-256 |
| --- | --- |
| `straight_line_geometry_attempt.md` | `51279663fe402d16e979b9fa9af646453ac307707563f501c164f89ee9a703ec` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The optional 13-function extension was supplied in the supervisor's prompt;
it is not part of the frozen 12-function candidate. No revised lead candidate
is implicitly covered by this review.

## 1. Independence and the finite determinant prescription

The substitution of `x rho^2=x-xt^2-xs^2` and its x^3 counterpart is an
invertible constant transformation of the twelve generators. Thus checking
equation (14) suffices. All its coefficients are degree-at-most-one
polynomials in x^2.

I checked the logarithm-continuation argument at a nonzero base point in
(0,1/10). A loop with winding one around 1/2 and zero around the other
three branch points changes s by pi i and leaves t unchanged. Repeating
it n times continues the identically zero germ to

\[
 A t+B(s+n\pi i)+xC+xDt^2+xEt(s+n\pi i)
                         +xF(s+n\pi i)^2=0.
\]

The quadratic coefficient in n gives F=0; the linear coefficient then
gives B+xEt=0. These conclusions hold as germ identities, not only at
one numerical base point. Continuing the latter around 1 changes t by
-pi i while leaving s unchanged, so xE=0 and hence E=B=0.
The remaining identity `At+xC+xDt^2=0`, continued repeatedly around 1,
gives D=A=C=0. Every original coefficient vanishes. The required loops
exist in the four-punctured plane; analytic continuation of the zero
germ stays zero. No unsupported transcendence assertion is needed.

Independence on this interval implies independence of the analytic germs
at zero. The construction of a basis with distinct vanishing orders is
valid: on each finite-dimensional remaining kernel, the lowest nonzero
Taylor coefficient is a nonzero linear functional, whose kernel reduces
dimension by one and eliminates that order. A nonzero analytic germ cannot
vanish to infinite order.

Factoring `a_i h^{n_i}` from each row gives exactly the leading determinant
and remainder in (15), with finitely many evaluation columns j=1,...,12.
The generalized Vandermonde factor is nonzero. A nonzero combination of
k distinct nonnegative powers has at most k-1 distinct positive roots:
divide by its smallest power, differentiate, and use Rolle's theorem and
induction on the number of nonzero terms. Twelve positive roots would
contradict that bound. Therefore the determinant has a nonzero leading
power of h and is nonzero for all sufficiently small positive h.

It follows that the set in (9) is nonempty, its minimum N is finite,
and the coefficient vector in (10) is a well-defined finite real vector.
The condition N>=121 ensures every j/N lies strictly inside (0,1/10).
This is an exact existence prescription, not a reported numerical value
of N or a claim about floating-point conditioning. No numerical determinant
or search outcome is needed for the counterexample.

## 2. Data geometry, gradients, and Hessians at the two points

For x in (0,1/10), the displayed arctanh bound gives t<1/8 and |s|<1/4,
so rho is strictly positive and each u_+ and u_- has norm one. Pairing
the signs cancels every third-coordinate gradient and the (1,3) and
(2,3) Hessian entries. The remaining four matrix entries are precisely
those in B(x).

At v_1=e_1 the paired gradient is `(1-x^2)(t,s,0)`. At v_2=e_2 it
is `(1-4x^2)(t,s,0)`. The four equations in (5) annihilate both.
Using `tanh''(z)=-2 tanh(z)(1-tanh(z)^2)`, the corresponding Hessians
are `-2x(1-x^2)B` and `4x(1-4x^2)B`. Substitution of (6) gives -I_3
in each case, including both off-diagonal and third-coordinate conditions.
Dividing by Q gives the negative definite Hessians of R.

Because the target b is nonzero, lambda is nonzero. Since all t_j>0
and `sum lambda_j t_j=0`, its nonzero entries cannot have only one sign.
The weights (11) are strictly positive after zero pairs are omitted,
sum to one, and carry both binary labels. Their signed potential is
exactly R=Rtilde/Q. Distinct scalar nodes give distinct positive first
coordinates; within a pair the third coordinates differ because rho>0.
Thus no points coincide, and positive first coordinates exclude antipodal
pairs. Unit parallel points would coincide. Scaling to physical
`x_a=sqrt(3)u_a` preserves every one of these pairwise properties and
gives the canonical normalized Gram diagonal one.

## 3. Cancellation of every canonical retained lower feature

The construction keeps the exact correlated lower law. The reverse feature
in coordinate pair i depends on `(G_i,Z_i)` and is correlated with its
forward feature; nothing in the proof replaces these by independent
features. The branch indicator depends only on |G_3| and has probabilities
2/3 and 1/3, giving `E K=(2/3)-2(1/3)=0`.

For each retained component belonging to coordinate pair 1, the product
of that component with sign(G_1) is independent of K, so its activation
pairing vanishes by E K=0. For every retained component in coordinate
pair 2 or 3, sign(G_1) is an independent centered factor, even though
the pair-3 feature can be correlated with K. Thus all six components of
every a_a vanish. This covers both normalized forward features and all
three normalized reverse residual features. It is not merely cancellation
of the one feature selected by M.

The field w is bounded and odd under simultaneous mark negation because
its branch does not change while sign(G_1) does. The readout b_{2,1} is
bounded and odd. The full matrix is admissible, and its chosen rank-one
value imposes no restriction on allowed perturbations.

The diagonal upper covariance gives gamma=kappa e_1 with kappa>0.
Every upper activation is zero, so the readout gradient vanishes.
Every a_a is zero, so the matrix gradient vanishes. Since R is odd,
its gradient is even and its Hessian is odd; consequently its gradient
vanishes at all four values +/-e_1 and +/-e_2 taken by w. Its Hessian
there is exactly `-sign(G_1) I_3/Q`. The physical lower gradient is
`-2 kappa b_{1,1} grad R(w)` and hence vanishes as well. The loss is
one by the unhalved weighted-square convention. No mobility or physical
input scaling factor is missing once the correction in item 1 is made.

## 4. Arbitrary L2 directions and exact flatness

For any fixed lower direction V in L2, integral Taylor expansion gives

\[
 a_a(\varepsilon)=\varepsilon A_a+\frac12\varepsilon^2B_a
                              +o(\varepsilon^2).
\]

After division by epsilon squared, the integrand remainder tends to zero
pointwise and is bounded by a constant times |V|^2. Bounded b_1 and tanh
second derivative justify dominated convergence. This requires no third
moment and is a statement for each fixed V, not uniformly over its L2 ball.

The upper preactivation is uniformly O(epsilon) over the upper carrier,
since it is a bounded feature vector paired with a finite vector. Its tanh
expansion has no quadratic term at zero. Multiplication by the perturbed
readout gives exactly (23): the only quadratic terms are
`gamma^T N A_a`, `delta gamma^T M A_a`, and `gamma^T M B_a/2`.
An arbitrary h in L2 is integrable, so this step does not require bounded h.
All entries of N are covered.

The vector identity (24) holds because grad R(w)=0 pointwise. It eliminates
the linear loss term and both mixed quadratic terms. The surviving squared
prediction term has positive sign, and the residual term is

\[
 -E_1[\kappa b_{1,1}V^T\nabla^2R(w)V]
            =\frac\kappa Q E_1[|b_{1,1}|\,|V|^2].
\]

This rederives every sign and factor in (25). Denote its total quadratic
coefficient by `q_2(V)`. It is finite and strictly positive for every
nonzero L2 V because b_{1,1} is nonzero almost surely. Thus each such
fixed line increases loss for all sufficiently small nonzero epsilon,
regardless of h and N. The neighborhood size may depend on the direction.

If V=0, every retained activation remains zero for the entire line.
Changing c and every entry of M cannot change that, so the loss stays
exactly one for every real line parameter. This is stronger than flatness
to a finite Taylor order.

For bounded V, tanh has a uniformly pole-free complex neighborhood along
the lower perturbation. Bounded features and finitely many inputs give
an analytic finite moment vector, and then the same property for the
upper arguments. The factor c+epsilon h is integrably dominated locally
when h is in L2. Hence the real loss restriction is analytic for bounded
V, in particular along all bounded state directions. Its first nonzero
Taylor term, when present, is exactly the positive quadratic term.

## 5. Direct smaller losses arbitrarily nearby

The identity `R(e_2)=-2R(e_1)` ensures at least one selected critical
value is nonpositive. If that value is negative, input-space oddness gives
a larger value at its negative point. If it is zero, the strictly negative
definite Hessian gives nearby negative values; the negatives of those
points have positive values. Thus there is a fixed finite v_new with
`Delta R=R(v_new)-R(v_j)>0` for at least one branch j.

The chosen branch has positive probability and is independent of G_1.
Intersecting it with a fixed interval of positive G_1 values supplies a
positive-measure set on which b_{1,1}>=beta>0 and w=v_j. The nonatomic
carrier supplies subsets E of arbitrarily small positive measure epsilon.
Replace w by v_new on E and by -v_new on -E. This is an admissible odd
change, of squared L2 norm exactly

\[
                    2\varepsilon|v_{\rm new}-v_j|^2.
\]

The exact feature changes are O(epsilon). The first finite-moment loss
variation is the expression in candidate Section 6, including its factor
four from square-loss differentiation and paired reflection. The finite
moment remainder is O(epsilon squared). Consequently

\[
 \Delta L=-4\kappa\Delta R\int_E b_{1,1}\,dP_1
                      +O(\varepsilon^2)
          \le-4\kappa\Delta R\,\beta\varepsilon
                      +O(\varepsilon^2)<0.
\]

This proves non-local-minimality directly, without invoking any previous
no-bad-local-minima theorem or another route's result.

## 6. The precise Hessian and coercivity issue

The function q_2 is a bounded quadratic form on the lower Hilbert space:
each F_a is bounded and linear in V, and its multiplication weight is
bounded. It is strictly positive on nonzero lower directions. Nevertheless
it is noncoercive even after restricting to the lower block.

For an explicit sequence, let

\[
 E_n=\{|G_1|<1/n\},\qquad
 V_n=\frac{\operatorname{sign}(G_1)1_{E_n}}{\sqrt{P_1(E_n)}}e_1.
\]

These are admissible odd directions with norm one. On E_n,
`|b_{1,1}|<=C/n`, so the weighted integral in q_2 is at most C/n.
Moreover

\[
 F_a(V_n)=\kappa E_1[b_{1,1}\operatorname{sech}^2(w\cdot u_a)
                                  (V_n\cdot u_a)]
\]

has magnitude at most `C sqrt(P_1(E_n))/n`, uniformly over the finite
input set. Its squared contribution tends to zero. Thus q_2(V_n) tends
to zero although every norm equals one. This checks the finite-rank term,
which the essential-infimum observation alone did not address.

There is also a stronger failure: q_2 is not the quadratic term of a
Fréchet expansion on the L2 state space. Suppose such an expansion existed.
Stationarity eliminates its linear term, and evaluation on every fixed
direction forces its quadratic term to be q_2, by the already established
directional limits. Apply it to the shrinking-set perturbations h_E of
Section 5, with upper and matrix increments zero. Their norms squared are
`2 epsilon |v_new-v_j|^2`, while

\[
 q_2(h_E)\ge\frac{2\kappa\beta}{Q}
                         \varepsilon|v_{\rm new}-v_j|^2>0.
\]

The actual loss change is negative of order epsilon by Section 5.
Therefore `Delta L-q_2(h_E)` is not `o(||h_E||_2^2)`, contradicting
the supposed Fréchet expansion. In particular the physical loss gradient
cannot be Fréchet differentiable at this equilibrium. There is no genuine
Fréchet Hilbert Hessian here, although all fixed-direction second
coefficients exist and form the bounded quadratic form (25).

This distinction explains why neither a usual positive-definite-Hessian
test nor a uniform neighborhood conclusion follows. It does not weaken
the intended counterexample to a negative leading coefficient on some
fixed line: every one of those fixed lines has already been classified.

## 7. Separately checked optional balanced-weight extension

The supervisor proposed adding `sum_j lambda_j=0` by adjoining the
constant function one to Phi and using thirteen nodes. This works.
Every original component is analytic and vanishes at zero, so evaluation
at zero eliminates the constant coefficient of any proposed dependence
between one and the original twelve functions. Their proved independence
then eliminates the rest. Thus

\[
 \Phi_{13}(x)=(\Phi(x),1),\qquad b_{13}=(b,0)
\]

defines thirteen independent analytic germs. The same distinct-order and
generalized-Vandermonde argument, now allowing vanishing order zero,
proves nonzero equally spaced determinants for all sufficiently large n.
The prescription

\[
 N_{13}=\min\{n\ge131:
     \det[\Phi_{13}(1/n)\ \cdots\ \Phi_{13}(13/n)]\ne0\}
\]

is therefore finite and keeps every node below 1/10. Solving with target
b_13 preserves all gradient and Hessian constraints and adds zero total
signed coefficient. The nonzero solution has

\[
 \sum_{\lambda_j>0}\lambda_j
     =-\sum_{\lambda_j<0}\lambda_j=Q/2.
\]

After the same two-sign input pairing and weight normalization, the total
weight of positive labels and of negative labels is exactly one half each.
There are at most 26 inputs after zero coefficients are omitted. Every
carrier cancellation, equilibrium calculation, line expansion, and direct
nearby-descent proof is unchanged. The physical scaling remains
`x_a=sqrt(3)u_a`. This validates the proposed extension mathematically;
it does not modify or silently replace the frozen 24-input candidate.

## Final scope

The checked result concerns an ambient state of the exact canonical p=1
nonatomic population model with its full matrix perturbation class. The
data and equilibrium are defined without numerical assumptions. The result
does not establish canonical reachability, attraction, basin probability,
SGD noise behavior, or fitting by any optimizer. It also makes no analogous
claim for a fixed finite population or finite-width network.

The earlier study files and frozen candidate are preserved. This report
is an informed internal check with explicit presentation corrections and
a separately labeled prompt-supplied extension. It is neither a fresh
isolated review nor promotion evidence.
