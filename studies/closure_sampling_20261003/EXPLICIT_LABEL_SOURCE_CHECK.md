# Independent check of explicit label and source constants

2026-10-04. Scoped independent reconstruction. This is an internal mathematical
check of the new explicit constants, not a promotion review or a replacement
for the inherited Gaussian insertion theorem. No experiment, Git operation,
maintained-book edit, or read of another study was made.

The complete inputs read were `EXPLICIT_LABEL_CONSTANTS_ROUTE.md` (frozen
SHA-256 `0fa619fde5966b55287eaaef6d3c59cc11e3d858964d989741556e173aadcb94`),
`EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` (original frozen version, to be supplemented
by its announced normalization repair), `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md`,
and the specifically named current-study prerequisites
`DEPTH_INDEPENDENT_EXPONENT.md` and `LABEL_SEPARATE_BUDGETS.md`.
The canonical-notation skill, its neural-network reference, and the rigorous
mathematics skill were read. The reports' inherited local insertion,
common-cavity transfer and vanishing-remainder interfaces are explicit proof
inputs here; this scoped check does not independently reprove them.

## 1. Quantified conclusion of the label reconstruction

Assume hidden depth L>=2. Let each activation be real on the real axis and
holomorphic and bounded by B_phi on |Im z|<a. Define

\[
 B=\max(1,B_\phi),\quad s=\max(1,4B/a),\quad
 t=\max(1,32B/a^2),\quad
 \beta=\max(10,B,s,t,16/a).
\]

This beta depends only on the common activation bounds, not on the number
of layers. Let gamma be the least eigenvalue of the initialized limiting
feature covariance, lambda=min(1,gamma/m)>0, and Y=||y||_2/sqrt(m).
For every fixed dataset and depth, the sufficient condition

\[
       0<Y/\lambda\le\exp[-\beta^{40L}]
\tag{C1}
\]

implies every nonvanishing smallness condition in the checked explicit
label route. It also implies the explicit asymmetric source-trace
conditions once the source route uses the label Hessian coefficients.
No input-dimension factor is required in (C1).

The proof below gives the stronger elementary bound
c_(L,phi)>=exp[-beta^(32L)] for the explicit minimum in that route.
The exponent 40 in (C1) leaves an additional margin; neither exponent is
claimed sharp.

## 2. Reconstruction of the surviving estimates

The Gaussian operator event with cap 8 is valid. A pair of 1/4-nets has
at most 9^(2n) pairs; fixed bilinear forms have variance 1/n, and the
net approximation bounds the operator norm by twice the net maximum.
Thus the displayed probability 2 exp[-n(8-2 log 9)] is correct.
The real cap 9 and complex cap 10 retain a strict increment margin.

For the mobility-normalized Hessian, the mixed readout terms factor
through one n-dimensional layer each. The two hidden-matrix terms at
layer ell are bounded by s^2 K_ell S P_(ell-1), and the curvature term
is bounded by t P_ell^2 times a carrier diagonal norm. At the top the
carrier is the deterministic readout; at all lower layers the stopped
exponential budget supplies

\[
 \|k\|_{p,n}\le Sp(2\mathcal B)^{1/p},\qquad
 \|k\|_\infty\le S\log(2n\mathcal B).
\]

This reconstructs all three displayed Hessian estimates with A_H,D_H,H2
in the author route, including the exclusion of the top deterministic
carrier from D_H. The operator propagator coefficient D_H S^2 multiplying
log n is a genuine smallness condition. The inequality
D_H S^2<=1/4000 leaves enough room for its inherited n^(1/1000) cap;
fixed exponential factors may enter the eventual width threshold.

For h>=1 residual-Hessian insertions, the endpoint estimate is

\[
 \frac{2S^h}{h!}
 [H\{1+S(h+2)(2\mathcal B)^{1/(h+2)}\}]^{h+2}.
\]

Splitting the power yields a first sum
4H^2[exp(2HS)-1]. The second is at most

\[
 8e^2 H^2\mathcal B S^2
 \sum_{h\ge1}(2eHS^2)^h(h+2)^2.
\]

