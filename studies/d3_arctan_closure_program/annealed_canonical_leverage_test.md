# Annealed test for the canonical bracket atom

## 1. Normalization and the exact atom

Use normalized row inner product and norm

\[
 \langle u,v\rangle_n=\frac1n\sum_{i=1}^n u_iv_i,
 \qquad \|u\|_n^2=\langle u,u\rangle_n.
\]

The fresh Ginibre block is normalized isonormally: if \(g\) is the fresh
row-space Gaussian innovation and \(P\) its conditional covariance
projection, write \(\mathcal I_g(w)\) for the corresponding matrix pairing,
so that

\[
 \mathbf E[\mathcal I_g(w)^2\mid\mathcal F^-]=\|Pw\|_n^2.   \tag{1}
\]

This convention absorbs the usual \(\sqrt n\) multiplying
\(\langle g,w\rangle_n\).  It is the normalization in which the canonical
Gaussian first-chaos transfer is an isometry.

In the notation of `predictor_chronological_decomposition.md`, the centered
old-chaos response at a fresh forward query has, to first order in the new
feature residual \(\alpha_k\),

\[
 \Delta M_{k,j}^{\rm old}
 =\alpha_k\mathcal I_{g_k}
 \!\left(P_k\operatorname{diag}(A^kd'(c_k))v_{k,j}\right)
 +o_{L^2}(\alpha_k).                                      \tag{2}
\]

Here \(v_{k,j}\) is the old canonical row-space representative of input
coordinate \(j\), normalized by

\[
 \|v_{k,j}\|_n\le1.                                     \tag{3}
\]

Thus the exact leading conditional bracket atom is

\[
 V_{k,j}^{\rm old}=\alpha_k^2
 \|P_k\operatorname{diag}(A^kd'(c_k))v_{k,j}\|_n^2.       \tag{4}
\]

There is an important qualification concerning Hanson--Wright.  The exact
fresh-quadratic term contains

\[
 \alpha g^2Dd(c,c+\alpha g)
 =g\{d(c+\alpha g)-d(c)\},                           \tag{4a}
\]

componentwise.  Hence

\[
 |\alpha gDd(c,c+\alpha g)|\le1,
 \qquad |\alpha g^2Dd(c,c+\alpha g)|\le|g|.          \tag{4b}
\]

Thus the exact quadratic-looking atom is dominated by a *linear* Gaussian
endpoint product.  Freezing \(Dd\) and applying Hanson--Wright is valid only
for the infinitesimal/bracket test (4); as a tail estimate for the full atom it
is strictly cruder and loses the arctangent saturation.  The issue tested
below is whether the sum of the genuine bracket atoms (4) has a width-uniform
annealed exponential moment when \(v_{k,j}\) is adapted to the same endpoint
marks.

## 2. Independent-mark leverage lemma

The following calculation shows that localization of the canonical direction
is harmless if it is independent of the Gaussian endpoint mark.

**Lemma.**  Let \(G_1,\ldots,G_n\) be independent \(N(0,1)\) variables.  Let
\(v_k\in\mathbb R^n\) and \(\alpha_k\ge0\) be deterministic relative to
\(G=(G_i)\), and suppose

\[
 S:=\sum_k\alpha_k^2\|v_k\|_n^2<\infty.              \tag{5}
\]

Then, for \(0\le\lambda<(2S)^{-1}\),

\[
 \mathbf E_G\exp\!\left\{
 \lambda\sum_k\alpha_k^2\|G\odot v_k\|_n^2\right\}
 \le \exp\!\left\{\frac{\lambda S}{1-2\lambda S}\right\}. \tag{6}
\]

*Proof.*  Put

\[
 w_i=\frac1n\sum_k\alpha_k^2v_{k,i}^2.
\]

Then \(\sum_iw_i=S\) and \(0\le w_i\le S\).  Independence gives exactly

\[
 \mathbf E_Ge^{\lambda\sum_iw_iG_i^2}
 =\prod_i(1-2\lambda w_i)^{-1/2}.
\]

For \(0\le x\le2\lambda S<1\),
\(-\log(1-x)\le x/(1-2\lambda S)\).  Taking logarithms of the product yields
(6).  Notice that no bound on \(\max_i|v_{k,i}|\) was used; a completely
localized canonical direction is allowed.

If \(A_i^k=G_i+c_i^k\), with \(|c_i^k|\le C_T\) even when \(c^k\) is random,
then

\[
 |A_i^k|^2\le2G_i^2+2C_T^2.                           \tag{7}
\]

Consequently the same conclusion holds, with changed constants, whenever the
families \((\alpha_k,v_k)\) are independent of the endpoint marks \(G\) and
(5) is bounded by a deterministic \(S_T\).

This proves that conditional Hanson--Wright plus the normalized canonical law
would be sufficient under genuine endpoint/canonical independence.  In
particular, localized directions are not by themselves an obstruction.

## 3. The exact joint-leverage lemma needed on the Euler orbit

On the actual orbit, \(v_{k,j}\), \(\alpha_k\), and \(c_k\) depend on \(A^0\)
through all previous forward/backward queries.  The precise missing statement
is the following.

**Joint causal leverage lemma (needed).**  For each finite \(T\), there should
exist \(\lambda_T,C_T>0\), independent of all widths and of the Euler mesh,
such that, for every coordinate \(j\),

\[
 \mathbf E\exp\!\left\{
 \lambda_T\sum_{k:t_k\le T}\alpha_k^2
 \|P_k\operatorname{diag}(A^kd'(c_k))v_{k,j}\|_n^2
 \right\}\le C_T.                                      \tag{JL}
\]

Endpoint atoms and the fresh-quadratic term require the same assertion with
\(d'\) replaced by the exact divided difference \(Dd\); since \(Dd\) is
uniformly bounded and \(|A^k-A^0|\le C_T\), (JL) is the strongest of these
weighted leverage requirements once the residual mass

\[
 S_{T,j}:=\sum_{k:t_k\le T}\alpha_k^2\|v_{k,j}\|_n^2       \tag{8}
\]

is controlled.

If (JL) holds, the conditional Gaussian linear atoms can be exponentiated by
(1).  The exact fresh-quadratic atoms should be estimated with (4a)--(4b), not
with a frozen-coefficient Hanson--Wright bound.  The Doob martingale in the
chronological decomposition is then \(\psi_1\).  The remaining
conditional-mean part must still be treated by the exact signed Abel identity;
(JL) addresses only the centered linearized bracket.

Neither Bessel nor the output energy proves (JL).  Bessel gives (3), but the
adapted choice \(v(A^0)=\sqrt n\,e_{\arg\max_i|A_i^0|}\) shows why (3) alone is
insufficient: the leverage is \(\max_i|A_i^0|^2\), whose exponential moment is
not width-uniform.  This example is only a test of the hypotheses, not a claim
that the Euler orbit realizes the argmax rule.  A proof of (JL) must use
causality of the actual canonical directions.

## 4. Whole-block cavity reduction

A block cavity gives a clean sufficient route to (JL), but it exposes a new
stability obligation.  Partition the output rows into a fixed number \(K\) of
blocks \(S_1,\ldots,S_K\).  For block \(S_r\), resample all endpoint marks and
all Ginibre rows in that block and construct a cavity orbit

\[
 (\alpha_k^{(-r)},v_{k,j}^{(-r)},c_k^{(-r)})_{k:t_k\le T}
\]

which is independent of the original marks \((A_i^0)_{i\in S_r}\) conditional
on the outside variables.  Define the unnormalized canonical residual

\[
 w_{k,j}:=\alpha_kv_{k,j},\qquad
 w_{k,j}^{(-r)}:=\alpha_k^{(-r)}v_{k,j}^{(-r)}.       \tag{9}
\]

The product \(w=\alpha v\), rather than the normalized direction \(v\), is
essential: it removes the discontinuity when a canonical residual is small.

For the pure cavity leverage

\[
 Q_r^{\rm cav}:=\frac1n\sum_{i\in S_r}(A_i^0)^2
       \sum_k|w_{k,j,i}^{(-r)}|^2,                  \tag{10}
\]

conditional integration over \((A_i^0)_{i\in S_r}\), followed by the proof of
(6), gives a uniform exponential moment provided

\[
 \sum_k\|w_{k,j}^{(-r)}\|_n^2\le S_T                \tag{11}
\]

almost surely (or with a sufficiently strong exponential tail).  Hölder with
exponents \(K\) yields

\[
 \mathbf E e^{\lambda\sum_rQ_r^{\rm cav}}
 \le\prod_{r=1}^K
       \{\mathbf E e^{\lambda KQ_r^{\rm cav}}\}^{1/K},       \tag{12}
\]

so a fixed \(K\) only shrinks the admissible \(\lambda\) by a fixed factor.
This proves that cross-dependence between different cavity blocks is harmless.

To compare the true and cavity leverages, the elementary inequality
\(|x|^2\le2|y|^2+2|x-y|^2\) leaves the error

\[
 \mathcal E_{T,j}^{\rm cav}
 :=\frac1n\sum_{r=1}^K\sum_{i\in S_r}(A_i^0)^2
       \sum_k|w_{k,j,i}-w_{k,j,i}^{(-r)}|^2.         \tag{13}
\]

Thus a whole-block cavity proves (JL) if, in addition to (11), one proves

\[
 \sup_{n,h,j}\mathbf E
       e^{\lambda_T\mathcal E_{T,j}^{\rm cav}}<\infty.       \tag{Cav}
\]

Equations (11) and (Cav) are the exact cavity obligations; no inverse Gram
matrix or canonical-direction denominator appears.

## 5. Why the cavity is not yet a proof

An \(L^2\) cavity estimate is insufficient for (Cav).  Differentiating the
unnormalized transported residual \(w=\alpha v\) between the true and
resampled orbits produces the same endpoint-weighted response as (2).  After
the diagonal arctangent curvature is dressed away, the lower-layer response
contains the exact off-diagonal commutator

\[
 \sum_{\ell\ne i}K_{i\ell}\frac{d_\ell}{d_i}R_{2,\ell}
       (d_\ell'\eta_\ell-d_i'\eta_i),               \tag{14}
\]

derived in `signed_predictor_abel_note.md`.  Energy controls the signed base
velocity, but it does not control the absolute or squared response in (14).
Accordingly, the estimates presently available give at most an \(L^2\) bound
for the cavity error, whereas (Cav) asks for an exponential bound on its
endpoint-weighted square.

A small canonical residual is not itself the problem: using \(w=\alpha v\)
in (13) removes that singularity.  The remaining problem is amplification of
the *unnormalized* row-cavity response by the adapted predictable part of
\(R_2\) in (14).  Proving (Cav) therefore requires the same signed response
continuation sought in the original theorem.  The whole-row/block cavity is a
valid reduction and it completely handles localization once (Cav) is known,
but it does not derive (Cav) from Bessel and energy; used without an additional
signed cancellation, it is circular.

## 6. Conclusion of the annealed test

1. Conditional Gaussian averaging neutralizes arbitrary localization when the
   endpoint marks are independent; formula (6) is the exact width-uniform
   estimate.  Hanson--Wright is appropriate for the frozen bracket, while the
   full divided-difference atom must use (4a)--(4b).
2. On the actual Euler orbit, the issue reduces precisely to the joint causal
   leverage estimate (JL).
3. A fixed-block cavity reduces (JL) to the residual-mass bound (11) and the
   exponentially weighted cavity stability estimate (Cav).
4. Bessel and the signed output energy do not prove (Cav); the first surviving
   term is the off-diagonal response commutator (14).

Hence annealing improves the pathwise bracket test substantially, but it does
not yet close the arbitrary-time theorem from the four stated inputs alone.
