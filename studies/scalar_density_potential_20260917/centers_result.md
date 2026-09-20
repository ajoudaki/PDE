# Class centers and singularities: what is proved unconditionally

Date: 2026-09-18. Continuation explicitly requested by the user. These are
internally checked study results, not promoted material.

The requested all-time fitting theorem from the specified initialization
remains open. No assumption on a future Gram eigenvalue or readout norm is
offered as its resolution. The new complete result is a genuine three-input,
actual-flow delay theorem that forces growth faster than every power in any
common-rate initial potential. The center formulation identifies the exact
initial-stall locus and a more informative geometric quantity than raw
center distance. Its dynamical coercivity is not proved.

## 1. Model and target

Use exactly the scalar closure, marks, initialization, probability loss, and
physical time specified in potential.md and three_input_result.md. In
particular phi=tanh, x_i in sqrt(2)S^1, w_0=g, c_0=0, and

\[
b_1=\frac{\phi(g_1)}{\sqrt{\nu+\eta}},\quad
b_2=\frac{\phi(\sqrt\nu Z)}{\sqrt{\tau+\eta}},\quad
M_0=\frac{\nu(1-\tau)}{\sqrt{(\nu+\eta)(\tau+\eta)}},
\]

with separate Gaussian populations, nu=E phi(G)^2,
tau=E phi(sqrt(nu)G)^2 and eta=1/4096. Thus ||b_1||_2,||b_2||_2<1.
The complete state is rho_1=Law(b_1,w), rho_2=Law(b_2,c), M. Every
assertion concerns this closure, not the full p=1 dictionary or neural net.

For binary labels (+,+,-), let p=(q/2,(1-q)/2,1/2), 0<q<1. Write

\[
a_i=\int b_1\phi(w^Tx_i/\sqrt2)d\rho_1,\quad
H_i=\phi(b_2Ma_i),\quad f_i=\int cH_i d\rho_2,
\quad d_i=\int b_2c\phi'(b_2Ma_i)d\rho_2.
\]

The exact gradient field and dissipation are equations (1) of
three_input_result.md. Input assumptions for the main target are three
pairwise nonparallel circle directions and exclusion of the explicit initial
stall locus below. A current-state potential may have declared data
singularities. Defining its singular set by unknown future nonconvergence,
or defining its value by integrating the unknown future trajectory, is not
an admissible construction.

## 2. Centers: the exact decomposition

For the upper hidden fields define

\[
H_+=qH_1+(1-q)H_2,\quad H_-=H_3,
\quad h=\frac{H_+-H_-}{2},\quad k=\frac{H_++H_-}{2},\quad s=H_1-H_2.
\]

The loss decomposes exactly as

\[
L=(\langle c,h\rangle-1)^2+\langle c,k\rangle^2
  +\frac{q(1-q)}2\langle c,s\rangle^2.
\tag{1}
\]

Here h is half the difference of the two class centers, k is their common
component, and s records within-positive-class variation. The genuine third
constraint is the last term. The identity follows by expanding the two
positive residuals around their weighted class average, then adding the
negative residual. The corresponding readout velocity is

\[
\dot c=2(1-\langle c,h\rangle)h
-2\langle c,k\rangle k-q(1-q)\langle c,s\rangle s.
\tag{2}
\]

The first-layer fields phi(w^Tx_i/sqrt2) admit the identical center/variance
decomposition. Their projections against b_1 are a_i. Taking a class mean
does not commute with the upper nonlinearity: H_+ is generally different
from phi(b_2M[qa_1+(1-q)a_2]). Replacing it by that latter expression
would change the dynamics and discard part of the third constraint.

### A geometric candidate that really mixes the three effects

Let B=span{k,s} in the upper population L2 space, let Pi_B be orthogonal
projection onto B, and define h_perp=h-Pi_B h. If h_perp!=0, the exact
minimum squared readout correction needed to fit all three labels with
the present hidden fields is

\[
\Phi_{\rm read}
=\|\Pi_Bc\|_2^2+
\frac{(1-\langle c,h_\perp\rangle)^2}{\|h_\perp\|_2^2}.
\tag{3}
\]

