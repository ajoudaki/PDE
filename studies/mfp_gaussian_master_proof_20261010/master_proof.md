# A Gaussian calculus for fixed finite derivative programs

Status: complete proof for the stated finite-program language, internally checked by two fresh independent reconstructions. This is a study result, not a promoted book theorem.

## 1. Statement and exact scope

Fix finitely many vector types, each represented by R^n, and finitely many named matrices between distinct specified types. Each initialized matrix has independent N(0,1/n) entries; different initialized matrices are independent. Reusing a transpose means using the transpose of that same initialized matrix. For each vector type there is a fixed finite Gaussian root tuple, sampled independently over neuron indices. Root tuples in distinct types and all initialized matrices are independent. Fixed deterministic constants and constant vectors are allowed. Root Gaussian laws may be singular.

A primitive program is a finite acyclic list with scalar and typed vector variables. Its instructions are:

1. coordinate maps v_i=F(u_i^1,...,u_i^k;s_1,...,s_q), with all vector inputs of the output type;
2. normalized averages s=n^{-1}sum_i F(u_i^1,...,u_i^k;t_1,...,t_q);
3. scalar sums and products;
4. calls Wu and W^T v to named initialized matrices, with their declared types.

Every F is a finite expression made from its arguments, fixed real constants, sums, products, and phi^(r), r>=0. Here phi is C-infinity and, for each r, |phi^(r)(x)| <= C_r(1+|x|)^{d_r}. All dimensions other than n, all program lengths, all expressions and all coefficients are fixed before n tends to infinity. Initial scalars are deterministic. There are no inverses, width-dependent coefficients, coordinate selection operations, or additional tensor contractions.

Matrix states of the form

\[
A=W_0+\sum_{\nu=1}^M c_\nu u_\nu v_\nu^T/n
\]

and pure sums of their rank-one terms are notation for the exact primitive expansions

\[
Ah=W_0h+\sum_\nu c_\nu u_\nu(v_\nu^Th/n),\qquad
A^Tu=W_0^Tu+\sum_\nu c_\nu v_\nu(u_\nu^Tu/n).
\tag{1}
\]

The derivative extension admits finite-dimensional input/constant-parameter derivatives, fixed-order directional derivatives with vector directions given by programs and matrix directions given by finite sums c uv^T/n, scaled ambient gradients (mobility n on trainable vector roots and mobility 1 on trainable matrices, with fixed block multipliers), their repeated directional derivatives, fixed numbers of gradient updates, and fixed-order gradient-flow jets. Derivatives of a sampling law are not an extra primitive. A single Frechet directional derivative freezes its directions; repeated vector-field differentiation differentiates their state dependence. No unrestricted dense matrix direction or unrestricted tensor-index sum is included.

An observable O_n is a scalar output of this derivative language. Vector outputs are described through their joint empirical laws and normalized averages, not through convergence of individual neurons to constants.

**Theorem.** Every such derivative program compiles exactly, at each finite n, into a finite primitive program. The source-response construction in Section 2 terminates and gives an explicit finite Gaussian-expectation DAG with deterministic scalar output O_* such that, for every finite p>=1,

\[
\mathbb E|O_n-O_*|^p\longrightarrow0.
\tag{2}
\]

For every vector node v_n and scalar node s_n, and every finite p,q>=1,

\[
\sup_n\mathbb E\left(\frac1n\sum_i|v_{n,i}|^p\right)^q<\infty,
\qquad \sup_n\mathbb E|s_n|^q<\infty.
\tag{3}
\]

The claims hold jointly for finitely many programs sharing roots and matrices. No rank-stability or nonsingularity assumption is imposed. For the initialization subclass specified in Section 8, the DAG reduces to a polynomial in recursively computed Gaussian activation-derivative moments.

This theorem is about the declared language. It does not assert convergence of an infinite Taylor series, positive-time reconstruction from jets, uniformity in growing depth/update count/order, arbitrary parameter-tensor contractions, or depth-linear compilation complexity.

## 2. The Gaussian evaluator

Give every type its own probability space. Roots have their declared Gaussian laws. A coordinate map acts on the corresponding scalar representatives and on already computed deterministic scalar values. An empirical average becomes the expectation on its type.

