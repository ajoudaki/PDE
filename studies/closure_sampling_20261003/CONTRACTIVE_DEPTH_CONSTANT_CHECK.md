# Independent internal reconstruction of the contractive-depth candidate

**Corrected verdict, 2026-10-04: PASS after the explicit external-trace
coefficient replacement in Section 9.** The original unchanged-candidate
PASS below is superseded. All final displayed numerical bounds survive;
the frozen candidate's definition of \(E\) does require a local repair.
Sections 1--8 are preserved to document the initial audit, and Section 9
supplies the corrected complete implication.

2026-10-04. **PASS, conditional on the stated inherited local insertion,
source-selection, and autonomous-runtime interfaces.** No correction to the
candidate's displayed sufficient label, error, radius, or storage constants
is required. This is an internal reconstruction, not a promotion review or
an independent reconstruction of the earlier cavity theorem.

The checked candidate is `CONTRACTIVE_DEPTH_CONSTANT_ROUTE.md`, SHA-256
`88f9a621c918bf8b9dbf210bd79085b8650a3533ad08655638afdd03a92787ac`.
The complete seven assigned scientific inputs and the necessary same-study
dependencies listed at the end were read. No sibling findings, other studies,
manuscript, experiments, or Git operations were used. The canonical-notation
skill and neural reference, rigorous-proof skill, and research-contract and
adversarial-audit instructions were applied. Only this report was written.

The result removes the additional exponential depth factors for the stated
small-gain nonlinear subclass. It does not give polynomial total storage in
depth for that subclass at its actual Gram gap: the gap itself is necessarily
at most exponentially small. The candidate states this distinction correctly.

## 1. Scope of the implication checked

The dense reference has unit inputs \(v=x/\sqrt d\), width \(n\), hidden
depth \(L\ge2\), forward equations

\[
z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad f_n=w^\top h^{(L)}/n,
\]

canonical independent Gaussian initialization, and zero initial readout.
It follows the candidate's physical-time gradient equations with mobilities
\((n,1,\ldots,1,n)\). Let \(Y=\|y\|_2/\sqrt m\) be label RMS,

\[
Q^{(0)}_{ab}=v_a^\top v_b,\quad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}),
\]

and \(\gamma=\lambda_{\min}(Q^{(L)})>0\),
\(\lambda=\min(1,\gamma/m)\), \(\ell_n=\log(en)\).
The explicit subclass is \(\phi_\ell(z)=c\tanh z\) at every layer,
with \(0<c\le1/40\). The candidate asserts, for

\[
0< u:=Y/\lambda\le 2^{-90}/L,
\]

same-initialization, same-physical-time, whole-sphere error at most
\(2^{150}LY\lambda^{-3/2}n^{-1/2}\), including the fitted endpoint.
The retained representation is the existing selected-neuron system with
fixed metrics, moving hidden weights, its own evolving residual, and an
algebraically corrected readout. It is not ordinary gradient flow of a
smaller iid network. This unchanged representation contract matters to
the implication.

All probability conclusions are for fixed architecture, data, positive
labels RMS, and confidence, followed by sufficiently large width. The
source width threshold remains unquantified. Zero labels give the exact
stationary predictor separately.

## 2. Small gains and the local insertion interface

The complex identity

\[
|\tanh(x+iy)|^2=
\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}
\]

gives \( |\tanh z|<2\) for \( |\Im z|<1\), and
\(|\tanh z|\le1\) for \( |\Im z|\le1/2\). Moreover
\(|\operatorname{sech}^2z|\le\sec^2(1/2)<2\) on the latter strip.
Thus value bound \(B=1\), first-derivative bound \(s=2c\le1/20\), and
second-derivative bound \(t=4c\le1/10\) are valid. On the real axis,
the bounds are \(c\) and \(2c\). Higher derivatives needed by the local
insertion graph are bounded by Cauchy's formula on a smaller fixed strip.

The original label/source notes choose first- and second-derivative
envelopes at least one. Their displayed exact recurrences do not require
this lower bound. Direct differentiation gives

