# A polynomial mixing coefficient for the odd two-input theorem

2026-09-07. Candidate assembled from independently derived affine and
source lemmas. Final review status is recorded separately. The previous
existence theorem and its proof files are unchanged.

## 1. Precise result

There is an absolute constant \(c_{\rm poly}>0\), specified below, such that
for every \(0<\delta\le1\), every
\[
 a\in[1/2,1],\qquad 0<e\le c_{\rm poly}\delta^{800},
 \qquad \phi_{a,e}(z)=az+e\arctan z,                     \tag{1}
\]
the complete theorem in
../two_sample_odd_activation_theorem/PROOF.md holds for all two-input
datasets with
\[
 \|x_1\|^2=\|x_2\|^2=d,\qquad
 |\rho|=\left|\frac{x_1^Tx_2}{d}\right|\le1-\delta,
 \qquad y_1,y_2\in\{-1,1\}.                            \tag{2}
\]
In particular,
\[
 \theta_\delta=c_{\rm poly}\delta^{800},\qquad
 \phi_\delta(z)=(1-\theta_\delta)z+
                         \theta_\delta\arctan z        \tag{3}
\]
is an admissible convex mixture.

The original independent Gaussian initialization, raw gradient metric
and simultaneous raw GD step \(n^{-2}\) are retained. The conclusions
are one autonomous global strong population flow, uniqueness against
bounded-primal strong competitors on the same canonical action spaces,
unique restart from reached states, and the full-width-sequence joint
GF/GD limits on every fixed finite physical interval. All four raw
kernels, both action orientations and adjoints on generated probes,
the stipulated same-layer path/velocity laws and second moments are
included. Every sample/layer remains nonaffine in the activation
regression sense; all initial hidden block and sample/layer
accelerations are nonzero.

The coefficient in (3) depends only on \(\delta\). This is not
convergence uniformly over datasets or over the infinite physical
half-line. The exponent 800 is a conservative sufficient exponent;
neither its optimality nor sufficiency of \(c\delta^2\) is claimed.
The constants below are also conservative.

## 2. The old selection and the new proof architecture

The literal old choice used
\[
 S_{\rm old}=192/\delta,\quad U_{\rm old}=11+12\sqrt{2/\delta},
 \quad p_{\rm old}=11+2U_{\rm old}+4S_{\rm old}(2U_{\rm old})^3,
\]
and contained the restriction
\[
 e_{\rm old}\le
 \frac{1}{1280p_{\rm old}^{\,2}S_{\rm old}
                   \exp(36p_{\rm old}^{\,2}S_{\rm old})}.
\]
Thus \(p_{\rm old}=\Theta(\delta^{-5/2})\) and that particular
selection obeys
\[
 e_{\rm old}\le C\delta^6\exp(-c/\delta^6).              \tag{4}
\]
Additional response constants could make it smaller still. Equation
(4) is not a necessary restriction on a successful activation and
does not identify the actual optimal threshold.

Two changes replace this dependence. First, exact balance identities
give logarithmic integrated affine curvature even though the affine
feature interval has length of order \(\delta^{-1/2}\). Second, positive
scaling of the affine Gaussian initialization controls the coupled
source-response inverse. The nonlinear source equations are then
treated using these exact affine inverses, so their only exponential
derivative envelope is multiplied by \(e\). Small polynomial \(e\)
controls that envelope.

The complete companion arguments are
AFFINE_POLYNOMIAL_BOUNDS.md and POLYNOMIAL_RESPONSE_LEMMA.md.
OLD_THRESHOLD_AND_NONAFFINITY.md supplies additional checks of (4)
and the Gaussian regression estimates. Preliminary audits concern
individual components; complete-theorem audits are recorded separately.

## 3. Polynomial affine bounds and a uniform nonlinear margin