For a named matrix W from the lower type to the upper type, list forward calls y_r=Wh_r and reverse calls v_s=W^T u_s in program order. Write H_r,U_s,Y_r,V_s for scalar representatives. Introduce centered jointly Gaussian forward sources xi_r and reverse sources zeta_s, with

\[
\operatorname{Cov}(\xi_r,\xi_t)=\mathbb E_{\rm lower}H_rH_t,
\qquad
\operatorname{Cov}(\zeta_s,\zeta_v)=\mathbb E_{\rm upper}U_sU_v.
\tag{4}
\]

Different oriented matrix groups, including the two orientations of one matrix, are independent of one another and of the roots. Set

\[
Y_r=\xi_r+\sum_{s\text{ earlier reverse}}U_s\,
              \mathbb E_{\rm lower}[\partial_{\zeta_s}H_r],
\tag{5}
\]
\[
V_s=\zeta_s+\sum_{r\text{ earlier forward}}H_r\,
              \mathbb E_{\rm upper}[\partial_{\xi_r}U_s].
\tag{6}
\]

The partials differentiate the explicit expression in named source coordinates, holding all previously computed expectations, covariances and coefficients fixed. Unavailable coordinates have derivative zero. Derivative paths through earlier calls to other matrices remain included. Each named coordinate remains a separate formal argument when its joint Gaussian covariance is singular.

At each call the required inputs and their formal derivatives already exist. The covariance extension is an input Gram extension, hence positive semidefinite. A finite-dimensional Gaussian measure exists for every such matrix, including singular ones. Functions and all finite-order formal derivatives have polynomial growth in their finite root/source arguments, by induction. Their Gaussian expectations therefore exist. This establishes existence, causality and termination of the construction independently of its asymptotic validity.

Collecting expectation nodes gives

\[
I_j=\int F_j(g;I_1,\ldots,I_{j-1})\,
             N(0,K_j(I_1,\ldots,I_{j-1}))(dg),\qquad O_*=P(I_1,\ldots,I_N).
\tag{7}
\]

Means of Gaussian roots are included as deterministic shifts in F_j. Dimensions, integrands, coefficients and covariance entries are all determined by the finite construction. P is a polynomial because scalar outputs are assembled from averages and scalar sums/products. No inverse covariance is part of (4)-(7).

## 3. Uniform moments: the essential estimate

The argument below is the finite-entry Taylor cancellation mechanism used in Golikov and Yang, *Non-Gaussian Tensor Programs* (NeurIPS 2022), supplementary Appendix J, Lemmas J.3 and J.6. We give the needed proof explicitly. It avoids relying on a rank-stability theorem or inferring uniform integrability from weak convergence.

**Moment lemma.** Allow, temporarily, the independent entries of each named matrix to be centered independent Gaussians of possibly different variances at most 1/n. For a fixed primitive program whose coordinate/scalar maps are C-infinity with polynomially bounded partial derivatives of every order, let alpha denote any finite list of raw matrix-entry differentiation variables. For every node, every finite p>=1, and every fixed derivative order |alpha|,

\[
\sup_{n,i,\alpha:\,|\alpha|=k}
  \mathbb E|\partial^\alpha v_{n,i}|^p<\infty,
\qquad
\sup_{n,\alpha:\,|\alpha|=k}
  \mathbb E|\partial^\alpha s_n|^p<\infty.
\tag{8}
\]

The constants are uniform over the allowed variances. They depend on the fixed graph and only finitely many polynomial derivative bounds of its functions. Thus they are uniform over any family of functions having common bounds at every derivative order.

All derivatives are derivatives of the program as a function of unconstrained raw matrix entries, evaluated at the indicated random entries. This convention remains meaningful when an entry's variance is zero.

*Proof.* Prove (8), simultaneously for every p and derivative order, by induction over instructions. Fixed-n integrability is available before the induction: all values and derivatives have polynomial growth in finitely many Gaussian inputs, with constants allowed at this point to depend on n.

For roots, matrix derivatives of positive order vanish and Gaussian moments are finite. Constants are immediate. For coordinate and scalar compositions, repeated chain/product rules express a fixed-order derivative as a finite sum of products of derivatives of earlier nodes and a polynomially bounded partial derivative of the coordinate function. The number of factors and summands depends on the fixed graph and derivative order, not n. Polynomial growth and Holder's inequality bound each product using higher moments in the induction hypothesis. This includes scalar feedback. For averages, differentiation commutes with the finite sum, and

