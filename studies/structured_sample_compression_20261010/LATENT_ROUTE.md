# Latent geometry and weighted sample compression

Status: an internally derived, conditional theorem route. This scoped analysis
uses only the supervisor's stated problem and required mathematical skills. It
does not verify any particular equation in the maintained book. The application
to an actual response-memory closure therefore remains conditional on matching
its equations to the hypotheses below.

The conclusion is positive for every fixed time horizon under uniform
regularity and stability bounds. A compact latent space and a fixed continuous
data map give a finite sample count independent of the number of observed
samples. A Lipschitz map and a quantitative latent covering bound give an
explicit count. Neither the latent coordinates nor their inverse are needed
to construct the weighted subset. Low latent dimension alone does not supply
the required numerical regularity constants or all-time trajectory stability.

## 1. Data, metric, and the retained object

There are \(m\geq1\) observed pairs \((x_a,y_a)\), with
\(x_a\in\mathbb R^d\) and \(y_a\in\mathbb R^r\). Define

\[
u_a=\frac{x_a}{\sqrt d},\qquad s_a=(u_a,y_a),\qquad
d_S((u,y),(v,w))=\|u-v\|_2+\|y-w\|_2.
\]

The factor \(1/\sqrt d\) is a declared input normalization for this route.
An application with another normalization must replace it consistently in the
metric and in every data regularity constant. It is not a change to that
application's training equations.

The empirical measure and the proposed weighted subset are

\[
\mu_m=\frac1m\sum_{a=1}^m\delta_{s_a},\qquad
\nu_M=\sum_{j=1}^M p_j\delta_{s_{a_j}},
\quad p_j>0,\quad \sum_{j=1}^M p_j=1.
\]

Here \(\delta_s\) denotes a unit point mass at \(s\). The retained pairs must
be observed pairs. The coefficients \(p_j\) are computed from the observed
sample counts, before running the reference trajectory. There is no access to
future states, latent coordinates, or latent labels beyond the observed data.

For a metric space \(Z\), let \(N_Z(h)\) be the smallest number of closed
balls of radius \(h>0\), with centers in \(Z\), that cover \(Z\). Suppose

