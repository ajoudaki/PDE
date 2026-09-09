# Independent adversarial review C

## Verdict and source integrity

**Verdict: the stated finite GF/GD first-layer compactness theorem passes this audit. I found no required mathematical correction.** The proof establishes strong joint compactness of the two-sample first-neuron tuple, reconstruction of actual raw first-row increments and velocities, and convergence of all four node-controlled first-kernel entries along every stated Wasserstein-convergent subsequence. Its no-defect statements have the claimed first-layer kinetic meaning.

This verdict is for the actual dynamics, initialization, fixed-input assumptions, and conclusions in the supplied document. It does not certify a mean-field identification theorem, nor does it require any of the conclusions expressly excluded in Section 12.

Source reviewed:

/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md

| Integrity item | Value |
|---|---|
| Supplied SHA-256 | 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9 |
| SHA-256 before reading | 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9 |
| SHA-256 after the mathematical audit | 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9 |
| Source size | 1,623 lines; 66,690 bytes |
| Source edits | None |

I read the entire source, including its scope section and provenance appendix. I did not open any listed dependency, other mathematical file, history, other review, or other-agent material. The appendix was read solely as part of the specified source; its statements about earlier work were not used as mathematical evidence. No experiments, subagents, external mathematical sources, or heavy imports were used. The only mathematical input to this review was the specified source, checked by direct derivation. Source references below are to that file's sections, equation numbers, and one-based line numbers.

## Required corrections versus optional clarifications

**Required mathematical corrections: none found.** In particular, I found no missing factor of two, width factor, input-dimension factor, unjustified replacement of the finite readout by zero, circular GD stability premise, loss of same-neuron pairing, endpoint nullspace ambiguity, or weak-to-strong inference in the kinetic conclusions.

Two optional clarifications would make the existing elementary arguments more explicit:

1. In Section 8, lines 1159–1167, the transfer from finite empirical approximants to points in their closure uses the Wasserstein triangle inequality with a finite intermediate marginal. The finite-table argument extends directly by conditioning on its finitely many atoms. Stating that extension in one sentence would clarify why no general disintegration theorem is needed. The construction and its verification are supplied in this review below; this is not a missing hypothesis or a mathematical obstruction.
2. In Section 11, beginning at line 1400, replace “successive uniform time averages” with “averages on uniform partitions whose mesh tends to zero.” The following density argument already has exactly this meaning. This is a wording clarification, not a correction to the representative construction.

These optional points do not change the theorem, constants, probability quantifiers, topology, or convergence claims.

## Theorem-obligation coverage

| Obligation | Source coverage | Audit result |
|---|---|---|
| Actual architecture, sum loss, raw metric, and simultaneous GD convention | Section 1; (1)–(9), (22)–(24) | Correct, including every factor of n, d, and two |
| Global finite-width GF existence and uniqueness | (24)–(25), Section 2 | Finite-dimensional continuation follows from the raw-action bound |
| GF primal and transpose-query estimates | (26)–(33) | Derived from actual finite equations |
| GF row work and improved moments | (34)–(42) | Boundary terms and all moment constants check |
| Actual GD descent without assumed stability | (43)–(49), (60) | Bootstrap closes; threshold is deterministic and independent of m, d, rho |
| GD recomputed-field regularity and node work | (50)–(62) | Held/recomputed distinction, Taylor absorption, and terminal cell handled |
| Antiparallel endpoint with actual readout | (63)–(69) | Exact architecture and label identities recover the controlled field |
| Uniform strong velocity translations over every admissible width/outcome | (70)–(80) | Relative-gate estimate and removal of the GD step error are valid |
| Compact containment of the complete same-neuron tuple in strong W2 | (81)–(86), remainder of Section 8 | Finite projections, fourth moments, and explicit coupling construction suffice |
| Gaussian event probabilities and random-law measurability | (87)–(91), Section 9 | Constants, independence requirements, and probability quantifiers check |
| Population compatibility and raw-row reconstruction | (92)–(97), Section 10 | Closed constraints and fixed linear maps establish (15)–(17) |
| Population time representatives | Section 11 through (98) | Jointly measurable representatives exist without evaluating arbitrary L2 classes |
| Three strong L1 speed-density limits | (99)–(101) | Establish exactly (18), including every fixed measurable time subset |
| Every controlled-kernel entry and total raw speed | (102)–(105), endpoint check | Full matrix-valued L1 convergence and the four-entry sum identity hold |
| GF/GD dissipation distinction and observable compactness | (106), end of Section 11 | Correct; no interpolated GD dissipation identity is assumed |
| T=0 and explicitly excluded conclusions | End of Section 8; Section 12 | Correctly separated and sufficient for the stated theorem |

The detailed audit below covers all numbered equations (1)–(106), the unnumbered derivations between them, and the theorem's quantifiers.

## 1. Setup and exact normalization

Source: Section 1, lines 13–282; raw metric and gradients at lines 284–309.

Equations (1)–(3) are consistent. The matrix C is positive semidefinite with eigenvalues 1+rho and 1-rho, both in [0,2]. In the interior it is invertible; at rho=-1 it has rank one. Input dimension is fixed, and a given dimension only permits correlations that can actually be realized by the specified pair. No argument assumes the existence of an impossible input pair.

The Euclidean/Frobenius conventions in (2) are respected throughout. The activation satisfies the stated bounds: its second derivative has magnitude

\[
\frac{2|s|}{(1+s^2)^2}\le \frac{1}{1+s^2}\le1.
\]

The finite readout in (4) appears with the prediction factor 1/n. It must therefore remain in both reverse fields before any limiting operation. Direct differentiation gives

\[
\begin{aligned}
D f_a[\xi]
={}&\frac1n(\delta^{(1)}_a)^T\xi^{(1)}x_a
 +\frac1n(\delta^{(2)}_a)^T\xi^{(2)}h^{(1)}_a
 +\frac1n(h^{(2)}_a)^T\xi^{(3)}.
\end{aligned}
\]

Because the loss is the sum of squared residuals, with no half or sample average, its three Euclidean gradients are exactly (23). Applying the inverse raw metric weights yields:

| Block | Metric weight on squared Euclidean/Frobenius norm | Negative raw gradient |
|---|---|---|
| First matrix | d/n | \(\frac1d\sum_a c_a\delta^{(1)}_a x_a^T\) |
| Second matrix | 1 | \(\frac1n\sum_a c_a\delta^{(2)}_a(h^{(1)}_a)^T\) |
| Readout | 1/n | \(\sum_a c_a h^{(2)}_a\) |

