# Isolated adversarial review: nonlinear response perturbation

**Verdict: PASS.**

The final candidate proves the stated conditional perturbation lemma. Under
the actual affine finite-mesh primal hypothesis P(B,S), its actual canonical
source coefficients have the claimed O(epsilon) forward-entry and backward-row
errors, uniformly over the covered meshes and finite caps. Its coordinate
laws have the claimed uniform subGaussian moment bounds for sufficiently
small fixed epsilon. I found no missing current-coordinate factor, circular
coefficient bootstrap, lost source-step factor, or growing-Gram conditioning
assumption in this argument.

This verdict is conditional on the expressly permitted affine baseline and
fixed finite-program identification dependency. It is not a verdict on a full
two-sample physical-flow theorem, existence of a continuous limit, cap removal,
or selection of one activation for every input angle. Those are outside the
candidate's conclusions and are not gaps in this lemma.

## Audited version and isolation

Audit date: 2026-09-05. The candidate was read completely, through line 930.
The corrected final hash supplied by the user is the version audited:

```text
ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568
/tmp/l3-two-sample-Un7kw9/NONLINEAR_RESPONSE_PERTURBATION.md
```

Permitted dependencies and instructions actually read:

```text
e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd
/tmp/l3-two-sample-Un7kw9/CONTRACT.md

a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f
/tmp/l3-two-sample-Un7kw9/TWO_SAMPLE_SOURCE_BASELINE.md

f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4
/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md

9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
/etc/codex/skills/solve-math-rigorously/SKILL.md
```

The contract, baseline, and skill were read fully. For the long local proof,
only lines 211--455 were read: its fixed-program statement, conditioning and
formal-source rule, singular-Gram treatment, and finite-program application.
The long proof's displayed hash identifies the entire dependency file, not
an assertion that its other sections were audited here.

No route proposal, other proposal, history, review, or worker result was
read. References to such material in the allowed documents were not followed.
No agents, experiments, simulations, or repository operations were used.
The candidate was not edited; its hash was checked again after the mathematical
audit and remained the final hash above. The skill informed the verification
of individual proof obligations and dependency hypotheses.

## 1. Exact scope and baseline substitution

The result concerns the explicit label-directed feature Euler program
(6)--(10), with c_a=y_a/2 and P=Gamma diag(c). It assumes a fixed finite S,
a fixed B, and P(B,S) for each mesh in the selected family. Width tends to
infinity at each fixed mesh and cap. Neither uniform probabilities over an
increasing family of meshes nor unconditional finite-width neuron tails are
claimed.

The clipping convention is the smooth clip specified in the permitted
baseline, Section 2, with the bounds displayed in candidate (5). This supplies
the C^1 regularity required by the finite-program theorem. The proof does not
require clip monotonicity or higher derivative bounds uniform in the cap.

The rectangular maximum absolute row-sum norm satisfies
|AB| <= |A||B|. The time-row norm is the sum of these block norms. In particular,
for two output samples,

\[
 \sum_j\max_a\sum_b|T_{ka,jb}|
 \le \sum_{j,a,b}|T_{ka,jb}|
 \le 2\max_a\sum_{j,b}|T_{ka,jb}|.
\]

Consequently the factor 2 in candidate (4) correctly converts the baseline's
backward output-row bounds to the stronger sum-of-block-norms convention.
The factor 2 in A_0 correctly sums the two entry bounds in each forward block.
Both substitutions dominate the bounds for both layers when B>=1. No factor
equal to the number of times or samples beyond this fixed factor is omitted.

The primary scope used below is the finite-width primal premise (2).
The optional population-primal interpretation has the stated substitution
through baseline (30)--(32); it is not an assertion that a continuous affine
bound automatically controls arbitrary coarse Euler meshes.

## 2. Primal comparison and passage to actual population moments

The cap-independent primal comparison is valid without a nonlinear response
bound. At the same raw state, forward differences come from the bounded
perturbation |epsilon arctan z| <= (pi/2)epsilon and multiplication by at
most b=2B at each subsequent layer. This gives (14). Backward differences
use |D(z,q)-q| <= epsilon|q| and the unchanged affine transposes, giving
the five bounds in (15).

The numerical vector-field bound can be checked directly. In units of
epsilon, the four update differences are at most

