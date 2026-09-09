# Exact order-17 controls for the one-square models

Status: exact fixed-order Gaussian-program computation, 20 August 2026.

These calculations are controls for the autonomous-closure search.  They do
not by themselves identify a positive-time width limit.

## Inner square, outer identity (`QI`)

For

\[
X=u^2,\qquad Z=(W/\sqrt n)X,\qquad f=\langle A,Z\rangle_n,
\]

the odd feature derivatives through order seventeen are

\[
\begin{array}{c|r}
k&F^{(k)}(0)\\ \hline
1&10\\
3&2\,488\\
5&1\,807\,264\\
7&2\,811\,322\,240\\
9&7\,931\,589\,932\,800\\
11&36\,633\,883\,968\,687\,616\\
13&258\,368\,409\,013\,848\,153\,856\\
15&2\,644\,616\,553\,317\,851\,113\,395\,200\\
17&37\,777\,225\,785\,282\,950\,544\,101\,916\,928.
\end{array}
\]

All even derivatives through order sixteen vanish.  The output-coordinate
moments are

\[
\begin{aligned}
\mu_0&=\frac{311}{25},&
\mu_1&=\frac{34833}{12500},\\
\mu_2&=\frac{8251943}{3125000},&
\mu_3&=\frac{392518546363}{131250000000},\\
\mu_4&=\frac{251796847970537}{65625000000000},&
\mu_5&=\frac{411958057913114187103}{77962500000000000000},\\
\mu_6&=\frac{13543117561820459318374321}
{1773646875000000000000000},&
\mu_7&=\frac{1944504270982246098829861872709}
{170270100000000000000000000000}.
\end{aligned}
\]

The ordinary matrix `H_3=(mu_{i+j})_{i,j=0}^3` is positive definite, but the
new shifted gate fails:

\[
\boxed{
\det H_3^+=-
\frac{12717014161759221378928329747546434159184880978088665219012521749}
{1006179463097402343750000000000000000000000000000000000000000000000}<0.}
\]

Thus a nonnegative Stieltjes source is **not** the general one-source
mechanism for partially quadratic networks.  This conclusion is independent
of the zero radius of the raw feature-time series.

## Inner identity, outer square (`IQ`)

For

\[
X=u,\qquad Z=(W/\sqrt n)X,\qquad f=\langle A,Z^2\rangle_n,
\]

the odd feature derivatives are

\[
\begin{array}{c|r}
k&F^{(k)}(0)\\ \hline
1&11\\
3&5\,728\\
5&8\,078\,592\\
7&23\,535\,365\,120\\
9&120\,020\,610\,703\,360\\
11&968\,530\,631\,583\,031\,296\\
13&11\,581\,863\,675\,946\,373\,849\,088\\
15&196\,016\,892\,478\,863\,092\,515\,520\,512\\
17&4\,538\,853\,851\,710\,314\,308\,412\,825\,042\,944.
\end{array}
\]

The corresponding moments are

\[
\begin{aligned}
\mu_0&=\frac{2864}{121},&
\mu_1&=\frac{5296928}{483153},\\
\mu_2&=\frac{19228168896}{1071794405},&
\mu_3&=\frac{3296982597404864}{89873176242465},\\
\mu_4&=\frac{41387453198994354208}{489359444640221925},&
\mu_5&=\frac{4501642069143097853971736}{21494134886932467611775},\\
\mu_6&=\frac{1416492818915340351495296160968}
{2603391111640147409605799775},&
\mu_7&=\frac{6912550078610266626577410600198169}
{4725154867626867548434526591625}.
\end{aligned}
\]

Every available principal minor of `H_3` and `H_3^+` is strictly positive.
This is an order-17 compatibility result, not an all-order Stieltjes theorem.

## Reproduction and cross-check

[`partial_activation_recurrence.py`](partial_activation_recurrence.py)
implements the three exact scalar Gaussian recurrences.  In `both` mode it
reproduces every accepted canonical derivative through order nine.
[`test_partial_activation_recurrence.py`](test_partial_activation_recurrence.py)
freezes the three order-nine controls; all three tests pass.

