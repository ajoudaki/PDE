# Activity-damped quantitative transfer

Root candidate, 2026-10-01. This improves the conservative physical-time transfer in TRANSFER_DERIVATION.md. It uses the finite-program candidate and its proxy-consistency addendum. Its quantitative conclusion is pending the complete internal checks of those dependencies and this note. The actual network and closure are unchanged.

## 1. Comparison with a perturbed reference path

Let theta_D be the actual dense path, with the small-label Gram gap Gamma_D>=lambda I and the physical bounds established in the paper. Let theta_p be a piecewise absolutely continuous reference path with the same initial state, in a fixed common physical tube, and put

\[
E_p=\dot\theta_p-F(\theta_p),\quad
\epsilon_p=\int_0^T\|E_p(t)\|\,dt,\quad
\rho_p=\|f(\theta_p)-y\|_m.
\]

The norm is the paper's sum of normalized first/readout norms and hidden Frobenius norms. Assume int rho_p<=S0 with S0 fixed independently of T,n. Let H_p(R,t) be the normalized sum of the reference backward-carrier tails at cutoff R, and Z_p=int rho_p H_p. Both paths have the bounded feature RMS, bounded hidden operators, bounded readout RMS, and bounded prediction differential required by the paper's subtraction identities.

Set d(t)=d_n(theta_D,theta_p), and u=r_D-r_p. The forward and backward subtractions, using only tails of the reference, give

\[
\|\delta_D-\delta_p\|_{\mathrm{RMS}}
\le C[(1+R)d+H_p],\qquad
\|\Gamma_D-\Gamma_p\|_{\mathrm{op}}
\le C[(1+R)d+H_p].
\]

The residual equation is exactly

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\]

Only the actual Gram gap is needed. With a fixed lower damping rate lambda0>0, the norm upper derivative obeys

\[
D^+\|u\|_m\le-\lambda_0\|u\|_m
+C\rho_p[(1+R)d+H_p]+C\|E_p\|.
\]

The formula at zeros follows by regularizing the norm by sqrt(||u||^2+zeta^2) and sending zeta to zero. Integration, u(0)=0, and dropping the nonnegative terminal norm yield

\[
\int_0^t\|u\|_m\le C\left[(1+R)\int_0^t\rho_p d
+\int_0^t\rho_pH_p+\int_0^t\|E_p\|\right].
\tag{1}
\]

Parameter update subtraction uses r_D delta_D h_D - r_p delta_p h_p = u delta_D h_D plus the reference-residual times the two response differences. Bounded physical RMS and the rank-one norm identity give

\[
d(t)\le C\int_0^t\|u\|_m
+C\int_0^t\rho_p[(1+R)d+H_p]+\int_0^t\|E_p\|.
\]

Insert (1). On each terminal interval bound the nondecreasing source by its terminal value and use the integrating factor for C(1+R)rho_p. Thus

\[
\sup_{t\le T}d(t)\le Ce^{C(1+R)S_0}(\epsilon_p+Z_p).
\tag{2}
\]

The amplification depends on residual activity rather than physical duration. The same proof applies on the paper's common population Hilbert spaces, with L2 and Hilbert--Schmidt norms and the true initialized adjoints. No finite-dimensional matrix inversion is used in (1)-(2).

## 2. Properties required of the quantitative Euler proxy

Let t_j=jh, 0<=j<=K, h=T/K, and use the original deterministic population Euler residuals r_j and source fields, with the original population empirical-contraction coefficients. Its small-label construction gives

\[
\sum_{j<K}h\rho_j\le C,\quad \rho_j\le C,
\]

and uniform Gaussian carrier tails. Evaluate its regularized/clipped finite program on the actual initialized arrays, reconstruct proxy weights from its rank-one source updates, and interpolate them affinely between nodes. The program's quantitative joint event supplies empirical contractions and carrier norm tests to accuracy eta, including bias to the original population program. All additional polynomial-in-N factors can be included in eta by enlarging the exponential constant in PROGRAM_RATE_ROUTE.md.

The needed node assertions are:

* proxy parameters lie in a fixed physical tube;
* recomputed forward features and residuals agree with their program values up to C eta, after propagating through the fixed depth;
* recomputed carriers and backward responses differ by at most C[(1+R)eta+exp(-cR²)]; the node velocity defect is at most C eta+C rho_j[(1+R)eta+exp(-cR²)];
* at each node, actual proxy carrier tails satisfy H_p(R,t_j)<=C[exp(-cR²)+(1+R)eta];
* proxy speed on segment j is at most C rho_j.

The fresh query noise and the original-versus-modified population bias are included in eta. The backward gate cutoff contributes the separate exp(-cR²) term displayed above; it is not absorbed into eta. These assertions are proved in PROGRAM_RATE_ADDENDUM.md, rather than assumed to follow from output concentration alone.

The last speed bound and the bounded prediction differential imply

\[
|\rho_p(t)-\rho_j|\le C\eta+Ch\rho_j,
\qquad t_j\le t\le t_{j+1}.
\]

Consequently

\[
\int_0^T\rho_p\le C(1+h)+CT\eta.
\tag{3}
\]

Thus S0 is fixed when T eta<=1; pointwise exponential decay of the proxy residual is unnecessary.

For the source defect, node residual recomputation can contribute C eta without a rho_j factor. All other consistency errors are multiplied by the frozen source residual, hence by rho_j. Subtracting the vector field between the node and its affine interpolation state, with the node as tail reference, gives

\[
\|E_p(t)\|\le C\eta+C\rho_j[(1+R)(h+\eta)+e^{-cR^2}].
\]

The residual difference term within this comparison has size C h rho_j, not an unweighted h: the parameter segment length is at most C h rho_j. The gate-change tail term is multiplied by the residual in each hidden update. Integration therefore yields

\[
\epsilon_p\le C[(1+T)(1+R)\eta+(1+R)h+e^{-cR^2}].
\tag{4}
\]

Carrier subtraction from the node and a 1-Lipschitz positive-part cutoff give, uniformly on each segment,

\[
H_p(R,t)\le C[e^{-cR^2}+(1+R)(h+\eta)],
\]

after changing cutoff constants. Use (3) to obtain the same bracket as an upper bound for Z_p. Equations (2)-(4) prove

\[
\sup_{t\le T}d_n(\theta_D,\theta_p)
\le Ce^{CR}[(1+T)(1+R)\eta+(1+R)h+e^{-cR^2}].
\tag{5}
\]

The unperturbed population Euler interpolation obeys (3)-(5) with eta=0. The comparison is to the actual population dense solution, whose Gram gap was proved in the paper. This gives quantitative population discretization error without exp(CRT) amplification.

## 3. Choosing the number of proof steps

Set

\[
K=\left\lfloor[\log(e^e+n)]^{1/128}\right\rfloor,
\quad N=\lceil C_0K^3\rceil,
\quad T=A\log K,\quad h=T/K,\quad R=B\sqrt{\log K}.
\tag{6}
\]

Use a fixed sufficiently large lower threshold on n so K>=2. N counts elementary instructions and added roots, allowing at most K passive probes and the needed tail tests. The proof below needs only a single passive probe per program; larger nets are handled by separate programs and a union bound. Pad unused budget harmlessly. Choose A with kappa A>=2 and B with cB²>=4. The finite-program bound has eta<=n^-1/16+Ce^-cN², and failure at most Cn^-1/4 for sufficiently large n, since N^5<=C(log n)^(15/128). All fixed polynomial-in-N factors are absorbed by decreasing 1/16 if needed; eta remains a negative power of n plus an exponentially small function of K.

From (5), the dominant discretization error is

\[
e^{CB\sqrt{\log K}}\frac{C(\log K)^{3/2}}K
=K^{-1+o(1)}\le CK^{-3/4}
\tag{7}
\]

once K exceeds a fixed problem-dependent threshold. Errors after T are bounded by Ce^-kappaT<=CK^-2. Hence dense finite predictions converge to dense population predictions on the whole physical-time interval, with normalized per-probe error at most CK^-3/4, on an event of polynomially small exceptional probability. The event can depend on the passive probe; its probability constants do not after normalizing the probe as in TRANSFER_DERIVATION.md.

