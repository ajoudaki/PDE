# Arbitrary fixed depth, one sample, through order five: flattened scalar Gaussian recursion

## Result and exact scope

For every separately fixed hidden depth \(H\), in the shared-activation,
unit-forward-Gram regime

\[
Q^0=Q^1=\cdots=Q^H=1,
\]

the order-five population coefficient has a completely Wick--Stein-contracted,
one-dimensional-moment realization.  Every displayed transition below is a
finite polynomial in deterministic scalar states and

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
  \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\tag{0.1}
\]

No auxiliary Gaussian, multivariate expectation, covariance/response matrix,
random tangent or backward variable, pseudoinverse, or implicit Stein
derivative remains.

The exact witness uses six chronological sweeps, with dynamic scalar
dimensions

\[
\boxed{7\;/\;8\;/\;4\;/\;4\;/\;3\;/\;3}
\tag{0.2}
\]

and hence 29 coordinate types.  It is a full \(M\)-only contraction, but it
does **not** realize the stronger one-forward/one-backward schematic in the
research request.  Compressing these six sweeps into one bottom-up and one
top-down pass remains open.  No minimality claim is made.

The producer recurrences were frozen before cross-route inspection.  Exact
rational expansion agrees with the accepted maps at \(H=2,3,4\), and the two
separately frozen assemblers agree atom by atom on every terminal sector
through \(H=4\).

## 1. Exact differential identities

Let \(\theta\) be the original finite-width parameter vector and define the
rescaled derivative

\[
\widetilde\nabla=\sqrt n\,\nabla_\theta,\qquad
p=\widetilde\nabla f_n.
\]

Then the model's operator is exactly

\[
D_n=n\nabla_\theta f_n\mathbin\cdot\nabla_\theta
=p\mathbin\cdot\widetilde\nabla.
\tag{1.0}
\]

In these rescaled coordinates put

\[
\mathsf H_f=\widetilde\nabla^2f_n,\qquad
T=\widetilde\nabla^3f_n,\qquad
U=\widetilde\nabla^4f_n,\qquad
V=\widetilde\nabla^5f_n,
\]

and

\[
A=\mathsf H_fp,\qquad B=T[p,p],\qquad c=\mathsf H_f^2p,
\qquad U_3=U[p,p,p].
\]

Repeated ordinary product differentiation first gives

\[
\begin{aligned}
D_nf_n&=\langle p,p\rangle,\\
D_n^2f_n&=2\mathsf H_f[p,p],\\
D_n^3f_n&=2T[p,p,p]+4\langle A,A\rangle,\\
D_n^4f_n&=2U[p,p,p,p]+14T[A,p,p]+8\langle A,c\rangle.
\end{aligned}
\tag{1.1}
\]

Differentiating the last line once more before merging equal contractions
gives all six exact finite-width families:

\[
\begin{aligned}
D_n^5f_n={}&2V[p,p,p,p,p]+22U[A,p,p,p]+14\langle B,B\rangle\\
&+30\langle B,c\rangle+36T[A,A,p]+16\langle c,c\rangle.
\end{aligned}
\tag{1.2}
\]

Define the moving gradient jets

\[
m_2=D_n^2p=B+c,
\qquad
m_3=D_n^3p=U_3+3T[p,A]+\mathsf H_fm_2.
\tag{1.3}
\]

Then

\[
\langle A,m_3\rangle
=U[A,p,p,p]+3T[A,A,p]+\langle B,c\rangle+\langle c,c\rangle,
\]

so (1.2) is exactly equivalent to

\[
\boxed{
D_n^5f_n=2V[p^5]+10U[A,p^3]+10\langle B,m_2\rangle
+4\lVert m_2\rVert^2+12\langle A,m_3\rangle.}
\tag{1.4}
\]

This regrouping is the structural reason the order-five contraction closes
with four additional moving-jet passes.

## 2. Deterministic depth data and notation

Impose \(M_{200000}=1\) and write

\[
d=M_{020000},\qquad
b_\ell=d^{H-\ell},\qquad
\tau_\ell=\sum_{r=0}^{\ell}d^r.
\tag{2.1}
\]

In the literal transition appendices, `M020000` means \(M_{020000}\),
`l1` means the current \(\tau_{\ell-1}\), and every other lower-case token is
one of the deterministic scalar states declared below.  A suffix `_next`
means the next higher layer in a forward sweep or the next lower layer in a
reverse sweep.

The coordinate types are:

| sweep | direction | dimension | dynamic state |
|---|---|---:|---|
| F1 | bottom-up | 7 | \((u,v,w,x,y,j,k)\) |
| R1 | top-down | 8 | \((e02,e11,e13,e22,c10,c21,c30,c32)\) |
| F2 | bottom-up | 4 | \((q02,q22,qfm,a2)\) |
| R2 | top-down | 4 | \((r02,r22,rfm,d21)\) |
| F3 | bottom-up | 3 | \((q13,a30,a32)\) |
| R3 | top-down | 3 | \((r13,d30,d32)\) |

The implementation stores earlier layer values, as in an ordinary
forward/backward recursion, so memory is \(O(H)\) at fixed scalar type count.
Five R1 sources, three R2 sources, and one R3 source are deterministic outputs
of the displayed local maps; they are not additional dynamic transition
coordinates.  There are four order-five accumulators \((AC,Bm2,M2,Am3)\)
and one order-three accumulator \(\mathcal H\).

## 3. Sweep F1: frozen forward jet, dimension 7

Let

\[
f_\ell=(u_\ell,v_\ell,w_\ell,x_\ell,y_\ell,j_\ell,k_\ell).
\]

Initialize

\[
\begin{aligned}
u_1&=b_1M_{121000},&v_1&=3b_1^2M_{140010},
&w_1&=b_1M_{040000},\\
x_1&=3b_1^2M_{050100},&y_1&=3b_1^2M_{042000},
&j_1&=3b_1M_{030100},\\
k_1&=15b_1^2M_{050001}.&&
\end{aligned}
\tag{3.1}
\]

For \(2\leq\ell\leq H\), set

\[
b=b_\ell,\qquad l1=\tau_{\ell-1},\qquad
l3=j_{\ell-1}+3u_{\ell-1},\qquad
l5=k_{\ell-1}+5v_{\ell-1},
\tag{3.2}
\]

and apply all seven equations in Appendix A.  Define

\[
S_{3,H}=j_H+3u_H,\qquad S_{5,H}=k_H+5v_H.
\tag{3.3}
\]

The projection \((w,u,j)\) is exactly the accepted three-forward-scalar
recurrence of Section 7.1 of the order-three document.

## 4. Sweep R1: frozen gradient jet, dimension 8

Initialize at the top boundary

\[
(e02,e11,e13,e22,c10,c21,c30,c32)_{H}
=(0,0,0,0,1,0,0,0).
\tag{4.1}
\]

