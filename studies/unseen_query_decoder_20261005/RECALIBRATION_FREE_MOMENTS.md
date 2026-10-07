# Posterior-marginal moments without calibration

2026-10-06. Scoped author derivation in the existing unseen-query study.
No experiments, independent review, promotion, or Git operation.

The statistical replacement works: the one-row marginal of the actual
prefix posterior can serve as a **proof-only** reference law. Its moments
are estimated by ordinary Gaussian-prior blocks, without evaluating its
density or normalizer. The observed noisy history Grams supply the common
geometry directly. Under the inherited physical/source interfaces, this
gives the same whole-sphere, all-time dense-upper-certificate error, with
an iid query calculation costing \(n\operatorname{polylog}(n)\) row work.

There is one separate computational interface in this note: replacing the
long iid random tape by a repeatable absolute-polylogarithmic seed while
preserving its block success probabilities and the quadratic work bound.
That interface is **not proved here**. In particular, pairwise-independent
rows cannot simply be substituted into the product-KL argument below.
The conclusion is a statistical theorem and a conditional compact-decoder
theorem, not an unconditional short-seed implementation theorem.

## 1. Contract and supplied physical interfaces

Keep the original width \(n\), fixed nonlinear depth \(L\), Gaussian
initialization, zero initial readout, mean-loss gradient flow, mobilities

\[
 (n,1,\ldots,1,n),
\]

fixed spanning sphere data with \(m\ge d\), original small-label allowance,
initial unweighted feature-Gram gap, and strip-analytic activations with
the original bounded derivatives. Activation values need not be bounded.
The target is the inherited dense-pair upper certificate \(b_n\), with one
event controlling every \(\|x\|=\sqrt d\) and \(t\in[0,\infty]\).
No input or test label is known during acquisition. A query reads the
current scalar summaries, its seed, and the row-circuit description.
It does not read dense weights, private acquisition packets, or replay
the scalar training evolution.

The complete source interfaces used here are those explicitly stated in
`DENSE_BUDGET_DECODER_CANDIDATE.md` and proved or derived within the
allowed geometry, information, synthesis, self-normalization, and scalar
acquisition notes. This note does not re-prove the physical-flow source
theorem. In particular, the following remain inherited inputs:

1. A finite predictable noisy-matrix program through
   \(T=C\log(en)\), a frozen prediction tail, and a passive-query
   comparison to the dense trajectory to \(n^{-a}\), for any prescribed
   fixed \(a\), at sufficiently large individual width.
2. At most \(R\le C\log^8(en)\) named history fields/matrix calls,
   \(P=O(R^2)\) retained noisy scalar moments after including all required
   raw history pairs, and a row circuit of absolute-polylogarithmic size.
   Already-created fields keep their old scalar arguments.
3. Gaussian matrix-answer noise
   \(\sigma=\exp[-\log^2(en)]\), explicit \(\sigma^2\)-gapped
   conditioning formulas, and bounds
   \(\exp[\operatorname{polylog}(n)]\) on raw coefficients,
   global row caps, and sensitivities. These bounds do not deteriorate
   when the subsequent scalar-noise scale \(\eta\) is decreased.
4. Bounded physical mixer norms and training RMS fields on a complete
   source event. Conditional mean mixer bounds hold on an observable
   prefix event. The actual passive network has a fixed-depth Gaussian
   moment form after removing rank-at-most-\(R\) covariance corrections.
5. A deterministic, proof-only dense center \(f_0(t,x)\) within \(b_n\)
   of the actual dense trajectory on a complete-tape event. The posterior
   passive-query version has the corresponding conditional high-mass
   interval at each input and time. Its physical and frozen-tail errors
   are included in the \(n^{-a}\) budget.

These are scientific assumptions supplied by the scoped assignment,
not consequences of low information alone. All bounds below are uniform
over fixed admissible problems; their constants and sufficiently-large
width threshold may depend on that problem and on confidence. An exponent

\[
 C_L
\]

in the final error may depend on the fixed depth. Storage and work factors
use an absolute logarithmic exponent inherited from the finite circuit.

## 2. The actual posterior marginal and one event for all prefixes

Let \(Z_1,\ldots,Z_n\) be iid row packets with Gaussian prior \(\mu\),
and \(E_1,\ldots,E_P\) independent standard Gaussian scalar noises. The
ideal retained summaries are

\[
 C_r=\frac1n\sum_{i=1}^nF_r(Z_i;C_{<r})+\eta E_r,
 \qquad |F_r|\le B_F.                                      \tag{1}
\]

For an ideal prefix \(c=C_{\le j}\), write \(\pi_c\) for the row-array
posterior and define

\[
 \nu_c:=\pi_c^1,\qquad
 K(c):=D(\pi_c\Vert\mu^{\otimes n}),\qquad
 H:=\frac P2\log(1+B_F^2/\eta^2).                         \tag{2}
\]

Permutation invariance of (1) gives a common one-row marginal. Factoring
the density against its own marginal product yields the exact identity

\[
 K(c)=D(\pi_c\Vert\nu_c^{\otimes n})
                         +nD(\nu_c\Vert\mu).             \tag{3}
\]

For verification, the logarithm of the density ratio to the prior is the
sum of its logarithm relative to \(\nu_c^{\otimes n}\) and the \(n\)
one-row log-density ratios. Integrating the latter against \(\pi_c\)
uses its marginal \(\nu_c\) in every term. Finite \(K(c)\) justifies
the identity, or equivalently it follows by the entropy chain rule and
truncation. Consequently both terms on the right are nonnegative and

\[
 D(\pi_c\Vert\nu_c^{\otimes n})\le K(c),\qquad
 D(\nu_c\Vert\mu)\le K(c)/n.                            \tag{4}
\]

This is the desired product-reference estimate, with no tilt feasibility
error, multiplier, or normalizer.

The information proof for bounded Gaussian-noisy updates gives

\[
 I(Z_{1:n};C_{\le P})\le H.
\]

The posterior entropies \(K(C_{\le j})\) are a nonnegative submartingale:
the earlier posterior is the conditional mixture of later posteriors and
relative entropy is convex. The first-crossing inequality therefore gives
an event of probability at least \(1-\alpha\) on which

\[
 K(c)\le K_*:=H/\alpha
 \quad\hbox{at every prefix}.                             \tag{5}
\]

Indeed the expectation of the terminal entropy is at most \(H\); on each
disjoint first-crossing event its conditional terminal expectation is at
least the crossed threshold \(H/\alpha\). Their sum proves the bound.

Similarly, put \(S_E=\sum_{r=1}^PE_r^2\). The nonnegative martingale

\[
 \mathbb E[S_E\mid C_{\le j}]
\]

has mean \(P\). Except on an event of probability \(\beta\),

\[
 \mathbb E[S_E\mid c]\le P/\beta
 \quad\hbox{at every prefix}.                             \tag{6}
\]

All subsequent posterior statements are made on the intersection of
(5) and (6). Set

