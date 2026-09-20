# A nonstationary obstruction for the scalar population closure

Claim type: exact theorem about the prescribed population flow. Internal
checking and source versions are recorded in `push_validation.md`. This is
study material, not promoted material. The scalar dictionary is not the full
canonical p=1 dictionary.

## Statement

Keep the fixed scalar Gaussian probes and initialization below. Let three
pairwise nonparallel inputs on the normalized circle have labels (+1,+1,-1)
and probability weights

\[
p_1=q/2,\qquad p_2=(1-q)/2,\qquad p_3=1/2,
\qquad 0<q<1,\quad q\ne1/2.
\]

Rotate all three inputs through an angle theta, without rotating the fixed
probe. There is at least one fixed angle theta_* whose initialized trajectory
satisfies

\[
\dot L(0;\theta_*)<0,\qquad
\frac12\le L(t;\theta_*)<1\quad\text{for every }t>0.                 \tag{1}
\]

Thus this trajectory starts learning and can never fit. This is an actual
trajectory statement, with no boundedness, future coercivity, or limiting
kernel assumption. Every rotated dataset in this theorem has a finite fitting
state with the same frozen marks, as proved below.

An explicit, well-separated data family is the equilateral template

\[
x_i(\theta)=\sqrt2\left(\cos\left(\theta+\frac{2\pi(i-1)}3\right),
\sin\left(\theta+\frac{2\pi(i-1)}3\right)\right),\qquad
(p_1,p_2,p_3)=(3/8,1/8,1/2).                                  \tag{2}
\]

There is no duplicate or antipodal pair. The vector -x_3/sqrt(2) separates
the labels with normalized margins 1/2,1/2,1, respectively. All three fitting
constraints are independent in the sense of finite representability proved
below. The normalized positive and negative class centers at theta=0 are
(5/8,sqrt(3)/8) and (-1/2,-sqrt(3)/2). Their determinant is -sqrt(3)/4,
so these centers are neither parallel nor antiparallel at any rotation.
The theorem proves existence of a bad angle in this explicit family;
it does not supply a numerical angle or show that its initial readout Gram
is invertible.

## Exact model and scope

Write phi=tanh. On separate fixed probability spaces let g be a standard
two-dimensional Gaussian and Z a standard one-dimensional Gaussian. Set

\[
\nu=\mathbb E\phi(G)^2,\qquad
\tau=\mathbb E\phi(\sqrt\nu G)^2,\qquad \eta=1/4096,
\]
\[
b_1(g)=\frac{\phi(g_1)}{\sqrt{\nu+\eta}},\qquad
b_2(Z)=\frac{\phi(\sqrt\nu Z)}{\sqrt{\tau+\eta}},
\]
\[
w_0(g)=g,\qquad c_0(Z)=0,\qquad
M_0=\frac{\nu(1-\tau)}{\sqrt{(\nu+\eta)(\tau+\eta)}}>0.          \tag{3}
\]

The marks b_1,b_2 are frozen. The population measures are
rho_1=Law(b_1,w) and rho_2=Law(b_2,c); no Lebesgue density is assumed.
The following expectation form is equally an integral against those measures.
With v_i=x_i/sqrt(2), define

