# Borel reconstruction after the population gradient-flow theorem

Independent audit for the supervisor, 5 September 2026. This note gives conditional deductions; it does not claim that neural Borel summability has been proved.

## Sources and reconciliation

Read the full `studies/causal_flow_peeling_calculus/GEVREY_BOREL_COMPLETION_AUDIT.md`, its README, evidence ledger, and machinery verdict, together with §10 (lines 830–1172) of `AUTONOMOUS_DEEP_FEATURE_LEARNING_THEOREM_AND_PROGRAM_2026-08-21.md`. Also checked the statement, conventions, and kernel identity in the new `GENERAL_POPULATION_GF_PROOF.md`.

The exact requested top-level conjecture is §10.3, “MFP–Borel kernel-hierarchy conjecture,” added 23 August 2026. It concerns the canonical **one-sample** arctangent flow and the **output-coordinate kernel**. Its proposed approximants use rational continuation of a Borel–Leroy transform followed by finite Laplace quadrature. They form a sequence of finite autonomous scalar ODEs. The source does not assert that the raw time Taylor series converges uniformly.

The CFPC verdict kills Borel as an *automatic method for obtaining the missing flow limit*. It does not disprove the more specific initialization-compiled scalar-kernel reconstruction conjecture. Its statements that arbitrary-depth flow existence remains open are historical and superseded, for the assumptions and fixed positive interval of the new theorem, by that new theorem. Its analytic counterexamples and warnings about flat functions remain relevant.

The old audit's demand to identify every finite-width flow with its Borel sum was tied to a route that would prove width convergence by exchanging width and Borel reconstruction. Once population GF existence and width convergence have been proved independently, **that finite-width Borel identification is unnecessary for the present task**. It suffices to reconstruct and identify the population observable, then use the existing convergence theorem and a triangle inequality. All-order jet compatibility and population identification remain additional obligations.

## What the conjecture actually says

Use the new physical time t=k eta_n. In the one-sample case, including all fixed layer multipliers in K,

    f'(t)=2(y-f(t))K(t).

The old source uses tau=2 eta t because its t and fixed eta follow an older convention. In the new convention put tau=2t; there is no remaining eta_n in the population differential equation.

Assume e0=y-f0>0 and K(0)>0. Continuity gives a fixed interval [0,T1] on which K>0. Then f is strictly increasing and its canonical orbit defines a continuous scalar function

    kappa(f(t))=K(t).

This is only an orbit restriction: it does not assert that arbitrary population states with the same prediction have the same kernel. Set z=f-f0. If the actual flow has all required derivatives, let

    d_j = (d^j f/d tau^j)(0).

Formal division and inversion give

    kappa(f0+z) ~ sum_(m>=0) c_m z^m,
    c0=d1/e0,
    c1=(e0 d2+d1^2)/(e0^2 d1),
    c2=d3/(2 e0 d1^2)-d2^2/(2 e0 d1^3)
         +d2/(e0^2 d1)+d1/e0^3.

The denominators require e0 and d1 nonzero. A zero readout does not obstruct them in the nondegenerate arctangent case: hidden initial speeds vanish, but f initially moves because the readout kernel is positive. The trivial e0=0 trajectory should be treated separately.

Each c_m uses only d1,...,d_(m+1), which the proposed compiler evaluates by fixed-order initialization peeling. Formal finite-width derivative calculations and fixed-program limits do not, by themselves, prove that these limits equal derivatives of the actual population path. Uniform path convergence alone never justifies differentiating the limit.

For a proposed exponent sigma>0, the transform is

    B(xi)=sum_(m>=0) c_m xi^m / Gamma(1+sigma m).

The reconstruction would be

    kappa(f0+z)=integral_0^infinity exp(-u) B(z u^sigma) du.          (1)

Changing variables xi=z u^sigma gives exactly the generalized Laplace formula in the audit. Its convention calls this summability order 1/sigma. Thus “order two Borel” means sigma=1/2 in this denominator convention, not sigma=2. If derivatives grow like C^m(m!)^s, the power-series coefficients, after dividing derivatives by m!, have the candidate exponent sigma=s-1. These are different uses of the word “order.” No sharp Gevrey order for the current network is established by the new GF theorem.

