# Identity activation: order-eleven Stieltjes/Hankel results

> **Endpoint update:** this order-eleven certificate remains valid, but its
> stopping point has been superseded by the exact order-thirteen extension in
> `ORDER13_RESULTS.md`, which determines \(\mu_5\) and \(H_2^+\).

## Verdict

For both two and three hidden layers, **every Stieltjes/Hankel condition
decidable from the exact derivatives through \(F^{(11)}(0)\) passes
strictly**.  In particular,

\[
 H_0,H_1,H_2,H_0^+,H_1^+\succ0
\]

at both depths.  All 13 distinct accessible square Hankel minors—five
one-by-one moment signs, seven two-by-two minors, and \(\det H_2\)—are
strictly positive.

The convention is

\[
 K_H(y)=F_H'\!\left(F_H^{-1}(y)\right)
 =F_H'(0)+\sum_{r\ge0}(-1)^r\mu_{r,H}y^{2r+2}.
\]

## Exact moments

| moment | two hidden layers | decimal | three hidden layers | decimal |
|---|---:|---:|---:|---:|
| \(\mu_0\) | \(8/3\) | 2.66666666667 | \(5\) | 5.00000000000 |
| \(\mu_1\) | \(67/81\) | 0.827160493827 | \(61/32\) | 1.90625000000 |
| \(\mu_2\) | \(6832/10935\) | 0.624782807499 | \(11131/5760\) | 1.93246527778 |
| \(\mu_3\) | \(414716/688905\) | 0.601993017905 | \(3235483/1290240\) | 2.50765981523 |
| \(\mu_4\) | \(182387864/279006525\) | 0.653704654398 | \(852431627/232243200\) | 3.67042663467 |

Rational series reversion/composition and a separately assembled triangular
solution of \(F'(t)=K(F(t))\) agree exactly on every entry.

## Complete PSD principal-minor audit

The five moment signs are all strictly positive.  The remaining distinct
principal-minor inequalities are:

| exact condition | two hidden layers | three hidden layers |
|---|---:|---:|
| \(\det H_1=\mu_0\mu_2-\mu_1^2\) | \(1193/1215\) | \(55559/9216\) |
| \(\det H_1^+=\mu_1\mu_3-\mu_2^2\) | \(90056012/837019575\) | \(1943047819/1857945600\) |
| \(H_2[\{0,2\}]=\mu_0\mu_4-\mu_2^2\) | \(125818816/93002175\) | \(15716963/1075200\) |
| \(H_2[\{1,2\}]=\mu_2\mu_4-\mu_3^2\) | \(982995978416/21356554456125\) | \(60275559699667/74912366592000\) |
| \(\det H_2\) | \(3447482166776/64069663368375\) | \(4045512994193/2080899072000\) |

Every displayed rational is positive.  Together with the positive diagonal
entries, these are all ten distinct scalar PSD inequalities supported by
five moments.  Hence all five accessible ordinary and shifted matrices are
positive definite.

## Cross-Hankel total-positivity diagnostics

The three accessible non-principal two-by-two Hankel minors also pass
strictly:

| exact condition | two hidden layers | three hidden layers |
|---|---:|---:|
| \(\mu_0\mu_3-\mu_1\mu_2\) | \(6748976/6200145\) | \(5712239/645120\) |
| \(\mu_0\mu_4-\mu_1\mu_3\) | \(1042313332/837019575\) | \(5043172849/371589120\) |
| \(\mu_1\mu_4-\mu_2\mu_3\) | \(3719967752/22599528525\) | \(7992083987/3715891200\) |

## Exact stopping point

The order-eleven feature jets determine only \(\mu_0,\ldots,\mu_4\).
The next moment \(\mu_5\), and therefore the shifted three-by-three matrix

\[
 H_2^+=
 \begin{pmatrix}
 \mu_1&\mu_2&\mu_3\\
 \mu_2&\mu_3&\mu_4\\
 \mu_3&\mu_4&\mu_5
 \end{pmatrix},
\]

requires \(F^{(13)}(0)\).  Thus the result is strict finite-order
compatibility, not a proof of an infinite Stieltjes moment sequence or a
representing measure.