\[
 h:=K_*/n,\quad \bar h:=\max(h,1/n),\quad
 T_\rho:=\sqrt{P/(\beta\rho)}.                            \tag{7}
\]

For any fixed \(0<\rho<1\), Markov's inequality gives

\[
 \pi_c\{S_E\le T_\rho^2\}\ge1-\rho.                     \tag{8}
\]

Here scalar noises can be recovered from the array and fixed prefix via
(1) for the acquired coordinates; the same notation also denotes the
joint posterior including unused noises. They are not independent after
conditioning. Taking conditional expectations in (1) instead gives

\[
 |\nu_c F_r(\cdot;c_{<r})-c_r|
 \le\eta\sqrt{P/\beta}\le\eta T_\rho.                    \tag{9}
\]

Thus the actual posterior marginal matches the retained raw moments at
the scalar-noise tolerance, without computing it.

Unused future training coordinates may first be marginalized out. The
projected posterior is still exchangeable, has entropy at most \(K_*\),
and has the correspondingly projected one-row marginal. Appending fresh
independent passive-query Gaussian coordinates preserves these entropy
bounds and the identity (3). This is the correct use of fresh query
coordinates; unused future training marks are not declared fresh.

## 3. Observed Grams, numerical prefixes, and private acquisition

Let \(\widehat c\) be any numerical prefix with

\[
 \|\widehat c-c\|_\infty\le\varepsilon_{\rm hist}.        \tag{10}
\]

It need not be a function of \(c\): the weighted acquisition panel and
its rounding may depend on private source information. Throughout this
section \(\nu_c\) stays fixed and the argument is pointwise in **every**

\[
 \widehat c\in\{u:\|u-c\|_\infty\le\varepsilon_{\rm hist}\}.
\]

For a needed history vector \(S(z;\widehat c)\in\mathbb R^r\),

\[
 Q_{S,\nu}=\nu_c(SS^T),\qquad
 Q_{S,0}=\frac1n\sum_iS(Z_i;\widehat c)S(Z_i;\widehat c)^T.
                                                               \tag{11}
\]

Let \(Q_{S,\mathrm{obs}}\) be its symmetric retained pair table.
Each entry was acquired once after both fields existed. The global
row-circuit sensitivity supplies a number \(L_{\rm pair}\) such that
the change in any relevant pair test on the ball (10) is at most

\[
 L_{\rm pair}\varepsilon_{\rm hist},\qquad
 \log(1+L_{\rm pair})=\operatorname{polylog}(n).
\]

Equation (9), respectively (1) on (8), implies entrywise

\[
 |Q_{S,\nu}-Q_{S,\mathrm{obs}}|_{ab},\quad
 |Q_{S,0}-Q_{S,\mathrm{obs}}|_{ab}
 \le e_G:=\eta T_\rho+(1+L_{\rm pair})\varepsilon_{\rm hist}.
                                                               \tag{12}
\]

The first bound is deterministic given \(c,\widehat c\); the second
holds on the one posterior event (8), simultaneously for all history
tables. A symmetric \(r\)-matrix with entrywise error at most \(e_G\)
has operator norm at most \(re_G\), by Cauchy--Schwarz in each row.
Choose precision so

\[
 R e_G\le\tau/4                                           \tag{13}
\]

for an artificial ridge \(\tau>0\), and set directly

\[
 Q_S^*:=Q_{S,\mathrm{obs}}+2\tau I_r.                     \tag{14}
\]

Then, on the indicated event,

\[
 Q_S^*\succeq Q_{S,\nu},Q_{S,0},\qquad
 Q_S^*\succeq\frac{7\tau}{4}I_r,\qquad
 \|Q_S^*-Q_{S,j}\|\le\frac{9\tau}{4},\quad j\in\{0,\nu\}.
                                                               \tag{15}
\]

No numerical integration of \(Q_{S,\nu}\) occurs. A further numerical
error at most \(\tau/4\) in operator norm is harmless after increasing
the buffer. On arbitrary bad states use a guarded default if the required
positive floor or magnitude bounds cannot be certified; on (15) that
guard never triggers. All these are small matrices with a prescribed
positive floor, not inverse empirical Grams.

In the common coordinates

\[
 U_S=(Q_S^*)^{-1/2}S,
\]

both the population and empirical raw second moments are at most identity.
In particular, small empirical history eigenvalues never appear in the
statistical constants.

Here is the physical effect of the buffer, stated explicitly. Let a mean
learned mixer have the inherited factorization

\[
 M=T A_0 S^T/n,
\]

where \(S,T\) are its history-column matrices and \(A_0\) is the raw
coefficient matrix computed from the retained summaries. Its common
whitened coefficient is

\[
 A=(Q_T^*)^{1/2}A_0(Q_S^*)^{1/2}.                         \tag{16}
\]

If \(q=\max(\|Q_{S,0}\|,\|Q_{T,0}\|)\) and each buffer changes
the empirical Gram by at most \(D\), then

\[
 \|A\|\le\|M\|+2\|A_0\|\sqrt{D(q+D)}.                 \tag{17}
\]

Partial-isometry factorizations of \(S/\sqrt n,T/\sqrt n\) identify

\[
 \|M\|=\|Q_{T,0}^{1/2}A_0Q_{S,0}^{1/2}\|.
\]

Subtract this product from (16) and use

\[
 \|P^{1/2}-Q^{1/2}\|\le\sqrt{\|P-Q\|}
\]

for positive semidefinite matrices, followed by the triangle inequality.
The geometry note proves that square-root inequality by the resolvent
integral and operator order, including singular matrices. This proves
(17). It bounds the operator in the stable coordinates; it does not
charge a raw inverse-noise coefficient as a physical amplification.

For the forward-observation block \(Q_0\), write its cross moment as

\[
 v=\frac1nV^Tq_{\rm in},\qquad
 c_{\rm in}=\|q_{\rm in}\|_2^2/n.
\]

Replacing \(Q_0\) by a dominating \(Q^*\) at distance \(D\) changes
the conditional variance by

\[
 0\le v^T[(\sigma^2I+Q_0)^{-1}-(\sigma^2I+Q^*)^{-1}]v
 \le(D/\sigma^2)c_{\rm in}.                              \tag{18}
\]

To verify it, set \(R_0=(\sigma^2I+Q_0)^{-1}\) and

\[
 E=R_0^{1/2}(Q^*-Q_0)R_0^{1/2}.
\]

Then \(0\preceq E\preceq D\sigma^{-2}I\), and the resolvent
difference equals \(R_0^{1/2}[I-(I+E)^{-1}]R_0^{1/2}\preceq
D\sigma^{-2}R_0\). The query/history Gram is positive semidefinite,
so \(v^TR_0v\le c_{\rm in}\). These facts prove (18).

