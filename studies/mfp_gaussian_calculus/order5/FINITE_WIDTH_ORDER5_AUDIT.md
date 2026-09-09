# Exact finite-width audit through `D_n^5 f_n`

**Status:** finite-width gate passed; no large-width generic-activation claim  
**Scope:** the exact `H=2`, `B=1` model in
[`PROOF_CONTRACT.md`](PROOF_CONTRACT.md)  
**Code:** [`finite_width/`](finite_width/)

This note records only identities which hold before taking \(n\to\infty\).
It does not perform the equality-partition, transpose-response,
or Wick--Stein peel needed to turn the generic fifth derivative into a
Gaussian normal form.

## 1. Active raw first-layer coordinate

Put

\[
q_0=\frac{\lVert x\rVert^2}{d_0}.
\]

For each first-layer neuron only the coordinate of `w_j` parallel to
`x` affects the network.  If `r_j` is this standard-normal
Euclidean coordinate, then

\[
u_j=\sqrt{q_0}\,r_j,\qquad r_j\sim N(0,1).
\]

All orthogonal coordinates have identically zero derivatives.  Consequently,
differentiating in the raw coordinates

\[
\theta=(r,W,a)
\]

is exactly equivalent to differentiating the original network.  In
particular, the factor `q_0` in the feature equation for `u`
is induced by the raw Euclidean metric; it is not an extra tunable
multiplier.

## 2. Independent derivation of the six families

First work in the whitened coordinate
`vartheta=theta/sqrt(n)`.  Write

\[
p=\nabla_\vartheta f,\quad
H=\nabla_\vartheta^2f,\quad
T=\nabla_\vartheta^3f,\quad
U=\nabla_\vartheta^4f,\quad
V=\nabla_\vartheta^5f,
\]

so that `D=p dot grad_vartheta`.  Define

\[
a=Hp,\qquad b=T[p,p],\qquad c=Ha=H^2p.
\]

Every tensor is symmetric.  Direct differentiation, without using the
candidate in the proof contract, gives

\[
\begin{aligned}
Df&=p\cdot p,\\
D^2f&=2H[p,p],\\
D^3f&=2T[p,p,p]+4a\cdot a,\\
D^4f&=2U[p,p,p,p]+14T[a,p,p]+8a\cdot Ha.
\end{aligned}
\tag{2.1}
\]

For the last line, the three summands differentiate as follows:

\[
\begin{aligned}
D\{2U[p^4]\}
   &=2V[p^5]+8U[a,p^3],\\
D\{14T[a,p,p]\}
   &=14U[a,p^3]+14T[b,p,p]+14T[c,p,p]
     +28T[a,a,p],\\
D\{8a\cdot Ha\}
   &=16T[c,p,p]+8T[a,a,p]+16c\cdot c.
\end{aligned}
\tag{2.2}
\]

Here `Da=b+c` and

\[
D(a\cdot Ha)
=2T[c,p,p]+T[a,a,p]+2\lVert c\rVert^2.
\]

Collecting (2.2) produces exactly six contraction families:

\[
\boxed{
D_n^5f_n=
2V[p,p,p,p,p]
+22U[Hp,p,p,p]
+14T[T[p,p],p,p]
+30T[H^2p,p,p]
+36T[Hp,Hp,p]
+16\lVert H^2p\rVert^2.}
\tag{2.3}
\]

Thus the proposed coefficients

\[
(2,22,14,30,36,16)
\]

are independently reproduced.

## 3. Raw-coordinate scaling audit

Now let every derivative tensor be with respect to the original raw
`theta` coordinate, set

\[
p_\theta=\nabla_\theta f_n,\qquad v=np_\theta,
\]

and continue to denote the raw Hessian and higher tensors by
`H,T,U,V`.  Since

\[
\nabla_\vartheta^r f_n=n^{r/2}\nabla_\theta^r f_n,
\qquad
p_\vartheta=\frac{v}{\sqrt n},
\]

(2.3) is equivalent, term by term, to

\[
\boxed{
\begin{aligned}
D_n^5f_n={}&
2V[v,v,v,v,v]
+22n\,U[Hv,v,v,v]\\
&+14n\,T[T[v,v],v,v]
+30n^2T[H^2v,v,v]\\
&+36n^2T[Hv,Hv,v]
+16n^3\lVert H^2v\rVert^2.
\end{aligned}}
\tag{3.1}
\]

