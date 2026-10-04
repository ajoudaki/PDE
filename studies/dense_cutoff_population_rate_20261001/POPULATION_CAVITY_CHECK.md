# Internal check of the deterministic-control fluctuation proposition

Date: 2026-10-01. **Verdict: PASS for the stated finite fluctuation
proposition and its disclosed limitations.** This is an internal
adversarial reconstruction, not a promotion review. It does not certify
an actual adaptive-control, physical-time, or population-centered rate.

## 1. Input scope and full-read coverage

The complete new candidate and its explicitly authorized same-study
dependency were read. Previously allowed manuscript sources and notation
instructions supply the network conventions. No other study or other
reviewer's report was read.

| Frozen input | Complete read coverage | SHA-256 |
|---|---:|---|
| POPULATION_CAVITY_ATTEMPT.md | lines 1–318 | c95075a84a47529d78873f9a6c342b950e640d51145a28577179de286d1f9e3b |
| FINITE_TAIL_ROUTE.md | lines 1–393 | da251f231832e69c74581ba4291e649d1322737eebd46b2a4d9c6ca1a8dd0d65 |

The dependence on the tail note was checked at proof level: the new
argument needs conditional bounds uniform over every deterministic
initial first-layer feature array, a stronger formulation than merely
averaging over its original Gaussian initialization.

The complete candidate was initially read at hash
bc5866384556dee52805ab40f6853921e9ef2a975bea8fae01659ed6fdcc7f3d.
The subsequently revised one-sample interpretation paragraph was reread
in full and checked; it changes no proof or proposition. The table records
the final version with that clarification.

