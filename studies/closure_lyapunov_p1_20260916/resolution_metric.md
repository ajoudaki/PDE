# Metric route: a regular-endpoint theorem and its exact label limitation

2026-09-16. Scoped theoretical subagent report. **This does not resolve the
primary problem with labels exactly (+1,+1,-1).** It proves an unconditional
secondary result: outside a locally finite exceptional set of common positive
label amplitudes, the canonical orthogonal reference has a regular fitting
endpoint, and the original mixed current-state potential decays exponentially
on an open family of genuinely nonsymmetric triples near that reference.
There are such families arbitrarily close to amplitude one. The argument
does not establish that amplitude one itself is outside the exceptional set.

No numerical experiment, parameter alteration in an actual run, shared-source
edit, or external scientific input was used. The result concerns the exact
population p=1 closure, not identification with a trained-network limit.

## 1. Inputs, target and notation

Scientific inputs were the complete `docs/README.md`, `docs/NOTATION.md`,
`docs/observable_p1.md`; `docs/global_nonlinear.md` C.4.7.9 and the relevant
state, equation and existence material of C.4.7.10 B, C.1 and D.3; and the
complete same-study `three_coordinate_candidate.md`,
`perturbation_metric_template.md`, and `perturbation_metric_check.md`.
References inside those artifacts were not opened. Required process inputs
were the investigate-conjectures and solve-math-rigorously skills, including
the former's research-contract and adversarial-audit references. The
supervisor subsequently clarified that unit labels remain the primary target
and requested this immediate freeze with the amplitude limitation explicit.

Retain exactly the d=3 p=1 Gaussian marks, eta=1/4096 normalization, full
4-by-7 evolving M, actual transpose, initial (w,c,M)=(g,0,D), physical
population L2/Frobenius metric, and unhalved mean square loss of the frozen
candidate. Write X=(w,c,M), and let g_i=grad_X f(v_i). Every gradient below
includes the row, middle and readout blocks.

Absorb only fixed signs, not label magnitudes: put

    sigma=(1,1,-1), v_i=sigma_i u_i, a_i=sigma_i y_i.

Oddness gives f(u_i)-y_i=sigma_i[f(v_i)-a_i]. Thus the reference physical
inputs (e1,e2,-e3) and labels (A,A,-A) are equivalent to v_i=e_i and
a_i=A. All three probabilities remain 1/3. An open data neighborhood below
means the ordinary product topology of (S²)^3 times R³ for (v,a).

For any such data and current state define

    r_i=[f(v_i)-a_i]/sqrt(3), L=|r|²,
    F=(f(v1)+f(v2)+f(v3))/3, q=E_2 c²,
    K_ij=<g_i,g_j>/3,
    C_init=E_2[(H^2_0(v1)+H^2_0(v2)+H^2_0(v3))/3]².

The initialized H^2_0 uses g,D and the fixed Gaussian marks. In particular
C_init requires no fitted endpoint or future trajectory. The proposed
potential on C_init>0 is precisely

    V=1+C_init(1+q)/(C_init+F²),     Phi=L V.                 (1)

It is nonsingular, depends only on current state and initialized data,
and satisfies L<=Phi. Its formula uses no exceptional-set decision and
no tangent inverse. For all data, the exact identities are

    Xdot=-2 sum_i r_i g_i/sqrt(3),
    rdot=-2Kr,       Ldot=-4 r^T K r.                        (2)

## 2. Statement of the secondary positive result

There is a locally finite set E of positive real numbers such that, for
every A>0 outside E, there is an open neighborhood U_A of

    ((v1,v2,v3),(a1,a2,a3))=((e1,e2,e3),(A,A,A))

and a fixed lambda_A>0 for which every initialized closure with data in
U_A satisfies, at every physical time t>=0,

    Phi_dot<=-lambda_A Phi,
    L(t)<=Phi(t)<=2 L(0) exp(-lambda_A t).                   (3)

The full state converges in

    ||w-g||_2 + ||c||_infinity + ||M||_F,                    (4)

