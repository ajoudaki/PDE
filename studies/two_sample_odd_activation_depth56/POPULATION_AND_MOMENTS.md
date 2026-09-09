# Population bridge, marginal moments, and initial motion

2026-09-07. No old theorem file is edited. This companion is part of the proof assembled in PROOF.md; it is not an independent final review.

## A. The remaining population bridge is valid for every fixed finite L

Assume the quantitative affine/source construction supplies, on one compact feature interval [0,S], uniformly in the backward cap and fine fixed Euler meshes: a raw primal ball with strict slack; marginal subGaussian tails of the L incoming fields; an affine endpoint g0(S)=3/2 with discrepancy below 1/4; and preactivation discrepancy Ez below one half of an explicit Gaussian regression residual square root. Then every conclusion of depth4/POPULATION_AND_MOTION.md extends by finite induction to L populations and L−1 adjacent Gaussian actions.

The finite Gaussian conditioning theorem actually concerns finitely many independent Gaussian matrices, not a fixed number three. A query constrains only its named matrix. Its common generated spaces therefore give L separate L2 spaces, bounded adjacent initialized actions, and their genuine adjoints. The raw learned increments are Hilbert–Schmidt. At a fixed cap the local gate satisfies |Dq|≤2 and |Dz|≤2eR, so bounded-action forward propagation and reverse induction make the raw field locally Lipschitz on the primal ball. The cap/mesh-uniform ball continues the capped strong solution through S.

For two capped or uncut states A,R on a common ball, the asymmetric gate estimate is

  ||D_A(Z_A,q_A)−D_R(Z_R,q_R)||2
  ≤2||q_A−q_R||2+2eR||Z_A−Z_R||2
      +2e|| |q_R|1_{|q_R|>R} ||2.

First bound all forward differences by C_{L,b} times the raw state difference. Induct backward from C through L gates. A reverse discrepancy is multiplied by a bounded action and the fixed gate bound 2; the R factor multiplies only the already bounded forward discrepancy. Consequently the raw direction difference is at most

  C_{L,b}(1+eR)||Theta_A−Theta_R||raw
    +C_{L,b}e sum_{i=1}^L || |q_{R,i}|1_{|q_{R,i}|>R} ||2.

There is one power of R, not R^L. Gaussian reference tails defeat exp(C_{L,b}RS). This gives strong cap removal, uniqueness against arbitrary bounded-primal strong competitors on the same spaces, including nonsymmetric physical competitors with their separate residuals, and restart from reached states.

Odd label folding and exchange equivariance imply f_i=y_i g for the constructed limit. The physical clock ds/dt=2(1−g) is global because g(0)=0 and g(S)>5/4, and the first-hit inverse clock diverges. This assertion does not require monotonicity of capped g.

At the uncut state, writing H=sum_i(y_i/2)h_i^L and g=<C,H>, the actual adjoint gives C'=H and C''=JJ*C. Radial convexity yields ||H||≥||H0|| and g'≥κ0=||H0||². Initialization gives κ0≥a^{2L}δ/2. Thus

  loss(t)≤exp(−2a^{2L}δt).

For convex a=1−theta≥3/4, L5 and L6 retain the old weaker rate exp(−δt/32), since 2(3/4)^12>1/32. No depth-uniform positive rate follows for arbitrarily large L.

All finite-GF/raw-GD and observable bridges use a fixed finite number L of products and queries. Finite-cap width limits precede cap removal; the GD consistency error is C_{L,R,T} n^{-2}. The actual random finite readout is retained and has RMS O_P(n^{-1}). There are L+1 raw kernel terms. Velocity queries are appended in layer order, clipping each new phi'(Z)P query, removing earlier inner clips with the current outer clip fixed, and then removing that outer clip. The product-rule comparison has one velocity truncation factor M times the state discrepancy and a sum of L reference tails. A compact L2 time image gives uniform tail removal. Integrated speed bounds then give same-layer path W2 laws by the interpolation bound 4h∫|x'|². Every such assertion fixes L before sending width to infinity.

## B. Explicit nonaffinity at every fixed depth

At a positive affine Euler mesh, every active forward coordinate is its initialized Gaussian path polynomial plus another polynomial with nonnegative coefficients. Every Gaussian monomial expectation is nonnegative. Thus E||x_l(k)||_n²≥1. Fixed-program moment convergence is justified by uniform integrability: the finite polynomial degree gives a fixed polynomial bound in initialized operator and root norms, whose moments are uniformly bounded. Strong affine Euler convergence yields ||x_l(s)||²≥1.

