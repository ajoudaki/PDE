# Four hidden layers with the same explicit power-ten coefficient

2026-09-07. This assembly and AFFINE_CERTIFICATE.md, SOURCE_RESPONSE.md,
and POPULATION_AND_MOTION.md constitute the four-layer proof. The
separate DEPTH_UNIFORMITY.md proves the stated initialization obstruction
and records precisely what remains open at arbitrary depth. Review
status and file identities are recorded separately and are not premises.

## 1. Statement and unchanged numerical pair

Let
\[
C_0=1296000\exp(1404),\quad C_z=1500C_0,\quad C_g=14400C_0,
\quad \eta_*={4\cdot404\exp(-1)\over27\pi\,405^4},
\]
\[
c_* =\min\left\{\frac12,
 {1\over2C_0(8\sqrt2)^3},
 {1\over4C_g(8\sqrt2)^{11/4}},
 {\sqrt{\eta_*}\over2C_z(8\sqrt2)^{7/2}}\right\},
\]
\[
H=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4,
\qquad c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.       \tag{1}
\]
These are exactly the constants of the earlier L3 power-ten theorem;
none is reselected after adding a layer.

For every \(0<\delta\le1\), every fixed deterministic dataset
\[
\|x_i\|^2=d,\qquad \rho=x_1^Tx_2/d,\qquad
|\rho|\le1-\delta,\qquad y_i\in\{-1,1\},                 \tag{2}
\]
and every
\[
\frac12\le a\le1,\qquad 0<e\le c_{\rm poly}\delta^{10},
\qquad \phi(z)=az+e\arctan z,                             \tag{3}
\]
the original complete population/GF/raw-GD theorem holds with **four
hidden layers**, in the precise form below. In particular the same
\[
0<\theta\le c_{\rm poly}\delta^{10},\qquad
\phi_\theta(z)=(1-\theta)z+\theta\arctan z                \tag{4}
\]
works at both L3 and L4. The coefficient depends on delta alone, not
the angle within (2), labels, dimension, width, physical horizon, or
which of these two depths is used.

At width n use independent entries
\[
W^1_{ij}\sim N(0,1/d),\quad W^\ell_{ij}\sim N(0,1/n)
\ (\ell=2,3,4),\quad C_i\sim N(0,n^{-2}).
\]
With \(\langle u,v\rangle_n=u^Tv/n\), set
\[
z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
z_i^\ell=W^\ell h_i^{\ell-1}\ (\ell=2,3,4),\quad
f_i=\langle C,h_i^4\rangle_n,\quad r_i=f_i-y_i,
\]
\[
b_i^4=C\phi'(z_i^4),\qquad
b_i^\ell=\phi'(z_i^\ell)(W^{\ell+1})^Tb_i^{\ell+1}
\quad(\ell=3,2,1).
\]
The loss \(\mathcal L=\frac12\sum_i r_i^2\) has raw metric
\[
\|d\Theta\|_{\rm raw}^2={d\over n}\|dW^1\|_F^2
+\sum_{\ell=2}^4\|dW^\ell\|_F^2+\|dC\|_n^2.
\]
Its exact GF is
\[
\dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
\dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
\quad \dot C=-\sum_i r_i h_i^4.                          \tag{5}
\]
GD is simultaneous Euler for (5) with step n^-2. Raw parameters are
interpolated linearly; hidden fields are recomputed, with right
derivatives at nodes and left derivatives at a terminal endpoint.
The finite random readout is retained throughout.

The conclusions are:

1. There is one global autonomous strong C1 population solution of
   (5) on four canonical neuron L2 spaces, three bounded initialized
   adjacent actions and their genuine adjoints, with HS learned
   increments. It is unique among bounded-primal strong competitors
   on those spaces, including nonsymmetric ones, and restarts uniquely
   from every reached state. The population initial readout is zero.
2. For every fixed finite physical T, both finite GF and the prescribed
   raw GD converge along the full width sequence in probability to
   that solution. Predictions, loss and all five raw kernels converge
   uniformly in time. Both action orientations on generated probes,
   same-layer joint field laws including true hidden velocities
   converge in Wasserstein-2 uniformly in time and jointly at any
   fixed finite collection of times. Their second moments and
   integrated squared speeds converge as well.
   The same-layer (z,h) path laws converge in Wasserstein-2 for the
   uniform path norm. No cross-layer coordinate pairing is asserted.
