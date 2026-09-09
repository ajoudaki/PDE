# Context audit of the August 19 synthesis for the initialization-jet question

Read in full: `/home/amir/Codes/PDE/UNIFIED_FINITE_CAUSAL_NEURAL_PDE_SYNTHESIS_2026-08-19.md`, all 3,150 lines. Also checked the status, scalar-object definition, exact reconstruction, failed-route, and open-obligation portions of `studies/stieltjes_conjecture/CURRENT_RESEARCH_STATE.md`; the latter is dated August 19 and agrees with the synthesis. I did not read every line of that 2,824-line maintained ledger because the synthesis already fully reconstructs this context. No experiments were run and no existing document was changed.

## Main source finding

The August 19 top-level synthesis has **no occurrence of Borel, Laguerre, Gevrey, or summability**. Its non-Taylor initialization-derived construction is the scalar **Stieltjes/Jacobi rational hierarchy**, not a Borel conformal series. This older branch must be distinguished from the later August 21 document read by the supervisor.

Exact locations in the top-level August 19 document:

- Lines 27–47: finite causal approximation contract, distinction between finite-dimensional source and a finite-dimensional scalar state, and anti-oracle/dense-restart requirements.
- Lines 1312–1365 (section 8.1–8.2): fixed-order derivative computation as finite Gaussian/Wick–Stein/tensor-program DAG; every derivative order is fixed before width. Imported Non-Gaussian Tensor Programs theorem requires C-infinity coordinate nonlinearities with every derivative polynomially bounded; finite C5 bounds alone do not justify the stated probability limit.
- Lines 1586–1658: order-five initialization compiler and multi-observable heads. Every separately fixed derivative order can be algorithmically evaluated in proved restricted scopes; no all-order growth or positive-time summation follows.
- Lines 2082–2126: zero Taylor radius for the quadratic formal jet, failure of positive Taylor partial-sum dynamics, and explicit warning that a complete smooth jet fails to identify its positive-time curve (flat corrections).
- Lines 2313–2400: exact scalar output-coordinate transformation, formulas for first transformed coefficients, and separation of positivity, determinacy, neural identification.
- Lines 2676–2765: conditional rational approximation and scalar-flow stability.
- Lines 2533–2589, 2790–2804: exact failures of universal Stieltjes extensions.
- Lines 3039–3050: supersession ledger.

## Scalar coordinate, with source scope preserved

The source canonical model is one sample, two hidden **square** layers, Gaussian roots, all three parameter blocks trained at the equal metric. This is not our current arctan/nonlinear Lipschitz theorem. In the source notation, feature time s runs the autonomous ascent of the scalar network output. Its formal initialization jet is

    J_k = lim_{n→∞} E[D_n^k f_n(0)],    D_n=n ∇f_n·∇.

This is a fixed-order annealed statement, not existence of a population feature-ascent curve. If an actual strictly increasing feature output F(s) exists near zero, its output-coordinate speed is

    κ(y)=F'(F^{-1}(y)).

Then F'=κ(F). For target 1 and squared loss, physical time traverses the same parameter route with ds/dt=2(1-F(s)), so

    dy/dt=2(1-y)κ(y),     L(t)=(1-y(t))².

The factor 2 is the squared-loss derivative. The source's general η is removable by physical-time rescaling; our joint limit uses t=kη_n, so η_n must not remain in the limiting physical ODE.

The maintained source explicitly states that this route reparameterization is special to one sample and local unless actual invertibility persists: `CURRENT_RESEARCH_STATE.md:178–194`. For a generic multi-input system, parameter drift is a sum of residual-weighted gradients with changing relative coefficients. There is no single loss-independent scalar feature clock. One can still form direct physical-time multi-observable initialization jets; scalar Stieltjes output inversion does not transfer automatically.

## What the initialization coefficients compile

Readout symmetry makes the source formal F odd, κ even. Set

    κ(y)=J_1+g_1 y²+g_2 y⁴+⋯,
    R(x)=(κ(√x)-J_1)/x=Σ_{r≥0}(-1)^r μ_r x^r.