Equivalently, in terms of `p_theta`, every unweighted family in
(2.3) acquires the common factor `n^5`.  For example,

\[
nU[Hv,v,v,v]=n^5U[Hp_\theta,p_\theta,p_\theta,p_\theta],
\]

and

\[
n^3\lVert H^2v\rVert^2
=n^5\lVert H^2p_\theta\rVert^2.
\]

This checks both raw forms and removes a possible ambiguity between the
flow velocity `v=n grad_theta f` and the whitened gradient
`p_vartheta`.

## 4. Two independent finite-width implementations

### Route A: moving feature-flow series

[`feature_flow.py`](finite_width/feature_flow.py) expands the exact
flow

\[
\begin{aligned}
\dot a_i&=\phi(z_i),\\
\dot W_{ij}&=\frac1{\sqrt n}a_i\phi'(z_i)\phi(u_j),\\
\dot u_j&=\frac{q_0}{\sqrt n}\phi'(u_j)
 \sum_iW_{ij}a_i\phi'(z_i)
\end{aligned}
\tag{4.1}
\]

in ordinary Taylor coefficients through order five.  Function composition
is implemented by the literal finite Taylor formula using
`phi^(0),...,phi^(5)`; there is no polynomial approximation of the
activation.

### Route B: raw multivariate automatic differentiation

[`raw_ad.py`](finite_width/raw_ad.py) never evolves (4.1).  It:

1. creates one multivariate Taylor variable for every active raw coordinate
   `(r,W,a)`;
2. evaluates the original network as a degree-five multivariate Taylor
   polynomial;
3. applies `n grad(f).grad` algebraically five times, decreasing
   the retained degree after each application; and
4. separately materializes `p,H,T,U,V` and evaluates all six
   contractions in (3.1).

The raw-AD recurrence and the tensor contraction are separate evaluations of
the same raw derivative data; Route A does not share either representation.
The raw route is intentionally capped at width two because its tensors have
audit, not production, purpose.

### Seedwise results

The frozen panel contains:

- widths `1,2`;
- arbitrary forward variance `q_0=0.73`;
- linear, generic cubic, `tanh`, and normalized-sine activations;
- distinct fixed seeds for every activation.

Across that panel, the largest scaled discrepancy between Routes A and B for
the full vector `(f,Df,...,D^5f)` was

\[
5.53\,10^{-14}.
\]

The largest scaled discrepancy between Route A's fifth derivative and the
sum of the six independently materialized tensor families was

\[
2.59\,10^{-14}.
\]

The preregistered normalized-sine seed panel uses three additional seeds at
each width.  Its worst scaled discrepancy was

\[
2.92\,10^{-14}.
\]

These are floating-point roundoff comparisons of exact finite algebraic
identities, not Monte Carlo tests of a width limit.

## 5. Exact parity

Let `R` reflect only the readout:

\[
R(r,W,a)=(r,W,-a).
\]

Then `f(R theta)=-f(theta)`.  If
`g(R theta)=epsilon g(theta)`, orthogonality of `R` gives

\[
(D_ng)(R\theta)=-\epsilon(D_ng)(\theta).
\]

Thus `D_n^k f_n` has readout parity
`(-1)^(k+1)`.  Symmetry of the Gaussian readout proves at every
finite width, whenever the expectation exists,

\[
\boxed{
\mathbb E f_n
=\mathbb E D_n^2f_n
=\mathbb E D_n^4f_n=0.}
\tag{5.1}
\]

No large-width argument is involved.

## 6. Exact controls

### Constant

For `phi(x)=c`,

\[
f_n=\frac c n\sum_i a_i,\qquad
D_nf_n=c^2,\qquad
D_n^k f_n=0\quad(k\ge2)
\tag{6.1}
\]

at every width.

### Linear

For `phi(x)=x` and `q_0=1`, direct Gaussian equality
partitioning gives the exact all-width result

\[
\boxed{
\begin{aligned}
\mathbb E D_nf_n&=3,\\
\mathbb E D_n^3f_n&=48+\frac{60}{n},\\
\mathbb E D_n^5f_n&=1464+\frac{4800}{n}
                         +\frac{4320}{n^2}.
\end{aligned}}
\tag{6.2}
\]