3. For every layer, sample and finite physical time,
   \[
   \inf_{\alpha,\beta}\mathbb E[
      \phi(z_i^\ell)-\alpha-\beta z_i^\ell]^2
                \ge e^2\eta_*/4>0.                     \tag{6}
   \]
   Every hidden raw block and every sample's layer preactivation and
   feature has a nonzero initial second derivative. The projected
   total kernel changes immediately to second order; the readout
   already has nonzero initial velocity. Perpetual nonzero hidden
   velocity is not asserted.
4. The population loss obeys
   \[
   \mathcal L(t)\le\exp(-2a^8\delta t).                 \tag{7}
   \]
   Thus the compact gain rectangle has rate at least delta/128. For
   the requested convex mixture (4), a>=3/4, and the earlier weaker
   rate \(\mathcal L(t)\le\exp(-\delta t/32)\) is retained.

The five kernels are
\[
K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_n,\qquad
K^\ell_{ij}=\langle b_i^\ell,b_j^\ell\rangle_n
                 \langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n
\ (\ell=2,3,4),\qquad
K^5_{ij}=\langle h_i^4,h_j^4\rangle_n,                    \tag{8}
\]
where \(\Gamma_{ij}=x_i^Tx_j/d\); population brackets are L2
inner products. In particular \(\dot f_i=-\sum_j\sum_{\ell=1}^5
K^\ell_{ij}r_j\).

## 2. Proof structure and affine input

Odd label folding replaces (x_i,y_i) by (y_i x_i,1) without changing
the finite raw loss or parameter path. Exchange of the two folded
inputs preserves their Gaussian initialization and equations. The
fixed-program population construction and its strong limits therefore
have \(f_i=y_i g\). This proves symmetry for the constructed flow;
it is not assumed for competitors. The population loss is (1-g)^2.
Feature time s is defined by the gradient field \(\Theta'=\nabla g\).

Write
\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad \lambda=a^4r,
\qquad M=\left({3\sqrt5\over2\lambda}\right)^{1/5}>1.
                                                               \tag{9}
\]
AFFINE_CERTIFICATE.md derives the exact normalized affine equations
for \(F=\langle D,A_4A_3A_2p\rangle\), \(g=\lambda F\),
in auxiliary time t=\(\lambda s\). Adjacent Gram balance identities
bound all primary norms by \(\sqrt{48+\|D\|^2}\). With c=\|D\|,
\[
F'\ge c^6(1+c^2),\quad F\ge c^5/\sqrt5,\quad
c'\ge1,\quad c'\ge c^4/\sqrt5.                          \tag{10}
\]
These prove strong affine continuation through its first hit g=3/2,
with feature duration S and
\[
S\le2/\lambda<M^5,\qquad
M^{100}\le76^{20}\delta^{-10}.                          \tag{11}
\]
The same balances strengthen the integrated radius-one-tube Hessian
bound to \(4000+4\log M\); hence the affine propagator is at most
\(e^{4000}M^4\). Explicit same-state capped comparison and integration
of its forcing give raw discrepancy \(HeM^{10}\), forward discrepancy
\(HeM^{13}\), and endpoint discrepancy \(HeM^9\). None of these
constants depends on the backward cap. Enlarging the affine Gaussian
initialization at three nearby beta scales leaves common time room
and adjacent gaps at least \(H^{-1}M^{-3}\).

The source proof deliberately uses the weaker M9 propagator and its
corresponding bounds. The affine certificate proves all its inputs,
including their explicit prefactors, by independent Gaussian answer
probes, exact time/sample normalization, both orientations, and current
direct terms. Thus the table in SOURCE_RESPONSE.md section 2 is a
proved interface, not an extra assumption. Its forward full-density
powers are (0,1,3), backward complete-row powers (18,16,14), local
resolvent row power 12, and local strict-transfer powers (0,1,3,5).

The same affine finite programs prove inactive-field freezing and
Gaussianity. A positive Gaussian polynomial expansion gives
\(\|A_\ell\cdots A_2p\|_2^2\ge1\) along the affine path:
each finite Euler polynomial contains its initialized chain and
all extra Wick contributions to its second moment are nonnegative.
Consequently every affine sample variance is at least
\(a^{2(\ell-1)}\ge1/64\). The old third-Hermite regression lower
bound eta_* therefore applies. The square root of the arctangent
regression residual is 1-Lipschitz under L2 coupling, so the forward
comparison preserves (6) once the cap is removed.

## 3. Six response coefficients and the new layer

SOURCE_RESPONSE.md derives all six exact coefficient families
\((A_2,A_3,A_4,B_4,B_3,B_2)\). The A families are strict causal;
the B families include current returns. Their terms are expected
formal Gaussian-source derivatives plus the actual learned moments.
All source covariances are full second moments. At a formal derivative
the coefficient arrays and Gaussian covariances are frozen, with
named source slots distinct even at singular covariance.

