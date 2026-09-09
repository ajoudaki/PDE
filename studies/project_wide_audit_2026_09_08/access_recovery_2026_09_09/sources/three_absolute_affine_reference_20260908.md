# Fixed absolute affine activation: global reference and the unresolved fitting clock

2026-09-08. User steering now permits an affine part `a z+b` with absolute constants independent of delta. This note investigates the concrete choice `a=b=1`. It does not import the separate large-gain theorem or rescale its activation. The desired perturbed family is `(1-theta_delta)(z+1)+theta_delta atan z` in all three hidden layers.

## 1. Exact affine reference

Set theta=0. On the original canonical neuron Hilbert spaces write the first normalized weight map as W, so `W u_i=w.x_i` with `u_i=x_i/sqrt(d)`. The first raw metric is the Hilbert--Schmidt norm of W's variation. Define

\[
 h_i^1=\mathbf1+Wu_i,\quad h_i^2=\mathbf1+A h_i^1,
 \quad h_i^3=\mathbf1+B h_i^2,
 \quad f_i=\langle C,h_i^3\rangle,
 \quad r_i=f_i-y_i.
\]

Let X map sample coefficients to `sum_i c_i u_i`, and H_l map them to `sum_i c_i h_i^l`. Put

\[
 b_2=B^*C,\qquad b_1=A^*B^*C.
\]

The exact raw GF is

\[
 C'=-H_3r,\quad B'=-C\otimes H_2r,
 \quad A'=-b_2\otimes H_1r,
 \quad W'=-b_1\otimes Xr.
 \tag{1}
\]

The initialized readout is zero at population level; the actual finite random readout must still be retained in a finite-width bridge.

This field is a polynomial in the raw parameters, built from bounded bilinear actions, adjunction, inner products and rank-one products. Unlike the genuinely nonlinear raw Nemytskii field, it is locally Lipschitz on every bounded raw ball. Its scalar loss has the exact gradient-chain identity

\[
 L'=-\|\Theta'\|_{\rm raw}^2.
 \tag{2}
\]

Therefore it has a unique strong C1 solution on all finite physical intervals: local Picard existence applies initially and at every reached state; on [0,T] the energy bound gives

\[
 \|\Theta(t)-\Theta(0)\|_{\rm raw}\le\sqrt{3T/2},
 \qquad
 \|\Theta(t)-\Theta(s)\|_{\rm raw}\le\sqrt{(t-s)L(s)}.
 \tag{3}
\]

If a maximal existence endpoint were finite, the second estimate would supply a strong raw limit there, and local Lipschitz existence from that state would extend the solution. No source cutoff or nonaffine regularization is needed for this affine existence result. Uniqueness includes nonsymmetric competitors on the same Hilbert spaces, and restart follows from the same local uniqueness.

The initialized affine feature Grams are exactly

\[
 Q_l(0)=\Gamma+l\mathbf1\mathbf1^T,\qquad l=1,2,3.
 \tag{4}
\]

At the first layer this uses centered initial Gaussian projections independent of the constant field. At each subsequent fresh Gaussian forward call, `A_0 h` or `B_0 h` has centered Gaussian law with covariance equal to the preceding Gram; adding one adds `11^T`. Thus the augmented geometric margin is positive before theta is introduced.

Equations (1)-(4) establish a global affine reference, but not yet the finite total residual clock required by the existing all-time perturbation method.

## 2. Every nonglobal stationary point below the initial loss has a constant predictor

Assume the three augmented inputs `(u_i,1)` are linearly independent. This holds for three distinct unit inputs: three collinear points on the unit sphere are impossible unless at least two coincide. In the task, pairwise separation rules out coincidences. Let Theta be any affine stationary raw state.

If C=0, then f=0 and L=3/2. Suppose C is nonzero. Stationarity of B in (1) implies `H_2r=0`. Stationarity of C and `H_3r=1 sum_i r_i+B H_2r` imply

\[
 \sum_i r_i=0.\tag{5}
\]

If b_2=0, then `f_i=<C,1>` is constant. Otherwise stationarity of A gives `H_1r=0`. If also b_1 is nonzero, stationarity of W gives `Xr=0`. Together with (5), augmented-input independence then forces r=0.

It follows that a nonglobal stationary state with C nonzero must have b_1=0 (possibly already b_2=0). Expanding the affine predictor gives

\[
 f_i=\langle C,\mathbf1\rangle+\langle B^*C,\mathbf1\rangle
       +\langle A^*B^*C,\mathbf1\rangle
       +\langle A^*B^*C,Wu_i\rangle.
 \tag{6}
\]