For \(\ell=H,H-1,\ldots,1\), use the stored \(f_{\ell-1}\), with
\(f_0=0\), and

\[
b=b_\ell,\qquad l1=\tau_{\ell-1},\qquad
l3=j_{\ell-1}+3u_{\ell-1}.
\tag{4.2}
\]

Evaluate every equation in Appendix B.  Store

\[
(s00,s02,s11,s13,s22)_\ell
=(source00,source02,source11,source13,source22)_\ell,
\tag{4.3}
\]

then send the eight `_next` values to layer \(\ell-1\).

Initialize

\[
AC=x_H,\qquad \mathcal H=w_H.
\]

For \(\ell\geq2\), add

\[
\begin{aligned}
AC&\mathrel{+}=s13_\ell+3s11_\ell u_{\ell-1}
+3s02_\ell w_{\ell-1}+s00_\ell x_{\ell-1},\\
\mathcal H&\mathrel{+}=s11_\ell+s00_\ell w_{\ell-1};
\end{aligned}
\tag{4.4}
\]

at \(\ell=1\), add \(s13_1\) and \(s11_1\).  Thus

\[
AC=U[A,p,p,p],\qquad
B_H=2S_{3,H}+4\mathcal H.
\tag{4.5}
\]

The \((w,u,j;e11,c10)\) projection is exactly the already-audited
three-forward/two-backward order-three recursion.

## 5. Sweep F2: moving feature jet of order two, dimension 4

Set

\[
(q02,q22,qfm,a2)_0=(0,0,0,0).
\tag{5.1}
\]

For \(\ell=1,\ldots,H\), use \(f_{\ell-1}\), the R1 state at \(\ell\),
the prior F2 state, and

\[
b=b_\ell,\qquad l1=\tau_{\ell-1},\qquad
l2=1+a2_{\ell-1}.
\tag{5.2}
\]

The four `feature2` equations in Appendix C give the next state.

## 6. Sweep R2: moving gradient jet of order two, dimension 4

Initialize

\[
(r02,r22,rfm,d21)_{H}=(0,0,0,1).
\tag{6.1}
\]

For \(\ell=H,\ldots,1\), apply the `gradient2` equations in Appendix C,
using (5.2) and the stored F1/R1/F2 values.  Store

\[
(t02,t22,tfm)_\ell
=(source02m,source22m,sourcefm)_\ell.
\tag{6.2}
\]

Initialize

\[
Bm2=qfm_H,\qquad M2=q22_H.
\]

For \(\ell\geq2\), add

\[
\begin{aligned}
Bm2\mathrel{+}={}&tfm_\ell+s02_\ell q02_{\ell-1}
+t02_\ell u_{\ell-1}+4s11_\ell w_{\ell-1}
+s00_\ell qfm_{\ell-1},\\
M2\mathrel{+}={}&t22_\ell+2t02_\ell q02_{\ell-1}
+4s11_\ell w_{\ell-1}+s00_\ell q22_{\ell-1}.
\end{aligned}
\tag{6.3}
\]

At \(\ell=1\), add \(tfm_1\) and \(t22_1\).  Then

\[
Bm2=\langle B,m_2\rangle,\qquad M2=\lVert m_2\rVert^2.
\tag{6.4}
\]

## 7. Sweep F3: moving feature jet of order three, dimension 3

Set

\[
(q13,a30,a32)_0=(0,0,0).
\tag{7.1}
\]

For \(\ell=1,\ldots,H\), use all stored lower-order states and

\[
\begin{aligned}
l2&=1+a2_{\ell-1},\\
l30&=4q02_{\ell-1}+3w_{\ell-1}+a30_{\ell-1},\\
l32&=1+a32_{\ell-1}.
\end{aligned}
\tag{7.2}
\]

The three `feature3` equations in Appendix C give the next state.

## 8. Sweep R3: moving gradient jet of order three, dimension 3

Initialize

\[
(r13,d30,d32)_{H}=(0,0,1).
\tag{8.1}
\]

For \(\ell=H,\ldots,1\), apply the `gradient3` equations in Appendix C and
store

\[
z13_\ell=source13m_\ell.
\tag{8.2}
\]

Initialize \(Am3=q13_H\).  For \(\ell\geq2\), add

\[
Am3\mathrel{+}=z13_\ell+3s11_\ell q02_{\ell-1}
+3t02_\ell w_{\ell-1}+s00_\ell q13_{\ell-1};
\tag{8.3}
\]

at \(\ell=1\), add \(z13_1\).  Therefore

\[
Am3=\langle A,m_3\rangle.
\tag{8.4}
\]

## 9. Terminal coefficients and Stieltjes-series data

The result is

\[
\boxed{
A_H=\tau_H,\qquad
B_H=2S_{3,H}+4\mathcal H,\qquad
C_H=2S_{5,H}+10AC+10Bm2+4M2+12Am3.}
\tag{9.1}
\]

Consequently

\[
\boxed{
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}.}
\tag{9.2}
\]

These are algebraic Taylor/Stieltjes-series coefficients.  Their existence
does not by itself prove positivity, complete monotonicity, or a Stieltjes
representation.

## 10. Why the stronger two-sweep form remains open

Order three closes after F1 and R1.  At order five, however, the secondary
feature tangent defining \(m_2\) depends on the differentiated reverse state
computed by R1.  Hence F2 cannot be run during F1.  The third moving feature
jet in turn depends on R2, so F3 cannot be run before R2.  The exact dependency
chain is

\[
\mathrm{F1}\to\mathrm{R1}\to\mathrm{F2}\to\mathrm{R2}
\to\mathrm{F3}\to\mathrm{R3}.
\tag{10.1}
\]

A putative one-forward/one-backward implementation would have to carry, in
F1, a function of an as-yet unknown top reverse boundary.  No audited
finite-dimensional scalar parametrization of that function is known; carrying
the function or its response operator would violate the requested terminal
grammar.  This is an obstruction for the present realization, not a proof
that every possible two-sweep realization is impossible.

## 11. Exact audits

Every comparison below used distributed coefficient maps and exact rational
arithmetic.

| depth | \(A_H\) terms | \(B_H\) terms | \(C_H\) terms | \(A/B/C\) discrepancies |
|---:|---:|---:|---:|---:|
| 2 | 3 | 46 | 974 | 0 / 0 / 0 |
| 3 | 4 | 160 | 6,519 | 0 / 0 / 0 |
| 4 | 5 | 350 | 17,641 | 0 / 0 / 0 |

The post-freeze two-route comparison separately canonicalized

\[
A,\ B,\ C,\ S_5,\ AC,\ Bm2,\ M2,\ Am3
\]

at \(H=1,2,3,4\); every sector had zero missing, extra, or unequal
coefficients.  The two assemblers were independently written, but they share
the independently frozen Route-A moving local transition table.  Thus this is
not mislabeled as two independent local Wick derivations.  The completion
chain is one full analytic local derivation, an independently written exact
reference loader/canonicalizer, exact comparison with pre-existing maps, and
hostile inspection.

