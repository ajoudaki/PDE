# Independent internal review of the exact weighted Gaussian formula

Date: 2026-09-21. Scope: fresh isolated mathematical review, not a promotion review. No numerical or training runs.

**Verdict:** PASS for the stated exact weighted Gaussian identities and initialized coefficient normalization. The displayed formulas **do not meet** the stricter terminal class consisting only of finite products of the original tanh and its derivatives at Gaussian arguments. They meet the explicitly enlarged density-weight class. No mathematical correction is required for the claims as scoped in the candidate. This verdict does not prove that another, strict representation is impossible.

## Frozen inputs and complete reading coverage

Read completely, with no truncated tool output:

- `EXACT_PEEL_WEIGHTED.md`, all sections 1–5 including 4a and all equations (1)–(7). SHA256: `b5e328d19bf00de0f84e4fc0bc93a4406cab442c615d5eb05407f29701571ecc`.
- `docs/observable_p1.md`, all sections. SHA256: `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
- `docs/NOTATION.md`, all sections. SHA256: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`, completely.

All three scientific-input hashes matched the assignment. No study README, other study artifact, previous verdict, history, implementation, or upstream linked source was consulted. The assignment treated the historical references as provenance; no additional dependency was needed for the identities reviewed here.

## Identity and normalization checks

**Setup and the 2×2 contraction.** The canonical definitions give `0<v,tau<1`, so all Gaussian variances and the divisions by `tau` used below are valid; `alpha=1-tau>0`. The pair `(h,k)` has second-moment matrix `[[v,beta],[beta,s]]`. Adding `eta I`, with `eta=1/4096>0`, makes `Gamma` positive definite, including any possible dependence of the unregularized pair.

Here is an independent reconstruction of the normalization. Write `c=sqrt(tau+eta)`, `r=(alpha v,alpha beta+tau gamma)`, and let `L` be the lower Cholesky factor of `Gamma`. For a normalized input with coordinate correlation `rho`, the raw lower projection is `q_rho=(A(rho),B(rho))^T`. The normalized projection is `L^{-1}q_rho`, while the initialized contraction row is `c^{-1}r L^{-T}`. Their product is therefore

    c^{-1} r L^{-T} L^{-1} q_rho
      = c^{-1} r Gamma^{-1} q_rho.

Multiplication by the upper dictionary feature `H_i/c` gives the coefficient `r Gamma^{-1}q_rho/(tau+eta)`, exactly `Lambda(rho)`. It also proves that the active entries before this last multiplication are `c(a_theta,b_theta)`. Input normalization `x/sqrt(2)=(cos theta,sin theta)` gives the claimed correlations; the constant projection vanishes by oddness. The reverse-use term `tau gamma` and the inverse transpose are both retained. At zero readout, only the readout part of the tangent kernel survives, giving the displayed upper-feature Gram without an extra loss factor.

**Change of measure and endpoint regularity, (1).** The inverse substitution is `g=atanh(z)/sqrt(q)` with Jacobian `1/[sqrt(q)(1-z^2)]`. Dividing its transformed density by the `N(0,q)` density gives precisely `w_q`, including the `exp(z^2/(2q))` factor. Thus `w_q` is nonnegative and normalized, and the equality extends to every integrable signed function by its positive and negative parts.

For the smooth extension, put `z=tanh(t)`. Then

    w_q(tanh t)=exp((tanh(t)^2-t^2)/(2q)) cosh(t)^2,
    d/dz=cosh(t)^2 d/dt.

Any fixed number of derivatives is bounded by a polynomial in `|t|` times `exp(-t^2/(2q)+C|t|)`. It tends to zero at either end. This verifies all endpoint derivatives, compact support, and boundedness, rather than merely continuity.