to a state fitting its own three targets. The potential is (1), with each
data set's own C_init. The same current equations restart from each reached
state. U_A contains nonorthogonal inputs and unequal label magnitudes,
with no permutation symmetry in either. This is a statement about a
nonempty open family, not a conditional assertion assuming K stays positive.

The set E has no accumulation in any compact interval of [0,infinity),
where zero is included by a harmless extension of the reference curve.
Consequently every neighborhood of A=1 contains amplitudes to which (3)
applies. Neither the size of U_A nor lambda_A is numerically evaluated.
This theorem gives no open neighborhood centered at the unit-label problem
unless 1 is proved not to belong to E. In particular, convergence as A tends
to one does not supply a uniform neighborhood or rate at one.

The proof first establishes analyticity in feature time and hence a discrete
set of potentially singular endpoints. It then uses finite-time continuity
and an explicit small-residual trapping argument. That second argument
needs positive definiteness only near the chosen reference endpoint.

## 3. Scalar reference for every positive common amplitude

Take v_i=e_i. The frozen candidate's permutation isometries fix the
initial state and preserve

    F(X)=(f(e1)+f(e2)+f(e3))/3.

Thus its autonomous feature-time curve X_s=grad F has equal predictions.
The curve and its initialization do not depend on the target A. The
candidate proves its global existence in

    B=L^infinity(Omega1;R³) x L^infinity(Omega2) x R^(4x7)

for the variables (w-g,c,M). On every bounded feature-time interval,

    ||c||_infinity<=s,
    ||M||op<=||D||op+s²/2,
    ||w-g||_infinity<=B1(||D||op s²/2+s⁴/8),                (5)

where B1 is the finite feature envelope. Put C0=C_init for the orthogonal
reference and k=||grad F||². The candidate's proof, which is independent
of target amplitude, gives

    F_s=k>=C0>0,     q<=F²/C0,
    Psi=(1+q)/(C0+F²),     Psi_s<=0.                        (6)

For clarity, its decisive calculation is q_s=2F, F_s=k,
F²<=q C<=q k, and c(s)=s U0+o(s), F(s)=C0 s+o(s),
q(s)=C0 s²+o(s²). Hence (q/F²)_s<=0 with initial limit 1/C0.
It follows that C>=C0 and k>=C0, and direct differentiation gives

    Psi_s=-2F[(q k-F²)+(k-C0)]/(C0+F²)²<=0.                (7)

For every A>0, F is strictly increasing from zero to infinity, so there
is exactly one s_A in (0,A/C0] with F(s_A)=A. The scalar equation

    sdot=2[A-F(s)],     s(0)=0

identifies the physical initialized reference curve with X(s(t)). Its
residual e=A-F satisfies edot=-2ke, remains strictly positive at finite
time, and tends to zero. Thus s(t) tends to s_A, and the reference tends
to X_A=X(s_A) in B. From (7), for all finite physical times,

    Phi_dot<=-4C0 Phi,    L<=Phi<=2L,    Phi(0)=2A².        (8)

This is just the complete frozen scalar proof with 1-F replaced by A-F;
it does not rescale the prescribed initialization or optimizer.

## 4. Analyticity despite the unbounded Gaussian row

Analyticity is used only for this fixed-input feature-time curve, in the
Banach space B of bounded increments in (5). It is not asserted for the
Nemytskii map on an unrestricted L2 ball.

Complexify B near a real state. For a real scalar x and sufficiently small
complex z, uniformly in x in R, the identity

    tanh(x+z)=[tanh x+tanh z]/[1+tanh x tanh z]

expresses tanh(x+z) as a convergent power series in z with a radius and
coefficient bounds independent of x. Indeed choose a complex disk on which
|tanh z|<rho<1 and expand the reciprocal denominator geometrically.
The expansion converges uniformly for all real x because |tanh x|<=1.
The differentiated tanh functions have the same property on a smaller
disk, either by termwise differentiation with a strictly smaller radius
or by their polynomial expressions in tanh.