Choose a target \(\varepsilon_0=n^{-a}\), with \(a>2\), and choose
the ridge first so that the right-hand error in (17), (18), including
its fixed-depth polynomial-in-\(B\) propagation, is at most
\(\varepsilon_0\). The raw coefficient, history magnitude, and
\(\sigma^{-1}\) bounds make \(\log(1/\tau)\) an absolute
polylogarithm. Next choose \(\eta\) so that (13) and the inherited
scalar-source perturbation budget hold, and finally choose
\(\varepsilon_{\rm hist}\) and arithmetic precision. This order
is not circular: raw coefficient bounds and the matrix noise floor were
fixed before \(\eta\). Although \(H\) increases when \(\eta\)
decreases, it remains absolute-polylogarithmic and does not enter (17).

The coefficient \(A\) in (16) is deterministic given
\(\widehat c\). To deduce its bound from a posterior physical event,
intersect that event with (8). Its posterior probability is positive at
the chosen fixed failure thresholds. On every array in that intersection,
(17) gives the same deterministic bound for \(A\). Thus the bound holds
for that prefix, and pointwise for every \(\widehat c\) in (10).
No conditioning on a privately selected array is needed.

The same argument bounds the final readout coefficient in the common
coordinates by its physical RMS bound plus the negligible buffer error.
A master incoming history contains all forward-query columns. If \(J\)
selects them, the variance coefficient is

\[
 P_{\rm var}=(\sigma^2I+JQ_S^*J^T)^{-1/2}J(Q_S^*)^{1/2},
 \qquad \|P_{\rm var}\|\le1,                            \tag{19}
\]

because its product with its transpose is bounded by identity. Outgoing
moment marks and mean-output marks may have different Grams; each gets
its own common bound (15).

## 4. The neural weak-moment bridge with the marginal reference

Only new passive features need the small cap. The inherited safe complex
time disks have radius \(r\asymp\log(en)^{-1/2}\) and uniformly bounded
imaginary preactivation. The first sine Fourier coefficient gives

\[
 |\partial_t z_i(t,x)|\le C/r.
\]

The initial Gaussian sphere-net bound is \(C\sqrt{\log(en)}\).
Integration through \(T=C\log(en)\) therefore yields a uniform physical
feature and preactivation bound

\[
 B=C\log^{3/2}(en).                                      \tag{20}
\]

Compose each activation with a smooth cap which agrees on that physical
range and satisfies

\[
 |\chi|\le B,\qquad |\chi'|\le a_1,\qquad
 |\chi''|\le a_2,                                      \tag{21}
\]

after absorbing a fixed factor into \(B\). The derivative constants are
bounded independently of \(n\). Source approximation with sufficiently
large fixed \(a\) makes its coordinate errors at most
\(\sqrt n\,n^{-a}\); hence these caps preserve completed source
queries on the physical event. Large earlier Picard/history fields are
controlled by their raw Grams, not by (20).

Condition on the finite observable predictable matrix transcript, not on
private roots or the full continuous trajectory. Gaussian likelihoods
factor by matrix label. For a new passive input the posterior covariance
has the inherited form

\[
 \Gamma=\beta I-K,\quad 0\preceq K\preceq\beta I,\quad
 \operatorname{rank}K\le R,\quad
 \beta=\sigma^2+c_{\rm in}-v^T(\sigma^2I+Q_0)^{-1}v.
                                                               \tag{22}
\]

Coupling \(\Gamma^{1/2}g\) and \(\sqrt\beta g\) with the same
standard Gaussian vector costs normalized squared error at most
\(\beta R/n\): only \(R\) eigenvalues can differ. Each hidden
matrix is used once in a passive forward query. The higher centered
posterior matrices have covariance dominated by their Gaussian prior,
and are independent of that layer's incoming difference. Their expected
squared RMS amplification is at most one, with bounded conditional mean
mixers adding a fixed factor. Layer hybrids through the fixed depth and
bounded readout give prediction RMS error at most

\[
 C_L B\sqrt{R/n}.                                        \tag{23}
\]

This is a conditional bound for every fixed query and time. It is not
a simultaneous random-function coupling. The later interval argument
uses precisely this conditional form.

The scalar-noised fields are coupled to the scalar-unperturbed consistent
transcript at the same packets. Equation (9) of the scalar acquisition
note bounds their prefix error by

\[
 \eta T_E P(1+L_C)^P.
\]

Its explicit circuit sensitivity and the gapped formulas make the induced
passive error at most \(\eta\exp[\operatorname{polylog}(n)]\).
The precision choice above makes this \(\le\varepsilon_0\).
The same holds uniformly for (10). Inserting noisy moments into the
exact Gaussian posterior without this coupling would be invalid.

After removing (22) and using (14), the reference recursion at a fixed
input/time has the following form. Its training row marks are distributed
according to \(\nu_c\); new \(g_\ell\) are independent standard
Gaussians. In common coordinates,

\[
 h_\ell=\chi_\ell\left(U_\ell^TA_\ell b_{\ell-1}
                           +\sqrt{\beta_\ell}\,g_\ell\right),
 \quad
 \beta_\ell=\sigma^2+c_{\ell-1}
                         -\|P_\ell b_{\ell-1}\|^2,
                                                               \tag{24}
\]

\[
 b_\ell=\mathbb E_{\nu_c,g}[V_\ell h_\ell],\qquad
 c_\ell=\mathbb E_{\nu_c,g}[h_\ell^2].                    \tag{25}
\]

Here \(\nu_c(U_\ell U_\ell^T),\nu_c(V_\ell V_\ell^T)\preceq I\),
the same bounds hold empirically on (8), \(\|A_\ell\|\le C\),
and \(\|P_\ell\|\le1\). Feasible exact moment pairs have
\(\beta_\ell\ge\sigma^2\) by positive semidefiniteness of their
query/history Gram. The first layer is directly evaluated from Gaussian
first-row marks, learned-update marks, and \(x\); the readout is a final
history cross moment. Denote this deterministic, inaccessible reference
prediction by

\[
 d_\nu(c,\widehat c;t,x).
\]

The posterior empirical comparison uses (3), not an iid-posterior claim.
For any deterministic scalar row test \(|G|\le B\) and any common
whitened history \(V\in\mathbb R^r\), the self-normalized entropy
bound gives

\[
 \mathbb E_{\pi_c}\!\left[
 \left\|n^{-1}\sum_iV_iG_i-\nu_c(VG)\right\|^2
 \mathbf1_{\{n^{-1}\sum_iV_iV_i^T\preceq I\}}\right]
 \le \frac{CB^2}{n}(K_*+r+1).                            \tag{26}
\]

Its hypotheses hold: the reference product is \(\nu_c^{\otimes n}\),
the population Gram is at most identity by (15), and its array relative
entropy is at most \(K_*\) by (3). The empirical-Gram event is supplied
by (8), (12), and (15), not by iid concentration. The scalar test
\(G^2\) has the analogous bound \(CB^4(K_*+1)/n\).

For clarity, (26) follows by applying the iid raw-second-moment
concentration lemma to each direction in a proof-only \(1/2\)-net of
size at most \(5^r\), integrating its Gaussian tail to obtain

\[
 \log\mathbb E_{\nu_c^{\otimes n}}
 \exp\!\left(\frac{n\,\mathbf1_E\|\overline{VG}-\nu_c(VG)\|^2}
                   {CB^2}\right)\le C(r+1),
\]

