# Depth-two identity: exact spectral closure and forty-moment audit

Status: **exact all-fixed-order formal closure; finite Stieltjes pass through
forty moments; no all-order Stieltjes theorem**, 20 August 2026.

> **Subsequent positive-time update.**  The formal spectral oscillator below
> has now been promoted to a deterministic, autonomous physical-MSE-time
> integro-differential limit, with compact-time finite-width identification
> and global limiting loss dynamics.  See
> [THEOREM_AND_PROOF.md](../depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md).
> This update does not change the still-open all-order Stieltjes claim.

## 1. Outcome

Depth two does have a genuine exact analogue of the depth-one solution, but
it is an implicit spectral fixed point rather than an elementary scalar
formula such as `sinh(2t)`.

Let

\[
x=A/\sqrt n,\qquad y=u/\sqrt n,\qquad B=W/\sqrt n.
\]

The feature-ascent characteristic flow is

\[
x'=By,\qquad y'=B^Tx,\qquad B'=xy^T,\qquad F=x^TBy.
\tag{1.1}
\]

The matrix

\[
C=BB^T-xx^T
\tag{1.2}
\]

is exactly conserved.  Consequently

\[
x''=(C+\|x\|^2+\|y\|^2)x.
\tag{1.3}
\]

The norm difference is also conserved and tends to zero at iid Gaussian
initialization.  Put

\[
r(t)=\lim_{n\to\infty}\|x(t)\|^2
    =\lim_{n\to\infty}\|y(t)\|^2.
\]

For each spectral parameter `lambda`, define

\[
\begin{aligned}
a_\lambda''&=(\lambda+2r)a_\lambda,
&a_\lambda(0)&=1,&a_\lambda'(0)&=0,\\
b_\lambda''&=(\lambda+2r)b_\lambda,
&b_\lambda(0)&=0,&b_\lambda'(0)&=1.
\end{aligned}
\tag{1.4}

Then the exact width-first formal closure is

\[
\boxed{
r(t)=\int a_\lambda(t)^2\,\rho_x(d\lambda)
     +\int b_\lambda(t)^2\,\rho_v(d\lambda),
\qquad F(t)=\frac12r'(t).}
\tag{1.5}

This is scalar self-consistency coupled to a one-parameter family of linear
ODEs.  It determines every fixed Taylor coefficient recursively.

## 2. The two explicit initialization measures

Let `MP` be the aspect-ratio-one Marchenko--Pastur law,

\[
d\rho_{MP}(\lambda)=
\frac1{2\pi}\sqrt{\frac{4-\lambda}{\lambda}}
\mathbf 1_{(0,4)}(\lambda)\,d\lambda.
\]

For `M=BB^T`, the rank-one resolvent identity gives

\[
x^T(z-C)^{-1}x
=\frac{x^T(z-M)^{-1}x}{1+x^T(z-M)^{-1}x}
\longrightarrow \frac{m_{MP}(z)}{1+m_{MP}(z)}.
\]

Therefore

\[
\boxed{
\rho_x=\frac34\delta_{-1/2}
+\frac{\sqrt{\lambda(4-\lambda)}}
       {2\pi(1+2\lambda)}\mathbf1_{(0,4)}(\lambda)d\lambda.}
\tag{2.1}

The initial velocity is `x'(0)=By`.  Isotropy and the fact that a fixed-rank
perturbation disappears from normalized traces give the size-biased law

\[
\boxed{
d\rho_v(\lambda)
=\lambda\,d\rho_{MP}(\lambda)
=\frac{\sqrt{\lambda(4-\lambda)}}{2\pi}
  \mathbf1_{(0,4)}(\lambda)d\lambda.}
\tag{2.2}

The cross spectral measure between `x(0)` and `x'(0)` vanishes.  As useful
checks,

\[
(\int\lambda^k\,d\rho_x)_{k\ge0}
=(1,0,1,2,6,18,57,186,\ldots),
\]

while `rho_v` has moments `C_(k+1)`.

These are spectral measures of the conserved initialization operator.  In
particular, the negative atom in `rho_x` does **not** make it a candidate
representing measure for the output-kernel moments $\mu_r$; those are
different objects.

## 3. Explicit all-order coefficient recurrence

Write

\[
a_\lambda=\sum_{k\ge0}a_k(\lambda)t^k,
\quad b_\lambda=\sum_{k\ge0}b_k(\lambda)t^k,
\quad r=\sum_{k\ge0}r_kt^k.
\]

Equation (1.4) becomes

\[
(k+2)(k+1)a_{k+2}
=\lambda a_k+2\sum_{i+j=k}r_i a_j,
\tag{3.1}
\]

and the identical recurrence for `b`.  Self-consistency gives

\[
r_k=\sum_{i+j=k}
\left(\int a_i a_j\,d\rho_x+\int b_i b_j\,d\rho_v\right).
\tag{3.2}

Finally,

\[
F^{(k)}(0)=\frac{(k+1)!}{2}r_{k+1}.
\tag{3.3}

Equations (3.1)--(3.3), followed by the triangular identity
`F'=K(F)`, are an exact all-fixed-order algorithm for every formal
output-kernel moment.  They are not a positivity proof for the resulting
infinite sequence.

## 4. Independent validation through order 81

The spectral recurrence was implemented without using an accepted feature
coefficient.  It agrees exactly with both linear-Gaussian detransposition
assemblers at every derivative through

\[
F^{(81)}(0)
=85458714898262995510692729243408517882087388069051120219314506246148492847511689601385343238271419432733444449591361536.
\]

After exact inversion/composition, all forty moments
`mu_0,...,mu_39` agree as well.  The first six remain

\[
\left(
\frac83,\frac{67}{81},\frac{6832}{10935},
\frac{414716}{688905},\frac{182387864}{279006525},
\frac{63196828537}{82864937925}
\right).
\]

The complete coefficient lists are in [RESULTS.json](RESULTS.json), and the
independent comparison is in
[SPECTRAL_CLOSURE_RESULTS.json](SPECTRAL_CLOSURE_RESULTS.json).

## 5. Closed-form search result

Using only `mu_0,...,mu_24`, the frozen search tested:

- algebraic equations for `M(q)=sum mu_r q^r` with degree at most four in
  `M`, degree at most six in `q`, and at most 25 fitted coefficients;
- polynomial recurrences of order at most four and coefficient degree at
  most four.

No candidate survived to test on `mu_25,...,mu_39`; in fact no unique
discovery relation appeared in the frozen classes.  A separate search for a
low-complexity equation after reducing the dynamics to `r''=G(r-1)` also
found none in the same bounded classes.

Thus (1.5) is presently the strongest exact closure.  It is not evidence
that no elementary or special-function formula exists outside the searched
classes.

## 6. Forty-moment Stieltjes audit

Exact rational LDL decompositions, independently checked by fraction-free
determinants, give

\[
H_d\succ0,\qquad H_d^+\succ0,
\qquad 0\le d\le19.
\]

All forty moment signs are positive.  This extends the earlier order-13
finite pass from `H_2,H_2^+` to `H_19,H_19^+`.  The exact determinants are
stored in [HANKEL40_RESULTS.json](HANKEL40_RESULTS.json).

The conclusion is deliberately finite: the spectral closure computes every
formal coefficient, but no representing measure for the output-kernel
moments and no proof that every future Hankel determinant is nonnegative has
been obtained.