Indeed a fitting correction v must satisfy Pi_B(c+v)=0 and
<c+v,h>=1. Its B component is necessarily -Pi_B c. Its component parallel
to h_perp must be (1-<c,h_perp>)h_perp/||h_perp||^2. All remaining
components add squared norm without changing any constraint, proving (3).
Thus the relevant separation for readout fitting is the class contrast
remaining after removing common-center and within-class directions. Raw
||H_+-H_-|| alone is insufficient. At initialization (3) is
1/||h_perp||^2. If h_perp=0, no readout can fit all three labels while
these hidden fields remain fixed, although feature learning may repair this.

This is exactly the inverse-readout-Gram candidate in new coordinates;
its geometric interpretation is new, not a new proven Lyapunov function.
It satisfies L<=Phi_read when finite. For the minimizing correction,
r_i=-<v,H_i>, so
L<=||v||^2 sum_i p_i||H_i||^2<=||v||^2.

## 3. The exact initial-stall locus is not opposing input centers

At initialization dot w=dot M=0 and dot c=2h_0. Therefore

\[
\text{initial stall}\quad\Longleftrightarrow\quad h_0=0
\quad\Longleftrightarrow\quad H_{+,0}=H_{-,0}.
\tag{4}
\]

The centers coincide in upper activation space; they do not oppose there.
For three pairwise nonparallel circle inputs the complete data classification
is, with x_i/sqrt2 denoting the normalized coordinates,

\[
q=\frac12,\qquad
x_1/\sqrt2=(\delta,s),\quad x_2/\sqrt2=(-\delta,s),\quad
x_3/\sqrt2=(0,\sigma),
\tag{5}
\]

where 0<delta<1, s=+/-sqrt(1-delta^2), sigma=+/-1, allowing a swap of
the two positive indices. The proof in centers_counter.md uses the strictly
increasing odd Gaussian covariance a_i(0)=h_G(x_{i1}/sqrt2) and independence
of tanh(bz) at distinct nonzero absolute z. A zero combination must cancel
inside each absolute-value group. Pairwise nonparallelness and balanced
weights then force exactly (5). There are no omitted generic initial stalls.

The raw input class centers in (5) are sqrt2(0,s) and sqrt2(0,sigma).
They can point in either the same or opposite direction, and their distance
is nonzero. Neither opposing nor separated raw centers characterize (4).
Opposite-label antipodal inputs, with nonzero projection on the fixed probe,
are a learnable endpoint of the already proved pair family. Oddness is
compatible with those labels. Same-label antipodal inputs instead impose
inconsistent outputs and form an architectural boundary, considered next.

## 4. A genuine three-input delay theorem away from initial stalls

For a small positive epsilon, take

\[
x_1=\sqrt2(1,0),\quad
x_2=\sqrt2(-\cos\varepsilon,-\sin\varepsilon),\quad
x_3=\sqrt2(\sin\varepsilon,\cos\varepsilon),
\]
\[
(y_1,y_2,y_3)=(1,1,-1),\qquad
(p_1,p_2,p_3)=(3/8,1/8,1/2).
\tag{6}
\]

For every fixed 0<epsilon<pi/4 these are three distinct, pairwise
nonparallel inputs with balanced classes. They are even homogeneously
linearly separable: the vector (sin(epsilon/2),-cos(epsilon/2)) has signed
margins sin(epsilon/2),sin(epsilon/2),cos(3epsilon/2)>0. The three
initialized upper features are linearly independent, since their absolute
Gaussian projection coordinates are 1,cos(epsilon),sin(epsilon). In
particular an exact finite fit exists using the initial hidden fields and
a finite readout. No third constraint is redundant.

**Unconditional theorem.** There are explicit epsilon_0>0 and s_0>0,
independent of epsilon, such that for every 0<epsilon<epsilon_0 the
prescribed canonical trajectory satisfies

\[
-\dot L_\varepsilon(0)\ge s_0,
\qquad
L_\varepsilon(t)\ge\frac3{32}
\quad\text{for }0\le t\le(C\varepsilon)^{-2/3},
\quad C=(M_0+1)(\sqrt2+1).
\tag{7}
\]