and applying the entropy inequality with array entropy \(K_*\).
Thus unbounded whitened coordinates cause no omitted tail assumption.

To propagate moments, integrate the new scalar Gaussian before comparing
parameters. If \(\chi\) satisfies (21), its Gaussian expectation is
\(a_1\)-Lipschitz in the mean and \(a_2/2\)-Lipschitz in the
variance. The second statement follows by twice integrating by parts at
positive variance; add a common positive variance and take it to zero to
cover zero variance. For \(\chi^2\) the corresponding constants are
\(2Ba_1\) and \(a_1^2+Ba_2\).

If \(x_\ell\) is a cross-moment norm discrepancy and \(y_\ell\) is
a second-moment discrepancy, comparison at fixed reference parameters
therefore gives

\[
\begin{split}
 x_\ell&\le a_1C x_{\ell-1}
       +\tfrac12a_2(y_{\ell-1}+2Bx_{\ell-1})+e_\ell,\\
 y_\ell&\le2Ba_1C x_{\ell-1}
       +(a_1^2+Ba_2)(y_{\ell-1}+2Bx_{\ell-1})+z_\ell.
\end{split}                                                \tag{27}
\]

Indeed an upper Gram bound gives RMS mean change at most
\(Cx_{\ell-1}\), and Bessel's inequality gives
\(\|b_{\ell-1}\|\le B\). Factoring the quadratic variance term
bounds its change by \(2Bx_{\ell-1}\). Finally

\[
 \|\mathbb E[Vq]\|\le\|q\|_{L^2}
\]

by duality and the upper Gram bound. These three estimates prove (27).

Apply (26) only to the tests at the deterministic reference parameters
in (24). Earlier random empirical query summaries are handled by (27),
not inserted into a fixed-test entropy estimate. Fresh query row noises
have conditional cross-moment variance at most \(B^2r/n\), and
second-moment variance at most \(B^4/n\), on the same training Gram
event. Add those terms to \(e_\ell,z_\ell\). Minkowski's inequality
in (27), restricted to the common training Gram event, gives

\[
 \left(\mathbb E[|Y_{\rm aux}-d_\nu|^2\mathbf1_E\mid c]
       \right)^{1/2}
 \le \frac{C\log^{C_L}(en)}{\sqrt n}.                    \tag{28}
\]

Here \(Y_{\rm aux}\) is the finite-array auxiliary query; physical
coupling, (23), and the small ridge/source errors are added separately.
The complement of \(E\) has posterior probability at most \(\rho\).
Choose a fixed multiple of the radius in (28) to make its conditional
Markov failure any chosen fixed small number. Combining these errors
produces a posterior high-mass interval around \(d_\nu\) with radius

\[
 e_n=C\log^{C_L}(en)/\sqrt n.                             \tag{29}
\]

No square root of a variance **error** occurs in (27). The strong
coupling is used for the finite-rank error (23); moment propagation uses
weak Gaussian expectations.

## 5. A prior-block estimator for a low-entropy marginal

The following lemma does not require a neural circuit or an accessible
posterior density.

Let probability laws \(\nu\ll\mu\) satisfy

\[
 D(\nu\Vert\mu)\le h,
\]

let \(U\in\mathbb R^r\) satisfy \(\nu(UU^T)\preceq I\), and
let \(|G|\le B\). Fresh independent row Gaussian coordinates may be
included in both laws. Set \(\bar h=\max(h,1/n)\), fix

\[
 \kappa=1/128,
\]

and suppose \(\bar h\le\kappa/2\). Use block size

\[
 s=\lfloor\kappa/\bar h\rfloor,
 \qquad \frac{\kappa}{2\bar h}\le s\le\frac\kappa{\bar h}.
                                                               \tag{30}
\]

Draw \(J\) independent blocks, each of \(s\) iid samples from the easy
law \(\mu\), and take the coordinatewise median of their means of

\[
 X=UG.
\]

For an odd number of blocks, call the resulting vector \(\widehat m\).
Then

\[
 \Pr\!\left\{\|\widehat m-\nu(UG)\|>
                   4B\sqrt{r/s}\right\}
 \le r\,2^{-J/2}.                                       \tag{31}
\]

In particular, the error is at most

\[
 C B\sqrt{r\bar h}.                                     \tag{32}
\]

Proof: under \(\nu^{\otimes s}\), each coordinate block mean has
variance at most \(B^2/s\), because

\[
 \nu(U_a^2G^2)\le B^2\nu(U_a^2)\le B^2.
\]

Chebyshev therefore bounds its failure at threshold \(4B/\sqrt s\)
by \(1/16\). Product entropy and the entropy-to-total-variation bound
give

\[
 \|\nu^{\otimes s}-\mu^{\otimes s}\|_{\rm TV}
 \le\sqrt{sD(\nu\Vert\mu)/2}
 \le\sqrt{\kappa/2}=1/16.                               \tag{33}
\]

Consequently the same coordinate block failure under \(\mu^{\otimes s}\)
is at most \(1/8\). Blocks are independent under the implemented iid
prior law. If the coordinate median fails, at least \(J/2\) blocks fail.
Summing over their possible subsets bounds this probability by

\[
 2^J(1/8)^{J/2}=2^{-J/2}.
\]

Union over \(r\) coordinates and convert their individual errors to a
Euclidean norm, obtaining (31). This proves the lemma.

The argument does not bound \(\mu(UU^T)\), which may be arbitrarily
larger than \(I\). It does not claim that \(\mu(UG)\) is the
desired moment. Each block succeeds by proximity of its *whole product
law* to \(\nu^{\otimes s}\), and the median rejects the remaining
prior blocks. Coordinatewise Chebyshev before median amplification is
important: using only a vector-norm block bound and then coordinate
medians would introduce an unnecessary extra \(\sqrt r\).

For the scalar \(G^2\), the same proof gives

\[
 |\widehat c-\nu(G^2)|\le C B^2\sqrt{\bar h}
                                                               \tag{34}
\]

with failure at most \(2^{-J/2}\). The zero-entropy case is covered
by \(\bar h\ge1/n\): then \(\nu=\mu\), and \(s\asymp n\)
gives the ordinary root-width sampling tolerance. Small exceptional
widths not satisfying the displayed condition can use a guarded default;
the theorem is at sufficiently large individual width.

Applying the lemma with \(\nu=\nu_c\), \(h=K_*/n\), and the
observed-Gram whitened marks is valid by (4), (15). For a layer test
one may sample one extra Gaussian \(g\) per row and evaluate (24),
rather than perform its one-dimensional integral analytically. The
reference remains \(\nu_c\otimes N(0,1)\), whose entropy relative
to \(\mu\otimes N(0,1)\) is still at most \(h\).

## 6. Guarded recursion and simultaneous iid-tape accuracy

The algorithm never uses \(\nu_c\). It constructs (14), evaluates
the inherited raw coefficients, and approximates each current query
moment in (25) using the prior blocks from Section 5. The first layer
and readout use the same rule. At every intermediate step project
cross moments onto the radius-\(B\) Euclidean ball and scalar second
moments onto \([0,B^2]\). Compute variance as

