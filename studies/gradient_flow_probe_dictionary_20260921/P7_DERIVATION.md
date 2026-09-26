# Full middle-increment factors through the eighth time power

This is a continuation of the same normalized two-probe investigation. The
independent candidate was frozen before cross-checking the other p7 routes.
The full expansion has additional residual-feedback factors beyond its
highest label degree: a nested sufficient list has `(14,28)` generators
through `t^7` (new p6), and `(26,46)` through `t^8` (new p7). These are
declared generator counts, not a minimality theorem for the Gaussian
population. In particular, the prior even/odd pairing does **not** justify
setting p6 equal to p5.

## Contract and notation

Use physical probes `x_a=sqrt(2)e_a`, normalized probe Gram `I`, unhalved
equal MSE `(r_1^2+r_2^2)/2`, zero limiting readout, and the physical
population mobilities. Write `W_0=W^(2)(0)`, `c=W^(3)`,
`g_a=W^(1)(0)e_a`, `h_a=phi(g_a)`, `Y_a=W_0h_a`, `H_a=phi(Y_a)`,
`phi=tanh`, `ell_a=phi'(g_a)`, `m_a=phi''(g_a)`,
`n_a=phi'''(g_a)`, and `d_a,e_a,f_a,k_a` for the first four derivatives
of phi at `Y_a`. Here the symbols `e_a` in derivative formulas denote
scalar gates; the input coordinate vectors appear only in the setup.
Products are pointwise on the stated population, and `u tensor h`
means `z -> u <h,z>_1`. Every adjoint is the actual `W_0^*`.

The labels are formal coefficient devices. No coefficient field depends
on a task's inputs, labels, sample count, or trained trajectory. All
pairings below are initial population expectations, not empirical task
contractions. The output is a finite formal coefficient statement.
Actual population Taylor differentiability through order eight needs the
corresponding product/expectation regularity; it is not established by
the lower-order strong-flow argument. Finite-dimensional smooth ODE jets
are exact, but empirical initial Grams do not equal their population
values without specially constructed fixtures.

Let `v=E[tanh(G)^2]`, `tau=E[tanh(sqrt(v)G)^2]`, with standard Gaussian
`G`. Initial probe Grams are `vI` and `tau I`. Define positive residuals
`b_a=y_a-output_a`. The exact vector field is

\[
\dot c=\sum_a b_a H_a(t),\quad
\dot W^{(2)}=\sum_a b_a u_a(t)\otimes h_a(t),\quad
\dot g_a=b_a\phi'(g_a(t))W^{(2)}(t)^*u_a(t),\qquad
u_a(t)=c(t)\phi'(Y_a(t)).
\tag{1}
\]

All time coefficients below are ordinary powers, without factorials.

## Existing p5 fields

The following reproduce the existing p5 definitions exactly:

\[
S=\sum_a y_aH_a,\quad U_{ab}=d_aH_b,\quad
L_{ab}=\ell_a^2W_0^*U_{ab},\quad F_{ab}=vU_{ab}+W_0L_{ab},
\]
\[
\mathcal D=\sum_a y_aSd_a\otimes h_a,\quad B_2=\mathcal D/2,
\quad q_a=\tfrac12y_a\ell_aW_0^*(Sd_a),\quad V_a=\ell_aq_a,
\]
\[
R_a=\tfrac12 y_a\sum_b y_bF_{ab},\quad
J=\sum_a y_ad_aR_a,\quad K_{3,a}=d_aJ/3+Se_aR_a,
\]
\[
\mathcal F=\sum_a y_a(K_{3,a}\otimes h_a+Sd_a\otimes V_a),
\]
\[
P_{4,a}=\frac{\ell_a}{4}\{y_aW_0^*K_{3,a}+B_2^*(y_aSd_a)\}
 +\frac{m_aq_a}{4}W_0^*(y_aSd_a),
\quad T_a=\ell_aP_{4,a}+m_aq_a^2/2,
\]
\[
E_a=W_0T_a+B_2V_a+\mathcal Fh_a/4,\quad
Q_a=d_aE_a+e_aR_a^2/2,\quad N=\sum_a y_aQ_a,
\]
\[
K_{5,a}=d_aN/5+(J/3)e_aR_a+Se_aE_a+Sf_aR_a^2/2,
\]
\[
\mathcal G=\sum_a y_a(K_{5,a}\otimes h_a+
 K_{3,a}\otimes V_a+Sd_a\otimes T_a).
\tag{2}
\]