**Proof of the delay.** The physical energy identity and L(0)=1 imply
||c_t||_2<=sqrt(t), |M_t|<=M_0+sqrt(t), and
||w_t||_2<=sqrt2+sqrt(t). Oddness and the Lipschitz bound |phi'|<=1 give

\[
|a_1+a_2|\le\varepsilon\|b_1\|_2\|w_t\|_2,
\qquad
|f_1+f_2|\le\|c_t\|_2\|b_2\|_2|M_t|\,|a_1+a_2|.
\]

Since the mark norms are less than one,

\[
|f_1+f_2|\le
\varepsilon\sqrt t(M_0+\sqrt t)(\sqrt2+\sqrt t).
\tag{8}
\]

Weighted Cauchy--Schwarz on the two positive errors yields

\[
L\ge\frac38(f_1-1)^2+\frac18(f_2-1)^2
\ge\frac3{32}(2-|f_1+f_2|)_+^2.
\tag{9}
\]

Choose epsilon<=1/C, so T=(Cepsilon)^(-2/3)>=1. The right side of (8)
is increasing in t and is at most Cepsilon T^(3/2)=1 at T. Equation
(9) proves the asserted floor for all t<=T.

To verify the nonzero initial descent, put A=M_0 nu/sqrt(nu+eta) and
R=||phi(b_2A)||_2>0. The initial velocity has the form
dot c_0=(3/4)phi(b_2A)-(1/4)phi(b_2B_epsilon)-phi(b_2D_epsilon),
where 0<D_epsilon<B_epsilon<A and
D_epsilon<=M_0 epsilon/sqrt(nu+eta). The first two terms have L2 norm
at least R/2. The third has norm at most
M_0 epsilon/sqrt(nu+eta). Thus for
epsilon<=R sqrt(nu+eta)/(4M_0), ||dot c_0||_2>=R/4 and s_0=R^2/16
works. This completes (7); the covariance estimates and initialization
independence are proved fully in centers_counter.md.

This theorem does not assert that any fixed positive-epsilon trajectory
fails to fit. It proves an actual arbitrarily long transient while the
initial gradient stays bounded away from zero and all constraints are
independent. The hidden-center difference at initialization likewise stays
bounded away from zero, since dot c_0=2h_0.

## 5. Required growth of a common-rate potential

Suppose a potential, finite on every dataset (6), is claimed to satisfy

\[
L_\varepsilon(t)\le\Phi_\varepsilon(S_t)^\alpha,
\qquad \Phi_\varepsilon(S_t)\le
e^{-\lambda t}\Phi_\varepsilon(S_0),
\]

with fixed alpha,lambda>0 independent of epsilon. Evaluating at the
time in (7) proves the necessary bound

\[
\Phi_\varepsilon(S_0)\ge
(3/32)^{1/\alpha}\exp[\lambda(C\varepsilon)^{-2/3}].
\tag{10}
\]

Thus finite-order poles in epsilon cannot suffice for a common positive
rate and this fixed power-law loss comparison. This is a real constraint
on the form of the potential, not a claim that singular potentials are
impossible. Calling this an essential singularity is only descriptive;
no analyticity of the hypothetical potential is assumed. The precise
assertion is the real growth lower bound (10).

There is an exact comparison with (3). Along (6), the initialized readout
Gram eigenvalues have orders 1, epsilon^2 and epsilon^4, and

\[
\Phi_{\rm read}(S_0)=\Theta(\varepsilon^{-4}).
\tag{10a}
\]

To verify this, write the initial features as H_A,-H_B,H_D with
A-B=k_2 epsilon^2+O(epsilon^4), D=k_1 epsilon+O(epsilon^3), k_1,k_2>0.
Then the normalized functions H_A,(H_A-H_B)/epsilon^2,H_D/epsilon
converge in L2 to H_A,k_2 b_2 phi'(b_2A),k_1 b_2. Their linear
independence follows from the Taylor coefficients of degrees 1,3,5.
The normalized Gram therefore stays bounded and positive definite.
The interpolation target in these coordinates is
(1,2epsilon^(-2),-epsilon^(-1)), proving (10a). The complete controlled
expansions and eigenvalue proof are centers_counter.md, Section 6.