Therefore the required limit is `(3,48,1464)`.
[`exact_controls.py`](finite_width/exact_controls.py) contains an
independent integer sparse-polynomial/Wick enumerator.  It represents

\[
P=\sum_{i,j}a_iW_{ij}u_j,\qquad f_n=n^{-3/2}P
\]

and applies `grad(P).grad` symbolically.  Exact rational results at
widths one, two, and three reproduce (6.2), including every finite-width
correction.  In the corresponding connected equality diagrams, each new
copy of \(P\) is attached by the differentiated coordinate, so the
unnormalized third- and fifth-order Wick counts have degree at most three
and four in \(n\), respectively.  The complete counts are

\[
48n^3+60n^2,
\qquad
1464n^4+4800n^3+4320n^2,
\]

which, after the exact normalizations \(n^{-3}\) and \(n^{-4}\), give
(6.2).

### Affine

The non-centered affine activation `phi(x)=1+2x` is an exact
control, not an approximation.  At width one, rational polynomial
differentiation followed by exact Gaussian Wick evaluation gives

\[
\bigl(\mathbb E f,\mathbb E Df,\ldots,\mathbb E D^5f\bigr)
=(0,57,0,34832,0,58495488).
\tag{6.3}
\]

Both general finite-width routes reproduce every seed before annealing.
The affine test exercises constant offsets, nonzero derivatives, and all
moving-weight channels simultaneously.

### Quadratic

For `phi(x)=x^2`, the generic Route A agrees seedwise through order
five with the pre-existing quadratic finite-width compiler at widths
`1,2,5` and two seeds per width.  The independent exact width-one
Wick values are

\[
(0,1455,0,25604087040,0,13167513029295424800).
\tag{6.4}
\]

The accepted, separately derived large-width quadratic targets are

\[
\boxed{(A,B,C)=(111,1685184,77400633120).}
\tag{6.5}
\]

The finite-width work here verifies that the generic fifth-order jet uses
exactly the same finite network and normalization as that compiler.  It does
**not** by itself re-prove the leading equality-sector enumeration behind
(6.5); the generic Gaussian-normal-form derivation must reproduce (6.5)
before promotion.

## 7. Preregistered smooth nonpolynomial regression

The exact activation oracle is

\[
\phi(x)=\frac{\sin x}{\sqrt{(1-e^{-2})/2}}.
\tag{7.1}
\]

No Hermite truncation is used.  The harness in
[`regression.py`](finite_width/regression.py):

1. refuses to sample a large-width panel until the extra seedwise exact
   Route-A/Route-B gate passes;
2. requires the flattened theoretical prediction for `C` as an
   explicit command-line argument;
3. performs the frozen weighted affine fit in `1/n`;
4. enforces width at most 512 and at most 10,000 networks; and
5. reports `pass`, `inconclusive`, or
   `fail_pending_replication` under the preregistered 3/5-standard-
   error rule.

The large-width panel has **not** been run or inspected in this audit.  It is
held until an independently flattened generic prediction is frozen.

## 8. Assumptions and exact claim boundary

For a deterministic finite network, the identities above require
`phi in C^5` in neighborhoods of the finitely many preactivations.
For the displayed finite-width annealed expectations it is enough additionally
that every term in (3.1) be integrable.  A simple sufficient condition is that
`phi^(r)` has polynomial growth for `0 <= r <= 5`.

This establishes:

- the exact finite-width identity (2.3)/(3.1);
- the raw/whitened scaling;
- seedwise agreement of two independent fifth-order programs;
- exact parity and the stated finite-width controls.

It does not establish:

- the generic equality-partition and width-counting limit;
- transpose-response or Wick--Stein reduction;
- a flattened formula for generic `C`;
- uniform integrability or convergence of the annealed width limit.

Those remain separate gates under the proof contract.

## 9. Reproduction

No third-party test runner is required:

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.order5.finite_width.run_checks
```

The frozen result is:

```text
PASS test_two_independent_routes_seedwise
PASS test_constant_and_affine_exact_width_one_controls
PASS test_linear_exact_controls
PASS test_quadratic_width_one_exact_wick_control
PASS test_generic_quadratic_matches_accepted_finite_width_compiler
PASS test_quadratic_exact_frozen_large_width_endpoint
PASS test_preregistered_sine_exact_pre_gate_only
```