Here c_a=-2r_a. Thus (6) is precisely raw-metric GF, and (7) is precisely simultaneous explicit Euler/raw GD for that same metric. The word “gradient” is not being used to conceal a different learning-rate normalization.

The GD interpolation convention is also adequate: first preactivations are affine on each cell because W^(1) is affine, while first activations are recomputed arctangents. Therefore the derivatives in (8) obey

\[
s_i^{(1)}=\phi'(z_i^{(1)})\odot v_i^{(1)}
\]

almost everywhere, even though s need not be a step function. Nonlinear deeper fields are recomputed unless barred; the kernel in (19) is expressly barred in GD. The velocity norms in (9) use unnormalized Lebesgue time and a strong L2 topology.

The theorem's assumptions (10) do not bound complete initial first rows. This is sufficient: all evolving first-layer quantities used here depend on those rows through the two evaluations, and raw first-row increments lie in the input span. The theorem reconstructs increments and velocities, not arbitrary initial orthogonal components.

## 2. Finite GF and transpose-query regularity

Source: Section 2, equations (22)–(33), lines 284–426.

**(24)–(25), existence.** Taking the raw inner product of the raw gradient with its negative gives exactly

\[
\dot\ell=-\|\dot W\|_{\rm raw}^2.
\]

At any fixed n,d this metric is positive definite and equivalent to the ordinary parameter-space norm. Consequently

\[
\|W(t)-W(s)\|_{\rm raw}
\le\sqrt{t-s}\left(\int_s^t\|\dot W\|_{\rm raw}^2\right)^{1/2}
\le\sqrt{(t-s)\ell(0)}.
\]

A solution approaching a finite maximal time therefore has a finite parameter limit. The smooth vector field has a local unique solution at that limit, giving an extension. The local contraction argument and this continuation argument prove global existence and uniqueness for every finite initial parameter state. No large-width or good-event condition is needed for this conclusion.

**(26)–(28), primal estimates.** Initially |f_a|<=B beta, so the initial residual norm is at most R0. Loss monotonicity keeps it there, and

\[
\sum_a|c_a|\le2\sqrt2\,|r|\le K_c^{\rm F}.
\]

The readout equation gives the coordinatewise bound beta+B K_c^F t. For each rank-one second-matrix update,

\[
\frac1n\|\delta_a^{(2)}(h_a^{(1)})^T\|_{\rm op}
\le \frac{M(t)\sqrt n\,B\sqrt n}{n}=B M(t).
\]

Integrating gives precisely A_F in (26), including the factor 1/2 in its quadratic-in-time term. Multiplication by the bounded gates and by W^(2) then gives all nondifferential estimates in (27).

Multiplying the first-matrix equation by x_a gives

\[
\dot z_a^{(1)}=\sum_b C_{ab}c_b\delta_b^{(1)}.
\]

Using |C_ab|<=1 yields each per-sample derivative bound in (27). The initial fourth-moment assumption implies each per-sample empirical L2 norm is at most m^(1/4), which proves (28) by integration. No coordinatewise bound on the first matrix or its reverse query is inserted.

**(29)–(31), genuine transpose differentiation.** The identities in (30) are exact product and chain rules. The estimates have the following origins:

\[
\begin{aligned}
\|\dot W^{(2)}\|_{\rm op}&\le K_cMB=D_A,\\
\|\dot W^{(3)}\|_\infty&\le K_cB=D_w,\\
\|\dot z_a^{(2)}\|/\sqrt n&\le D_AB+AK_cQ=D_Z,\\
\|\dot\delta_a^{(2)}\|/\sqrt n&\le D_w+MD_Z=D_\delta,\\
\|\dot q_a^{(1)}\|/\sqrt n&\le D_AM+AD_\delta=D_q.
\end{aligned}
\]

The crucial multiplication in the second reverse derivative is by the coordinatewise bounded readout. It does not require multiplying two uncontrolled empirical L2 fields. There is no independence assumption about a reused forward/transpose matrix.

**(32)–(33), prediction dynamics.** Inserting the three raw GF blocks into Df_a gives respectively

\[
C_{ab}\frac{\delta_a^{(1)T}\delta_b^{(1)}}n,\qquad
\frac{\delta_a^{(2)T}\delta_b^{(2)}}n
\frac{h_a^{(1)T}h_b^{(1)}}n,\qquad
\frac{h_a^{(2)T}h_b^{(2)}}n.
\]

Thus \(\dot r=kc=-2kr\), with exactly the kernel in (32). Each entry is bounded by K_*=Q^2+M^2B^2+B^2, so its operator norm is at most 2K_*. Since \(\dot c=4kr\), its l1 norm is at most \(8\sqrt2 K_*R_0\), exactly (33). Equivalently, the full raw speed is \(4r^Tkr\), in agreement with (24); there is no extra sample-average factor.

## 3. GF row work and moment gain

Source: Section 3, equations (34)–(42), lines 428–523.

**(34)–(38).** Differentiating u_a=c_a q_a and applying the empirical Euclidean triangle inequality across the two samples gives

\[
\left(\frac1n\sum_i\Big(\sum_a|\dot u_{a,i}|\Big)^2\right)^{1/2}
\le Q\sum_a|\dot c_a|+D_q\sum_a|c_a|.
\]

This is (36) with the declared K_u^F. Applying the same inequality to the initial value and time integral gives the envelope estimate (38), with precisely V_F=K_c^F Q_F+T K_u^F. Only this scalar envelope is auxiliary; u and q remain actual finite fields.

**(39), exact one-row identity.** Regarding a row as a column,

\[
\dot W_i^{(1)}=\frac{Xe_i}{d},\qquad v_i=Ce_i.
\]

Therefore

\[
d|\dot W_i^{(1)}|^2=e_i^TCe_i
=e_i^Tv_i
=\sum_a u_{a,i}\phi'(z_{a,i})v_{a,i}
=\sum_a u_{a,i}s_{a,i}.
\]

All equalities are valid for singular C as well. In particular the left side is an individual raw row energy multiplied by d, not an empirical mean or a separate energy for each sample.

**(40), integration by parts.** The action is nonnegative. Integrating u dot h' includes the u(T)h(T) and u(0)h(0) terms. Their bounds plus the variation term give