Thus `P4` is the quartic part of the lower preactivation coefficient;
its displayed formula avoids division by a small lower gate. The old raw
columns are unchanged: lower `(h_1,h_2,2![V],4![T])`, upper
`(U11,U12,U21,U22,3![K3],5![K5])`, with the exact existing ordering.

## Residual feedback and the missing sixth-order upper factors

Define initial scalar polynomials and their upper readout fields:

\[
\beta_a=\langle J,H_a\rangle_2/3+\langle S,d_aR_a\rangle_2,
\quad B=\sum_a\beta_aH_a,
\]
\[
X_a=d_a(y_aB/20+\beta_aS/5),\quad
A_a=-\ell_a^2W_0^*X_a,
\quad Z_a=W_0A_a-vX_a
       =-\sum_b(y_a\beta_b/20+\beta_ay_b/5)F_{ab},
\]
\[
Z_a^+=\sum_b(y_a\beta_b/10+3\beta_ay_b/8)F_{ab},\quad
A_a^+=\sum_b(y_a\beta_b/10+3\beta_ay_b/8)L_{ab}.
\tag{3}
\]

The degree-five upper polynomial needed at the sixth time coefficient is

\[
M_a=\frac{d_a}{6}\sum_b(y_bd_bZ_b-\beta_bd_bR_b)
       -\frac14Be_aR_a+Se_aZ_a.
\tag{4}
\]

It comes from the fifth hidden coefficient and the sixth readout
coefficient, not from the highest label degree. The next time coefficient
also uses the degree-five polynomial

\[
P_a=\frac{d_a}{7}\sum_b\left[y_bd_b(Z_b^+-Z_b)
                         +\frac{11}{4}\beta_bd_bR_b\right]
       +\frac35Be_aR_a+Se_a(Z_a^+-Z_a/2).
\tag{5}
\]

In the initialized Gaussian population, parity and the actual adjoint
response give

\[
\beta_a=\frac23y_a(C_{\rm diag}y_a^2+C_{\rm off}y_{3-a}^2).
\tag{6}
\]

For `h=tanh(G)`, `ell=1-h^2`, `H=tanh(sqrt(v)G)`, `d=1-H^2`, put
`mu=E[d^2-2H^2d]`. The constants are

\[
C_{\rm diag}=(v+E\ell^2)E[H^2d^2]+E[h^2\ell^2]\mu^2,
\]
\[
C_{\rm off}=(v+E\ell^2)\tau E[d^2]+vE[\ell^2](E[d])^4.
\tag{7}
\]

Indeed write `W_0^*U_ab=zeta_ab+sum_j h_j mu_ab,j`. The source covariance
is `<U_ab,U_cd>_2`, and the nonzero response coefficient is
`mu_ab,b=mu` if `a=b`, otherwise `(E d)^2`. Independence of the Gaussian
source and lower row gives
`<U_ba,F_bc>=0` for `a!=c`, and the two diagonal cases in (7).
Substituting `R_b=(y_b/2)sum_c y_cF_bc` into beta yields (6).

256-node Gaussian quadrature gives
`Cdiag=0.0802460693411846`, `Coff=0.19148288432154675`;
the beta coefficients are approximately `0.0534973795607897` and
`0.1276552562143645`. This numerical discrepancy is not a rigorous
inequality bound, but the formulas show that radial beta is an extra
identity, not a symmetry consequence. If beta were radial,
`beta_a=kappa(y1^2+y2^2)y_a`, then `Z_a=-kappa(y1^2+y2^2)R_a/2`
and `M_a=-3kappa(y1^2+y2^2)K3_a/4`; this explains precisely the
special cancellation that cannot simply be presumed.

Treating the four `F_ab` as formal fields and using `d_a=1-H_a^2`, exact
rational coefficient algebra gives ranks 8 for the eight K3 columns,
12 after adjoining all twelve M columns, and 14 after adjoining all
twelve P columns. The radial beta part adds nothing, so the calculation
can use `beta=(y1^3,y2^3)` for the nonradial component. The pivot choices
below apply whenever `Cdiag!=Coff`. These are exact sufficient
collection identities after substituting the actual fields. Proving
minimal Gaussian support dimensions against the full p5 span additionally
requires nondegeneracy of the relevant conditional query innovations;
the formal rank computation alone does not prove that theorem.

## New homogeneous sixth-order lower and seventh-order upper fields

Let

\[
J_{3,a}=y_aW_0^*K_{3,a}+B_2^*(y_aSd_a).
\]

The degree-six lower activation coefficient is