\[
s_a=\Phi(z_a),\qquad z_a\in Z,
\qquad d_S(\Phi(z),\Phi(z'))\leq L_\Phi d_Z(z,z').
\]

The map \(\Phi\), its values away from the observed points, and \(z_a\) need
not be known to the compression algorithm. A quantitative hypothesis is

\[
N_Z(h)\leq C_Z\max\{1,(R_Z/h)^k\},\qquad h>0,
\tag{1}
\]

where \(C_Z\geq1\), \(R_Z>0\), and \(k>0\) are fixed geometric bounds.
Calling \(Z\) merely a compact \(k\)-dimensional space does not imply (1)
with specified constants. For example, if \(Z\subset[0,D]^k\) has the
Euclidean metric, a grid of cubes of side \(h/\sqrt k\), and a point of
\(Z\) from each occupied cube, gives

\[
N_Z(h)\leq \max\{1,\lceil D\sqrt k/h\rceil\}^{k}.
\]

For \(L_\Phi=0\), all pairs coincide and one representative is exact. Assume
\(L_\Phi>0\) in expressions that divide by it.

## 2. An observed-data construction

Fix \(\delta>0\). Read the pairs once. Retain the first point. For each new
point, assign it to any existing representative at distance at most
\(\delta\), incrementing that representative's count. If none exists, retain
the new point as a representative with initial count one. Let \(c(a)\) be the
representative index assigned to sample \(a\), and let

\[
p_j=\frac{\#\{a:c(a)=j\}}m.
\]

The representatives never move, so the algorithm directly certifies

\[
d_S(s_a,s_{a_{c(a)}})\leq\delta\quad\hbox{for every }a.
\tag{2}
\]

Different representatives have distance strictly greater than \(\delta\).
Cover \(Z\) by balls of radius \(\delta/(2L_\Phi)\). Two data points whose
latent points lie in the same ball have image distance at most \(\delta\).
Consequently each ball contains at most one retained representative, and

\[
M\leq\min\{m,N_Z(\delta/(2L_\Phi))\}
\leq\min\left\{m,
C_Z\max\{1,(2L_\Phi R_Z/\delta)^k\}\right\}.
\tag{3}
\]

This proof does not require the algorithm to find the latent ball containing
a sample. The latent cover only bounds the number of mutually separated
observed representatives.

An explicit coupling of the two empirical measures is

\[
\pi=\frac1m\sum_{a=1}^m
\delta_{(s_a,s_{a_{c(a)}})}.
\]

It has marginals \(\mu_m\) and \(\nu_M\), maximum transport distance at
most \(\delta\), and mean transport distance

\[
D_m=\frac1m\sum_a d_S(s_a,s_{a_{c(a)}})\leq\delta.
\tag{4}
\]

In particular, their 1-Wasserstein distance, defined as the infimum of mean
transport distance over couplings, is at most \(D_m\). For any vector-valued
function \(g\) satisfying
\(\|g(s)-g(t)\|\leq Kd_S(s,t)\), direct subtraction under this coupling gives

\[
\left\|\int g\,d\mu_m-\int g\,d\nu_M\right\|
\leq\frac1m\sum_a\|g(s_a)-g(s_{a_{c(a)}})\|
\leq KD_m.
\tag{5}
\]

Variable masses are part of the construction. Replacing the \(p_j\) by
\(1/M\) changes the sampled distribution: two well-separated clusters of
masses \(0.99\) and \(0.01\) would instead both receive mass \(0.5\).

For a fixed continuous map \(\Phi\) on compact \(Z\), the same proof uses
its uniform modulus of continuity. If

\[
\omega_\Phi(h)=
\sup_{d_Z(z,z')\leq h}d_S(\Phi(z),\Phi(z')),
\qquad \omega_\Phi(h)\longrightarrow0\quad(h\downarrow0),
\]

choose \(h\) with \(\omega_\Phi(2h)\leq\delta\); then
\(M\leq N_Z(h)\). This gives a finite cap for every fixed map and accuracy,
but no numerical cap from \(k\) alone. If the map is Hölder with
\(\omega_\Phi(h)\leq L_\Phi h^\alpha\), the count from (1) is at most

\[
C_Z\max\left\{1,
\left[2R_Z(L_\Phi/\delta)^{1/\alpha}\right]^k\right\}.
\]

The construction has worst-case arithmetic cost
\(O(mM(d+r))\) using direct distance comparisons. It can store only the
representatives and counts, using \(O(M(d+r+1))\) scalar or integer slots;
storing the full assignment map \(c\) is optional. Exact counts require
\(O(\log m)\) bits each. Thus the claim is a sample-count or scalar-storage
cap, not a literal bit bound independent of \(m\), and it does not remove
the initial cost of reading all \(m\) pairs.

## 3. A finite-horizon theorem for a common state

Suppose the reference and compressed systems have a common state space
\(\mathbb R^P\), common initial state \(\theta_0\), and equations

\[
\dot\theta(t)=F_{\mu_m}(\theta(t)),\qquad
\dot{\widetilde\theta}(t)=F_{\nu_M}(\widetilde\theta(t)),\qquad
F_\mu(\theta)=\int G(\theta;s)\,\mu(ds).
\tag{6}
\]

Assume both solutions exist on \([0,T]\) and remain in a set on which,
uniformly in \(s,t\) and the displayed states,

\[
\begin{aligned}
\|G(\theta;s)-G(\vartheta;s)\|&\leq\Lambda\|\theta-\vartheta\|,\\
\|G(\theta;s)-G(\theta;t)\|&\leq Kd_S(s,t),
\end{aligned}
\qquad \Lambda,K\geq0.
\tag{7}
\]

The set and constants must be specified independently of \(m\) to obtain
a bound uniform in \(m\). If they are obtained from a trajectory tube, both
solutions must be known to remain in that tube; closeness is not itself a
proof of this premise without a separate exit argument.

Insert and subtract \(F_{\mu_m}(\widetilde\theta)\) in (6). The first
inequality in (7) controls the state difference; (5) controls the change of
measure. For \(e(t)=\|\theta(t)-\widetilde\theta(t)\|\), its upper right
derivative satisfies

\[
D^+e(t)\leq\Lambda e(t)+KD_m,\qquad e(0)=0.
\]

Multiplication by \(e^{-\Lambda t}\), followed by integration, gives

\[
\sup_{0\leq t\leq T}e(t)\leq KD_m\psi_\Lambda(T),\qquad
\psi_\Lambda(T)=
\begin{cases}
(e^{\Lambda T}-1)/\Lambda,&\Lambda>0,\\
T,&\Lambda=0.
\end{cases}
\tag{8}
\]

For a target state error \(\varepsilon>0\), taking
\(\delta=\varepsilon/[K\psi_\Lambda(T)]\), when the denominator is positive,
and combining (3) and (8) yields

\[
M\leq\min\left\{m,
C_Z\max\left\{1,
\left[\frac{2L_\Phi R_ZK\psi_\Lambda(T)}\varepsilon\right]^k
\right\}\right\}.
\tag{9}
\]

If the denominator vanishes, the common state is unaffected by this measure
approximation on the stated interval. For an observable
\(A(\theta;s)\) Lipschitz in state with constant \(L_A\) and in data with
constant \(K_A\), the same assignment gives

\[
\left\|\int A(\theta(t);s)d\mu_m(s)
-\int A(\widetilde\theta(t);s)d\nu_M(s)\right\|
\leq L_A e(t)+K_A D_m.
\tag{10}
\]

The normalized empirical average in (6) matters. If the intended equation
uses an unnormalized sum, the change-of-measure error and/or the physical-time
stability constants can scale with \(m\). A uniform claim must retain the
model's actual mobility and normalization; a time rescaling cannot be left
implicit.

As an illustration, for a scalar predictor \(f_\theta(u)\), residual
\(r_\theta(u,y)=f_\theta(u)-y\), and squared loss

\[
\mathcal L_\mu(\theta)=\frac12\int r_\theta(u,y)^2\,\mu(du,dy),
\]

gradient flow has
\(G(\theta;(u,y))=-r_\theta(u,y)\nabla_\theta f_\theta(u)\).
On a common state tube assume
\(|f_\theta|\leq B_f\), \(|y|\leq B_y\),
\(\|\nabla_\theta f_\theta\|\leq B_J\), and input-Lipschitz constants
\(L_f,L_J\) for \(f_\theta\) and \(\nabla_\theta f_\theta\).
Subtracting the two products gives the valid data constant

\[
K=\max\{B_JL_f+(B_f+B_y)L_J,\ B_J\}.
\]

If the parameter Hessian of \(f_\theta\) has operator norm at most \(B_H\)
on a convex state tube, differentiating the gradient gives
\(\Lambda=B_J^2+(B_f+B_y)B_H\). These assumptions are an explicit
sufficient condition, not a claimed uniform estimate for arbitrary neural
networks or a verification of a response-memory model. They may fail for
nonsmooth activations or grow with other model scales.

## 4. A theorem that also compresses per-sample states

Equation (6) alone does not justify removing sample-indexed memory states.
The following second theorem addresses that issue for a stated interaction
form. Each training pair has a state \(U_a(t)\in\mathbb R^p\), with fixed
dimension \(p\), and evolves by

\[
\dot U_a
=B(U_a,s_a)+\frac1m\sum_{b=1}^m
H(U_a,s_a,U_b,s_b),\qquad U_a(0)=U_0(s_a).
\tag{11}
\]

The weighted representative system is

\[
\dot{\widetilde U}_j
=B(\widetilde U_j,s_{a_j})+
\sum_{i=1}^M p_i
H(\widetilde U_j,s_{a_j},\widetilde U_i,s_{a_i}),\qquad
\widetilde U_j(0)=U_0(s_{a_j}).
\tag{12}
\]

It is autonomous once the representatives, weights, and initial states are
stored. Suppose both systems exist on \([0,T]\) and, on their common
state/data region,

\[
\begin{aligned}
\|B(U,s)-B(V,t)\|
&\leq L_B\|U-V\|+K_Bd_S(s,t),\\
\|H(U,s,U',s')-H(V,t,V',t')\|
&\leq L_1\|U-V\|+L_2\|U'-V'\|\\
&\quad+K_1d_S(s,t)+K_2d_S(s',t'),\\
\|U_0(s)-U_0(t)\|&\leq L_0d_S(s,t).
\end{aligned}
\tag{13}
\]

All constants are nonnegative and independent of \(m\). Introduce only for
this estimate

\[
\Lambda=L_B+L_1+L_2,\qquad K=K_B+K_1+K_2,
\qquad E(t)=\frac1m\sum_a\|U_a(t)-\widetilde U_{c(a)}(t)\|.
\]

The compressed interaction in the equation for \(\widetilde U_{c(a)}\)
can be written exactly as

\[
\frac1m\sum_b
H(\widetilde U_{c(a)},s_{a_{c(a)}},
\widetilde U_{c(b)},s_{a_{c(b)}}),
\]

because \(p_i\) is the fraction of original samples assigned to \(i\).
Thus, for \(e_a=\|U_a-\widetilde U_{c(a)}\|\) and
\(d_a=d_S(s_a,s_{a_{c(a)}})\), (13) gives

\[
D^+e_a\leq(L_B+L_1)e_a+L_2E+(K_B+K_1)d_a+K_2D_m.
\]

Averaging yields \(D^+E\leq\Lambda E+KD_m\), with
\(E(0)\leq L_0D_m\). Integrating as above proves

\[
\sup_{0\leq t\leq T}E(t)
\leq D_m\left[L_0e^{\Lambda T}+K\psi_\Lambda(T)\right].
\tag{14}
\]

Because every \(d_a\leq\delta\), the identical calculation for the maximum
over \(a\) proves the stronger pointwise lifted bound

\[
\sup_{0\leq t\leq T}\max_a
\|U_a(t)-\widetilde U_{c(a)}(t)\|
\leq\delta\left[L_0e^{\Lambda T}+K\psi_\Lambda(T)\right].
\tag{15}
\]

An averaged observable Lipschitz in \(U\) and \(s\), with constants
\(L_A,K_A\), has error at most \(L_AE(t)+K_AD_m\). Consequently the
appropriate choice in (3) for its target error \(\varepsilon\) is

\[
\delta=
\frac{\varepsilon}
{L_A[L_0e^{\Lambda T}+K\psi_\Lambda(T)]+K_A},
\tag{16}
\]

provided the denominator is positive. For state error, use (16) with
\(L_A=1\) and \(K_A=0\).

The moving state count is \(Mp\), with fixed data storage
\(M(d+r)\) plus weights. A dense implementation of (12) can still cost
\(O(M^2)\) interactions per evaluation. There is no width, input-dimension,
memory-order, or coefficient-storage reduction hidden in this sample theorem.
If a particular model does not have (11), its exact dependence on empirical
averages must be exhibited and estimated separately. Products of averages,
global states, or nested layer recursions can admit extensions, but they are
not covered merely by naming them interactions.

## 5. What the latent premise does and does not buy

**Unknown coordinates and self-intersections.** The construction uses only
\(s_a=(x_a/\sqrt d,y_a)\) and their distances. It therefore works when the
latent coordinates are unknown and when \(x(z)\) is non-injective. If two
latent points have the same input but substantially different labels, the
joint metric keeps them apart. A cover based only on inputs cannot use this
argument unless labels, or the relevant sample gradient, are additionally
controlled as functions of inputs.

**Unseen inputs.** The training coreset is not a latent-coordinate recovery
algorithm. The example \(Z=[0,1]\), \(x(z)=0\), \(y(z)=z\) is continuous
and Lipschitz but makes the latent label unknowable from the input alone.
Where the model retains a predictor \(f_\theta(x)\) that is evaluable on
new inputs, it can evaluate that predictor without a latent inverse. If
\(f_\theta(x)\) is uniformly \(L_f^{\mathrm{par}}\)-Lipschitz in \(\theta\)
on a specified query domain, (8) implies prediction error at a fixed query
input at most \(L_f^{\mathrm{par}}e(t)\). A reduction that retains only
training-sample states must separately define and justify its query rule;
(15) alone does not provide arbitrary unseen-input predictions. Nor do these
deterministic empirical bounds imply population generalization.

**Dimension without a modulus.** A continuous polygonal curve from
\([0,1]\) can visit \(N\) orthonormal vectors in \(\mathbb R^N\). Its
latent dimension is one, latent diameter is one, and image norm is one, but
its image contains \(N\) points at mutual distance \(\sqrt2\). For empirical
data consisting of those points and \(\delta<\sqrt2\), the greedy
construction retains all \(N\). Its Lipschitz constant grows with \(N\),
as the curve must traverse a total length \((N-1)\sqrt2\) in unit time.
Thus latent dimension alone supplies no dimension-free entropy cap; even
when ambient dimension is fixed, no latent \(\delta^{-k}\) rate follows
without a controlled map modulus. Ambient compactness can still give its own
dimension-dependent covering bound. This example attacks the covering route's
uniform complexity, not every possible model-specific coreset.

**Noise.** If the observed pairs are within joint distance \(\eta\) of a
Lipschitz latent image, points with latent coordinates in a radius-\(h\)
ball can differ by at most \(2L_\Phi h+2\eta\). For the observed greedy
cover, when \(\delta>2\eta\), the same counting argument gives

\[
M\leq N_Z\left(\frac{\delta-2\eta}{2L_\Phi}\right).
\]

Below this noise scale, low latent dimension alone no longer controls the
observed-pair cover: the noise directions can occupy the full ambient space.
Unbounded noise also gives no uniform deterministic bound on the maximum
sample distance. Average-transport or probabilistic guarantees might tolerate
such noise, but require additional distributional assumptions and are not
proved here. The deterministic theorems approximate the actual empirical
training flow, including its observed labels; replacing noisy labels by
unobserved noiseless labels would be a different target.

**Finite horizon versus all time.** Bounds (8), (14), and (15) hold on a
specified finite horizon. The scalar equations \(\dot\theta=0\) and
\(\dot{\widetilde\theta}=\delta\), initialized at zero, have uniformly
\(\delta\)-close vector fields but error \(\delta t\), so field accuracy
alone cannot give an all-time trajectory estimate. If one can instead prove
a contraction estimate

\[
D^+E\leq-\gamma E+KD_m,\qquad\gamma>0,
\]

then direct integration gives

\[
E(t)\leq e^{-\gamma t}E(0)
+\frac{KD_m}{\gamma}(1-e^{-\gamma t}),
\]

which is uniform for all time while its assumptions hold. Such contraction
is an extra hypothesis; it does not follow from compact latent geometry,
small training loss, or continuity of the data map. A nonexpansive estimate
with an integrable-in-time compression forcing could also suffice, but that
integrability would need its own proof.

## 6. Optional square-loss refinement using synthetic mean labels

For ordinary gradient flow of the scalar square loss, an input-only cover can
replace the joint cover if synthetic labels are permitted. This is a different
retained object from the observed-pair subset in Sections 1–5.

Cluster the normalized inputs so that
\(\|u_a-u_{a_{c(a)}}\|_2\leq h\), where \(h>0\). For each cluster retain
its observed representative input, its empirical mass \(p_j\), and its mean
label

\[
\overline y_j=
\frac{1}{\#\{a:c(a)=j\}}\sum_{a:c(a)=j}y_a.
\]

If \(u(z)\) is \(L_u\)-Lipschitz on \(Z\), the same greedy argument gives
\(M\leq N_Z(h/(2L_u))\), with the constant-map case handled separately.
Labels can vary arbitrarily within an input cluster. Define

\[
\overline Y_m=\frac1m\sum_a|y_a|,
\qquad J_\theta(u)=\nabla_\theta f_\theta(u).
\]

Under the half-square-loss normalization already used above, the full field
and the mean-label field are

\[
\begin{aligned}
F_{\mu_m}(\theta)
&=\frac1m\sum_a[-f_\theta(u_a)J_\theta(u_a)+y_aJ_\theta(u_a)],\\
\widetilde F(\theta)
&=\sum_jp_j[-f_\theta(u_{a_j})J_\theta(u_{a_j})
+\overline y_jJ_\theta(u_{a_j})]\\
&=\frac1m\sum_a[-f_\theta(u_{a_{c(a)}})J_\theta(u_{a_{c(a)}})
+y_aJ_\theta(u_{a_{c(a)}})].
\end{aligned}
\]

The last identity is exact because the gradient field is affine in the label.
Assume, uniformly on the common state region, that the maps
\(u\mapsto f_\theta(u)J_\theta(u)\) and \(u\mapsto J_\theta(u)\) have
Lipschitz constants \(L_{fJ}\) and \(L_J\). Termwise subtraction gives

\[
\|F_{\mu_m}(\theta)-\widetilde F(\theta)\|
\leq h(L_{fJ}+L_J\overline Y_m).
\tag{17}
\]

The earlier predictor assumptions supply
\(L_{fJ}\leq B_JL_f+B_fL_J\). If the state Lipschitz constant is
\(\Lambda\), (8) therefore applies with forcing
\(h(L_{fJ}+L_J\overline Y_m)\). A uniform first absolute label moment
\(\overline Y_m\leq\overline Y\) suffices for this field error and, with
the Hessian bound from Section 3, the full averaged field has state Lipschitz
constant at most
\(B_J^2+(B_f+\overline Y)B_H\). No Lipschitz relation between input and label
is needed. For the unhalved loss \(m^{-1}\sum_a(f_\theta(u_a)-y_a)^2\), both
gradient-field constants have the additional factor two.

When all inputs within a cluster are identical, the gradient contribution of
that cluster is preserved exactly. Its loss differs from the mean-label loss
by the parameter-independent quantity

\[
\frac1{2m}\sum_a
(y_a-\overline y_{c(a)})^2.
\]

This scalar can be stored if exact loss reconstruction at the representative
inputs is required. With nonidentical inputs the preceding identity applies
to the dataset in which inputs have first been replaced by their cluster
representatives; (17) bounds the resulting gradient error for the original
dataset. The refinement is specific to the affine label dependence of this
gradient field. It does not automatically commute with nonlinear
sample-dependent memory equations and does not prove an all-time estimate.

## 7. Exact remaining bridge to a particular closure

The weighted subset and transport estimate are unconditional under the stated
data geometry. The trajectory conclusion requires the reference equations to
fit (6) or (11), or a separately proved generalization, with a common
well-posed state region and constants uniform in \(m\). In particular, any
sample-indexed initialization, fixed random features, normalization factors,
and reconstructed coefficients must be Lipschitz in the declared observed
pair metric with explicit constants. This is a genuine proof obligation,
not supplied by the existence of a compact latent space. No experimental,
population, or all-time claim is established by this note.
