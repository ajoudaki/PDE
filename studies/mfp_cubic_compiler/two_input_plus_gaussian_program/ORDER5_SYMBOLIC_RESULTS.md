# Two-input raw-cubic plus channel: exact symbolic jet through order five

## Result

For two unit-RMS inputs, the parameter

\[
\rho=\frac{\langle x_1,x_2\rangle}{\|x_1\|\,\|x_2\|}
\]

is their cosine similarity; the geometric angle is
\(\arccos\rho\).  In the frozen two-hidden-layer raw-cubic model, define

\[
g=\frac{f_1+f_2}{2},\qquad
D_+=n\nabla g\mathbin\cdot\nabla,\qquad
F_+^{(k)}(0;\rho)=\lim_{n\to\infty}E[D_+^k g].
\]

The exact accepted symbolic jet is

\[
F_+^{(0)}=F_+^{(2)}=F_+^{(4)}=0,
\]

\[
\begin{aligned}
F_+^{(1)}(0;\rho)={}&\frac{305775}{2}+\frac{54675}{2}\rho
+45684\rho^3+39366\rho^5\\
&+32076\rho^7+8424\rho^9,
\end{aligned}
\]

\[
\begin{aligned}
F_+^{(3)}(0;\rho)={}&
19310071119750
+6082858923750\rho
+4950930928050\rho^2\\
&+16553736233190\rho^3
+14601768753564\rho^4
+21566517052140\rho^5\\
&+10179565523964\rho^6
+24773966615700\rho^7
+10747229306328\rho^8\\
&+8081925224220\rho^9
+9565735816224\rho^{10}
+5163082687008\rho^{12}\\
&+1993411099008\rho^{14}
+502141358592\rho^{16}
+45067456512\rho^{18},
\end{aligned}
\]

and

\[
\begin{aligned}
F_+^{(5)}(0;\rho)={}&
\frac{18976299600145783044375}{2}
+\frac{8566479134898122570625}{2}\rho\\
&+4182723155910015096750\rho^2
+13791857325918829217100\rho^3\\
&+\frac{35067920445973906393365}{2}\rho^4
+\frac{48109754419245214167015}{2}\rho^5\\
&+21522171320710240139550\rho^6
+38209489253942064977484\rho^7\\
&+27542359021746518299620\rho^8
+27219829067609211611802\rho^9\\
&+30802228745709036733470\rho^{10}
+16786702086870711026070\rho^{11}\\
&+22798964025459977630040\rho^{12}
+12091511501326180976400\rho^{13}\\
&+12510519670022170908240\rho^{14}
+7692735692047997089440\rho^{15}\\
&+4276358838817463285280\rho^{16}
+4436101670195976842880\rho^{17}\\
&+576486682116898855680\rho^{18}
+1925735466780118487808\rho^{19}\\
&+593508487276783607040\rho^{21}
+130087074546316120320\rho^{23}\\
&+17363028725221294080\rho^{25}
+884051241086048256\rho^{27}.
\end{aligned}
\]

The omitted coefficients of \(\rho^{20},\rho^{22},\rho^{24},\rho^{26}\)
in the last display are exactly zero.

## Requested correlations

All even derivatives listed here are zero.

| \(\rho\) | angle | \(F_+^{(1)}(0)\) | \(F_+^{(3)}(0)\) | \(F_+^{(5)}(0)\) |
|---:|---:|---:|---:|---:|
| \(0\) | \(90^\circ\) | \(305775/2\) | \(19310071119750\) | \(18976299600145783044375/2\) |
| \(1/2\) | \(60^\circ\) | \(11120895/64\) | \(1770631347661101/64\) | \(1119944003422467481309157877/65536\) |
| \(1\) | \(0^\circ\) | \(305775\) | \(154118008098000\) | \(302467842967104331335000\) |

The \(\rho=1\) row agrees exactly with the previously frozen one-input
raw-cubic jet through order five.

## Kernel consequence

Writing

\[
a=F_+^{(1)}(0;\rho),\qquad
b=F_+^{(3)}(0;\rho),\qquad
c=F_+^{(5)}(0;\rho),
\]