For 0<=q<=1/2,

\[
 \sum_{h\ge1}q^h(h+2)^2
 =\frac{q(9-11q+4q^2)}{(1-q)^3}\le36q.
\]

Thus the second sum is at most 576 e^3 H^3 mathcal B S^4,
exactly the author's coefficient. The h=0 bound 2H2^2 must use the
two Hilbert--Schmidt endpoint bounds; it does not follow from two
operator norms. The direct external trace and learned-column terms
then have the stated bound D S(1+S^2 mathcal B)+o(1).

The carrier split at R_c=4 log(8 sqrt(2 mathcal B)/v) is also consistent.
Its high part times the gate bound 2s is at most s S v. Its low part
is controlled by S^2 R_c v<=14 sqrt(v) when
S^2 log(e+mathcal B)<=1. This proves the displayed G recursion for the
backward increment modulus without replacing a sample budget by a
maximum across samples.

For the conditional Gaussian process, the proposed dyadic increment
thresholds have summable failure probability less than exp(-z^2).
Their sum is at most 32G(1+z). Integrating this tail gives

\[
 \mathbb E e^{qZ}\le
 e^{32qG}[1+32qG\sqrt\pi\,e^{256q^2G^2}].
\]

The complex correction does not rely on convergence in probability alone.
The specifically checked prerequisite provides a Gaussian tail scale tending
to zero as well as a mean supremum tending to zero; this implies that its
fixed exponential moments tend to one. Consequently the numerical target
E exp(2 correction)<=2 for sufficiently large n is justified, and the
Cauchy--Schwarz value mathcal M_c=sqrt(2 mathcal M(2)) is valid.

Finally mathcal B=2L+8(L-1) mathcal M_c exp(D) and
exp(D S^2 mathcal B)<=2 imply that the per-sample moment ratio is at most
1/4. At every fixed integer moment degree p the limiting failure bound
is m 4^(-p). Taking the width limit first and then the infimum over p
makes it zero. No growing deletion count or independence across samples
was used.

## 3. An elementary activation-only envelope

All bounds in this table follow from the actual displayed recurrences;
the symbols on the left retain the definitions in the label route.

| Quantity | Explicit upper bound |
| --- | --- |
| C_* | beta^(5L) |
| K_ell, P_ell | beta^(2L) |
| D_H | beta^(5L) |
| H, H2 | beta^(8L) |
| T0 | beta^(17L) |
| T1 | beta^(27L) |
| E | beta^(7L) |
| D | beta^(28L) |
| V_ell | beta^(6L) |
| G | beta^(10L) |
| log mathcal M_c | beta^(22L) |
| log mathcal B | beta^(30L) |

Here are details sufficient to check the exponent bookkeeping. Use
10s<=beta^2 and L<=beta^(L-1). The closed expression for F_L yields
C_*<=beta^(5L). The recurrence P_ell=B+1+10s P_(ell-1) gives
P_ell<=3 beta^(2ell-2)<=beta^(2ell-1), and
K_ell<=beta^(2L). Inserting these in the finite sums for A_H,D_H,H2
gives H,H2<=beta^(8L) and D_H<=beta^(5L).
Since 2+4(e^2-1)<28<=beta^2 and 576e^3<beta^5,
T0<=beta^(16L+2)<=beta^(17L) and
T1<=beta^(24L+5)<=beta^(27L). The direct sum E is at most
beta^(7L). Hence

\[
 D\le4\beta^{27L+1}\le\beta^{28L}.
\]

The affine recurrence for V is bounded by the sum of at most L geometric
terms, giving V_ell<=beta^(6L). The descending G recurrence has a
forcing at most beta^(6L+4), its terminal value is at most
beta^(6L+3), and each backward step costs at most beta^2. Therefore
G<=beta^(10L).

For G>=1 the logarithm of mathcal M(2) is at most

\[
 64G+\log(1+64G\sqrt\pi\,e^{1024G^2})
 \le1100G^2\le\beta^{22L}.
\]