\[
\mathbb E\left|\frac1n\sum_i a_i\right|^p
\le\frac1n\sum_i\mathbb E|a_i|^p
\tag{9}
\]

applies to each differentiated integrand.

Consider a new matrix call y=Wv and a fixed coordinate i. For a list alpha of k raw-entry derivatives, the product rule gives

\[
\partial^\alpha y_i
=\sum_{j=1}^n W_{ij}\partial^\alpha v_j+R_i,
\tag{10}
\]

where R_i is a sum of at most k earlier-node derivatives, of order k-1: each nonzero term differentiates one occurrence of W_{ij} and fixes its j. A second derivative of that linear factor vanishes. Thus R_i is bounded by induction. Transpose calls have exactly the same form with the entries of a column in place of a row.

Put w_j=W_{ij} and z_j=partial^alpha v_j. It suffices to bound an even moment of sum_j w_j z_j; every other finite moment is bounded by a larger even moment. Fix an even integer p. Expansion gives ordered tuples (j_1,...,j_p). For a tuple let b be its number of distinct indices, and s the number of indices appearing exactly once. The tuple contributes

\[
\mathbb E\left[\left(\prod_{a=1}^p w_{j_a}\right)
                         \left(\prod_{a=1}^p z_{j_a}\right)\right].
\tag{11}
\]

We show its absolute value is at most C n^{-b}, uniformly over the tuple and n.

Here is a mixed finite-difference version of Taylor cancellation, which also handles s=0. Let S be the set of singleton indices, M the weight product in (11), and Z the product of z's. For u in S set Delta_u Z=Z-Z|_{w_u=0}. Expanding the commuting difference operators gives E[MZ]=E[M(prod_{u in S}Delta_u)Z]: every other term leaves some singleton weight appearing only in its centered linear factor, independently of the other factors, and its expectation vanishes. Repeated use of the fundamental theorem of calculus gives the exact identity

\[
\mathbb E[MZ]=\int_{[0,1]^s}
 \mathbb E\left[M\left(\prod_{u\in S}w_u\right)
       (\partial_S Z)(W^{(t)})\right]dt.
\tag{12}
\]

The notation W^(t) means the entire raw input array with each singleton entry w_u replaced by t_u w_u, consistently in every reuse and transpose. Empty products and a zero-dimensional integral cover s=0.

The squared moment of M prod_{u in S}w_u is at most C n^{-(p+s)}, by Gaussian moments (or Holder). The factor (partial_S Z)(W^(t)) has bounded second moment uniformly in t,n and the selected indices. Indeed its product-rule expansion uses only derivatives of the earlier node v. The modified entries remain independent centered Gaussians with variances at most 1/n, so the strengthened induction hypothesis applies uniformly. Differentiate the deterministic program in its raw coordinates first, then evaluate the derivative at W^(t). This is not the derivative of the composed map W -> Z(W^(t)); no extra factors t_u or division by t_u occurs, including at t_u=0. Fixed-n polynomial integrability justifies the centering and integral exchanges in (12).

Cauchy-Schwarz and integration in t now bound (11) by C n^{-(p+s)/2}. Counting multiplicities gives

\[
p\ge s+2(b-s)=2b-s,
\]

so again the bound is C n^{-b}.

There are at most C_p n^b tuples of any fixed equality pattern with b distinct indices, and finitely many such patterns for fixed p. Summing their absolute bounds proves E|sum_j w_j z_j|^p<=C_p. This proves the matrix step and closes the induction.

All uniformity assertions follow from this same finite induction: each step uses finitely many earlier bounds, higher derivative bounds, and Gaussian moments, never a minimum variance or Gram inverse. This proves the lemma. QED.

In particular, k=0 gives uniform coordinate and scalar moments. Jensen gives

\[
\mathbb E\left(\frac1n\sum_i|v_i|^p\right)^q
\le\frac1n\sum_i\mathbb E|v_i|^{pq},
\tag{13}
\]

which proves (3).

We will also use uniform operator-norm moments of initialized matrices. A 1/4-net with at most 9^n points and a Gaussian tail bound yield