The terminal scan found no residual scalar symbols, every atom had six
derivative slots, and the maximum activation derivative was exactly five.

## 12. Controls and the unit-Gram boundary

Genuine unit-Gram controls from the new recurrence are:

| activation | \(H\) | \(A_H\) | \(B_H\) | \(C_H\) |
|---|---:|---:|---:|---:|
| \(1\) | 2,3,4 | 1 | 0 | 0 |
| \(x\) | 2 | 3 | 48 | 1,464 |
| \(x\) | 3 | 4 | 160 | 13,888 |
| \(x\) | 4 | 5 | 400 | 73,240 |
| \((1+x)/\sqrt2\) | 2 | \(7/4\) | \(31/4\) | \(615/8\) |
| \((1+x)/\sqrt2\) | 3 | \(15/8\) | 12 | \(13447/64\) |
| \((1+x)/\sqrt2\) | 4 | \(31/16\) | \(479/32\) | \(179193/512\) |
| \(x^2/\sqrt3\) | 2 | \(37/9\) | \(561728/243\) | \(25800211040/6561\) |
| \(x^2/\sqrt3\) | 3 | \(175/27\) | \(191282624/6561\) | \(655126467433760/1594323\) |
| \(x^2/\sqrt3\) | 4 | \(781/81\) | \(51094842176/177147\) | \(10678160325919415648/387420489\) |

The canonical unnormalized quadratic \(\phi(x)=x^2\) is **not** a literal
specialization of the unit-Gram quotient: its forward Gram chain is

\[
(1,3,27,2187,14348907,\ldots).
\]

The accepted companion layer-tagged/arbitrary-Gram controls are

| \(H\) | \(A_H\) | \(B_H\) | \(C_H\) |
|---:|---:|---:|---:|
| 2 | 111 | 1,685,184 | 77,400,633,120 |
| 3 | 14,175 | 139,445,032,896 | 4,298,284,752,832,899,360 |
| 4 | 138,351,807 | 59,385,566,223,611,232,192 | 81,427,352,525,619,060,193,821,492,876,576 |

At \(H=2\), (9.2) therefore reproduces the accepted exact control

\[
\mu_{0,2}=\frac{280864}{4107},\qquad
\mu_{1,2}=\frac{38443196932}{5616860517}.
\tag{12.1}
\]

For clarity, merely substituting unnormalized \(x^2\) moments into the
already-quotiented unit recurrence gives the formal algebraic values

\[
\begin{array}{c|rrr}
H&A&B&C\\\hline
2&21&321600&9391605792\\
3&85&128455488&313377512166432\\
4&341&64111733568&17305789745609614368,
\end{array}
\]

which are not coefficients of the actual unnormalized quadratic network.

For the normalized smooth nonpolynomial activation

\[
\phi(x)=\frac{\sin x}{\sqrt{(1-e^{-2})/2}},
\]

96-point Gaussian quadrature gives

\[
\begin{array}{c|rrr}
H&A&B&C\\\hline
3&6.300850741690993&-854.3718615768605&1076854.459362389\\
4&9.273239352504905&-4566.130252113061&19488618.524776075.
\end{array}
\]

The preregistered 7,700-network finite-width regression passed at both
depths: the \(C\)-intercept z-scores were 1.200 and 0.475 and the affine
\(1/n\) fit p-values were 0.403 and 0.365.

## 13. Parity, derivative ceiling, and probability boundary

Readout reflection is exact at finite width and gives

\[
F_H(0)=F_H^{(2)}(0)=F_H^{(4)}(0)=0.
\tag{13.1}
\]

The finite-width fifth derivative contains activation derivatives only
through \(\phi^{(5)}\).  The inverse-free Wick--Stein elimination always
pairs a raw Gaussian factor before differentiating the base activation
product; the derivation aborts if a \(\phi^{(6)}\) factor would be generated.
The independent atom scan of every frozen transition and of the expanded
\(H=2,3,4\) roots confirms derivative ceiling five.

For a convenient theorem-level annealed limit at each separately fixed
\(H\), it is sufficient to assume \(\phi\in C^\infty\), every derivative of
\(\phi\) has polynomial growth, and the finite Tensor Program converges in
every finite \(L^p\).  A weaker bridge may instead use the required
convergence in probability together with, for some \(\epsilon>0\),

\[
\sup_n\mathbb E\lvert D_n^k f_n\rvert^{1+\epsilon}<\infty,
\qquad k=1,3,5.
\tag{13.2}
\]

The latter is the explicit uniform-integrability hypothesis that permits
interchanging the fixed-depth width limit and expectation.  Exact
finite-width differential identities require only the derivatives and
integrability actually appearing through order five; they do not by
themselves prove (13.2).

No claim here covers \(H=H(n)\), growing batch, fixed positive training time,
an all-orders series, a depth-uniform flattened-size bound, or a two-sweep
compression.

## 14. Evidence ladder and reproduction

The claims separate as follows:

1. (1.1), (1.2), (1.4), and readout parity are exact finite-width identities.
2. Appendices A--C are a formal population Wick--Stein contraction.
3. The exact H=2,3,4 and cross-route comparisons make that contraction an
   algebraically audited normal form.
4. The sine experiment is empirical finite-width support, not a proof.
5. Identification with \(\lim_n\mathbb E[D_n^k f_n]\) is theorem-level only
   under the stated fixed-depth regularity and uniform-integrability bridge.