\[
P_1=2,\qquad P_\ell=2+10sP_{\ell-1},\qquad
K_\ell=2(10s)^{L-\ell}.
\]

The direct matrix derivative is bounded by the feature bound \(B=1\);
the additional one allows a single external preactivation direction.
Propagation of a feature derivative costs \(s\), while the matrix
operator costs ten. Backward propagation has the same product \(10s\)
and starts from the deterministic readout bound. Hence, with
\(q_{\rm src}=10s\le1/2\),

\[
P_\ell\le4,\qquad K_\ell\le2,\qquad
\sum_{\ell=1}^L K_\ell\le4.
\]

The mixed Hessian and mixed endpoint identities in
`EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` and
`DEPTH_INDEPENDENT_EXPONENT.md` use multiplication by the actual
derivative bounds; they contain no division by \(s\), no comparison
of a preactivation derivative with a smaller feature derivative, and no
geometric-sum estimate requiring \(10s\ge1\).

The same-study local interface was also inspected directly.
`DEEP_ACTIVATION_EXTENSION.md`, Sections 2--6, expresses its graph in
terms of bounded gates and derivatives, coordinate products, normalized
pairings, and matrix actions. It explicitly does not divide by an
activation derivative. Its coarse constants can remain enlarged above
one for local Gaussian nets and nonlinear remainders. These constants
multiply polylogarithms and strict negative powers of width. The only
logarithmic-in-width variational coefficient that persists in the label
restriction is controlled below. No new lower slope bound, bounded
carrier hypothesis outside the stopped budgets, or unspecified additional
small-label condition is needed for this substitution.

This verifies a change in the quantitative estimates of the stated local
interface. It does not remove that interface from the premises or replace
its earlier Gaussian insertion proof by the present check.

## 3. Persistent source smallness is explicit

Use \(S=16u\), horizon \(T=32\lambda^{-1}\ell_n\), and the candidate's
definitions \(A_H,D_H,H_2\) of the Hessian coefficients. The readout,
mixed-weight, and full curvature contributions are bounded respectively by

\[
2sP_L\le0.4,\qquad
2s^2\sum_{\ell\ge2}K_\ell P_{\ell-1}\le0.08,\qquad
t\sum_\ell P_\ell^2K_\ell\le6.4.
\]

The top curvature contribution alone is at most \(3.2\). Therefore
\(A_H\le4\), \(H_2\le7\), and \(D_H\le2L\), as claimed. The
unweighted curvature coefficient \(D_H\) is not uniformly bounded in
depth by this argument.

For the remaining label-route constants, the candidate's recurrences give

\[
E\le0.4,\quad
D_0\le98+64(e^2-1)+0.4+0.01<512,
\quad D_1\le576e^3(2L)^3<10^5L^3.
\]

The activity coefficient satisfies \(V_\ell\le0.1+V_{\ell-1}/2\),
so \(V_\ell\le0.2\). The terminal Gaussian modulus coefficient is
at most \(0.09\); every other forcing is at most
\(0.0005+0.28+0.05=0.3305\), with propagation at most one half.
Consequently the defined envelope \(G=\max(1,G_1,\ldots,G_L)\) is one.

Take \(\eta=1/512\), \(\mathcal B=64e^2L<512L\), and
\(\Lambda=\log(e+\mathcal B)+\log512\le14L\). At
\(S\le1/(4096L)\), the five persistent quantities are bounded by

\[
\begin{array}{c|c}
SA_H &4/(4096L)\\
D_HS^2/\eta &1024/(4096^2L)\\
16eS^2(D_H/\eta)\sqrt{2\mathcal B}
 &1572864/(4096^2\sqrt L)\\
S^2\Lambda/\eta &7168/(4096^2L)\\
D_1\mathcal BS^4/\eta^2
 &10^5\,512^3/4096^4=10^5/2^{21}<1/20.
\end{array}
\]

They meet, respectively, the required bounds \(1/4,1/4000,1,1,1\).
Also \(2sK_1S^2\le1\). For real fitting, the recurrence in the
label route has forcing at most \(s^2\), multiplier at most \(9/20\),
and initial value at most \(s^2\). Its stated \(C_*\) is therefore
one. The real fitting condition \(u\le1/8\), the first-weight margin,
and the mixer margins are satisfied.

