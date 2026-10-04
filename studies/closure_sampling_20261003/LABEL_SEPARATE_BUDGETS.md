# Separate sample budgets remove the Gaussian-maximum label penalty

2026-10-04. **Internally checked bounded refinement.** The independent
reconstruction in
[LABEL_SEPARATE_BUDGETS_CHECK.md](LABEL_SEPARATE_BUDGETS_CHECK.md) passed
at report SHA-256
`96f9766dc398b08b229581e64eb6590298b4ff95aaa4a7a7fac492cf29c2e059`.
That complete report was read before this status update. The independently
written author derivation had SHA-256
`82989e948e0713beb84d5fe984a29e46fadc2b757e5460d3d48ea9cce255b298`;
its proof content is preserved below. This is an internal study check,
not a promotion review or established-book result.
The carrier and complex-source arguments can use a separate empirical
exponential budget for each training sample. Their local deterministic
estimates require only these individual budgets. The union over the fixed
number of samples can be taken after the fixed-block moment estimate,
instead of inside the Gaussian exponential moment.

Consequently the full source and carrier conclusions admit the sufficient
label condition

\[
                         0<Y\le c\lambda,                \tag{1}
\]

with structural c independent of sample count. This improves the earlier
sufficient condition Y<=c lambda exp(-C sqrt(log(em))). It does not prove
that (1) is necessary or optimal, and does not remove sample count from
the width threshold or the normalized gap lambda.

The coordinator proposed the separate-budget change. This note audits and
derives its consequences using the complete explicitly assigned
DEPTH_CAVITY_ROUTE.md, DEPTH_INSERTION_CHECK.md, and
DEPTH_CAVITY_PROBABILITY_CHECK.md in the authorized prior study, together
with this study's complete DEEP_COMPLEX_SOURCE.md,
DEEP_ACTIVATION_EXTENSION.md, DATASET_SOURCE_CONSTANTS.md, and
DATASET_MAXIMUM_REFINEMENT.md. No additional research sources or experiments
were used. All writes are confined to this study.

## 1. Model, gap, and the changed proof budget

Use the canonical width-n network, fixed hidden depth L, and m fixed sphere
training inputs v_a=x_a/sqrt(d). The forward and backward quantities are

\[
 z_a^{(1)}=Av_a,\quad z_a^{(l)}=W^{(l)}h_a^{(l-1)},\quad
 h_a^{(l)}=\phi_l(z_a^{(l)}),\quad f_a=w^\top h_a^{(L)}/n,
\]
\[
 r_a=f_a-y_a,\quad k_a^{(L)}=w,\quad
 \delta_a^{(l)}=\phi_l'(z_a^{(l)})\odot k_a^{(l)},\quad
 k_a^{(l)}=W^{(l+1)\top}\delta_a^{(l+1)}.
\]

The loss is m^-1 sum_a r_a² and mobilities are (n,1,...,1,n), so

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \quad\dot W^{(l)}=-\frac2{mn}\sum_a
                   r_a\delta_a^{(l)}h_a^{(l-1)\top},
 \quad\dot w=-\frac2m\sum_a r_ah_a^{(L)}.                 \tag{2}
\]

Initialization is the canonical independent Gaussian law with w(0)=0.
Activations satisfy the existing bounded-strip-holomorphic assumptions.
Define

\[
 Y=\|y\|_2/\sqrt m,\qquad
 \lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}>0,
 \qquad S=C_0Y/\lambda,
\]

where Q^(L) is the existing initialized limiting feature covariance.
The checked real energy argument supplies the full and fixed-size cavity
physical tubes, residual decay rate kappa=c_0 lambda, and total activity
O(S) under Y<=c lambda. Constants C,c below depend only on d,L and the
activation strip bounds. They are independent of m, lambda, Y, width,
and the later empirical moment degree, except where explicitly stated.
The case Y=0 is stationary and separately exact.

Fix a structural eta>0. For sample a, define its running real budget

\[
 \mathcal H_a(t)=\frac1n\sum_{l=1}^{L-1}\sum_i
   \exp\left\{\frac\eta S
                     \sup_{0\le u\le t}|k_{a,i}^{(l)}(u)|\right\}.
                                                               \tag{3}
\]

