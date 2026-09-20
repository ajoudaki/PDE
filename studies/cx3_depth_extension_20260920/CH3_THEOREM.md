# C-X3-H3: nonlinear observable computation at every fixed tanh depth

Author theorem and proof assembly, 2026-09-20. This completes the mathematical
C-H3 branch of CONTRACT §§2,3,5 by the three linked proof units below, subject
to the internal check disposition recorded in README. Numerical operation and
checks have their own evidence; no promotion or C-H4 completion is asserted.

## 1. The theorem

Fix separately a hidden depth L>=3 and use tanh in all L hidden layers, no
biases, normalized inputs u=x/sqrt(d), Gaussian stored variances 1 in the first
matrix, 1/n in every hidden matrix and 1/n^2 in the readout. The output is
c^T H_L/n and the block mobilities are (n,1,...,1,n). The loss is the unhalved
probability-weighted squared error. Every block trains; the actual finite
random readout is retained. Population c(0)=0.

There is T_L>0, depending on L and the fixed label/initialization bounds,
chosen before width, sampling and numerical limits, with these properties.

1. Every Borel probability law on sqrt(2)S1 x [-1,1] has a canonical strong
   C1 raw population flow on [0,T_L], unique on its initialized carrier and
   uniquely restartable from every reached state under the same law.
   The interval is independent of sample count, atom masses, covariance
   rank and the particular law. It retains the full first row, every
   initialized action and its actual adjoint, and HS learned increments.
2. The same result holds for every separately fixed d,m and arbitrary
   normalized finite input list with bounded labels and positive probability
   weights. No exclusion of coincident, parallel, antiparallel or singular-Gram
   data is needed for existence. The proof in fact gives each fixed dimension's
   full compact-sphere Borel-law completion. No growing-dimension claim is made.
3. For finite data satisfying |u_a.u_b|<1 for distinct indices, all labels
   nonzero and all weights positive, there is a possibly smaller T_act>0
   depending on this fixed data and L. At EVERY input and EVERY hidden layer,
   paired activation and preactivation displacement have nonzero order-t^2
   coefficients, RMS speed has order t, and squared displacement has order
   t^4. Each visited marginal has positive preactivation/activation variance
   and positive best-affine-fit activation error on [0,T_act]. There is also
   a fixed nonempty open Borel-law subfamily with positive paired motion in
   all layers, including original-family nonatomic arc laws, as proved below.
4. Actual finite GF and simultaneous raw GD for EVERY deterministic eta_n->0
   converge on the asserted local interval. Predictions converge uniformly
   in time and input. Fixed typed same-layer observations converge with their
   second moments, including initial/current paired activations, RMS motion
   and risk. For fixed finite datasets the joint hidden paths converge in W2
   for the uniform path norm, and kernels/integrated squared speeds converge.
   Circle laws can converge deterministically or by independent iid sampling,
   jointly with width and step, without relative growth restrictions.
5. One determining current observable hierarchy has autonomous finite-feature
   closures converging to that SAME target. Its initializer retains distinct
   identities and both orientations of all L-1 matrices. Its numerical state
   contains actual finite arrays for all L complete joint populations and
   all evolving and initial feature matrices. It has no neural width and no
   accumulating time history, and restarts from its own complete current state.
6. Numerical refinement converges uniformly in time and whole input, and
   preserves all the specified paired/joint observations and second moments.
   With outermost limits first, the order is

       lim_N lim_(epsilon down to 0) lim_Q lim_P lim_m lim_(h down to 0) lim_p.

   Here N is hierarchy order, epsilon source regularization, Q initializer
   integration, P complete population replay, m represented-input quadrature,
   h closure time step and p arithmetic precision. Omit m for exactly
   represented finite data. This is qualitative iterated convergence, with
   finite cost accounting; no rate, arbitrary diagonal, tolerance selector or
   per-run true-error certificate is claimed.

At L=2 the maintained C-H3 theorem, including its literal interval 1/200,
remains available unchanged. New local constants at greater depths do not
rewrite that theorem. C-H4's substantial-training interval is a separate target.

## 2. Proof assembly and exact dependencies

The complete arguments are:

- [CH3_LOCAL_PROOF.md](CH3_LOCAL_PROOF.md), §§2–9: raw strong flow, common
  local time, passive-query tails, law completion, uniqueness/restart, actual
  GF/GD and observations.
- [CH3_ACTIVITY_PROOF.md](CH3_ACTIVITY_PROOF.md), §§2–7: positive forward and
  backward Grams, actual adaptive Gaussian conditioning, every-layer
  noncancellation induction, onset expansions and nonaffinity.