\[
 7b^3,\qquad
 9b^3+\frac\pi2b^2,\qquad
 4b^3+\frac\pi2b(b+1),\qquad
 \frac\pi2(b^2+b+1).
\]

Here the matrix-2 estimate uses 3b^2 times the nonlinear feature bound 3b,
plus the affine delta bound b^2 times pi/2; matrix 3 is analogous. Their sum is

\[
 20b^3+\frac\pi2(3b^2+2b+1)<30b^3\qquad(b\ge2).
\]

The baseline's affine Lipschitz bound 9b^2 applies to the sum of the four
raw state-distance components. Splitting the vector-field difference as
[V_e(theta_e)-V_0(theta_e)]+[V_0(theta_e)-V_0(theta_0)] therefore gives
the candidate recurrence and

\[
 d_k\le30b^3\epsilon\sum_{j<k}h_j
                  \prod_{j<r<k}(1+9b^2h_r)
       \le30b^3S e^{9b^2S}\epsilon.
\]

If the last expression is at most B/2, a state already within the comparison
ball maps to a state whose four sizes are at most 3B/2<2B. This is a literal
induction over nodes, including a final node with no subsequent update.
It does not assume stability of a nonlinear vector field with a constant
uniform in R.

The transfer to population moments has the needed hypotheses. At each fixed
mesh and cap, the union of the nonlinear and affine calculations sharing
the initial matrices is a finite program. Its coordinate instructions are
C^1 and globally Lipschitz with bounded first derivatives: for D these bounds
are 2epsilon R and 1+epsilon, and the forward derivative is bounded by 2.
Roots are iid joint tuples of finite second moment, independent of the two
initial Gaussian matrices. Adding finitely many sample slots or the second
calculation does not change these conditions. Learned contractions can be
frozen and then transferred by the baseline's finite induction.

The resulting joint empirical W_2 limit supplies a coupling of the actual
coordinate laws. Its marginals agree with each program's own canonical law
by applying the same fixed-program identification to that program alone.
The small finite initial readout may equivalently be replaced by zero using
the dependency's fixed-program comparison. No derivative is taken in this
passage, and no mesh-uniform comparison of covariance square roots is used.

Thus a high-probability bound on the normalized query differences passes to
the deterministic L^2 bound in this joint law. Cauchy--Schwarz then proves
(17). The learned forward error keeps its explicit h_j; summing the learned
backward error costs only sum_j h_j <= S. Individual Gaussian source variances
are uniformly bounded by the corresponding query second moments. This entire
step precedes, and is independent of, the coefficient bootstrap.

## 3. Moment bounds and the current-factor exponential envelope

Assume a bounded coefficient prefix (18). The middle feature moment maximum
U_k=max_{v<=k}||H^2_v||_p satisfies

\[
 U_k\le K(1+2AS)\sqrt p+2AM\sum_{r<k}h_rU_r.
\]

Discrete iteration bounds it by K sqrt(p), with constants independent of p,
mesh, and cap. The bottom calculation has the same form with feedback 2M.
For the top, the double integral in (21) is bounded by
2AS sum_{v<k}h_v max_{u<=v}||C_u||_p, giving the same conclusion. All maxima
here are maxima of deterministic norms. No random maximum of source coordinates
over time has been estimated. The remaining fields follow by their displayed
linear equations and |D(z,q)|<=2|q|.

Expanding the exponential using the even moments verifies (22), including
its constants. Hence, for Q equal to the relevant absolute backward input,
there is a uniform L with E exp(Q_r^2/L^2)<=2.

Differentiation of the exact source equations gives (24), (26), and (28).
For a single transpose source j, the direct forcing has size at most 2h_j
or 2Ah_j and all earlier derivatives vanish. For a full forward-source row,
summing the identity sources costs exactly |I|=1: at time k only the current
source has a direct identity block. Padding other rows by zero makes the
triangle inequality compatible with these time-row sums. The resulting
inequalities are exactly (25), (27), and (29).

For nonnegative lambda_r, the elementary majorant
w_{k+1}=(1+h_k lambda_k)w_k proves (30). At a backward output, however, the
additional term L_k J_k is present. In the middle its row norm is at most
epsilon Q_k u_k, and at the top the same bound holds with Q_k=|C_k|. This
establishes the necessary terminal factor in (32). It cannot simply be
discarded in favor of a past-time exponential.