Fold labels exactly as in the old theorem, so both labels become
positive. Let \(\tau=y_1y_2\), \(\sigma=y_1\), and put
\[
 v=\frac{1+\tau\rho}{2},\qquad r=\sqrt v,\qquad
 \lambda=a^3r,\qquad \frac{\sqrt\delta}{8\sqrt2}\le\lambda\le1.
\]
For the affine activation \(az\), set \(p=P_1/r\), \(D=\sigma C\),
and use normalized feature time \(t=\lambda s\).
The active gradient system is exactly
\[
 \dot p=A^*B^*D,\quad
 \dot A=B^*D\otimes p,\quad
 \dot B=D\otimes Ap,\quad
 \dot D=BAp.                                             \tag{5}
\]
Its objective is \(F=\langle D,BAp\rangle\), and \(g=\lambda F\).
The first-layer raw metric on the normalized active coordinate is
exactly its \(L^2\) metric. Perpendicular first-layer directions are
annihilated by the affine objective, including in variations of a
nearby nonlinear state.

With \(c=\|D\|\), the exact balance identities are
\[
 BB^*-D\otimes D=B_0B_0^*,\qquad
 AA^*-B^*B=A_0A_0^*-B_0^*B_0,
\]
\[
 A^*A-p\otimes p=A_0^*A_0-p_0\otimes p_0,\qquad
 \|p\|^2=1+c^2.                                         \tag{6}
\]
Consequently \(\|B\|^2\le100+c^2\), \(\|A\|^2\le200+c^2\),
and \(F\ge c^4/\sqrt2\). Radial convexity gives
\(c(t)\ge t\) and \(\dot c\ge c^3/\sqrt2\) after zero.
The first hit \(T\) of \(F=3/(2\lambda)\) therefore satisfies
\[
 T<2,\quad S=T/\lambda\le2/\lambda,\quad
 c\le M:=\left(\frac3{\sqrt2\lambda}\right)^{1/4},
\]
\[
 \int_0^T(200+c^2)\,dt\le401+\sqrt2\log M.                \tag{7}
\]
The strong endpoint and polynomial local existence arguments in the
companion prove existence through this hit.

The affine Hessian has norm at most \(3\lambda(200+c^2)\)
in the sum of the four raw component norms. In a raw radius-one tube
its integrated Lipschitz bound is at most \(1404+5\log M\).
The same-state capped nonlinear forcing is at most \(40eb^3\);
only the affine field is differentiated in the comparison.
The companion proves, uniformly in cap,
\[
 E_{\rm raw}\le C_0e\lambda^{-3},\quad
 \max_{i,\ell}\|z_{i,e}^{\ell}-z_{i,0}^{\ell}\|_2
                  \le C_z e\lambda^{-7/2},\quad
 |g_e(S)-3/2|\le C_g e\lambda^{-11/4},                    \tag{8}
\]
where
\[
 C_0=1296000\exp(1404),\qquad C_z=1500C_0,\qquad C_g=14400C_0.
\]

The variance loss of the old proof is unnecessary on actual reference
fields. From (6), radial coercivity and
\(\|B_0A_0p_0\|=1\),
\[
 \|BAp\|^2\ge1,\qquad
 \|Ap\|^2\ge
 \max\{c^2(1+c^2),(100+c^2)^{-1}\}\ge1/101.
\]
The frozen inactive Gaussian field is orthogonal to the active field.
Since \(v+(1-v)=1\), the three sample preactivation variances are at
least \(1,1/404,1/16\), respectively.

For \(\mathcal R(Z)=\inf_{\alpha,\beta}
\mathbb E[\arctan Z-\alpha-\beta Z]^2\), the Hermite calculation
in the companion supplies the absolute lower bound
\[
 \mathcal R(z_{i,0}^{\ell}(s))\ge
 \eta_*:=\frac{4\cdot404\exp(-1)}{27\pi\,405^4}>0.        \tag{9}
\]
Also \(\sqrt{\mathcal R}\) is 1-Lipschitz in \(\mathcal W_2\):
the optimal regression slope of arctangent lies in \([0,1]\), so
\(z\mapsto\arctan z-\beta z\) is 1-Lipschitz for that slope.
Testing its regression residual on a coupled second variable proves
the assertion in both directions. No inverse variance is needed.

Define
\[
 c_*=\min\left\{\frac12,
 \frac1{2C_0(8\sqrt2)^3},
 \frac1{4C_g(8\sqrt2)^{11/4}},
 \frac{\sqrt{\eta_*}}{2C_z(8\sqrt2)^{7/2}}\right\}.        \tag{10}
\]
Every \(e\le c_*\delta^{7/4}\) closes the radius-one tube, gives
\(g_e(S)\ge5/4\), and preserves
\(\mathcal R(z_{i,e}^{\ell})\ge\eta_*/4\) through the entire capped
feature interval. These statements alone are not the population
limit theorem; the source estimates below are also required.

