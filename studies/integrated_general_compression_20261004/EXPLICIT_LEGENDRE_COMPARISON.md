# Numerical same-width Legendre comparison and a near-quarter order

2026-10-04. Assembly of three checked general components: explicit dense
fitting, explicit all-order closure fitting, and the general source carrier
event. The deterministic comparison is reconstructed in
`GENERAL_LEGENDRE_TRANSFER.md` §6. The order inversion below is a new
elementary calculation. No dense-to-population theorem is used.

Use the canonical Gaussian model and original residual-RMS-clock closure
defined in `GENERAL_LEGENDRE_TRANSFER.md` §§1–2. In particular both have
width \(n\), the same initialization, zero initial readout, the fixed
initialized mixers, and physical time. Let
\[
Y=\|y\|_2/\sqrt m,\qquad \lambda=\gamma/m>0,
\quad\|f-g\|_* =\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
\]
Assume the three numerical label conditions: the dense cap in
`GENERAL_EXPLICIT_FITTING.md` (7), the closure cap in
`GENERAL_EXPLICIT_CLOSURE_FITTING.md` (4), and the source cap in
`UNBOUNDED_COMPRESSOR_BRIDGE.md` (10), with its \(S=16Y/\lambda\).
Each is an explicit activation/depth constant times \(\gamma/m\).
There is no other trajectory assumption. All apply to unbounded values
in the common strip-analytic bounded-derivative class.

Write \(H\) for the Gaussian feature-moment maximum from the dense note,
\(s=\max(1,\max_\ell\|\phi_\ell'\|_\infty)\), and
\(t_2=\max_\ell\|\phi_\ell''\|_\infty\). Use the following constants:
\[
\kappa=\lambda/4,\quad R=8Y/\sqrt\lambda,\quad
T_0=9s,\quad F_z=2HT_0^{L-1},\quad
B=sT_0^{L-1}R,\quad P=1+2H(L-1),\quad G=PB+2H.
\tag{1}
\]
Let \(V_h\) and \(C_c\) be the explicit outputs (18)–(19) of the
closure fitting note. They are finite recurrences in the already defined
\(H,s,L,Y,\lambda\), not estimated or assumed response constants.

On the source event, for every sufficiently large width, the actual dense
all-time carrier maximum is at most
\[
M=2K_{\rm src}S\sqrt{\log(en)},\qquad S=16Y/\lambda,
\tag{2}
\]
where \(K_{\rm src}\) is the fully specified recurrence (22) in the
source bridge. Through its horizon the source gives the same bound without
the factor two; the exponentially decaying physical carrier tail justifies
that factor through infinity. The event has probability tending to one.
The source's stochastic width threshold remains unquantified.

Define, at each width,
\[
B_d=sT_0^{L-1}(1+B)+Lt_2F_zT_0^{L-1}M,
\quad J=PB_d+[1+(L-1)B]sF_z,
\]
\[
\mathcal A=\left(1+\frac{4GHB}{\kappa}\right)
\exp\left\{2J\left(1+\frac{4G^2}{\kappa}\right)\frac Y\kappa\right\},
\quad V_z=2F_zBP,
\]
\[
V_\delta=T_0^{L-1}
[4sH+4sH(L-1)B^2+Lt_2MV_z],
\quad a_0=Y/\kappa,
\quad F_h=V_h a_0\sqrt{(1+a_0)/2},
\]
\[
b_1=\frac{2\sqrt{1+a_0}}\kappa C_cB,
\quad b_0=\frac{\sqrt{1+a_0}Y}\kappa V_\delta+2B\sqrt{a_0},
\quad C_f=2H+RsF_z.
\tag{3}
\]
Every expression is numerical in the specified data, activation bounds,
depth, label amplitude and width.

For every integer
\[
q\ge q_{\rm abs}:=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A,
\tag{4}
\]
the simultaneous-in-order comparison is
\[
\boxed{
\|f_{n,q}-f_n\|_*
\le\frac{4(L-1)C_f\mathcal A F_h}{q^2}
                    (b_0+b_1\sqrt{\log q}).}
\tag{5}
\]
It uses the same single source event for every order; there is no countable
union of failure probabilities over \(q\).

To verify the assembly, the normalized parameter discrepancy \(D\) obeys
\(D\le\mathcal A\varepsilon\), where \(\varepsilon\) is the integrated
absolute reconstruction defect. The forward projection error is at most
\(F_h/q\). Recording the dense backward response in the closure clock,
then freezing after physical time \(2\log(q)/\kappa\), gives a backward
projection error at most
\((b_0+b_1\sqrt{\log q})/q+B_d\sqrt{a_0}D\).
The exact projection-error product consequently implies
\[
\varepsilon\le2(L-1)F_h
\left[\frac{b_0+b_1\sqrt{\log q}}{q^2}
       +\frac{B_d\sqrt{a_0}D}{q}\right].
\]
Condition (4) absorbs the last term. Forward subtraction on every query
and readout subtraction give output discrepancy at most \(C_fD\).
The fitting theorems supply both endpoint limits. This proves (5).

## A completely specified order

For \(Y>0\), define
\[
C_n=4(L-1)C_f\mathcal A F_h(b_0+b_1),\qquad
Q_n=\max\{3,q_{\rm abs},n^{1/4}\sqrt{C_n/Y}\},
\]
\[
\boxed{q_n=\left\lceil4Q_n\sqrt{\log(e+Q_n)}\right\rceil.}
\tag{6}
\]
This proves the strict, width-independent error coefficient
\[
\boxed{\|f_{n,q_n}-f_n\|_*\le Y/\sqrt n.}
\tag{7}
\]
Indeed \(q_n\le5Q_n\sqrt{\log(e+Q_n)}\) since \(Q_n\ge3\), and
\(\log(eq_n)\le4\log(e+Q_n)\). Thus
\[
\frac{C_n\sqrt{\log(eq_n)}}{q_n^2}
\le\frac{C_n}{8Q_n^2\sqrt{\log(e+Q_n)}}
\le\frac Y{\sqrt n}.
\]
The right side of (5) is bounded by the left side of this inequality.
Condition (4) holds by construction. For fixed nonzero labels and fixed
other problem parameters,
\(M=O(\sqrt{\log n})\), \(\log\mathcal A=O(\sqrt{\log n})\), and
all other coefficients in (3) grow at most polynomially in \(\sqrt{\log n}\).
Therefore
\[
q_n=n^{1/4+o(1)},\qquad
S_{\rm moving}=n(d+1)+1+2(L-1)mnq_n=n^{5/4+o(1)}.
\tag{8}
\]
There remain \((L-1)n^2\) fixed mixer entries. Formula (8) concerns moving
coordinates, not total retained storage. If \(Y=0\), the exact zero
predictor suffices and (6)'s division by \(Y\) is unnecessary.

At confidence \(1-\delta\), (5)–(8) hold for each sufficiently large
individual width. The intermediate fixed-order coefficient in (5) depends
on width through the explicitly displayed \(M\) and \(\mathcal A\).
The final coefficient one in (7) is independent of width and time, and
the base activation/data constants are independent of width and order.
They do not assert one simultaneous event over infinitely many independent
widths. The initialization width is explicit; the inherited source event's
eventual stochastic width is not. Consequently this is a numerical error
and order theorem with an asymptotic probability threshold, not a fully
effective bound on that threshold.