The proof stop is the first time max_a H_a(t) reaches a common B>L,
capped at T=C lambda^-1 log(en). Each autonomous cavity has its own
corresponding stop at 2B. A missing coordinate can be filled with zero,
adding only its count divided by n. These budgets and stops are solely
proof devices; equation (2) is unchanged.

For the complex source argument replace the real-time supremum in (3)
by the supremum over the current scaled time rectangle. Keep its existing
pole and forward/angular response stops. Query angles do not enter the
training carrier budgets. At domain scale zero all carriers vanish and
each H_a equals L-1, so B>L gives a strict starting margin.

This budget is weaker than the former mean-over-neurons exponential of a
sample maximum. We do not infer the old stronger budget from (3).
Instead the next sections check the exact estimates the proof needs.

## 2. Every local deterministic carrier estimate remains valid

On max_a H_a<=B, every sample, neuron, layer, and stopped time satisfies

\[
 |k_{a,i}^{(l)}|\le\frac S\eta\log(nB),                  \tag{4}
\]

because its individual nonnegative exponential is a summand of nH_a.
The cavity version has 2B. Thus the weak coordinate cap used for local
operator bounds, control amplitudes, contour Lipschitz constants, Taylor
remainders, and the variational propagator is unchanged. Once B is fixed,
it is at most CS log(en) with structural C for all sufficiently large n.

For a fixed sample a and any real p>=2,

\[
 \left(\frac1n\sum_i|k_{a,i}^{(l)}|^p\right)^{1/p}
       \le CSp B^{1/p}.                                \tag{5}
\]

Indeed x^p<=(p/e)^p exp(x), applied with
x=eta sup|k_{a,i}^{(l)}|/S, proves (5). The stronger p=2 estimate CS
continues to follow from the physical operator/readout tube, independently
of B. The top carrier w is bounded by CS coordinatewise and needs no
stochastic budget.

In mobility coordinates Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w), put
F_a=nf_a. The exact Hessian formula in the prior carrier source, equation
(11), decomposes D²F_a into a bounded-operator O(n)-rank term and a fixed
sum of bounded-map contractions of single carrier diagonals k_a^(l).
Every diagonal carries the same sample index a as F_a; no diagonal of
max_b |k_b| appears. Therefore (5) gives exactly its required estimates

\[
 \|H_{1,a}\|_{2,n}\le CS,\qquad
 \|H_{1,a}\|_{p,n}\le CSp(2B)^{1/p},\qquad
 \|D^2F_a\|_{\rm op}\le C(1+S\log(nB)),                 \tag{6}
\]

where ||M||_{p,n}=(tr|M|^p/n)^(1/p). The same individual-sample bound
applies to the response derivative B_a=D_Theta delta_a^(j+1):

\[
 \|B_a\|_{2,n}\le C,\qquad
 \|B_a\|_{p,n}\le C[1+Sp(2B)^{1/p}].                    \tag{7}
\]

Here B_a denotes a derivative map, not the budget B or H_a.

The variational Hessian uses a mixture over training samples. Define its
activity measure and normalized signed matrix by

\[
 d\mu(t)=\frac2m\sum_a|r_a(t)|dt,\qquad
 \mathcal A(t)=\frac{\sum_a r_a(t)D^2F_a(t)}
                         {\sum_a|r_a(t)|},              \tag{8}
\]

with A=0 when the denominator vanishes. By the norm triangle inequality,
(6), and the fact that its absolute coefficient weights sum to one,

\[
 \|\mathcal A(t)\|_{p,n}\le C[1+Sp(2B)^{1/p}].           \tag{9}
\]

This argument also controls every mixed-sample Hessian product: apply
normalized Schatten Holder to the factors separately. The sample indices
of the factors need not agree. No empirical maximum across those indices
is required. In particular a Dyson trace term with h Hessian insertions
between response endpoints B_b and B_a has exactly the former bound

