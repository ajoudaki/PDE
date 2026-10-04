# Exact empirical path quadrature and the neuron-count target

2026-10-03. Coordinator derivation for the user's clarified neuron-reduction
objective. This is a quadrature lemma for a prescribed reference path, not a
closed reduced training algorithm. Scientific inputs are the current study's
original neuron-sampling note, the manuscript's model and query norm, and the
canonical notation contract. No population-limit estimate is imported.

## 1. Error against the realized finite model

Let the width-n reference closure have neuron contributions
\[
 F_i(t,x)=w_i(t)h_i^{(2)}(t,x),\qquad
 \widehat f_{n,q}(t,x)=\frac1n\sum_{i=1}^nF_i(t,x).
\]
Its initialization, fixed mixer and all its training trajectories are fixed
for the following conditional sampling calculation. The sampling design is
chosen from permitted initialization information; it does not observe the
reference's trained path. The path is used only in the mathematical error
bound. In particular, the estimate below is not an implementable reduced
model unless a separate dynamics supplies the sampled contributions.

Partition the indices into nonempty cells C_s, s=1,...,N, and put
p_s=|C_s|/n. Independently choose I_s uniformly from C_s, and define the
reference-path estimator
\[
 Q_NF(t,x)=\sum_{s=1}^Np_sF_{I_s}(t,x).
\]
Conditional on the full initialized network, its pointwise expectation is
exactly the original finite predictor at every t,x. This has no
finite-width-to-population bias. The conditioning includes the reference
trajectory because that trajectory is determined by the initialization;
it does not make the random selections depend on that trajectory.

Let mu be the fixed query probability law. Suppose F_i(0,x)=0 and the
F_i are absolutely continuous in time with the integrability needed below.
Define the within-cell variance of the prediction velocity by
\[
 V_s(t)=\frac1{2|C_s|^2}\sum_{i,j\in C_s}
       \int |\dot F_i(t,x)-\dot F_j(t,x)|^2\,d\mu(x).
\]
This is a property of the original trajectory, not a newly assumed neural
regularity estimate. Conditional independence and zero means give the exact
identity
\[
 \mathbb E\int\left|
    \sum_s p_s\dot F_{I_s}(t,x)
      -\frac1n\sum_i\dot F_i(t,x)
 \right|^2d\mu(x)
 =\sum_s p_s^2 V_s(t).
\tag{1}
\]
To verify the factor in V_s, expand the squared pair differences: half
their average is the mean squared distance from the cell mean.

For any absolutely continuous zero-initialized error e(t,x),
\[
 \left(\int\sup_{t\ge0}|e(t,x)|^2d\mu(x)\right)^{1/2}
 \le\int_0^\infty
       \left(\int|\dot e(t,x)|^2d\mu(x)\right)^{1/2}dt.
\]
The pointwise fundamental theorem of calculus gives the first bound;
Minkowski's inequality then gives the displayed integral. Apply Minkowski
once more in the sampling probability space, and use (1). The resulting
full-time empirical quadrature estimate is
\[
 \left[\mathbb E\int\sup_{t\ge0}
       |Q_NF(t,x)-\widehat f_{n,q}(t,x)|^2d\mu(x)\right]^{1/2}
 \le\int_0^\infty
       \left[\sum_s p_s^2V_s(t)\right]^{1/2}dt.
\tag{2}
\]
One may first prove this on [0,T] and then let T increase using monotone
convergence. If the right side is B_N, Markov's inequality gives error
at most B_N/sqrt(delta) with probability at least 1-delta. No union bound
over training times or assumption of independent errors at different times
is used. Integrable variation also transfers the estimate to existing limits.

For example, if marks xi_i in R^D admit cells of diameter at most C N^(-1/D)
and p_s <= C/N, and the actual reference prediction velocities satisfy
\[
 \|\dot F_i(t,\cdot)-\dot F_j(t,\cdot)\|_{L^2(\mu)}
 \le L(t)|\xi_i-\xi_j|,\qquad \int_0^\infty L(t)dt<\infty,
\]
then (2) is bounded by
\[
 C N^{-1/2-1/D}\int_0^\infty L(t)dt.
\tag{3}
\]
Indeed V_s(t) <= C L(t)^2 N^(-2/D), and sum p_s^2 <= C/N.
Equation (3) explains the possible gain but does not establish these mark
and regularity properties for the actual network. A finite number of
population measures alone supplies neither property.

## 2. The remaining dynamical term cannot be dropped

If an autonomous reduced model supplies contributions \(\widetilde F_s\),
its predictor is \(\widetilde f=\sum_s p_s\widetilde F_s\). The exact
comparison splits as
\[
 \widetilde f-\widehat f_{n,q}
 =\sum_s p_s(\widetilde F_s-F_{I_s})
       +(Q_NF-\widehat f_{n,q}).
\tag{4}
\]
The second term is controlled by (2). The first contains the changed
forward mixer action, its reverse action, both moment populations, the
residual and clock. It need not be centered or small even when the second
term is an excellent quadrature estimate. Counting selected neurons only
after supplying them their exact reference trajectories would omit this
term and violate autonomy.

The reference-path method does avoid one incorrect adaptivity objection:
the source quadrature error can be evaluated on the full reference flow,
which is independent of the sampling coins conditional on initialization.
There is no need to assert that the reduced model's adaptively chosen
integrands are pointwise unbiased. What is still necessary is a genuine
feedback comparison controlling the first term of (4), including all
systematic bias. No such general estimate is asserted here.

## 3. What sampling rate would make total learned state sublinear?

Suppose, only for this arithmetic assessment, that a full dynamical
sampling theorem eventually yields N^(-alpha+o(1)) error, with all
constants controlled uniformly in the chosen q, n and physical time.
Matching n^(-1/2) then requires
\[
 N=n^{1/(2\alpha)+o(1)}.
\]
If this can be combined with the separately proved q=n^(1/6+o(1))
memory order without further losses, the moving count becomes
\[
 Nq=n^{1/(2\alpha)+1/6+o(1)}.
\tag{5}
\]
Thus a strict power saving below linear requires alpha>3/5. At the
boundary alpha=3/5, this exponent calculation yields n^(1+o(1)) and
does not decide whether subpolynomial factors give little-o(n). This is not a lower bound
against other compression designs; it is the exact exponent criterion for
these two error certificates combined in this manner.

| Hypothetical full sampling error | Neuron count at root-n accuracy | Combined moving count |
|---|---:|---:|
| N^(-1/2) | n | n^(7/6+o(1)) |
| N^(-3/4) | n^(2/3) | n^(5/6+o(1)) |
| N^(-1) | n^(1/2) | n^(2/3+o(1)) |

For first-order stratification in a fixed D-dimensional mark space,
alpha=1/2+1/D would give N=n^(D/(D+2)+o(1)). Equation (5) has a power
exponent below one precisely when D<10. At D=10 the subpolynomial
factors remain undetermined. A mark dimension that grows with q or n
does not furnish this conclusion. Higher regularity or summable
anisotropy could change this arithmetic, but its actual neural estimates
must be proved. Neither a near-root population limit nor a closed
finite-dimensional mark representation is a premise of the present lemma.

## Status

Equations (1), (2) and (4) are exact finite empirical statements; (3) is
a conditional corollary whose neural hypotheses remain open. Equation (5)
is resource arithmetic, not a neural convergence result. None establishes
the user's requested neuron-reduced autonomous all-time closure.
