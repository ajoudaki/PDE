# Frozen expected-sign attempt at the fitted reference

Date: 2026-09-12. Author: scoped `gaussian_sign_route` agent.

**Conclusion.** Neither `beta_+(s_dagger)>0` nor `beta_-(s_dagger)<0` is
proved. The actual exchange symmetry does diagonalize the Gaussian source
covariances into independent sum and contrast histories. It does **not**
diagonalize the nonlinear responses in time. The precise endpoint quantity
is a contraction of the complete source covariance row with all historical
response derivatives, given below. A proposed argument based on positive
source covariance and inhibitory causal memory is invalid: even a bounded
tanh memory equation with these stronger positivity properties can reverse
its expected initial-source sign at a finite time.

The counterexample below tests that proposed inference only. It is not a
replacement model, an actual neural-reference counterexample, or a change to
E₀. The actual endpoint signs and E₀ remain open. No new early-time jet,
experiment, family redesign, or Git write was used.

## 1. Actual exchange-sector Gaussian reduction

Use the positive-label coordinate representation of the same actual
reference from `GAUSSIAN_SIGN_TRANSPORT.md`: `v1=w1`, `v2=-w2`,
`H_a^1=tanh(v_a)`, `z_a=A H_a^1`, `delta_a=c sech²(z_a)`. The actual
action and its adjoint are retained. Let

\[
v_0=E\tanh^2G\in(0.39,0.4),\qquad
X=z_1(0),\quad Y=z_2(0),
\]

where `X,Y` are independent `N(0,v0)`. As before,

\[
\beta_\pm(s)=\frac1{2v_0}
 E[(X\pm Y)(\delta_1(s)\pm\delta_2(s))].
\tag{E1}
\]

First work on an arbitrary fixed reference Euler mesh from C.4.5.2, with
the whole prior source history retained. Both reference controls are now
`h_r/2`; the label change is only the odd-network identity. The complete
forward source equation is

\[
z_{ka}=\xi_{ka}+\sum_{r<k,b}a_{ka,rb}\delta_{rb},
\quad
a_{ka,rb}=E_1[\partial_{\zeta_{rb}}H^1_{ka}]
              +\frac{h_r}{2}E_1[H^1_{ka}H^1_{rb}].
\tag{E2}
\]

These are the actual coefficients, including response to reused transpose
calls. They are not replaced by their learned-rank part. The reverse source
rule and first-row clocks determining them remain the full rules in
C.4.5.2.R5–R7.

For any two-component field write `V_±=(V1±V2)/sqrt(2)`. The exchange
symmetry gives, simultaneously at every pair of mesh times,

\[
E[H^1_{k+}H^1_{r-}]=0,\qquad
C_\pm(k,r):=E[\xi_{k\pm}\xi_{r\pm}]
            =E[H^1_{k\pm}H^1_{r\pm}].
\tag{E3}
\]

To verify the zero, expand its four contractions. Exchange identifies the
two diagonal contractions and the two cross contractions, which cancel.
The source rule identifies these contractions with Gaussian covariance.
Thus the entire finite `+` and `-` forward Gaussian source histories are
independent; zero cross-covariance implies independence for their joint
Gaussian law, also at singular covariance. Each `C_pm` is a positive
semidefinite time Gram matrix. Positivity of its individual off-diagonal
entries has not been established by this argument.

The same exchange symmetry makes each two-by-two block in (E2) have equal
diagonal entries and equal off-diagonal entries. With
`a_pm(k,r)=a_(k1,r1)±a_(k1,r2)`, equation (E2) becomes

\[
z_{k\pm}=\xi_{k\pm}+\sum_{r<k}a_\pm(k,r)\delta_{r\pm}.
\tag{E4}
\]

This is a decomposition in the two anchor indices, not independence of the
trained fields. The two responses still couple through

\[
c_k=\sum_{r<k}\frac{h_r}{2}(\tanh z_{r1}+\tanh z_{r2}),
\quad
\delta_{k\pm}=\frac{c_k}{\sqrt2}
 [\operatorname{sech}^2z_{k1}\pm\operatorname{sech}^2z_{k2}].
\tag{E5}
\]

In particular, neither the random readout nor the other exchange sector
can be discarded when assessing the response sign.

## 2. The exact expected-sign formula and endpoint passage

Set `xi_(0±)=(X±Y)/sqrt(2)`, so `C_pm(0,0)=v0`. Gaussian integration by
parts in the complete forward source list gives exactly