Taking sqrt(2 mathcal M(2)) preserves this upper bound. Also
mathcal B<=10L mathcal M_c e^D, so
log mathcal B<=log(10L)+log mathcal M_c+D<=beta^(30L).
Every inverse-polynomial term in S_* is at least exp[-beta^(31L)].
For its smallest potentially exponential term,

\[
 -\log\sqrt{\frac{\log2}{D\mathcal B}}
 =\tfrac12[\log D+\log\mathcal B-\log\log2]
 \le\beta^{31L}.
\]

The factor 16 in c_(L,phi) and the separate real fitting condition then
give

\[
 c_{L,\phi}
 =\min\{(8\sqrt{C_*})^{-1},S_*/16\}
 \ge\exp[-\beta^{32L}].
\]

This proves (C1). It explicitly displays the depth penalty instead of
hiding an uncomputed C_L inside a newly named constant.

## 4. Asymmetric source trace conditions require no additional restriction

Use h0=A_H, h1=D_H and h2=H2 in the source estimate. The augmented
forward bounds P_ell dominate the ordinary forward endpoints. The top
curvature term is already in A_H, so it must not also be estimated from
an exponential top-carrier budget with coefficient eta=1; no such budget
was imposed on the readout.

For h>=1, use Hilbert--Schmidt exponent 2 at the response endpoint,
operator exponent infinity at the forward endpoint, and exponent 2h at
each residual Hessian. The reciprocals sum to one. Thus there is no
ambient parameter-dimension loss. For h=0 use both endpoint
Hilbert--Schmidt bounds. The source's resulting sufficient conditions are

\[
 SA_H\le1/4,\qquad
 16eS^2D_H\sqrt{2\mathcal B}\le1.
\]

They are automatic under the label route's existing S<=mathcal B^(-1/2).
Indeed H>=max(A_H,D_H,1),
D>=4(e^2-1)H^2>=24H^2, and mathcal B>=8exp(D), so

\[
 SA_H\le H e^{-12H^2}/\sqrt8<1/4,
\]
\[
 16eS^2D_H\sqrt{2\mathcal B}
 \le8eH e^{-12H^2}<1.
\]

Both scalar functions decrease for H>=1, so their values at 1 prove
the strict numerical inequalities. The same explicit label coefficient
therefore closes the asymmetric trace series.

## 5. Status and limits

The new label constant and the asymmetric trace closure pass this scoped
independent reconstruction. The model, fixed-depth quantifiers, initialized
Gram assumption, and canonical Gaussian law are unchanged. The constants
left unspecified by the inherited local insertion interfaces multiply
strictly vanishing width errors and affect the sufficiently-large-width
threshold. They have not been used to absorb a nonvanishing coefficient
of log n, a moment base, a pole-margin coefficient, or the retained-state
prefactor.

The author's source cap normalization repair and the final joined theorem
remain to be checked separately before this report certifies their exact
formulas. This report does not make the width threshold uniform in depth,
dimension, labels, or confidence, and does not claim the conservative
exponential label coefficient is sharp.


## 6. Independent runtime and final-assembly reconstruction

After the independent label calculation was frozen at report SHA-256
`bde8a706b32fbf96811c8c4ef093292629b7d60197a41597f9ca9848b1554672`,
the coordinator requested a joined-theorem check. The complete
`EXPLICIT_ARCHITECTURE_CONSTANTS.md` at SHA-256
`19a307c4c8d9325605b0a88099dce8668baf1f61e3bf7088bc5ba36deee3c64d`
was read. The full runtime derivation was reread, and its precise
construction prerequisite `STORAGE_QUADRATIC_IMPROVEMENT.md` was read
completely. The independent source author's announced normalization
addendum was not yet on disk at this stage, so its final algebra is recorded
in the next section when available.

The runtime interface requires one correction, already explicit in the
assembly. A carrier upper bound based on the allowance 16Y/lambda does
not imply the stronger same coefficient times actual integral activity.
With K=8+4K_src, the direct input

\[
 M\le1+16K_{\rm src}(Y/\lambda)\sqrt{\log(en)}
   \le1+4K(Y/\lambda)\sqrt{\log(en)}
\]

