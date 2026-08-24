# Identity activation: exact order-thirteen extension

## Bottom line

Both identity architectures still pass **every** Stieltjes/Hankel condition
available after extending the feature jet through \(F^{(13)}(0)\).  At each
depth all six accessible ordinary and shifted matrices are positive definite:

\[
 H_0,H_1,H_2,H_0^+,H_1^+,H_2^+\succ0.
\]

All 23 distinct square minors of the infinite Hankel array that use only
\(\mu_0,\ldots,\mu_5\) are strictly positive.

## New exact derivatives and moments

| quantity | two hidden layers | three hidden layers |
|---|---:|---:|
| \(F^{(12)}(0)\) | \(0\) | \(0\) |
| \(F^{(13)}(0)\) | \(109038689280\) | \(111466749771776\) |
| \(\mu_5\) | \(63196828537/82864937925\) | \(314669435827/54499737600\) |
| decimal \(\mu_5\) | 0.762648595648 | 5.77377891498 |

The ordinary-Taylor and derivative-normalized jet assemblers agree exactly
through order thirteen.  Rational series reversion/composition and the
separate triangular identity \(F'(t)=K(F(t))\) agree exactly on all six
moments.

## Newly complete shifted matrix

For two hidden layers,

\[
H_2^+=
\begin{pmatrix}
67/81&6832/10935&414716/688905\\
6832/10935&414716/688905&182387864/279006525\\
414716/688905&182387864/279006525&63196828537/82864937925
\end{pmatrix}.
\]

Its new principal minors are

\[
\mu_1\mu_5-\mu_3^2
=\frac{12612365878909}{46984419803475}>0,
\]

\[
\mu_3\mu_5-\mu_4^2
=\frac{27212376873949924}{856291050918331875}>0,
\]

\[
\det H_2^+
=\frac{4662092676191348}{2157853448314196325}
\approx0.00216052331072>0.
\]

For three hidden layers,

\[
H_2^+=
\begin{pmatrix}
61/32&11131/5760&3235483/1290240\\
11131/5760&3235483/1290240&852431627/232243200\\
3235483/1290240&852431627/232243200&314669435827/54499737600
\end{pmatrix}.
\]

Its new principal minors are

\[
\mu_1\mu_5-\mu_3^2
=\frac{172787841942029}{36623823667200}>0,
\]

\[
\mu_3\mu_5-\mu_4^2
=\frac{1365134847024722833}{1356127870648320000}>0,
\]

\[
\det H_2^+
=\frac{114573182642874004393}{708802833725521920000}
\approx0.161643234467>0.
\]

Together with \(\mu_5>0\), these are the four new distinct PSD conditions.

## Newly accessible cross-Hankel minors

The four new non-principal two-by-two minors are:

| condition | two hidden layers | three hidden layers |
|---|---:|---:|
| \(\mu_0\mu_5-\mu_1\mu_4\) | \(371154772528/248594813775\) | \(3576078293971/163499212800\) |
| \(\mu_0\mu_5-\mu_2\mu_3\) | \(16482976712/9943792551\) | \(3927729989399/163499212800\) |
| \(\mu_1\mu_5-\mu_2\mu_4\) | \(7464124804567/33560299859625\) | \(921341510571233/235438866432000\) |
| \(\mu_2\mu_5-\mu_3\mu_4\) | \(526232669534896/6342896673469125\) | \(515107138477543/263691530403840\) |

Every value is strictly positive.

The two new non-principal three-by-three determinants, written by their
moment-index matrices, are:

| moment-index matrix | two hidden layers | three hidden layers |
|---|---:|---:|
| \(\begin{psmallmatrix}0&1&2\\1&2&3\\3&4&5\end{psmallmatrix}\) | \(1941659902332781/19028690020407375\) | \(86667224522660401/17579435360256000\) |
| \(\begin{psmallmatrix}0&1&2\\2&3&4\\3&4&5\end{psmallmatrix}\) | \(115285184467328464/2568873152754995625\) | \(1510605104345431393/527383060807680000\) |

Both are strictly positive.  Counting \(\mu_5\), the six new two-by-two
minors involving \(\mu_5\), and the three new three-by-three determinants,
all ten conditions newly exposed at order thirteen pass at both depths.

## Claim boundary

This is strict finite-order compatibility through \(H_2\) and \(H_2^+\),
not an infinite-sequence theorem.  The next ordinary matrix \(H_3\) needs
\(\mu_6\), hence \(F^{(15)}(0)\); the shifted \(H_3^+\) additionally needs
\(\mu_7\), hence \(F^{(17)}(0)\).

