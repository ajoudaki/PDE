# A fourth-power sufficient mixing coefficient

2026-09-07. Complete candidate proof. Current independent-review status
is recorded in REVIEW_STATUS.md. All earlier theorem files are unchanged.

## 1. Full theorem and explicit coefficient

Use the precise model and conclusions of
../two_sample_odd_activation_theorem/PROOF.md. In particular there are
two deterministic inputs with \(\|x_i\|^2=d\), all binary labels,
three hidden layers with one common activation, the original
independent Gaussian initialization with its original finite readout,
the raw gradient metric and simultaneous raw GD with step \(n^{-2}\).

Retain exactly the numerical prefactor of the preceding quantitative
theorems:
\[
C_0=1296000\exp(1404),\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
H=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4,\qquad
c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.        \tag{1}
\]
Here \(c_*\) is the explicit primal/nonaffinity constant in equation
(10) of ../two_sample_odd_activation_quantitative/PROOF.md. No numerical
constant is newly chosen after the data or trajectory are observed.

For every \(0<\delta\le1\), every such dataset satisfying
\[
|\rho|=\left|\frac{\langle x_1,x_2\rangle}{d}\right|
\le1-\delta,
\]
every \(a\in[1/2,1]\), and every
\[
0<e\le c_{\rm poly}\delta^4,\qquad
\phi_{a,e}(z)=az+e\arctan z,                        \tag{2}
\]
the complete original theorem holds. Consequently
\[
0<\theta_\delta\le c_{\rm poly}\delta^4,\qquad
\phi_\delta(z)=(1-\theta_\delta)z+
                       \theta_\delta\arctan z      \tag{3}
\]
is an admissible convex mixture. The proposed
\(c_{\rm poly}\delta^8\) choice is included.

The conclusions are the original autonomous global strong population
flow, uniqueness against nonsymmetric bounded-primal strong competitors
on the same canonical action spaces, and restart from reached states;
the full-width-sequence joint GF/raw-GD population limits on every fixed
finite physical interval; every original action/adjoint, raw kernel,
same-layer path/velocity and second-moment observable; nonaffinity at
every finite physical time and all the original initial feature-motion
certificates.

The coefficient depends on delta alone. Width convergence is for each
fixed dataset on each fixed finite interval, not uniform over datasets
or the infinite time half-line. No three-input extension is asserted.
The old very small numerical prefactor remains unchanged. Exponent
four is sufficient; neither sharpness nor necessity is claimed.

## 2. Exact intrinsic scale and the previous primal estimates

Fold labels using oddness and set
\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad
\lambda=a^3r,\quad
M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.       \tag{4}
\]
The normalized affine time is \(t=\lambda s\). Its first prediction
target \(3/2\) occurs before \(T<2\), on an original feature interval
of length \(S\), where
\[
S\le2/\lambda\le M^4,\quad
r=\frac3{\sqrt2a^3}M^{-4},\quad
M\le24^{1/4}\delta^{-1/8}.                         \tag{5}
\]
All powers of r below use its exact identity in (5); the uniform delta
envelope is used only for selecting the activation.

The previous cap-uniform primal comparison is still sufficient:
(2) implies \(e\le c_*\delta^{7/4}\). Hence its raw radius-one tube,
endpoint margin \(g_e(S)\ge5/4\), and absolute regression margin hold.
In intrinsic notation, the raw discrepancy is at most \(HeM^{12}\)
and every learned-moment coefficient discrepancy is at most
\(HeM^{15}h_j\). A backward time-row sum costs at most \(HM^4\),
giving \(H^2eM^{19}\). These are estimates on the actual capped
program before the new source bootstrap.

The same actual primal bound also gives
\[
\|q^1_k\|_2\le HM^3,\quad
\|q^2_k\|_2\le HM^2,\quad
\|C_k\|_2\le HM,                                   \tag{6}
\]
uniformly in cap and sufficiently fine fixed mesh. For example
\(q^2=B^*\delta^3\), \(q^1=A^*\delta^2\), while each capped backward
gate has norm at most \((a+e)\) times its incoming norm. The bounded
raw matrices and readout give (6), and the fixed-program identification
gives the same norms for their named source output laws.