the output-coordinate kernel
\(K_+(y;\rho)=F_+'(F_+^{-1}(y;\rho);\rho)\) satisfies

\[
K_+(0)=a,\qquad K_+'(0)=K_+^{(3)}(0)=0,
\]

\[
K_+''(0)=\frac{b}{a^2},\qquad
K_+^{(4)}(0)=\frac{ac-4b^2}{a^5}.
\]

This is the kernel governing the genuine equal-label two-example MSE on
the exchange-symmetric width-first orbit.  A generic finite-width sample
still requires the full \(2\times2\) tangent-kernel matrix.

## Stieltjes moments and accessible Hankel conditions

Use

\[
K_+(y;\rho)=a(\rho)+\sum_{r\ge0}(-1)^r
\mu_r(\rho)y^{2r+2}.
\]

The order-five feature jet determines exactly two moment candidates:

\[
\mu_0(\rho)=\frac{b}{2a^2},
\qquad
\mu_1(\rho)=\frac{4b^2-ac}{24a^5}.
\]

Writing

\[
\begin{aligned}
a&=\frac{81}{2}(1+\rho)A(\rho),\\
b&=39366(1+\rho)^2P(\rho),\\
4b^2-ac&=\frac{387420489}{4}(1+\rho)^4N(\rho),
\end{aligned}
\]

gives the reduced exact forms

\[
\boxed{\mu_0(\rho)=\frac{12P(\rho)}{A(\rho)^2}},
\qquad
\boxed{\mu_1(\rho)=
\frac{N(\rho)}{27(1+\rho)A(\rho)^5}}.
\]

The coefficient lists for \(A,P,N\) are stored in
`stieltjes_order5_audit.json`.  Exact Sturm sequences show that all three
polynomials have no roots on \([-1,1]\) and are positive there.  Therefore

\[
\mu_0(\rho)>0,
\qquad
\mu_1(\rho)>0,
\qquad -1<\rho\le1.
\]

The exact requested values are

| \(\rho\) | \(\mu_0\) | \(\mu_1\) |
|---:|---:|---:|
| \(0\) | \(47090556/114005\) | \(9007737597469/441577832349375\) |
| \(1/2\) | \(146249888/319225\) | \(2226187969218708704/91794899448972309375\) |
| \(1\) | \(93960072/114005\) | \(5787193487251/147192610783125\) |

Thus the complete accessible Hankel matrices are

\[
H_0=[\mu_0]\succ0,
\qquad
H_0^+=[\mu_1]\succ0
\]

throughout the nondegenerate correlation interval.  The first genuine
two-by-two condition,

\[
\det H_1=\mu_0\mu_2-\mu_1^2\ge0,
\]

cannot be evaluated: \(\mu_2\) requires \(F_+^{(7)}(0;\rho)\).

At \(\rho=-1\), \(a=0\) and the plus-channel inverse is undefined.
Although \(\mu_0\) has the removable right limit
\(24558272/43923\), \(\mu_1\) has a positive simple pole.  Neither is an
output-coordinate moment at the degenerate endpoint.

## Validation and stopping boundary

The ordinary-Taylor and derivative-normalized Gaussian-program assemblers
agree coefficient-for-coefficient through order five.  A separately coded
connected-tree compiler reproduces the same polynomial.  Its direct
vertex-partition and quotient-Wick terminal evaluators agree on every one of
the 10,217 globally color-quotiented terminal keys reached through order
five.  Fixed exact evaluations at \(\rho=0,1/2,1\), lower-order regression,
readout parity, normalization, and the one-input endpoint all pass.

The separate exact Stieltjes audit derives the moment formulas by both series
reversion and the triangular identity, and then certifies the full-interval
signs by exact Sturm variation counts.

Order-seven connected runs reached their frozen resource caps, and a final
fixed-endpoint run was stopped when the requested scope was relaxed.  No
order-seven or order-nine value was emitted or accepted.  Those outcomes are
computationally inconclusive; they are not evidence that a higher derivative
does not exist.

The result is an exact fixed-order formal width-first calculation under the
accepted Gaussian-program/connected-tree assumptions.  It does not prove a
positive-time limit, convergence of the full Taylor series, or scalar
closure for generic finite-width/asymmetric dynamics.