\[
\mathbb P\{\|W\|_{\rm op}>t\}
\le2\exp\{n(2\log9-t^2/8)\}\le2e^{-t^2/16}\quad(t\ge10).
\tag{14}
\]

The first inequality follows from ||W||op<=2 max_{u,v in net}|u^TWv|, where each fixed pairing is N(0,1/n). Integrating the last bound proves uniform moments of every order. A finite list of matrices and their transposes has the same property.

## 4. Bounded-derivative Gaussian program law

We need the following established Gaussian fact, including its singular case: a fixed finite program with globally Lipschitz C^1 coordinate maps having bounded continuous first derivatives has deterministic same-type empirical laws converging in W_2 in probability. Its laws are (4)-(6). Causal scalar averages and globally Lipschitz dependence on previous scalars are permitted. A proof, including the conditioning and singular-query arguments, is supplied here in the form needed below; the maintained book contains the same construction in docs/12-three-sample-learning.qmd, III.F.1-III.F.6.

**Adaptive conditioning.** After earlier observations WV=Y and W^TU=Q, condition on the entire transcript. An operation without a matrix call is measurable from that transcript. A new matrix input is therefore fixed under the conditional law. Initially the matrices are independent Gaussians; conditioning on a new linear observation of one matrix leaves the other conditional matrix factors unchanged. Induction makes adaptive queries legitimate.

Write P_V and P_U for orthogonal projections onto the column spans. If the two column Grams are invertible, Gaussian conditioning gives

\[
W\mid\mathcal H\overset d=
Y(V^TV)^{-1}V^T+
U(U^TU)^{-1}Q^TP_{V^\perp}
 +P_{U^\perp}\widetilde W P_{V^\perp},
\tag{15}
\]

with an independent copy tilde W. Indeed U^TY=Q^TV; the first two terms satisfy both observed constraints and are orthogonal, in Frobenius inner product, to every homogeneous solution P_{U^perp}KP_{V^perp}. Vectorizing an isotropic Gaussian proves (15). For dependent columns the same statement holds using minimum-norm solutions, but no continuity of these solutions will be assumed.

For a new forward input h, put

\[
\alpha_n=(V^TV)^{-1}V^Th,\quad h_\perp=h-V\alpha_n,\quad
\beta_n=(U^TU/n)^{-1}Q^Th_\perp/n.
\]

Then

\[
Wh\mid\mathcal H\overset d=
Y\alpha_n+U\beta_n+
\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g,
\tag{16}
\]

where g is an independent standard Gaussian vector. Reverse calls exchange the two sides.

**Positive limiting Grams.** Suppose first that all query Grams have positive definite limits. Induct on the transcript. The iid root empirical law converges in W_2 in probability: the weak law applies to bounded continuous tests and to squared norms; finite second moments suffice, by truncation. A countable determining family of tests and tightness give weak convergence, and convergence of second moments upgrades it to W_2.

At a matrix call, all coefficients and the variance in (16) converge, since normalized inner products converge and inversion is continuous at a positive definite fixed-size matrix. The removed Gaussian projection is negligible because

\[
\mathbb E[\|P_Ug\|_2^2/n\mid\mathcal H]=\operatorname{rank}(U)/n.
\]

The new coordinate is thus, up to vanishing empirical mean-square error, a fixed linear combination m_i of earlier same-type coordinates plus sigma g_i. Conditional on the transcript, empirical bounded test averages have variance at most C/n. Their conditional means are earlier empirical averages of the bounded continuous Gaussian-smoothed test and therefore converge. The second-moment identity

\[
\frac1n\sum_i(m_i+\sigma g_i)^2
=\frac{\|m\|_2^2}{n}+\frac{2\sigma}{n}\sum_i m_ig_i
 +\frac{\sigma^2}{n}\sum_i g_i^2
\]

gives convergence of second moments: the middle term has conditional variance 4 sigma^2||m||_2^2/n^2. Coordinate maps preserve W_2 convergence by their global Lipschitz bound. Scalar averages converge by their at-most-linear growth. Dependence on preceding scalar values is handled by replacing those values by their deterministic limits: the Lipschitz bound controls the resulting normalized vector error by the scalar error. This closes the induction.

**Identification of the response.** In the limiting version of (16), denote the old forward inputs by H_r, reverse inputs by U_s, and their answers by Y_r,V_s. Inductively let