At each local population set \(Z=\xi+K\delta\),
\(q=\zeta+Bh\), \(h=\phi(Z)\), and
\(\delta=aq+e(1+Z^2)^{-1}\tau_R(q)\). The exact same-array
affine derivative subtraction is
\[
J-J_0=U[\Delta V I_\zeta+P J],\qquad
\partial\delta-\partial\delta_0=L[\Delta V I_\zeta+PJ],
                                                               \tag{12}
\]
where \(U=(I-a^2KB)^{-1}K\), \(L=(I-a^2BK)^{-1}\), and
every term in P has a factor e or e times an incoming field. The
companion gives P explicitly and retains all sample gate entries and
current diagonals. Solving source values first gives uniform marginal
subGaussian tails. Strict U then gives derivative envelopes controlled
by deterministic time weights and those marginal tails, without a
random supremum over source times.

The resulting defect bounds, in strict density for the forward
families and complete row norm for the backward families, are
\[
(d_2,d_3,d_4)\le H^{40}e(M^{35},M^{35},M^{37}),\qquad
(q_2,q_3,q_4)\le H^{40}e(M^{52},M^{50},M^{41}).          \tag{13}
\]
They include learned-moment errors. The derivative moment restriction
is \(eH^{30}M^{35}\le1\).

At the inner beta scale freeze the three forward coefficients and
add backward errors recursively. In the notation of the companion,
\[
\Delta_4=J_4,\quad
\Delta_3=J_3+a^2L_3J_4R_3^*,\quad
\Delta_2=J_2+a^2L_2J_3R_2^*
                   +a^4L_2L_3J_4R_3^*R_2^*.            \tag{14}
\]
Positivity makes these exact backward supersolutions. Two extra
resolvent pairs cost M48 on the top error, whose power is only 41.
The largest backward excess is therefore \(H^{50}eM^{89}\).
It lies inside the complete-row radius \(H^{-20}M^{-9}\)
provided \(eH^{72}M^{98}\le1\).

For the forward comparison, positive identities compress strict
chains, for example \(V_iL_{i+1}\le V_{i+1}/(\beta^2a^2)\).
Each backward error retains strict factors on both sides, preserving
the actual source step h_j. The most restrictive forward condition
is only \(eH^{63}M^{86}\le1\). The inactive sector closes separately
with its zero affine backward rows. The outer and inner beta margins
leave strict entrywise forward slack and full backward-row slack.
Amplitude homotopy and finite chronological first-exit comparison
therefore bound the actual arrays on every cap and sufficiently fine
mesh. Section 5 of the companion proves these assertions including
the individual powers; no generic inverse of the entire coefficient
system or missing-step-density bound is used.

By (1), (3), (11) and \(76^{20}<H\),
\[
eM^{100}\le10^{-70}H^{-399},\qquad
eH^{72}M^{98}\le10^{-70}H^{-327}<1.                     \tag{15}
\]
This also enforces every tube, endpoint, moment, forward-slack and
nonaffinity restriction. For the latter it suffices that
\(HeM^{13}\le\sqrt{\eta_*}/2\), and the explicit value of eta_*
in (1) makes this immediate from (15). Thus the complete source
construction is valid with the unchanged numerical pair (c_poly,10).

## 4. Strong population construction, global time and full limits

POPULATION_AND_MOTION.md verifies the four-layer construction and
limit steps explicitly. The finite Gaussian conditioning theorem used
in the earlier proof covers any fixed finite list of independent
matrices; it is applied to all three adjacent square matrices in both
orientations. Fixed-cap coordinate maps have linear growth and bounded
derivatives. Finite rank regularization handles singular queries. The
generated Gaussian spaces admit three bounded adjacent initialized
actions, and finite transpose identities give their genuine adjoints.
Fixed-cap Euler comparison and rank-one unrolling control all five
raw blocks with width-independent constants on the stopped primal
ball. The affine tube above supplies its strict margin.

Backward substitution in the asymmetric gate comparison gives one
factor (1+eR) multiplying the raw discrepancy. Four gates change its
finite constant, not its degree in R. The source tails from section 3
therefore bound cap errors by
\[
C\exp\{C(1+eR)S-cR^2\}\longrightarrow0.                \tag{16}
\]
This yields a strong C1 uncut gradient path through S and the endpoint
g(S)>=5/4. The cap limit also preserves (6).