Inactive fields freeze by telescoping the L−1 matrix factors; each learned correction has bounded ordinary Frobenius norm and has vanishing normalized action on the independent inactive Gaussian root. Hence every affine marginal is centered Gaussian with

  Var Z_i^l=a^{2(l−1)}[v||x_l||²+(1−v)]≥a^{2(l−1)}.

For all a≥1/2, let B_L=4^{L−1} and

  eta_L=4 B_L exp(−1)/(27 pi (B_L+1)^4).

The third-Hermite test proves inf_{alpha,beta}E[atan(sigma G)−alpha−beta sigma G]²≥eta_L whenever sigma²≥1/B_L. The integration-by-parts identity is

  E[atan(sigma G)(G³−3G)]
       =−2 sigma³ E[G²/(1+sigma²G²)²].

After u=sigma G substitution its absolute value is monotone in sigma. Restriction to |G|≤1 at sigma=B_L^{-1/2}, followed by division by E(H3²)=6, gives the displayed constant. Regression slopes belong to [0,1], so the square-root residual is 1-Lipschitz under L2 coupling. Therefore Ez≤sqrt(eta_L)/2 implies the activation regression error≥e²eta_L/4.

For requested convex gains a≥3/4 and L≤6, a^{2(L−1)}≥(3/4)^10>1/404. The old eta_* with B=404 is therefore retained without modification.

## C. Initial motion induction is independent of the quantitative amplitude threshold

Every initialized feature pair has a positive definite Gram matrix, by Gaussian full support and phi'>0. Put H0=sum p_i h_i^L, beta_i^L=H0 phi'(Z_i^L), and descend beta_i^l=phi'(Z_i^l)A_{l+1,0}* beta_i^{l+1}. The top full second-moment matrix S_L=E beta^L(beta^L)^T is positive definite because phi'' is not identically zero. The actual reused-matrix conditioning identity at each downward step is

  A_{l+1,0}* beta_i^{l+1}=G_i^l+sum_j h_j^l T_ij,
  Cov G^l=S_{l+1},

where G^l is independent of the local initialized forward pair and T is the full expected formal derivative, with named slots and coefficients frozen. In particular the covariance is the full second moment, not a residual covariance. Conditional covariance then gives S_l≥a² lambda_min(S_{l+1})I>0.

Every hidden acceleration block has squared raw norm tr(S_l diag(p)F_{l−1}diag(p))>0. The forward-acceleration recurrence and adjunction give sum_i p_i<beta_i^l,U_i^l>=sum_{j≤l}||V_j||raw²>0; exchange makes both sample norms equal, so both are nonzero. Multiplication by phi'≥a gives nonzero feature acceleration. The total projected kernel satisfies κ(s)=κ0+2s²||V||raw²+o(s²), hence κ(t)=κ0+8t²||V||raw²+o(t²). All these are fixed-finite-L statements.

## D. Independent audit of positive product compression and the enlarged active box

Let V_i=a²R_i A_i, R_i=(I−a² A_iB_{i+1})^{-1}, and L_i=(I−a²B_{i+1}A_i)^{-1}. All products below are finite causal matrices and nonnegative entrywise. Affine positive recursion gives A_{i+1}≥beta² V_i, so R_{i+1}V_i≤(beta²a²)^{-1}V_{i+1}. Similarly V_iL_{i+1} compresses.

For i<t, the exact telescoping identity is

  R_{t−1}...R_i
   =I+sum_{j=i}^{t−1}R_{t−1}...R_{j+1} V_j B_{j+1}.

Compressing the strict factor on the left yields

  R_{t−1}...R_i≤I+C_L V_{t−1}sum_{j=i}^{t−1}B_{j+1}.

The transpose-oriented L product obeys the analogous bound. This retains all arbitrary current backward errors. No beta derivative is needed.

For starred coefficients, scale all row defects J by alpha∈[0,1] and bootstrap both the backward row-radius bound and the entrywise constraints V_i*≤2V_i. Since A_{i+1}≥beta² V_i≥(beta²/2)V_i*, every strict-chain compression remains valid with at most an 8^L numerical factor for a≥1/2. The forward loop contains strict factors on both sides of each J, so both sides compress to V_{t−1}; a sufficiently small resulting relative loop implies V_i*≤(1+epsilon)V_i<2V_i. The backward estimates then lie strictly inside the row-radius bound. Finite strict-causal inverses are polynomial, so the homotopy is continuous and has no pole. This closes the two bootstrap constraints simultaneously.