- [CH3_HIERARCHY_PROOF.md](CH3_HIERARCHY_PROOF.md), §§2–8: determining word
  language, finite law/array equations, global fixed-order existence,
  conditional order comparison, all inner numerical limits and finite costs.

The local theorem discharges the hierarchy theorem's target hypotheses:
strong C1 flow in full-row/HS state, generated-space invariance, bounded raw
and action norms, bounded readout, and uniform individual Gaussian tails
of every passive backward field. The hierarchy's conditional comparison is
therefore UNCONDITIONAL on this local interval. Its longer-horizon application
remains conditional. The activity theorem applies to this same flow because
its restriction to any finite training list is the unique maintained C.1
flow on the common interval. No different model or readout limit is substituted.

For the finite-data assertion with a general fixed label bound, put
Y=max(1,max_a|y_a|). The hierarchy proof writes its energy bounds for Y=1;
the extension needed here is immediate from its unchanged gradient identity:

    loss_N(t)+integral_0^t ||theta_N'(s)||metric^2 ds <= Y^2,
    ||c_N(t)||infinity <= 2Yt,
    ||w_N(t)-g||2^2+||c_N(t)||2^2
              +sum_ell ||M_ell(t)-D_ell||F^2 <= Y^2 t,
    ||M_ell(t)||op, ||A_(ell,N)(t)||op <= 10+Y sqrt(t).

The readout estimate uses integral|r|dmu<=sqrt(loss_N)<=Y; the displacement
estimate is Cauchy--Schwarz on the integrated metric velocity. These bounds
replace hierarchy (9) and its inner-limit energy bounds. Fixed-order drift
and stability constants may depend on Y, and remain finite; consequently
fixed-order continuation and all its numerical limits follow unchanged.
The outer comparison uses the local theorem's already Y-dependent time and
tail constants. No data normalization, time rescaling, or change to the
physical equations is made. Thus clauses 2,5,6 cover arbitrary fixed bounded
finite labels, not only the hierarchy proof's displayed unit-label case.

All proof units use only this study and maintained material. The supervisor
checked the actual calculations against complete C.1–C.3, C-H3 A–C, the
relevant C-H1/H2 units, the Gaussian conditioning/source/common-space/raw-metric
and chain-rule units III.F.1–10, and A.1–A.4. These checks do not constitute
promotion or a new audit of every unrelated transitive theorem in the book.

Three estimates explain why the arguments close.

First, C.2's causal response induction gives, on a depth-dependent common
positive interval, tails C exp(-cR^2) for each backward query, uniformly in
finite law and time mesh. Adding a passive input with positive mass then
sending its mass to zero extends these bounds to every passive query.
Subtracting two raw vector fields gives

    ||F_mu(theta)-F_nu(theta_bar)||sum
      <= C(1+R)(||theta-theta_bar||sum+W1(mu,nu))+C exp(-cR^2).

At every fixed depth the cutoff enters LINEARLY. Each new gate error uses
the already controlled forward error; propagating a backward error multiplies
it only by bounded actions and gates. Hence exp(CRT_L-cR^2)->0. Euler paths
are Cauchy in full-row L2 and middle HS norms; this proves completion and
one-reference uniqueness, including against competitors with no tail premise.
The same estimate against a fixed finite-program proxy proves the raw-GD
bridge for arbitrary vanishing eta_n. The Gaussian theorem is never applied
directly to a transcript whose length grows with n.

Second, for finite nondegenerate data write p_a=omega_a y_a,
d_(ell,a)=sech^2(Z_(ell,a)(0)), and let E_(ell,a) denote the activation
coefficient in

    H_ell(t,u_a)-H_ell(0,u_a)=2t^2 E_(ell,a)+o_L2(t^2).

Let rho_(ell,a) be the L2 distance of E_(ell,a) from the span of that
layer's initial activation tuple. If D_2 is the positive backward-source
Gram for this depth, Gaussian conditioning gives

    rho_(1,a)^2 >= lambda_min(D_2) p_a^2 E[d_(1,a)^4] > 0,
    rho_(ell,a)^2 >= rho_(ell-1,a)^2 E[d_(ell,a)^2] > 0.

For the second line, the fresh forward reuse of edge ell has conditional
innovation rho_(ell-1,a) gamma after all previous forward AND reverse
calls to that edge. It is independent of the preceding receiving-population
tuple, which includes its upper-edge backward fields. Every other acceleration
term is measurable in that tuple, so cannot cancel this variance. Innovations
within a batch may be correlated. This proves each input's motion at every
layer, not merely positive aggregate hidden energy.