## 4. Polynomial affine source inputs, including enlarged initialization

Here we verify every input to POLYNOMIAL_RESPONSE_LEMMA.md, rather
than assuming that a raw tangent estimate is a source theorem.
Uniformly over the data, let
\[
 M_\delta=24^{1/4}\delta^{-1/8},\qquad
 S_\delta=16\sqrt2\,\delta^{-1/2},\qquad
 R_\delta=\sqrt{200+M_\delta^2}.
\]
The symbol \(R_\delta\) in this section is a primal radius, not a
backward cutoff.

Choose
\[
 \beta_*=1+\frac1{10^5R_\delta^2}.                       \tag{11}
\]
The affine normalized trajectory extends beyond its own endpoint by
at least \(1/(1000R_\delta^2)\) while its component sizes stay below
\(2R_\delta\). Indeed on that larger ball the sum vector-field norm
is at most \(32R_\delta^3\); the indicated time changes the sum norm
by less than \(R_\delta/2\), so a stopped local existence argument
closes. Its added integrated radius-one-tube Hessian bound is less
than one. As \(T<2\),
\[
 \beta_*^2T-T\le6(\beta_*-1)
                        <1/(1000R_\delta^2).
\]
Homogeneity gives the scaled trajectory
\(\Theta_\beta(t)=\beta\Theta_1(\beta^2t)\). Thus the same original
mesh interval is admissible for every \(\beta\in[1,\beta_*]\).
The affine propagator on the reference and enlarged reference has
the uniform bound
\[
                         G_\delta\le \exp(1410)M_\delta^5.          \tag{12}
\]
For sufficiently fine Euler meshes enlarge this bound by a factor
two. Strong affine Euler convergence supplies that margin.

Use the exact affine Gaussian-probe identity from Sections 5--7 of
the attached TWO_SAMPLE_SOURCE_BASELINE.md. A perturbation of one
matrix answer at time \(j\) first changes an update with its factor
\(h_j\); the four answer perturbation costs are at most \(3b\).
The four output Lipschitz costs are at most \(2b\). Propagation with
(12), followed by the independent Gaussian probe identity, gives
each expected affine derivative entry a bound
\(6b^2G_\delta h_j\). Summing entries gives a backward row bound
\(6b^2G_\delta S_\delta\). The affine current return is zero.
Learned moments add at most a universal multiple of \(b^4h_j\).
The argument also works at the scaled Gaussian variance \(\beta^2\),
whose extra return factor is at most four.

For clarity, this applies the same fixed-program probe identity as
the old proof, not a new identification of a derivative after an
uncontrolled limit. One may use the deterministic perturbation
estimate on the common generated population actions at each fixed
mesh; they retain both probe and reference programs and their
adjoints. The affine fields are polynomials, so their Euler
approximations converge strongly. Then the finite-program
independent-root identity and its continuous probe-amplitude limit
give the formal coefficient. Alternatively, finite affine Euler
balance identities have only \(O(\max h_j)\) defects on bounded
prefixes and give the same deterministic bounds before the width
limit. No covariance inverse or growing-transcript theorem is used.

All reference, enlarged reference and radius-one nonlinear primal
quantities can be bounded by
\[
                         b_\delta=200\delta^{-1/8}.      \tag{13}
\]
For the finite-array premise, each affine matrix HS path-length
integral is at most \(500M_\delta\), by the companion's change of
variable in (7). Strong population affine Euler approximation and
fixed-mesh convergence of the update-factor contractions give
finite sums of update norms at most \(502M_\delta\) with probability
tending to one. Exact rank-one unrolling and the initial norm bound
ten therefore supply, for example,
\[
                         P_\delta=12+600M_\delta.        \tag{14}
\]
This verifies the finite-array premise without trained operator-norm
convergence across widths.

The following exponents verify the full polynomial input interface.
Each table bound has an absolute coefficient independent of
\(\delta\), data, gain, mesh and cap:

| Interface input | Upper bound as \(\delta\downarrow0\) |
|---|---|
| \(S_\delta\) | \(C\delta^{-1/2}\) |
| \(v^{-1}\) | \(2\delta^{-1}\) |
| \((\beta_*-1)^{-1}\) | \(C\delta^{-1/4}\) |
| primal norms and source Gaussian standard deviations | \(C\delta^{-3/8}\) |
| affine forward coefficient density | \(C\delta^{-7/8}\) |
| affine backward coefficient row norm | \(C\delta^{-11/8}\) |
| raw state discrepancy divided by \(e\) | \(C\delta^{-3/2}\) |
| preactivation discrepancy divided by \(e\) | \(C\delta^{-7/4}\) |
| each learned-moment coefficient discrepancy divided by \(e h_j\) | \(C\delta^{-15/8}\) |

The forward/row entries use
\(b_\delta^2G_\delta+b_\delta^4=O(\delta^{-7/8})\).
For the last entry, write \(E\) for (8). Direct gate comparison to
the affine gate, requiring no nonlinear Lipschitz estimate, gives
\[
 \|\Delta h^1\|\le E+\pi e/2,\quad
 \|\Delta h^2\|\le2b_\delta E+\pi e b_\delta,\quad
 \|\Delta b^3\|\le E+e b_\delta,\quad
 \|\Delta b^2\|\le2b_\delta E+3e b_\delta^2.
\]
The corresponding norms are at most \(2b_\delta\) in the first and
third cases and \(4b_\delta^2\) in the second and fourth. The
identity for a difference of two inner products therefore bounds
every learned second-moment difference by
\(C(b_\delta^3 E+e b_\delta^4)\), proving the table.
A backward row sum costs an extra \(S_\delta\); the source lemma
explicitly pays \(B^2e\) for that sum, rather than requiring the
last table entry to bound the whole row divided by \(e\).

One fully numerical envelope for the coefficients in this table is
\[
 C_B=10^{30}\bigl(1+C_0+C_z+C_g+\exp(1410)\bigr)^4,\qquad
                         B_\delta=C_B\delta^{-2}.        \tag{15}
\]
To check its coefficient slack, \(M_\delta<3\delta^{-1/8}\),
\(S_\delta<23\delta^{-1/2}\), and (13) bound all elementary
factors above. The probe coefficient is bounded by
\(100b_\delta^2G_\delta+100b_\delta^4\), including scaled variance
and Euler margins. After separating the powers of \(\delta\), its
numerical coefficient is at most
\(100\cdot200^2\cdot3^5\exp(1410)+100\cdot200^4\).
The largest moment-comparison numerical coefficient is at most
\(40\cdot200^3 C_0(8\sqrt2)^3+40\cdot200^4\).
These are below \(C_B\), as are
\(10^5(200+9)\), all listed comparison constants, and the fixed
two-sample basis conversion factors. Every exponent in the table
is at most two. Thus (15) verifies all inputs of the source lemma
uniformly, with no untracked dependence on \(\delta\).

## 5. The polynomial response estimate and final coefficient

POLYNOMIAL_RESPONSE_LEMMA.md proves the following precise implication.
If its affine, enlarged-scale and stopped nonlinear inputs are
bounded by \(B\ge2\) in the specified norms, then
\[
                         e\le10^{-70}B^{-400}             \tag{16}
\]
gives cap- and mesh-uniform source-response bounds and subGaussian
incoming fields. Its crucial new step is a polynomial bound for
the complete coupled affine coefficient inverse, not just the raw
variational propagator. We summarize its proof to identify the
mathematical dependencies.

The affine coefficients satisfy an exact causal fixed-point system
with four blocks, retaining both matrix orientations and all
learned memories. In the active sample sector its coefficients and
learned moments are nonnegative polynomials in a positive Gaussian
initialization scale \(\beta\). Gaussian conditioning at variance
\(\beta^2\) multiplies each formal return by \(\beta^2\).
Differentiating in \(\beta\) supplies a positive forcing for the
coupled coefficient Jacobian. Its strict entries are bounded below
by a fixed multiple of \(v h_j\).