is sufficient for every subsequent runtime inequality. No lower bound
on actual residual activity is needed. This is a correction of a literal
interface assertion, not an extra hypothesis in the joined result.

Here are independently reconstructed essential steps of that runtime:

1. On normalized Gram at least lambda/8, its exact raw energy identity
   gives path length at most sqrt(8) Y/sqrt(lambda). Orthogonality of the
   corrected readout's two components gives norm at most sqrt(40)
   Y/sqrt(lambda). Integrating the hidden-direction bound yields
   56 U (Y/lambda)^2 sqrt(lambda), so 224FU(Y/lambda)^2<=1 closes
   both the Gram and mixer stops.
2. Coordinate source approximation and the source metric isometry give
   selected-vector norm at most its reference norm plus 3K epsilon.
   Expanding the two source pairings produces exactly
   3K epsilon(||u||+||v||)+11K^2 epsilon^2. Substitution in each
   learned rank-one action proves the stated forward and reverse defects.
3. With V=F/sqrt(m), T=V(V*V)^(-1), residual discrepancy e, p=Te,
   raw readout discrepancy z, and zeta=z+p, the corrected readout
   difference is exactly
   (I-P)zeta-p-T(Delta V)*w_R-Td_R. The two terms 2V e and -2V e
   cancel in zeta'. This is the relevant cancellation; it does not
   assume that non-diagonal activation gates are self-adjoint.
4. Factoring the Gram difference before applying T converts one forward
   factor to the orthogonal projector P. The other forward term uses
   nu=||V_R c_n/sqrt(m)|| with integral at most (W/2)Y/sqrt(lambda).
   For the lifted residual energy, V*p=e gives its negative term
   -2||e||^2. The hidden Gram costs at most
   18J0^2(Y/lambda)^2||e||^2, absorbed by 6J0Y/lambda<=1.
5. Regularizing the norm at p=0 proves
   ||p||+integral ||e||^2/||p||<=I and
   integral ||e||<=3I/sqrt(lambda). This yields the displayed integral
   Gronwall inequality with forcing scale epsilon/sqrt(lambda), retaining
   zero initial error. The resulting raw exponent is
   C1(Y/lambda)+C2(Y/lambda)^2 sqrt(log(en)), using the corrected
   direct carrier bound above.
6. The projection derivative formulas give the stated all-query speed
   bound T1 lambda^(-1/2) rho. Hence each integrated endpoint tail is
   at most 4T1Y lambda^(-3/2) exp(-lambda t/4). The finite-horizon
   root-width conversion follows by completing the square in
   q=sqrt(log(en)); it retains the factor Y, since exp(u)-1<=u exp(u).

I also checked the elementary runtime table (29) against its recurrences.
For X=64B_rt(K+1), gR<=X and sqrt(L)<=X^L, the entries for U,F,J0,
C_f,H0,Z0,J1,G,C1,C2,O0,T1 all have the stated exponent margins.
Thus Q=X^(16L+48) bounds both reciprocal runtime smallness caps and
all four constants C1,C2,O0,T1. This yields 40Q^2 as asserted.

For the final assembly, assuming the reconciled source expressions
R0<=beta^(50Ld)(d+3)^(3d/2) lambda^(-1) ell_n^(3d/2+1) and
K_src<=beta^(4L), the following substitutions are exact or conservative:

\[
 K\le\beta^{5L},\quad X\le\beta^{7L},\quad
 Q\le\beta^{280L^2},\quad
 40Q^2B^3\le\beta^{562L^2}.
\]

The capped-gap removal is legitimate because gamma<=B^2 implies
lambda>=gamma/(mB^2). Thus lambda^(-p)<=B^(2p)(m/gamma)^p.
With A_phi=beta^1024, the displayed label condition implies
Y/lambda<=B^2 exp(-beta^(1024L))<=exp(-beta^(40L)); it also implies
Y/lambda<=Q^(-1), since beta^(40L)>=280L^2 log(beta).