Third, ridge-normalized initialized features give positive contractions
Q_(ell,N)->I strongly. The two compressed orientations converge strongly on
the compact exact forward/backward field families, and

    sup_t ||Q_(ell,N) K_ell'(t) Q_(ell-1,N)-K_ell'(t)||HS -> 0.

Call the sum of these omitted sources epsilon_N. Energy bounds the endpoint
and coefficient displacements by Y sqrt(T), so all compressed action norms
are bounded independently of N. The same one-reference cutoff argument gives

    sup_(t<=T_L) e_N(t)
      <= C T_L exp(C(1+R)T_L)
                       [(1+R)epsilon_N+C0 exp(-a0 R^2)].

Take N->infinity at fixed R, then R->infinity. This supplies the required
source estimate and propagation estimate. No Gaussian tails of projected
or numerical solutions, finite-core sufficiency, or hidden target-state reset
is assumed. Fixed-order numerical limits then use bounded feature marks and
the actual finite-dimensional gradient metric, with separate precision,
time, input, population, initializer and covariance limits.

## 3. The open Borel family with genuine activity

The finite-data activity proof alone does not claim activity for every Borel
law: label cancellation can make the population stationary. Here is the
additional open-family bridge required by the contract.

In normalized coordinates choose

    mu_0 = (1/2) delta_(e1,+1)+(1/2) delta_((3/5,4/5),-1).

This is the original ArcLaw with both intervals degenerate at zero. Its two
directions are pairwise nonparallel, so the preceding activity theorem applies.
Choose one t_a in (0,min(T_L,T_act)] and define

    J_ell(mu,t_a)=integral ||H_ell^mu(t_a,u)-H_ell^mu(0,u)||2^2 dmu(u,y).

All L numbers J_ell(mu_0,t_a) are positive. The initialization is the same
law-independent carrier. Uniform-in-u L2 continuity of the trained hidden
fields under W1 changes in mu gives convergence of the paired integrand,
uniformly in u, because hidden values are bounded by one. Changing the law
of integration contributes a vanishing error: the fixed reference integrand
is continuous on the compact data domain and bounded by four. Thus each
J_ell is W1-continuous at mu_0. There is delta>0 for which

    J_ell(mu,t_a) >= J_ell(mu_0,t_a)/2 > 0

for every ell and every Borel mu with W1(mu,mu_0)<delta.

Nonaffinity can be kept on an early interval simultaneously. At initialization
every unit-direction marginal in layer ell is a nondegenerate Gaussian with
the same positive variance q_(ell-1), where q_0=1 and
q_ell=E tanh^2(sqrt(q_(ell-1))G). Its best-affine-fit error is positive.
The variance and affine-error formula are continuous under L2 convergence
while the variance stays positive. Continuity on compact time x sphere at
the reference therefore supplies a positive early interval with uniform
positive variances/errors in all L layers. Shrink t_a to that interval.
The law-continuity theorem then preserves these bounds on a smaller open
W1 neighborhood of mu_0. This uses finitely many layers and compact input
directions, not a minimum of unconstrained infinitely many positive numbers.

For any sufficiently small rational epsilon>0, the original ArcLaw with
p=1/2, a=c=-epsilon, b=d=epsilon lies in that neighborhood: couple each arc
to its central atom and use |U(s)-U(0)|<=2|s|. Its law has no atoms. Hence
the required open nonlazy family contains represented nonatomic members,
as well as genuinely nonorthogonal pairs. It is fixed before all numerical
and width limits. The larger original ArcLaw family still has the existence
and numerical convergence conclusions; universal strict motion is not inferred
from this particular open-family argument.

## 4. Implementation and check boundary

[depth_initialization.py](depth_initialization.py) implements an exhaustive
typed initialized-word grammar, Chebyshev enrichment, one finite joint source
program with matrix-specific orientation groups, positive source regularization,
ridge normalization, and separate population replay. Its derivative traversal
retains response paths through neighboring matrices. Its outputs discard the
source transcript before evolution.

[depth_closure.py](depth_closure.py) implements all L finite populations,
L-1 evolving coefficient matrices and their actual transposes, generic finite
unit-sphere data, simultaneous Heun, whole-input evaluation, every-layer paired
observations, and exact working-scalar restart. The arithmetic backend includes
the maintained finite rational algorithms for the precision limit. Tests and
operation are specified by [CH3_VALIDATION_PLAN.md](CH3_VALIDATION_PLAN.md).

The theorem is local. It neither establishes substantial training nor extends
C-H4's perturbation-through-fitting result. Passing deterministic finite
checks is evidence about the implementation, not a substitute for the proofs
or an error certificate for the tested numerical resolutions.