When b_1=0 this is constant. By (5), its constant value equals the average label. Hence:

- if all three labels agree, every stationary state with loss below 3/2 is a zero-loss state;
- for mixed binary labels, any nonglobal stationary state with loss below 3/2 has constant predictor equal to the average label and loss exactly 4/3.

This is a structural critical-point statement for the original fixed-offset affine architecture. It does not prove that its canonical initialized GF avoids convergence to the constant-predictor saddle set or escapes to infinity.

The initial loss strictly decreases: with C_0=0 the initial hidden gradients vanish and

\[
 -L'(0)=y^TQ_3(0)y>0.
\]

For binary labels `|sum_i y_i|>=1`, equation (4) even gives `-L'(0)>=3`. This excludes staying at the zero-readout stationary level, but a positive initial derivative does not alone prove passage below the mixed-label level 4/3.

## 3. Fixed offsets alter the usual deep-linear balance identities

It is tempting to cite a bias-free deep-linear balance theorem after augmenting inputs with a constant. That does not preserve the present gradient dynamics: each hidden offset is fixed, whereas a fully augmented matrix factorization would train its bias column and possibly its final row.

The change is visible in exact operator identities. Let `s=sum_i r_i`, and let 1 denote the constant vector in the appropriate layer. From (1),

\[
 \frac{d}{dt}(BB^*-C\otimes C)
 =s(C\otimes\mathbf1+\mathbf1\otimes C),
 \tag{7}
\]

\[
 \frac{d}{dt}(A^*A-WW^*)
 =-s(\mathbf1\otimes b_1+b_1\otimes\mathbf1),
 \tag{8}
\]

and

\[
 \frac{d}{dt}(B^*B-AA^*)
 =-s(\mathbf1\otimes b_2+b_2\otimes\mathbf1).
 \tag{9}
\]

For example, in (8), differentiating A*A yields
`-(H_1r tensor b_1+b_1 tensor H_1r)`, while differentiating WW* yields the same expression with `H_1r` replaced by `WXr`. Their difference is exactly (8), because `H_1r=1 s+WXr`. In (9), use `H_2r=1 s+A H_1r`.

Thus full operator balances are not conserved. If P is orthogonal projection off the constant vector at a given layer, compressing (7)-(9) on both sides by P does remove the right sides. Those projected balances are genuine invariants. For example,

\[
 P(BB^*-C\otimes C)P=P B_0B_0^*P.
 \tag{10}
\]

This is useful structure, but it does not by itself give a lower bound for the trained sample-feature Gram or for the full `B^*C`, since the constant component of C can interact with `B^*1`. Any attempt to use these invariants for a global fitting clock must handle those remaining offset components explicitly.

## 4. Exact affine feature and residual equations

Differentiating the hidden sample-column operators gives

\[
 H_1'=-b_1 r^T\Gamma,
\]

\[
 H_2'=-b_2 r^TQ_1-A b_1 r^T\Gamma,
\]

\[
 H_3'=-C r^TQ_2-BB^*C r^TQ_1-BAA^*B^*C r^T\Gamma.
 \tag{11}
\]

Therefore the total raw sample kernel is exactly

\[
 K=Q_3+\|C\|^2Q_2+\|B^*C\|^2Q_1
          +\|A^*B^*C\|^2\Gamma,
 \qquad\dot r=-Kr.
 \tag{12}
\]

Every summand is positive semidefinite. The offset supplies an initial augmented margin (4), but (11) does not make Q_l monotone; it contains signed residual outer products and different lower Grams. Assuming `Q_3(t)>=Q_3(0)` would need a new proof.

Equations (7)-(12) are the concrete balance/kernel system which a non-lazy fixed-affine reference theorem would have to control. Unlike the two-input scalar-symmetric case, the residual direction need not stay fixed. Merely knowing that the affine regression problem is realizable does not supply a uniform residual-length clock for this factorized GF.

## 5. Literature check and scope

Two relevant primary sources inspected at abstract/theorem-summary level were:

- Arora et al., *A Convergence Analysis of Gradient Descent for Deep Linear Neural Networks*, https://arxiv.org/abs/1810.02281 . Its stated linear-rate result assumes approximate balancedness and a deficiency margin for a bias-free product on whitened data.
- Chen, Lin and Zhang, *On Non-local Convergence Analysis of Deep Linear Networks*, https://proceedings.mlr.press/v162/chen22p.html . Its stated analysis uses balanced initialization and permits convergence to saddle points.