\[
 \sigma^2+\max\{0,c-\|P b\|^2\}.                        \tag{35}
\]

The exact \(\nu_c\) moments lie in these guards, so the projections
do not increase their discrepancies. The maximum in (35) is one-Lipschitz
and preserves the linear variance-error bound used in (27), since the
exact variance is feasible. These guards give a fixed bounded parameter
domain even when a numerical sample fails.

The block output is required simultaneously over every finite context
the algorithm may use; merely conditioning on seed-dependent earlier
query estimates would invalidate the fixed-function lemma. Conditional
on the complete source and actual numerical acquisition, all ideal
prefixes \(c_j\), numerical prefixes \(\widehat c_j\), and reference
laws \(\nu_{c_j}\) are fixed. The iid query tape is independent of that
source. At each query moment call, round the following quantities to a
prescribed finite grid:

- sphere inputs;
- each compact physical-time patch coordinate;
- all guarded incoming query-moment parameters at each layer.

The number of real parameters is absolute-polylogarithmic. The inherited
global caps and row-circuit sensitivities, together with the prescribed
\(\tau\) and \(\sigma\) floors, give absolute-polylogarithmic
logarithms of continuity constants. The maps are Lipschitz, or
one-half-Hölder if a zero-variance square root is used instead. The latter
only squares the necessary mesh. Choose grid precision so that replacing
an actual argument by its rounded context changes the exact population
moment by at most \(n^{-a}\). The finite set of context codes then has

\[
 \log N_{\rm ctx}=\operatorname{polylog}(n).              \tag{36}
\]

Only the current code is stored, not a table of codes. The block
concentration lemma applies at every guarded code, including moment
pairs which do not themselves arise as exact moments. Such pairs still
give a bounded \(\chi\) through (35); the upper Gram bound concerns the
fixed history marks and remains true. Quantization is a separate error
source in (27), not an assertion that the rounded median varies
continuously. For each fixed code, (31), (34) hold. Choose

\[
 J\ge C\big[\log N_{\rm ctx}+\log(P(R+1)L/\delta_{\rm q})+1\big]
                                                               \tag{37}
\]

odd. Union over all prefixes, layer moment tests, coordinates, and context
codes. Couple the finite Gaussian stream to ideal Gaussian rows with
its separately assigned numerical error and probability. With conditional
probability at least
\(1-\delta_{\rm q}\), the same iid tape estimates every needed
moment at every possible rounded argument. Add the population-map
rounding error to handle the actual input/time and intermediate arguments.
The resulting errors are

\[
 e_\ell^{\rm num}\le C B\sqrt{R\bar h}+n^{-a},\qquad
 z_\ell^{\rm num}\le C B^2\sqrt{\bar h}+n^{-a}.           \tag{38}
\]

Apply (27) under the fixed reference law \(\nu_c\), now comparing
the deterministic recursion (24)--(25) to the guarded block recursion.
At fixed depth it gives

\[
 \sup_{j,t,x}|f_{\rm block}(\widehat c_j;t,x)
                 -d_\nu(c_j,\widehat c_j;t,x)|
 \le \frac{C\log^{C_L}(en)}{\sqrt n}.                    \tag{39}
\]

The \(R\) in (38) is permitted: \(R,K_*,B\) are all
absolute-polylogarithmic, so their fixed-depth amplification remains a
logarithmic root-width error. No target \(n^{-3/4}\) numerical
tolerance is needed. The unavoidable block scale is already sufficient
for the inherited dense-upper certificate.

Two uniformities should not be confused. The posterior-to-center argument
is deterministic and holds for every \(\widehat c\) in (10). For
the independent numerical seed event, one conditions on the full actual
source and its chosen \(\widehat c_j\), and takes the finite set only in
query/time/moment parameters. There is no union over all possible private
panels, no conditioning of \(\pi_c\) on that panel, and no assumption
that \(\widehat c\) is measurable from \(c\).

## 7. Exact short-seed interface and resource accounting

With genuine iid sampling, the row count per query is

\[
 O(LJs),\qquad s\le\kappa/\bar h\le\kappa n,
 \qquad J=\operatorname{polylog}(n).                     \tag{40}
\]

The row circuit is a finite directed acyclic graph of
absolute-polylogarithmic size. At a fixed packet, cache its node values
and evaluate it in topological order. This uses only
absolute-polylogarithmic storage and avoids exponential recursive
recomputation. The matrix macros have dimension at most \(R^2\), known
positive floors, and absolute-polylogarithmic logarithmic precision.
Ordinary counted small-matrix routines therefore have polynomial cost
in these quantities. The same activation primitive convention as a dense
forward pass is used. A bit-time statement additionally requires
polynomial-time precision access to the activation primitives.

A block is streamed with one row packet and an \(r\)-vector accumulator.
Retaining the \(J\) block means for coordinate medians costs \(O(Jr)\)
numbers. Row values, counters, current query moments, scalar histories,
small matrices, and arithmetic precision remain an absolute logarithmic
power. The primitive work is

\[
 n\operatorname{polylog}(n),                             \tag{41}
\]

eventually at most \(O(Ln^2+dn)\). A retained long iid tape, however,
would cost \(n\operatorname{polylog}(n)\) bits. Generating fresh
independent randomness separately for each query gives no repeatable
uniform decoder function. Neither is the requested implementation.

The missing simulator must provide the following **specific interface**:

1. A finite-bit iid baseline representing the streamed capped/quantized
   Gaussian blocks with per-integrand deterministic or coupled numerical
   error below the assigned \(n^{-a}\) tolerance. The number of input
   random bits, evaluation steps, and row operations are
   \(n\operatorname{polylog}(n)\); working space is
   absolute-polylogarithmic. All logarithmic precisions are counted.
2. One source-independent seed of absolute-polylogarithmic length whose
   repeatable stream fools each fixed-parameter finite-precision block
   estimator failure test to additive error at most
   \(\delta_{\rm q}/[CPL(R+1)N_{\rm ctx}]\). A test may hardwire
   its fixed parameter point and a finite-precision approximation to
   the target moment. Such thresholds are proof advice for the
   indistinguishability assertion, not numerical inputs to the decoder.
3. Seed generation, stream generation/replay, and the entire actual query
   evaluation together use at most \(O(Ln^2+dn)\) work and
   absolute-polylogarithmic live and retained space. The simulator must
   work uniformly over the allowed scalar-circuit inputs and precision.

Fooling separate fixed-parameter tests and union-bounding is sufficient;
the simulator need not fool a single program enumerating the exponentially
large context set. Since (36) holds, the logarithm of its required additive
error inverse is still absolute-polylogarithmic. Supplying this interface
transfers the iid event in Section 6 with an additional allocated failure
probability. This note does not invoke an unverified pseudorandom-generator
theorem to assert that the interface has been met.

