# Actual finite GF and raw GD: a fixed-proxy bridge

Author candidate, 2026-09-19. This unit assumes the completed raw-Euler
construction and uniform source cap in PERTURBATION_PROOF.md. It does not
assume uniform finite-width exponential moments. Its maintained inputs are
the complete fixed Gaussian-program and Hilbert calculus in
`docs/special_data_limits.md` III.F.1--11, `docs/global_nonlinear.md` A.1--4,
and the fixed-proxy method of C.4.7.5, with hypotheses checked below.

## 1. Exact input and conclusion

Fix the separately fixed m,d, binary labels and admitted directions of
THEOREM.md, and a finite T. Suppose the population raw Euler programs on every
mesh of maximal step h<=h_* converge strongly, uniformly in time, to the
unique C1 canonical raw flow theta. Suppose their fields at every node and
appended passive query obey the mesh-independent marginal bounds

  ||c||infty<=C_0, ||A||op<=M_0, ||w||2<=W_0,
  ||Q(u)1_(|Q(u)|>R)||2 <= B exp(-aR^2), R>=1,             (F1)

with a,B>0 independent of h and u. An affine raw Euler segment is covered by
appending its shorter final step. PERTURBATION_PROOF supplies exactly these
facts; the cap is on actual named response rows, not on a replacement action.
Every fixed program has its complete joint Gaussian interpretation, with
both orientations of the same initialized matrix and full first-row roots.

Then the actual finite GF and actual simultaneous raw GD, with initialized
stored variances (1,1/n,1/n^2), mobilities (n,1,n), and unhalved mean loss,
converge to theta in the declared observation senses through T. For raw GD,
the sufficient condition in this proof is simply eta_n->0. In particular it
includes eta_n sqrt(n)->0. Interpolate the stored raw GD parameters linearly
on their physical mesh and recompute nonlinear observations; predictions
converge in probability uniformly on [0,T] times the whole input sphere.
Each fixed finite admissible same-population tuple converges uniformly in
time in W2, with all its quadratic contractions. No growing-d/m assertion
and no uniform-in-time finite-width limit beyond this fixed T is intended.

## 2. Width-independent raw bounds for the actual algorithms

Use normalized row/readout RMS and ordinary middle Frobenius increment norm.
Let C_n=||c_n||infty. Since hidden activations have modulus at most one,
|f_n(u)-y|<=1+C_n for every training input. The exact readout GD step gives

  1+C_(n,k+1) <= (1+2eta_n)(1+C_(n,k)).                   (F2)

For GF the integral inequality gives 1+C_n(t)<=(1+C_n(0))exp(2t).
At a raw node, the middle and full-row velocity bounds are

  ||dot K_n||F <=2(1+C_n)C_n,
  ||dot w_n||F/sqrt(n) <=2(1+C_n)||A_n||op C_n.           (F3)

For the middle term each rank is delta h^T/n and its Frobenius norm is the
product of its two RMS norms. The row term is an average of Q phi'(z)u;
|u|=1 and ||Q||RMS<=||A_n||op C_n. These are literal raw-coordinate
calculations for both algorithms, without transformed gates or discrete
energy decrease.

With probability tending to one, simultaneously

  ||A_n(0)||op<=3, ||w_n(0)||F/sqrt(n)<=sqrt(d)+1,
  ||c_n(0)||infty<=1.                                   (F4)

The first two are the contained Gaussian matrix/row bounds in III.F and A.3;
the last follows from 2n exp(-n^2/2). For eta_n<=1, nodes and stages needed
to cover [0,T] lie within physical time T+1. Equations (F2)--(F3) give one
finite deterministic bound on c infinity, A operator norm, row RMS, and
all three velocity norms, uniformly in n. Call an enlargement V_T for sum
speed. Finite GF exists globally: the smooth finite vector field has these
bounds on each compact interval, gives Cauchy endpoints, and extends by
finite-dimensional local Picard iteration. GD needs no existence theorem.
Its raw affine interpolation obeys

  ||theta_n(t)-theta_n(floor(t/eta_n)eta_n)||sum<=V_T eta_n.
                                                               (F5)

All estimates keep the actual finite random readout. Its use is not replaced
by population zero initialization.

## 3. One fixed oracle program and its finite proxy

Fix h>0 and a finite population raw Euler mesh through T with maximal step
at most h. At this point its length, m,d and every requested passive list
are fixed independently of n. Expand every learned middle update into its
finite rank sum. In its coordinate expressions freeze each scalar residual,
pairing and response coefficient to its recursively computed population
value. Evaluate the resulting fixed Gaussian program on the actual initialized
finite first rows and matrix, with that matrix's actual transpose. Define
proxy parameters by the assigned raw increments from these oracle fields.
Start the proxy at the actual arrays, including the actual c_n(0) added to
the assigned readout increments. The population program starts at c=0.

