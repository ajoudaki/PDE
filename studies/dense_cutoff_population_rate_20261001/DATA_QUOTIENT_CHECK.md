# Internal reconstruction of the data quotient and persistent clock

2026-10-03. This is an **internal collaborator check**, not an independent
isolated review or a promotion approval. I read and reconstructed the complete
`DATA_QUOTIENT_CLOCK.md`, including its fixed-order bootstrap, weighted-history
argument, and endpoint-filter identities. I used the current manuscript
definitions and proofs already read within the assigned scope and the required
canonical-notation, rigorous-proof, and research skills. No other study,
experiment, historical chat, manuscript edit, or Git operation was used.

**Verdict after the disclosed corrections:** the exact quotient, positivity of
its population initialization Gram, fixed-order small-effective-label physical
convergence, endpoint pairing, endpoint-residual isometry, and signed defect
identity are internally checked in their stated scopes. The argument does not
prove an order-uniform small-label threshold, a tracking counterexample, or a
failure of the desired general-data root-width theorem.

The source hashes are:

- Read version: `0b22aea21581f35a1f986566384519457a53b8c1d561e5f30d7144e28da1c952`.
- Corrected and checked version:
  `592a3002e1c018b037a184a62016416646c8b95c25ffe82c9b92f4972b33c1db`.

The coordinator authorized two narrow source changes during this check. The
final backward-history estimate was missing the normalization \(n^{-1}\) on
its left side. I restored it. The weighted bootstrap previously invoked small
original labels to make \(\alpha\rho/A\) small, whereas Section 3 allowed
small effective labels with arbitrary fixed \(\sigma>0\). I replaced that
step by a finite initial-time split, which proves the weighted conclusion in
the stronger Section 3 scope. No other source changes were made.

## 1. Quotient reconstruction and clock

For each sign class \(I_j\), write its normalized inputs as
\(v_a=s_a u_j\), let \(p_j=|I_j|/m\), and set
\[
 \bar y_j=|I_j|^{-1}\sum_{a\in I_j}s_a y_a,
 \qquad \eta_a=y_a-s_a\bar y_j,
 \qquad \sigma^2=m^{-1}\sum_a\eta_a^2.
\]
Then \(\sum_{a\in I_j}s_a\eta_a=0\). Odd tanh forward maps and even
tanh gates imply, at every parameter state,
\[
 h_a^{(\ell)}=s_a h_j^{(\ell)},\qquad f_a=s_a f_j,
 \qquad \delta_a^{(\ell)}=\delta_j^{(\ell)}.
\]
Thus for \(e_j=f_j-\bar y_j\) and
\(u^2=\sum_jp_je_j^2\),
\[
 r_a=s_a e_j-\eta_a,\qquad
 \rho^2=u^2+\sigma^2,
 \qquad \sum_{a\in I_j}s_a r_a=mp_j e_j.
\]
This verifies all signs and class weights in the dense updates. It also gives
the orthogonal label decomposition
\(m^{-1}\sum_a y_a^2=\sum_jp_j\bar y_j^2+\sigma^2\).

The original forward moments have the same parity as the forward features.
Consequently only the signed class averages of the original backward moments
appear in reconstruction. Their source is exactly \(e_j\delta_j\), their
dilation coefficient is still \(\rho/\tau\), and their weights in
reconstruction are \(p_j\). This verifies equation (3), including its
initial prefix and \(1/(n\tau)\) normalization. The quotient is a
coordinate reduction of the physical trajectory, with the **original** clock
\(\dot\tau=\sqrt{u^2+\sigma^2}\). Substituting \(u\) for that clock
would change the algorithm when \(\sigma>0\).

When every \(\bar y_j=0\), the zero readout forces every backward response
and every effective update to vanish. Original backward moments also vanish
because their source contains that response. The forward mode-zero moments
are \(\tau h(0)\), with other forward modes zero. Reconstruction stays at
initialization, and \(\tau=1+\sigma t\). The source correctly excludes
divergent-clock or inconsistent-label arguments alone as counterexamples.

## 2. Population Gram and finite-width initialization