Here are two numerical details needed by that interface. First, a
fixed-context true target \(m=\nu_c(UG)\) may be inaccessible. For the
failure tester only, hardwire a rational \(\widetilde m\) with
\(\|\widetilde m-m\|_\infty\le\epsilon\ll B/\sqrt s\). The target
coordinates are bounded by \(B\); scalar second moments are bounded by
\(B^2\). Use a comparator radius, for example \(8B/\sqrt s\), larger
than the iid statistical radius plus rounding error. Its iid failure
probability is still bounded by (31), while success implies a true
coordinate error at most \(8B/\sqrt s+\epsilon\), plus the separately
budgeted arithmetic error. The target is fixed after conditioning on the
source and context, so no additional union over possible target values is
needed. The actual decoder never evaluates or receives these thresholds.

Second, if Gaussian sampling uses a clipped inverse distribution
function with cutoff \(T_G\), its inverse derivative within the clipped
range is at most \(C\exp(T_G^2/2)\). To couple \(b\) uniform bits to
one exact Gaussian with coordinate error \(\epsilon_G\), choose

\[
 b\log 2\ge T_G^2/2+\log(C/\epsilon_G).
\]

The clipped tail costs at most \(2\exp(-T_G^2/2)\) per coordinate.
Choose \(T_G^2\) to dominate the logarithm of the total sample,
context, and coordinate count and the requested failure inverse.
Larger constants in the same absolute logarithmic precision exponent
then satisfy the uniform-bit requirement. This couples the finite
sampler to ideal \(\mu\) blocks after (33); a separate tail bound under
the inaccessible \(\nu_c\) is unnecessary.

The supervisor subsequently supplied a proposed block finite-state
simulator interface: one pseudorandom block supplies a whole Gaussian
row, only persistent between-row state enters its finite-state bound,
and row scratch is cleared after that row. Across queries the seed is
restarted; every fixed-context tester is a single pass through its row
blocks. This is compatible with the statistical proof. It does not
require independence after substituting the simulator: the iid argument
establishes a baseline failure probability, and the simulator transfers
that one test probability. Verification of the cited generator theorem,
its exact seed exponent, and its total work belongs to the supervisor's
separate interface proof and is not claimed by this note.

Within-block pairwise independence is insufficient **for the argument
given here**. Equation (33) compares exactly
\(\nu^{\otimes s}\) and \(\mu^{\otimes s}\). A small-seed,
pairwise-independent block law can have total variation almost one from
the product law. For example, pairwise-independent fair-bit families from
all nonzero linear forms of a logarithmic-size uniform binary seed have
at most \(s+1\) possible length-\(s\) strings, whereas the iid law has
\(2^s\). The support event has probability one for the former and
at most \((s+1)/2^s\) for the latter. This does not disprove that a
particular pseudorandom construction works; it invalidates replacing the
product distribution by such a construction without a separate proof.
Also, Chebyshev under the prior is not an available repair: only
\(\nu(UU^T)\preceq I\), not a useful prior second moment, was proved.

The autonomous acquisition updates also need no calibration. The existing
positive panel has \(q\le P+1\) packets, and each scalar update is

\[
 \widehat C_r=\sum_{j=1}^q\widehat p_j
               F_r(\widehat z_j;\widehat C_{<r})
                     +\eta\widehat E_r
\]

to its assigned arithmetic precision. Cache the finite row DAG for one
packet at a time. A scalar update, even including all current small
coefficient/Gram calculations, then has absolute-polylogarithmic work
and space; a finite source step consists of absolute-polylogarithmically
many such updates. This observation does not charge a recursive
exponential evaluator when its whole one-row DAG fits the workspace.
It does not show quadratic **initial construction** of the selected
panel: source-dependent preprocessing and support selection remain the
separate inherited acquisition task.

## 8. One event for all inputs, all times, and the endpoint

Let \(\mathcal G\) be the complete source event containing the dense
center certificate, physical/source coupling, relevant operator bounds,
and successful acquisition precision. Its failure can be assigned an
arbitrarily small fixed fraction of the requested \(\delta\), using
the inherited fixed-confidence versions and sufficient-width threshold.
The process

\[
 M_j=\Pr(\mathcal G^c\mid C_{\le j})
\]

is a nonnegative martingale. Append one terminal reveal of
\(\mathbf1_{\mathcal G^c}\) to the filtration. The first-crossing
inequality bounds the probability that this extended martingale exceeds
a fixed threshold \(q_0\in(0,1)\) by

\[
 \Pr(\mathcal G^c)/q_0.
\]

On the complementary event, the actual tape belongs to
\(\mathcal G\) and every ideal prefix has posterior source failure
at most \(q_0\). This construction justifies both claims at once;
a small posterior failure at prefixes alone would not force the actual
hidden tape to be good.

Intersect this event with (5), (6). For each prefix, every numerical
prefix in its error ball, and every query/time pair, the actual passive
query posterior has a high-mass interval around

\[
 f_0(t,x)
\]

of radius \(b_n+n^{-a}\), by the inherited dense-center/source input.
Equations (23)--(29) give a second posterior interval around

\[
 d_\nu(c,\widehat c;t,x)
\]

of radius \(e_n\), with fixed high mass. Choose the conditional Gram,
source, rank-coupling, and RMS thresholds sufficiently small that the
two masses sum to more than one. For example all constituent losses can
be allocated \(1/32\), with the constants in (29) increased as needed.
The intervals intersect, so their deterministic centers obey

\[
 |d_\nu(c,\widehat c;t,x)-f_0(t,x)|
 \le b_n+n^{-a}+e_n.                                    \tag{42}
\]

This implication holds separately at every query on the same prefix
event. It needs neither a union over uncountably many posterior queries
nor a simultaneous pathwise query coupling. The parameterwise numerical
prefix argument makes (42) valid for the actual privately acquired
\(\widehat c\).

Now use the single independent iid-tape event of Section 6, or its
short-seed replacement **if** Section 7's interface is supplied. Adding
(39), (42), and the actual dense-to-center bound gives

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\rm block}(t,x)-f_n(t,x)|
 \le 2b_n+\frac{C\log^{C_L}(en)}{\sqrt n}.              \tag{43}
\]

The completed time patches and frozen source tail include the fitted
endpoint. No endpoint derivative assumption has been added.

An explicit failure allocation is available: take the source event with
failure at most \(q_0\delta/4\), giving extended-maximal failure
at most \(\delta/4\); take \(\alpha=\beta=\delta/8\);
allocate \(\delta/4\) to the numerical tape/simulator event including
its union bound. Their sum is \(3\delta/4\), leaving
\(\delta/4\) for separate Gaussian discretization/acquisition
failures if not already included. Fixed conditional failures enter the
interval masses, not new growing outer unions. Use \(b_n\) at the
corresponding smaller fixed confidence in the source event.