\[
B\bigl(|u(T)|_1+|u(0)|_1+\operatorname{Var}_1(u)\bigr)
\le2B\upsilon_i.
\]

The endpoint term was not omitted. This is the essential linear-in-envelope bound.

**(41)–(42), moments.** The eigenvalue bound on C gives \(|Ce|^2\le2e^TCe\), and \(|e_i|\le\upsilon_i\). Consequently

\[
|v_i|\le2\upsilon_i,\quad
\int|v_i|^2\le4B\upsilon_i,\quad
\int|v_i|^3\le8B\upsilon_i^2.
\]

Also |s_i|<=|v_i|. The position displacement is at most \(\sqrt{2T\mathcal A_i^{\rm F}}\); raising this to the fourth power and using \((a+b)^4\le8(a^4+b^4)\) gives the coefficient \(128B^2T^2\) in (42). Finally \(\|v_i\|_2^4\le16B^2\upsilon_i^2\), giving the stated \(4BV_F\) after empirical averaging and a square root. These are fourth moments of whole-path L2 norms and cubic moments under space-time measure, as required later. They are not merely uniform bounds on average quadratic action.

## 4. Actual GD descent: all premises checked

Source: Section 4, equations (43)–(49), lines 525–643; explicit threshold (60).

**(43), stopped bootstrap.** Stop at a candidate first residual exit. Every preceding update uses an admissible old node, so the readout and rank-one matrix bounds can be summed up to and including the candidate exit endpoint. Since N eta<=T+1=H, the bounds are M_G and A_G as written. Convexity extends those two norm bounds over each raw segment. This step does not presuppose loss descent.

**(44), first differentials.** For a raw unit tangent, \(\|\xi^{(1)}\|_F\le\sqrt{n/d}\), \(\|\xi^{(2)}\|_F\le1\), and \(\|\xi^{(3)}\|\le\sqrt n\). Input normalization gives

\[
\|\xi^{(1)}x_a\|/\sqrt n\le1.
\]