Apply this identity pointwise to x=g dot e_i+(w-g) dot e_i. The fixed g is
unbounded but real, and the perturbation of w-g is bounded. Uniform power
series convergence therefore proves that lower activation and gate maps
are holomorphic in the complex L-infinity increment ball. Bounded feature
multiplication and population expectation are bounded linear operations.
The upper preactivation is b2^T M E_1[b1 H1], so its imaginary perturbation
is uniformly small on a sufficiently small complex B ball, since b1,b2
are bounded. The same tanh argument applies upstairs. Products with c
and multiplication by M or M^T preserve holomorphy. Thus the complete
feature-time vector field grad F is locally holomorphic on the complex
Banach space, with a finite local bound and Lipschitz constant.

Here is the needed time-analytic existence argument. Center a complex
B ball of radius R at the real reached state. Shrink it so the field is
bounded by B_* and Lipschitz with constant L_* on that ball. On a complex
time disk of radius h with h B_*<R and h L_*<1, apply Picard iteration
to holomorphic B-valued functions, using the path integral along the
straight segment from zero to time z. Its supnorm contraction estimate
is h L_* and its image remains in the ball. The iterates converge
uniformly. Their limit is holomorphic: on every smaller time disk, the
Cauchy coefficient integrals of the uniformly converging iterates
converge, their coefficient norms obey the common geometric Cauchy
bound, and their convergent power series represent the limit. The
integral equation identifies that holomorphic limit with the unique
real solution on the real interval. Repeating around every finite reached
state, using (5), proves real analyticity for every finite s>=0 and in
a small two-sided neighborhood of s=0.

The three full gradients g_i are likewise analytic B-valued expressions
(with row/readout components included in L2 by the probability-space
embedding). Their pairings have holomorphic extensions using bilinear
pairings, without complex conjugation; on the real curve these are the
ordinary physical Hilbert pairings. Therefore each K_ij(s) is real
analytic. This proves the analyticity needed below without treating an
unbounded Gaussian coordinate as a bounded Banach variable.

## 5. Locally finite exceptional amplitudes

Permutation invariance makes K(s) have a common diagonal and a common
off-diagonal entry. Its eigenvalue on n=(1,1,1)/sqrt(3) is k(s) from (6).
Its other two eigenvalues coincide and equal

    nu(s)=K_11(s)-K_12(s)=||g_1(s)-g_2(s)||²/6>=0.          (9)

At initialization only the readout gradient is nonzero. The candidate's
exact initialization gives

    H^2_0(e_i)=tanh[kappa(1) Z_i],

where the Z_i are independent symmetric nondegenerate upper marks and
kappa(1)>0. These fields are independent, centered and have the same
strictly positive variance h0. Hence K(0)=(h0/3) I and

    nu(0)=C0=h0/3>0.                                     (10)

By Section 4, nu is real analytic. A nonzero real analytic function has
isolated zeros: at a zero, its first nonzero Taylor coefficient isolates
that zero. If every Taylor coefficient vanished, its convergent series
would vanish on a neighborhood; the set of such neighborhoods extends
along the connected real interval by the same series argument, which
would contradict (10). Compactness now makes the number of zeros on
each finite closed s interval finite. There are no zeros near s=0 by
continuity and (10).

Define the proof object

    E={F(s): s>0 and nu(s)=0}.                             (11)

For any amplitude bound A_max, (6) implies that amplitudes at most A_max
come from s at most A_max/C0. There are finitely many zeros there, so E
is locally finite as claimed. For A outside E, K(X_A)>0 because its
eigenvalues are k(s_A)>=C0 and nu(s_A)>0. Neither (11) nor X_A is an
input to the closure or to the potential (1). They are used to prove
existence of the family and rate. This argument gives no sign certificate
for nu(s_1), and it does not show that nu has no intermediate zeros.

## 6. Data continuity in the appropriate norm

