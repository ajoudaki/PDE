# Machinery Candidates and Kill Gates

## Executive assessment

Three clean-slate designs independently converged on the same broad architecture:

1. retain a finite list of current-time vector/operator **types**;
2. expand each type in an infinite graded Gaussian-response or rooted-diagram space;
3. encode a source matrix and its transpose as two orientations of one generator;
4. normal-order every adaptive source query into a fresh/divergence part plus exact response contractions;
5. prove a weighted tail estimate so finite truncations approximate the autonomous completed flow.

This agreement is meaningful, but it does not prove constructability.  All three designs move the hard problem to a norm or graph-enumeration theorem.  The primary decision is therefore not which diagram notation to use; it is which proposed **master estimate** can actually be proved on the complete two-hidden-layer arctangent flow.

## 1. Common exact atom

Let `Gamma_ij=n^{-1/2}g_ij` and let `D_ij` differentiate with respect to the standardized Gaussian `g_ij`.  For an arbitrary smooth adaptive vector `X(g)`, Gaussian divergence gives the exact identity

\[
(\Gamma X)_i
=\delta\left(n^{-1/2}\sum_jX_j e_{ij}\right)
+\frac1{\sqrt n}\sum_jD_{ij}X_j.
\tag{1}
\]

Likewise,

\[
(\Gamma^*Y)_j
=\delta\left(n^{-1/2}\sum_iY_i e_{ij}\right)
+\frac1{\sqrt n}\sum_iD_{ij}Y_i.
\tag{2}
\]

The same derivative coordinates occur in (1) and (2), so exact transpose reuse is automatic.  Equations (1)--(2) are the dynamic analogue of MFP's fresh-field plus response rule.  They are exact, but they are not yet a closure theorem: the divergence and derivative contractions require quantitative bounds.

## 2. Candidate A: rooted-traffic Koopman calculus

### State and recursion

A typed graph algebra contains current vectors, current learned morphisms, immutable Gaussian edges, adjoint orientations, normalized contractions, rank-one vertices, and gate vertices.  The Liouville derivation

\[
\mathscr LQ=DQ[Y]F(Y)
\]

is a finite local rewrite rule.  Every fixed `L^kQ(Y(0))` is a finite static Gaussian program and can be evaluated by MFP/Wick--Stein peeling.

For arctangent, the differential chain can be finitely presented using

\[
R_\pm(z)=(z\pm i)^{-1},
\qquad
\dot R_\pm=-R_\pm\dot z R_\pm,
\]

or `d(z)=(1+z^2)^{-1}` and its rational differential rule.  On real arguments the resolvents are bounded.

### Required master estimate

The analytic version requires a weighted graph scale satisfying

