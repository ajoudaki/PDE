# Internal adversarial check of Gaussian sign transport

Author: /root/harmonic_route, 2026-09-12.

**Scoped verdict: PASS. No mathematical correction to the frozen input is
required.** The covariance transport formulas retain the actual first-row
term. The rescaled source estimate supplies the necessary $L^4$ control;
the strong $O(s^4)$ remainder is justified. The reused-action calculation
has a strictly positive conditional Gaussian innovation variance, with its
response retained. The event of initial-contrast reversal has positive
probability at every sufficiently small fixed positive feature time.

This is an internal reconstruction, not an independent promotion review.
The result defeats the stated pointwise ordering cone for the actual
population reference. It neither reverses the previously proved expected
covariance sign nor establishes a covariance sign at the fitted endpoint
or an E₀ advantage.

## 1. Frozen inputs and complete coverage

Read the assigned GAUSSIAN_SIGN_TRANSPORT.md completely, lines 1–602,
including all claims, proofs, limitations and provenance. Its SHA-256 is

    5f44ec005410cbdfa4557580c243ea77c1abce6a067882a722d2552578cb484c

Its stated study dependency ROUTE_GAUSSIAN_SIGN.md was already read
completely, lines 1–484, and is retained at the unchanged hash

    2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c

The relevant established dependencies were already completely read within
the authorized source scope: global_nonlinear.md A.1–A.4; C.4.5.1 §§1–3
and its rational initialization certificate; C.4.5.2 §§1–4; the selected
strong equations in C.4.10; and special_data_limits.md III.F in full.
For this check I reread global_nonlinear.md lines 1840–1898 and 6104–6521,
and special_data_limits.md lines 3933–3976. These include the precise
local-forcing/source coefficients, common-flow passage, bounded-product
extension, action norm, and both source orientations used below.

Relevant established and process hashes:

| Input | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

The previously completely read solve-math-rigorously and
investigate-conjectures skills remain applied. No other current review,
other study, experiment, numerical integration, training run, or Git
operation supplied an input. The frozen input was preserved.

## 2. Relabeling, transport, and the proposed cone

The replacement $v_2=-w_2$ gives $H_2=-H_2^{\rm old}$ and
$z_2=-Z_2^{\rm old}$, while $S_2,\delta_2,Q_2$ remain unchanged.
Thus both readout and rank updates have positive label signs in (T5);
the factor $1/2$ is unchanged. This is the exact original reference in
different coordinates.

Differentiating $z_a=AH_a$ yields

$$
z_a'=\frac12\sum_b\langle H_a,H_b\rangle\delta_b
       +\frac12A(m_aA^*\delta_a).
$$

Both terms in (T6) are necessary. On the direct sum of two upper
population spaces, the Gram action and each diagonal $Am_aA^*$ action
are positive self-adjoint. That property is a Hilbert-space quadratic-form
property; it is not coordinatewise order preservation.

For $\delta_a=cS_a$, the strong derivative is
$\delta_a'=hS_a-2cT_aS_az_a'$. All products lie in $L^2$ on a finite
feature interval: the readout and scalar gates are bounded and $z_a'$ is
in $L^2$. A.4's bounded-multiplier continuity also gives continuity of the
derivative. Pairing with fixed $\xi_\pm\in L^2$ proves (T8).
Its second coefficient is $-1/v_0$, because the derivative of $S_a$
contributes the factor $-2$. Integrating gives exactly (T9), and extracting
the first-row term gives (T10).

For (T11), each rank part has norm at most
$\min(s,\sqrt{10})$, and each first-row part at most
$M^2\min(s,\sqrt{10})/2$. Summing over two anchors gives the stated
$(2+M^2)\min(s,\sqrt{10})$ bound. With
$\|\xi_\pm\|_2=\sqrt{2v_0}$ and $|h(S_1\pm S_2)|\le2$, the displayed
factors in (T11) follow. Subtracting the initial first integrand costs at
most twice that first bound, giving the $2\sqrt{2/v_0}\,s$ term in (T12).
These inequalities are valid and deliberately unsigned.

The endpoint bound (T13) is also valid:
$b(s)=\langle c,h\rangle\le s$, while $b(s_\dagger)=1$.
Thus $s_\dagger\ge1$, independently of any desired covariance sign.