The singleton shift, including its dependence on the budget exponent,
is exactly bounded by

\[
S\left[D_0+\frac{D_1\mathcal BS^4}{\eta^3}\right]+o(1).
\]

Multiplying by \(\eta/S\) gives exponential cost at most two, since
\(\eta D_0\le1\). The Gaussian reference moment uses
\(\eta G\le1/128\); combining its real part with the vanishing
complex correction gives first moment less than four eventually.
Thus the layer-summed budget ratio is at most

\[
\frac{(L-1)4e^2}{64e^2L}<\frac1{16}.
\]

At each fixed empirical degree \(p\), the limiting hit probability is
at most \(m16^{-p}\). Width tends to infinity before taking the
infimum over fixed \(p\). This neither assumes a growing-deletion
estimate nor conditions Gaussian roots on full-model survival.
The resulting sufficient source restriction is indeed
\(u\le2^{-16}/L\). In particular the nonvanishing coefficient of
\(\log n\) in the variational estimate has been bounded explicitly;
it has not been moved into the width threshold.

## 4. Radius, source count, and retained coordinates

With the endpoint coefficients defined in the candidate, the previous
bounds give \(f_\ell\le0.2\), \(t_\ell\le0.1\), \(g\le0.2\),
\(r_\ell\le0.8\), \(q_\ell\le0.04\), and \(b_\ell\le1\).
The mixed forward endpoint forcing is at most

\[
0.1(0.8)(4)+0.05(0.04+0.1\cdot0.2)=0.323.
\]

Its propagation factor is at most one half and its first value is
at most \(0.08\), so \(e_\ell\le0.646<0.65\). The query mixed
endpoint forcing is at most \(8+0.05=8.05\), its first value is at
most \(4.1\), and therefore \(a_\ell\le16.1<17\). It follows that

\[
E_Q\le0.2\cdot7+0.65<3,\quad E_J\le17,
\quad T_Q\le4.8<5,\quad T_J\le27.2<28.
\]

The asymmetric trace conditions are exactly the persistent conditions
already checked in Section 3. The source carrier coefficient is
\(K_{\rm src}=32\max(1,\max K_\ell,\max sK_\ell)=64\).

Put \(D=d+3\) only for the next arithmetic. With the spherical Gaussian
multiplier \(16\sqrt D\), the row-insertion formulas yield

\[
U_*\le\max\{12.8,40.912+1.28\sqrt D\}\le22\sqrt D,
\]
\[
V_*^{\rm qry}\le
\max\{64\sqrt D+14.8,32\sqrt D+187.6\}
\le126\sqrt D,
\]

using \(\sqrt D\ge2\). The added one in each defining source
recurrence is included. Hence

\[
c_t^{-1}\le11264\sqrt{d+3},\qquad
c_q^{-1}\le16128\sqrt{d+3},
\]

and both are below \(2^{14}\sqrt{d+3}\). The spherical pole estimate
is \(8c_tYSU_*+c_qV_*\le3/128\), with strip width one and
\(Y,S\le1\). Its query net, mixed endpoint, and simultaneous
stop-transfer arguments use the same bounded geodesic derivatives as
the supplied spherical source proof. No sum over \(d-1\) independent
imaginary query segments is reintroduced.

All four source families \(h,W_0h,\delta,W_0^\top\delta\) have
coordinate magnitude at most \(8\sqrt n\): value bound one controls
the features, initialized mixer norm eight controls their images, and
the backward RMS bound controls both reverse families. This polynomial
magnitude is used only for approximation, not for runtime carrier control.

The spherical weighted-degree count therefore gives

\[
4N\le1024\,9^d\frac{c_t^{-1}c_q^{-(d-1)}}{d!}
\lambda^{-1}\ell_n^{3d/2+1}
\le2^{28d}\frac{(d+3)^{d/2}}{d!}
\lambda^{-1}\ell_n^{3d/2+1}.
\]