The source proposes a finite-jet rational continuation B_N and universal finite quadrature, giving

    kappa_(N,M)(f0+z)=sum_(j=1)^M w_j B_N(z u_j^sigma),
    f_(N,M)'=2(y-f_(N,M)) kappa_(N,M)(f_(N,M)).

The substantive claim is convergence to the *actual* orbit kernel, uniformly on the needed output interval, by a declared initialization-only scheme. It includes control of rational poles and quadrature errors. Generic diagonal Pade convergence cannot be assumed.

## Four distinct analytic assertions

1. **Coefficient growth / local transform convergence.** A bound |c_m| <= C A^m Gamma(1+sigma m) gives a positive radius for B around xi=0.
2. **Continuation and Laplace existence.** B must be continued along the positive ray, with a suitable growth bound.
3. **Identification.** The Laplace sum in (1) must equal the orbit kernel of the actual population GF.
4. **Finite-jet approximation.** The chosen rational-continuation/quadrature scheme must converge uniformly to that sum on a fixed output interval.

The first assertion does not imply the other three. For every z>0, z u^sigma leaves any finite convergence disk as u increases. Moreover, exact integration of a finite Borel polynomial gives

    integral exp(-u) sum_(m=0)^N c_m (z u^sigma)^m/Gamma(1+sigma m) du
      =sum_(m=0)^N c_m z^m.

Thus simply integrating truncated Borel power series reproduces the possibly divergent raw Taylor truncations. Analytic continuation/resummation is the essential added step.

A concrete sufficient uniform-integrability condition is

    |B(xi)| <= C exp(b xi^(1/sigma)), xi>=0.

For 0<=z<=Z with b Z^(1/sigma)<1, the Laplace integrand is bounded by C exp[-(1-b Z^(1/sigma))u], uniformly in z. Local uniform convergence B_N->B on the ray, together with the same growth envelope for all B_N, therefore gives uniform convergence of their Laplace integrals on [0,Z]: split u at a large U, use local uniform convergence on [0,Z U^sigma], then use the uniform exponential tail. Uniform quadrature convergence completes the construction. These are sufficient conditions, not asserted necessary conditions for every conceivable reconstruction scheme.

Matching all jets does not establish (3). The elementary function exp(-t^(-1/sigma)), extended by zero at t=0, has every derivative at zero equal to zero and is positive for t>0. It satisfies Gevrey-flat remainder estimates. Adding it to a candidate observable leaves its entire initialization jet unchanged. This example does not create a second solution to the same unique GF; it shows why a proposed scalar reconstruction must still be proved to solve or represent that GF.

There are at least two sound ways to discharge identification:

- Prove the actual observable belongs to an appropriate quasianalytic sectorial asymptotic class, and that its jet has the declared Borel sum there.
- Reconstruct the full population state in the strong solution class, prove its Laplace sum satisfies the same integral GF equations and initialization, and then apply the new uniqueness theorem.

Matching only a scalar kernel or predictor jet does not verify the full GF equations, so full-state uniqueness cannot be invoked at that point.

For the conventional nonuniform Gevrey asymptotic class on a complex sector, injectivity holds for opening strictly greater than pi sigma; the threshold admits the displayed flat example. This is the specific Watson criterion checked in Lastra–Malek–Sanz, *Summability in general Carleman ultraholomorphic classes*, pp. 1–2: https://arxiv.org/pdf/1402.1669. It is a theorem about that class, not a universal necessary condition for identification by every possible method. No complex-sector hypothesis is supplied by the real GF existence theorem.

## A quantitative local scalar consequence

Fix 0<T<T1<=T_* such that K(t)>0 on [0,T1]. Let I=[f0,f(T1)], and write

    a=min_I kappa>0,   M=max_I kappa,
    delta=sup_I |kappa_N-kappa|,   rho=delta/a<1.

Assume kappa_N is continuous (the declared rational scheme should in particular have no poles on I). The approximate scalar velocity is between (1-rho) and (1+rho) times the true scalar velocity. Integration of the separated clock gives, as long as (1+rho)T<=T1,

    f((1-rho)t) <= f_N(t) <= f((1+rho)t), 0<=t<=T.