\[
\beta_\pm^{\mathrm{mesh}}(s_k)
 =\frac1{v_0}\sum_{r\le k}C_\pm(0,r)
                 E[\partial_{\xi_{r\pm}}\delta_{k\pm}].
\tag{E6}
\]

All covariance entries, chosen coefficients, and earlier contractions are
held fixed under these named derivatives. This is the derivative convention
in III.F and C.4.5.2. Its hypotheses hold for every fixed reference graph by
the root-clipping/readout-bounding argument in C.4.5.2 §2. The derivatives
are integrable; the contained Gaussian integration-by-parts proof applies
after conditioning on the independent opposite-sector source group. No
inverse of a singular covariance is required. The left side is the actual
mixed moment, so the right side is invariant under any ambiguity of named
derivatives on a singular support.

Equivalently, jointly decompose the whole same-sector source vector as

\[
\xi_{r\pm}=\frac{C_\pm(0,r)}{v_0}\xi_{0\pm}+\eta_{r\pm},
\tag{E7}
\]

where the Gaussian remainder vector `eta_pm` is independent of `xi_(0±)`.
Formula (E6) is the expectation of the derivative of the complete output
under a change of `xi_(0±)`, with that remainder vector and the opposite
sector fixed. Such a change shifts **every** correlated historical source
by the corresponding covariance coefficient. Keeping all later source
slots numerically fixed would give the wrong derivative.

On a sequence of reference meshes ending at the actual `s_dagger`, the
strong convergence established in C.4.5.2 gives convergence of the mixed
moments, because `xi_(0±)` is the same fixed `L2` variable. Therefore

\[
\beta_\pm(s_\dagger)=
\lim_{\mathrm{mesh}\to0}\frac1{v_0}
 \sum_{r\le k}C_\pm(0,r)
                  E[\partial_{\xi_{r\pm}}\delta_{k\pm}].
\tag{E8}
\]

This statement passes only the complete invariant contraction. It does not
assert convergence of every named derivative, a continuous response kernel,
or an interchange of the derivative with an increasing transcript. Those
stronger assertions are unnecessary for (E8) and have not been proved here.

The exact unresolved condition for this route is a mesh-uniform signed
comparison for the contraction in (E8) at the fitted endpoint. The
established coefficient bounds control absolute values, while the Gaussian
covariance matrices control squares. Neither provides that signed
comparison.

There are two tempting conditional arguments that do not repair the gap:

- Conditioning on an independent source sector in (E6) is legitimate.
  Conditioning on the trained response remainder in (E2) does not leave
  the original Gaussian source law unchanged: that remainder depends on
  the same earlier sources. The covariance proof supplies no such
  conditional Gaussianity.
- Exchange and the activation's global oddness give parity under sign changes of an entire
  sector history. It does not make the conditional output odd, or
  monotone, as a function of `xi_(0±)` when the same-sector remainder in
  (E7) is held fixed. The parity operation also changes that remainder.

## 3. Positive source covariance and inhibitory memory do not suffice

The following complete finite-time counterexample targets a possible
inference from (E4), even granting positivity properties not established for
the actual coefficients. It leaves the actual reference unchanged.

Let `Z~N(0,v0)`, use the constant Gaussian source history `xi(t)=Z`, and
define the scalar causal equation on `[0,2]`

\[
d(t)=Z+\int_0^t K(t,r)\delta(r)\,dr,\qquad
\delta(t)=-\tanh d(t),\qquad
K(t,r)=10\,\mathbf1_{\{r\le t-1\}}.
\tag{E9}
\]

The source covariance is the positive constant `v0`, so its time covariance
is positive semidefinite and entrywise positive. The causal memory kernel
is nonnegative. The instantaneous response is bounded, odd, and strictly
decreasing, and it has the inhibitory pointwise sign
`d(t) delta(t)<=0`. All these properties are stronger than merely knowing
exchange parity and a positive semidefinite source covariance.

Nevertheless the expected initial-source response changes sign. The
method of steps gives the unique solution explicitly on this interval:

\[
d(t)=Z\quad(0\le t\le1),\qquad
d(t)=Z-10(t-1)\tanh Z\quad(1\le t\le2).
\tag{E10}
\]

Thus initially `E[Z delta(t)]=-E[Z tanh Z]<0`. At the finite time two,

\[
E[Z\delta(2)]=E[-Z\tanh(Z-10\tanh Z)]>0.
\tag{E11}
\]