\[
 \frac{(CS)^h}{h!}
       [C\{1+S(h+2)(2B)^{1/(h+2)}\}]^{h+2}.             \tag{10}
\]

Summing the series and the direct terms therefore gives the unchanged
singleton shift

\[
 \sup_{a,t}|k_{a,i}^{(j)}(t)
       -x_i^\top\delta_a^{(j+1),-i}(t)|
                \le CS(1+S^2B)+o(1).                  \tag{11}
\]

The coefficient in (11) is the singleton constant, independent of the
later deletion count and empirical moment degree. The direct external
trace uses only carrier RMS, the incoming/outgoing cross term is centered
by root independence, and the adaptive-residual rank-one term vanishes
with width, exactly as in the checked calculation.

The forward-response extension in DEEP_COMPLEX_SOURCE.md also remains
valid. Its endpoint DQ_b involves the Hessian F_b and stopped lower
forward-response diagonals; its trace pairing with a training derivative
C_a uses (6)--(9) and those lower caps. The angular endpoint involves only
its stopped lower angular derivatives. Its upward cap induction has no
new average of a sample maximum. All residual sums remain divided by m.
The enlarged activation graph uses only the weak coordinate cap (4) for
carrier multipliers, so its nonlinear insertion remainder is unchanged.

Uniform Gaussian control events still include the finite collection of
all sample indices. Their net cardinalities and eventual width thresholds
can depend on m. They do not change (6)--(11)'s structural constants or
the smallness condition on S: normalized sample averages control their
operator coefficients, while fixed m affects only a prefactor in the
net entropy dominated by the same strict powers of n.

## 3. The real Gaussian path estimate is needed one sample at a time

For a cavity use the common activity clock u(t)=mu([0,t])/S. Its total
range is bounded structurally. For one fixed sample a, physical parameter
speed estimates give the same preactivation increments as before. In a
changed backward gate split this sample's reference carrier at SR.
Its large-coordinate tail is controlled directly by H_a<=2B:

\[
 \frac1n\sum_i|k_{a,i}^{(l)}|^2
             \mathbf1_{|k_{a,i}^{(l)}|>SR}
                 \le CS^2 B e^{-c_\eta R}.              \tag{12}
\]

This follows by bounding x² exp(-eta x/2) uniformly and using (3) on
x=|k|/S. The small-coordinate part of the changed gate costs CS³Rv.
Taking R=C_eta[1+log(e+B)+log(1/v)], where
v=|u(t)-u(s)|<=1, proves the previous modulus for this fixed a:

\[
 \frac{\|\delta_a(t)-\delta_a(s)\|_2}{S\sqrt n}
 \le Cv[1+S^2\log(e+B)+S^2\log(1/v)]\le C\sqrt v,        \tag{13}
\]

provided S²log(e+B)<=c and S is structurally small. This deduction uses
only H_a, not the mean-over-neurons exponential of max_b |k_b|. Other
samples influence the common parameter motion only through normalized
residual activity (8).

Freeze each cavity reference at its own stop, or use the zero reference
if its own retained initialization conditions fail. These conventions are
measurable in retained initialization and remain independent of every
omitted root. For one fixed a, one omitted x_i~N(0,I/n), and a common
same-layer cavity -I, define

\[
 Z_{a,i}^{-I}=\sup_t|x_i^\top\delta_a^{(j+1),-I}(t)|/S.
\]

The process begins at zero. Equation (13) gives a structural covering
bound C epsilon^-2 in its conditional Gaussian metric. The checked dyadic
Gaussian-net argument therefore gives

\[
 \Pr\{Z_{a,i}^{-I}>C(1+z)\mid\text{cavity}\}
       \le Ce^{-cz^2},\qquad
 \mathbb E[e^{q Z_{a,i}^{-I}}\mid\text{cavity}]
       \le\mathcal L_{\rm one}(q)<\infty.                \tag{14}
\]

For each fixed q, L_one(q) is structural and independent of a,m,B,
width, and the fixed deletion count, after the displayed smallness
conditions. No maximum over a is taken in (14). Conditional on one
common cavity, the variables for distinct i are independent, because
they use independent outgoing roots. Independence across samples is
neither true in general nor needed.