\[
a_i=\mathbb E_g[b_1\phi(w\cdot v_i)],\qquad
H_i=\phi(b_2Ma_i),\qquad f_i=\mathbb E_Z[cH_i],
\]
\[
d_i=\mathbb E_Z[b_2c\phi'(b_2Ma_i)],\qquad r_i=f_i-y_i.
\]

The exact scalar dynamics, in the physical population metric, are

\[
\begin{aligned}
\dot w&=-2\sum_i p_i r_i b_1 M d_i\phi'(w\cdot v_i)v_i,\\
\dot c&=-2\sum_i p_i r_iH_i,\\
\dot M&=-2\sum_i p_i r_i d_i a_i.
\end{aligned}                                                   \tag{4}
\]

The unhalved probability-weighted square loss obeys

\[
L=\sum_i p_i(f_i-y_i)^2,\qquad L(0)=1,
\qquad \dot L=-\|\dot w\|_2^2-\|\dot c\|_2^2-\dot M^2.          \tag{5}
\]

These are the scalar coefficients derived in `potential.md` from the
established coefficient and population equations. All subsequent arguments
use (3)--(5) directly. They do not change the initialization, the gradient
metric, the clock, or the number of scalar dictionary channels.

## Finite-time continuity and global existence

Use the Hilbert space

\[
\mathcal H=L^2_g(\mathbb R^2)\times L^2_Z\times\mathbb R
\]

for (w,c,M). The vector field in (4) is locally Lipschitz, uniformly in unit
input directions on every bounded state ball. Here are the estimates needed
both for existence and for parameter continuity. The marks are bounded;
phi,phi',phi'' are bounded; and phi,phi' are Lipschitz. For two states and
directions in a ball of radius R,

\[
|a_i-\widetilde a_i|
\le\|b_1\|_\infty\bigl(\|w-\widetilde w\|_2
                         +R|v_i-\widetilde v_i|\bigr).
\]

Also |a_i|<=E|b_1|, |f_i|<=||c||_2 and |d_i|<=||b_2||_infty||c||_2.
The preceding estimate bounds the differences of H_i in L-infinity and of
f_i,d_i in R by a constant depending on R times the state and input difference.
For the remaining functional factor use

\[
\|\phi'(w\cdot v_i)v_i-
\phi'(\widetilde w\cdot\widetilde v_i)\widetilde v_i\|_2
\le |v_i-\widetilde v_i|
+\|\phi''\|_\infty
 (\|w-\widetilde w\|_2+R|v_i-\widetilde v_i|).
\]

These estimates prove the asserted vector-field bound. Local solutions may
be obtained by contraction of the integral equation on a sufficiently short
interval. The loss identity then gives, for every local solution,

\[
\|S(t)-S_0\|_{\mathcal H}
\le\sqrt{t\int_0^t\|\dot S(s)\|_{\mathcal H}^2ds}\le\sqrt t.   \tag{6}
\]

On each finite horizon this stays in a common bounded ball, where the vector
field is bounded and Lipschitz. Successive local extensions therefore give a
unique solution through that horizon; no finite-time escape is possible.

For two rotations theta,psi and a fixed T, subtraction of the integral
equations on the common ball in (6) gives

\[
\|S(t;\theta)-S(t;\psi)\|_{\mathcal H}
\le C_T\int_0^t
 \bigl(\|S(s;\theta)-S(s;\psi)\|_{\mathcal H}+|\theta-\psi|\bigr)ds.
\]

Iteration of this scalar integral inequality, or its integrating-factor
proof, yields an upper bound (exp(C_T t)-1)|theta-psi|. Thus the state,
a_i and L are continuous in theta at each finite time. No estimate uniform
as T tends to infinity is required.

## Rotation forces an all-time loss floor

There are two steps: a zero scalar code exists at every finite time for some
rotation, and monotonic loss turns those time-dependent witnesses into one
fixed dataset.

When every input changes sign, substitution in (4) shows that the solution
changes by

\[
w(t;\theta+\pi)=w(t;\theta),\quad
M(t;\theta+\pi)=M(t;\theta),\quad
c(t;\theta+\pi)=-c(t;\theta).                                \tag{7}
\]

Indeed, oddness of phi and evenness of phi' give a_i -> -a_i, H_i -> -H_i,
f_i -> f_i, r_i -> r_i, and d_i -> -d_i. The two signs in the w equation
(from d_i,v_i) and in the M equation (from d_i,a_i) cancel, while the c
equation changes sign. The initialization is preserved because c_0=0.
Uniqueness proves (7). In particular,

\[
a_i(t;\theta+\pi)=-a_i(t;\theta),\qquad
L(t;\theta+\pi)=L(t;\theta).                                  \tag{8}
\]

Fix a finite time t. The continuous scalar function a_3(t;theta) takes
opposite values at antipodal angles. It therefore vanishes at some angle.
At that angle H_3=phi(0)=0 and f_3=0, so L>=p_3=1/2.

For each positive integer n, let

\[
E_n=\{\theta\in[0,2\pi]:L(n;\theta)\ge1/2\}.
\]

Each E_n is nonempty by the zero just proved, and closed by finite-time
continuity. Equation (5) gives E_(n+1) subset E_n. Nested nonempty closed
subsets of this compact interval have a common point: explicitly, select a
point in each E_n, extract a convergent subsequence, and use nesting and
closedness to put its limit in every fixed E_N. Call that point theta_*.
For any real t>=0, choose an integer n>=max(1,t); then

\[
L(t;\theta_*)\ge L(n;\theta_*)\ge1/2.                         \tag{9}
\]

Compactness was used only in data space. No state limit, bounded infinite
trajectory, limit exchange, or claim that a_3 stays zero was used.
The same proof for any chosen sample gives a fixed trajectory with loss
at least that sample's weight. The balanced negative sample gives (9).

## No rotation is initially stalled

For a unit direction with first coordinate rho, the initial lower feature is

\[
A(\rho)=\frac{\mathbb E[\phi(G_1)
\phi(\rho G_1+\sqrt{1-\rho^2}G_2)]}{\sqrt{\nu+\eta}}.
\]

This function is odd, continuous, and strictly increasing. To verify the last
claim, differentiate at -1<rho<1 and integrate by parts in G_1,G_2. The two
terms containing phi'' cancel, leaving

\[
A'(\rho)=\frac{\mathbb E[\phi'(G_1)
\phi'(\rho G_1+\sqrt{1-\rho^2}G_2)]}{\sqrt{\nu+\eta}}>0.        \tag{10}
\]

All derivatives are bounded and the Gaussian factors are integrable locally
in rho, justifying differentiation and integration by parts. Continuity at
the endpoints extends strict monotonicity to [-1,1].

For distinct positive numbers s_j, the functions b -> tanh(s_j b) are
linearly independent under the law of b_2. That law has positive density on
an interval about zero. An almost-sure zero linear combination is therefore
zero on that interval by continuity, and on the real line by real analyticity.
As b tends to positive infinity, its coefficients sum to zero. Subtract
this limit, multiply by exp(2s_min b), and use
tanh(sb)-1=-2/(exp(2sb)+1) to eliminate the smallest-scale coefficient.
Induction eliminates them all. Negative scales just change signs.

At initialization d_i=0, so dot w=dot M=0 and

\[
\dot c(0)=2[p_1\phi(b_2M_0a_1(0))+
             p_2\phi(b_2M_0a_2(0))-
             p_3\phi(b_2M_0a_3(0))].                         \tag{11}
\]

If (11) vanished, coefficients would have to cancel separately within groups
of the same nonzero |a_i(0)|. A singleton cannot cancel. Two nonzero terms
can cancel only with equal weights, impossible here: p_3 exceeds both other
weights and p_1 differs from p_2. If all three are nonzero they must share
one magnitude. Since p_3=p_1+p_2, cancellation then forces all three a_i
to have the same sign and hence the same value. Equation (10) would give
three distinct circle points with the same first coordinate, which is
impossible. Finally, three zero features would require three distinct circle
points with first coordinate zero, also impossible. These cases exhaust
the possibilities. Thus dot c(0) is nonzero for every rotation.

Equations (5) and (11) prove dot L(0)<0 and L(t)<1 for every t>0. There is
even a uniform initial decrease over this compact rotation family: the
continuous positive function ||dot c(0;theta)||_2^2 has a positive minimum
kappa. Joint finite-time continuity gives a delta>0 such that

\[
L(t;\theta)\le1-\kappa t/2\qquad
(0\le t\le\delta,\ \theta\in[0,2\pi]).                       \tag{12}
\]

Consequently the trajectory in (9) has a limit in
[1/2,1-kappa delta/2]. This is not an infinitesimally weak initial-gradient
counterexample.

## The scalar closure can fit every triple in this family

This representability argument preserves the frozen marks and M=M_0. At
w=g define bounded perturbation directions

\[
h_j(g)=b_1(g)\phi'(g\cdot v_j)v_j.
\]

Their Gram matrix K is positive definite for pairwise nonparallel v_j.
Indeed, a zero squared norm of a linear combination would imply, after
division by b_1 outside its null hyperplane,

\[
\sum_j\beta_j\phi'(g\cdot v_j)v_j=0
\]

almost everywhere. Continuity extends the identity to every g. Fix k and
take g=t z with z perpendicular to v_k. For j unequal to k, z dot v_j is
nonzero by nonparallelity, so phi'(t z dot v_j) tends to zero; the k-th
factor is phi'(0)=1. The limit yields beta_k v_k=0. Each beta_k is zero,
which proves positive definiteness.

Now consider w_z=g+sum_j z_j h_j. The map z -> (a_1,a_2,a_3) is continuously
differentiable near zero, with derivative K at zero. Its image contains a
neighborhood of the initial feature vector. One can see this directly:
for sufficiently small z, write a(z)=a(0)+Kz+R(z), where R has Lipschitz
constant smaller than 1/(2||K^{-1}||). For every sufficiently small target
shift u, the map z -> K^{-1}(u-R(z)) is a contraction of a small closed
ball into itself, and its fixed point satisfies a(z)=a(0)+u.

Choose u so that the resulting three a_i are nonzero with distinct absolute
values; the excluded coordinate and pair-equality hyperplanes have empty
interior. The tanh independence proved above makes

\[
G_{ij}=\mathbb E_Z[H_iH_j]
\]

positive definite. The finite L2 readout

\[
c=\sum_j (G^{-1}y)_j H_j
\]

satisfies E[cH_i]=y_i for all three inputs. The perturbation w_z-g is
bounded and M=M_0 is finite. Thus a finite fitting state exists with exactly
the same marks, and all three prescribed outputs are independent constraints.
This construction is an existence proof, not a claim that gradient flow
reaches that state.

## Consequences for potentials and singular data

For the bad dataset, no finite nonnegative state potential can satisfy both

\[
\Phi(S_t)\le e^{-\lambda t}\Phi(S_0),\qquad
L(t)\le\omega(\Phi(S_t)),\qquad
\lambda>0,\quad\omega(0)=\lim_{s\downarrow0}\omega(s)=0.        \tag{13}
\]

Indeed, (13) would force L(t) to zero, contradicting (9). The rate and the
comparison function may depend on the particular dataset. The obstruction
therefore applies even when no geometry-independent rate is requested, and
includes every fixed-power comparison L<=C Phi^alpha with C,alpha>0.

Allowing Phi=+infinity on excluded datasets is logically consistent. The
theorem says that excluding initial equilibria is insufficient: additional
singular configurations intersect every rotation family above, including
well-separated, linearly separable triples with uniform initial progress.
Their location is not classified here. Calling the unknown set of all failed
trajectories the excluded set would restate the problem, not solve it.

There is also an unconditional neighborhood consequence. For any target
0<ell<1/2 and finite T, continuity at theta_* gives a neighborhood in which
L(T;theta)>ell. Monotonicity then gives

\[
\tau_\ell(\theta):=\inf\{t:L(t;\theta)\le\ell\}>T.
\]

Since T is arbitrary, tau_ell tends to infinity as theta tends to theta_*,
in the extended sense. This asserts arbitrarily long delays nearby, without
assuming that the nearby trajectories eventually fit. If a potential on
nearby successful angles has a common lambda>0 and common comparison
L<=C Phi^alpha, then

\[
\Phi(S_0;\theta)>
(\ell/C)^{1/\alpha}e^{\lambda T}
\]

through that neighborhood. Such an initial potential must diverge toward
theta_*. A rate allowed to tend to zero can instead encode the delay.

The mechanism is a continuous sign choice for a scalar hidden code: an
antipodal rotation reverses the code, and a zero code forces a zero prediction.
Monotonic loss prevents all orientations from eventually crossing below the
mass of that sample. Both layers move in (4); ignoring lower-layer motion
is not part of the argument. For a vector-valued lower code the elementary
scalar intermediate-value step does not apply. No failure theorem for the
full p=1 dictionary, an adaptive probe, or a nonzero readout initialization
is asserted.

## What remains open

The existence proof does not locate theta_*, establish positive measure of
bad angles, or show failure when the initial readout Gram is positive
definite. For a fixed triple, singular initial Grams occur at finitely many
orientations (zero projection or equal absolute projections); this proof
does not exclude those orientations as all its witnesses. It therefore does
not refute an almost-everywhere theorem, or a theorem on a further explicitly
specified nondegenerate data class. An unconditional exponential fitting
theorem for a genuine successful three-input family is still open in this
study. The theorem proved here rules out the broader claim that removing
only initial stalls suffices.
