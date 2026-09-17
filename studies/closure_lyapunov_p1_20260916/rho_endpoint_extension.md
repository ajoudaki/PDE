# The full rho family: isolated degeneracy and the unit-amplitude gap

2026-09-16. Scoped independent theoretical continuation. No experiment.
Internal study result; nothing here is promoted to the established library.

Inputs: the permitted canonical state, initialization and gradient material in
`docs/README.md`, `docs/NOTATION.md`, `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3, and the complete
same-study `three_coordinate_candidate.md`, `resolution_open_family.md`,
`perturbation_orthogonal.md`, and `resolution_endpoint.md`. No other route,
review, study history, or numerical result was consulted. The
investigate-conjectures and solve-math-rigorously skills were applied.

**Result.** The isolated-rank-loss theorem extends to every member of the
original family, including rho=-1/2. Every possible rank loss has a strictly
positive quadratic coefficient. On compact geometry sets and bounded positive
label-amplitude ranges, the number of exceptional amplitudes has a uniform
finite bound. The exceptional geometry/amplitude pairs lie locally in finitely
many Lipschitz graphs. Every nonexceptional pair has an open neighborhood of
nonsymmetric input triples with all-time exponential fitting and strict decay
of the original mixed potential; rank losses earlier than the fitting endpoint
do not obstruct that conclusion.

This gives an unconditional all-rho theorem for all but finitely many amplitudes
in each bounded range. It does **not** give an almost-every-rho theorem at the
specified amplitude one. The fixed-amplitude slice of the exceptional graphs
has not been controlled. Beyond the two near-coincident branches already
accessible by continuity, this route does not prove the requested unit-amplitude
perturbation theorem. That distinction is an unresolved substantive gap.

## 1. Contract and orientation

Keep the exact dimension-three p=1 Gaussian populations, correlated lower
marks, eta=1/4096 normalization, full evolving 4-by-7 matrix and its actual
transpose, and population-L2/Frobenius gradient metric of the candidate.
The physical inputs are sqrt(3) times

\[
 (u_1,u_2,u_3)=(v_1,v_2,-v_3),\qquad
 v_1=(a,b,b),\quad v_2=(b,a,b),\quad v_3=(b,b,a),
\]
\[
 a^2+2b^2=1,\quad a\ne b,\quad
 \rho=v_i\cdot v_j=2ab+b^2\quad(i\ne j).
\]

The requested labels are (1,1,-1), all weights 1/3. The amplitude A used
below denotes the explicitly separated consequence with labels (A,A,-A).
Changing A is not presented as solving the unit-label problem.

Put d=a-b and m=a+2b. Direct expansion gives

\[
 d^2=1-\rho>0,\qquad m^2=1+2\rho,\qquad -1/2\le\rho<1.
\tag{1}
\]

Global input negation is an exact equivalence: replacing every v_i by -v_i
and the state (w,c,M) by (w,-c,M) preserves the predictions with absorbed
positive labels and every gradient norm. In the auxiliary equations, a_i and
d_i change sign, M_s is unchanged, and the two sign changes in Q_i v_i
leave w_s unchanged. The transformation fixes the prescribed initial state.
Thus, modulo this proved equivalence, take d>0 and parametrize all cases by
omega=m/d in R:

\[
 a(\omega)=\frac{\omega+2}{\sqrt{3(\omega^2+2)}},\qquad
 b(\omega)=\frac{\omega-1}{\sqrt{3(\omega^2+2)}},\qquad
 \rho(\omega)=\frac{\omega^2-1}{\omega^2+2}.
\tag{2}
\]

For -1/2<rho<1, omega has two signs. They are two orientations relative to
the fixed dictionary, not an identified single case. At rho=0, omega=1 is
(a,b)=(1,0), while omega=-1 is (a,b)=(1/3,-2/3). A rotation of the input Gram
does not prove equivalence of those initialized closures. Only the established
coordinate-permutation action and the explicit global-negation argument above
are used here. The two branches meet at omega=0, rho=-1/2. The coincident limit
rho=1 is excluded.

## 2. Exact symmetric curve for every rho

Absorb the third input sign, and write f_i=f(v_i). All quantities in this
section are evaluated on the prescribed auxiliary curve

\[
 X_s=\nabla F,\quad F=\tfrac13\sum_i f_i,\qquad
 c_s=U:=\tfrac13\sum_i H_i,
\]
\[
 M_s=\tfrac13\sum_i d_i a_i^T,\qquad
 w_s=\tfrac13\sum_i g_i Q_i v_i,
\tag{3}
\]
where a_i=E_1[b_1 tanh(w.v_i)], z_i=b_2^TMa_i, H_i=tanh z_i,
d_i=E_2[b_2 c sech^2(z_i)], Q_i=b_1^TM^Td_i, and
g_i=sech^2(w.v_i). This is a proof reparametrization of the same optimizer.

The candidate proves finite-s global existence, permutation symmetry,
initialized rank three, and

\[
 C=E_2 U^2\ge C_0>0,\quad F_s=\|\nabla F\|^2\ge C_0,
 \quad q:=E_2c^2\le F^2/C_0.
\tag{4}
\]

The inactive constant coordinates vanish by the exact oddness argument, so
use active notation b_1 in R6, b_2=Z/R_Z in R3, and M in R^(3-by-6).
Here Z_j=tanh Xi_j and R_Z=sqrt(tau+eta), exactly as initialized in the
candidate. The Z law has positive density on (-1,1)^3.

With P_parallel=11^T/3 and P_perp=I-P_parallel, permutation symmetry gives

\[
 A_l=a_{l\perp}P_\perp+a_{l\parallel}P_\parallel,
 \qquad M_l=m_{l\perp}P_\perp+m_{l\parallel}P_\parallel
 \quad(l=h,k),
\]
\[
 [d_1\ d_2\ d_3]=d_\perp P_\perp+d_\parallel P_\parallel.
\]

Here A_h,A_k are the two blocks of [a_1 a_2 a_3]. Define two-component
vectors a_perp,a_parallel,m_perp,m_parallel from the h,k coefficients and

\[
 \theta_\perp=m_\perp^Ta_\perp,\qquad
 \theta_\parallel=m_\parallel^Ta_\parallel,\qquad S=Z_1+Z_2+Z_3.
\]
Then, for all rho in (1),

\[
 z_i=\frac{\theta_\perp(Z_i-S/3)+\theta_\parallel S/3}{R_Z}.
\tag{5}
\]

The proof is exactly matrix multiplication in the two permutation blocks;
it requires no orthogonality of the inputs. The same upper-coordinate exchange
calculation as in the supplied orthogonal report gives d_perp=r(s)theta_perp,
where r is continuous and |r(s)|<=4s/R_Z^2. Consequently

\[
 (m_\perp)_s=\tfrac13r(s)a_\perp a_\perp^Tm_\perp.
\tag{6}
\]

Both initialized bands of m_perp are positive. Multiplying the inequality
(|m_perp|^2)' >= -(2/3)|r| |a_perp|^2 |m_perp|^2 by its exponential
integrating factor proves m_perp(s) is nonzero at every finite s. This
observation alone does not imply theta_perp is nonzero.

## 3. The transverse Gram for nonorthogonal inputs

Let G_ij=<grad f_i,grad f_j> be the unweighted full tangent Gram. It has
one parallel and two equal transverse eigenvalues by permutation symmetry.
The gradient blocks are H_i, d_i a_i^T, and g_i Q_i v_i. Therefore

\[
 \lambda_\perp=\tfrac12E_2(H_1-H_2)^2
 +\tfrac12\|d_1a_1^T-d_2a_2^T\|_F^2
 +\tfrac12E_1|g_1Q_1v_1-g_2Q_2v_2|^2,
\tag{7}
\]
\[
 \lambda_\parallel=3\|\nabla F\|^2\ge3C_0.
\tag{8}
\]

Indeed lambda_perp=||grad f_1-grad f_2||^2/2, and expansion of the mean
gradient gives (8). The original negative label conjugates G by
diag(1,1,-1), preserving its eigenvalues.

For real x,y,

\[
 |xv_1-yv_2|^2=x^2+y^2-2\rho xy
 \ge (1-|\rho|)(x^2+y^2).
\tag{9}
\]

The coefficient is positive throughout (1), including rho=-1/2. Thus it
is pairwise nonparallelism, not invertibility of the three-input Gram, that
is needed for the transverse argument.

For every finite s the exact criterion is

\[
 \lambda_\perp=0\quad\Longleftrightarrow\quad
 \theta_\perp=0\ \hbox{and}\ d_\parallel=0.
\tag{10}
\]

To prove the forward implication, the first term in (7), injectivity of tanh,
and positive upper density force theta_perp=0. Then z_i=kS for all i,
where k=theta_parallel/(3R_Z). Equation (4) forces k!=0, and hence
m_parallel!=0. Symmetry gives d_perp=0 and

\[
 d_i=(d_\parallel/3)\mathbf1,\qquad
 d_\parallel=R_Z^{-1}E_2[S c\,\operatorname{sech}^2(kS)].
\tag{11}
\]

Put V=b_1^TM^T1; then Q_i=d_parallel V/3. The active lower features are
linearly independent in L2: condition a vanishing linear combination of raw
h_j,k_j on G; the independent reverse noises give strictly positive
conditional variances, forcing all k_j coefficients to vanish, and independence
of h_j then removes the remaining coefficients. Normalization is invertible.
Since M^T1!=0, V is nonzero in L2. Equation (9), positivity of each gate,
and the last term of (7) force d_parallel=0. Conversely these two zero
conditions make every term in (7) vanish. This proves (10) for the entire
rho range, without assuming full input rank.

## 4. A forced crossing and a positive quadratic coefficient

Fix any finite rank-loss time s_0. All expressions not showing an argument in
this section are evaluated there. Equations (3), (10), and (11) give

\[
 d_i=Q_i=0,\quad M_s=w_s=(a_i)_s=(z_i)_s=0,
 \qquad c_s=H:=\tanh(kS),\quad k\ne0.
\tag{12}
\]

Differentiating d_i under its expectation consequently yields

\[
 (d_i)_s=\tfrac{\delta}{3}\mathbf1,\qquad
 \delta=(d_\parallel)_s
 =R_Z^{-1}E_2[S\tanh(kS)\operatorname{sech}^2(kS)]\ne0.
\tag{13}
\]

The sign of delta is the sign of k: the integrand has that strict sign
whenever S!=0, which has positive probability. All differentiations are
justified by bounded features and gates and the finite-s bounds on c,M,w-G.
The same bounds and dominated convergence give continuity of the derivatives.
Thus d_parallel is strictly monotone in a neighborhood of s_0. Each rank-loss
time is isolated, and there are finitely many on any compact s interval:
otherwise their closed zero set would have a nonisolated accumulation point.

More precisely define

\[
 J_\rho=\frac{\|a_1-a_2\|^2}{6}
 +\frac1{18}E_1\left[V^2|g_1v_1-g_2v_2|^2\right]>0.
\tag{14}
\]

The strict inequality follows from (9), positive gates, and V nonzero in L2.
This proof still applies to the linearly dependent input triple rho=-1/2.
For h=s-s_0, (12)--(13) give

\[
 d_i(s)=\delta h\mathbf1/3+o(h),\quad
 Q_i(s)=\delta hV/3+o(h),\quad H_1(s)-H_2(s)=o(h).
\]

The Q and upper remainders are in L-infinity, because their coefficients are
finite-dimensional differentiable curves and the dictionaries are bounded.
The lower gates are continuous in L-infinity along this fixed-data curve.
Substitution into (7) therefore gives the exact expansion

\[
 \lambda_\perp(s)=\delta^2 J_\rho(s-s_0)^2+o((s-s_0)^2).
\tag{15}
\]

Thus every possible event has both a nonzero crossing speed of d_parallel
and a positive quadratic loss of transverse rank. This is a restriction on
the actual initialized curve, beyond the ambient criterion (10).

## 5. Exceptional amplitudes and geometry: the quantifiers that are proved

For fixed omega, let s_A be the unique time with F(s_A)=A, A>0. Equation
(4) gives s_A<=A/C_0, and physical training with labels (A,A,-A) traverses
the same curve with ds/dt=2(A-F), tending to s_A. In particular all positive
amplitudes use a single auxiliary curve, not new initializations.

Equation (15) proves that only finitely many A in any bounded positive range
have a rank-deficient endpoint. The bound can be made uniform when omega
ranges over any compact set I and 0<A<=A_max.

Here are the needed uniformity details. On bounded feature-time intervals,
the candidate's bounds

\[
 \|c\|_\infty\le s,\quad \|M\|_{op}\le\|D\|_{op}+s^2/2,
 \quad\|w-G\|_\infty\le B_1(\|D\|_{op}s^2/2+s^4/8)
\]

are independent of the unit input directions. State and input subtraction
in the Hilbert metric gives local Lipschitz continuity uniformly on these
balls. In particular the only unbounded mark term obeys

\[
 \|\tanh(w\cdot v)-\tanh(\widetilde w\cdot\widetilde v)\|_2
 \le\|w-\widetilde w\|_2+\|\widetilde w\|_2|v-\widetilde v|.
\]

All subsequent coefficient and gradient differences use bounded dictionaries,
bounded gates, and finite matrices. The integrating-factor estimate for the
subtracted ODEs proves joint continuity and local Lipschitz dependence on
omega of X, F, theta_perp, and d_parallel. It also proves continuity of
partial_s d_parallel jointly in (s,omega), by differentiating its defining
expectation in s and using the same products. No analyticity in geometry is
assumed.

C_0(omega) is continuous and positive. Hence c_I=min_I C_0>0. All relevant
endpoints lie in 0<=s<=A_max/c_I. The rank-loss set in this compact rectangle
is closed. At each of its points (13) supplies a rectangle on which
partial_s d_parallel has one strict sign and is bounded away from zero.
A finite subcover exists. Each such rectangle contains at most one zero of
d_parallel on each fixed-omega vertical fiber. The number of covering
rectangles therefore bounds, uniformly, the number of rank-loss times and
exceptional amplitudes on each fiber.

There is also a precise graph statement. Near any rank-loss point choose
s_-<s_0<s_+ with opposite signs of d_parallel. These signs persist at nearby
omega. Strict monotonicity in s gives a unique zero s=sigma(omega) between
them. If the local lower bound on |partial_s d_parallel| is b>0 and the
Lipschitz constant in omega is L, subtraction and the mean-value inequality
give

\[
 |\sigma(\omega)-\sigma(\widetilde\omega)|
 \le (L/b)|\omega-\widetilde\omega|.
\]

Thus every nearby rank-loss endpoint lies on the Lipschitz amplitude graph

\[
 A=\mathcal A(\omega):=F(\sigma(\omega),\omega),
\tag{16}
\]
and in addition must satisfy theta_perp(sigma(omega),omega)=0. Compact
rectangles need only finitely many such graph charts. A Lipschitz graph has
two-dimensional measure zero: partition a bounded omega interval into pieces
of length h; the graph over each lies in a rectangle of width h and height
at most 2(L+1)h, whose total area tends to zero with h. A countable cover of
the whole parameter plane proves that exceptional (omega,A) pairs form a null
set. Their complement is open, by continuity and strict endpoint coercivity,
and dense, by the finite exceptional-amplitude result on every fixed fiber.

These are joint-parameter and amplitude-fiber statements. They imply no
measure-zero, discreteness, or empty-interior conclusion about the slice A=1.
For example a Lipschitz graph can coincide with A=1 on an entire interval.
One cannot upgrade (16) to an almost-every-rho unit-label theorem by slicing
a null set at a prescribed amplitude.

## 6. Endpoint coercivity suffices despite earlier rank losses

For completeness this section supplies the perturbation consequence of every
nonexceptional (omega,A); it does not assume all-time full Gram positivity of
the seed. Fix such a pair, and let X_* be its fitting endpoint. The normalized
Gram K=G/3 has K(X_*) positive definite. By local continuity there is a
Hilbert ball B(X_*,r) and an input neighborhood in which K>=k I for some k>0.

Choose finite physical time T so that the seed is within r/8 of X_* and its
loss satisfies sqrt(L_seed(T))<r sqrt(k)/16. Finite-time continuous dependence
gives a positive radius of perturbations of the signed unit inputs v_i for
which X(T) lies within r/4 of X_* and sqrt(L(T))<r sqrt(k)/8. For as long as
this perturbed path remains in the ball, let z_i=(f_i-A)/sqrt(3). Then

\[
 \mathcal L=|z|^2,\qquad
 \mathcal L'=-\|X'\|^2=-4z^TKz\le-4k\mathcal L,
\]
\[
 -\frac d{dt}\sqrt{\mathcal L}
 =\frac{\|X'\|^2}{2\sqrt{\mathcal L}}
 \ge\sqrt{k}\|X'\|.
\tag{17}
\]

If loss becomes zero, uniqueness makes the path stationary. Otherwise its
remaining length before any proposed exit is at most sqrt(L(T)/k)<r/8.
Together with the distance r/4 at entry this contradicts a first exit.
Consequently the path stays in the coercive ball forever, its loss decays
exponentially, and it has a fitting full-state limit. Its tail length satisfies
integral_t^infinity ||X'||<=sqrt(L(t)/k) for t>=T.

An exponential inequality can also start at time zero. The seed residual is
strictly positive before its endpoint, and on [0,T]
-L_seed'/L_seed=4||grad F||^2>=4C_0. This ratio is continuous near the
compact finite-time seed path, including any transverse-rank-loss points,
because its loss is bounded away from zero there. Reducing the input radius
gives -L'/L>=2C_0 on [0,T]. Combining with (17) yields

\[
 \mathcal L(t)\le A^2e^{-\lambda_L t},\qquad
 \lambda_L=\min(2C_0,4k)>0.
\tag{18}
\]

The original current-state mixed potential also persists. For the actual
perturbed data use U=(H_1+H_2+H_3)/3, F=E_2[cU], q=E_2c^2,
C_0=E_2U(0)^2, and

\[
 W=1+C_0\frac{1+q}{C_0+F^2},\qquad \Phi=\mathcal LW.
\tag{19}
\]

The seed proof gives Phi_seed'<=-4C_0 Phi_seed for amplitude A as well:
q<=F^2/C_0 and the derivative of W are unchanged, while its physical clock
is 2(A-F)>0. On the compact interval [0,T], Phi_seed is bounded away from
zero. Continuity of Phi and its full derivative therefore preserves
Phi'/Phi<=-2C_0 after reducing the input neighborhood.

For the tail, on the coercive ball C_0 stays bounded away from zero and
there are finite B,Lambda with ||grad W||<=B and ||K||op<=Lambda. The full
gradient, in block order (w,c,M), is

\[
 \nabla W=\frac{2C_0(0,c,0)}{C_0+F^2}
 -\frac{2C_0F(1+q)\nabla F}{(C_0+F^2)^2}.
\]

Thus, without assuming W is monotone on the perturbed path,

\[
 \Phi'\le-4k\Phi+2B\sqrt\Lambda\,\mathcal L^{3/2}.
\tag{20}
\]

Increase T so that the seed satisfies sqrt(L(T))<k/(B sqrt(Lambda)) with
strict margin, and then reduce the input radius once more. If B=0 no extra
restriction is needed. Loss monotonicity preserves this inequality in the
tail, so Phi'<=-2k Phi there. Consequently for some lambda_Phi>0,

\[
 \Phi'\le-\lambda_\Phi\Phi,\qquad
 \mathcal L\le\Phi,\qquad \Phi(0)=2A^2.
\tag{21}
\]

The data neighborhood is open in (S2)^3 and admits unequal angles without
permutation symmetry. All dynamics and the potential use only the current
saved state. The fitting endpoint and T enter the proof, not the autonomous
equations. Exponential residual decay, bounded coefficient norms in the ball,
and bounded dictionaries additionally give integrable L-infinity speeds for
w-G and c. Thus their limits exist in those norms, M converges in Frobenius
norm, and the common initialized-mark coupling proves W2 convergence of both
complete current/frozen population laws.

## 7. What remains at amplitude one

Let E_1 be the set of omega for which the unit-amplitude endpoint is singular.
The proved unit-amplitude good set R\E_1 is open. The near-coincident argument
of `resolution_open_family.md` supplies both tails |omega|>Omega for some
finite Omega. To verify the second tail, its seed parameter e can be taken
negative as well as positive: the positivity at e=0 and its continuity
estimates use no sign of e, and the input eigenvalues e,e,e+3 remain nonzero
for all sufficiently small nonzero e. Global negation then matches the
negative-omega branch in (2). This observation does not extend the theorem
into a new range bounded away from rho=1.

For a broader unit-amplitude conclusion, the unresolved statement is

\[
 F(s,\omega)=1,\quad \theta_\perp(s,\omega)=0
 \quad\Longrightarrow\quad d_\parallel(s,\omega)\ne0.
\tag{22}
\]

A concrete missing positivity estimate can be expressed using the *actual*
readout history, solely as a proof identity. At any candidate time in (22),
put k=theta_parallel(s)/(3R_Z), which is nonzero by (4). Since c(s)=integral_0^s
U(r)dr, boundedness permits Fubini and gives

\[
 d_\parallel(s)=\frac1{R_Z}\int_0^s
 E_2\left[S\,U(r,Z)\,\operatorname{sech}^2(kS)\right]dr.
\tag{23}
\]

Strict positivity of k times the integral in (23), at every such candidate
time, would settle (22). The supplied noncollapse estimate controls
E U(r)^2 and <c,U>, not the sign of these weighted cross-time correlations.
No sign for them has been proved here. Nonvanishing of m_perp in (6) also
does not control its projection theta_perp.

Alternatively, the graph result in (16) would give almost-every geometry at
amplitude one if the level sets {omega: A(omega)=1, theta_perp(sigma(omega),omega)=0}
were shown null. Local Lipschitz dependence and a nonzero derivative in feature
time do not prove that assertion. Nor has analyticity of this population flow
in the geometry parameter been established: the frozen Gaussian enters
tanh(G.v(omega)), whose geometry derivatives are not uniformly bounded in
the characteristic essential-supremum norm. Finite-dimensional analytic ODE
arguments cannot be imported without repairing this issue.

| Claim | Status | Scope |
|---|---|---|
| Rank-loss criterion (10) and nonzero crossing (13) | Proved here | Every rho in [-1/2,1), both orientations |
| Positive quadratic coefficient (15) | Proved here | Every finite rank-loss event on the initialized curve |
| Uniform finite exceptional-amplitude count | Proved here | Compact orientation sets, bounded positive amplitudes |
| Exceptional pairs lie in locally finite Lipschitz graph charts | Proved here | Joint geometry/amplitude space |
| Nonsymmetric perturbation theorem (18),(21) | Proved here | Every nonexceptional geometry/amplitude pair |
| Almost-every or every rho at amplitude one | Open | Cannot be inferred by taking a specified slice of the joint null set |
| New unit-amplitude range away from near coincidence | Not obtained | No unsupported rank or sign inference is substituted |

These results extend the supplied orthogonal isolated-event theorem; they do
not supersede its warning about a specified amplitude. No new claim of network
identification, order accuracy, universal fitting, or rotation invariance is
made.