Here is an explicit sign certificate. For `0<x<=3`, the function
`tanh x/x` decreases, since
`(tanh x-x sech²x)'=2x tanh x sech²x>0` and that difference vanishes at
zero. Also `tanh 3>3/4`. Hence
`x-10 tanh x<-3x/2` throughout this interval. By oddness the integrand in
(E11) is nonnegative on `|Z|<=3`, and on `1/2<=|Z|<=1` it exceeds `1/4`,
because `tanh(3/4)>1/2`.

Using `0.39<v0<0.4`, the Gaussian density on `[1/2,1]` is bounded below
by `1/8`: its normalizing prefactor exceeds `1/2` and its exponential
factor exceeds `1/4`. The latter follows from
`1/(2v0)<1.3` and `e^1.3<4`. Therefore
`Pr{1/2<=|Z|<=1}>1/8`. The only possibly negative contribution is the tail,
where its magnitude is at most

\[
E[|Z|\mathbf1_{|Z|>3}]
 =\sqrt{2v_0/\pi}\,e^{-9/(2v_0)}
 <e^{-11.25}<1/64.
\]

Consequently (E11) exceeds `1/32-1/64=1/64`. The elementary exponential
bounds can be checked by positive series: the degree-five lower sum for
`e^11.25` exceeds 64, while the degree-three sum for `e^1.3` plus its
geometrically bounded remaining tail is less than 4. No numerical
integration or experiment is used.

The discontinuity of `K` is inessential. Replace its step by a smooth
nondecreasing transition over a strip of width `epsilon`, preserving
`K_epsilon>=0`. Its time-row `L1` difference is at most `10 epsilon`.
Subtract the integral equations and use the one-Lipschitz tanh to obtain,
on `[0,2]`,

\[
\sup_{t\le2}|d_\epsilon(t)-d(t)|
 \le10\epsilon e^{20}.
\]

This follows by iteration of the integral inequality, whose `j`th term is
bounded by `(10t)^j/j!`. The expected response changes by at most this
bound times `E|Z|`. Choosing a sufficiently small positive `epsilon`
preserves the strict sign reversal, now with a smooth nonnegative memory
kernel.

Thus a comparison theorem asserting that nonnegative causal memory,
positive Gaussian source covariance, and an inhibitory odd gate preserve a
negative initial-source covariance is false. Delay in the response can
overcorrect that covariance. The actual neural coefficients may possess
an additional property preventing this behavior; that property has not
been established by the available Gram or source bounds. The example
makes no assertion that these artificial coefficients are reached by the
actual neural reference.

## 4. Remaining endpoint obligation and scope

For the actual contrast sector, a valid expected-sign proof must control the
complete historical response in (E8), including its coupled readout and
first-row dependence. Positive covariance, exchange parity, the sign of an
instantaneous gate, and coefficient magnitude bounds are insufficient.
For the actual sum sector there is likewise no proved order-preserving
response to the correlated initial-source shift (E7). Neither missing
property follows from the other sector's sign or from reference fitting.

The earlier actual early-reference covariance signs and actual failure of
the pointwise contrast-order cone are unchanged. This attempt adds the
exact exchange-sector endpoint reduction and a precise failure of a weaker
proposed memory-based sign inference. It does not disprove either actual
endpoint sign. Even an eventual proof of one such sign would still need
its connection to the E₀ projected population-risk comparison.

All four target coefficients, the odd target perturbation, full-circle
density perturbation, raw metric, actual initialization, and required
width/contamination/sample order remain those of the frozen contract.
No empirical, finite-network, added-time advantage, or relative-component
benefit is asserted here.

## 5. Source and check record

Inputs were only the two own frozen reports and the previously authorized
established sources, plus required shared process instructions and skills.
No other route or review was read. The report was analytically self-checked
for sector normalization, singular-source integration by parts, complete
contraction passage, the memory solution, its tail certificate, and
smoothing stability. It has not received an independent audit or promotion.

At the pre-write metadata check HEAD was
`fbe203c51ebd62805b0fdd9ec3824d6d8aac7859`, with empty staged index. Shared
instructions and established source hashes were unchanged from the source
reports. The frozen own-input hashes were:

```text
ROUTE_GAUSSIAN_SIGN.md
2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c
GAUSSIAN_SIGN_TRANSPORT.md
5f44ec005410cbdfa4557580c243ea77c1abce6a067882a722d2552578cb484c
```