The candidate controls it correctly. With t=s_k and S>0, the weights
h_r/S and 1-t/S sum to one. Jensen's inequality therefore gives (33), with
the unused weight assigned to zero. For the envelope in (31), this yields
the explicit bound

\[
 \mathbb E\mathcal E_k^p
 \le 2\exp\!\left(pKS+
            \frac{(pK\epsilon S)^2L^2}{4}\right)
 \qquad(1\le p<\infty).
\]

Indeed uQ<=Q^2/L^2+u^2L^2/4 bounds each exponential moment appearing in
Jensen's inequality. Finally,

\[
 \|(1+Q_k)\mathcal E_k\|_p
 \le(1+\|Q_k\|_{2p})\|\mathcal E_k\|_{2p}.
\]

This proves (34) without any independence between Q_k and the past, any random
time supremum, or any lower bound on a covariance eigenvalue. Constants for
these derivative-envelope moments may depend on p, which is sufficient for
the subsequent first-moment estimates. The subGaussian field estimate itself
has the stronger K sqrt(p) bound with K independent of p.

## 4. Comparison with the affine derivative system at the same arrays

Setting G=V=I and L=0 freezes a deterministic derivative system at the
nonlinear coefficient arrays. It does not replace those arrays by the
baseline arrays. Subtraction in the middle gives affine feedback on
J-J_aff plus precisely the terms displayed in (37): the gate error on a
direct transpose source, L_r J_r, and the two gate errors in V_r b_r G J.

For a single transpose source all nondirect terms inherit h_j from (30).
The direct term appears only at r=j and is multiplied by a_{kj}, or by
h_j P in the bottom population. This proves the h_j factor in (38) for
unequal meshes. For a full forward-source row the direct identity cancels,
and the identical estimate holds with f=1.

Since the envelope is increasing in time, the accumulated forcing is bounded
by K epsilon f times
1+sum_{r<k}h_r(1+Q_r) E_r. This last expression is increasing in k.
Applying the finite-product majorant to the remaining deterministic affine
feedback proves (39); its expectation is O(epsilon f) by the preceding
envelope calculation. Feature multiplication contributes only
(G_k-I)J_k, of the same expected order.

For the top system, substitution of Delta T into Delta J in (40) leaves
affine feedback at most AS sum_{r<k}h_r max_{v<=r}|Delta J_v|_r. The extra
gate forcing has the same bound (38), since each additional nested time sum
is at most S. Delta T then has the same O(epsilon) expected row bound.

The output differences (41)--(42) contain all remaining terms. In particular,
their current L_k J_k terms cost K epsilon E[Q_k E_k], which is uniformly
finite by the proved Holder estimate. Deterministic b-row weights multiply
the row differences from (39); summing them costs M, not the number of times.
This verifies (35)--(36), including the stronger formulation with expectation
outside the sum of random block norms. Combining them with (17) justifies
the remainder bounds (52).

## 5. Deterministic stability and the four construction stages

The recursions (43)--(47) are obtained by direct substitution in the affine
derivative equations. In particular, T_k only uses a^3_r for r<k; U_k uses
current a^2_k and past b^3_r; and W_k=b^3_k U uses current b^3_k. The matrix
orientations in these products are consistent. Their bounds (48)--(49) follow
from the respective feedback constants M, AM, AM, and AS. The top bound is
S exp(AS^2), with one S coming from the direct readout forcing.

Here is a check of the deterministic error estimates with their time factors.
Use alpha, beta, E_k and I_k as defined in (53); all constants below depend
only on the fixed bounded-prefix constants and S.

* Subtracting the F recursions gives (54). The term containing Delta b^2_r is
  at most K_F h_j beta^2_r before the outer multiplication by h_r. Dividing
  by h_j and iterating gives |Delta F_{kj}|/h_j <= K I_k. Equation (50)
  therefore gives alpha^2_k <= K(epsilon+I_k), using only past b^2.
* In the V recursion, the difference of a^2 b^3 V has the three terms in
  (56). The term with Delta a^2_k costs MS K_V alpha^2_k; the direct source
  costs alpha^2_k; and Delta b^3_r costs A K_V h_r beta^3_r. The remaining
  feedback is AM sum_{r<k}h_r max_{v<=r}|Delta V_{vj}|/h_j. Iteration gives
  alpha^3_k <= K(epsilon+I_k). There is no current b^3_k in this step.
