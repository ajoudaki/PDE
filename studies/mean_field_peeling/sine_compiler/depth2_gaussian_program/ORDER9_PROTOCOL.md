# Sine depth-2 derivatives and Stieltjes audit through order nine

## Canonical models

Use the same one-input, equal-width, two-hidden-layer network, standard
Gaussian initialization, unit metric on all parameter blocks, and width-first
operator

\[
D_n=n\nabla f_n\mathbin\cdot\nabla.
\]

Evaluate both already distinguished activations:

\[
\phi_{\rm raw}(x)=\sin x,
\qquad
\phi_{\rm unit}(x)=\lambda\sin x,
\qquad
\lambda=\sqrt{\frac2{1-e^{-2}}}.
\]

For either fixed \(\lambda\), put

\[
X=\lambda\sin U,
\quad C=\lambda\cos U,
\quad Z=n^{-1/2}WX,
\quad G=\lambda\sin Z,
\quad E=\lambda\cos Z,
\]

\[
f_n=n^{-1}A^\top G,
\qquad B=A\odot E,
\qquad R=n^{-1/2}W^\top B.
\]

The exact feature-ascent flow is

\[
\dot A=G,
\qquad
\dot W=n^{-1/2}BX^\top,
\qquad
\dot X=C^2\odot R,
\qquad
\dot C=-X\odot C\odot R.
\]

Also

\[
\dot G=E\odot\dot Z,
\qquad
\dot E=-G\odot\dot Z.
\]

No activation polynomial, Hermite truncation, unit-Gram substitution in the
raw model, finite-width extrapolation, or frozen-feature approximation is
allowed.

## Fixed-matrix Gaussian/Fourier reduction

Integrating \(W\) gives

\[
Z(t)=n^{-1/2}W_0X(t)
+\int_0^tB(s)\langle X(s),X(t)\rangle_n\,ds,
\]

\[
R(t)=n^{-1/2}W_0^\top B(t)
+\int_0^tX(s)\langle B(s),B(t)\rangle_n\,ds.
\]

Chronological detransposition uses column innovations \(\xi_k\), row
innovations \(\eta_k\), and the exact responses

\[
E[\eta_k\eta_j]=E[X_kX_j],
\qquad
\widehat Z_k=\eta_k+
\sum_{j<k}E[\partial_{\xi_j}X_k]B_j,
\]

\[
E[\xi_k\xi_j]=E[B_kB_j],
\qquad
\widehat R_k=\xi_k+
\sum_{j\le k}E[\partial_{\eta_j}B_k]X_j.
\]

Each scalar state is represented as a finite sum

\[
\sum_{\alpha,m}c_{\alpha,m}G^\alpha e^{imG_*},
\]

where \(G_*\) is the initial preactivation carrying the sine/cosine phase.
For a centered joint Gaussian with covariance \(\Sigma\), the tilted-Wick
recurrence is

\[
M_\alpha(m)=E[G^\alpha e^{imG_*}],
\]

\[
M_\alpha(m)
=im\Sigma_{j*}M_{\alpha-e_j}(m)
+\sum_k(\alpha_k-\delta_{jk})\Sigma_{jk}
M_{\alpha-e_j-e_k}(m),
\]

with \(M_0(m)=e^{-m^2\Sigma_{**}/2}\).  This evaluates every expectation
without numerical quadrature.

## Outputs and lower-order gates

Compute

\[
F^{(k)}(0)=\lim_{n\to\infty}D_n^kf_n,
\qquad 0\le k\le9,
\]

for both activations.  Readout reflection requires exact zeros at
\(k=0,2,4,6,8\).

The previously accepted order-five prefixes are mandatory gates:

\[
\begin{array}{c|ccc}
&F'(0)&F^{(3)}(0)&F^{(5)}(0)\\ \hline
\text{raw sine}
&1
&-1.88699982730593110088\ldots
&79.4149898161446530575\ldots\\
\text{unit sine}
&4.03709694646564177004\ldots
&-103.257331146774188914\ldots
&29944.4323429372823639\ldots
\end{array}
\]

## Independent coefficient routes and precision gates

1. Route T stores ordinary Taylor coefficients and uses Volterra
   denominators directly.
2. Route D stores actual derivatives and independently uses explicit
   binomial/multinomial and differentiated-Volterra weights.
3. The routes may share only sparse Fourier-polynomial arithmetic and the
   tilted-Wick expectation primitive.  Their output jets must agree through
   order nine to relative error below \(10^{-65}\) at 100 decimal digits.
4. Repeating Route T at 80 and 100 decimal digits must agree through order
   nine below \(10^{-55}\).
5. Every computed even derivative must have magnitude below \(10^{-70}\) at
   100 digits before being reported as the exact parity zero.

## Moment and Hankel audit

For each activation use

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=F'(0)+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2}.
\]

The order-nine jet determines exactly \(\mu_0,\ldots,\mu_3\).  Compute them
by two routes:

1. formal series reversion and composition;
2. the triangular identity \(F'(t)=K(F(t))\).

They must agree below \(10^{-65}\).  Audit all accessible matrices

\[
H_0=[\mu_0],
\quad H_0^+=[\mu_1],
\quad
H_1=\begin{pmatrix}\mu_0&\mu_1\\\mu_1&\mu_2\end{pmatrix},
\quad
H_1^+=\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}.
\]

Thus the six unique scalar PSD conditions are the four moment signs and

\[
\mu_0\mu_2-\mu_1^2\ge0,
\qquad
\mu_1\mu_3-\mu_2^2\ge0.
\]

Also report the redundant accessible cross minor
\(\mu_0\mu_3-\mu_1\mu_2\).  A sign is accepted only if it is stable between
80 and 100 digits and separated from zero by at least \(10^{-40}\); otherwise
it is inconclusive.

## Resource and claim boundary

- Maximum derivative order: nine.
- Per activation and coefficient route: 10 minutes and 4 GiB.
- Exhausting a resource or precision gate is inconclusive.
- Passing or failing a finite Hankel condition concerns only the stated sine
  activation.  No conclusion about the quadratic model, series convergence,
  positive-time dynamics, or arbitrary-order closure is licensed.