Here \(1024(9\,2^{14})^d\le2^{28d}\) for \(d\ge1\). The
separate two-query count for \(d=1\) also fits: its coefficient is
at most \(8\cdot514\cdot2^{14}\cdot2<2^{29}\), which is the
coefficient of the proposed dimension-one bound. Adding \(2m+d+1\)
exact initialized vectors proves the candidate's source-rank estimate.

The scalar initial-jet, quadrature, and coefficient operations commute
with each initialized matrix action. Using identical operations for both
members of each pair preserves both forward and reverse pairings, while
each member has its own coordinate approximation guarantee. The source
construction therefore supplies the actual runtime interface at accuracy
\(\epsilon=n^{-1}\), without a trained trajectory table.

The supplied inventory is \(1020(L+1)R^2+10m(d+1)\). Squaring the
rank bound with \((a+b)^2\le2a^2+2b^2\) gives exactly the candidate's
two terms with coefficient \(2040(L+1)\). The spherical factor
\((d+3)^d/(d!)^2\le25/4\) is valid. The explicit factor \(2^{56d}\)
still remains; the claim is removal of the joint exponential \(C^{Ld}\),
not polynomial dependence on input dimension.

## 5. Runtime replacement for gains below one

For the fixed neuron metric, \(D/4\preceq H\preceq D\) and
\(\mathbf1^\top D\mathbf1\le4\). Thus \(h=2\) bounds feature norms,
\(g=2c\le1/20\) bounds diagonal gate operators, and
\(\kappa=4c\le1/10\) bounds changed gates times a coordinate-bounded
reference carrier. The last assertion follows directly from

\[
\|[\phi'(z_C)-\phi'(z_R)]\odot k_R\|_H
\le 2c\|k_R\|_\infty\|z_C-z_R\|_D
\le4cM\|z_C-z_R\|_H.
\]

The initialized compressed mixer has operator norm at most eight by the
source isometry, so the real tube is \(R=9\). It is not \(K+1\).
The actual source normalization addendum requires the direct bound

\[
K=8+4K_{\rm src}=264,\qquad
M\le1+4Ku\sqrt{\ell_n}.
\]

Indeed \(K_{\rm src}S=16K_{\rm src}u\le4Ku\). No reverse
inequality comparing the activity allowance with actual activity is
used. This also bounds the coordinate approximation multiplier and the
initialized norm as required by the runtime proof.

With \(q=9g\le9/20\), the backward coefficients are
\(b_\ell=gq^{L-\ell}\), and

\[
U^2=b_1^2+h^2\sum_{\ell=2}^Lb_\ell^2
\le4g^2\sum_{j\ge0}q^{2j}<1.
\]

For a unit hidden parameter direction, preactivation derivatives satisfy
\(Z_1\le1\), \(Z_\ell\le h+qZ_{\ell-1}\). Their bound is at
most \(h/(1-q)<4\), and feature derivatives cost another factor \(g\).
Thus \(F=4\) is a valid common envelope above one. This supplies the
preactivation bound that the old proof obtained using \(g\ge1\).

For hidden tuple error \(a\), forward subtraction has direct terms
\(ha+A_0\epsilon\) and propagation \(q\). Therefore

\[
\|\Delta z_\ell\|,\ \|\Delta h_\ell\|
\le C_f(a+\epsilon),\qquad C_f=4(1+A_0),
\]

because \((h+A_0)/(1-q)\le4(1+A_0)\). In backward subtraction the
three nonterminal forcing terms are

\[
gD_\delta\alpha a,\qquad gA_0\epsilon,qquad
\kappa MC_f(a+\epsilon),\quad \alpha=Y/\sqrt\lambda\le1.
\]

They arise respectively from the changed mixer acting on the selected
reference response, the reverse source defect, and the changed gate
acting on the actual selected reference carrier. The terminal readout
error has coefficient \(g\). Summing each forcing once over its
geometric propagation gives

\[
\|\Delta\delta^{(\ell)}\|
\le b_\ell\|\widehat w_C-w_R\|+Z_0M(a+\epsilon),\qquad
Z_0=\frac{\kappa C_f+gD_\delta+gA_0}{1-q}.
\]