Normalized representatives from different sign classes are pairwise
nonproportional. A null quadratic form of the first-layer Gaussian feature
covariance would yield
\(\sum_jc_j\tanh(u_j^\top x)=0\) for every \(x\), by continuity and
Gaussian full support. Fixing a nonzero coefficient and applying one finite
difference perpendicular to every other representative eliminates all other
ridge functions. Every remaining step size can vary independently because its
chosen direction is not perpendicular to the retained representative.

The resulting vanishing \((J-1)\)-fold scalar differences force tanh to be
a polynomial of degree at most \(J-2\): mollify, differentiate in the
steps, and then recover the finite-dimensional polynomial limit by
interpolation. This contradicts bounded nonconstant tanh. The separate
\(J=1\) argument uses positive variance. In dimension one normalization
already forces \(J=1\), so no unavailable perpendicular direction is used.

At each later layer a positive-definite Gaussian covariance gives full
support in \(\mathbb R^J\); varying one coordinate in a putative identity
\(\sum_jc_j\tanh(Z_j)=0\) eliminates its coefficient. This proves
positivity at every fixed depth. Multiplication by
\(\operatorname{diag}(\sqrt p)\) preserves positivity. The finite-width
conditional law-of-large-numbers argument applies to this fixed list of
representatives. Its required moments are bounded here because tanh is bounded.

For the original sample set the covariance is \(SQ^{(L)}S^\top\), where
\(S_{aj}=s_a\) on class \(I_j\). Positivity of \(Q^{(L)}\) proves its
nullspace is exactly \(\ker S^\top\). The claim is for each fixed
normalized dataset, not a geometry-uniform margin. The extension of the
fitting proof to fixed positive weights \(p_j\), when \(\sigma=0\), is
valid after replacing residuals by \(\sqrt{p_j}e_j\); the kernel is then
a symmetric Gram and has the stated weighted readout Gram as a summand.

## 3. Fixed-order physical convergence

This part assumes exactly two hidden tanh layers, zero initial readout, fixed
order \(q\), a bounded initialized hidden operator, and a positive
initialized weighted readout Gram gap. Let
\(Y_0=(\sum_jp_j\bar y_j^2)^{1/2}\), and stop at effective activity
\(\int_0^t u=S\) or at the hidden-operator tube boundary.

The first three estimates are independent of the original clock:
\[
 \|w\|_\infty\le2S,\qquad
 \max_j\|\delta_j^{(2)}\|_2/\sqrt n
       +\max_j\|\delta_j^{(1)}\|_2/\sqrt n\le CS,
 \qquad \max_j\|\dot h_j^{(1)}\|_2/\sqrt n\le CSu.
\]
They follow directly from the weighted updates, bounded tanh, bounded gates,
and the stopped operator norm. Factors involving fixed \(p_j^{-1}\) are
permitted constants.

The finite-order projection kernel has absolute integral at most \(q^2\).
Move one projection onto the forward history in reconstruction and use
\(b_j\,d\tau=e_j\delta_j^{(2)}dt\). Its integrable backward mass is
at most \(CS^2\sqrt n\), while the projected forward RMS is at most
\(q^2\). This proves the hidden displacement \(C_qS^2\). The direct
first-layer update gives \(CS^2\). Forward subtraction gives a
\(C_qS^2\) readout-Gram change, so sufficiently small \(S\) preserves
both tube and gap.

The defect calculation is also valid before the bootstrap closes. Put
\(A(t)=\tau(t)\). The projected backward endpoint satisfies
\[
 \|b_j^*(t)\|_2/\sqrt n\le Cq^2 S^2/A(t).
\]
The forward endpoint residual is the physical-time derivative convolved with
\(L_q(x)=(p_q(x)+p_{q-1}(x))/2\). Its bounds
\(L_q(0)=0\), \(|L_q|\le1\), and
\(|L_q(x)|\le\min(1,B_qx)\) imply equation (9).

For finite stopped terminal time, Tonelli and \(dA=\rho dt\) give
\[
 \int_{A(s)}^{A(t)}A^{-1}\min(1,B_qA(s)/A)\,dA
 \le1+\log B_q.
\]
Extending this nonnegative scalar integral to infinity does not assume that
the stopped solution already exists there. No positive lower bound on
\(\sigma\) is used. The current backward factor contributes
\(CS^3\int u\le CS^4\); the projected factor contributes
\(C_qS^3\int u\le C_qS^4\). This verifies the absolute, not merely
signed, defect estimate.