\[
T_{6,a}=\frac{\ell_a^2}{6}
 \left[y_aW_0^*K_{5,a}+B_2^*(y_aK_{3,a})
                   +\frac14\mathcal F^*(y_aSd_a)\right]
 +\frac{\ell_am_aq_a}{6}J_{3,a}
 +\frac43m_aq_aP_{4,a}+\frac13n_aq_a^3.
\tag{8}
\]

This follows by collecting coefficient five in
`phi'(g_a(t)) W(t)^*[b_a(t)u_a(t)]`, dividing by six, and composing
`phi(g_a(t))`. The composition terms `m_a q_a P4_a+n_a q_a^3/6`
combine with velocity terms to give the final coefficients `4/3` and
`1/3` in (8). Every term is divisible by `y_a`, hence has six possible
binary sextic coefficients per axis.

Set

\[
E_{6,a}=W_0T_{6,a}+B_2T_a+\mathcal F V_a/4+\mathcal G h_a/6,
\]
\[
O=\sum_a y_a(d_aE_{6,a}+e_aR_aE_a+f_aR_a^3/6),
\]
\[
K_{7,a}=\frac17d_aO+\frac15Ne_aR_a
 +\frac13J(e_aE_a+f_aR_a^2/2)
 +S(e_aE_{6,a}+f_aR_aE_a+k_aR_a^3/6).
\tag{9}
\]

There are eight binary septic coefficients of each K7, hence sixteen
new upper candidates.

## Complete time expansion and containment

The following formulas expose all lower label degrees. Let
`kappa=7tau^2/12`, `rho=31tau^4/360`, `sigma=13tau^2/6`. Then

\[
h_{a,0}=h_a,\quad h_{a,1}=0,\quad h_{a,2}=V_a,\quad
h_{a,3}=-\tau V_a,\quad h_{a,4}=\kappa V_a+T_a,
\]
\[
h_{a,5}=-\tau^3V_a/4-2\tau T_a+A_a,\qquad
h_{a,6}=\rho V_a+\sigma T_a+\tau A_a^++T_{6,a}.
\tag{10}
\]

The corresponding upper preactivation coefficients replace
`(V,T,A,Aplus,T6)` in (10) by `(R,E,Z,Zplus,E6)`.

For completeness define the degree-five scalar feedback

\[
\gamma_a=\langle N,H_a\rangle/5+\langle J,d_aR_a\rangle/3
                  +\langle S,Q_a\rangle,\quad C=\sum_a\gamma_aH_a,
\]
\[
\delta_a=\frac16\left\langle\sum_b(y_bd_bZ_b-\beta_bd_bR_b),H_a\right\rangle
            -\langle B,d_aR_a\rangle/4+\langle S,d_aZ_a\rangle,
\quad D_\delta=\sum_a\delta_aH_a.
\tag{11}
\]

The positive residual coefficients through order six are

\[
b_{a,0}=y_a,\quad b_{a,1}=-\tau y_a,\quad b_{a,2}=\tau^2y_a/2,
\]
\[
b_{a,3}=-\tau^3y_a/6-\beta_a,\quad
b_{a,4}=\tau^4y_a/24+7\tau\beta_a/4,
\]
\[
b_{a,5}=-\tau^5y_a/120-8\tau^2\beta_a/5-\gamma_a,
\]
\[
b_{a,6}=\tau^6y_a/720+61\tau^3\beta_a/60+8\tau\gamma_a/3-\delta_a.
\tag{12}
\]

The upper factor coefficients are

\[
u_{a,0}=0,\quad u_{a,1}=Sd_a,\quad u_{a,2}=-\tau Sd_a/2,
\quad u_{a,3}=\tau^2Sd_a/6+K_{3,a},
\]
\[
u_{a,4}=-\tau^3Sd_a/24-3\tau K_{3,a}/2-Bd_a/4,
\]
\[
u_{a,5}=\tau^4Sd_a/120+5\tau^2K_{3,a}/4+7\tau Bd_a/20+K_{5,a},
\]
\[
u_{a,6}=-\tau^5Sd_a/720-3\tau^3K_{3,a}/4
             -5\tau K_{5,a}/2-4\tau^2Bd_a/15-Cd_a/6+M_a,
\]
\[
u_{a,7}=\tau^6Sd_a/5040+43\tau^4K_{3,a}/120+10\tau^2K_{5,a}/3
 +61\tau^3Bd_a/420+8\tau Cd_a/21-D_\delta d_a/7+\tau P_a+K_{7,a}.
\tag{13}
\]