Equal-label exchange gives $L_{11}=L_{22}$ and $L_{12}=L_{21}$ at the
population reference. Subtracting and adding (T6), then using
$S_1-S_2=-2h(T_1-T_2)$, gives (T14)–(T16) with their stated signs.
The divided-difference gate is continuous, positive, and at most one.
Its coefficient $\lambda$ is bounded on every finite feature horizon.
The first-row remainder is time-integrable in $L^2$, hence time-integrable
almost surely. Absolutely continuous coordinate representatives therefore
justify (T17) without assuming a sign for $\lambda$.

The proposed cone conditions $ch\ge0$ and $\xi_-d\ge0$ make the integrand
in (T16) nonnegative, giving $\beta_-\le0$; strictness additionally needs
positive integral. These are sufficient conditions rather than necessary
ones. Failure of the contrast condition need not change the sign of the
expectation. The report's crossing argument maintains this distinction.

## 3. Rescaled source moment bound

The rescaling of C.4.5.2 is legitimate. For $0<S\le1$, the whole interval
lies before the fitted endpoint by (T13), so the source proof's allowed
outer ball $M=7,C=4$ applies. Its local forcing argument, including the
width-first and zero-forcing order, is unchanged.

The proof's horizon-dependent quantities give

$$
E_S\le e^{36},\quad P_S\le17/2,\quad K_S\le14,\quad
2SP_SK_SE_S+SC^2+2S\le(238e^{36}+18)S.
$$

The $238$ is $2(17/2)14$. The last $18S$ is the learned coefficient
bound $16S$ plus the matching current response bound $2S$.
The current reverse source variance improves to $S^2$ because the exact
and Euler readouts satisfy $|c(t)|\le t\le S$. This improvement does not
change the outer ball used to extract response coefficients.

The common-source isometry and strong mesh completion pass the bounded
remainder and Gaussian variance to the actual flow. Minkowski's inequality
then gives $\|Q_a(t)\|_4\le C_QS$ for $t\le S$, and taking $S=t$ gives
(T19) with the stated $C_Q$. This is not an $L^4$ operator estimate for
$A_0$.

Jointly measurable representatives from the established strong flow allow
time integration of these moment bounds. In particular the use of
Minkowski to obtain the row displacement bound does not presume
unproved $L^4$ differentiability of the flow.

## 4. Explicit reconstruction of the strong remainder

The orders in (T21)–(T23) can be checked with fixed finite constants.
Here is one choice, solely to expose every error order. Put

$$
V_2=C_Q/4,\qquad Z_2=2V_2+\tfrac12,\qquad D_3=\tfrac73Z_2,\qquad
Q_3=2D_3+\tfrac12.
\tag{H1}
$$

Using $\|A_0\|\le2$ and $0<s\le1$, the following estimates follow in order:

$$
\|v_a(s)-v_a(0)\|_4\le V_2s^2,\quad
\|K(s)\|_{HS}\le s^2/2,\quad
\|z_a(s)-X_a\|_2\le Z_2s^2,
$$
$$
\|c-sh_0\|_2\le (Z_2/3)s^3,\quad
\|\delta_a-sd_a^0\|_2\le D_3s^3,\quad
\|Q_a-sq_a^0\|_2\le Q_3s^3.
\tag{H2}
$$

For the third bound, subtract $A_0H_a^0$ as
$A_0(H_a-H_a^0)+KH_a$. For the fifth, use
$c-sh_0$ and $s h_0(S_a-S_{X_a})$; the gate is two-Lipschitz.
For the last, use the actual identity
$Q_a-sq_a^0=A_0^*(\delta_a-sd_a^0)+K^*\delta_a$.

Thus $Q_a(s)/s\to q_a^0$ in $L^2$. The already proved uniform $L^4$
bound on $Q_a(s)/s$, an almost surely convergent subsequence, and Fatou
give $\|q_a^0\|_4\le C_Q$. This step is not circular.

Define further constants

$$
V_4=Q_3/8+V_2^2,\quad K_4=(D_3+V_2)/4,\quad
H_4=V_4+V_2^2,\quad Z_4=2H_4+K_4+V_2/2.
\tag{H3}
$$