This is the required replacement for the old \(L(gR)^L\) envelope;
simply substituting a subunit \(gR\) there would not be valid.

The remaining exact projection identities, raw energy identity,
source pairing errors, lifted residual damping, and readout cancellation
use \(F,C_f,Z_0\) only as upper bounds in these positions. Inspecting
the complete explicit runtime proof reveals no further use of
\(g\ge1\). Its conditions \(224FUu^2\le1\), \(6J_0u\le1\),
and \(u\le1\) retain their previous meanings. They hold at the
candidate's \(u_*=2^{-90}/L\).

## 6. Numerical runtime certificate and strict root-width rate

All candidate runtime table entries are valid. In particular

\[
D_\delta\le792.15<800,\quad W=8480<2^{14},\quad
J_0\le1584.7\sqrt L<2^{11}\sqrt L,
\]

and \(P_h=768240<2^{20}\),
\(P_\delta\le766893.6<2^{20}\). Inserting these values gives
\(A_0<2^{33}\), \(C_f<2^{36}\), \(H_0<2^{52}\), and
\(Z_0\le2(C_f+D_\delta+A_0)<2^{38}\).
The tuple and Gram sums give
\(J_1<2^{55}\sqrt L\) and \(D_0^{\rm rt}<2^{23}L\).
Successive substitution then yields

\[
F_0<2^{72}L,\quad G<2^{75}L,\quad
C_1<2^{89}L,\quad C_2<2^{88}L,\quad O_0<2^{55},
\]
\[
W_1<2^{25}L,\qquad T_1<2^{27}L.
\]

Only the stated tuple factors \(\sqrt L\) and layer sum \(L\)
survive. No layer product is put inside these constants.
At \(u_*=2^{-90}/L\),

\[
C_1u_*\le1/2,\qquad C_2u_*\le1/4,\qquad
C_2^2u_*^4\le2^{-184}/L^2.
\]

The exponent in the runtime coefficient is consequently below two.
The actual formula therefore gives

\[
\begin{split}
C_{\rm err}
&=O_0\left[1+\sqrt e(C_1+C_2u_*)
                e^{C_1u_*+C_2^2u_*^4}\right]+8T_1\\
&<2^{55}[1+16(2^{89}L+1)]+2^{30}L<2^{150}L.
\end{split}
\]

The source tolerance remains \(n^{-1}\). For
\(q_n=\sqrt{\ell_n}\), the raw exponent is
\(C_1u+C_2u^2q_n\). The inequality
\(C_2u_*^2q_n\le q_n^2/4+C_2^2u_*^4\), combined with
\(\sup_{q\ge0}qe^{-q^2/4}<1\), is exactly the supplied conversion
to a strict \(n^{-1/2}\) error with no logarithmic loss. The two model
tails are each bounded by
\(4T_1Y\lambda^{-3/2}e^{-\lambda t/4}\). The chosen horizon
\(32\lambda^{-1}\ell_n\) is more than sufficient to include every
later physical time and the fitted endpoint.

## 7. What survives the subclass restriction

The subclass is nonempty with positive gap. For example, for orthogonal
unit training inputs with \(m\le d\), oddness gives zero off-diagonal
covariances, while each scalar variance satisfies

\[
q_0=1,\qquad q_\ell=c^2\mathbb E[\tanh^2(\sqrt{q_{\ell-1}}G)]>0,
\quad G\sim N(0,1).
\]

Thus \(\gamma=q_L>0\) at every fixed finite depth. The model keeps
nonlinear activation maps and all hidden updates. This does not assert
a uniform lower bound on nonlinear influence or on hidden motion.
Arbitrary label signs are allowed once their RMS meets the cap.

For every allowed dataset, \( |c\tanh x|\le c|x|\) gives

\[
Q^{(\ell)}_{aa}\le c^{2\ell},\qquad
0<\gamma\le\operatorname{tr}(Q^{(L)})/m\le c^{2L}.
\]

Consequently \(\lambda=\gamma/m\le c^{2L}/m\). The displayed
inverse-gap storage coefficient obeys
\(\lambda^{-2}\ge m^2c^{-4L}\), and the allowed absolute label
RMS satisfies
\(Y\le2^{-90}c^{2L}/(mL)\). These are unavoidable implications
of this certificate's actual gap. They are not lower bounds on the
optimal compressor size or on its realized prediction error.