**Upper kernel and singular pairs, (2).** Apply (1) independently to the two upper raw features. Their product density is exactly `w_v(Y1)w_v(Y2)`. Linear combinations have the displayed covariance, and their covariances with each root are `v` times its coefficient. The joint Gaussian may be singular: no inverse or Gaussian density on the image is used. Zero, coincident, opposite, and other linearly dependent coefficient pairs are covered. Absolute integrability is bounded by `E[w_v(Y1)w_v(Y2)]=1`. This argument establishes the weighted expectation, not an unweighted Gaussian law for the actual upper preactivation.

**Lower formulas and Stein step, (3)–(4).** Replacing `tanh(G)` by the weighted reference root `S` gives each of (3), with covariance `Cov(S,R)=[[1,alpha],[alpha,alpha^2+tau]]`. The identity `tanh'=1-tanh^2`, together with `E w_1=1`, gives `gamma=1-s`. Logarithmic differentiation yields

    w_1'/w_1 = z + (2z-atanh(z))/(1-z^2)

on the open support. The derivative `w_1'` extends by zero at and beyond the endpoints. For fixed `Z`, Gaussian integration by parts applied to `w_1(S)tanh(alpha S+sqrt(tau)Z)` gives exactly the two terms in (4), with a positive factor `alpha` in the second. Compact support and the bounded derivatives established above justify the integration, zero boundary terms, and averaging over `Z`.

**Correlated lower density ratio, (5)–(6).** Transforming only the first coordinate of the correlated pair `(G,T)` gives the stated joint density of `(tanh(G),T)`. Division by the density of **independent** standard `(S,Y)` reproduces every factor in `J_rho`, including its determinant factor and cross-term sign. Under the reference measure, `R` and `Y` are independent, while the weight restores the required dependence. Nonnegativity and total mass one prove integrability; boundedness of `J_rho` is neither required nor claimed. At `rho=0`, `J_0=w_1` and the independent odd factor gives `B(0)=0`. At `rho=±1`, the density-ratio construction is correctly replaced by direct substitution, giving `A(±1)=±v` and `B(±1)=±beta`. Bounded convergence in the original coupled variables proves the asserted endpoint limits.

**Translation alternative, (7).** Conditional on `G`, set `m=alpha tanh(G)`. The ratio of the `N(m,tau)` density at `T` to the `N(0,tau)` density is `exp(mT/tau-m^2/(2tau))`, exactly `L`. Applying this conditional identity with `V` retained proves all four expressions in (7). Its conditional expectation is one. The bound `L<=exp(alpha |T|/tau)` is valid because `alpha>0` and `|tanh G|<=1`; the Gaussian exponential has finite expectation. The stated covariance of `(G,Y_rho,T)` is correct, including its singular endpoint cases. In particular `Y_1=G`, `Y_{-1}=-G`, and the formula recovers the endpoint values without a density for `(G,Y_rho)`.

## Adversarial checks and scope limitations

The audit explicitly tested missing ridge factors, the Cholesky-transpose orientation, loss normalization, omitted reverse response, accidental correlation in the reference roots, endpoint singularities, boundary terms, normalization of every density ratio, and interchange of integrals. None produces a defect in the claimed identities. All integrations are justified by nonnegative normalized weights and bounded activation factors, or by the explicit smooth compact support used in Stein's identity.

The extra terminals cannot be silently classified as original activation factors. For example, nonzero compactly supported `w_q` is not a finite product of real-analytic tanh derivatives at linear arguments; `L` is unbounded along a suitable `T` direction with fixed nonzero `G`, whereas such activation products are bounded. These observations classify the displayed integrands only. They do not preclude a different expectation identity within the strict class. Section 5 states this distinction correctly. The words about Gaussian activation arguments describe the explicit tanh factors; the density weights still carry the nonlinear dependence.

The review accepts the frozen established source-rule/contraction target in `observable_p1.md` and checks its specialization and normalization here. It does not independently re-prove the upstream adaptive Gaussian source theorem, authenticate historical provenance, audit maintained code or numerical cost claims, establish positive-time behavior, or establish a closure-order limit. Those are not claims of this candidate. This internal PASS is not promotion approval and does not close the stricter original-activation-only problem.
