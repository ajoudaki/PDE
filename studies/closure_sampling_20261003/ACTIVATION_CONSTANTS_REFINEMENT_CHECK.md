# Independent internal reconstruction of the actual tanh constants

**2026-10-04 check-only arithmetic correction:** the manually reduced
depth-two constants in Section 7 are corrected in Section 9. The frozen
candidate, its two reproduced numerical tables, and the PASS verdict are
unchanged. The original manual paragraph is preserved for provenance.

2026-10-04. **PASS within the stated inherited interfaces.** The candidate's
activation and operator bounds, separated source/runtime constants,
restored activity factors, label restrictions, radius and storage formulas,
and deterministic tables pass reconstruction. Section 5 below supplies
explicit nested pole stops for the enlarged radius; this is a proof
clarification requiring no changed hypothesis, radius, or final constant.

Checked candidate: ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md, SHA-256
407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660.
The full candidate, including its evaluator, was read. Required canonical
notation and neural conventions, rigorous-proof instructions, and research
contract and audit instructions were applied. All scientific dependencies
used are from the assigned study and are listed below. No other study or
sibling review was read. No training experiment, Git operation, manuscript
change, or promotion was performed.

The candidate keeps ordinary tanh at every hidden layer of the canonical
Gaussian reference network. It substantially improves a sufficient
certificate, but still has exponential depth dependence in the angular
radius and large error constants. The conclusion remains asymptotic at
fixed architecture and data, with an unquantified stochastic width threshold.

## 1. Model and exact quantities

For \(v=x/\sqrt d\in S^{d-1}\), the dense model is

\[
z^{(1)}=Av,\quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\quad
h^{(\ell)}=\tanh z^{(\ell)},\quad f_n=w^\top h^{(L)}/n.
\]

It has width \(n\), hidden depth \(L\ge2\), independent standard Gaussian
first weights, independent \(N(0,1/n)\) hidden mixer entries, and
\(w(0)=0\). The loss and physical mobilities are exactly the candidate's
mean squared loss and \((n,1,\ldots,1,n)\). The compressed representation
is the inherited autonomous corrected-readout system, with its own
residual and moving hidden weights.

Let \(Q^{(0)}_{ab}=v_a^\top v_b\) and
\(Q^{(\ell)}_{ab}=\mathbb E[\tanh Z_a\tanh Z_b]\) for
\(Z\sim N(0,Q^{(\ell-1)})\). Set
\(\gamma=\lambda_{\min}(Q^{(L)})>0\),
\(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m\), \(u=Y/\lambda\), and
\(\ell_n=\log(en)\). Since every diagonal of \(Q^{(L)}\) is at most
one, \(\gamma\le1\) and \(\lambda\le1\), so the old gap cap is inactive.
There is no missing sample normalization.

The proposed joint condition is \(0<u\le c_L\), where all constants
defining \(c_L\) are finite recurrences in \(L\). The source tolerance is
\(\epsilon=n^{-1}\), its horizon is \(T=32\lambda^{-1}\ell_n\), and
its activity allowance is \(S=16u\). Labels retain arbitrary signs.
The error is uniform over all sphere queries and all physical times,
including the fitted endpoint, for the same realized dense initialization.
Zero labels are stationary and are covered separately.

## 2. Activation and initialization bounds

The outer strip \(a=1/2\) has value bound \(B=1\). Writing
\(v=\sinh^2x\), \(b=\sin^2y\) temporarily, one has

\[
|\tanh(x+iy)|^2=\frac{v+b}{v+1-b},\quad
|\tanh'(x+iy)|=\frac1{v+1-b},\quad
|\tanh''(x+iy)|^2=\frac{4(v+b)}{(v+1-b)^3}.
\]

For \(|y|<1/2<\pi/4\), the first ratio is at most one. On the safe
strip \(|y|\le1/4\), \(\cos y\ge31/32\), and hence the first
derivative is at most \(1024/961<16/15=s\).
For the last ratio, \(b<1/4\) and the maximum over \(v\ge0\)
occurs at \(v=(1-4b)/2\). Its square root is
\(4/(3\sqrt3\cos(2y))\). Since
\(\cos(2y)\ge7/8\), this is at most \(32/(21\sqrt3)<1=t\).
All stated complex bounds are valid. The three real bounds are at most
one, so the runtime may use \(B_{\rm rt}=1\).
Higher derivatives required by local insertion remain bounded on a
slightly larger strip by Cauchy's formula; they do not enter the displayed
persistent constants.