Use the hybrid Banach norm (4), denoted ||.||_H below, on the variables
(w-g,c,M). Supnorm continuity of lower fields under input changes would
be invalid because g is unbounded. The hybrid norm avoids that issue.
For unit inputs v,v' and rows w,w',

    ||tanh(w dot v)-tanh(w' dot v')||_2
        <=||w-w'||_2+||w'||_2 |v-v'|.                      (12)

The lower gates obey the same estimate with an extra factor 2. Bounded
b1 makes a(v) Lipschitz under (12). Bounded b2 then makes the upper
preactivation and H2 Lipschitz in upper L-infinity. On any H ball with
bounded c,M, predictions, backward coefficients and Q are Lipschitz;
Q is bounded in lower L-infinity. Multiplication of the lower gate
difference by that bounded Q handles the row-velocity difference in
L2. Subtracting the other bounded factors handles every remaining term.
Thus the vector field is locally Lipschitz jointly in state and the
finite data parameters, in H. The same calculations make K,F,q,V and
the derivative Phi_dot computed from the field continuous in H and data.

For labels in a fixed bounded neighborhood, energy and the bounded
features give the candidate's finite-time polynomial bounds, with the
label bound inserted. They also bound the H norm. The integral-map
contraction proves local existence in H, while these bounds prevent
finite-time escape. It agrees with the bounded-increment characteristic
solution by uniqueness. On each fixed [0,T], subtract the two integral
equations to obtain

    D(t)<=B epsilon t+L_* integral_0^t D(s) ds,

where epsilon is the data distance and D is the H distance between
solutions from the common initialization. Iterating this scalar integral
inequality gives D(t)<=B epsilon (exp(L_* t)-1)/L_*; for L_*=0 use
B epsilon t. Thus paths and all named continuous quantities converge
uniformly on [0,T] as data approach the reference. Equation (12) also
proves continuity of C_init, which stays positive near its C0>0 value.

## 7. Endpoint trapping and preservation of the mixed potential

Fix A outside E. By continuity at (X_A,reference data), choose a radius
R>0, a preliminary data neighborhood, and kappa>0 such that throughout
the H ball ||X-X_A||_H<R and that data neighborhood,

    K>=kappa I.                                         (13)

Shrink the ball and neighborhood if necessary. Boundedness of c,M there,
contraction of the normalized feature maps, and (2) give a finite constant
B such that

    ||Xdot||_H<=B sqrt(L).                               (14)

For example the readout L-infinity speed is at most 2 sqrt(L); the
middle speed is at most 2||c||_2 sqrt(L); and the lower L2 speed is at
most 2||M||op ||c||_2 sqrt(L). These estimates use the probability
normalization in Cauchy--Schwarz. The bounded derivative of V in this
ball, with C_init bounded below, supplies another finite constant B_V
such that

    |Vdot|<=B_V sqrt(L).                                 (15)

These are explicit consequences of the current equations, not assumptions
about the future perturbed path.

Choose delta>0 with

    B delta/(2 kappa)<R/4,     B_V delta<2 kappa.          (16)

Take T so late on the existing symmetric physical reference that
||X_ref(T)-X_A||_H<R/4 and sqrt(L_ref(T))<delta/2.
Section 6 permits a smaller open data neighborhood on which

    ||X(T)-X_A||_H<R/2,     sqrt(L(T))<delta.              (17)

While the perturbed path remains in the ball, (2) and (13) imply

    sqrt(L(t))<=sqrt(L(T)) exp[-2 kappa(t-T)].             (18)

Integrating (14) bounds its subsequent H displacement by
B sqrt(L(T))/(2 kappa)<R/4. Starting at distance less than R/2,
it therefore cannot reach radius R: a first finite exit would already
contradict the strict displacement bound. Global finite-time existence
was established in Section 6. Thus (13)--(18) hold for all t>=T.
Integrability of (14) proves convergence in H to a fitting state.

Now differentiate (1), retaining its complete moving factor:

    Phi_dot=V Ldot+L Vdot
       <=-4 kappa Phi+B_V L sqrt(L)
       <=[-4 kappa+B_V sqrt(L)] Phi
       <=-2 kappa Phi,                t>=T,              (19)