Subtracting $s\phi'(v_a(0))q_a^0/2$ from $v_a'$ costs at most
$(Q_3/2+V_2C_Q)s^3$ in $L^2$. Integrating gives the row remainder
$V_4s^4$ in (T22). Subtracting the leading rank derivative costs at most
$(D_3+V_2)s^3$ in HS norm, so its integrated remainder is $K_4s^4$.

The scalar tanh Taylor remainder has magnitude at most the square of its
increment. Its $L^2$ norm is therefore at most $V_2^2s^4$, using the
previous $L^4$ displacement. This gives the activation remainder
$H_4s^4$. Finally expand

$$
z_a=A_0H_a+K H_a^0+K(H_a-H_a^0).
$$

The three remaining errors are bounded by
$2H_4s^4$, $K_4s^4$, and $(V_2/2)s^4$, respectively. The initial Gram is
$v_0I$, giving exactly

$$
z_a=X_a+\frac{s^2}{4}
 [v_0d_a^0+A_0(m_a^0q_a^0)]+R_{a,s},
\qquad \|R_{a,s}\|_2\le Z_4s^4.
\tag{H4}
$$

Consequently (T29) may use $C=2Z_4$. In particular its strong remainder
does not rely on an ambient Hessian, a third time derivative, a formal
series, or a moment bound on $A_0$ outside $L^2$.

## 5. Reused-action innovation and independence

The initial two forwards have no response term. Their outputs $X,Y$ are
independent centered Gaussians of variance $v_0$. The reverse inputs
$d_a^0=h_0S_{X_a}$ are bounded smooth functions of these two sources.
Their expected derivatives are

$$
\mathbb E\partial_Xd_1^0=\eta/2,\quad
\mathbb E\partial_Yd_1^0=\mu^2/2,\quad
\mathbb E\partial_Xd_2^0=\mu^2/2,\quad
\mathbb E\partial_Yd_2^0=\eta/2.
$$

For example the first derivative contains both the derivative of $h_0$
and that of $S_X$. Averaging yields
$\tfrac12\mathbb E(S_X^2-2T_X^2S_X)$; omitting the readout derivative
would give a different coefficient. Thus (T24) includes the correct
four response coefficients.

The reverse source pair is independent of the full initial first-row
root; its covariance is the Gram of $(d_1^0,d_2^0)$.
The actual reverse answers are not independent of the initialized action
or of their response terms.

In the final forward input
$r=m_1^0q_1^0-m_2^0q_2^0$, the two formal source derivatives are
$m_1^0$ and $-m_2^0$. Thus the new forward response is exactly
$\bar m(d_1^0-d_2^0)$, as in (T26). The initial first-row fields are
root-only functions, so no additional source derivative of $m_a^0$
occurs. The products meet A.2's bounded-gate extension of the finite
source theorem.

Expanding (T24) and using root independence and oddness gives

$$
\mathbb E[rH_1^0]=(\eta\kappa-\mu^2\bar m v_0)/2=\alpha v_0,\qquad
\mathbb E[rH_2^0]=-\alpha v_0.
$$

The division by $v_0$ in (T25) is therefore correct. The new forward
source is jointly Gaussian with the old forward sources, so its
orthogonal projection is $\alpha X-\alpha Y$. Its residual is
$\sigma G_*$ independent of $X,Y$, and

$$
\sigma^2=\|r-\alpha(H_1^0-H_2^0)\|_2^2.
\tag{H5}
$$

To verify strict positivity, split $r$ into its root-only part and
$N=m_1^0\zeta_1-m_2^0\zeta_2$. Independence of the reverse source
from the roots gives $\mathbb E[N\mid\text{first-row root}]=0$.
Thus $N$ is orthogonal to every root-only function, including the
projection subtracted in (H5). Conditional variance gives

$$
\mathbb E N^2
\ge(\gamma_d-\gamma_o)\mathbb E[(m_1^0)^2+(m_2^0)^2]
=2(\gamma_d-\gamma_o)\mathbb E\operatorname{sech}^8G.
$$