\[
Y_r=\xi_r+\sum_s D_{rs}U_s,\qquad
D_{rs}=\mathbb E[\partial_{\zeta_s}H_r].
\]

For a new input H, let alpha be its L^2 projection coefficients onto the old H_r and H_perp=H-sum_r alpha_r H_r. Each old V_s is zeta_s plus a deterministic linear combination of earlier forward inputs, so

\[
\mathbb E[V_sH_\perp]=\mathbb E[\zeta_sH_\perp].
\]

Gaussian integration by parts, with C_st=E[U_sU_t], yields

\[
\mathbb E[\zeta H_\perp]=C\,\mathbb E[\nabla_\zeta H_\perp].
\]

The limiting beta in (16) is therefore E[nabla_zeta H]-sum_r alpha_r E[nabla_zeta H_r]. On substituting the old Y_r, the second term cancels. This is (5); the remaining Gaussian source has cross-covariance E[HH_r] and variance E[H^2]. The same calculation gives (6). Integration by parts is justified by at-most-linear growth and bounded source derivatives. Independence of distinct oriented source groups follows inductively by adjoining independent conditional innovations. This construction specifies source covariance, not independence of actual matrix outputs.

**Singular limiting Grams.** Add a fresh independent standard Gaussian root chi before each call and perturb that call's input by epsilon chi. For each fixed epsilon>0, the new input's normalized squared distance to the span of its prior same-orientation inputs has limit at least epsilon^2. In detail, the cross term has conditional variance at most 4 epsilon^2||h||_2^2/n^2, while ||P_{V^perp}chi||_2^2/n tends to 1 because rank V is bounded. Inductively every query Gram is positive definite, so the preceding argument applies.

Couple the perturbed and original programs using the same original roots and matrices. On an event with probability tending to one, all matrix operator norms are at most 10 and all new roots have RMS at most 2. The finite Lipschitz instruction list, including scalar averages/feedback, propagates an O(epsilon) error in each vector RMS and scalar absolute value. The constant depends on the fixed list, not n or epsilon<=1.

The scalar construction itself is continuous as epsilon decreases to zero. Inductively its coefficients converge. Its source covariance matrices converge entrywise by dominated convergence, and their positive semidefinite square roots converge even at rank loss. For completeness, bounded square roots have convergent subsequences; any subsequential limit is positive semidefinite and squares to the limiting matrix, whose positive semidefinite square root is unique. Couple each finite source prefix by these square roots applied to standard Gaussians. Node functions have uniform linear growth and bounded first source derivatives for coefficient lists in a compact set. Dominated convergence therefore passes both input Grams and expected source derivatives to the zero-noise formulas (4)-(6).

The triangle inequality for W_2, using the coordinatewise finite-width coupling, now proves the original program's convergence: first let n tend to infinity for fixed epsilon, then epsilon tend to zero. No inverse Gram estimate is used in this removal step. This proves the bounded-derivative law.

## 5. Remove coordinate clipping uniformly in width

The preceding law will be applied to the already differentiated primitive program. Clipping is a proof device applied after derivative compilation; no derivative of a clipped network is substituted for a derivative of the actual network.

For every coordinate or scalar map F choose a smooth cutoff chi equal to 1 on the unit ball and zero outside the ball of radius 2, and put F_B(x)=chi(x/B)F(x), B>=1. Include scalar arguments among the arguments being cut off. Scalar additions/products may be clipped in the same manner. For a zero-argument constant leave it unchanged.

Each F_B is globally Lipschitz and has bounded continuous derivatives of every order. For each fixed derivative order, its polynomial growth bound can be chosen independently of B: the product rule gives factors B^{-j}(D^j chi)(x/B) times a derivative of F, and B^{-j}<=1. Moreover F_B converges to F with every derivative on compact sets.

The moment lemma consequently applies uniformly in both n and B to every node of the original and clipped programs. We claim, for corresponding vector and scalar nodes,

\[
\lim_{B\to\infty}\sup_n\mathbb E\frac1n\sum_i|v_{n,i}-v_{n,i}^{B}|^2=0,
\qquad
\lim_{B\to\infty}\sup_n\mathbb E|s_n-s_n^B|^2=0.
\tag{17}
\]

Here and below the root/matrix samples are coupled identically.