## 4. Cavity survival and common-cavity comparison

The local insertion estimate supplies uniform retained-coordinate error
epsilon_(n,r)=o(1) for any fixed deletion count r. Until the earlier full
or cavity stop, it yields separately for every sample a

\[
 \mathcal H_a^{-I}(t)
 \le e^{\eta\epsilon_{n,r}/S}\mathcal H_a(t)+O(r/n)
 \le B+o(1)<2B.                                        \tag{15}
\]

Taking the maximum outside these inequalities proves that no cavity hits
its budget before the full stop. The initial cavity Gram/operator margins
are inherited as in the checked source. Query poles and response caps in
the complex proof transfer by the same coordinate-small comparisons.
This is a continuation argument, not conditioning a Gaussian law on the
full-network stopping event.

The common-cavity comparison also remains samplewise. For each a and
I containing i, project the complete frozen difference between the
singleton and I-cavity response paths onto its deterministic Euclidean
ball of radius C_r n^(1/100). This process remains independent of x_i.
Its Gaussian radius tends to zero, and (13) controls its entropy. It
agrees with the unprojected difference on the successful full prefix.
The checked estimate consequently yields

\[
 \sup_{a,t\le\sigma}
 |x_i^\top(\delta_a^{-i}(t)-\delta_a^{-I}(t))|=o(1)        \tag{16}
\]

outside a superpolynomially small event. The union over fixed m and fixed
r affects that exceptional probability and width threshold only. It
does not enter the singleton shift or the fixed-sample moment base.

## 5. Fixed-sample moments, then the union over samples

Let G_n be the strict full initialization event already used in the
source, independent of the later moment degree, and let sigma be the full
separate-budget stop. For one fixed a and layer j<L put

\[
 H_{a,n,j}=\mathbf1_{G_n}\frac1n\sum_i
     \exp\left\{\frac\eta S
                   \sup_{t\le\sigma}|k_{a,i}^{(j)}(t)|\right\}.
                                                               \tag{17}
\]

Fix an integer p before taking n large. Expand H_(a,n,j)^p. For a tuple
of p distinct neurons use its common p-neuron cavity. Equations
(11), (16), and (14), after dropping the full-event indicators only from
the nonnegative Gaussian upper bound, give expected product at most

\[
 [\mathcal L_{\rm one}(\eta)
                         e^{C\eta(1+S^2B)}]^p+o(1).      \tag{18}
\]

All factors in this product concern the same fixed sample a and different
independent omitted roots. Collision tuples use L_one(d_i eta) for the
fixed multiplicities d_i; their O_p(n^(p-1)) count gives a vanishing
normalized contribution. The exceptional insertion event contributes
at most B^p times its vanishing probability, because H_a is stopped below
B. Thus, with

\[
 D(B,S)=\mathcal L_{\rm one}(\eta)e^{C\eta(1+S^2B)},
\]

one has

\[
 \limsup_{n\to\infty}\mathbb E H_{a,n,j}^p\le D(B,S)^p,
 \qquad
 \limsup_{n\to\infty}\mathbb E
                  \left(\sum_{j<L}H_{a,n,j}\right)^p
                         \le[(L-1)D(B,S)]^p.            \tag{19}
\]

The second inequality is Minkowski; it needs no independence between
layers. The base is structural and independent of p and a. Fixed-p
remainder constants and width thresholds may depend on p and m.

Choose a structural B larger than L and
4(L-1)L_one(eta) exp(C eta). Then choose a structural upper bound on S
small enough for every local, trace and modulus condition and
exp(C eta S²B)<=2. This gives a ratio

\[
                    \vartheta=(L-1)D(B,S)/B<1,
\]

uniformly in m. If any sample's budget hits B, its sum in (19) equals B
on G_n. A union bound over the fixed m samples and Markov's inequality
therefore give, for every fixed p,

\[
 \limsup_{n\to\infty}
  \Pr\{G_n,\ \max_a\mathcal H_a\text{ reaches }B\}
                       \le m\vartheta^p.               \tag{20}
\]