For the initialized nonlinear forward recursion let q_l,c_l be its
common feature variance and cross moment after l layers. Oddness and
phi'>=a imply \(q_l\pm c_l\ge a^{2l}(1\pm\rho)\).
Writing \(\kappa=\|\nabla g\|_{\rm raw}^2\), the zero initial
population readout gives
\[
\kappa(0)=(q_4+y_1y_2c_4)/2\ge a^8\delta/2.            \tag{17}
\]
Along the constructed feature path write H for the label-projected
top feature in this paragraph only. The identities C'=H and
C''=JJ^*C, with J its hidden derivative, make \|C\| convex and
imply \(\kappa(s)\ge\|C'(s)\|^2\ge\kappa(0)\).

Let s_* be the first hit g=1, before S. The function
\[
t(s)=\int_0^s{du\over2(1-g(u))}
\]
diverges at s_* because g' is bounded on the compact feature path.
Its inverse produces the global physical solution of (5). Moreover
\(\dot{\mathcal L}=-4\kappa\mathcal L\), so (17) proves (7).
All finite physical times occur inside the already controlled feature
interval; the activation is not reselected for longer times.

Physical asymmetric comparison retains both residuals, uses tails
only from the constructed reference, and proves uniqueness against
nonsymmetric bounded-primal competitors. Starting it at a reached
state proves restart. Width is taken first at fixed cap and finite
auxiliary mesh; deterministic Euler estimates remove that mesh, then
(16) removes the cap on any fixed physical horizon. The prescribed
raw GD adds \(C_{R,T}n^{-2}\). The readout initialization has RMS
norm \(O_{\mathbb P}(n^{-1})\) and is retained until its limit.

The additional velocity queries are now W2 U1, W3 U2, and W4 U3.
The companion derives all four forward velocity identities, applies
finite-program conditioning to their truncated products, and gives
the deterministic reference-tail comparison. Width precedes cap
removal at fixed truncation; the final velocity truncation is removed
using the compact L2 time image of the uncut velocity. Convergent L2
products yield the five kernels (8), all required second moments and
integrated speeds. The interpolation inequality
\(\|x-I_hx\|_\infty^2\le4h\int|x'|^2\), combined with fixed-grid
joint Wasserstein-2 convergence, gives the stated same-layer path laws.

The companion also proves strict positivity of every initial backward
full second-moment matrix by a downward three-transpose induction,
retaining all reuse responses. Each hidden block's acceleration norm
is a positive contraction with the preceding positive forward Gram.
Adjunction and exchange symmetry then make both sample accelerations
nonzero at every layer. With V the total hidden feature-time initial
acceleration, \(\|V\|>0\),
\[
\kappa(s)=\kappa(0)+2s^2\|V\|^2+o(s^2),\qquad
\kappa(t)=\kappa(0)+8t^2\|V\|^2+o(t^2).                 \tag{18}
\]
This proves the motion claims and completes the four-layer theorem.

The energy-normalized family from the earlier theorem is also
admissible: for \(0<r_0\le c_{\rm poly}\delta^{10}\), set
\(D=\sqrt{\mathbb E(G+r_0\arctan G)^2}\). Then 1<D<1+r_0<=2,
so a=1/D and e=r_0/D satisfy (3), and the activation has exactly unit
Gaussian energy. This is distinct from the convex weights in (4).

## 5. What follows, and does not follow, for arbitrary depth

The new layer is covered with the same pair (c_poly,10). This does
not prove a common positive pair for all finite L. The general
adjacent balance, source and supersolution identities are recorded
in the companions, but their explicit bounds depend on L. A source
estimate valid for all finite L at one common amplitude remains open.

There is a separate rigorous limitation on depth-uniform numerical
convergence bounds for the convex mixture. DEPTH_UNIFORMITY.md proves
for each fixed theta in (0,1), with the width limit taken first,
\[
q_L\sim{1\over2\theta L},\qquad
{\delta q_L\over2}\le\kappa_L(0)\le q_L.                \tag{19}
\]
Thus \(\mathcal L_L'(0)=-4\kappa_L(0)\to0\), precluding
\(\mathcal L_L(t)\le\exp(-\gamma_\delta t)\) with any common
positive gamma_delta for all L and all t>=0. The initialized
activation regression residual is asymptotic to
\(1/(12\theta L^3)\), so it too has no positive uniform lower
bound. Both quantities are strictly positive at each finite L.
These facts do not disprove one common mixing coefficient yielding
the qualitative theorem at every fixed finite depth with other
constants allowed to depend on L. That question is unresolved here.

The prefactor (1) remains the previous very conservative one. Neither
a practical prefactor nor optimality of exponent ten is claimed.