We spell out the induction, including the needed higher moments. Regard a vector value as a random variable under the product of the original probability measure with uniform measure on its neuron index. The moment lemma gives uniformly bounded moments of every order under this probability measure. If a difference tends to zero in L^2 there, interpolation with a uniformly bounded higher moment makes it tend to zero in every fixed finite L^p. The interpolation constants do not depend on n. Scalar differences have the identical property; a scalar can be broadcast over the neuron index.

For a coordinate operation, the mean-value theorem and polynomial growth of first derivatives give

\[
|F(x)-F(y)|\le C(1+|x|+|y|)^d|x-y|.
\tag{18}
\]

Split F(x)-F_B(y) as F(x)-F(y)+F(y)-F_B(y). The first term tends to zero in joint L^2 by Holder, the induction hypothesis upgraded to L^4, and uniform higher moments of x,y. The second is at most C(1+|y|)^d 1_{|y|>B}; every higher moment of y is bounded uniformly. Its L^2 norm therefore tends to zero uniformly in n,B by a power tail bound. This proves the coordinate step, including scalar inputs. The same argument and Jensen prove the average and scalar-operation steps.

For a matrix call with input error e,

\[
\mathbb E\frac{\|We\|_2^2}{n}
\le (\mathbb E\|W\|_{\rm op}^4)^{1/2}
       \left[\mathbb E\left(\frac{\|e\|_2^2}{n}\right)^2\right]^{1/2}
\le C\left(\mathbb E\frac1n\sum_i|e_i|^4\right)^{1/2}\longrightarrow0.
\tag{19}
\]

This requires no independence of W and e. Equation (14), interpolation, and the previous step justify the last limit. Transposes obey the same estimate. Roots have zero error. This proves (17) for the entire finite list, including causal scalar feedback.

## 6. Identify the limit and obtain Lp convergence

For each fixed B the bounded-derivative law gives scalar output convergence O_n^B -> O_*^B in probability, where O_*^B is evaluated by (4)-(6) with the clipped maps.

The clipped Gaussian evaluator converges to the unclipped one:

\[
O_*^B\longrightarrow O_*.
\tag{20}
\]

Here is the required domination argument. Induct over the finite evaluator. Earlier coefficients that converge remain bounded. At a new step all node expressions and every finite number of their formal source derivatives have polynomial bounds in the named roots/sources, uniformly over B, because the F_B have common derivative profiles. The input Gram entries and response coefficients are Gaussian expectations of these expressions. Couple a finite source prefix through the positive semidefinite covariance square roots. If earlier covariances converge, these square roots converge and remain bounded. Thus the functions of the fixed standard Gaussian roots converge pointwise and have a common polynomial envelope. Gaussian dominated convergence gives convergence of every needed expectation and every fixed moment of the fields. This extends the covariance and coefficient induction, proves (20), and never differentiates a covariance square root.

For eta>0, choose B so that |O_*^B-O_*|<eta/3. Then

\[
\mathbb P\{|O_n-O_*|>\eta\}
\le \mathbb P\{|O_n-O_n^B|>\eta/3\}
 +\mathbb P\{|O_n^B-O_*^B|>\eta/3\}.
\]

The first probability is uniformly small by (17) and Markov's inequality; the second tends to zero with n. Let B tend to infinity after taking limsup in n. Hence O_n -> O_* in probability.

Finally fix p<infinity and choose q>p. The moment lemma bounds E|O_n-O_*|^q uniformly. On {|O_n-O_*|>R}, the pth moment is at most R^{p-q} times that bound; on the complement it tends to zero by convergence in probability and boundedness (split again at an arbitrary small threshold). First n tends to infinity, then R tends to infinity. This proves (2), including expectation convergence. Applying the argument to a finite union of programs proves the joint statement.

Thus the analytical part of the theorem is unconditional under its stated hypotheses. The previously missing uniform-integrability estimate is Section 3; clipping removes the polynomial-growth and scalar-feedback difficulty without a rank-stability condition.

## 7. Exact derivative compilation and neural training

The class of C-infinity functions whose derivatives have polynomial growth is closed under finite sums, products, composition and differentiation. The product and multivariate chain rules prove this: every derivative is a finite sum of products of polynomially bounded factors; composition of polynomial bounds is polynomial. Therefore every finite expression in phi and its derivatives has the required profile.

