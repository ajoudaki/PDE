# Unit-variance sine depth-2 order-five supplement: frozen protocol

In addition to the raw-sine model frozen in `PROTOCOL.md`, evaluate

\[
\phi_{\rm unit}(x)
=\frac{\sin x}{s},
\qquad
s=\sqrt{E[\sin^2G]}
=\sqrt{\frac{1-e^{-2}}2}.
\]

Then \(E[\phi_{\rm unit}(G)^2]=1\), so both hidden preactivation variances
are one.  Architecture, initialization, trainable parameter blocks, metric,
and width-first derivative convention are otherwise unchanged.

Compute \(F^{(0)}(0),\ldots,F^{(5)}(0)\).  Orders zero, two, and four must
vanish by readout parity.

Two independently frozen unit-Gram representations must agree:

1. `UNIT_GRAM_ABC_NORMAL_FORM.txt`, SHA-256
   `3be176963679c40127ac4f94305eeb7e4ef684a06910ae99a68a0f3528333214`;
2. `independent_coefficient_map.json`, SHA-256
   `fa3b4a6f7dc665e63e2c02355a14122f89f56bdfd34f0fe7402be4cab0ff2878`.

Every moment atom is evaluated by the same closed finite-Fourier identity as
the raw-sine protocol, with the additional exact factor
\(s^{-\sum_r\nu_r}\).  Evaluations at 80 and 120 decimal digits must agree to
60 digits, the two coefficient maps must agree to 60 digits, and independent
Gauss--Hermite orders 64 and 96 must agree within \(10^{-10}\) at orders one
and three and \(10^{-7}\) at order five.

The previously frozen normalized-sine control values

\[
F'(0)=4.03709694646564\ldots,
\quad
F^{(3)}(0)=-103.257331146774\ldots,
\quad
F^{(5)}(0)=29944.4323429373\ldots
\]

are mandatory regression gates.  The hard bound is 60 seconds and 2 GiB.
The claim is limited to the formal width-first jet through order five.