The actual outer box can allow growing active excess r0=C_L^{-K}M^k, where k=min(L−2,4), provided it EXPLICITLY includes V_i(|A|,|B|)≤2V_i,beta_out. Indeed

  R=I+VB, L=I+BV

and |B|≤B_ref+J yield row bounds by 2 reference resolvent rows plus 2|V_ref|row |J|row. With d=L+1, h=2L−1, and u_i=max(0,2i−L−4), the required inequality is d+max_{i<L}u_i+k≤h, precisely the stated choice of k. No small Neumann ratio is needed. Source moments use only these explicit outer-box norms, so there is no circularity. The inner supersolution gives V*≤1.25V_inner<2V_outer, hence it also controls a first exit through the new transfer boundary. Keep the inactive small box separate. Exchange makes deterministic coefficient blocks diagonal, so scalar sector comparison is valid; individual random derivative gates remain full matrices in the response estimates.

## E. Further sharpening: recover Gaussian source scales from raw primal L2 bounds

The following Gaussian-part lemma is used in SOURCE_RESPONSE.md, which gives its explicit prefactors and sufficient smallness condition.

Assume the proved cap-uniform raw comparison implies, at each actual coefficient list under consideration,

  ||Z_i||2≤C_L, ||q_i||2≤C_L M^{L+1−i}.

Write h=atan Z, d_gate=g(Z)tau_R(q), so |h|≤pi/2 and |d_gate|≤|q|. At those SAME deterministic arrays,

  Z=Z_G+e U[d_gate+aBh], Z_G=Rxi+aU zeta,
  q=q_G+e[a B U d_gate+L B h], q_G=L zeta+aBRxi.

Top zeta is zero and top B is the fixed readout integration kernel; the formulas remain valid. Z_G and q_G are centered Gaussian because their arrays are frozen and their named source groups are jointly centered Gaussian. This is an identity for their actual common law, not an independent-covariance substitution.

Use the primitive powers |U_i|density≤C_L M^{u_i}, |B_i|row≤C_L M^{b_i}, |R_i|row+|L_i|row≤C_L M^h, where b_i=4L−1−2i for i<L and b_L=L+1. With d=L+1, h=2L−1, u_i=max(0,2i−L−4), one checks

  d+u_i+b_i≤5L−2,
  h+b_i−(L+1−i)≤5L−2,
  d+u_i+(L+1−i)≤5L−2.

The L2 triangle inequality and e C_L M^{5L−2} sufficiently small therefore give

  ||Z_G||2≤C_L,
  ||q_G||2≤C_L M^{L+1−i}.

Gaussian moments give corresponding sqrt(p) bounds. In the exact q equation, the coefficient on ||q||p is e|aBU|row≤e C_L M^{5L−2}; absorb it. The bounded h term is covered by the same smallness and the displayed Gaussian q scale. Return to the exact Z equation. Thus for every finite p≥2,

  ||Z_i||p≤C_L sqrt(p),
  ||q_i||p≤C_L M^{L+1−i}sqrt(p).

The estimates concern deterministic suprema of marginal norms, not random time suprema. They immediately give cap/mesh-uniform marginal subGaussian tails with the much sharper primal q power. Their premises are already available from the raw affine tube comparison before any source response estimates; this avoids circularity.

The Gaussian-part sharpening only reduces the incoming-field contribution to the derivative defects. It does NOT remove the deterministic gate terms a DeltaV B+a B DeltaG+DeltaV B DeltaG from P. Their row bound costs e M^{b_i}; therefore the previously proposed exponent 5L−1−i alone was invalid. The corrected derivative-only row exponent is 2h+max(L+1−i,b_i), namely

  Q_i=8L−3−2i (2≤i<L), Q_L=5L−1.

The learned-moment row exponent 5L+4−2i is no larger at every layer for L≥3. Any still sharper derivative bound must control the deterministic B-gate terms separately, for example via an actually proved positive-affine gain derivative; it cannot simply replace their B power by the incoming-field moment power. The rejected exponent assignment is recorded here to make the retained deterministic B-gate contribution explicit.