For a jet u_[r]=(1/r!)d^r u(t)/dt^r at zero, coefficient extraction in the truncated ring R[t]/(t^{R+1}) gives

\[
(uv)_{[r]}=\sum_{a+b=r}u_{[a]}v_{[b]},\quad
(Au)_{[r]}=\sum_{a+b=r}A_{[a]}u_{[b]},
\]
\[
\phi(u)_{[r]}=[t^r]\sum_{k=0}^r\frac{\phi^{(k)}(u_{[0]})}{k!}
                  \left(\sum_{j=1}^r u_{[j]}t^j\right)^k.
\tag{21}
\]

Taylor's theorem through finite order justifies the coefficient identity for smooth functions; analyticity is not required. Averages are linear and commute with finite differentiation. Mixed jets use multivariate truncated polynomials. Differentiating a finite sum of uv^T/n leaves a finite sum of such terms. Equation (1) therefore compiles all represented directional jets exactly.

For reverse differentiation of a scalar O, let b_u=n partial O/partial u for vector nodes and a_s=partial O/partial s for scalars. Initialize a_O=1 and all other adjoints to zero; visit instructions in reverse order and accumulate every use. A coordinate map v=F(u;s) contributes

\[
b_u\mathrel{+}=b_v\odot F_u,\qquad a_s\mathrel{+}=n^{-1}\sum_i b_{v,i}F_s(u_i;s).
\tag{22}
\]

An average t=n^{-1}sum_i F(u_i;s) contributes

\[
b_u\mathrel{+}=a_tF_u,\qquad a_s\mathrel{+}=a_t n^{-1}\sum_iF_s(u_i;s).
\tag{23}
\]

There is a contribution for each argument. Scalar sums/products use their ordinary chain rules. For v=Au,

\[
b_u\mathrel{+}=A^Tb_v,\qquad \nabla_A O\mathrel{+}=b_vu^T/n;
\]

for v=A^Tu,

\[
b_u\mathrel{+}=Ab_v,\qquad \nabla_A O\mathrel{+}=ub_v^T/n.
\tag{24}
\]

These identities follow by differentiating the finite Euclidean/Frobenius differential dO. They prove exact reverse compilation, with accumulation across every repeated use of a parameter. The ambient current-parameter gradient is computed before substituting the stored representation (1), so it is not confused with a pullback to stored update factors.

A vector-root gradient multiplied by mobility n is b_u; a matrix gradient with mobility 1 is the finite sum in (24). Fixed block multipliers preserve the representation. Their contractions are explicit:

\[
n\,\nabla_u O^T\nabla_u S=b_u^Tb_u^{S}/n,
\quad
\langle uv^T/n,pq^T/n\rangle_F=(u^Tp/n)(v^Tq/n).
\tag{25}
\]

Consequently each fixed gradient update preserves (1) and the root-vector program representation. A finite update count gives a finite primitive program, even though its rank and length can grow with that fixed count.

For the book's MLP convention,

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\quad f_{n,a}=W^{(L+1)T}h_a^{(L)}/n,
\]

take independent first-weight entries N(0,1), hidden entries N(0,1/n), and stored readout entries N(0,tau^2). The columns of the first matrix and the readout are Gaussian vector roots. The data and d,m,L are fixed. With residuals r_a=f_{n,a}-y_a and loss mathcal L_n=m^{-1}sum_a r_a^2, the block mobilities n kappa_1,kappa_2,...,kappa_L,n kappa_{L+1} give the admitted gradient field V_n=-D_n grad mathcal L_n. The different small-readout model is not silently substituted here.

A smooth finite-dimensional vector field has a local solution at each finite-width state. Its finite jets are determined without any common positive existence horizon by

\[
(r+1)\theta_{[r+1]}=[t^r]V_n\left(\sum_{j=0}^{r}\theta_{[j]}t^j\right).
\tag{26}
\]

The rule differentiates all state dependence, including that of the gradient direction. For example, the second observable derivative is D^2O[V,V]+DO[DV V]. Equations (21)-(26) prove exact finite compilation for every admitted finite order. Applying Sections 3-6 after this compilation proves the claimed neural derivative and training-jet limits. No derivative/width-limit interchange is used.