where V>=1 and (16)--(18) were used.

It remains to control the finite interval before T, without assuming
full-K positivity there. On the reference, (8) gives

    Phi_dot+2 C0 Phi<=-2 C0 Phi<0,      0<=t<=T.           (20)

The reference residual remains positive on this compact interval, so
the continuous right-hand side has a strictly negative maximum. The
joint continuity in Section 6 and uniform path comparison preserve the
inequality Phi_dot+2 C0 Phi<=0 for all nearby data, after one final
shrinking of the open neighborhood. Here C0 is the fixed reference
constant used only in the proof of a rate; C_init in (1) is still the
actual data's initialized coefficient. Equations (19)--(20) prove (3)
with lambda_A=min(2C0,2kappa). At initialization q=F=0, so V=2 and
Phi(0)=2L(0), completing every stated bound.

The saved laws converge in their ordinary Euclidean W2 metrics by
coupling equal frozen marks: lower transport cost is bounded by the
squared L2 row distance and upper cost by the squared readout L2
distance. Bounded features, Gaussian g and bounded reached increments
give the required finite second moments. This adds no network-limit
identification.

## 8. What the inverse metric condition does and does not add

For E_inv=r^T K^(-1)r, the template correctly gives

    E_inv_dot=-4L-r^T K^(-1) Kdot K^(-1)r.

The matrix inequality Kdot>=lambda K-4K² controls every tangent
direction, although the exact loss needs only r^T K r. In particular
an unexcited shrinking transverse direction can violate a fixed-lambda
matrix inequality while the actual common residual still decays
exponentially. For a purely algebraic illustration, take
K(t)=diag(1,exp(-t),exp(-t)) and r(t)=(exp(-2t),0,0).
Then rdot=-2Kr and L=exp(-4t), but the transverse entries of
Kdot-lambda K+4K² are eventually negative for every lambda>0.
This example concerns the general residual identity, not a claimed
reachable p=1 closure trajectory.

The theorem above avoids both that stronger differential condition and
an inverse defined at every intermediate time. Its unconditional new
input is regularity of almost every amplitude endpoint, proved in
Sections 4--5. Full endpoint regularity at the particular amplitude one
remains an unproved necessary premise for applying this route there.

The disjoint row-gradient blocks at orthogonal inputs give a useful but
incomplete diagnostic: the row Gram is diagonal, with entries
E_1[sech^4(w_i) Q_i²]/3. Each entry is positive whenever
M^T d_i is nonzero, because the lower initialized feature Gram is
positive definite and the gates are strictly positive at finite rows.
The inputs read here do not establish that nonvanishing at s_1. No
unproved sign or monotonicity of M^T d_i is used in this report.

## 9. Status and hostile checks

* Proved within the supplied exact closure: the amplitude exception set
  is locally finite; each nonexceptional amplitude has an open nonsymmetric
  family with an exponentially decaying mixed potential and fitting endpoint.
* Not proved: that amplitude one is nonexceptional, that the exceptional set
  is empty, or that any neighborhood/rate is uniform as amplitudes approach
  an exceptional value. The primary exact-unit-label problem remains open
  by this route.
* The potential has neither trajectory playback nor an endpoint constant.
  Reference endpoint and feature clock occur only in its existence proof.
* Input perturbations are controlled in H, not in a false Gaussian-row
  supnorm topology. Analyticity is proved separately in the fixed-input
  bounded-increment Banach space, not inferred from an L2 composition map.
* A full-rank initialized Gram alone is not extrapolated to the endpoint.
  Real analyticity gives isolated possible losses of rank, not their absence.
* The entire full matrix and its actual transpose keep evolving. No readout-only
  replacement, frozen kernel, finite-width theorem, or numerical evidence is
  substituted for this population statement.

This is a secondary scoped theorem with an explicit unresolved primary case,
not a declaration that the original unit-label research objective is solved.
