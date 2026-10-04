# Removing the artificial quadratic depth exponent in runtime stability

2026-10-04. Candidate derivation, frozen before reading the new label route.
This continues the same architecture-constant investigation. It changes no
network, optimizer, observable, source tolerance, or clock. Complete inputs:
`EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md`, `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`
including its normalization addendum, `EXPLICIT_ARCHITECTURE_CONSTANTS.md`,
and their previously read construction and geometric-comparison prerequisites.
No experiment or external theorem is needed.

## 1. The avoidable loss

The previous runtime derivation used one source coefficient K for both the
initialized mixer norm and the carrier bound, then set its mixer tube to
R=K+1. The source estimate gives K<=beta^(5L), whereas the initialized
mixers are bounded by the numerical constant 8. Propagating through L
layers with the larger artificial tube produces a beta^(O(L²)) bound.

Use the actual initialized cap 8 and tube **R=9** instead. Keep the
source coefficient K separately, with K<=beta^(5L). Every occurrence of
R in the original proof bounds a mixer operator; every other occurrence
of K may retain its old bound. This substitution improves those estimates
without any new assumption.

Here beta=max(10,B,4B/a,32B/a²,16/a), B=max(1,B_phi), for the common
activation strip width a and bound B_phi. The real activation norm
B_rt=max(1,B_phi,2B_phi/a,8B_phi/a²) is at most beta. The scope is
L>=2 and fixed data with lambda=min(1,gamma/m)>0, label RMS Y,
s=Y/lambda, and coordinate source accuracy epsilon=n^-1<=Y.

The actual carrier input is the corrected direct bound

\[
 M\le1+4Ks\sqrt{\log(en)}.
\tag{1}
\]

It is not a bound normalized by the actual integral of residual activity.

## 2. Finite recurrences and their bounds

Use all definitions in equations (4), (7), (11)--(12), (14)--(15),
(17), (19), and (22) of `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md`, with
g=h=2B_rt and R=9. In this note call that route's backward coefficient
beta_ell by b_ell, and its maximum by b, to distinguish it from the
activation-only base beta. Thus

\[
b_\ell=g^{L-\ell+1}9^{L-\ell},\quad
U=(b_1^2+h^2\sum_{\ell=2}^L b_\ell^2)^{1/2},\quad
F_1=g,\quad F_\ell=g(h+9F_{\ell-1}).
\]

All remaining finite definitions are unchanged. The following bounds now
have exponents linear in depth:

| Quantity | Bound |
| --- | --- |
| b | beta^(3L) |
| U, F=max F_ell | beta^(5L), beta^(6L) |
| D_delta, W | beta^(6L), beta^(7L) |
| J0, V0 | beta^(8L), beta^(12L) |
| P_h, P_delta, D_r | beta^(11L), beta^(11L), beta^(12L) |
| A0, C_f | beta^(18L), beta^(25L) |
| H0, Z0 | beta^(33L), beta^(30L) |
| J1, D0 | beta^(39L), beta^(19L) |
| F0, T0' | beta^(48L), beta^(13L) |
| G | beta^(49L) |
| C1, C2, O0 | beta^(57L), beta^(55L), beta^(35L) |
| W1, T1 | beta^(17L), beta^(19L) |

To check the exponent accounting, gR<=18beta<=beta³, so b<=beta^(3L).
The sums in U and the affine recurrence for F cost at most a factor
polynomial in L times beta^(3L+2), giving the stated bounds since
L<=beta^(L-1). Since K<=beta^(5L), D_delta=3b+3K<=beta^(6L),
W=32(K+1)<=beta^(7L), and J0=h sqrt(L)(7b+3K)<=beta^(8L).
The two pairing coefficients are at most 29 beta^(10L), hence at most
beta^(11L). Substituting gives A0<=29 beta^(17L)<=beta^(18L),
C_f=F(1+A0)<=beta^(25L), and H0<=7 beta^(32L)<=beta^(33L).

Next Z0=L(gR)^L(D_delta+A0+C_f)<=3L beta^(28L)<=beta^(30L).
In J1 the largest summand is h b H0<=2beta^(36L+1); the sum and
sqrt(L) factor fit beta^(39L). The Gram-defect coefficient D0 is at
most 14L beta^(17L)<=beta^(19L). Thus F0<=38 beta^(47L)<=beta^(48L),
G<=12 beta^(48L)<=beta^(49L), and multiplication by 8+W/2 or 16K
gives the C1,C2 entries. The final readout coefficient is bounded by
6beta^(33L+1)<=beta^(35L). Finally W1<=84beta^(16L)<=beta^(17L),
and T1<=9beta^(17L+1)<=beta^(19L). All these inequalities hold for
beta>=10,L>=2.

## 3. Fitting, comparison and endpoint

The fitting argument's two numerical conditions are unchanged:
224FU s²<=1 and 6J0s<=1. They make hidden displacement at most 1/4,
which now closes the *actual* mixer tube 9 from its initialized bound 8.
The same exact raw energy, readout projection identity and geometric
cancellation therefore give the existing all-time error coefficient

\[
C_{\rm err}=
O_0\{1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}\}+8T_1,
\qquad s\le c.
\tag{2}
\]

This step uses no stronger source statement: the source norm defects and
the direct carrier bound (1) have exactly the form used in that proof.
The only altered parameter is the smaller justified mixer tube.

Put Q_rt=beta^(60L). The table implies that Q_rt bounds C1,C2,O0,T1,
as well as 6J0 and sqrt(224FU). Thus s<=Q_rt^-1 closes fitting and
the comparison, and makes the exponential in (2) at most e². The
same elementary bound as in the original explicit runtime route gives
C_err<=40 Q_rt²<=beta^(122L). Consequently, subject to the source
theorem's own label conditions,

\[
Y\le\lambda\beta^{-60L}
\quad\Longrightarrow\quad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{122L}\frac{Y}{\lambda^{3/2}\sqrt n}.
\tag{3}
\]

The endpoint is included by the unchanged integrated speed tail
4T1 Y lambda^(-3/2) exp(-lambda t/4). The horizon
32 lambda^-1 log(en) is more than sufficient. Since
lambda^(-3/2)<=B³(m/gamma)^(3/2), a bound entirely in gamma is

\[
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.
\tag{4}
\]

This replaces the quadratic depth exponent by a linear one. No
architecture-dependent factor has been discarded into a width threshold
to obtain this improvement. The remaining exponential-in-L estimates use
products of actual layer norm bounds. Removing those products requires
new information beyond separating the previously conflated constants.