For a fixed unit vector \(v\), \(n\|W_0v\|^2\) is chi-square with
\(n\) degrees of freedom. Its moment-generating function and Markov's
inequality give

\[
\Pr\{\|W_0v\|^2\ge q\}\le
\exp[-n(q-1-\log q)/2]\qquad(q>1).
\]

A \(1/8\)-net has at most \(17^n\) points and gives
\(\|W_0\|_{\rm op}\le(8/7)\max_{\rm net}\|W_0v\|\).
At \(q=(49/16)^2\), the proposed matrix cap is \(7/2\).
Using \(\log q<7/3\),

\[
\frac{q-1-\log q}{2}>\frac{4643}{1536}>3>\log17.
\]

Thus the union bound tends to zero exponentially at fixed depth.
The strict initialized cap \(K_0=7/2\) is justified without a sharper
random-matrix theorem. Rectangular cavities are restrictions and keep
the same norm bound with the original normalization.

For \(A_0/\sqrt n\), a \(1/4\)-net of the fixed-dimensional input
sphere has at most \(9^d\) points. Image threshold \(3/2\), followed by
the net factor \(4/3\), proves strict operator cap two with probability
tending to one. This is a fixed-\(d\) statement, as required.

The real fitting energy proof gives hidden displacement at most \(1/4\)
under the displayed \(c_{\rm src}\). Therefore a strict initial cap
\(7/2\) stays below \(15/4\). The first-weight condition
\(2sK_1S^2\le1\) bounds its normalized displacement by \(1/2\).
Short complex continuation then leaves hidden mixers below four and the
normalized first matrix below three eventually. The query derivative
starts at six because the intrinsic input derivative has norm at most
two. The smaller physical caps are supplied by these arguments, rather
than assumed in place of the original initialization.

## 3. Source and label recurrences

The candidate's recurrences are obtained by substituting

\[
B=1,\quad s=16/15,\quad t=1,\quad
R_{\rm real}=15/4,\quad R_{\rm complex}=4
\]

in the exact label and endpoint identities. Here \(4s=64/15>1\).
In particular the ancestor external-trace domination that replaces an
insertion layer by the first layer is valid for this candidate.
It must not be generalized to subunit propagation gains without a
replacement, but no such replacement is needed here.

The augmented derivative recurrence \(P_1=2\),
\(P_j=2+4sP_{j-1}\) still includes a unit external injection at any
one layer. Backward coefficients start from \(K_L=2\).
The Hessian coefficients \(A_H,D_H,H_2\), direct trace \(E\),
singleton coefficients \(D_0,D_1\), and activity moduli all match the
complete label-route definitions with these substitutions. The query
coefficients \(j_j=6(4s)^{j-1}\) and their mixed endpoints use the
new first-matrix cap; the other endpoint terms are unchanged.

Every nonvanishing source requirement remains visible in the minimum
defining \(S_*\): real activity at most one, \(SA_H\le1/4\),
\(D_HS^2/\eta\le1/4000\), the asymmetric trace convergence condition,
\(S^2[\log(e+\mathcal B)+\log(1/\eta)]/\eta\le1\), endpoint feedback,
and the first-weight margin. The exponent \(\eta\) still controls
the Gaussian modulus and the fixed singleton shift, with budget
\(\mathcal B=64e^2L\). No activity requirement was dropped when the
physical operator caps were reduced.

The actual training-carrier statement is
\(\max|k|\le K_{\rm src}S\sqrt{\ell_n}\), with
\(K_{\rm src}=32\max(1,\max K_j,\max sK_j)\).
It is normalized by the allowed activity \(S\), not by an asserted
lower bound on the realized activity. The source event and fixed-order
stop removal are inherited with their original order of limits.

## 4. Separating the runtime source constants

The source approximation supplies coordinate error \(\epsilon\) for
each member of an initialized image pair, so its error multiplier is
one. The source carrier multiplier is a different quantity.
Exact source isometry and \(D/4\preceq H\preceq D\) give selected
coordinate-error norm at most \(2\epsilon\).
For paired approximants \(s,W_0s\), the initialized action is exact.
Subtracting the actual source and its image therefore gives defect

\[
\|B_0u_I-(W_0u)_I\|_H
\le2K_0\epsilon+2\epsilon
=2(K_0+1)\epsilon.
\]