Run the deterministic exact checker from the repository root:

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.run_checks
```

Its required summary is `C_counts = 974, 6519, 17641`, all discrepancy counts
zero, derivative ceiling 5, the two-route sector comparison passing, and the
normalized-sine regression gate passing.

# Appendix A: frozen forward transition

### `j_next`

```text
j_next = 3*M002000*l1*u + 3*M010100*l1*u + 3*M010100*l1*w + M020000*l3 + 3*M030100*b*l1^3
```

### `k_next`

```text
k_next = 15*M000200*l1*u^2 + 30*M001010*l1*u^2 + 30*M001010*l1*u*w + 5*M002000*l1*v + 10*M002000*l3*u + 15*M010001*l1*u^2 + 30*M010001*l1*u*w + 15*M010001*l1*w^2 + 5*M010100*l1*v + 20*M010100*l1*x + 15*M010100*l1*y + 10*M010100*l3*u + 10*M010100*l3*w + M020000*l5 + 90*M021010*b*l1^3*u + 30*M030001*b*l1^3*u + 30*M030001*b*l1^3*w + 30*M030100*b*l1^2*l3 + 15*M050001*b^2*l1^5
```

### `u_next`

```text
u_next = M020000*u + M101000*u + M101000*w + M121000*b*l1^2
```

### `v_next`

```text
v_next = 3*M002000*u^2 + 6*M010100*u^2 + 6*M010100*u*w + M020000*v + 6*M030100*b*l1^2*u + 3*M100010*u^2 + 6*M100010*u*w + 3*M100010*w^2 + M101000*v + 4*M101000*x + 3*M101000*y + 12*M111100*b*l1^2*u + 6*M120010*b*l1^2*u + 6*M120010*b*l1^2*w + 4*M121000*b*l1*l3 + 3*M140010*b^2*l1^4
```

### `w_next`

```text
w_next = M020000*w + M040000*b*l1^2
```

### `x_next`

```text
x_next = 3*M002000*u*w + 3*M010100*u*w + 3*M010100*w^2 + M020000*x + 9*M022000*b*l1^2*u + 3*M030100*b*l1^2*u + 6*M030100*b*l1^2*w + M040000*b*l1*l3 + 3*M050100*b^2*l1^4
```

### `y_next`

```text
y_next = 2*M002000*u^2 + 2*M002000*u*w + 3*M002000*w^2 + 2*M010100*u^2 + 2*M010100*u*w + M020000*y + 6*M022000*b*l1^2*u + 6*M022000*b*l1^2*w + 2*M030100*b*l1^2*u + 3*M042000*b^2*l1^4
```

# Appendix B: frozen reverse transition

### `c10_next`

```text
c10_next = M002000*b*l1 + M010100*b*l1 + M020000*b + M020000*c10 + M101000*c10
```

### `c21_next`

```text
c21_next = 2*M010100*b*l1 + M020000*c21 + 2*M101000*c10
```

### `c30_next`

```text
c30_next = 3*M000200*b*l1*u + 6*M001010*b*l1*u + 3*M001010*b*l1*w + M002000*b*l3 + 3*M002000*b*u + 3*M002000*c10*u + 3*M002000*c21*w + 2*M002000*c32*u + M002000*c32*w + 3*M002000*e02*l1 + 3*M010001*b*l1*u + 3*M010001*b*l1*w + M010100*b*l3 + 3*M010100*b*u + 3*M010100*b*w + 6*M010100*c10*u + 3*M010100*c10*w + 3*M010100*c21*w + 2*M010100*c32*u + M010100*c32*w + 3*M010100*e02*l1 + M020000*c30 + 3*M020000*e02 + 9*M021010*b^2*l1^3 + 9*M022000*b*c21*l1^2 + 3*M022000*b*c32*l1^2 + 3*M030001*b^2*l1^3 + 9*M030100*b^2*l1^2 + 3*M030100*b*c10*l1^2 + 3*M030100*b*c21*l1^2 + M030100*b*c32*l1^2 + 3*M040000*b*c21*l1 + 3*M100010*c10*u + 3*M100010*c10*w + M101000*c30 + 6*M111100*b*c10*l1^2 + 3*M120010*b*c10*l1^2 + 6*M121000*b*c10*l1
```

### `c32_next`

```text
c32_next = 3*M010100*b*l1 + M020000*c32 + 3*M101000*c10
```

### `e02_next`

```text
e02_next = M002000*b*u + M010100*b*u + M010100*b*w + M020000*e02 + 3*M030100*b^2*l1^2 + M040000*b*c21*l1 + 2*M121000*b*c10*l1
```

### `e11_next`

```text
e11_next = M002000*b*w + M020000*e11 + 3*M022000*b^2*l1^2 + 2*M121000*b*c10*l1 + M220000*c10^2
```

### `e13_next`

```text
e13_next = 3*M000200*b*u*w + 3*M001010*b*u*w + 3*M001010*b*w^2 + M002000*b*x + 3*M002000*e02*w + 3*M002000*e11*u + 3*M010100*e11*u + 3*M010100*e11*w + 18*M012100*b^2*l1^2*u + M020000*e13 + 9*M020200*b^2*l1^2*u + 9*M021010*b^2*l1^2*u + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l3 + 3*M022000*b*c10*l1*u + 9*M022000*b*c21*l1*w + 3*M022000*b*c32*l1*u + 3*M022000*b*c32*l1*w + 9*M022000*b*e02*l1^2 + 3*M030100*b*c10*l1*u + M030100*b*c32*l1*u + 3*M030100*b*e11*l1^2 + M040000*c10*c32*u + 15*M041010*b^3*l1^4 + 9*M042000*b^2*c21*l1^3 + 3*M042000*b^2*c32*l1^3 + 3*M103000*b*c10*l1*u + 12*M111100*b*c10*l1*u + 9*M111100*b*c10*l1*w + 3*M120010*b*c10*l1*u + 3*M120010*b*c10*l1*w + M121000*b*c10*l3 + M121000*b*c30*l1 + 6*M121000*c10^2*u + 3*M121000*c10*c21*w + 3*M121000*c10*c32*u + M121000*c10*c32*w + 3*M121000*c10*e02*l1 + 9*M131100*b^2*c10*l1^3 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*c21*l1^2 + M141000*b*c10*c32*l1^2 + 3*M202000*c10^2*u + 3*M210100*c10^2*u + 3*M210100*c10^2*w + M220000*c10*c30 + 3*M230100*b*c10^2*l1^2
```

### `e22_next`

```text
e22_next = 2*M000200*b*u^2 + 2*M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*u^2 + 2*M001010*b*u*w + M002000*b*y + 2*M002000*e02*u + 4*M002000*e11*w + 2*M010100*e02*u + 2*M010100*e02*w + 12*M012100*b^2*l1^2*u + M020000*e22 + 6*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*u + 4*M022000*b*c10*l1*u + 6*M022000*b*c21*l1*u + 4*M022000*b*e11*l1^2 + 2*M030100*b*c21*l1*u + 6*M030100*b*c21*l1*w + 6*M030100*b*e02*l1^2 + M040000*c21^2*w + 2*M040000*c21*e02*l1 + 15*M040200*b^3*l1^4 + 6*M050100*b^2*c21*l1^3 + M060000*b*c21^2*l1^2 + 4*M103000*b*c10*l1*u + 8*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 4*M121000*c10*c21*w + 4*M121000*c10*e02*l1 + 12*M131100*b^2*c10*l1^3 + 4*M141000*b*c10*c21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2
```

### `source00`

```text
source00 = M020000*b
```

### `source02`

```text
source02 = M002000*b*u + M010100*b*u + M010100*b*w + M020000*e02 + 3*M030100*b^2*l1^2 + M040000*b*c21*l1 + 2*M121000*b*c10*l1
```

### `source11`

```text
source11 = M002000*b*w + M020000*e11 + 3*M022000*b^2*l1^2 + 2*M121000*b*c10*l1 + M220000*c10^2
```

### `source13`

```text
source13 = 3*M000200*b*u*w + 3*M001010*b*u*w + 3*M001010*b*w^2 + M002000*b*x + 3*M002000*e02*w + 3*M002000*e11*u + 3*M010100*e11*u + 3*M010100*e11*w + 18*M012100*b^2*l1^2*u + M020000*e13 + 9*M020200*b^2*l1^2*u + 9*M021010*b^2*l1^2*u + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l3 + 3*M022000*b*c10*l1*u + 9*M022000*b*c21*l1*w + 3*M022000*b*c32*l1*u + 3*M022000*b*c32*l1*w + 9*M022000*b*e02*l1^2 + 3*M030100*b*c10*l1*u + M030100*b*c32*l1*u + 3*M030100*b*e11*l1^2 + M040000*c10*c32*u + 15*M041010*b^3*l1^4 + 9*M042000*b^2*c21*l1^3 + 3*M042000*b^2*c32*l1^3 + 3*M103000*b*c10*l1*u + 12*M111100*b*c10*l1*u + 9*M111100*b*c10*l1*w + 3*M120010*b*c10*l1*u + 3*M120010*b*c10*l1*w + M121000*b*c10*l3 + M121000*b*c30*l1 + 6*M121000*c10^2*u + 3*M121000*c10*c21*w + 3*M121000*c10*c32*u + M121000*c10*c32*w + 3*M121000*c10*e02*l1 + 9*M131100*b^2*c10*l1^3 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*c21*l1^2 + M141000*b*c10*c32*l1^2 + 3*M202000*c10^2*u + 3*M210100*c10^2*u + 3*M210100*c10^2*w + M220000*c10*c30 + 3*M230100*b*c10^2*l1^2
```

### `source22`

```text
source22 = 2*M000200*b*u^2 + 2*M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*u^2 + 2*M001010*b*u*w + M002000*b*y + 2*M002000*e02*u + 4*M002000*e11*w + 2*M010100*e02*u + 2*M010100*e02*w + 12*M012100*b^2*l1^2*u + M020000*e22 + 6*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*u + 4*M022000*b*c10*l1*u + 6*M022000*b*c21*l1*u + 4*M022000*b*e11*l1^2 + 2*M030100*b*c21*l1*u + 6*M030100*b*c21*l1*w + 6*M030100*b*e02*l1^2 + M040000*c21^2*w + 2*M040000*c21*e02*l1 + 15*M040200*b^3*l1^4 + 6*M050100*b^2*c21*l1^3 + M060000*b*c21^2*l1^2 + 4*M103000*b*c10*l1*u + 8*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 4*M121000*c10*c21*w + 4*M121000*c10*e02*l1 + 12*M131100*b^2*c10*l1^3 + 4*M141000*b*c10*c21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2
```

# Appendix C: moving-gradient transitions

## feature2

### `a2_next`

```text
a2_next = M020000*l2
```

### `q02_next`

```text
q02_next = M020000*q02 + M101000*q02 + M101000*w + M121000*b*l1^2 + M121000*b*l1*l2 + M220000*c10*l2
```

### `q22_next`

```text
q22_next = 2*M002000*q02^2 + 2*M002000*q02*w + 3*M002000*w^2 + 2*M010100*q02^2 + 2*M010100*q02*w + M020000*q22 + 6*M022000*b*l1^2*q02 + 6*M022000*b*l1^2*w + 6*M022000*b*l1*l2*q02 + 6*M022000*b*l1*l2*w + M022000*b*l2^2*w + 2*M030100*b*l1^2*q02 + 2*M030100*b*l1*l2*q02 + 2*M040000*c10*l2*q02 + M040000*e11*l2^2 + 3*M042000*b^2*l1^4 + 6*M042000*b^2*l1^3*l2 + 3*M042000*b^2*l1^2*l2^2 + 6*M121000*c10*l2*q02 + 2*M121000*c10*l2*w + 2*M141000*b*c10*l1^2*l2 + 2*M141000*b*c10*l1*l2^2 + M240000*c10^2*l2^2
```

### `qfm_next`

```text
qfm_next = 2*M002000*q02*u + M002000*q02*w + M002000*u*w + 3*M002000*w^2 + 2*M010100*q02*u + M010100*q02*w + M010100*u*w + M020000*qfm + 3*M022000*b*l1^2*q02 + 3*M022000*b*l1^2*u + 6*M022000*b*l1^2*w + 3*M022000*b*l1*l2*u + 3*M022000*b*l1*l2*w + M030100*b*l1^2*q02 + M030100*b*l1^2*u + M030100*b*l1*l2*u + M040000*c10*l2*u + 3*M042000*b^2*l1^4 + 3*M042000*b^2*l1^3*l2 + 3*M121000*c10*l2*u + M121000*c10*l2*w + M141000*b*c10*l1^2*l2
```

## gradient2

### `d21_next`

```text
d21_next = M002000*b*l2 + 2*M010100*b*l1 + M020000*b + M020000*d21 + 2*M101000*c10
```

### `r02_next`

```text
r02_next = M002000*b*q02 + M010100*b*q02 + M010100*b*w + M020000*r02 + 3*M022000*b^2*l1*l2 + 3*M030100*b^2*l1^2 + M040000*b*d21*l1 + 2*M121000*b*c10*l1 + M121000*b*c10*l2
```

### `r22_next`

```text
r22_next = 2*M000200*b*q02^2 + 2*M000200*b*q02*w + 3*M000200*b*w^2 + 2*M001010*b*q02^2 + 2*M001010*b*q02*w + M002000*b*q22 + 4*M002000*e11*w + 2*M002000*q02*r02 + 6*M004000*b^2*l1*l2*q02 + 3*M004000*b^2*l2^2*w + 2*M010100*q02*r02 + 2*M010100*r02*w + 12*M012100*b^2*l1^2*q02 + 18*M012100*b^2*l1*l2*q02 + 18*M012100*b^2*l1*l2*w + M020000*r22 + 6*M020200*b^2*l1^2*q02 + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*q02 + 4*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l2*q02 + 6*M022000*b*d21*l1*q02 + 2*M022000*b*d21*l2*w + 4*M022000*b*e11*l1^2 + 4*M022000*b*e11*l1*l2 + M022000*b*e11*l2^2 + 6*M022000*b*l1*l2*r02 + 15*M024000*b^3*l1^2*l2^2 + 2*M030100*b*d21*l1*q02 + 6*M030100*b*d21*l1*w + 6*M030100*b*l1^2*r02 + 30*M032100*b^3*l1^3*l2 + M040000*d21^2*w + 2*M040000*d21*l1*r02 + 15*M040200*b^3*l1^4 + 6*M042000*b^2*d21*l1^2*l2 + 6*M050100*b^2*d21*l1^3 + M060000*b*d21^2*l1^2 + 4*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l2*q02 + 4*M103000*b*c10*l2*w + 8*M111100*b*c10*l1*q02 + 12*M111100*b*c10*l1*w + 4*M111100*b*c10*l2*q02 + 2*M111100*b*c10*l2*w + 4*M121000*c10*d21*w + 4*M121000*c10*l1*r02 + 2*M121000*c10*l2*r02 + 12*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1*l2^2 + 12*M131100*b^2*c10*l1^3 + 6*M131100*b^2*c10*l1^2*l2 + 4*M141000*b*c10*d21*l1^2 + 2*M141000*b*c10*d21*l1*l2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 4*M222000*b*c10^2*l1*l2 + M222000*b*c10^2*l2^2
```

### `rfm_next`

```text
rfm_next = 2*M000200*b*q02*u + M000200*b*q02*w + M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*q02*u + M001010*b*q02*w + M001010*b*u*w + M002000*b*qfm + M002000*e02*q02 + 4*M002000*e11*w + M002000*r02*u + 3*M004000*b^2*l1*l2*u + M010100*e02*q02 + M010100*e02*w + M010100*r02*u + M010100*r02*w + 6*M012100*b^2*l1^2*q02 + 6*M012100*b^2*l1^2*u + 9*M012100*b^2*l1*l2*u + 9*M012100*b^2*l1*l2*w + M020000*rfm + 3*M020200*b^2*l1^2*q02 + 3*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 3*M021010*b^2*l1^2*q02 + 3*M021010*b^2*l1^2*u + 2*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l1*u + M022000*b*c10*l2*u + 3*M022000*b*c21*l1*q02 + M022000*b*c21*l2*w + 3*M022000*b*d21*l1*u + 3*M022000*b*e02*l1*l2 + 4*M022000*b*e11*l1^2 + 2*M022000*b*e11*l1*l2 + M030100*b*c21*l1*q02 + 3*M030100*b*c21*l1*w + M030100*b*d21*l1*u + 3*M030100*b*d21*l1*w + 3*M030100*b*e02*l1^2 + 3*M030100*b*l1^2*r02 + 15*M032100*b^3*l1^3*l2 + M040000*c21*d21*w + M040000*c21*l1*r02 + M040000*d21*e02*l1 + 15*M040200*b^3*l1^4 + 3*M042000*b^2*c21*l1^2*l2 + 3*M050100*b^2*c21*l1^3 + 3*M050100*b^2*d21*l1^3 + M060000*b*c21*d21*l1^2 + 2*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l1*u + M103000*b*c10*l2*u + 2*M103000*b*c10*l2*w + 4*M111100*b*c10*l1*q02 + 4*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 2*M111100*b*c10*l2*u + M111100*b*c10*l2*w + 2*M121000*c10*c21*w + 2*M121000*c10*d21*w + 2*M121000*c10*e02*l1 + M121000*c10*e02*l2 + 2*M121000*c10*l1*r02 + 6*M123000*b^2*c10*l1^2*l2 + 12*M131100*b^2*c10*l1^3 + 3*M131100*b^2*c10*l1^2*l2 + 2*M141000*b*c10*c21*l1^2 + M141000*b*c10*c21*l1*l2 + 2*M141000*b*c10*d21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 2*M222000*b*c10^2*l1*l2
```

### `source02m`

```text
source02m = M002000*b*q02 + M010100*b*q02 + M010100*b*w + M020000*r02 + 3*M022000*b^2*l1*l2 + 3*M030100*b^2*l1^2 + M040000*b*d21*l1 + 2*M121000*b*c10*l1 + M121000*b*c10*l2
```

### `source22m`

```text
source22m = 2*M000200*b*q02^2 + 2*M000200*b*q02*w + 3*M000200*b*w^2 + 2*M001010*b*q02^2 + 2*M001010*b*q02*w + M002000*b*q22 + 4*M002000*e11*w + 2*M002000*q02*r02 + 6*M004000*b^2*l1*l2*q02 + 3*M004000*b^2*l2^2*w + 2*M010100*q02*r02 + 2*M010100*r02*w + 12*M012100*b^2*l1^2*q02 + 18*M012100*b^2*l1*l2*q02 + 18*M012100*b^2*l1*l2*w + M020000*r22 + 6*M020200*b^2*l1^2*q02 + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*q02 + 4*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l2*q02 + 6*M022000*b*d21*l1*q02 + 2*M022000*b*d21*l2*w + 4*M022000*b*e11*l1^2 + 4*M022000*b*e11*l1*l2 + M022000*b*e11*l2^2 + 6*M022000*b*l1*l2*r02 + 15*M024000*b^3*l1^2*l2^2 + 2*M030100*b*d21*l1*q02 + 6*M030100*b*d21*l1*w + 6*M030100*b*l1^2*r02 + 30*M032100*b^3*l1^3*l2 + M040000*d21^2*w + 2*M040000*d21*l1*r02 + 15*M040200*b^3*l1^4 + 6*M042000*b^2*d21*l1^2*l2 + 6*M050100*b^2*d21*l1^3 + M060000*b*d21^2*l1^2 + 4*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l2*q02 + 4*M103000*b*c10*l2*w + 8*M111100*b*c10*l1*q02 + 12*M111100*b*c10*l1*w + 4*M111100*b*c10*l2*q02 + 2*M111100*b*c10*l2*w + 4*M121000*c10*d21*w + 4*M121000*c10*l1*r02 + 2*M121000*c10*l2*r02 + 12*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1*l2^2 + 12*M131100*b^2*c10*l1^3 + 6*M131100*b^2*c10*l1^2*l2 + 4*M141000*b*c10*d21*l1^2 + 2*M141000*b*c10*d21*l1*l2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 4*M222000*b*c10^2*l1*l2 + M222000*b*c10^2*l2^2
```

### `sourcefm`

```text
sourcefm = 2*M000200*b*q02*u + M000200*b*q02*w + M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*q02*u + M001010*b*q02*w + M001010*b*u*w + M002000*b*qfm + M002000*e02*q02 + 4*M002000*e11*w + M002000*r02*u + 3*M004000*b^2*l1*l2*u + M010100*e02*q02 + M010100*e02*w + M010100*r02*u + M010100*r02*w + 6*M012100*b^2*l1^2*q02 + 6*M012100*b^2*l1^2*u + 9*M012100*b^2*l1*l2*u + 9*M012100*b^2*l1*l2*w + M020000*rfm + 3*M020200*b^2*l1^2*q02 + 3*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 3*M021010*b^2*l1^2*q02 + 3*M021010*b^2*l1^2*u + 2*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l1*u + M022000*b*c10*l2*u + 3*M022000*b*c21*l1*q02 + M022000*b*c21*l2*w + 3*M022000*b*d21*l1*u + 3*M022000*b*e02*l1*l2 + 4*M022000*b*e11*l1^2 + 2*M022000*b*e11*l1*l2 + M030100*b*c21*l1*q02 + 3*M030100*b*c21*l1*w + M030100*b*d21*l1*u + 3*M030100*b*d21*l1*w + 3*M030100*b*e02*l1^2 + 3*M030100*b*l1^2*r02 + 15*M032100*b^3*l1^3*l2 + M040000*c21*d21*w + M040000*c21*l1*r02 + M040000*d21*e02*l1 + 15*M040200*b^3*l1^4 + 3*M042000*b^2*c21*l1^2*l2 + 3*M050100*b^2*c21*l1^3 + 3*M050100*b^2*d21*l1^3 + M060000*b*c21*d21*l1^2 + 2*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l1*u + M103000*b*c10*l2*u + 2*M103000*b*c10*l2*w + 4*M111100*b*c10*l1*q02 + 4*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 2*M111100*b*c10*l2*u + M111100*b*c10*l2*w + 2*M121000*c10*c21*w + 2*M121000*c10*d21*w + 2*M121000*c10*e02*l1 + M121000*c10*e02*l2 + 2*M121000*c10*l1*r02 + 6*M123000*b^2*c10*l1^2*l2 + 12*M131100*b^2*c10*l1^3 + 3*M131100*b^2*c10*l1^2*l2 + 2*M141000*b*c10*c21*l1^2 + M141000*b*c10*c21*l1*l2 + 2*M141000*b*c10*d21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 2*M222000*b*c10^2*l1*l2
```

## feature3

### `a30_next`

```text
a30_next = 3*M002000*l1*q02 + 3*M002000*l2*w + M002000*l32*q02 + 3*M010100*l1*q02 + 3*M010100*l1*w + M010100*l32*q02 + M010100*l32*w + M020000*l30 + 9*M022000*b*l1^2*l2 + 3*M022000*b*l1*l2*l32 + 3*M030100*b*l1^3 + 3*M030100*b*l1^2*l32 + M040000*d21*l1*l32 + 3*M121000*c10*l1*l2 + 2*M121000*c10*l1*l32 + M121000*c10*l2*l32
```

### `a32_next`

```text
a32_next = M020000*l32
```

### `q13_next`

```text
q13_next = 3*M002000*q02*w + 3*M010100*q02*w + 3*M010100*w^2 + M020000*q13 + 9*M022000*b*l1^2*q02 + 9*M022000*b*l1*l2*w + 3*M022000*b*l1*l32*q02 + M022000*b*l2*l32*w + 3*M030100*b*l1^2*q02 + 6*M030100*b*l1^2*w + M030100*b*l1*l32*q02 + 3*M030100*b*l1*l32*w + M040000*b*l1*l30 + M040000*d21*l32*w + M040000*l1*l32*r02 + 9*M042000*b^2*l1^3*l2 + 3*M042000*b^2*l1^2*l2*l32 + 3*M050100*b^2*l1^4 + 3*M050100*b^2*l1^3*l32 + M060000*b*d21*l1^2*l32 + 3*M121000*c10*l2*w + 2*M121000*c10*l32*w + 3*M141000*b*c10*l1^2*l2 + 2*M141000*b*c10*l1^2*l32 + M141000*b*c10*l1*l2*l32
```

## gradient3

### `d30_next`

```text
d30_next = 3*M000200*b*l1*q02 + 3*M000200*b*l2*w + 2*M000200*b*l32*q02 + M000200*b*l32*w + 6*M001010*b*l1*q02 + 3*M001010*b*l1*w + 3*M001010*b*l2*w + 2*M001010*b*l32*q02 + M001010*b*l32*w + M002000*b*l30 + 4*M002000*b*q02 + 3*M002000*b*w + 3*M002000*c10*q02 + 3*M002000*d21*w + 2*M002000*d32*q02 + M002000*d32*w + 3*M002000*e11*l2 + 3*M002000*l1*r02 + M002000*l32*r02 + 3*M004000*b^2*l1*l2*l32 + 3*M010001*b*l1*q02 + 3*M010001*b*l1*w + M010100*b*l30 + 4*M010100*b*q02 + 4*M010100*b*w + 6*M010100*c10*q02 + 3*M010100*c10*w + 3*M010100*d21*w + 2*M010100*d32*q02 + M010100*d32*w + 3*M010100*e11*l2 + 3*M010100*l1*r02 + M010100*l32*r02 + 18*M012100*b^2*l1^2*l2 + 6*M012100*b^2*l1^2*l32 + 9*M012100*b^2*l1*l2*l32 + M020000*d30 + 3*M020000*e11 + 4*M020000*r02 + 9*M020200*b^2*l1^2*l2 + 3*M020200*b^2*l1^2*l32 + 9*M021010*b^2*l1^3 + 9*M021010*b^2*l1^2*l2 + 3*M021010*b^2*l1^2*l32 + 9*M022000*b^2*l1^2 + 12*M022000*b^2*l1*l2 + 3*M022000*b*c10*l1*l2 + 2*M022000*b*c10*l1*l32 + M022000*b*c10*l2*l32 + 9*M022000*b*d21*l1^2 + 3*M022000*b*d21*l1*l32 + 3*M022000*b*d32*l1^2 + 3*M022000*b*d32*l1*l2 + 3*M030001*b^2*l1^3 + 12*M030100*b^2*l1^2 + 3*M030100*b*c10*l1^2 + 3*M030100*b*c10*l1*l2 + 3*M030100*b*d21*l1^2 + M030100*b*d21*l1*l32 + M030100*b*d32*l1^2 + M030100*b*d32*l1*l2 + 4*M040000*b*d21*l1 + M040000*c10*d32*l2 + 3*M100010*c10*q02 + 3*M100010*c10*w + M101000*d30 + 3*M103000*b*c10*l1*l2 + 2*M103000*b*c10*l1*l32 + M103000*b*c10*l2*l32 + 6*M111100*b*c10*l1^2 + 12*M111100*b*c10*l1*l2 + 4*M111100*b*c10*l1*l32 + 2*M111100*b*c10*l2*l32 + 3*M120010*b*c10*l1^2 + 3*M120010*b*c10*l1*l2 + 14*M121000*b*c10*l1 + 4*M121000*b*c10*l2 + 6*M121000*c10^2*l2 + 3*M121000*c10*d32*l2 + 3*M202000*c10^2*l2 + 3*M210100*c10^2*l2 + 3*M220000*c10^2
```

### `d32_next`

```text
d32_next = M002000*b*l32 + 3*M010100*b*l1 + M020000*b + M020000*d32 + 3*M101000*c10
```

### `r13_next`

```text
r13_next = 3*M000200*b*q02*w + 3*M001010*b*q02*w + 3*M001010*b*w^2 + M002000*b*q13 + 3*M002000*e11*q02 + 3*M002000*r02*w + 3*M004000*b^2*l1*l32*q02 + 3*M004000*b^2*l2*l32*w + 3*M010100*e11*q02 + 3*M010100*e11*w + 18*M012100*b^2*l1^2*q02 + 27*M012100*b^2*l1*l2*w + 9*M012100*b^2*l1*l32*q02 + 9*M012100*b^2*l1*l32*w + M020000*r13 + 9*M020200*b^2*l1^2*q02 + 9*M021010*b^2*l1^2*q02 + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l30 + 3*M022000*b*c10*l1*q02 + M022000*b*c10*l32*q02 + 9*M022000*b*d21*l1*w + M022000*b*d21*l32*w + 3*M022000*b*d32*l1*q02 + 3*M022000*b*d32*l1*w + M022000*b*d32*l2*w + 6*M022000*b*e11*l1*l2 + 2*M022000*b*e11*l1*l32 + M022000*b*e11*l2*l32 + 9*M022000*b*l1^2*r02 + 3*M022000*b*l1*l32*r02 + 15*M024000*b^3*l1^2*l2*l32 + 3*M030100*b*c10*l1*q02 + M030100*b*d32*l1*q02 + 3*M030100*b*e11*l1^2 + 3*M030100*b*e11*l1*l2 + 45*M032100*b^3*l1^3*l2 + 15*M032100*b^3*l1^3*l32 + M040000*c10*d32*q02 + M040000*d32*e11*l2 + 15*M041010*b^3*l1^4 + 9*M042000*b^2*d21*l1^3 + 3*M042000*b^2*d21*l1^2*l32 + 3*M042000*b^2*d32*l1^3 + 3*M042000*b^2*d32*l1^2*l2 + 3*M103000*b*c10*l1*q02 + 3*M103000*b*c10*l2*w + M103000*b*c10*l32*q02 + 2*M103000*b*c10*l32*w + 12*M111100*b*c10*l1*q02 + 9*M111100*b*c10*l1*w + 6*M111100*b*c10*l2*w + 2*M111100*b*c10*l32*q02 + M111100*b*c10*l32*w + 3*M120010*b*c10*l1*q02 + 3*M120010*b*c10*l1*w + M121000*b*c10*l30 + M121000*b*d30*l1 + 6*M121000*c10^2*q02 + 3*M121000*c10*d21*w + 3*M121000*c10*d32*q02 + M121000*c10*d32*w + 9*M121000*c10*e11*l2 + 3*M121000*c10*l1*r02 + M121000*c10*l32*r02 + 9*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1^2*l32 + 6*M123000*b^2*c10*l1*l2*l32 + 9*M131100*b^2*c10*l1^3 + 18*M131100*b^2*c10*l1^2*l2 + 3*M131100*b^2*c10*l1^2*l32 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*d21*l1^2 + M141000*b*c10*d21*l1*l32 + M141000*b*c10*d32*l1^2 + 2*M141000*b*c10*d32*l1*l2 + 3*M202000*c10^2*q02 + 3*M210100*c10^2*q02 + 3*M210100*c10^2*w + M220000*c10*d30 + 6*M222000*b*c10^2*l1*l2 + 2*M222000*b*c10^2*l1*l32 + M222000*b*c10^2*l2*l32 + 3*M230100*b*c10^2*l1^2 + 3*M230100*b*c10^2*l1*l2 + M240000*c10^2*d32*l2 + 3*M321000*c10^3*l2
```

### `source13m`

```text
source13m = 3*M000200*b*q02*w + 3*M001010*b*q02*w + 3*M001010*b*w^2 + M002000*b*q13 + 3*M002000*e11*q02 + 3*M002000*r02*w + 3*M004000*b^2*l1*l32*q02 + 3*M004000*b^2*l2*l32*w + 3*M010100*e11*q02 + 3*M010100*e11*w + 18*M012100*b^2*l1^2*q02 + 27*M012100*b^2*l1*l2*w + 9*M012100*b^2*l1*l32*q02 + 9*M012100*b^2*l1*l32*w + M020000*r13 + 9*M020200*b^2*l1^2*q02 + 9*M021010*b^2*l1^2*q02 + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l30 + 3*M022000*b*c10*l1*q02 + M022000*b*c10*l32*q02 + 9*M022000*b*d21*l1*w + M022000*b*d21*l32*w + 3*M022000*b*d32*l1*q02 + 3*M022000*b*d32*l1*w + M022000*b*d32*l2*w + 6*M022000*b*e11*l1*l2 + 2*M022000*b*e11*l1*l32 + M022000*b*e11*l2*l32 + 9*M022000*b*l1^2*r02 + 3*M022000*b*l1*l32*r02 + 15*M024000*b^3*l1^2*l2*l32 + 3*M030100*b*c10*l1*q02 + M030100*b*d32*l1*q02 + 3*M030100*b*e11*l1^2 + 3*M030100*b*e11*l1*l2 + 45*M032100*b^3*l1^3*l2 + 15*M032100*b^3*l1^3*l32 + M040000*c10*d32*q02 + M040000*d32*e11*l2 + 15*M041010*b^3*l1^4 + 9*M042000*b^2*d21*l1^3 + 3*M042000*b^2*d21*l1^2*l32 + 3*M042000*b^2*d32*l1^3 + 3*M042000*b^2*d32*l1^2*l2 + 3*M103000*b*c10*l1*q02 + 3*M103000*b*c10*l2*w + M103000*b*c10*l32*q02 + 2*M103000*b*c10*l32*w + 12*M111100*b*c10*l1*q02 + 9*M111100*b*c10*l1*w + 6*M111100*b*c10*l2*w + 2*M111100*b*c10*l32*q02 + M111100*b*c10*l32*w + 3*M120010*b*c10*l1*q02 + 3*M120010*b*c10*l1*w + M121000*b*c10*l30 + M121000*b*d30*l1 + 6*M121000*c10^2*q02 + 3*M121000*c10*d21*w + 3*M121000*c10*d32*q02 + M121000*c10*d32*w + 9*M121000*c10*e11*l2 + 3*M121000*c10*l1*r02 + M121000*c10*l32*r02 + 9*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1^2*l32 + 6*M123000*b^2*c10*l1*l2*l32 + 9*M131100*b^2*c10*l1^3 + 18*M131100*b^2*c10*l1^2*l2 + 3*M131100*b^2*c10*l1^2*l32 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*d21*l1^2 + M141000*b*c10*d21*l1*l32 + M141000*b*c10*d32*l1^2 + 2*M141000*b*c10*d32*l1*l2 + 3*M202000*c10^2*q02 + 3*M210100*c10^2*q02 + 3*M210100*c10^2*w + M220000*c10*d30 + 6*M222000*b*c10^2*l1*l2 + 2*M222000*b*c10^2*l1*l32 + M222000*b*c10^2*l2*l32 + 3*M230100*b*c10^2*l1^2 + 3*M230100*b*c10^2*l1*l2 + M240000*c10^2*d32*l2 + 3*M321000*c10^3*l2
```