Neither stated theorem verifies the present fixed-bias, unbalanced canonical Gaussian initialization. I have not used either as a proof premise. Augmenting the input without verifying the gradient/metric and balance hypotheses would be an easier-model substitution.

## 6. Current conclusion and next missing lemma

The fixed-affine option removes the earlier singular-initialization obstruction and gives a globally well-posed polynomial affine reference. Its nonconstant-output stationary structure and projected balance identities are now explicit.

What remains unproved in this route is a bound, for each fixed delta, of the form

\[
 \sup_{t\ge0}\|\Theta_{\rm aff}(t)-\Theta_0\|_{\rm raw}
 \le R_\delta<\infty,
 \qquad
 \int_0^\infty\|r_{\rm aff}(t)\|_1dt\le S_\delta<\infty,
 \tag{13}
\]

uniform over the compact class of admissible three-input Grams and labels. A proven global fitting/clock theorem using (7)-(12), or another valid fixed-affine argument, would then let the existing controlled perturbation machinery choose one sufficiently small theta_delta independently of physical horizon. This note does not yet establish (13) or the complete nonlinear extension.

## 7. Universal residual-clock energy and a conditional full-rank fitting result

A useful simplification does not require a separate first-factor norm calculation. On any true GF with nonzero residual, let

\[
 u(t)=\int_0^t\|r(s)\|_2\,ds,\qquad R_r(u)=\|r(t(u))\|_2.
\]

Because L=R_r^2/2 and `Theta_u=-grad L/R_r`, exact differentiation gives

\[
 \frac{dR_r}{du}=-\|\Theta_u\|_{\rm raw}^2,
 \qquad
 \int_0^u\|\Theta_v\|_{\rm raw}^2dv\le\sqrt3,
 \qquad
 \|\Theta(u)-\Theta_0\|_{\rm raw}^2\le\sqrt3\,u.
 \tag{14}
\]

This holds for the complete raw state, regardless of fixed offsets or effective-bias growth. It permits every individual raw factor norm to be bounded by a constant times sqrt(1+u), without first proving a finite clock.

For illustration, it gives a rigorous conditional fitting theorem in the positive input-Gram case. Suppose `Gamma>=lambda I` with lambda>0, the binary labels are mixed, and at some finite clock u_0 the loss satisfies `L<=4/3-epsilon_0` for epsilon_0>0. Set

\[
 \nu=\sqrt{8/3}-\sqrt{8/3-2\epsilon_0}>0.
\]

Loss monotonicity and the projection P off the sample constant vector imply `||Pf||>=nu` subsequently. The nonconstant part of the affine predictor is `P X^*W^*b_1`. Since `||X||<=sqrt3` and the initialized first map is an isometry on the input span,

\[
 \nu\le\sqrt3\,\|W\|\,\|b_1\|,
 \qquad\|W\|^2\le(1+3^{1/4}\sqrt u)^2\le4(1+u).
\]

Thus

\[
 K\succeq\|b_1\|^2\Gamma
 \succeq\frac{\lambda\nu^2}{12(1+u)}I_3,
 \qquad
 \frac{dR_r}{du}\le-\frac{\lambda\nu^2}{12(1+u)}.
 \tag{15}
\]

Integrating the logarithmic lower dissipation forces a finite total clock, with the upper bound

\[
 1+u_\infty\le(1+u_0)
       \exp\left(\frac{12R_r(u_0)}{\lambda\nu^2}\right).
 \tag{16}
\]

Indeed continuation to a larger residual clock would make the integrated upper bound for R_r negative. By (14), this finite clock supplies a bounded raw path and a strong endpoint. In physical time the residual tends to zero; the positive lower bound in (15) on this finite clock then gives an exponential tail.

The unresolved hypotheses are substantial: the present work does not prove entry below 4/3, and pairwise separation does not give a delta-only positive lambda for Gamma. At rank two, (15) controls only the input range and misses the constant-completing direction. The same issue persists for nearly singular rank-three configurations if one seeks uniformity in delta alone. Consequently (16) is not the requested uniform affine clock theorem.

One additional caution concerns actual affine coefficients. For rank-two inputs, augmented-input independence controls the entire effective coefficient `(v,c)` from the three predictions. For rank-three inputs, the augmented input space has dimension four while there are only three observations: predictions control only the minimum-norm representative, not an arbitrary actual effective bias c. An unobserved coefficient direction can carry cancellations. The universal identity (14) avoids needing a bound on that actual bias.