This justifies the changed term of \(A_0\). Each image's approximation
error is controlled separately; it is not deduced by applying an operator
bound to a coordinate error.

The pairing and response transfers consequently use
\[
P_h=17,\quad P_\delta=18\beta+11,\quad
D_\delta=3\beta+3,\quad W=64,
\]
with the candidate's backward coefficient
\(\beta_j=2(2R)^{L-j}\), \(R=15/4\). The gate norm and changed-gate
Lipschitz coefficient are both bounded by two in the fixed metric,
because the real first and second derivatives are at most one.
Thus the old runtime envelope \(L(2R)^L\) is valid: its propagation
factor \(2R=15/2\) exceeds one.

Inspecting the complete explicit runtime proof shows that the source
coefficient's other role is the direct carrier bound
\[
M\le1+16K_{\rm src}u\sqrt{\ell_n}.
\]
Its integrated comparison exponent is therefore
\[
G_{\rm rt}(8+W/2)u
 +64K_{\rm src}G_{\rm rt}u^2\sqrt{\ell_n},
\]
which gives \(C_1=40G_{\rm rt}\) and
\(C_2=64K_{\rm src}G_{\rm rt}\), exactly as stated.
The remaining runtime recurrences, the conditions \(224FUu^2\le1\)
and \(6J_0u\le1\), the exact geometric cancellation, and the two
model tail bounds retain their meanings. No hidden appearance of the
larger \(K_{\rm src}\) remains in a coordinate-error estimate.

## 5. Restored activity factors, smaller Gaussian multiplier, and poles

For the spherical query grid of at most \(n^{4d+10}\) points eventually,
the tail at \(G_d\sigma\sqrt{\ell_n}\), with
\(G_d=4\sqrt{d+3}\), is at most
\[
4\exp[-(4d+12)\ell_n].
\]
The union is \(O(n^{-2})\), enough for the fixed-confidence source event.
The fixed multiplicities and grid prefactors only change the threshold.
The local insertion event retains its separate stronger Gaussian
concentration argument. Off-grid interpolation and strict response-cap
margins are unchanged.

Each same-root angular correction has one exterior activity factor \(S\)
and a training response bounded by
\(sK_{\rm src}S\sqrt{\ell_n}\). The learned-row correction has the
same two factors. At layer one, integrating the first-weight update gives
the same \(S^2\). There is no inverse \(S\) in the trace coefficient
\(T_J\), because the endpoint is an unnormalized query derivative.
Consequently every retained \(S^2\) in equation (13) is justified.

Let \(b_*=6s(4s)^{L-2}\), as in the candidate. Its angular cap gives
\[
2sK_{\rm src}S^2\le1,\qquad
sK_{\rm src}S^2(T_J+Bb_*)\le1.
\]
Since \(b_*\ge2\), the first-layer and later-layer formulas both satisfy
\(V_*^{\rm qry}\le2G_db_*+4\).
The time response bound is \(U_*\le A_U+B_UG_d\).
For \(u\le c_{\rm time}\), using \(YS=16u^2\lambda\le16u^2\)
gives precisely
\[
8c_tYSU_*\le128u^2(A_U+B_U)\le a/8,\qquad
c_qV_*^{\rm qry}\le a/8
\]
at
\[
c_t=1/G_d,\qquad c_q=a/(16G_db_*+32).
\]
Both coefficients are at most \(1/8\) for \(d\ge2\).
The total displacement is at most \(a/4\), as asserted.
For \(d=1\), the two queries require only \(G_1=8,c_t=1/8\).

To make the inherited local-interface margin fully explicit, one need
not double a pole cap all the way to the boundary of the derivative
strip. Choose the full-system pole stop at \(3a/8\) and each autonomous
cavity pole stop at \(7a/16\). Their difference is the fixed positive
margin \(a/16\), and both lie strictly inside \(|\Im z|<a/2\).
The local coordinate differences are \(o(1)\), so a cavity cannot reach
its pole stop while the full prefix stays below \(3a/8\). The calculation
above improves the full cap to \(a/4\). Joining segments used in the
augmented Taylor graph remain inside the derivative strip, because their
coordinate increments tend to zero from a reference at most \(7a/16\).
The response, carrier, and budget stops can keep their doubled values.

The proof only needs fixed separated pole caps; their ratio is not a
mathematical assumption of the insertion graph. This explicit choice
justifies the enlarged margin without claiming that the old smaller
rectangle contains the new one and without using the sharper derivative
constants outside their certified strip. Short complex propagators and
Gaussian corrections still multiply vanishing widths.