The old cap \(u\le\beta^{-62L}\), with \(\beta\ge10\), implies
the new cap because \(62L\log_2(10)>90+\log_2L\) for \(L\ge2\).
This comparison and the removal of additional depth multipliers are
valid. Holding an explicit symbolic \(\gamma\) fixed while comparing
formulas is not a construction of an arbitrarily deep fixed-\(c\)
family with a uniform positive gap.

There is therefore no unresolved new assumption in the checked
subclass implication. The surviving limitations are the inherited local
insertion and selection premises, fixed-architecture probability
quantifiers, unquantified width threshold, exact-real preprocessing and
precision contract, and the actual gap collapse. None is silently
replaced by a favorable numerical constant in the candidate.

## 8. Complete scientific inputs and freeze

| Input | SHA-256 |
| --- | --- |
| `INPUT_DIMENSION_REFINEMENT.md` | `c869a1af90beefe4fa5739be3d8a2abcec051703a7e2a13d909349aaff3cd2c4` |
| `LABEL_DEPTH_RESCALING_ROUTE.md` | `d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1` |
| `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` | `d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a` |
| `DEPTH_CONSTANT_SEPARATION.md` | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md` | `775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd` |
| `SPHERICAL_SOURCE_DIMENSION_ROUTE.md` | `bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8` |
| `DEPTH_INDEPENDENT_EXPONENT.md` | `73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda` |
| `DEEP_ACTIVATION_EXTENSION.md` | `b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141` |
| `DEEP_COMPLEX_SOURCE.md` | `7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2` |
| `WHOLE_QUERY_RESPONSE_SOURCE.md` | `9222c93f0bb9d0c6943f86192cc4a8ad1bbb6b3f6199dd2b056b15fc3adec0d4` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |

References to other studies and previous check reports in these inputs
were not followed. The preceding PASS concerns the complete displayed
quantitative implication at the frozen candidate hash, within its
explicit inherited-interface boundary.

## 9. Correction: a later external injection cannot be shifted to layer one

While subsequently reconstructing the independently assigned tanh-constant
route, I read the complete necessary same-study dependency
EXPLICIT_LABEL_CONSTANTS_ROUTE.md. Its Section 3 explains the ancestor
of the candidate's external-trace coefficient: an injection at layer
\(p\) propagates to layer \(\ell\ge p\) with norm at most
\((Rs)^{\ell-p}\), and its proof replaces \(p\) by one. That last
domination uses \(Rs\ge1\). It reverses for the present
\(q_{\rm src}=10s\le1/2\). This dependency invalidates the initial audit's
claim that the definition of \(E\) could be retained without correction.

For a unit external preactivation direction inserted at layer \(p\),
differentiate the forward equations while holding the weights fixed.
The derivative is the identity at that layer, zero below it, and has
operator norm at most \(q_{\rm src}^{\ell-p}\) above it. The external
Hessian of \(F_a=nf_n(v_a)\) is the sum of the curvature contractions

\[
\sum_{\ell=p}^L
(D_ez_a^{(\ell)})^\top
\operatorname{diag}(\phi_\ell''(z_a^{(\ell)})k_a^{(\ell)})
D_ez_a^{(\ell)}.
\]

Carrier RMS and the normalized trace inequality therefore give the bound
\(S t\sum_{\ell=p}^L q_{\rm src}^{2(\ell-p)}K_\ell\).
Replace the \(E\) in candidate equation (13) by

\[
\widetilde E
:=\max_{1\le p\le L}
t\sum_{\ell=p}^Lq_{\rm src}^{2(\ell-p)}K_\ell.
\tag{C1}
\]

It is also safe, and simpler, to use \(t\sum_{\ell=1}^LK_\ell\)
in place of \(\widetilde E\). Since every propagation factor in (C1)
is at most one,

\[
\widetilde E\le t\sum_{\ell=1}^LK_\ell\le0.4.
\tag{C2}
\]

The old expression is just the \(p=1\) term and cannot serve as the
uniform argument: for example at \(q_{\rm src}=1/2,L=3\), its value
is \(0.875t\), whereas the bound at \(p=L\) is \(2t\).
These are bounds used in the proof; no counterexample to the final
compression theorem is asserted.

Define the corrected singleton coefficient by

\[
\widetilde D_0
=\max\{1,2H_2^2+4A_H^2(e^2-1)+\widetilde E
                          +s^2K_{\max}^2\}.
\tag{C3}
\]

The valid shift is
\(S[\widetilde D_0+D_1\mathcal BS^4/\eta^3]+o(1)\).
By (C2), precisely the same arithmetic gives
\(\widetilde D_0<512\). Thus the candidate's fixed
\(\eta=1/512\), \(\mathcal B=64e^2L\), all five persistent smallness
conditions, and its source cap \(Y/\lambda\le2^{-16}/L\) are unchanged.
The subsequent radius, source dimension, runtime, final label cap
\(2^{-90}/L\), and final error coefficient \(2^{150}L\) do not use
the former definition of \(E\) elsewhere. They follow with (C1)--(C3).

I also checked the other possible uses of an earliest-layer maximum:

1. **Augmented preactivation derivatives.** For training inputs of norm
   one, let \(D_{(\Theta,e)}z^{(\ell)}\) include an external vector
   at an arbitrary fixed layer \(p\). Its first-layer norm is at most
   \(1+\mathbf1_{\{p=1\}}\le2\). At later layers, direct parameter
   variation costs \(B=1\), the external direction costs at most
   \(\mathbf1_{\{\ell=p\}}\le1\), and propagation costs
   \(q_{\rm src}\). Therefore the recurrence
   \(P_\ell=2+q_{\rm src}P_{\ell-1}\) bounds every insertion location
   without moving it to the first layer. It remains valid for the
   augmented Hessian and its response endpoint blocks.
2. **Query derivatives.** The coefficient
   \(j_\ell=20q_{\rm src}^{\ell-1}\) bounds the actual intrinsic query
   derivative beginning at \(Aq'(z)\). Its source is genuinely at
   layer one. It is not used to bound a later external injection.
   Its mixed parameter endpoint contains the curvature product
   \(tj_\ell P_\ell\), the direct matrix term \(sb_{\ell-1}\), and
   the propagated previous endpoint. Thus equation (19) remains valid.
   Lower incoming-row forward probes in the local insertion graph are
   maps \(D_\Theta z\,C_a^\top y\) and \(D_\Theta h\,C_a^\top y\);
   their forward factors use \(P_\ell,sP_\ell\), not \(j_\ell\).
   Their finite local constants are not claimed to decay with the
   earliest-layer query coefficient.
3. **Real fitting.** The ancestor proof uses \(b_\ell\le b_1\),
   which also reverses for \(9s<1\). Here every
   \(b_\ell=s(9s)^{L-\ell}\le s\le1/20\), and the forward feature
   coefficient is below one. The candidate's \(C_*=1\) therefore
   dominates \(B^2\max_\ell b_\ell\), not just \(B^2b_1\).
   Using that direct maximum in the existing energy proof gives the
   same normalized Gram and mixer margins. No numerical restriction
   or new assumption is required.
4. **Remaining source constants.** The backward \(K_\ell\) start at the
   top and use their actual layer indices. The mixed Hessian sums,
   \(D_H\), \(H_2\), activity recurrences, and the learned-column term
   use explicit sums or \(K_{\max}\), rather than a presumed largest
   first-layer value. The former reconciliation's lower bound
   \(H_2\ge2s+4K_1\) is not needed: the candidate explicitly imposes
   \(2sK_1S^2\le1\) for its first-weight tube. No additional reversed
   geometric domination is used in the final implication.

The current internal verdict is therefore **PASS for the candidate with
(C1)--(C3), retaining every final displayed bound**. The frozen candidate
itself has a local proof-coefficient defect and should be cited together
with this correction. The gap-collapse limitation in Section 7 remains.
This correction neither upgrades the inherited local interfaces nor
constitutes promotion.