The complete fixed-program theorem applies before h changes. Roots are a
fixed d-dimensional Gaussian tuple; every additional value product is a
bounded smooth gate times a named L2 field, of at most linear growth in
its coordinate arguments. A.1--2 justify such value instructions by their
contained clipping extension. At a fixed graph the uncut answers have finite
Gaussian/polynomial envelopes, so the extension's moment hypotheses hold.
Both action orientations, all rank-factor tuples and any fixed passive
observations are included in one finite union. Singular source covariances
are covered by the full initialized theorem; none is inverted without its
prescribed null-space treatment.

The finite proxy's recomputed fields differ from the assigned oracle fields
by o_P(1) in RMS at all its finitely many nodes. To see this induction
explicitly, scalar pairings converge by
|<a_n,b_n>-<a,b>|<=||a_n-a|| ||b_n||+||a|| ||b_n-b|| on an identified
same-carrier comparison, or by the identified joint second moments when
passing between carriers. Recomputed rank actions are finite sums of one
bounded-RMS factor times such a pairing error. Bounded Lipschitz gates
preserve RMS errors. For a bounded continuous gate times a named unbounded
field, subtract the field error, clip the fixed oracle field at R, pass n
to infinity, and remove R by its identified joint second-moment tail.
This step does not replace uniform integrability by a mere L2 bound.
Finally ||c_n(0)||RMS and ||c_n(0)||infty tend to zero in probability; the
same induction propagates this additive difference. The proxy starts at
the actual readout, while its limiting program has zero readout.

Let bar theta_(n,h) be the affine proxy parameter interpolant. Its assigned
velocity and recomputed raw field at the preceding proxy node differ by
epsilon_(n,h)=o_P(1), uniformly over those finitely many nodes. On events
whose probabilities tend to one its raw norms and sum speed are in a fixed
enlargement of the population bounds, independent of h. To justify the
middle norm, if K=sum_i a_i tensor b_i, then

  ||K||HS^2=sum_(i,j)<a_i,a_j><b_i,b_j>,                  (F6)

and the finite ranks a_i b_i^T/n have exactly this Frobenius formula with
normalized pairings. Thus there is no operator-norm subtraction between
different-width carriers. Proxy readout supremum also has the direct bound
||c_n(0)||infty+2T sup|r_oracle|, since every assigned upper activation is
bounded by one. This bounds it on the same deterministic enlargement.

For each fixed cutoff R, the proxy's recomputed Q fields inherit the
asymptotic RMS tail envelope

  max_(proxy nodes) m^-1 sum_a tau_R(bar Q_(n,h)(u_a))
       <= B_1 exp(-a_1 R^2)+o_P(1),                     (F7)

where B_1,a_1>0 are independent of h. Indeed
tau_R(X)<=2||(|X|-R/2)_+||2, the latter positive-part map is Lipschitz,
and joint W2 convergence identifies its norm. Its target norm is at most
tau_(R/2)(Q), bounded by (F1). Recomputed-field RMS errors add o_P(1).
Enlarge B_1 to cover small R. Only finitely many node/input fields are used
at a fixed h,R. This proves (F7), not a uniform finite-n moment theorem.

## 4. Comparison with actual GF or arbitrarily fine raw GD

Work on the common actual finite carrier. The one-reference gate estimate
is, for any bounded raw states on the preceding enlarged ball,

  ||F(theta)-F(bar theta)||sum
    <=C_T(1+R)||theta-bar theta||sum
        +C_T m^-1 sum_a tau_R(bar Q(u_a)).               (F8)

The readouts here have a common infinity bound. To derive (F8), subtract
lower and upper forwards by tanh Lipschitzness and bounded actions. Upper
backward subtraction costs at most
||c-bar c||2+2||bar c||infty||z2-bar z2||2. Subtract A*delta using the
middle HS difference and bounded adjoints. In the sole unbounded lower
product split the unchanged bar Q at R:

  ||[phi'(z1)-phi'(bar z1)]bar Q||2
       <=2R||z1-bar z1||2+2tau_R(bar Q).                 (F9)

Subtract residual and rank factors and average the data weights. Every
remaining factor is bounded on the raw ball. This gives (F8) with a finite
width-independent C_T. No Lipschitz estimate on unrestricted raw L2 balls
and no tail hypothesis on the actual finite trajectory is used.

Set E(t)=||theta_n(t)-bar theta_(n,h)(t)||sum. For GF, evaluate its field
at t and the proxy's field at its preceding h-node. For GD, evaluate its
field at its preceding actual eta_n-node and again compare to that same
proxy node. The node/interpolant distances cost at most V_T(h+eta_n), by
(F5) and the proxy speed bound; take eta_n=0 in the GF formula. Thus almost
everywhere (including in the upper-derivative interpretation at zero norms)

  D^+ E <= C_T(1+R)[E+V_T(h+eta_n)]
            +C_T B_1 exp(-a_1 R^2)+o_P(1), E(0)=0.      (F10)