For fixed nonzero labels, \(Y=\|y\|_2/\sqrt m>0\), the inherited
certificate contains a positive factor
\(\exp(CY^2\sqrt{\log(en)})\). It eventually dominates every
fixed logarithmic power in (43); hence its additional term is eventually
at most \(b_n\), giving \(3b_n\). This is the same dense-upper-bound
scale, not the earlier literal remainder \(1/n\). Zero labels give
the identically zero predictor. The width threshold remains dependent
on the original fixed problem parameters.

## 9. Claim boundary and adversarial checks

| Statement | Status here | Essential boundary |
|---|---|---|
| Actual-marginal product entropy (3) | Proved | Exchangeable posterior of iid-prior rows |
| Marginal/empirical moments admit observed common Grams | Proved | Retained raw pairs, scalar-noise maximal bound, prescribed rounding |
| Prior iid blocks estimate posterior-marginal cross moments | Proved | Block size \(s\le\kappa/h\), genuine within-block product law |
| Fixed-depth neural posterior-to-reference error | Proved under inherited source interfaces | Physical caps, gapped source coupling, bounded mean mixers |
| Whole-sphere/all-time statistical certificate (43) | Proved for one iid tape | Long random tape is not compact retained state |
| Online summary updates avoid exponential calibration | Proved under counted row-DAG interface | Initial panel construction is separate |
| Repeatable compact decoder with the same certificate and quadratic query work | Conditional | Exact short-seed interface in Section 7 |

The largest surviving obstruction in this scoped route is the simulator,
not an uncomputed posterior normalization. The posterior marginal is never
sampled, normalized, or stored; its sole role is to supply (3), the
observed-Gram geometry, and the target moments in the proof. Using a
different surrogate law without moment matching would lose that geometry.
Using a prior expectation would lose the near-null-direction control.

No claim is made that information alone stabilizes an arbitrary noisy
scalar program. Stability comes from the inherited neural normal form
and (27); the earlier redundant-moment counterexample remains valid for
naive prior substitution. No bounded-activation assumption, reduced label
range, frozen-feature model, training-input restriction, history-Gram gap,
or finite-horizon replacement has entered this argument.