In weighted residual coordinates the preserved gap yields
\[
 D^+u\le-\kappa u+CS\|E_2\|_F,
 \qquad
 u(t)+\kappa\int_0^t u\le Y_0+C_qS^5.
\]
This remains valid at \(u=0\); with \(\sigma>0\), memory can still
move there, so treating it as an equilibrium would have been invalid. The
source does not make that error. Choosing \(S=2Y_0/\kappa\) and
\(C_qS^5<Y_0/2\) excludes the activity boundary with strict margin.

Continuation can be checked directly. On every finite physical interval,
\(u\) and hence \(\rho\) are bounded, \(1\le\tau\le C_T\),
forward raw moments are bounded by \(C_T\sqrt n\), and effective backward
moments by \(CS^2\sqrt n\). The original backward moments, if retained,
also stay finite because their additional sources are the fixed
\(-\eta_a\delta_j\) and the time interval is finite. The first matrix
and readout remain bounded by their integrated updates. Thus the finite
dimensional, locally Lipschitz raw ODE cannot have a finite maximal endpoint.

Finally, every physical velocity is integrable: first-layer and readout
velocities are controlled by \(CSu\) and \(Cu\); the hidden matrix has
its dense-form contribution \(CSu\) plus the integrable defect. Parameters
therefore converge. Their effective residual norm converges and is
integrable, forcing its limit to be zero. This proves the stated conclusion
even for arbitrary fixed \(\sigma>0\); \(Y_0=0\) is the stationary case.

The order dependence is real in this proof. One may take \(B_q\le q^2\)
from the Legendre derivative bound. The displayed estimates then give
\(C_q\lesssim q^2[1+\log(e+q)]\) for the integrated defect and
\(C_{q,\alpha}\lesssim_\alpha q^{2+2\alpha}\) for the weighted
defect below. A sufficiently small choice \(S\le c_\alpha/q\)
satisfies all displayed bootstrap conditions, including the separate
\(q^2S^2\) tube estimate. This is merely a crude sufficient threshold;
it supplies no fixed positive label threshold as \(q\to\infty\).

## 4. Persistent-clock endpoint

For \(\sigma>0\), \(\tau(t)\ge1+\sigma t\to\infty\).
Absolute integrability of \(e_j\delta_j\) and \(|p_k|\le1\) justify
dominated convergence in each fixed backward moment, giving
\(\bar\delta_{j,k}\to(-1)^kD_j\), with
\(D_j=\int_0^\infty e_j\delta_jdt\).

For the forward moment, divide by \(\tau\) and rescale its interval to
\([0,1]\). Bounded forward histories converge at every positive rescaled
coordinate to their final feature, while the single point zero has zero
measure. This gives \(\bar h_{j,k}/\tau\to h_j(\infty)\mathbf1_{k=0}\).
Only mode zero survives in reconstruction, proving equation (15).

The conclusion does not identify different orders' endpoints: both \(D_j\)
and the limiting features depend on their closed trajectories. It also applies
to effective signed backward moments, not to the individual original backward
moments whose inconsistent-label sources may persist. These distinctions are
correctly stated in the source.

## 5. Isometry, weighted histories, and signed defect

For \(v\in L^2(0,\infty)\), integrate the growing projection-energy
identity from zero. The initial energy tends to zero because it is bounded
by \(\int_0^A\|v\|^2\). Therefore
\[
 \int_0^A\|R_qv\|^2
 =\int_0^A\|v\|^2-\|\Pi_q^Av\|_2^2.
\]
For bounded compactly supported histories, the last projection norm is
\(O_q(A^{-1})\). Approximation in \(L^2\) and projection contraction
extend its decay to arbitrary \(L^2\) histories. Hence \(R_q\) is an
isometry, and \(T_q=I-R_q\) has norm at most two. Surjectivity of
\(R_q\) is neither asserted nor needed.