The random remainder here is for fixed h,R, uniform over the finite proxy
nodes, from (F7) and epsilon_(n,h). No event uniform over growing transcripts
has been invoked. Integrating the scalar inequality gives

  sup_(t<=T) E(t) <= T exp(C_T(1+R)T)
       {C_T(1+R)V_T(h+eta_n)+C_T B_1 exp(-a_1R^2)+o_P(1)}.
                                                               (F11)

For any requested accuracy choose R large enough that the amplified Gaussian
tail is small: -a_1R^2+C_TTR tends to minus infinity. Next choose a fixed
proxy mesh h small enough, also inside the allowed h_*, so its amplified
error is small and its population interpolant is close to theta. Finally
send n to infinity; eta_n and the finitely many fixed-program probability
errors vanish. A union bound combines their events with (F4). This proves
arbitrarily small actual/proxy raw error in probability through T, followed
by the strong population proxy limit. A vanishing eta_n is sufficient;
there is no factor sqrt(n) in (F5) or (F10). The reference chart argument
in REFERENCE_PROOF.md proves a narrower sufficient condition by a different
comparison and is consistent with this stronger bridge.

This order of choices is essential. It does not claim that a Gaussian
program theorem applies to the actual growing GD transcript, nor that h
can be sent to zero inside an unproved width-uniform probability estimate.

## 5. Observations, the whole sphere and strict margins

Fix an admissible finite observation graph: full row and readout seeds,
initialized fields, bounded elementary gates/products, and either action
orientation on an admitted operand. On a common finite carrier the action
subtraction costs its bounded norm times operand RMS error plus the operand
RMS norm times the middle HS error. Bounded Lipschitz gates and bounded
products propagate such errors by finite induction. Frozen initial fields
are shared exactly. This controls every fixed typed joint word between the
actual and proxy paths by a vanishing function of their raw discrepancy.
For a named bounded continuous gate times an L2 field, use the truncation
argument of Section 3 on the reference/proxy field. Uniformity in time uses
its compact continuous L2 curve and a finite L2 net for its second-moment
tails. No arbitrary unbounded product is admitted.

For the proxy/population passage, a fixed finite time grid is appended to
the fixed program, including all initialized/current components in the same
tuple. Its joint empirical laws converge in Euclidean W2. The raw paths
have uniformly bounded sum speeds; along a fixed typed graph the same
bounded-gate/action induction gives a common RMS time-continuity modulus.
For the optional bounded-continuous-gate pushforwards use uniform continuity
on compact boxes and the preceding uniform tail truncation. A fine time
grid and the triangle inequality therefore extend this joint limit uniformly
in t. For k output coordinates on one population the same-neuron coupling
gives W2 squared at most the sum of their squared RMS errors. This is a
joint observation claim, not independently coupled marginal convergence.
Second moments and all declared quadratic contractions converge by the
two-factor Cauchy--Schwarz subtraction.

For predictions at every unit passive u, actual and proxy same-carrier
prediction subtraction is uniform in u on the raw ball. Their input modulus
is explicitly

  |f_n(t,u)-f_n(t,v)|
    <=||c_n(t)||RMS ||A_n(t)||op ||w_n(t)||RMS |u-v|.     (F12)

The high-probability bound above is independent of n and t. The population
analogue has the same finite bound. Choose a finite net of the compact
sphere (including the two-point sphere when d=1), apply the time-uniform
fixed-program prediction limit on that finite list, and refine the net.
Together with (F11) and the population mesh limit, this proves

  sup_(t<=T,u in S^(d-1)) |f_n(t,sqrt(d)u)-f(t,sqrt(d)u)|
                       ->0 in probability.             (F13)

The fixed dataset loss follows by its finite mean and bounded predictions.
For paired motion retain time-zero and current activations in the same
observation tuple; W2 gives convergence of their squared difference and
the training average. For nonaffinity also retain preactivations; variance
and covariance converge, and a positive limiting variance makes
Var(tanh Z)-Cov(Z,tanh Z)^2/Var(Z) continuous. Strict population margins
therefore imply finite-network margins with any fixed smaller constant,
with probability tending to one. A floor-time observation differs from
the interpolated prescribed time by a vanishing mesh-continuity error.

All conclusions concern every separately fixed admitted data configuration.
Nothing here couples neural width to closure order or claims empirical
exponential moments uniformly in finite width. Neural GF/GD capture and
the separate numerical-closure limit identify the same canonical flow by
their explicit construction, with their distinct limit orders preserved.