The candidate concerns two hidden tanh layers, a fixed number of
orthonormal training inputs, zero initial readout and Gaussian initial
weights. Its driver \(b:[0,S]\to\mathbb R^m\), with
\(0<S\le1\), is deterministic and absolutely continuous, with
\(b(0)=0\) and \(\sum_a|b_a'|\le1\) a.e. It asserts

\[
 \mathbb E\sup_{0\le u\le S}
   |f_{n,a}^b(u)-\mathbb Ef_{n,a}^b(u)|^2\le CS^2/n
\]

for each training output. All Gaussian initialization randomness is
averaged. The assertion is uniform in the choice of a deterministic
driver through its constant; it does not move the driver supremum
inside the expectation.

## 2. Transformed equations and the exact prediction derivative

For
\[
 F(z)=z/2+\sinh(2z)/4,\qquad
 \psi(p)=\tanh(F^{-1}(p)),
\]
one has \(F'(z)=\cosh^2z\), and, with \(z=F^{-1}(p)\),

\[
 \psi'(p)=\operatorname{sech}^4z,\qquad
 \psi''(p)=-4\tanh z\,\operatorname{sech}^6z.
\]

Hence \(0<\psi'\le1\), \(|\psi''|\le4\), and
\[
 |(\log\psi')'(p)|
    =4|\tanh z|\operatorname{sech}^2z\le4.
\]
These are the derivative bounds used later.

For the actual canonical gradient flow, define
\(db_a=-2r_a\,dt/m\). Orthonormality makes the first-layer
preactivation equation
\(dz_a^{(1)}=\operatorname{sech}^2(z_a^{(1)})k_a\,db_a\).
Multiplication by \(F'\) gives \(dp_a=k_a\,db_a\).
The readout and hidden-matrix controlled equations retain, respectively,
no width normalization and the factor \(1/n\). Thus the candidate's
controlled system has the correct signs and mobilities.

Write \(h_a=\psi(p_a)\), \(h_a^{(2)}=\tanh(Wh_a)\),
\(\delta_a^{(2)}=w\odot\operatorname{sech}^2(Wh_a)\), and
\(k_a=W^\top\delta_a^{(2)}\). Under an infinitesimal \(db_b\),
the three parameter blocks contribute to \(df_a\) as follows:

\[
 \frac{h_a^{(2)\top}h_b^{(2)}}n,\qquad
 \frac{\delta_a^{(2)\top}\delta_b^{(2)}}n
     \frac{h_a^\top h_b}n,\qquad
 \mathbf1_{a=b}\frac1n\sum_i\psi'(p_{a,i})k_{a,i}^2.
\]

The last term follows from
\(\partial f_a/\partial p_a=\psi'(p_a)\odot k_a/n\).
Since \(\psi'(p_a)=\operatorname{sech}^4(z_a^{(1)})\),
this is exactly the first-layer gradient contribution, with the
square of the original tanh derivative. The resulting matrix
\(\Lambda\) is \(m\) times the manuscript's tangent Gram, and
\[
 \frac d{du}f_a^b(u)=\sum_b b_b'(u)\Lambda_{ab}(u)
\]
has no missing factor of two or \(m\): those factors are already
absorbed into the definition of the driver.

For each fixed finite initialization, these are ordinary controlled
ODEs with measurable bounded driver derivative and locally Lipschitz
state dependence. Bounded features give \(\|w(u)\|_\infty\le u\),
and the matrix increment is bounded in Frobenius norm by \(CS^2\).
Together with the finite initial operator norm, these bounds also
ensure existence on the entire controlled interval, even on the
exceptional initialization event later used in projection removal.

## 3. Projection, dependence and the conditional moment input

The Frobenius projection \(\Pi_K\) onto the operator-norm ball is
nonexpansive because that ball is closed and convex. The candidate
derives the relevant variational inequalities and hence
\(\|\Pi_K A-\Pi_K B\|_F\le\|A-B\|_F\).
Therefore \(G\mapsto\Pi_K(G/\sqrt n)\) is \(1/\sqrt n\)-Lipschitz.
The projected matrix is not Gaussian and does not have independent
columns; the proof does not make either claim.

For the projected dynamics, uniformly over all Gaussian input arrays,
\[
 \|w\|_\infty\le S,\qquad
 \|W\|_{\rm op}\le K+CS^2,\qquad
 \|k_a\|_2/\sqrt n\le CS.
\]
On \(E_n=\{\|G/\sqrt n\|_{\rm op}\le K\}\), projection is the
identity and both controlled trajectories agree. The net bound yields
\(\Pr(E_n^c)\le Ce^{-cn}\) for a fixed sufficiently large \(K\).

The conditional strengthening of the tail input is justified directly
by FINITE_TAIL_ROUTE:

- Its deterministic controlled estimates use only the boundedness and
  global Lipschitz continuity of \(\psi\), the bounded top activation,
  and the initialized matrix operator bound. They never require a norm
  bound on the initial transformed coordinates or an initial Gram gap.
- In the deleted-column argument, all first-layer coordinates are
  conditioned on. The surviving Gaussian column remains independent of
  the cavity. The Gaussian family is defined to be zero when the retained
  initialized matrix exceeds its operator bound.
- The true-carrier remainder is bounded by \(CS\) on \(E_n\), and
  no Gaussian law is declared after conditioning on \(E_n\) itself.
- The control class has metric entropy
  \(\log N(\varepsilon)\le
  C_m(1+S/\varepsilon)\log(2+S/\varepsilon)\).
  Its Gaussian increment metric is at most \(C\|b-c\|_\infty\).
  At dyadic scale \(S2^{-j}\), the Gaussian maximum estimate gives
  a summable bound
  \[
  CS2^{-j}\{\sqrt p+\sqrt{(j+1)2^j}\}.
  \]
  Summation gives \(CS\sqrt p\) for the carrier supremum.

All constants in these steps are uniform for every deterministic
initial feature array \(H_0\in(-1,1)^{n\times m}\). Terminal-time
suprema over the control class also bound all prefix times: freeze
each prefix driver for the remainder of \([0,S]\). Thus the needed
uniform conditional square-exponential carrier bound follows
from the dependency's proof without an extra first-layer hypothesis.

For projected carriers on \(E_n\), it gives
\[
 \mathbb E_G\left[\mathbf1_{E_n}
        \sup_{b,u}|k_{a,i}^b(u)|^4\right]\le CS^4.
\]
On \(E_n^c\), the deterministic RMS bound implies
\[
 \frac1n\sum_i |k_{a,i}^{\Pi}(u)|^4
 \le \frac1n\left(\sum_i |k_{a,i}^{\Pi}(u)|^2\right)^2
 \le CnS^4.
\]
Its expectation on the bad event is at most \(CnS^4e^{-cn}\).
This verifies the first assertion in the candidate's (5).

Writing \(U_{a,i}=p_{a,i}-p_{a,i}(0)\),
\(|U_{a,i}|\le S\sup|k_{a,i}|\). On \(E_n\), Gaussian-square
carrier tails therefore give every fixed linear-exponential moment
of \(\sup|U_{a,i}|\). On \(E_n^c\),
\(|U_{a,i}|\le CS^2\sqrt n\), so for fixed \(p\)
the contribution is bounded by
\[
 C\exp(-cn+CpS^2\sqrt n),
\]
uniformly in \(n\) and \(S\le1\). This proves the second assertion
in (5). The argument safely handles the dependence introduced by
projection rather than assuming it absent.

## 4. Matrix-initialization variance

Fix a deterministic \(H_0\). The common-driver state estimate in the
tail note, now with a nonzero initial matrix difference, gives
\[
 D_X(u)\le C\|\Delta W_0\|_F
\]
for the sum of normalized transformed-coordinate and readout
differences and the matrix Frobenius difference. The constant is
independent of \(n,H_0,b,S\le1\). The same estimate applies to
first variations.

Forward, top-backward and carrier variations have RMS at most
\(CD_X\). In the derivative of \(\Lambda_{ab}\), the only
additional carrier-weighted term is
\[
 \frac1n\sum_i\psi''(p_{a,i})\Delta p_{a,i}k_{a,i}^2.
\]
It is bounded by
\[
 4\frac{\|\Delta p_a\|_2}{\sqrt n}
       \left(\frac1n\sum_i k_{a,i}^4\right)^{1/2}.
\]
The squared-carrier derivative is bounded by the carrier RMS times
its RMS variation. The other Gram contributions have bounded RMS
factors. Hence
\[
 |D\Lambda_{ab}[\Delta X]|
 \le C\left[1+
       \left(\frac1n\sum_i k_{a,i}^4\right)^{1/2}\right]D_X.
\]

Composing with the \(1/\sqrt n\)-Lipschitz projected initialization
gives at a.e. Gaussian input
\[
 \|\nabla_G\Lambda_{ab}^{\Pi}\|_F^2
 \le\frac Cn\left(1+\frac1n\sum_i|k_{a,i}^{\Pi}|^4\right).
\]
The finite-dimensional functions are locally Lipschitz, so weak
gradients and a.e. differentiation suffice; differentiability of
the spectral projection everywhere is not required.
The conditional fourth-moment estimate makes this gradient square
integrable. Gaussian Poincaré therefore gives
\[
 \operatorname{Var}_G(\Lambda_{ab}^{\Pi}(u)\mid H_0)\le C/n.
\]
There is no hidden coordinate maximum in this bound.

## 5. First-layer randomness and the averaged Lipschitz estimate

The crucial distinction in the candidate is correct: it establishes
Lipschitz continuity of the matrix-averaged Gram, not a pathwise
operator norm bound for a random diagonal multiplier.

For \(-1<h<1\), set \(T(h)=F(\operatorname{artanh}h)\) and
\(J(h,U)=\psi(T(h)+U)\). Since \(T'=1/\psi'(T(h))\),
\[
 \partial_hJ(h,U)=
   \frac{\psi'(T(h)+U)}{\psi'(T(h))},\qquad
 |\partial_hJ(h,U)|\le e^{4|U|},\qquad
 |\partial_UJ|\le1.
\]
The logarithmic derivative calculation in Section 2 proves the
ratio bound uniformly even as \(h\) approaches \(\pm1\).

Fix two deterministic initial arrays \(H_0,H_0'\), use the same
projected matrix, and compare increment coordinates \(U,U'\).
They both start from zero, despite the potentially large difference
between \(T(H_0)\) and \(T(H_0')\). Coordinatewise,
\[
 |h_{a,i}-h_{a,i}'|
 \le e^{4|U_{a,i}|}|H_{0,ia}-H_{0,ia}'|
                   +|U_{a,i}-U_{a,i}'|.
\]

The random forcing size \(R\) in the candidate contains deterministic
weights \(|H_{0,ia}-H_{0,ia}'|^2\). For \(p\ge2\), apply
Minkowski in \(L^{p/2}(G)\) before taking the square root:
\[
 \left\|\left(\frac1n\sum_i
    e^{8\sup|U_{a,i}|}|\Delta H_{0,ia}|^2\right)^{1/2}\right\|_{L^p}
 \le
 \left(\frac1n\sum_i|\Delta H_{0,ia}|^2
       \|e^{8\sup|U_{a,i}|}\|_{L^{p/2}}\right)^{1/2}.
\]
The conditional exponential moment from Section 3 gives
\[
 \|R\|_{L^p(G)}
 \le C_p\|H_0-H_0'\|_F/\sqrt n.
\]
This argument would fail for arbitrary matrix-dependent perturbation
weights. Here the perturbation is fixed before taking the expectation,
which is exactly what a Lipschitz estimate for the averaged map needs.

Subtracting the increment-state equations gives the pointwise bound
\[
 \sup_{u\le S}D_{\rm inc}(u)\le CS e^{CS}R.
\]
Indeed, each vector-field difference is bounded by
\(C(D_{\rm inc}+R)\): first-feature differences have the preceding
bound; top-feature differences use bounded operators; top-backward
differences use \(\|w\|_\infty\le S\); the hidden update is a
rank-one product. Gronwall integrates against total driver variation
at most \(S\), and the initial increment-state difference is zero.
This gives the claimed \(L^p(G)\) RMS estimates for features,
top-backward fields and carriers.

Rewrite the last Gram summand using
\(\psi'(p)=(1-h^2)^2\). This coefficient is bounded and Lipschitz
on \([-1,1]\), so its difference is bounded by
\[
 C\frac{\|h_a-h_a'\|_2}{\sqrt n}
       \left(\frac1n\sum_i k_{a,i}^4\right)^{1/2}
 +C\frac{\|k_a-k_a'\|_2}{\sqrt n}.
\]
Cauchy--Schwarz in \(G\), the fourth carrier moment, and the
\(L^2(G)\) feature estimate yield
\[
 |\mathbb E_G\Lambda_{ab}^{\Pi}(u;H_0)
       -\mathbb E_G\Lambda_{ab}^{\Pi}(u;H_0')|
 \le C\|H_0-H_0'\|_F/\sqrt n.
\]
The other two Gram summands have simpler bounded-factor estimates.
No independence between the feature difference and carrier factor
has been invoked.

The initial \(Z_0\) coordinates are independent standard Gaussians
because the normalized training inputs are orthonormal.
The map \(Z_0\mapsto H_0=\tanh(Z_0)\) is 1-Lipschitz in
Frobenius norm. Gaussian Poincaré applied to the deterministic
matrix-averaged map now gives
\[
 \operatorname{Var}_{Z_0}
       (\mathbb E_G[\Lambda_{ab}^{\Pi}(u)\mid Z_0])\le C/n.
\]
Combining this with the conditional variance by total variance is
valid. For the prediction derivative, the coefficients \(b_b'(u)\)
are deterministic and have total absolute value at most one.
Cauchy--Schwarz for covariances therefore gives
\[
 \operatorname{Var}\left(\sum_b b_b'(u)\Lambda_{ab}^{\Pi}(u)\right)
 \le\left(\sum_b|b_b'(u)|
                   \sqrt{\operatorname{Var}\Lambda_{ab}^{\Pi}(u)}\right)^2
 \le C/n.
\]

## 6. Full activity interval and projection removal

The Gram entries of the projected path are deterministically bounded:
top features are bounded, top backward RMS is at most \(S\), and
carrier RMS is at most \(CS\). Thus
\(|df_a^{\Pi,b}/du|\le C\) a.e., independently of the initial
first-layer coordinates. Fubini/dominated integration identifies
the derivative of its mean with the mean derivative.

For \(g=f_a^{\Pi,b}-\mathbb Ef_a^{\Pi,b}\), one has \(g(0)=0\)
and
\[
 \sup_{u\le S}|g(u)|^2\le S\int_0^S|g'(u)|^2\,du.
\]
Expectation and the derivative variance bound give \(CS^2/n\).
No time mesh, derivative regularity in time, or supremum of a
Gaussian gradient over time is required.

Both original and projected controlled predictors satisfy
\(|f_a^b(u)|\le S\) for every initialization. They agree on
\(E_n\). Therefore their mean-square supremum difference is at most
\(CS^2e^{-cn}\), and their mean difference is at most \(CSe^{-cn}\).
The latter is the direct first-moment bound, not an unjustified
square root improvement. Combining the centered paths and using
\(e^{-cn}\le C/n\) proves the proposition for the original
Gaussian initialized controlled dynamics.

## 7. Scope limits and verdict

The candidate consistently centers at \(\mathbb Ef_n^b\), its
finite-width mean. It does not identify that mean at any numerical
rate with a population predictor. The example of a hypothetical
deterministic \(n^{-1/4}\) bias correctly illustrates a logical
possibility compatible with the variance estimate; it is not
presented as a counterexample for this network.

For one training sample, the residual equation preserves its initial
sign, so the activity-parametrized actual driver is the deterministic
path \(b(u)=\operatorname{sign}(y)u\), with the zero-label case
stationary. Applying the controlled result to an entire actual
training curve requires that its total activity be at most \(S\).
In the source setting this is supplied on the fitting event by
\(S=2Y/\kappa\). The result concerns the activity curve; its random
physical-time change and its population bias remain separate issues.
It is not an unconditional all-initialization assertion that every
actual training trajectory fits inside an arbitrarily chosen
\([0,S]\).

The revised candidate states these qualifications explicitly. It also
correctly distinguishes its unconditional prescribed-control variance
bound from a conditional variance given the fitting event; the latter
does not follow merely by reinterpreting the center of the former.

For several samples, the actual control is random. Uniform constants
for each deterministic driver do not imply an estimate after adaptive
driver selection. The candidate explicitly states this distinction.
The conditional Gaussian supremum in the tail proof is a different
argument and cannot be reused as if the centered prediction were
that Gaussian process.

Finally, the cavity remainder in the carrier decomposition is
\(O(S)\), not \(o_n(1)\). It includes the order-one population
response. Neither the \(L^2\) cavity distance nor the fluctuation
proposition proves the necessary response identification or a
coordinatewise Taylor-remainder estimate. These remaining steps
are correctly left open.

**Final verdict: PASS.** The controlled finite fluctuation bound is
proved under the stated restricted geometry and activation assumptions.
No remaining algebraic, Gaussian-dependence, normalized-gradient, or
averaged-map gap was found in the checked snapshots. **The actual
adaptive physical-time whole-input population root-width theorem
is not proved by this candidate.**