The Mellin formula can also be verified explicitly. Shifted Rodrigues and
integration by parts first give
\[
 \int_0^1p_k(x)x^{s-1}dx
 =\frac1s\prod_{r=1}^k\frac{s-r}{s+r}
\]
where the integrations by parts are valid. Both sides are the same rational
function throughout \(\operatorname{Re}s>0\). Define
\(P_k(s)=\prod_{r=1}^k(s-r)/(s+r-1)\), with \(P_0=1\).
Then the \((2k+1)\)-weighted displayed integral is
\(P_k-P_{k+1}\); summing proves equation (18). At
\(s=1/2+i\omega\), numerator and denominator of each factor have equal
modulus. This agrees with the energy proof of the isometry.

For the actual fixed-order trajectory, the weighted defect estimate follows
by the same Tonelli calculation, replacing \(A^{-1}\) by
\(A^{\alpha-1}\), where \(1/2<\alpha<1\). The scalar integral in the
source is exact, and it gives
\(\int_0^T A^\alpha\|E_2\|_F\le C_{q,\alpha}S^3M_\alpha(T)\).
The corrected finite-time split uses the already proved bounds
\[
 \rho\le\rho_*<\infty,\qquad A(t)\ge1+\sigma t.
\]
Thus \(\alpha\rho/A\le\kappa/2\) after a finite \(T_0\). The
finite earlier weighted integral is placed on the right-hand side. Absorbing
\(C_{q,\alpha}S^4M_\alpha\) proves \(\sup_T M_\alpha(T)<\infty\).
This is noncircular: global physical convergence and the unweighted activity
bound were established in Section 3 before this argument, and every finite
\(M_\alpha(T)\) is already defined.

The forward tail is consequently bounded in normalized RMS by
\(CSM_\alpha(\infty)A^{-\alpha}\), which is square integrable in the
clock. The corrected backward estimate is
\[
 \frac1n\int_0^\infty\|b_j\|_2^2dA
 \le CS^2\int_0^\infty\frac{u^2}{\rho}dt
 \le CS^3.
\]
Here \(u\le\rho\), and the fixed sample weights are absorbed into
\(C\). This verifies the hypotheses used to polarize the isometry.

Constants are annihilated by the endpoint residual. Applying real
polarization component by component to \(b\) and \(h-h_\infty\)
therefore gives equation (19). The constant prefix contributes nothing to
its left side for \(A\le1\), because the backward history is zero there.
Changing variables \(dA=\rho dt\) in the actual defect gives equation
(20), with its displayed positive sign and \(2/n\) factor.

There is a second, shorter verification of (20) that does not require the
weighted-history argument. Section 3 already proves absolute integrability of
the actual defect and of the dense-form update along the closure path.
Integrating \(\dot{\widehat W}=F_W(\widehat\theta)+E_2\) gives
\[
 \widehat W(\infty)-W_0
 =-\frac2n\sum_jp_j\int_0^\infty e_j\delta_jh_j^\top dt
   +\int_0^\infty E_2dt.
\]
Substitute the independently checked final-feature pairing from equation
(15). Rearrangement gives precisely (20). Thus the signed identity itself
already holds in the Section 3 regime; the weighted argument additionally
establishes the hypotheses for its isometry representation.

The final step-history example is correct: for \(q=1\) and a unit step at
\(A_0\), the endpoint residual is zero before the step and \(A_0/A\)
after it, so its squared integral is \(A_0\). This prevents a bound from
total variation alone on an unbounded clock. It does not show that an actual
network realizes a late step or produces a nonzero prediction discrepancy.

## 6. Remaining scope limits

No unresolved error was found in the corrected fixed-order arguments checked
above. The following stronger implications remain unproved and must not be
inferred from this check:

- a positive effective-label threshold uniform in \(q\);
- control of simultaneous large-width, large-order, and infinite-time limits;
- an order-independent endpoint, since the endpoint formula contains
  order-dependent trajectories and integrals;
- a surviving discrepancy in predictions, as opposed to a difference between
  two algebraic descriptions of learned matrices;
- a counterexample to the canonical same-width root-width tracking target.

This check establishes only the internal mathematical validity of the stated
quotient and fixed-order results at the corrected source hash.
