# Quantitative transfer to all time and whole-input predictions

Root derivation, 2026-10-01. This note separates a proved transfer calculation from its finite-Gaussian-program premise. The latter is being investigated in PROGRAM_RATE_ROUTE.md; until that premise is completely checked, this note is not an unconditional width-rate theorem.

## 1. What a source rate would imply

The current paper gives, on its common initial good events,

\[
D_{n,q}\le C\omega(q)+C\Phi(a_n),\qquad
\omega(q)=q^{-2}e^{K\sqrt{\log(e+q)}},\qquad
\Phi(u)=u e^{K\sqrt{\log(e+1/u)}}.
\]

For prediction against the dense population it adds the actual dense-to-population discrepancy d_n,mu:

\[
\mathcal E_\mu(\widehat f_{n,q},f_\infty)
\le C_\mu\omega(q)+C_\mu\Phi(a_n)+d_{n,\mu}.
\tag{1}
\]

If a_n=O_P(n^-beta) and d_n,mu=O_P(n^-gamma) for positive beta,gamma, then

\[
C_\mu\Phi(a_n)+d_{n,\mu}
=O_P\bigl(n^{-\beta}e^{K'\sqrt{\log(e+n)}}+n^{-\gamma}\bigr).
\tag{2}
\]

Indeed, for each desired confidence choose a constant A making a_n<=A n^-beta on that event. For all sufficiently small u, Phi is increasing: its logarithmic derivative is 1 minus a term bounded by K/(2 sqrt(log(1/u))), hence positive. Substitute A n^-beta and absorb constant logarithms into K' and the prefactor. A fixed bounded range of n can be absorbed into the confidence-dependent constant. The Gaussian amplification changes the algebraic exponent only by o(1). This does not prove either premise rate.

Squared error and RMS error have different powers: a prediction variance of order 1/n corresponds to error of order 1/sqrt(n), not 1/n.

## 2. A precise finite-program input sufficient for a slow explicit rate

Let J be a maximum number of physical Euler steps, with fixed depth and batch. Suppose the finite Gaussian reference-program argument can be made to give the following quantified assertion, with some fixed finite integer p and constants C,c independent of J,n:

For every Euler reference on a horizon T<=J with at most J steps, every needed empirical contraction and normalized vector consistency/tail measurement differs from its population value by at most

\[
\eta_{n,J}=e^{C J^p}n^{-c}+e^{-cJ}
\tag{3}
\]

outside an event of probability at most e^{C J^p}n^-c. The assertion must cover the joint computations and all the soft carrier cutoffs used below, not only one output. The source distributions are those of the actual small-activity population reference. It must account for both orientations of each reused matrix and singular query covariances.

The exponent p need not be optimized. If justified, choose

\[
J=\left\lfloor a[\log(e+n)]^{1/p}\right\rfloor
\]

with sufficiently small fixed a so the statistical part and failure probability are at most n^-c/2 (after harmless constant changes). Choosing a smaller power of log(n) works as well.

The source regularization used to prove (3), if any, must be a proof device whose error is included in eta; it cannot change the actual network.

## 3. Explicit horizon/cutoff balance

The paper's reference comparison comes directly from bounded tube constants and a cutoff product inequality. With all empirical consistency/tail errors bounded by eta, its finite-horizon consequence can be written

\[
\mathrm{Err}_{n,J}(T)
\le C(1+T)e^{C(1+R)T}
\left[(1+R)h+e^{-cR^2}+\operatorname{poly}(J)\eta_{n,J}\right],
\quad h=T/J.
\tag{4}
\]

Here Err includes parameter comparison to the reconstructed proxy and population Euler error; the polynomial accommodates the finite sums in proxy contractions. To justify the explicit time constant, subtract the two integral equations on the common physical tube. The vector-field difference has coefficient C(1+R), uniformly in physical time. The per-unit-time consistency error is bounded by the bracket. Integration gives a factor T, and an integrating factor gives exp(C(1+R)T). All physical constants were fixed by the all-time small-activity bootstrap, so no additional unspecified C_T is needed. Any fixed polynomial in J can instead be absorbed by enlarging p in (3).

Take R=B sqrt(log(e+J)) and T=A sqrt(log(e+J)). First choose B with cB^2>=4, then choose A>0 with 2CAB<=1/8, enlarging J's fixed lower threshold to absorb the linear-in-T part of the exponent. The amplification is at most J^1/8. The mesh term in (4) is at most C(log J)^(3/2)J^-7/8. The Gaussian tail term is at most C sqrt(log J)J^-31/8. The statistical term remains a negative power of n times a fixed polynomial in J; e^-cJ is harmless. Consequently Err<=C J^-1/2 for sufficiently large n.

The physical tails of both the actual dense flow and population flow satisfy

\[
|f(t,x)-f(T,x)|\le Ce^{-\kappa T}(1+\|x\|/\sqrt d),\quad t\ge T.
\]

Thus the late-time error dominates the power of J, giving the explicit shape

\[
r_n=C\exp[-c\sqrt{\log\log(e^e+n)}].
\tag{5}
\]

This rate tends to zero more slowly than every fixed negative power of log(n). It is much weaker than n^-1/2. Its value would be an explicit all-time theorem under unchanged assumptions, not an efficient quantitative width theorem.

## 4. Carrier excess uniformly over its cutoff

To derive a_n, apply the same reference comparison to g_M(v)=(|v|-M)_+. This scalar map is 1-Lipschitz uniformly in M, and |v|1_(|v|>2M)<=2g_M(v). The finite reference-program estimate must include its empirical squared norms. Uniform Gaussian fourth moments bound their variances independently of M. Union bounds over finitely many reference nodes and integer M<=J cost only a polynomial in J.

The parameter comparison and the reference-cutoff product inequality then control actual carrier differences with at most another factor C(1+R), which is absorbed into J^-1/2 after weakening the power. The population tail is Ce^-cM². The physical-time integral multiplies errors by at most a fixed activity budget (or T, which is still harmless). After T the whole tail integral is <=Ce^-kappaT uniformly in M. This yields

\[
Z_n(M)\le Ce^{-cM^2}+Cr_n\quad (1\le M\le J).
\]

For M>J, monotonicity gives Z_n(M)<=Z_n(J)<=Ce^-cJ²+Cr_n. Thus a_n<=Cr_n on the common event, with constants independent of q. This argument requires joint soft-tail measurements in (3); output concentration alone is insufficient.

Since log(1/r_n) has order sqrt(log log n),

\[
\Phi(r_n)\le C\exp[-c'\sqrt{\log\log(e^e+n)}]
\]

after decreasing c'>0. The positive correction from Phi has only order (log log n)^(1/4) in the exponent and is absorbed by the negative square-root term.

## 5. Test distributions and bounded input domains

For a fixed passive query, divide its forward fields by s_x=1+||x||/sqrt(d). Its coordinate activations become phi(s_x u)/s_x, whose Lipschitz constants and values at zero are uniformly bounded. The normalized first-layer root variance is bounded. Passive prediction needs forward queries only, so no derivative of that rescaled activation occurs in its coordinate program. If (3) is uniform over these normalized query maps, the preceding estimates have constants independent of x after dividing predictions by s_x.

On the common physical good event, absolute normalized predictions are bounded. Hence a per-query bound by r_n with exceptional probability n^-c yields

\[
\mathbb E[1_{\mathcal G_n}\sup_{t\ge0}
|f_{n,D}(t,x)-f_\infty(t,x)|^2]\le C s_x^2 r_n^2.
\]

Integrate over any fixed mu with finite second moment. Tonelli and Markov then imply

\[
d_{n,\mu}=O_P(r_n),
\]

without a new quantitative tail assumption on mu. The discarded initial-good-event probability must also have been bounded by the quantitative program/initialization calculation.

For a fixed bounded domain, take a net of mesh r_n. Its size is at most C r_n^-d. Predictions are uniformly Lipschitz in x, so the net error extends to the domain. This subpolynomial-in-n net size can be absorbed in the n^-c exceptional probability from (3). The uniform absolute prediction error has the same r_n shape.

## Status

The transformations (1)-(2) and the cutoff/horizon optimization (3)-(5) are explicit algebraic consequences of their stated premises. The current full-width result remains conditional until a quantitatively correct finite-program lemma (3), including the uncut-to-regularized comparison, is supplied and checked. No polynomial rate or efficient epsilon-width cost is implied by this weak route.