The differentiated second preactivation is \(\xi^{(2)}h_a^{(1)}+W^{(2)}[\phi'(z_a^{(1)})\odot \xi^{(1)}x_a]\), proving the more precise a_1,a_2 bounds in (44). The prediction derivative is bounded by \(Ba_3+M(Ba_2+Aa_1)\le F_*\).

**(45)–(46), Hessian normalization.** The displayed three terms are all mixed derivatives of the second preactivation: the two cross-matrix terms and the first-gate second derivative. After division by sqrt(n), their bounds are 1, 1, and A sqrt(n), respectively. In particular, the possible concentration of two first-preactivation tangent vectors was not mistakenly estimated at order one.

The second prediction derivative then has exactly four terms. The two readout cross terms sum to at most 2J0. The second-layer gate term satisfies

\[
\frac{M}{n}\sum_i
|D_\zeta z^{(2)}_{a,i}|\,|D_\xi z^{(2)}_{a,i}|
\le MJ_0^2;
\]

it incurs no sqrt(n) factor. The remaining term is at most \(M(2+A\sqrt n)\). Thus F_**(n) in (46) is a valid bound on the bilinear second prediction differential for raw unit tangents.

**(47), segment residual and loss Hessian.** At the old node the raw update speed is at most K_c F_*. Integrating Df along its actual straight segment bounds each prediction change by eta K_c F_*^2. This gives the residual bound \(R+\sqrt2\eta K_cF_*^2\le R+1\), under the first condition in (60). Hence

\[
\|D^2\ell\|_{\rm raw}
\le4F_*^2+2\sqrt2(R+1)F_{**}(n)=H_*(n).
\]

The sample count and factor two from the sum loss are correct here as well.

**(48)–(49), closing the induction.** Taylor's integral formula along the actual raw-gradient segment gives descent by at least eta/2 times its squared raw gradient norm when eta H_*(n)<=1. This bound is available on the candidate exit segment before assuming the endpoint is admissible. The candidate endpoint then has residual norm at most R0<R, closing the induction.

The summation of this descent inequality gives (49), with the factor 1/2 outside the complete raw action. This is a discrete inequality, not an equality of instantaneous loss dissipation with affine-interpolation speed.

All coefficients entering these conditions depend only on T, alpha, beta. The Hessian growth is a constant plus a constant times sqrt(n), so eta=n^(-2) makes both descent conditions true for all sufficiently large n. No bound on initial first-row coordinates, no good Gaussian event, and no assumption of continuous-time/GD closeness is required for the deterministic GD result.

## 5. GD query regularity, work, and moments

Source: Section 5, equations (50)–(62), lines 645–790.

**(50)–(53), recomputed fields.** The held old-node update bounds the raw segment derivatives. Applying the genuine product rules (30) to the recomputed nonlinear fields is valid almost everywhere; continuity at nodes then allows integration over cells. This gives (51). Also

\[
\sum_a|\dot c_a|\le4K_c^{\rm G}F_*^2,
\]

since each prediction derivative is at most F_* times the raw segment speed. The three finite-difference identities (52) have the correct old/new endpoint factors and imply the same node-increment estimates. The first-primal bound (53) follows from integration through at most H time units.

There is no substitution of a held nonlinear activation for the actual recomputed activation derivative. Residual norms are only claimed to be bounded by R+1 within segments; the stronger R0 bound is a node statement.

**(54)–(56), node-controlled envelope.** The exact identity

\[
\Delta(c_aq_a)=(\Delta c_a)q_{k,a}+c_{k+1,a}\Delta q_a
\]

gives (54), using already established endpoint control bounds. Summing the resulting empirical l2 bounds gives V_G. The envelope includes nodes 0 through N-1, exactly those producing velocities. It need not include u_N. The estimate \(\max_i\upsilon_i\le\sqrt n V_G\) follows directly from the empirical square bound, and is proved before it is used for Taylor absorption.

**(57)–(59), discrete row work.** The actual update gives

\[
\Delta z_i=\eta Ce_{k,i},\qquad
d|\Delta W_i/\eta|^2=a_{k,i},\qquad
|\Delta z_i|^2\le2\eta^2 a_{k,i}.
\]

For each sample, Taylor's remainder for its activation is at most \(|\Delta z_{a,i}|^2/2\). Multiplication by u and summation therefore yields

\[
|r_{k,i}^{\rm Tay}|
\le\frac12\upsilon_i|\Delta z_i|^2
\le\eta^2\upsilon_i a_{k,i}.
\]

The main Taylor term is \(\eta e_{k,i}^TCe_{k,i}\), with the correct sign and coefficient.

Discrete summation by parts produces exactly the displayed u_(N-1)h_N and u_0h_0 boundary terms and the interior variation terms. Its absolute value is at most 2B upsilon_i. Therefore, writing \(\mathcal A_i=\sum_k\eta a_{k,i}\),

\[
(1-\eta\upsilon_i)\mathcal A_i\le2B\upsilon_i.
\]

The third condition in (60) ensures eta upsilon_i<=1/2 and yields \(\mathcal A_i\le4B\upsilon_i\). This is not circular: the envelope bound depends on the preceding GD stability and query estimates, not on the row work inequality.

**(60), threshold dependencies.** With eta=n^(-2), the maximum-envelope error is at most V_G n^(-3/2). All three displayed conditions eventually hold and remain valid for every larger n. Their coefficients are independent of m, d, and rho.

**(61)–(62), moment constants and terminal cell.** The raw interpolated velocity is Ce_k on every cell. Thus

\[
\int_0^T|v_i|^2\le2\mathcal A_i\le8B\upsilon_i,\qquad
\int_0^T|v_i|^3\le16B\upsilon_i^2.
\]

The sum defining the action extends to N eta and dominates integration over a partial final cell. The displacement bound \(\sqrt{2H\mathcal A_i}\) gives the fourth-moment coefficient 512 B^2 H^2 in (62). The square root of the empirical fourth power of the velocity L2 norm is at most 8B V_G. The recomputed activation derivative has magnitude at most |v_i|, so the same estimates hold for it. The N=1 empty variation sum and a nonintegral T/eta cause no problem.

## 6. Antiparallel endpoint and recovery of the controlled vector

Source: Section 6, equations (63)–(69), lines 792–852.

At rho=-1, normalization gives x_2=-x_1. The bias-free linear maps and odd activations imply every forward relation in (63) for every parameter state. The arbitrary shared readout preserves f_2=-f_1; it need not vanish.

Evenness of phi' gives equality of the two second deltas, first transpose queries, and first deltas, exactly (64). Opposite labels then give r_2=-r_1 and c_2=-c_1. These imply (66), including the factor two in all three raw update blocks. They also apply at every GD node and inside every raw segment because they are identities of the architecture at arbitrary parameter values.

In particular u and e lie in \(E_-=\{(b,-b)\}\), as do the two-component positions and activation derivatives. On this space C acts as multiplication by two. Therefore

\[
v=Ce=2e,\qquad e=(C/4)v.
\]

This verifies (67); the interior inverse and its operator norm in (68)–(69) are correct. At the endpoint, D=C/4 has eigenvalues 0 and 1/2. In the interior its largest eigenvalue is 1/(1-|rho|).

This endpoint argument supplies a necessary piece of information beyond a generic pseudoinverse manipulation: a nullspace component of e would be invisible to v while affecting individual kernel entries. Here that component is exactly absent because of (63)–(65). The proof establishes its absence using the actual readout and actual labels. No fictitious one-sample initialization or zero-readout replacement is used.

## 7. Strong time translations, including all admissible GD widths

Source: Section 7, equations (70)–(80), lines 854–1043.

**(70)–(72), combined constants and increments.** The sqrt(2) in K_z correctly combines the two per-sample empirical derivative bounds into the Euclidean two-vector bound. J^3 is the empirical space-time cubic bound, while A_kin is the square root of the empirical fourth power of a whole-path L2 norm. These distinct moments are used in their proper roles.

Integrating the actual derivative bounds gives the GF shifts in (72). In GD, two times separated by tau cross at most tau/eta+1 node increments, giving tau+eta for the held controlled query and held gate positions. The unbarred first position integrates its actual affine velocity and has the sharper tau bound. The time integration contributes sqrt(T); no time normalization is suppressed.

**(73)–(74), relative gate.** Direct differentiation gives

\[
|(\log\phi')'(x)|=\frac{2|x|}{1+x^2}\le1.
\]

For positive gates A,B,

\[
\frac{|A-B|}{A+B}
=\tanh\left(\frac{|\log A-\log B|}{2}\right).
\]

This proves theta<=min(1,|x-y|/2). For a=phi'(x)u and b=phi'(y)v, the estimate in (74) follows by replacing phi'(x)|v| with |a|+phi'(x)|u-v|. It is valid for signed u,v, not only positive controlled fields. Taking the maximum of the two sample gate ratios and the Euclidean triangle inequality preserves the constants. There is no division by c, q, or a uniform positive gate lower bound.

**(75)–(76), preactivation velocity.** Since e=Dv, its empirical space-time L3 norm is at most kappa_rho J. Meanwhile theta lies in [0,1], so

\[
\int_{\rm emp,time}\theta^6
\le\int_{\rm emp,time}\theta^2
\le \frac14 T K_z^2(\tau+\epsilon)^2.
\]

Hölder with \(1/2=1/6+1/3\) gives exactly (75), including the factor two for the sum of the shifted and unshifted e norms. Multiplication by C costs at most two. Absorbing a linear power into a one-third power on [0,T+1], then squaring, proves (76). The allowed dependence on fixed rho occurs at precisely e=Dv.

**(77), recomputed activation velocity.** The difference of s splits into the gate times the velocity difference and the gate difference times the old velocity. The largest coordinate gate difference is bounded by min(1,|Delta z_i|). Its L6 norm is therefore bounded using the unbarred position shift, and another L6-L3 Hölder estimate proves (77). This uses the recomputed gate, as required for the actual activation derivative.

**(78)–(80), uniform removal of eta.** For tau<=eta a step velocity can change only across an internal node. There are at most T/eta such nodes, each affecting a starting-time interval of length at most tau. The empirical squared jump is at most 4K_z^2. This proves (78), including when there are no internal nodes.

Combining that estimate with (76) gives (79). For 0<tau<min(1,T), set delta=tau^(3/5). If eta<=delta, then tau+eta<=2delta and the first estimate is O(tau^(2/5)). If eta>delta, then tau<eta and the crossing estimate is O(tau/eta)<=O(tau^(2/5)). The activation estimate then gives (80). GF has the stronger squared exponent 2/3, which implies 2/5 on this interval.

This addresses the important quantifier: the translation bound holds uniformly over every outcome and every admissible width, not only along a sequence with eta tending to zero. Merely retaining the error (tau+eta)^(2/3) would not have sufficed for that claim; the source actually removes it.

## 8. Strong joint compactness and population-law limits

Source: Section 8, equations (81)–(86) and the following constructions, lines 1045–1198.

**(81)–(84), finite projections.** The velocity averaging map is a contraction in L2; polygonal interpolation is a contraction in the supremum norm. Their product has finite-dimensional range for each fixed partition. The notation h_1 for the activation argument prevents confusion with the mesh.

For a cell of length h, direct square expansion proves

\[
\int_I|v-v_I|^2=\frac1{2h}\int_I\int_I|v(t)-v(s)|^2\,ds\,dt.
\]

Splitting into ordered pairs cancels the factor two, and enlarging the within-cell pairs gives the coefficient 1/h multiplying the integral over shifts. Since

\[
\frac1h\int_0^h\tau^{2/5}\,d\tau=\frac57h^{2/5},
\]

the constant in (82) is correct.

For the continuous positions, the displayed absolute-continuity identity has two integral terms, each bounded by sqrt(h) times the cell's velocity L2 norm. Taking the supremum and bounding by the full time integral gives (83). The same estimate applies to the activation coordinate. The total squared transport bound in (84) is therefore exactly

\[
\varepsilon(h)=8hTK_z^2+\frac{5C_1}{7}h^{2/5}.
\]

Most importantly, this transport sends the complete tuple for neuron i to the projection of that same tuple. Neither sample nor either velocity coordinate is independently rearranged.

**(85), quadratic-tail control.** The tuple norm squared is the sum of four squared coordinate norms. Its square is at most four times the sum of their squares. The respective fourth-moment bounds are B_path, A_kin^2, 4B^4, and A_kin^2. This proves M4 in (85). The finite projections preserve that bound.

Consequently, outside a radius-R norm ball,

\[
\int \|\xi\|^2\mathbf1_{\{\|\xi\|>R\}}\,d\mu_n
\le M_4/R^2.
\]

Thus the finite-dimensional projection argument controls Wasserstein distance, not only weak convergence. Rare neurons cannot carry a nonvanishing amount of quadratic mass outside every bounded set while satisfying this bound.

**Finite-dimensional covers.** Moving projected mass outside the ball to zero costs at most M4/R^2. Quantizing the remaining bounded finite-dimensional ball costs at most delta^2. On the resulting fixed finite support, unmatched mass a can be transported at cost at most a times the squared support diameter. A finite grid in the probability simplex supplies a finite Wasserstein net. These facts prove total boundedness of all projected laws. Combining with (84) proves total boundedness of the union of all original admissible laws.

This union includes every admissible outcome at each fixed width. Its proof does not choose one initialization per width, discard finitely many admissible widths, or assume that fixed-width admissible parameter sets are themselves bounded.

**(86), existence of a measure limit.** The finite transport tables may be chosen with summable root-mean-square costs. Dividing by their finite marginal masses defines valid transition probabilities. Recursively partitioning a unit interval according to these probabilities realizes all finite transitions on one probability space; zero-mass rows can be ignored. In particular, the construction is not an appeal to an unproved coupling of infinitely many arbitrary population laws.

The sum of the expected successive distances is finite, so the sum of those distances is finite almost surely. Completeness of C and L2 then gives an almost-sure limit in the product path space. Moreover,

\[
\left(\mathbb E\|\xi_j-\xi\|^2\right)^{1/2}
\le\sum_{k\ge j}
\left(\mathbb E\|\xi_{k+1}-\xi_k\|^2\right)^{1/2}
\longrightarrow0.
\]

This also bounds the limit's second moment. Separability ensures the limit is a legitimate measurable path-space random element. Thus its law is a W2 limit, with the strong velocity topology intact.

For completeness, the extension of the finite gluing argument used when passing to the closure is elementary. If the intermediate measure is

\[
\sigma=\sum_jp_j\delta_{y_j},
\]

a coupling of lambda with sigma provides conditional measures gamma_j on the first coordinate, obtained by dividing its restrictions by p_j. A coupling of sigma with nu similarly provides theta_j on the last coordinate. The triple law

\[
\sum_{j:p_j>0}p_j\,\gamma_j\otimes\delta_{y_j}\otimes\theta_j
\]

has both desired pair marginals. The pointwise triangle inequality followed by the L2 triangle inequality bounds the root-mean-square endpoint distance by the sum of the two costs. Arbitrary couplings can be approximated at their infima. This proves every finite-intermediate triangle inequality needed to approximate closure points by finite empirical measures and transfer their convergence. There is no unresolved measure-theoretic obstruction in the closure step.

**Compact closure and direct tightness.** Approximating a sequence in the closure within 1/j by union points and taking the preceding subsequence gives sequential compactness of the closure. The open-cover argument in the source is valid: otherwise one can find points with radius-1/j relative balls contained in no cover member; a convergent subsequence contradicts openness at its limit. A finite net then gives a finite subcover.

The separate compact path-space set C is closed, and its uniform approximation by bounded finite-dimensional sets makes it totally bounded. Completeness makes it compact. The probability outside it is bounded by

\[
M_4/R^4+\sum_{j\ge1}2^{2j}\varepsilon(h_j)
\le a/2+(a/2)\sum_{j\ge1}2^{-j}=a.
\]

This independently verifies tightness, while (85) supplies uniform quadratic tails.

**T=0.** At zero horizon both L2 spaces are zero spaces. Only the initial two-vector and its activation remain, in a finite-dimensional setting with a uniform fourth-moment bound. Raw increments are zero and all L1 time observables are the zero class. No positive-time translation, division by T, or GD work estimate is needed. The theorem's inclusion of T=0 is therefore valid.

## 9. Gaussian initialization and probability quantifiers

Source: Section 1, (12)–(14); Section 9, (87)–(91), lines 1200–1308.

**(12), actual initialization.** For each first row, Gaussian covariance is

\[
\mathbb E[z_{a,i}^{(1)}(0)z_{b,i}^{(1)}(0)]
=\frac{x_a^Tx_b}{d}=C_{ab}.
\]

Different rows are independent because the entries of W^(1) are independent. This holds for every fixed deterministic normalized pair and dimension, including the degenerate antiparallel pair. No independence of later neuron trajectories is required.

**(87)–(88), first-row moment event.** Gaussian integration by parts gives E G^4=3 and E G^8=105. For the represented pair (G,Y), E G^2Y^2=1+2rho^2. Therefore

\[
\mathbb E|(G,Y)|^4=3+3+2(1+2\rho^2)=8+4\rho^2\le12.
\]

Also

\[
(G^2+Y^2)^4\le8(G^8+Y^8),
\]

so the eighth moment is at most 1680. Independence across rows bounds the variance of the empirical fourth moment by 1680/n. Its mean lies at least one below the threshold 13, and Chebyshev gives (88). The proof does not confuse a fourth moment of a two-vector with a fourth moment of an individual sample coordinate.

**(89), middle-matrix operator norm.** A maximal 1/4-separated sphere subset is a 1/4-net. Disjoint radius-1/8 balls fit inside the radius-9/8 ball, giving at most 9^n net points. Approximating both test vectors costs at most half the operator norm, so the operator norm is bounded by twice the largest net bilinear form.

Each such form has variance

\[
\frac1n\sum_{i,j}u_i^2v_j^2=\frac1n.
\]

Its two-sided tail above four is at most 2 exp(-8n). There are at most 9^(2n) pairs. The resulting bound is exactly \(2e^{-(8-2\log9)n}\); the exponent coefficient is positive. No sharp random-matrix theorem is being implicitly used.

**(90), readout event.** A readout coordinate has variance n^(-2), so its tail above one is at most \(2e^{-n^2/2}\). A union bound gives \(2ne^{-n^2/2}\). This event bounds the actual nonzero Gaussian readout. It does not replace that readout by its limiting value.

**(13)–(14), containment.** Adding the three failure estimates gives b_n exactly. Independence between the three events is unnecessary. On E_n, the initial deterministic hypotheses hold with (alpha,beta,m)=(8,1,13), and both schemes belong to the same compact family for n beyond the deterministic GD threshold. Common initialization therefore has joint failure probability at most b_n, not 2b_n. For separate initializations the union bound gives at most 2b_n even without invoking independence.

The event itself depends only on initialization and can be used for every fixed horizon; the compact set and admissible GD threshold may depend on that horizon. The probability bound is uniform over deterministic inputs and dimensions, whereas the strong compactness constant is allowed to depend on the fixed correlation.

**Measurability.** At fixed width, GD is a finite composition of continuous maps. Its interpolation partition is fixed, so the position paths and their piecewise velocity classes depend continuously on the initial parameter tuple. The recomputed activation derivative does also.

For GF, a bounded neighborhood of an initial point has uniformly bounded initial loss. The action bound places all corresponding finite-dimensional trajectories through T in one bounded ball. Smoothness supplies a Lipschitz constant there. Iteration of the difference integral inequality yields the stated exponential bound, and continuity of the vector field controls velocity differences. Pairing equal neuron indices then gives continuity of the empirical law in W2. Consequently its membership in the compact set is measurable.

**(91), exact integrability statement.** On E_n, the tuple-norm tail is at most M4/R^2. The velocity-value tail is bounded using

\[
|v|^2\mathbf1_{\{|v|>R\}}\le |v|^3/R,
\]

and hence is at most J^3/R. For any fixed tolerance, sufficiently large R makes these quantities below that tolerance on E_n; their failure probabilities are then at most b_n for large n. This proves the iterated probability limits.

These statements do not estimate an expectation over bad initialization events. The source explicitly avoids that inference. It also correctly avoids claiming eventual goodness almost surely over all widths from the nonsummable leading term 1680/n.

## 10. From finite same-neuron tuples to population fields and raw rows

Source: Section 10, (92)–(97), lines 1310–1396; theorem (15)–(17).

**Coupling and closed compatibility.** Every chosen coupling has a finite-neuron tuple as one marginal and the complete population tuple as the other. Its error is in the sum of the two uniform norms and the two strong L2 norms. No separate coordinate or sample-marginal convergence is substituted for joint convergence.

The primitive defect map is continuous because

\[
\left\|z-z(0)-\int_0^\cdot v
 -\left(z'-z'(0)-\int_0^\cdot v'\right)\right\|_\infty
\le2\|z-z'\|_\infty+\sqrt T\|v-v'\|_2.
\]

The arctangent relation is closed by its Lipschitz continuity. The activation-velocity relation is closed by (92): the term multiplying the gate difference is the fixed limit velocity, with finite L2 norm, and the other term converges strongly. The analogous activation primitive defect is also continuous. Hence the full set of tuples satisfying (15) is closed.

Every empirical atom belongs to this set. Its bounded distance function has population expectation at most the expected coupling distance, which tends to zero. The population law is therefore concentrated on that set. The same reasoning preserves E_- constraints at rho=-1. This justifies both the pathwise continuous identities and the L2 identities in (15); it does not presume point evaluation of an arbitrary L2 element.

**(93)–(95), exact reconstruction.** For the interior and for the established endpoint subspace,

\[
e=Dv,\qquad \dot W_i^{(1)}=\frac{XD}{d}v_i.
\]

In both cases D is symmetric positive semidefinite and DCD=D. Thus, for A_row=XD/d,

\[
A_{\rm row}^TA_{\rm row}
=\frac{DX^TXD}{d^2}
=\frac{DCD}{d}
=\frac Dd.
\]

This proves the exact raw-energy identity

\[
d|\dot W_i^{(1)}|^2=v_i^TDv_i
\]

and \(\|A_{\rm row}\|_{\rm op}^2=\kappa_\rho/d\).

At rho=-1, taking e=(b,-b) gives v=(2b,-2b) and raw row velocity 2b x_1/d. Its squared norm multiplied by d is 4b^2. Meanwhile |v|^2=8b^2 and v^TDv=4b^2. The source's factor 1/2 relative to the two-sample Euclidean velocity norm is correct.

**(96), increments and joint pushforwards.** Integrating the exact raw velocity gives the exact first-row increment \(A_{\rm row}(z_i-z_i(0))\). The map to increments and velocities satisfies

\[
\|\Delta R\|_\infty^2+\|\Delta B\|_2^2
\le \|A_{\rm row}\|_{\rm op}^2
\bigl(4\|\Delta z\|_\infty^2+\|\Delta v\|_2^2\bigr).
\]

It is therefore globally Lipschitz with the stated squared constant. Pushing the complete coupling through this map proves (17). Retaining the original coordinates adds their coupling cost and proves the asserted joint convergence.

The laws here concern the ordinary Euclidean increments and velocities of actual raw rows. The factor d needed for raw kinetic energy is applied separately. No normalized Frobenius convention is being introduced into the pushforward statement.

**(97), full-row limitation.** The matrix \(P=XD X^T/d\) is symmetric and idempotent. It is the orthogonal projection onto the input span; at the endpoint this follows directly from its action on the two opposite columns. All first-row velocities lie in this span. Consequently

\[
W_i^{(1)}(t)=A_{\rm row}z_i^{(1)}(t)+(I-P)W_i^{(1)}(0).
\]

The last term is constant and is absent from the two-evaluation law. This does not obstruct any reconstruction claimed in the theorem, which concerns increments and velocities. No additional full-row assumption is needed.

## 11. Population representatives, no kinetic defect, and every kernel entry

Source: Section 11, (98)–(106), lines 1398–1551; theorem (18)–(21).

### 11.1 Jointly measurable time representatives

Point evaluation is not a bounded functional on L2. The source does not use it as one.

For partitions with mesh tending to zero, the time-average maps P_h converge strongly to the identity on L2. To verify this directly, first check interval-step functions: any discrepancy is supported in shrinking cells near finitely many endpoints. Their density and the contraction property give convergence for arbitrary L2 functions. The stated density construction uses approximation of Lebesgue measurable sets in measure by finite unions of intervals on the bounded time interval.

The map \((v,t)\mapsto(P_hv)(t)\) is measurable: each of its finitely many time coefficients is a bounded linear functional of the L2 class. Moreover

\[
\|P_hv-v\|_2^2\le4\|v\|_2^2.
\]

The population has finite second moment, so integrating over its path variable proves convergence in \(L^2(\mu\times dt)\). Selecting a subsequence with summable increments in that space gives a jointly measurable almost-everywhere limit. By Fubini and the already known pathwise L2 convergence of the time averages, its section represents the prescribed velocity class for almost every population tuple.

The same construction applies to S. It proves (98), and Cauchy–Schwarz then makes all products used for energy and kernel entries integrable on the product space. Changes on product-null sets do not alter the resulting scalar or matrix L1 time classes. Pulling these representatives into any coupling is legitimate because its population marginal is exactly mu.

Thus the passage from finite same-neuron tuples to population representatives is complete. It neither chooses arbitrary incompatible representatives for each time nor asserts convergence at a fixed time of an L2 path.

### 11.2 No kinetic defect in all three claimed densities

Under the chosen coupling, let \(\varepsilon_n\) bound the root-mean-square complete tuple distance. Then

\[
\left(\mathbb E\|v_n-V\|_2^2\right)^{1/2}\le\varepsilon_n,\qquad
|M_n-M|\le\varepsilon_n.
\]

For the first speed density,

\[
\begin{aligned}
\int_0^T\left|\mathbb E|v_n(t)|^2-\mathbb E|V(t)|^2\right|dt
&\le\mathbb E\int_0^T |v_n-V|(|v_n|+|V|)\,dt\\
&\le\varepsilon_n(M_n+M).
\end{aligned}
\]

Here Cauchy–Schwarz is applied on time times the coupling space, followed by the triangle inequality for its L2 norm. This is (99), and the two marginal expectations are respectively the exact empirical density and the population density. The same argument applies to s_n and S.

For the raw row density, (93) gives

\[
g_n^{(1)}=\frac dn\|\dot W_n^{(1)}\|_F^2
=\frac1n\sum_i v_i^TDv_i.
\]

The pointwise quadratic difference bound costs \(\|D\|_{\rm op}=\kappa_\rho\), so (100) follows. No lower-semicontinuity argument is being upgraded to equality: the convergence is directly strong enough to bound the absolute L1 difference of the quadratic densities.

Equation (101) follows for every fixed measurable time set A by bounding its integral error by the full L1 norm. In particular there is no unaccounted kinetic mass in time or in rare neurons for these observables. This concerns the two first-neuron speeds and the normalized raw first-matrix speed. It does not claim absence of an energy defect in unproved all-layer limits or in expectations over external initialization randomness.

### 11.3 All four controlled entries, with signs and factors explicit

For GF, e is instantaneous; for GD, e is evaluated at the held old node producing v. Since each control is common to the neurons of its sample,

\[
\begin{aligned}
j_{n,ab}^{(1)}
&=c_ac_b C_{ab}\frac1n\sum_i\delta_{a,i}^{(1)}\delta_{b,i}^{(1)}\\
&=C_{ab}\frac1n\sum_i e_{a,i}e_{b,i}\\
&=C_{ab}\frac1n\sum_i(Dv_i)_a(Dv_i)_b.
\end{aligned}
\]

This is the exact identity (102). Because c_a=-2r_a, the residual form contains the correct factor \(4r_ar_b\). Neither control convergence nor division by a control is necessary.

For an interior correlation, write, for each finite or population velocity,

\[
p=\frac{v_1-\rho v_2}{1-\rho^2},\qquad
q=\frac{v_2-\rho v_1}{1-\rho^2}.
\]

The matrix contributed by that velocity is exactly

\[
\mathcal H(v)=
\begin{pmatrix}
p^2&\rho pq\\
\rho pq&q^2
\end{pmatrix}.
\]

Thus the limiting four entries are

\[
J_{11}=\mathbb E_\mu p^2,\quad
J_{12}=\rho\mathbb E_\mu pq,\quad
J_{21}=\rho\mathbb E_\mu pq,\quad
J_{22}=\mathbb E_\mu q^2.
\]

The off-diagonal expectation is taken with both sample coordinates from the same population tuple. Replacing the joint law by separate sample marginals would not justify these entries; the source never does so. When rho=0 the two off-diagonal entries vanish exactly. The formula does not divide by rho.

The four-entry sum is

\[
p^2+2\rho pq+q^2
=v^TDv
=\frac{v_1^2-2\rho v_1v_2+v_2^2}{1-\rho^2}.
\]

At rho=-1, write v=(w,-w). Then Dv=(w/2,-w/2), and

\[
\mathcal H(v)=\frac{w^2}{4}
\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\sum_{a,b}\mathcal H(v)_{ab}=w^2=v^TDv.
\]

With w=2b this is the source's b^2 matrix and row energy 4b^2. Its trace is only half its full-entry sum. This checks the endpoint sign and rules out interpreting the speed identity as a trace identity.

### 11.4 Full matrix L1 convergence

For arbitrary e,f in R^2,

\[
ee^T-ff^T=(e-f)e^T+f(e-f)^T
\]

and the ordinary Frobenius norm of an outer product is the product of its vector norms. Therefore

\[
\|ee^T-ff^T\|_F\le|e-f|(|e|+|f|).
\]

Entrywise multiplication by C is a Frobenius contraction because every entry has magnitude at most one. Setting e=Dv and f=Dw and integrating proves (104), with the factor \(\kappa_\rho^2\), not \(\kappa_\rho\). In particular H has quadratic growth and is a continuous map from strong L2 to matrix-valued L1.

Moving the difference inside the coupled expectation and applying Cauchy–Schwarz yields

\[
\|j_n^{(1)}-J^{(1)}\|_{L^1(F)}
\le\kappa_\rho^2\varepsilon_n(M_n+M)\longrightarrow0.
\]

This is (105). It controls all four entries simultaneously. It is stronger than convergence of the trace or four-entry sum, and does not depend on recovering the unweighted kernel.

For every velocity vector, DCD=D gives

\[
\sum_{a,b}\mathcal H(v)_{ab}
=(Dv)^TC(Dv)=v^TDv.
\]

This proves both identities in (21). Also

\[
a^T\mathcal H(v)a=(a\odot Dv)^TC(a\odot Dv)\ge0,
\]

so positivity of the finite matrices and of a population almost-everywhere representative is justified. Positivity is an additional check, not a replacement for entrywise convergence.

The representative construction gives an almost-everywhere formula for the limiting L1 function. L1 convergence does not imply almost-everywhere convergence of the complete sequence; the source explicitly states this distinction.

### 11.5 Actual GD loss derivative and compactness of observables

In an affine GD cell, the raw velocity is the fixed vector -g_k. Applying the chain rule at the current raw state gives exactly

\[
\frac d{dt}\ell(W(t))
=-\langle\operatorname{grad}_{\rm raw}\ell(W(t)),g_k\rangle_{\rm raw}.
\]

This proves (106) and explains why the node-controlled kernel is tied to raw interpolation speed without asserting the instantaneous GF dissipation identity for GD.

The pushforward to raw increments/velocities is Lipschitz on tuples. The three density maps and the matrix expectation map are continuous on P2 because every W2-convergent sequence admits the coupling estimates above and has bounded second moments. These maps are defined on the whole P2 space; on the admissible compact set their values coincide with the actual finite observables.

The joint image of that compact set, retaining the original law, is therefore compact. Under initialization E_n, all actual observables lie in it, so the same probability bound applies. This final compact-containment conclusion needs no limit of controls or residuals as additional coordinates.

## 12. Premise and scope checks

Source: theorem (10)–(21); Section 12, lines 1553–1597.

The deterministic arguments use precisely the architecture and hypotheses that are stated:

| Premise or potential obstruction | Resolution in the source |
|---|---|
| Arbitrarily large initial first-row coordinates or orthogonal components | Bounded gates control finite estimates; only the two-evaluation fourth moment enters position compactness; orthogonal row components are constant |
| Large neuronwise transpose queries despite an operator bound | The proof uses empirical query bounds and an L2 envelope, not a nonexistent coordinatewise uniform bound |
| Possible finite-time GF blowup | Raw dissipation gives a Cauchy endpoint at every finite terminal time |
| GD loss descent used before it is known | Stopped segment bounds and a raw Hessian estimate close the exit contradiction first |
| Taylor error depending on a maximal neuron | The previously proved envelope bounds it by V_G n^(-3/2), then absorbs it |
| Widths remaining fixed while taking different initial outcomes | The uniform step-crossing estimate proves a common translation modulus for all such outcomes |
| Singular C at rho=-1 | Actual parity and opposite labels force e into E_-, eliminating the invisible component |
| Vanishing residual/control | Every kernel argument uses e=c delta directly and never divides by c |
| Mismatched two-sample marginals | Full neuron tuples are transported jointly at every projection and coupling step |
| Undefined pointwise L2 evaluation | Jointly measurable time representatives are constructed from averaging maps |
| Concentration of kinetic mass | Fourth tuple moments prove W2 compactness; strong velocity couplings give explicit L1 quadratic-error bounds |
| False identification of GD cell loss dissipation with node speed | Equation (106) states the actual derivative and preserves the distinction |
| Bad-event expectations or almost-sure full-width assertions | Neither is inferred from compact containment in probability |

There is no implicit assumption of zero readout, neurons remaining independent during training, an independently resampled transpose matrix, bounded reciprocal controls, uniform nonvanishing gates, an initial first-matrix operator bound, or an all-layer limit.

The final deterministic compact set supports extraction from any sequence of good outcomes, including either scheme or interleavings. Conditional on any W2-convergent subsequence, the compatibility and observable arguments depend on its own limiting law. They do not assert uniqueness or equality of limits from different sequences.

The probability conclusions assert compact containment and the stated empirical integrability in probability. A population-neuron expectation under a limiting law is not an expectation over the original initialization. The source maintains that distinction.

The explicitly excluded claims are not needed for the proof:

- An identified or unique mean-field evolution, convergence of the whole width sequence, or equality of GF and GD limits.
- Strong compactness or kinetic identities for unproved second-layer/population objects.
- Recovery of the unweighted kernel or equality with a kernel recomputed inside GD cells.
- Almost-everywhere time convergence of the complete kernel sequence.
- Expectation-level bounds on bad initialization outcomes.
- The endpoint rho=1, uniformity as rho varies toward endpoints, full raw-row laws without the initial orthogonal component, or matching original neuron indices across widths.

The stated further-subsequence almost-everywhere observation is valid: select summable L1 errors, integrate their pointwise sum, and conclude almost-everywhere convergence on that further subsequence.

## Final assessment

Every stated theorem obligation is discharged by the supplied proof within its actual finite GF/GD, first-layer scope. The raw metric normalization, row work estimates, GD stability premises, same-neuron compactness, population representative construction, all four controlled-kernel entries, and first-layer no-kinetic-defect statements are valid.

Required mathematical changes: **none found**. The two clarifications identified above are optional exposition only. The source's provenance claims were not needed or independently consulted, and the source was not edited.