Complete scientific inputs read for this note were exactly
`DENSE_BUDGET_DECODER_CANDIDATE.md`, `DENSE_BUDGET_GEOMETRY.md`,
`DENSE_BUDGET_SELF_NORMALIZED.md`, `EFFICIENT_QUERY_INFORMATION.md`,
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md`, and
`NOISY_SCALAR_HISTORY_ACQUISITION.md`. No prior isolated reviews,
other studies, old book material, or external scientific sources were
read. The research and rigorous-proof skills and their selected process
references were read. The required custom canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned `Permission denied`; no readable equivalent was found in the
available skill roots. The supervisor's explicit fallback was used:
preserve supplied canonical symbols and define every new object locally,
without pretending to have read the unavailable skill or neural reference.
Only this assigned note was written.

## 10. Authorized addendum: explicit query precision closure

The supervisor subsequently authorized the complete additional input
EXPLICIT_COMPILER_EXPONENT.md and requested numerical degrees for the
observed-Gram query circuit. That note supplies, with
\(\ell=\log(en)\),

\[
 R\le C\ell^8,\quad P\le CR^2,\quad N\le CR^7,\quad
 X=C_*(2+n+R+\sigma^{-1}),\quad \log X=O(\ell^2).
 \tag{44}
\]

Its named row operands have cap \(X^{100}\), its row-function
amplitude has cap \(X^{200}\), and its conditioning coefficient
operands are included in the \(X^{100}\) bound. Its shared-DAG
compiler has logarithmic sensitivity \(CR^7\log X\), scalar-history
propagation logarithm \(CR^9\log X\), and complete evaluation bounds
\[
 {\cal H}=2+b+CR^7\log_2X,\qquad
 T_{\rm row}\le C{\cal H}^{16},\qquad
 S_{\rm row}\le C{\cal H}^{6}.                            \tag{45}
\]

Here and below the fixed-primitive qualification in that source applies.
The following derivation verifies that whitening does not change these
numerical degrees. It is an author extension, not a fresh independent
review of that compiler.

Take a dyadic power \(\overline X\in[X,2X]\), increasing the fixed
constant \(C_*\) if necessary, and choose

\[
                  \tau=\overline X^{-512}.               \tag{46}
\]

The following raw bounds justify this choice. A learned-list coefficient
is bounded by the fixed residual and collocation bounds in the compiler's
physical schedule. A Gaussian mean coefficient is assembled from the
compiler's explicit conditioning operands, each capped at \(X^{100}\).
Concatenating histories and adding at most \(CR\) such contributions
gives entrywise bound \(\overline X^{101}\), and multiplying by the
at-most-\(CR\) row/column dimension gives

\[
                    \|A_0\|\le\overline X^{102}.          \tag{47}
\]

There is no product across all source times in this construction:
learned rank lists concatenate their factors, and the conditional mean
uses its current gapped matrix coefficients. Each matrix product used
inside such a coefficient was already part of the compiler's checked
operand bound. The readout raw coefficient vector obeys the same loose
norm bound.

For extra safety, do not rely on a fixed RMS bound for every master
history coordinate. The global row cap alone, with at most \(CR\)
coordinates, gives

\[
 \|S(z)\|\le\overline X^{101},\qquad
 q=\max(\|Q_{S,0}\|,\|Q_{T,0}\|)\le\overline X^{202}.       \tag{48}
\]

Physical Grams often obey the much smaller \(\overline X^2\) bound;
it is not needed here. With \(D\le3\tau\), (17), (47), and (48) give

\[
 2\|A_0\|\sqrt{D(q+D)}
 \le C\overline X^{102+101-256}
 =C\overline X^{-53}.                                    \tag{49}
\]

Even the very loose cap \(B^2\le\overline X^{200}\), together with
\(\sigma^{-2}\le\overline X^2\), gives variance error

\[
             DB^2/\sigma^2\le C\overline X^{-310}.        \tag{50}
\]

Every fixed-depth propagation factor in (27) is a fixed polynomial in
the physical \(B=C\ell^{3/2}\). It is at most \(\overline X\)
eventually for each fixed problem. Thus (49)--(50), including propagation,
are below \(n^{-10}\) at sufficiently large width. If an arbitrarily
large prescribed exponent \(a\) is wanted instead, replace 512 by
\(512+2a\); all degree conclusions below are unchanged.

For a globally defined query coefficient circuit one may use the
mathematical extension

\[
 Q_{\rm safe}=\tau I+(Q_{\rm obs}+\tau I)_+.              \tag{51}
\]

Here the positive part is the existing PSD matrix macro. On the good
event \(Q_{\rm obs}\succeq-\tau I/4\), so (51) equals
\(Q_{\rm obs}+2\tau I\) exactly. Globally it has floor \(\tau\).
An equivalent guarded implementation may test the same floor and return
a fixed default on failure. The former extension makes the Lipschitz
accounting direct. Numerical positive-part/root outputs use the
compiler's PSD-safe interface; allocate matrix error at most \(\tau/4\)
in operator norm and retain the remaining positive margin. Scalar noisy
observations themselves are still unclipped; the prescribed boxes apply
to their use inside coefficient routines.

To enumerate the added query graph, compute a square root and inverse
square root for each needed common history table, form the mean matrix
(16), form the forward-selection coefficient (19), transform one packet's
incoming/outgoing/readout marks, evaluate (24), (35), and form the vector
and scalar moment integrands. The number of history systems and query
layers is at most \(CR\); even padding their matrix products and every
scalar access gives at most \(CR^4\) added mathematical instructions.
The existing \(CR^7\) bound dominates this. No matrix dimension exceeds
the already permitted \(CR^2\).

Here are explicit range and conditioning margins for the new nodes:

\[
 \|Q_{\rm safe}^{-1/2}\|\le\overline X^{256},\quad
 \|Q_{\rm safe}^{1/2}\|\le C\overline X^{101},\quad
 \|U_S(z)\|\le\overline X^{357},\quad
 \|A\|\le C\overline X^{304}.                            \tag{52}
\]

The last bound is a global operand bound; the good-prefix physical
bound remains the much smaller (17). The variance coefficient has
exact norm at most one by (19) on every PSD-safe table. Guarded moments
have norm/range at most \(B,B^2\). Even bounding \(B\) by
\(\overline X^{100}\), mean partial sums, variance calculations,
whitened moment products, and streamed row accumulators lie below a
fixed power smaller than \(\overline X^{1000}\). For example the
mean's norm-product bound is
\(\overline X^{357+304+100}\), and one extra factor
\(\overline X^2\) safely covers scalar partial sums. A cross-moment
integrand is at most \(\overline X^{457}\); its unnormalized sum
over \(s\le n\le\overline X\) rows is at most
\(\overline X^{458}\).

The source's Gaussian root cap is \(\overline X^9\); the eventual
finite sampling cutoff \(O(\ell^{60})\) lies within it. For a new
ideal Gaussian query coordinate, clipping at \(\overline X^9\)
can be coupled to the unclipped coordinate with failure at most
\(2\exp(-\overline X^{18}/2)\). That exceptional probability is
charged in the Gaussian sampling event. No claim is made that a
finite cap is identically inactive on every Gaussian realization.
For clipped rows and guarded query contexts, choosing mathematical
operand cap \(\overline X^{4096}\) therefore changes none of the
preceding formulas. It also covers row-noise terms and fixed activation
values on their capped arguments. These are harmless larger query
caps; the smaller source caps remain in force for old row nodes.

For positive matrices with floor \(\tau\), the square-root and
inverse bounds from the explicit compiler imply

\[
 \|P^{-1/2}-Q^{-1/2}\|_F
 \le \tfrac12\tau^{-3/2}\|P-Q\|_F
 =\tfrac12\overline X^{768}\|P-Q\|_F.                    \tag{53}
\]

Indeed write inverse square root as the inverse of the positive square
root, apply the inverse bound with inverse-root norms at most
\(\tau^{-1/2}\), and then the square-root bound
\((2\sqrt\tau)^{-1}\). The other new inverses retain the \(\sigma^2\)
floor. PSD projection is nonexpansive. Entrywise/Frobenius conversions
cost a fixed power of \(R\le\overline X\). Binary operations on the
larger operand box, the gapped roots/inverses, and the fixed activation
primitives are consequently covered by the deliberately loose local
Lipschitz bound \(\overline X^{16384}\).

Topological induction through the enlarged shared DAG proves

\[
 \log\Lambda_{\rm query}\le CR^7\log\overline X=O(\ell^{58}),
 \qquad
 \log\Lambda_{\rm seq}\le CR^9\log\overline X=O(\ell^{74}).
 \tag{54}
\]

All coefficients in the powers above are fixed numbers. Increasing
their values changes constants in (54), not its exponents.
In particular, it would be incorrect to substitute the amplitude
\(\overline X^{4096}\) itself for its logarithm in a precision count.

For explicit scalar-noise and history schedules, the fixed confidence
thresholds give \(R\le\overline X^2\) and
\(T_\rho\le\overline X^2\) eventually. Choose a dyadic noise with

\[
 \log_2(1/\eta)\ge
 (a+3)\log_2(en)+C_\eta R^9\log_2\overline X
                         +520\log_2\overline X.          \tag{55}
\]

The first two terms are the source scalar-coupling allowance with the
new sensitivity constant. The last guarantees
\(R\eta T_\rho\le\overline X^{-516}\ll\tau/8\).
Thus (55) satisfies both source perturbation and common-Gram requirements,
with \(\log(1/\eta)=O(\ell^{74})\). It also gives the explicit
information degree \(H=O(\ell^{90})\), since \(P=O(\ell^{16})\);
the block lemma therefore still has \(\bar h=\operatorname{polylog}(n)/n\).

Let \(L_{\rm pair}\) include the sensitivity of each retained pair
test on the numerical-prefix ball. Enlarge the constant below to
dominate all final query/coefficient sensitivity constants in (54) as
well. Equation (54) and the source pair product rule give

\[
 \log_2(1+L_{\rm pair})\le C_{\rm pair}R^7\log_2\overline X.
\]

A sufficient retained-history bit accuracy is

\[
 b_h\ge (a+3)\log_2(en)+C_{\rm pair}R^7\log_2\overline X
                              +520\log_2\overline X.     \tag{56}
\]

With \(\varepsilon_{\rm hist}=2^{-b_h}\), it ensures
\(R(1+L_{\rm pair})\varepsilon_{\rm hist}\ll\tau/8\)
and the passive finite-circuit perturbation allowance. Together
(55)--(56) imply (13) with room for arithmetic matrix error.
The acquisition quantization recurrence requires only the additional
entry precision

\[
 b_{\rm entry}=b_h+CR^9\log_2\overline X+C\log_2(en).       \tag{57}
\]

Thus the concrete choice \(b_h=C_h\ell^{100}\) satisfies (56), and
(57) remains \(O(\ell^{100})\). This bound concerns actual selected
packet, weight, and noise rounding, so it includes the private-prefix
issue addressed above.

Finally, a context precision \(b_{\rm ctx}=C_{\rm ctx}\ell^{100}\)
dominates the full \(O(\ell^{74})\) exact-circuit sensitivity in (54).
Its deterministic map error is at most
\(\exp[-c\ell^{100}+C\ell^{74}]\), below \(n^{-a}\).
Requesting internal precision \(b=C_b\ell^{120}\) in (45), with the
larger constants now established, still gives

\[
 T_{\rm row}=O(\ell^{1920}),\qquad
 S_{\rm row}=O(\ell^{720}).                              \tag{58}
\]

The tiny floor (46) has logarithmic reciprocal only \(O(\ell^2)\);
it does not increase the 120 precision degree. The Gaussian cutoff
and uniform-bit constants must also satisfy the inequality following
Section 7's threshold discussion; they can do so at degree 120.
Consequently degrees 58, 74, 100, and 120 survive the observed-Gram
whitening, learned mean, variance selection, and raw query integrands.
This closes the explicit precision extension. The short-seed theorem
itself remains a separate supervisor interface, as stated in Section 7.