Thus (3), or a fixed polynomial of inverse initial Gram quantities, cannot
support a common-rate exponential theorem with the fixed loss comparison
above. A faster-growing function could meet this necessary initial-size
constraint, but an increasing scalar transformation alone cannot repair a
positive time derivative of the underlying candidate.

Geometry-dependent rates remain possible. For example, any bound
L_epsilon(t)<=exp(-lambda_epsilon t) must have
lambda_epsilon<=log(32/3) C^(2/3)epsilon^(2/3). A delay prefactor can
also grow. Nor does (10) directly apply to an arbitrary non-power loss
comparison: if L<=F(Phi) with a fixed continuous increasing invertible F,
replace (3/32)^(1/alpha) by F^{-1}(3/32). If the comparison itself depends
on epsilon, that dependence must also be included rather than hidden.

## 6. Both hidden layers enter the unresolved estimate

Let P=diag(p_i), D=diag(d_i), and let K be the lower derivative Gram

\[
K_{ij}=\frac{x_i^Tx_j}{2}
\int b_1^2\phi'(w^Tx_i/\sqrt2)\phi'(w^Tx_j/\sqrt2)d\rho_1.
\]

Exact differentiation gives

\[
\dot a=-2MKDP r,\quad
\dot M=-2a^TDP r,\quad
\frac d{dt}(Ma)=-2(M^2K+aa^T)DP r.
\tag{11}
\]

Thus first-layer feature learning supplies M^2K and connector learning
supplies aa^T. Neither is absent from the attempted proof. In the weighted
sample coordinates the full output Gram is

\[
\Theta=P^{1/2}\{G+D(M^2K+aa^T)D\}P^{1/2},
\quad G_{ij}=\int H_iH_jd\rho_2.
\]

For R=P^(1/2)r one has dot R=-2Theta R. The full tangent correction
V=R^TTheta^{-1}R, where invertible, has exact derivative

\[
\dot V=-4L-R^T\Theta^{-1}\dot\Theta\Theta^{-1}R.
\tag{12}
\]

Class-center coordinates are an invertible change of these three residual
coordinates and do not remove the last term. centers_geometry.md derives
all of dot K, dot a, dot M, dot d and the induced center/scatter mixing.

The bounded diagnostic in centers_diagnostic_result.md found a positive
derivative of this full-metric candidate on a genuine triple, with the
precommitted grid and solver checks satisfied. This is empirical evidence
against that candidate, not a rigorous population counterexample and not
a counterexample to another possible state functional. The observed failure
includes the first-layer contribution; freezing it cannot explain the test.

One unconditional positive geometric constraint survives for every nonstalled
trajectory. Energy gives ||c_t||^2<=t(1-L_t), while weighted
Cauchy--Schwarz gives <c_t,h_t>>=1-sqrt(L_t). Therefore, for t>0,

\[
\|h_t\|_2^2\ge
\frac{1-\sqrt{L_t}}{t(1+\sqrt{L_t})}.
\tag{13}
\]

The hidden contrast cannot vanish faster than this bound, and its squared
norm has divergent time integral. The analogous bound on M^2 is (13)
divided by (E|b_1|)^2 E b_2^2. These statements do not control cancellation
among the three terms in (2). Finite positive-loss stationary states with
nonzero contrast can in fact be constructed; they are not asserted to be
reached from the prescribed initialization.

## 7. Exact remaining gap

The user correctly identifies singular geometry as a design constraint.
This pass establishes its exact initial-stall locus and a new required
growth scale near another obstruction, while retaining genuine three-input
feature learning. It does not establish a Lyapunov inequality on all
nonstalled canonical trajectories.

The unresolved step is a trajectory-specific control of signed readout and
center/scatter cancellation together with motion of M^2K+aa^T. A uniform
bound assumed on that expression, a future readout bound, or initial
invertibility does not resolve it. The negative results also do not prove
that every candidate potential fails, or that a fixed admissible generic
triple has infinite fitting time. No affirmative unconditional fitting
claim is made.