## 3. All four gradient terms give an affine propagator of order M cubed

AFFINE_PROPAGATOR.md proves the following improvement in full, including
the numerical constants, beta enlargement and source probes.
The normalized affine system is
\[
p'=A^*B^*D,\quad A'=B^*D\otimes p,\quad
B'=D\otimes Ap,\quad D'=BAp,\quad F=\langle D,BAp\rangle.
\]
Let \(z=\|D\|^2\). The exact balances give
\[
\|p\|^2=1+z,\quad A^*A=p\otimes p+K,\quad
AA^*=B^*B+J,\quad BB^*=D\otimes D+K_B,
\]
with \(-I\le K\le100I\), \(-100I\le J\le100I\),
and \(0\le K_B\le100I\). Thus
\[
z(1+z)\le\|Ap\|^2\le(z+101)(z+1),\quad
z^2\le\|B^*D\|^2\le z^2+100z.
\]
The two matrix-gradient terms each contribute at least \(z^3+z^2\).
The other two obey
\[
\|D'\|^2\ge z^3-99z^2-10200z-10100,\qquad
\|p'\|^2\ge z^3-100z^2-10000z.
\]
Adding all four terms of \(F'=\|\nabla F\|^2\) yields
\[
F'\ge4z^3-197z^2-20200z-10100,\qquad z'=2F.
\]
Integration, followed by the previous \(F\ge z^2/\sqrt2\) bound
for small z, gives
\[
F\ge z^2-100z,\qquad
\left(\log\sqrt{1+z}\right)'\ge z-101.             \tag{7}
\]
No division by z or F at the initial point is used.

At initialization scale beta define
\(w_\beta=\sqrt{\beta^2+\|D_\beta\|^2}\). Homogeneity and (7) give
\[
(\log w_\beta)'\ge\|D_\beta\|^2-101\beta^2.
\]
The radius-one raw Hessian bound is
\(3(\sqrt{200\beta^2+\|D_\beta\|^2}+1)^2\).
Its linear-radius term is integrable with an absolute bound, using
the original radial inequality. The resulting two-time estimate is
\[
G_\beta(t,s)\le
\exp(2100)\left(\frac{w_\beta(t)}{w_\beta(s)}\right)^3
\le10^5\exp(2100)M^3.                             \tag{8}
\]
This holds on the entire common enlarged affine interval. The exact
coefficient three in front of the logarithm is retained; replacing the
radius-one expression by a fixed multiple of the squared radius would
lose this improvement.

Use the same intrinsic beta family as the preceding proof:
\[
\beta_j=1+\frac{j}{10^6(200+M^2)},\quad j=1,2,3,
\qquad
\beta_{\rm far}=1+\frac1{10^5(200+M^2)}.
\]
Every gap is at least \(H^{-1}M^{-2}\). The older continuation argument
places the whole family on the same interval. The independent-root
Gaussian probe identities then turn (8) into bounds on the actual
frozen formal coefficients, retaining both orientations and current
direct terms. No raw-tangent/source-derivative identification is assumed
without those identities.

In original feature time, write d for strict density and r for complete
causal row norm. The new affine input table is

| Quantity | Active sample sector | Full sample bound |
|---|---|---|
| \(F,A_2\), density | \(HM^{-5}\) | \(H\) |
| \(V,A_3\), density | \(HM^{-3}\) | \(H\) |
| \(T,B_3\), row | \(HM^7\) | \(HM^7\) |
| \(W,B_2\), row | \(HM^9\) | \(HM^9\) |
| All required forward/backward resolvents, row | \(HM^5\) | \(HM^5\) |
| \(U_{\rm top}\), \(FL\), \(RF\), density | \(HM^{-1}\) | \(H\) |

The inactive forward densities are bounded, its affine backward arrays
vanish, and its resolvents are identity. The numerical ledger in the
companion bounds all new prefactors by \(10^{30}\exp(2100)<H\).
Thus (1) remains an explicit admissible numerical envelope.

## 4. Source response: use the raw L2 norm after controlling the exponential

PRIMAL_L2_RESPONSE.md proves the source estimate on the sector box in
the next section. SECTOR_SUPERSOLUTION.md independently records the
same response calculation as part of its closure proof.

The full-sample transfer bounds on that box are
\[
|F|_d,|V|_d,|U_{\rm top}|_d\le H^2,\quad
|R_i|_r,|L_i|_r\le H^2M^5,\quad
|B_2|_r\le H^2M^9,\quad |B_3|_r\le H^2M^7.
\]
They are forward density and backward row bounds; arbitrary backward
row errors need not have a bounded strict density.

Solving the nonlinear source value equations by exact affine resolvents
at the same coefficient arrays and absorbing their e-weighted self
terms gives
\[
\|q^1_k\|_p\le H^{10}M^{15}\sqrt p,\quad
\|q^2_k\|_p\le H^{10}M^{13}\sqrt p,\quad
\|C_k\|_p\le H^{10}M^{11}\sqrt p,\quad p\ge2.       \tag{9}
\]
These supply subGaussian tails. They are not the bounds used for every
subsequent expectation.

For a local source population, the exact same-array derivative
identities from the preceding proof are
\[
J-J_{\rm aff}=U[\Delta V I^\zeta+PJ],\qquad
D\delta-D\delta_{\rm aff}=L[\Delta V I^\zeta+PJ],    \tag{10}
\]
where
\[
P=L_{\rm gate}+a\Delta V B+aB\Delta G+\Delta V B\Delta G,
\quad |\Delta V|,|\Delta G|\le Ce,\quad
|L_{{\rm gate},k}|\le CeQ_k.
\]
The random gates retain their full sample action. The strict U kernels
yield an exponential envelope
\[
\mathcal E_k=
\exp\left\{eH^6\sum_{r<k}h_r(Q_r+M^b)\right\},
\qquad b=9,7,4
\]
at the three populations. Weighted Jensen and (9) show
\[
eH^{22}M^{19}\le1
\quad\Longrightarrow\quad
\mathbb E\mathcal E_k^8\le2.                       \tag{11}
\]
There is no random supremum over source times.

Now apply Cauchy--Schwarz using (6), not the larger bounds (9):
\[
\mathbb E[Q_r\mathcal E_k]\le
\|Q_r\|_2\|\mathcal E_k\|_2
\le H^2M^{q_{\rm raw}},\qquad q_{\rm raw}=3,2,1.    \tag{12}
\]
This holds for any pair of times, without independence. The exact
single-insertion identities (10) contain only one explicit Q factor,
including current and source-time terms, so (12) is sufficient.
The bounded gate perturbations involving B remain in the calculation.

The resulting forward strict-density defects have powers 13 and 11;
the complete backward row defects have powers 17 and 14. The larger
learned-moment row bound from Section 2 dominates them. Explicitly,
the complete coefficient forcing satisfies
\[
q\le H^{30}eM^{19}
\quad\text{when }eH^{22}M^{19}\le1.                \tag{13}
\]
Here q denotes the common defect bound, not an incoming field.
The companion proves all terms and numerical products in (13),
including the current returns and the initial \(h_j\) factor for a
single transpose-source slot.

## 5. Separate sector boxes close at the twelfth power

All actual deterministic coefficient blocks are sample diagonal by the
previous fixed-program exchange-equivariance proof. This does not
diagonalize individual random gates or impose symmetry on physical
competitors. It permits different deterministic boxes in the two
sample sectors.

SECTOR_SUPERSOLUTION.md proves the exact closure with
\[
r_{\rm active}=H^{-10}M^{-2},\qquad
r_{\rm inactive}=H^{-10}M^{-5}                    \tag{14}
\]
for backward row excess. The active forward majorant is the reference
at \(\beta_2\); the inactive forward majorant is its affine baseline
plus a fixed strict-density margin. On this box the active Neumann
ratios are small because \(|F|_r=O(M^{-1})\) and
\(|V|_r=O(M)\). The inactive radius separately controls its integration
row of order \(M^4\). All full-sample transfer bounds in Section 4
therefore persist.

Use the same positive supersolution at \(\beta_1\) as in the preceding
theorem. Arbitrary backward causal errors \(J_3,J_2\), including their
current diagonals, are inserted exactly:
\[
A_2^*=A_{2,\beta_1},\quad A_3^*=A_{3,\beta_1},\quad
B_3^*=B_{3,\beta_1}+J_3,
\]
\[
R^*=(I-a^2A_2^*B_3^*)^{-1},\quad W^*=a^2B_3^*R^*,
\quad B_2^*=B_{2,\beta_1}+W^*-W_{\beta_1}+J_2.
\]
The backward inequalities are exact. In the forward inequalities the
strict/row/strict sandwich bound and the new active table give
\[
|FJ_2F|_d=O(M^{-6}q),\quad
|(FL)J_3(R^*F)|_d=O(M^2q).
\]
Dividing by the active leading lower bound
\(F_{kj},V_{kj}\ge H^{-2}M^{-8}h_j\) costs eight powers;
the beta margin costs two. The resulting active condition is
\(q=O(M^{-12})\). Backward reconstruction costs \(M^{10}q\)
and fits the active radius in (14) under the same condition.
The inactive equations are controlled directly, with backward rows
\(O(q)\) and forward additions \(O(M^4q)\).

The complete numerical criterion is
\[
q\le H^{-16}M^{-12}.                              \tag{15}
\]
Under (15) both sectors lie strictly inside their boxes, including
the inner/outer beta forward margin. Signed coefficients are treated by
\(|\mathcal T_0(\mathcal C)|\le\mathcal T_0(|\mathcal C|)\)
and finite chronological comparison. No lower bound on a mesh step
or backward strict-density assumption is used.

## 6. Numerical selection and the full population/GF/GD conclusion

Equation (5) gives \(M^{32}\le24^8\delta^{-4}\), and \(24^8<H\).
Thus (1)--(2) imply
\[
eM^{32}\le10^{-70}H^{-399},\qquad
eH^{22}M^{19}\le10^{-70}H^{-377}<1,
\]
\[
qM^{12}\le H^{30}eM^{31}
\le10^{-70}H^{-369}<H^{-16}.                       \tag{16}
\]
At each fixed cap and sufficiently fine mesh, the source coefficients
are continuous along the amplitude homotopy from zero to e. At a
proposed first exit from (14), (13) and (16) hold, while the positive
supersolution puts all bounds strictly inside. This contradiction
closes the source construction uniformly in cap and mesh.

The original downstream bridges now have every required premise:
bounded primal feature paths, cap/mesh-uniform subGaussian incoming
fields, and an endpoint prediction above one. Strong asymmetric cap
comparison constructs the uncut autonomous feature flow. Its first-hit
clock gives one global physical population trajectory. The physical
estimate retains both actual residuals and proves nonsymmetric
uniqueness and restart from reached states.

At finite width, the original initialized readout is retained. Width
is taken at fixed cap and auxiliary mesh, deterministic Euler estimates
remove the mesh, and then the asymmetric comparison removes the cap.
The prescribed simultaneous raw GD has its original \(C_{R,T}n^{-2}\)
reference error. No Gaussian theorem for growing transcripts or trained
operator-norm convergence across widths is invoked.

The old velocity bridge retains product-query truncation and the order
of cap removal at fixed reference-velocity truncation, followed by
removal of that truncation. The uncut velocity has a compact continuous
L2 time image. These facts preserve all original velocity/path laws,
second moments, integrated squared speeds, kernels and action/adjoint
conclusions. The prior absolute regression margin and odd-family
initial-motion proof impose no further amplitude restriction.

This proves the complete theorem under (2), and hence (3). The new
power count is \(19+12=31<32\). The separate improvement of the
extremely small universal prefactor remains open.