\[
\|\mathscr LQ\|_{\rho'}
\le
\frac{C_T}{\rho-\rho'}\|Q\|_\rho.
\tag{3}
\]

Together with a positive radius for the initialized observables, (3) would give a uniform Taylor tail, fixed-length block continuation, and an autonomous Koopman hierarchy.

### Strength

All Gaussian evaluation occurs at initialization.  No adaptive matrix is re-Gaussianized at positive time, and no query history is stored.

### Weakness

Time analyticity of finite-dimensional trajectories does not imply a width-uniform analytic radius for averaged observables.  Coordinatewise products are not continuous on normalized `L^2`, and the maximum-coordinate Lipschitz constant grows with width.  Estimate (3) must exploit diagram cancellation or a graded tail norm; a generic Banach-ODE argument does not prove it.

### Kill gate A

For the complete two-hidden-layer arctangent flow and each target observable `Q`, test

\[
a_k(Q)=
\sup_n
\left(
\frac{\mathbb E|\operatorname{ev}_{n,0}(\mathscr L^kQ)|}{k!}
\right)^{1/k}.
\tag{4}
\]

Unbounded `a_k` disproves the simple analytic Koopman norm.  Bounded low-order numerics support but do not prove (3).

### Gate outcome

The gate fails rigorously.  In the coordinate-only `L=1` arctangent flow with `u(0)=0` and Gaussian `A(0)`, the raw-kernel coefficient `P_k=[t^k]Theta` has a degree-`k+2` Gaussian component whose leading coefficient has root `3/2`.  Its `L^1` and `L^2` coefficient roots grow at least as a constant times `sqrt(k)`.  See `KOOPMAN_ANALYTIC_NO_GO.md`.

Rooted Koopman diagrams remain a useful finite-order syntax, but analytic Taylor block continuation is removed from the candidate master theorem.

## 3. Candidate B: Wick--Malliavin response calculus

### State and recursion

Each current field carries colored Malliavin response jets.  Gaussian queries use (1)--(2); unary maps use Faà di Bruno; products and learned rank-one morphisms use Leibniz.  A rooted diagram records response-edge cuts and source contractions.  Fixed diagrams are evaluated by Wick pairing and equality partitions.

For a vector field `X`, two relevant families are the normalized energy-response norms

\[
E_{p,k}(X)=
\left\|
\left(
\frac1n\sum_i\|D^kX_i\|_{\rm HS}^2
\right)^{1/2}
\right\|_{L^p},
\]

and coordinate-response norms

\[
C_{p,k}(X)=
\left(
\frac1n\sum_i
\mathbb E\|D^kX_i\|_{\rm HS}^p
\right)^{1/p}.
\]

They can be packaged with factorial response weights.

### Exact favorable estimate

On a source-operator event `||Gamma||op <= M`, differentiating a source query gives

\[
D^k(\Gamma X)
=\Gamma D^kX
+k\,(D\Gamma)\widetilde\otimes D^{k-1}X.
\]

The `n^{-1/2}` injection balances the sum over derivative indices, giving schematically

\[
E_{p,k}(\Gamma X)
\le ME_{p,k}(X)+kE_{p,k-1}(X).
\tag{5}
\]

Thus source action is tame in the energy-response grade without assuming independence.

### The remaining loss

To obtain coordinate `L^p` control of an adaptive query, the divergence inequality applied to (1) needs one additional Malliavin derivative.  Schematically,

\[
C_{p,k}(\Gamma X)
\lesssim_{p}
E_{p,k}(X)+E_{p,k+1}(X).
\tag{6}
\]

Pointwise products then use coordinate/probability Hölder.  The calculus therefore contains a response-radius or differentiability loss.  A credible proof must show that the loss can be absorbed for all required times; merely writing an exponential generating norm does not do so.

### Candidate master estimate

The desired one-color theorem is a closed majorant for a time-dependent radius `rho(t)>0`:

\[
\sup_n\sup_{t\le T}
\sum_{k\ge0}
\frac{\rho(t)^k}{k!}
\bigl(E_{p,k}(S_n(t))+C_{p,k}(S_n(t))\bigr)
\le C_{T,p},
\tag{7}
\]

together with a chaos/diagram tail and a restart defect tending to zero.  For arctangent, global derivative bounds make a positive radius plausible, but (6) means it is not automatic.

### Kill gate B

Prove (7), or an explicitly weaker norm sufficient for Osgood stability, for the full two-hidden-layer arctangent flow.  Failure of every positive radius, loss of uniform integrability of the first adaptive transpose signal, or a nonvanishing Galerkin restart defect kills this version.

## 4. Candidate C: forest-renormalized self-energy calculus

### Proposed enhancement

Instead of retaining all response chains separately, promote coherent one-port contractions to Onsager drift and coherent two-port contractions to covariance/self-energy.  A forest formula subtracts nested promoted subdiagrams.  A finite current propagator solves

\[
\dot U=\Sigma U,
\qquad
\dot V=-V\Sigma,
\qquad
\dot C=VB,
\qquad
J=U(J_0+C).
\tag{8}
\]

If `V=U^{-1}`, (8) is the ordinary variation-of-constants resummation of a linear response equation.  It stores current propagator factors, not a two-time kernel.

### Strength

This could turn an unbounded chain registry into a fixed response type and makes the analogue with renormalized perturbation theory explicit.

### Weakness

The construction is valid only after proving that:

1. the projected self-energy is a bounded operator on a specified response space;
2. the forest grammar is complete and does not double count;
3. every unpromoted zero-defect diagram is absent or is added as a new state type;
4. the remainder has a summable width/complexity deficit.

Calling the projection `Sigma` does not prove any of these.

### Kill gate C

At the one-color nonlinear rung, enumerate the complete primitive grammar through the first overlapping response order and prove a topology-preserving induction.  At depth three, the decisive proposed statement is that overlapping two-spine diagrams leave no unrepresented zero-defect three-port primitive.  A surviving primitive falsifies a Gaussian/two-port-only closure and forces a larger state.

## 5. Existing rigorous machinery: usable scope

- **Tensor Programs / MFP:** rigorous and close to turnkey for each fixed finite program with exact transpose responses.  It is the static evaluator, not the compact-time theorem.
- **Rigorous high-dimensional first-order-method limits:** the Euler-to-AMP-to-state-evolution proof architecture demonstrates how compact-time convergence can be obtained for narrower reused-design systems.  Its available theorems do not cover several trainable square matrices, nested forward/backward passes, and rank-one matrix updates, and their natural state uses two-time kernels.
- **Traffic probability:** supplies a natural static language for transpose, diagonal, Hadamard, row-degree, and graph substitutions.  Published static traffic convergence does not supply nonlinear ODE stability, a truncation tail, or the required dynamic uniqueness.
- **Malliavin/Meyer inequalities:** provide dimension-free divergence estimates in Hilbert/UMD-valued Gaussian Sobolev spaces.  They support (6), but do not by themselves close the nonlinear response-radius evolution.
- **Ovsyannikov/Cauchy--Kowalevsky scales:** provide a standard way to solve equations that lose analytic radius.  Their use is legitimate only after the exact CFPC operations satisfy the required scale estimates and the available radius survives the desired horizon.

## 6. Current strategic choice

The program will not choose between “Koopman” and “Malliavin response” as mutually exclusive calculi.  The most constructable current design is:

1. use the exact Wick--Malliavin rules as the **source-query layer**;
2. use rooted typed diagrams as the **syntax and static evaluator**;
3. use uniform finite-program/Picard completion whenever a dimension-free state stability estimate is available;
4. use Koopman diagrams for finite-order syntax and audits, but not an ordinary analytic Taylor completion under Gaussian seeds;
5. introduce self-energy promotion only after a finite grammar proves that it genuinely sums a complete response family.

The immediate make-or-break problem is not depth three.  It is the one-color, two-hidden-layer arctangent estimate (7), or a rigorously sufficient replacement.  Until that gate passes, no response-propagator or two-spine claim is promoted beyond hypothesis.

## 7. First rollback: no universal Hilbert chaos algebra

The first preregistered probe and an independent analytic derivation settle an important design question.  If

\[
\arctan Z=\sum_qc_q\,\mathrm{He}_q(Z)/\sqrt{q!},
\qquad Z\sim N(0,1),
\]

then, along odd orders,

\[
|c_q|\asymp q^{-3/4}e^{-\sqrt q}.
\]

The derivative gate has the same root-exponential scale.  Therefore every norm with a positive exponential weight in chaos degree excludes the base activation.

The apparently natural root-Gevrey Hilbert replacement is not an ordinary-product algebra.  For normalized Hermite polynomials `h_m`, the top-chaos coefficient of `h_m^2` is

\[
\frac{\sqrt{(2m)!}}{m!}\sim\frac{2^m}{(\pi m)^{1/4}}.
\]

No subexponential radius loss absorbs this exponential multiplication factor.  Thus a single diagonal Hilbert chaos norm that both dominates `L^2`, contains arctangent, and is closed under arbitrary pointwise multiplication is impossible.

This kills a **universal Fock Hilbert algebra**, not the typed CFPC architecture.  The surviving design rules are:

1. retain arctangent and its rational differential chain as primitive symbolic gate nodes rather than expanding them into chaos before multiplication;
2. type bounded Schur multipliers separately from energy vectors;
3. admit `bounded multiplier times energy vector`, normalized contractions, and normalized outer products, but never infer `energy times energy -> energy`;
4. use Malliavin grades only for source queries and response contractions, with a projective or syntax-aware multiplication norm;
5. require every actual network product to match one of these typed rules.

The two-hidden-layer gate is now sharper: prove that the **restricted network grammar**, not arbitrary Gaussian functionals, preserves the typed response certificate.