* For T, the direct h_j c^T forcing cancels. The Delta a^3_r term costs
  S K_T h_r alpha^3_r, while exchanging the two feedback sums gives
  AS sum_{v<k}h_v t_v. This is (58) and implies beta^3_k <= K(epsilon+I_k).
  Its affine comparison has no current alpha^3_k. Its nonlinear derivative
  remainder may use current a^3_k, which has already been bounded.
* Summing the U difference by source blocks gives (60): its forcing is
  MS K_U alpha^2_k+A K_U sum_{r<k}h_r beta^3_r, with the same AM feedback.
  Hence u_k <= K(epsilon+I_k). Finally
  |Delta W_k|_r <= K_U beta^3_k+sum_{v<=k}|b^{3,0}_{kv}|u_v
  <= K_U beta^3_k+M_0 max_{v<=k}u_v. This proves the claimed beta^2_k bound.

Whenever a past error appears in these estimates, I_v<=I_k bounds it by the
same nondecreasing forcing. These calculations justify the passage to

\[
 E_k\le K\epsilon+K\sum_{r<k}h_rE_r
\]

after enlarging a single K to cover the sum of the two backward discrepancies.
There is no term K E_k on the right requiring absorption and no Lipschitz
constant in the total number of source coordinates.

The bounded-prefix induction is consequently valid in this order:

| New coefficient row | Coefficient rows needed for its response bound |
| --- | --- |
| a^2_k | Past b^2 |
| a^3_k | Current a^2_k and past b^3 |
| b^3_k | a^3 through time k; no backward row |
| b^2_k | Current a^2_k and b^3_k, with the earlier rows |

Source variances and learned-moment errors were already bounded independently
in Section 2. Thus their use at a stage does not add a dependency on an
unconstructed current row. The moment arguments also respect this order:
q^2_k is needed only after b^3_k, and q^1_k only after b^2_k.

For completeness, if the induction hypothesis is (66), then

\[
 \epsilon+I_k
 \le\epsilon\left[1+\sum_{r<k}Kh_r
                    \prod_{v<r}(1+Kh_v)\right]
 =\epsilon\prod_{r<k}(1+Kh_r).
\]

The amplitude bound (65) makes each newly constructed discrepancy at most
1/2, so it fits strictly inside A=A_0+1 or M=M_0+1. The recurrence for E_k
then establishes (66) for the completed node. At k=0, C_0 and the top delta
are zero, giving b^3_0=0; the middle backward input and b^2_0 are then zero.
The induction has a valid base and makes no simultaneous assumption about
the four unknown current rows.

The current entries (68)--(69) are correct: partial_{xi^3_k} C_k=0 and
partial_{xi^3_k} Z^3_k=I, whereas
partial_{xi^2_k} q^2_k=b^3_{kk}G^2_k. Thus the middle return is V^2_k
b^3_{kk}G^2_k, with the sample-b gate in the correct column. Both current
blocks are diagonal here, and both are O(epsilon). They are included in the
row comparison rather than removed by a support convention or an inverse.

## 6. Endpoints and conclusion of the audit

The forward zero extension for j>=k and the convention h_N=0 make the
terminal forcing expressions well-defined; no actual zero mesh step is
divided by in (11) or (53). Every such division has j<k<=N and h_j>0.
For S=0 there are no updates and the backward assertions are immediate.

Input geometry and labels enter only through |P|<=1, |c^T|=1, and the stated
source covariance identities. Formal derivatives retain separate named
arguments when a covariance is singular. The allowed finite-program theorem
handles those singularities by fixed-program regularization; its constants
are not imported as uniform estimates over growing meshes. In particular,
rho=-1, arbitrary label signs, and zero initial backward sources create no
unverified Gram condition in this proof.

After the coefficient induction, the earlier coordinate moment estimates
apply to every node, proving (11)--(12). The derivative-envelope estimates also
prove (70). The optional inheritance of the exponential moment by a weak
limit is valid by testing bounded continuous truncations of exp(X^2/L^2),
then using monotone convergence; it asserts no existence of such a limit.

No mathematical revision is required for the candidate's stated conditional
scope. The final candidate is unchanged.