## 6. Joint label condition and source/storage arithmetic

The minimum
\[
c_L=\min(c_{\rm src},c_{\rm rt},C_1^{-1},C_2^{-1/2},
                            c_{\rm ang},c_{\rm time})
\]
implies \(C_1c_L+C_2^2c_L^4\le2\). The exact runtime coefficient
\[
O_0[1+\sqrt e(C_1+C_2c_L)
                 e^{C_1c_L+C_2^2c_L^4}]+8T_1
\]
therefore has the stated meaning, including the endpoint contribution.
The supplied \(n^{-1}\) to \(n^{-1/2}\) conversion uses this complete
formula and introduces no logarithmic error loss.

The old tanh values \(B=2,s=2,t=4,R_{\rm real}=9,
R_{\rm complex}=10\) dominate the new positive recurrences. Although
the outer strip is narrower here, it does not occur in the finite
source-label recurrence; its effect is retained explicitly in the new
radii and in local vanishing remainder constants. Thus the source
envelope gives \(c_{\rm src}\ge16^{-32L}\).
The old runtime bound gives \(c_{\rm rt}\ge16^{-60L}\),
\(C_1\le16^{57L}\), and \(C_2\le16^{55L}\).
Source-error separation can only decrease these old runtime expressions.

The old source estimates for \(K_{\rm src},T_J,b_*\) imply
\(c_{\rm ang}^{-1}\le16^{12L}\). Also
\(A_U+B_U\le2\,16^{30L}\sqrt5\), by comparison with the old
dimension-two source response. With \(a=1/2\), this gives
\(c_{\rm time}^{-1}\le16^{17L}\). Consequently
\[
c_L\ge16^{-60L}.
\]
The old \(16^{-62L}\) label condition does imply every new condition.
These envelope comparisons are analytic, not inferences from the table.

The spherical tail calculation keeps
\(\alpha=c_t\lambda/(128\ell_n^{3/2})\),
\(r_q=c_q/\sqrt{\ell_n}\), the full source magnitude, and all its
tail logarithms. Its actual inverse-radius product is
\[
c_t^{-1}c_q^{-(d-1)}
=G_d\left[(16G_db_*+32)/a\right]^{d-1}.
\]
Inserting this into the inherited \(4N\) count proves equation (20).
The explicit time-only count supplies \(d=1\).
Paired initial-image identities and initialization-only scalar
coefficient construction are retained.

For the convenient tanh envelope, use
\[
b_*=\frac{32}{5}(64/15)^{L-2},\quad G_d=4\sqrt{d+3},\quad a=1/2.
\]
Then
\[
\frac{16G_db_*+32}{a}
=\frac{4096}{5}\sqrt{d+3}(64/15)^{L-2}+64
\le\sqrt{d+3}\left[\frac{4096}{5}(64/15)^{L-2}+32\right].
\]
This gives equation (22), including its factor \(4096\,9^d/d!\).
Squaring the source rank and using
\((a+b)^2\le2a^2+2b^2\) gives the exact inventory with
\(2040(L+1)\), the separate initialized-vector term, and \(10m(d+1)\).
The depth factor in the leading coefficient grows as
\((64/15)^{2(L-2)(d-1)}\), with the displayed numerical factors and
the remaining factor \(L+1\). The dimension ratio
\((d+3)^d/(d!)^2\le25/4\) is valid but does not erase the other
exponential dimension factors.

## 7. Deterministic evaluation check

I inspected the complete retained evaluator against equations (1)--(17),
then ran it in memory with exactly the listed depths and dimension pairs.
It reproduced every displayed rounded entry in both tables. No extra
parameter fit, stochastic simulation, or training run was used. The
candidate correctly describes these numbers as rounded diagnostics,
not rigorous floating-point upper bounds.

An independent depth-two arithmetic reduction provides a check on the
runtime normalization. At \(L=2\),
\[
\beta=15,\quad U=\sqrt{241},\quad F=34,\quad D_\delta=48,
\quad K_{\rm src}=65536/225,
\]
\[
P_h=17,\quad P_\delta=281,\quad
A_0=11034,\quad C_f=375190,\quad H_0=72036889,
\]
\[
Z_0=43455600,\quad
J_0=216\sqrt2,\quad J_1=2266026990\sqrt2,\quad
D_{\rm gram}=71115,\quad O_0=312159852.
\]
These are obtained directly from the displayed formulas, and give
\(c_L=4.75594265\cdot10^{-16}\) and
\(C_{\rm err}=1.64383715\cdot10^{24}\) to the shown precision.
The full evaluation reproduced:

| \(L\) | \(c_{\rm src}\) | \(c_L\) | \(C_{\rm err}(c_L)\) |
| ---: | ---: | ---: | ---: |
| 2 | \(2.85768090\cdot10^{-7}\) | \(4.75594265\cdot10^{-16}\) | \(1.64383715\cdot10^{24}\) |
| 3 | \(1.13804648\cdot10^{-9}\) | \(1.03068728\cdot10^{-19}\) | \(4.18143471\cdot10^{29}\) |
| 5 | \(3.56741149\cdot10^{-14}\) | \(6.00367353\cdot10^{-27}\) | \(2.26380626\cdot10^{40}\) |
| 10 | \(2.81034041\cdot10^{-25}\) | \(8.69878282\cdot10^{-45}\) | \(8.79800295\cdot10^{66}\) |
| 20 | \(2.09120141\cdot10^{-47}\) | \(3.72087988\cdot10^{-80}\) | \(6.52262196\cdot10^{119}\) |

The five old/new leading storage logarithm pairs also reproduce exactly
to the stated three decimal places:
\((395.747,21.481)\), \((1972.777,80.725)\),
\((19632.911,664.714)\), \((4934.912,114.885)\), and
\((98623.182,1662.680)\), in the candidate's table order.

## 8. Source boundary and remaining limitations

Complete scientific inputs used:

| Input | SHA-256 |
| --- | --- |
| INPUT_DIMENSION_REFINEMENT.md | c869a1af90beefe4fa5739be3d8a2abcec051703a7e2a13d909349aaff3cd2c4 |
| ARCHITECTURE_CONSTANT_REFINEMENT.md | b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7 |
| LABEL_DEPTH_RESCALING_ROUTE.md | d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1 |
| DEPTH_CONSTANT_SEPARATION.md | 6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f |
| EXPLICIT_SOURCE_CONSTANTS_ROUTE.md | d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a |
| EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md | 775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd |
| SPHERICAL_SOURCE_DIMENSION_ROUTE.md | bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8 |
| EXPLICIT_LABEL_CONSTANTS_ROUTE.md | 0fa619fde5966b55287eaaef6d3c59cc11e3d858964d989741556e173aadcb94 |
| DATASET_LABEL_DEPENDENCE.md | bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52 |
| DEPTH_INDEPENDENT_EXPONENT.md | 73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda |
| DEEP_ACTIVATION_EXTENSION.md | b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141 |
| DEEP_COMPLEX_SOURCE.md | 7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2 |
| WHOLE_QUERY_RESPONSE_SOURCE.md | 9222c93f0bb9d0c6943f86192cc4a8ad1bbb6b3f6199dd2b056b15fc3adec0d4 |
| STORAGE_QUADRATIC_IMPROVEMENT.md | ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2 |

Previously completed readings in the immediately preceding assigned check
were reused; no sibling findings were inputs. Links to other studies and
prior review reports were not followed. The local insertion event and
source-selection theorem remain inherited premises. The new numerical
estimates do not prove them afresh.

The result does not bound practical precision or preprocessing cost, make
the width threshold uniform in depth or dimension, remove inverse-gap
dependence, or prove a complexity lower bound. The source cap alone is
not the joint useful label cap for the moderated error coefficient.
Within those stated limits, the frozen tanh refinement passes without a
changed formula.

## 9. Check-only correction to the manual depth-two reduction

The manual calculation in Section 7 used \(F=34\), which is an arithmetic
error: the candidate's exact recurrence gives
\[
F=2[2+(15/4)2]=19.
\]
Its dependent constants must read
\[
C_f=209665,\qquad H_0=40256089,\qquad
Z_0=49668075/2,\qquad
J_1=1267414665\sqrt2,\qquad O_0=174443052.
\]
The other manually displayed values, including \(A_0=11034\),
\(D_{\rm gram}=71115\), \(U=\sqrt{241}\), and \(K_{\rm src}=65536/225\),
are unchanged. Direct rational arithmetic verifies these replacements.
The candidate's retained evaluator already used the correct \(F=19\);
therefore every reproduced table entry and the quoted values of
\(c_L\) and \(C_{\rm err}\) remain correct. This corrects the review
paragraph, not the frozen candidate or its theorem.