These coefficients are obtained by substituting (10) into
`H_a(t)=phi(Y_a(t))`, computing `c_{k+1}=sum_a sum_{i+j=k} b_ai H_aj/(k+1)`,
then multiplying `c(t)phi'(Y_a(t))`. In particular, the time-six and
time-seven M/P pieces have different collection ratios.

For every `2<=q<=8`, the complete middle coefficient is the finite sum

\[
[t^q](W^{(2)}(t)-W_0)=\frac1q\sum_a
  \sum_{i+j+k=q-1}b_{a,i}u_{a,j}\otimes h_{a,k},\qquad j\ge1.
\tag{14}
\]

Equations (10)--(14) prove containment in the stated two-sided spans:
the residual coefficients are scalars; `A,Aplus` use old L fields;
`Bd,Cd,Ddelta*d` use old U fields; the only upper additions are M,P,K7;
the only lower additions are T6. This does not discard lower label
degrees and does not assume frozen residuals or either frozen hidden
block.

## Nested raw lists and scales

Coefficient ordering uses `[y1^(d-j)y2^j]`, increasing `j`. Retain every
existing p5 raw column in its original position and scale.

For p6 append four upper columns `6![monomial]M_a`, in the order
`(a,j)=(1,1),(1,2),(2,3),(2,4)` at total label degree five.
There are no new lower columns. Thus the declared p6 list is `(14,28)`.

For p7 retain that complete p6 list and append:

- Lower: `6![y1^(6-j)y2^j]T6_1`, `j=0,...,5`, then the same T6_2
  coefficients for `j=1,...,6`.
- Upper: `7![y1^4 y2](tau P_1)` and `7![y1 y2^4](tau P_2)`, then
  `7![y1^(7-j)y2^j]K7_a`, `a=1,2`, `j=0,...,7`.

This gives 26 lower and 46 upper generators: 72 vectors and 1196 free
middle entries. Factorials refer to the **time derivative of that
factor**, not its label degree: M occurs at time six despite label
degree five, and tau P occurs at time seven despite label degree five.
These nonzero scales preserve spans but matter for a fixed ridge.

## Required population contractions

No dense correction operator needs to be formed. Beyond the existing
`<h_b,V_a>` and `<Sd_b,Sd_a>`, only these families are needed to build
the retained new fields:

\[
\langle h_b,T_a\rangle_1,\qquad
\langle V_b,V_a\rangle_1,\qquad
\langle Sd_b,K_{3,a}\rangle_2.
\tag{15}
\]

For example,

\[
B_2^*(y_aK_{3,a})=\tfrac12\sum_b y_bh_b
                            \langle Sd_b,y_aK_{3,a}\rangle_2,
\]
\[
\mathcal F^*(y_aSd_a)=\sum_b y_b\{h_b\langle K_{3,b},y_aSd_a\rangle_2
                   +V_b\langle Sd_b,y_aSd_a\rangle_2\},
\]
\[
B_2T_a=\tfrac12\sum_b y_bSd_b\langle h_b,T_a\rangle_1,
\]
\[
\mathcal F V_a/4=\tfrac14\sum_b y_b
    \{K_{3,b}\langle h_b,V_a\rangle_1+Sd_b\langle V_b,V_a\rangle_1\},
\]
\[
\mathcal G h_a/6=\tfrac16\sum_b y_b
 \{v\delta_{ab}K_{5,b}+K_{3,b}\langle V_b,h_a\rangle_1
                                  +Sd_b\langle T_b,h_a\rangle_1\}.
\tag{16}
\]

The scalar gamma/delta expectations in (11) are well-defined initial
population contractions for the full expansion, but their individual
values are unnecessary for the retained spans, because their factor
fields are already U. Formula (15) requires Gaussian peeling for the
population-derived implementation; substituting empirical contractions
would define a different candidate. The independently supplied
`p7_gaussian_check.population_contractions` API supplies UK, hT, VV,
hV, C and beta in ordinary binary polynomial coefficient convention.

## Verification and remaining distinction

The scratch exact symbolic rank check is in
`data/generated/gradient_flow_probe_dictionary_20260921/p7_derivation01/structural.py`.
It verifies the ranks and pivot choices quoted above with exact rational
arithmetic. The finite formal-series comparison is an algebra check,
not a width-limit test or training experiment. The population Gaussian
moment check and finite exact-Gram oracle are separate validations.

The strict claim that p6 increases the **minimal actual Gaussian span**
over all p5 columns is not proved by the formal rank alone. What is
established here is the full feedback mechanism, its extra formally
independent factor combinations, and a sufficient nested construction
that retains them. Any smaller construction must prove the missing
containment using the actual Gaussian law instead of assuming parity.