Series inversion gives, in the source normalization,

    μ_0=J_3/(2 J_1²),
    μ_1=(4J_3²-J_1J_5)/(24J_1⁵),
    μ_2=(J_1²J_7-26J_1J_3J_5+70J_3³)/(720J_1⁸).

Thus each finite transformed prefix is a deterministic algebraic function of finitely many initialization jets; no positive-time trajectory is fitted. Positivity of raw jets does not force positivity of transformed coefficients.

The source conjecture is R(x)=∫(1+λx)^{-1}ρ(dλ) for a finite positive measure on [0,∞). The three logically independent obligations are:

1. V1: all ordinary and shifted moment Hankel forms are nonnegative, giving a representing measure.
2. V2: moment determinacy, giving a unique measure.
3. V3: this resolvent equals the actual independently constructed neural output-coordinate kernel.

The August 19 text explicitly warns V1–V2 do not imply V3, even if all derivatives match: lines 2394–2400.

With N quadrature nodes, moments determine a rational kernel

    κ_N(y)=J_1+y² Σ_{j=1}^N w_j/(1+λ_j y²),

and a scalar autonomous ODE y_N'=2(1-y_N)κ_N(y_N). The N nodes and weights are fixed initialization-compiled coefficients, not trained state variables. Consequently these particular output approximants have a scalar evolving state, although their compiler complexity grows with N. This is much more specialized than a finite collection of population fields/operators.

The maintained source at lines 1874–1927 explicitly records conditional local uniform resolvent convergence under determinacy, followed by the full three-bridge assumption and the uniform loss comparison below.

## Conditional scalar stability and the present positive-time theorem

If κ is already identified on the output interval [0,1] and a=inf κ>0, M=sup κ<∞, then for ε_N=sup|κ_N−κ|<a,

    sup_{t≥0}|L_N(t)−L(t)|
      ≤ [M/(a e)] [−log(1−ε_N/a)].

This all-time comparison belongs only to the source one-sample positive kernel and full output-interval hypotheses. It is not a consequence of merely having our new GF on [0,T_*]. For any fixed T<T_* one can instead restrict comparison to the compact output range actually attained, with the usual local scalar ODE stability if the approximated kernel is regular there. On that compact interval a uniform kernel error yields a uniform output/loss error. Generic multi-input physical-time Borel reconstruction needs its own vector observable or state identity.

Our GF theorem newly supplies an actual target curve on a nonvanishing interval for Lipschitz smooth activations. It does **not** by itself supply:

- all time derivatives at zero for C^{1,1} activations;
- an all-order derivative compiler;
- identification of a separately compiled fixed-order limit as an actual derivative of the population curve;
- a Gevrey bound or Borel continuation/growth estimate;
- equality between any Borel/Stieltjes reconstruction and that curve;
- any all-time claim, arbitrary-depth strict activity, or finite-source PDE compression.

For arctan, the coordinate activation is analytic and its fixed-order derivative programs satisfy substantially stronger smoothness/moment conditions, but a uniform-in-order summability theorem is still additional. If the later Borel hypothesis explicitly asserts convergence **to the actual population observable** on [0,T_B] for fixed T_B>0, then combined with population GF convergence it yields the desired initialization-only finite approximation of finite-width GD on every T≤min(T_B,T_*). If it asserts only convergence of a constructed series to some function, neural identification remains an obligation. GF uniqueness helps only after that reconstructed function/state is shown to satisfy the same population initial-value problem in the uniqueness class.

## Exact Stieltjes failures to keep separate from Borel

The source canonical raw-square model passes only its eight available moments; all-order V1–V3 remain open. Smooth-activation universality is exactly false: a normalized sine example has μ_0<0 and μ_1<0 (`UNIFIED...:2543`, maintained source 1238–1256). The entire strictly positive metric segment β=1, 0<α≤0.01 has a negative shifted 3×3 Hankel determinant (top-level lines 2549–2583). These falsify a positive Stieltjes representation in those scopes. They do not falsify a signed Borel or conformal-Borel reconstruction for smooth bounded activations.

No canonical Stieltjes breakthrough supersedes the August 19 synthesis in the maintained Stieltjes status checked here. The new September GF result applies to a different activation scope, so it does not retroactively prove positive-time existence for the unbounded quadratic laboratory; square activation violates the bounded-first-derivative assumption.