## 4. Quantitative carrier remainder

For every integer carrier cutoff 1<=M<=N, compare actual dense carriers to the proxy on [0,T], using cutoff R from (6). The difference is bounded by

\[
C[(1+R)K^{-3/4}+e^{-cR^2}+(1+R)h+\eta]
\le CK^{-2/3}.
\]

The soft-tail tests and the population Gaussian envelope give the additional Ce^-cM² term uniformly in M. Integrate against bounded total dense activity. After T, the remaining integral is at most CK^-2. For M>N use monotonicity and the result at N. Thus the carrier excess can be chosen to satisfy

\[
a_n\le CK^{-2/3}
\quad\text{with probability at least }1-Cn^{-c_0}.
\tag{8}
\]

The paper's Phi transform then gives, after increasing the fixed width threshold,

\[
b_n=C\Phi(a_n)\le CK^{-1/2}.
\tag{9}
\]

These are simultaneous in q because the event concerns only dense training and its reference programs. The already proved tracking argument therefore yields D_nq<=C omega(q)+CK^-1/2 for every q on this event. Constants may depend on the fixed depth, training data, activation bounds, Gram margin and small-label choice, not n,q,t.

## 5. Whole-input prediction and explicit confidence

For any x put s_x=1+||x||/sqrt(d). The normalized passive-query lemma and the deterministic prediction bound on the original good event imply

\[
\mathbb E[1_{\mathcal G_n}\sup_{t\ge0}
|f_{n,D}(t,x)-f_\infty(t,x)|^2]
\le C s_x^2[K^{-3/2}+n^{-c_0}].
\tag{10}
\]

The moment on the bad program event is bounded using deterministic physical bounds on G_n; no claim about the dynamics outside G_n is needed. Tonelli gives the same bound with factor integral s_x² dmu for the squared all-time test metric. Markov at threshold C_mu K^-1/2 yields

\[
\Pr\{\mathcal G_n\ \text{and}\ d_{n,\mu}>C_\mu K^{-1/2}\}
\le C_\mu K^{-1/2},
\tag{11}
\]

where the polynomially small term in n has been absorbed. Combining (9), (11), and the explicit initial-good-event probability gives a simple common rate

\[
\mathcal E_\mu(\widehat f_{n,q},f_\infty)
\le C_\mu\omega(q)+C_\mu[\log(e^e+n)]^{-1/256}
\quad\text{simultaneously for every }q\ge1,
\tag{12}
\]

with probability at least 1-C_mu[log(e^e+n)]^-1/256, for sufficiently large n. A weaker exponent such as 1/512 provides additional slack without changing the scientific content. For any fixed confidence delta, (10) instead gives d_n,mu<=C_mu delta^-1/2 K^-3/4 with probability 1-delta-O(n^-c0); (9) then dominates the combined remainder by K^-1/2 after a confidence-dependent width threshold.

For a bounded input set, take a net of mesh K^-3/4. Its size is O(K^(3d/4)), which need not fit N=CK³ for large fixed d. Either enlarge the program budget and decrease the exponent 1/128 accordingly, or use separate single-probe events and a union bound over the net. The latter keeps N=CK³ for each probe and costs only a fixed power of K multiplying n^-c0, which is harmless. Uniform input Lipschitz continuity extends (7) to the bounded domain. Its entire time/space supremum satisfies (12) with at least the same probability and constants depending on that domain.

## Interpretation and scope

This candidate would replace an unspecified width remainder by an explicit, very slow logarithmic rate under the paper's existing assumptions. It does not prove a polynomial rate in n and does not justify a Monte Carlo n^-1/2 accuracy law for the full nonlinear model. The tiny exponent is a proof budget, not a prediction of observed convergence. Physical training is continuous and unchanged; the Euler mesh, noisy queries, and clipping are confined to the comparison proof.

The finite-program lemma, its node/interpolation consistency addendum, and this damped transfer must all be checked before the full conclusion is labelled internally checked. The prior conservative stretched-logarithm candidate remains a fallback but is superseded if this activity-damped argument passes.