Here $\gamma_o\ge0$, so $\gamma_d-\gamma_o$ is the smallest eigenvalue.
The identity
$\gamma_d-\gamma_o=\tfrac12\mathbb E[h_0^2(S_X-S_Y)^2]>0$
is correct. Its integrand is positive off the two lines $X=Y$ and
$X=-Y$, a set of full Gaussian measure. This proves (T28).

The source law is about uncentered input Grams and centered Gaussian
source covariances; no centering correction has been lost. Subtracting
the two instances of (H4) and retaining the response in (T26) gives
exactly (T29), including the coefficient $v_0+\bar m$.
The Gaussian $G_*$ describes an innovation of the original reused action.
It is not noise added to the reference evolution.

## 6. The shrinking event and the actual crossing

The triple $(X+Y,X-Y,G_*)$ has the independence stated in §4.3:
the first two variables are jointly Gaussian with zero covariance, and
the third is independent of their pair by (T27).
No independence of the strong remainder $E_s$ from this triple is needed.

For an explicit lower-bound check, put

$$
p_a=\Pr\{|N(0,2v_0)|\le1\},\quad
p_G=\Pr\{-2\le N(0,1)\le-1\},\quad
\rho_*=(4\pi v_0)^{-1/2}e^{-1/(4v_0)}.
$$

All are strictly positive. Whenever $\sigma s^2/16\le1$, the Gaussian
density on the contrast interval is at least $\rho_*$. Therefore the
event in (T30) satisfies

$$
\Pr(\mathcal A_s)\ge c_0s^2,\qquad
c_0=p_ap_G\rho_*\sigma/16>0.
\tag{H6}
$$

The noninnovation term in the braces of (T29) is bounded by
$C_1|X-Y|$, with the report's $C_1$; the estimate uses only
$|h_0|\le1$ and the two-Lipschitz gate. On $\mathcal A_s$ the leading
expression is at most
$-3\sigma s^2/16+C_1\sigma s^4/64$.
If $C_1s^2\le4$, it is at most $-\sigma s^2/8$.

Chebyshev applied to the actual strong remainder gives

$$
\Pr\{|E_s|>\sigma s^2/16\}
\le (16C/\sigma)^2s^4.
\tag{H7}
$$

Thus, when additionally
$(16C/\sigma)^2s^2\le c_0/2$, subtraction of this unconditional bad-event
probability from (H6) gives a good intersection of probability at least
$c_0s^2/2>0$. On it the actual contrast is at most
$-\sigma s^2/16<0$, whereas $X-Y>0$. This proves (T18).

All three smallness conditions hold on some fixed positive interval.
For instance, with the explicit $C$ above, any

$$
0<s<
\min\left\{1,\frac4{\sqrt\sigma},\frac2{\sqrt{C_1}},
                  \frac{\sigma\sqrt{c_0}}{16\sqrt2\,C}\right\}
$$

satisfies them. The constants need not be practically small or numerically
evaluated for this existence theorem. The comparison is between an
order-$s^2$ event probability and an order-$s^4$ error probability, not
between an order-$s^2$ threshold and the bare $L^2$ error.

The quantifier is important and correct in the input: every sufficiently
small fixed deterministic time has a positive-probability crossing event,
which may depend on that time. It is not one positive-probability set that
crosses at all arbitrarily small times. That stronger assertion would
conflict with continuity when the initial contrast is strictly positive.

## 7. Claim limits and required corrections

| Component | Scoped verdict |
|---|---|
| Relabeling, actual covariance transport, and unsigned estimates | PASS |
| First-row remainder and integrating-factor cone diagnosis | PASS |
| Horizon-rescaled $L^4$ source bound | PASS |
| Strong $O(s^4)$ remainder with fixed finite constants | PASS; explicit constants reconstructed above |
| Actual reused-action response, innovation, and nondegeneracy | PASS |
| Positive-probability contrast reversal at every small fixed time | PASS |
| Change of expected covariance sign, sign at fitted endpoint, or E₀ advantage | Not established, and not claimed |

No required correction was found. The exact limiting population reference
is the object of the crossing theorem. This check does not turn it into a
finite-width probability theorem, a practical time window, or an obstruction
to every possible covariance-sign argument. Expected cancellations and
fitted-endpoint signs remain separate questions.