Here uniqueness follows directly from separation because both velocities are strictly positive on I. Since |f'|<=2e0 M and |[(y-f)^2]'|<=4e0^2 M,

    sup_(t<=T) |f_N(t)-f(t)| <= (2e0 M T/a) delta,
    sup_(t<=T) |L_N(t)-L(t)| <= (4e0^2 M T/a) delta.              (2)

This local transfer needs no positive-time data and no derivative bound for kappa. The small time margin T1>T avoids silently evaluating the true flow outside its proved interval. If the reconstruction is only known on [0,T0] with fixed T0<T_*, its implication is confined to t<T0. A shrinking interval T_N->0 establishes no approximation at any fixed t>0. Existence up to T_* does not extend the radius or summability range of an initialization expansion.

The source's all-time proposal further requires reconstruction over the complete output interval to the target and a global positive kernel lower bound. The local GF theorem alone does not supply those requirements.

## Fixed datasets require a different extension

For m inputs and normalized weights, the new theorem gives

    f_a'=-2 sum_b omega_b K_ab(t)(f_b-y_b).

There is generally no common scalar monotone predictor coordinate. Individual predictors may turn or remain still while other examples and features move. The one-sample output-coordinate Borel conjecture therefore does not automatically cover the current multi-input setting.

A precise conditional alternative is to Borel-reconstruct the matrix K(t) from its **time** initialization jets. If K_N(t) is such a reconstruction, put Omega=diag(omega_a) and

    A(t)=Omega^(1/2) K(t) Omega^(1/2),
    A_N(t)=Omega^(1/2) K_N(t) Omega^(1/2),
    delta_N=sup_(t<=T) ||A_N(t)-A(t)||_op.

Let u=Omega^(1/2)(f-y), u_N=Omega^(1/2)(f_N-y), and let f_N solve the known-coefficient vector equation with K_N. Then u'=-2Au and u_N'=-2A_Nu_N. The true A is positive semidefinite, so ||u(t)||<=||u(0)||. Since the symmetric part of A_N is bounded below by -delta_N I,

    ||u_N(t)|| <= exp(2delta_N t)||u(0)||.

For e=u_N-u, use e'=-2Ae-2(A_N-A)u_N. Taking its norm and integrating gives

    sup_(t<=T)||u_N(t)-u(t)||
        <= [exp(2delta_N T)-1]||u(0)||,
    sup_(t<=T)|L_N(t)-L(t)|
        <= [exp(4delta_N T)-1]L(0).                              (3)

If A_N is also positive semidefinite, the sharper bounds are 2delta_N T||u(0)|| and 4delta_N T L(0). Uniform entrywise kernel error <=epsilon implies delta_N<=epsilon, because the Frobenius norm of Omega^(1/2)(K_N-K)Omega^(1/2) is at most epsilon when sum omega_a=1.

This matrix construction is an extension of the proposal, not a result asserted by §10. It may be written as a finite autonomous ODE after adding a clock s'=1, because K_N(s) is precomputed from initialization. That is a different state construction from the original one-dimensional output-only ODE; the distinction must be stated. It uses no fitted positive-time trajectory or oracle if the finite-jet reconstruction is genuinely supplied.

## What one could then conclude about actual networks

Once a finite initialization-compiled approximant has population error <=epsilon on a fixed interval, existing joint width/GD convergence gives

    sup_(t<=T)||f_n^GD(t)-f_N(t)||
      <= sup_(t<=T)||f_n^GD(t)-f(t)|| + epsilon
      = o_P(1)+epsilon.

The norm is the ordinary scalar norm in the one-sample case or the weighted prediction norm used in (3). One first fixes the desired accuracy and its finite initialization compilation; width then tends to infinity and eta_n tends to zero with no extra relation. No arbitrary joint growth of approximation order with n follows without an additional quantitative estimate.

Thus the conjecture would provide a finite initialization-only predictor/loss computation, valid uniformly over a fixed positive interval. It would not by itself reconstruct hidden field laws, prove a finite-dimensional state law for all population states, eliminate nonlinear feature learning, or prove all-time control.

Finally, the new theorem's broad C1,1 activation class does not even assume all-order differentiability. The arctangent Borel program remains an additional analytic conjecture for the appropriate smoother subclass. Even C-infinity smoothness by itself is insufficient because of flat functions. Gaussian averaging can sometimes improve observable regularity, but no such all-order/quasianalytic improvement is established by the current GF proof.