For each fixed m, the infimum over positive integers p is zero. Width
tends to infinity first at fixed p; no growing-deletion estimate is used.
For a fixed requested confidence, p can be chosen of order
log(m/eta_confidence), after which the width threshold is enlarged for
that finite p. Neither B nor the bound on S changes with this choice.
Adding Pr(G_n^c)=o(1) removes the last initialization indicator.

This order of operations is the improvement: m appears only in the
probability union (20), not in the exponential moment used to choose B.

## 6. Complex domain and the unchanged source magnitudes

Run the same proof with each H_a defined over the current complex time
rectangle. The local insertion interfaces use algebraic transposes and
complex linear/quadratic Gaussian forms as before; (4)--(10) remain valid
with complex singular-value norms. Products of the base propagators
still incur only the total short vertical/backward contour length, while
the positive real propagator remains contractive.

For one fixed sample, decompose its complex cavity response as

\[
 \delta_a(t+is)=\delta_a(t)+[\delta_a(t+is)-\delta_a(t)].
\]

The real part has (14). The normalized bracket has radius
D_n=C r_n ell_n and the checked two-parameter covering bound. Its Gaussian
mean is o(1), and its tail scale is o(1). Applying Cauchy--Schwarz for
this one sample proves a structural complex exponential moment
L_one,complex(q). There is no summation over a at this step. The extra
factor lambda^-1 in the time-domain covering number enters its logarithm
and only the already allowed width threshold. Redefine L_one by this
complex constant and choose B as in Section 5.

Cavity survival (15), common-cavity comparison (16), the mixed-sample
endpoint traces (10), and the fixed-sample moment proof all apply to the
complex supremum. The existing forward-response and angular induction
then exclude query poles and all response stops. The empirical budget
obstruction has probability tending to zero by (20), completing the
same complex source domain as before:

\[
 r_n=c\ell_n^{-(L+4)},\qquad T=C\lambda^{-1}\ell_n.
\]

The prior source magnitudes remain structural, and the whole-query
backward source refinement continues to use its sufficient C sqrt(n)
magnitude. No source-family count or approximation degree is increased.

The real all-time carrier maximum is obtained from (11) and the
single-sample Gaussian tail followed by a union over a,j,i. Directly this
gives CS sqrt(log(e n m)). For n>=m it is at most CS sqrt(log(en)) with
structural C. Its all-time tail follows from the existing crude RMS
backward differentiation and residual decay. This last logarithmic union
changes the width threshold, not the label smallness condition. The
source theorem already concerns sufficiently large width for fixed m.

## 7. Label conclusion, limits, and supersession

The complete list of non-real smallness requirements is now

\[
 S\le c,\qquad S^2B\le c,\qquad
 S^2\log(e+B)\le c,
\]

with one fixed structural B. They follow from one structural bound S<=c.
The independent real energy theorem requires Y<=c lambda and supplies
S=C_0Y/lambda. Reducing its structural c therefore enforces every
condition and proves (1) for the full source and carrier construction.

This author derivation supersedes the need for the Gaussian-maximum
penalty in DATASET_MAXIMUM_REFINEMENT.md. The earlier maximum calculation
is correct for its stronger budget; the present result uses a weaker
budget sufficient for all audited interfaces. The previous smaller-label
conclusions remain valid.

Combining with WHOLE_QUERY_RESPONSE_SOURCE.md and the separately checked
quadratic-storage runtime would preserve the explicit bound
C gamma^-2 m² log(en)^[2d(L+5)+2]+Cm(d+1) when lambda=gamma/m, now under
Y<=c gamma/m. This note does not establish the separate runtime review,
any improved geometric relation between m and gamma, or a label threshold
independent of the normalized gap.

The remaining quantifiers are unchanged: fixed d,L,m, positive lambda,
fixed positive Y and requested confidence before sufficiently large n.
The final threshold may depend on m through fixed moment degrees,
control-net counts, initialized Gram concentration, and Gaussian unions.
No uniform growing-data theorem, finite-precision construction, or claim
of optimal label dependence is added. The present status is internally
checked, not an established or promoted result.