## 8. Initialization activation-moment normal form

Take the ordinary feedforward MLP just specified. Construct all its original forward preactivations first. The restricted subclass consists of compiled derivative programs evaluated at initialization in which every nonlinear node has literal argument one of these original z_a^(ell)(0), and hence has the form phi^(r)(z_a^(ell)(0)). All other operations are the polynomial arithmetic, matrix calls, normalized averages and admitted contractions already specified. This is a syntactic condition on the finite differentiated graph. It does not admit arbitrary nonlinear heads or nonlinearities applied to derivative fields.

In the Gaussian evaluator each original forward preactivation is a centered Gaussian source or a linear combination of first-layer Gaussian roots: no reverse call precedes these original forward calls. Their within-layer covariance is determined by

\[
Q^{(1)}_{ab}=x_a^Tx_b/d,\qquad
Q^{(\ell+1)}_{ab}=\mathbb E_{Z\sim N(0,Q^{(\ell)})}\phi(Z_a)\phi(Z_b).
\tag{27}
\]

Original preactivations, all auxiliary roots and all later named sources form a finite joint Gaussian family. If a preactivation is a linear combination rather than a named coordinate, adjoin it for Gaussian integration with its induced covariance; singularity is harmless. Formal source derivatives continue to use the original named source arguments, so this notational augmentation does not redefine any derivative.

Inductively every symbolic field is a finite sum of

\[
c\,P(G)\prod_{\nu=1}^r\phi^{(k_\nu)}(G_{a_\nu}),
\tag{28}
\]

where P is a polynomial, the activation arguments are designated original preactivations, and c is polynomial in previously computed scalar coefficients. Original Gaussian roots with deterministic means have those means absorbed into P. The class is closed under sums, products and formal source derivatives. Equations (5)-(6) append a Gaussian source and finite linear combinations of old fields with coefficients that are expectations of fields in the same class. The covariance entries (4) are likewise expectations in that class. This proves symbolic closure.

For a centered Gaussian G of covariance K and a smooth polynomial-growth function F,

\[
\mathbb E[G_iF(G)]=\sum_jK_{ij}\mathbb E[\partial_jF(G)].
\tag{29}
\]

To justify the singular case, write G=BZ for a standard Gaussian Z and use one-dimensional integration by parts in each coordinate; polynomial growth makes the boundary terms vanish and permits Fubini. For (28), apply (29) to one factor of a Gaussian monomial. A derivative hitting the remaining polynomial reduces its degree; a derivative hitting an activation factor raises its derivative order and still removes the chosen explicit Gaussian factor. Thus induction on polynomial degree terminates and leaves finite sums of covariance monomials times atoms

\[
M_j=\mathbb E_{G\sim N(0,K_j)}
                   \prod_\nu\phi^{(r_{j,\nu})}(G_{a_{j,\nu}}).
\tag{30}
\]

Their covariances are computed in earlier steps of the same acyclic recursion. Substitution expresses O_* as a finite polynomial in these recursively computed atoms and fixed model/data constants. The reduction is finite but no complexity bound beyond finiteness is asserted. Sections 3-7 already identify this symbolic quantity with the unconditional expectation limit, completing the master theorem for the declared language. QED.

## Sources and provenance

- Maintained book: docs/index.qmd and docs/notation.qmd; complete finite Gaussian-program argument in docs/12-three-sample-learning.qmd, III.F.1-III.F.6 (lines 316-688 when read).
- Eugene Golikov and Greg Yang, *Non-Gaussian Tensor Programs*, NeurIPS 2022, Definition 3.1, Definition 3.5, Setups 3.3/3.6, Theorem 3.7; supplementary Appendix I and complete Appendix J. The elementary moment proof in Section 3 is explicitly based on their finite-entry Taylor cancellation argument, with the singleton cancellation and zero-singleton case written out. Their stronger result independently supplies all-Lp convergence for the compiled language. No novelty claim is made for the probabilistic program theorem.
- Public paper: https://papers.nips.cc/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf
- Public supplement: https://papers.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Supplemental-Conference.zip
- Downloads and text extractions are in data/generated/mfp_gaussian_master_proof_20261010/sources/; exact source hashes are recorded separately in this study.

No numerical training experiment, formal proof assistant, or book promotion is part of this argument.