For a polynomial with nonnegative coefficients,
\(f'(1)\le f(\beta_*)/(\beta_*-1)\). The enlarged-scale affine
probe bound therefore dominates the full causal inverse. All
other sample sectors are acyclic. An exact algebraic shift
converts arbitrary backward row forcing, including current
diagonals, into strict forward forcing; the kernel sandwich
bound preserves the \(h_j\) factor without a smallest-step
assumption.

Near that affine solution, exact affine resolvents and a Neumann
estimate bound source values polynomially. Applying these same
resolvents before estimating formal derivatives leaves only
perturbative drift \(e(1+Q_r)\), with strict time weights.
The derivative envelope is proportional to
\(\exp(eP\sum h_r(1+Q_r))\); its required moments are bounded
under polynomial smallness. The current backward factors and
both endpoint multipliers are retained.

The explicit estimates in that lemma give, for coefficient
discrepancy \(D\) in its mixed density/row norm,
\[
 D\le2\cdot10^{36}B^{220}e+10^{26}B^{120}D^2.
\]
Amplitude homotopy at each fixed cap and mesh closes inside
\(D\le(4\cdot10^{26}B^{120})^{-1}\) under (16).
No exponential in a polynomial of \(1/\delta\) is introduced.

Now specify the universal coefficient in (1):
\[
 c_{\rm poly}=\min\{1/4,\ c_*,\ 10^{-70}C_B^{-400}\}>0.   \tag{17}
\]
For \(0<\delta\le1\), \(e\le c_{\rm poly}\delta^{800}\)
implies both \(e\le c_*\delta^{7/4}\) and
\(e\le10^{-70}B_\delta^{-400}\). The former verifies all
stopped primal, endpoint and nonaffinity inputs; the latter
closes the nonlinear source construction. This completes the
quantitative selection without using the old response threshold.

## 6. From the new source estimate to the complete theorem

The old construction and limit bridges require bounded primal paths,
cap/mesh-uniform subGaussian \(C,q^2,q^1\), and the endpoint margin
\(g_R(S)>1\). Sections 3--5 supply all three under (1).
The asymmetric comparison removes caps with error
\(C\exp(C(1+eR)S-cR^2)\to0\), producing the uncut strong feature
gradient path. Population symmetry gives \(f_i=y_i g\), and the
first hit of \(g=1\) is strictly before the affine endpoint.
The divergent scalar clock
\[
 t_{\rm physical}(s)=\int_0^s\frac{du}{2(1-g(u))}
\]
gives one global physical trajectory. For capped references use
their capped feature field, which need not be a gradient; their
first-hit clock uses only a bounded derivative.

The existing asymmetric physical estimate retains both actual
residuals and proves uniqueness against nonsymmetric competitors
and unique continuation from reached states. Width tends to
infinity at fixed cap and auxiliary mesh; deterministic Euler
estimates remove that mesh; then the cap is removed. For the
prescribed simultaneous raw GD, the extra reference error is
\(C_{R,T}n^{-2}\). The original small random finite readout is
retained.

The existing velocity proof first truncates product queries and
then removes the cap at fixed reference-velocity truncation,
before removing that truncation. Compactness of the uncut
velocity's continuous \(L^2\) time image supplies the needed
uniform tails. The path interpolation inequality and squared
speeds give the asserted path-space \(\mathcal W_2\) limits.
These bridge arguments have no new amplitude restriction once
the source estimate is supplied.

The affine regression margin transfers through the strong limits:
the activation regression error is at least \(e^2\eta_*/4>0\)
at all finite physical times. The old odd-family initial-motion
proof applies to every positive \(e\): full initial Gram support,
both reused-transpose covariances and returns, and sample
symmetry give the stated initial block/sample accelerations and
changing projected kernel. These claims require no additional
smallness depending on angle or physical horizon.

This verifies every conclusion of the original theorem under
the polynomial coefficient (17). In particular, the theorem
also continues to allow the Gaussian-unit-energy family
\((z+r\arctan z)/\sqrt{\mathbb E(G+r\arctan G)^2}\)
for \(0<r\le c_{\rm poly}\delta^{800}\), because its two
coefficients lie in the proved compact-gain rectangle.

The result establishes a polynomial sufficient relationship.
It does not establish a practical mixing coefficient or a
sharp exponent. Improving 800 towards 2 remains a separate
quantitative problem.