The all-retained-coordinate count 1020(L+1)R0^2+10m(d+1) has ample
room for the listed raw and fixed matrices, four sample-feature caches
per layer, and a dozen sample-square solve arrays. Its use of d,m<=R0
is valid: d is dominated by the explicit dimension factor, while
m lambda<=B^2. After replacing lambda, the leading coefficient is at
most beta^(110Ld)(d+3)^(3d), since
1020(L+1)B^4<=beta^(10Ld). This is below A_phi^(Ld)(d+3)^(3d).
The error coefficient beta^(562L^2) is below A_phi^(L^2).

For d=1 the query sphere has two points. The assembly explicitly takes
two time-only source families; this handles both queries and doubles the
time coefficient count. Merely declaring a zero-angle chart would have
missed one point. The source envelope's numerical margin absorbs the
factor two. The supremum over time includes both fitted limits, while
the probability statement is for each sufficiently large width at fixed
confidence, not one asserted event simultaneously over all widths.

Subject to verification of the reconciled source addendum, all three
boxed formulas in the indicated assembly version pass this independent
algebraic and deterministic reconstruction. Their large explicit depth
factors are sufficient envelopes, not optimal architecture constants.


## 7. Final source reconciliation and verdict

The complete post-exchange source addendum, Section 7 of
`EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`, was read at SHA-256
`d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a`.
It makes every numerical substitution required by the label route:
initialized/real/complex operator caps 8,9,10; contour allowance
16Y/lambda; decay lambda/4; horizon 32 lambda^(-1) ell_n;
ordinary forward derivative bounds dominated by the augmented P_ell;
top deterministic carrier included in A_H; and constant-vector inclusion.

I checked the remaining source envelopes independently. With the new
forward bounds, f_ell and g are at most beta^(4L); their products give
r_ell<=beta^(7L) and q_ell<=beta^(8L). The mixed derivative recurrence
has forcing at most a fixed multiple of beta^(10L+1) and propagation
factor at most beta^2, giving e_ell<=beta^(14L). This yields the stated
E_Q,E_J,T_Q,T_J bounds. In particular

\[
 U_*,V_*\le\beta^{30L}\sqrt{d+3},\quad
 K_{\rm src}\le\beta^{4L},\quad M_0\le\beta^{4L}.
\]

The explicit radius formula then gives
c^(-1)<=beta^(40L)(d+3)^(3/2); the factor d-1 counts actual angular
segments and is not hidden inside the activation constant. For the new
horizon, alpha=c lambda/(128 ell_n^(3/2)), so the Fourier normalization
has exactly the displayed logarithmic constant 1024d M0 3^d
lambda^(-1)c^(-d). The bound H_n<=4 ell_n yields p+1<=514 c^(-1)
lambda^(-1) ell_n^(5/2), as stated. Multiplying the angular counts
and including exact additions proves the R envelope used in Section 6.
The separate d=1 count also lies strictly inside that envelope.

The first-weight tube is supplied explicitly: H2>=2s+4K1 implies
D>=2H2^2>=sK1, and S^2<=mathcal B^(-1) makes sK1S^2<1.
The stated beta^(50Ld) source envelope, beta^(5L) runtime coefficient,
and beta^(40L) sufficient label coefficient therefore have their
required common normalization.

**Verdict: PASS for the explicit constants and joined theorem**, relative
to the named inherited source/insertion interfaces and their fixed-data,
sufficiently-large-width quantifiers. This includes all three boxes in
assembly SHA-256
`19a307c4c8d9325605b0a88099dce8668baf1f61e3bf7088bc5ba36deee3c64d`.
The unsupported literal actual-activity normalization in the initially
frozen runtime interface is corrected explicitly in both final source
and assembly notes; the proof needs only their direct allowance-based
carrier bound. No other numerical or normalization defect was found.

This internal pass certifies the new quantification and assembly, not
independent promotion of the inherited full theorem. The width threshold
is still unquantified, all depths and dimensions are fixed before width
tends to infinity, preprocessing and precision are outside the retained
real-coordinate count, and the compressed optimizer is the already
specified corrected-readout autonomous system.
