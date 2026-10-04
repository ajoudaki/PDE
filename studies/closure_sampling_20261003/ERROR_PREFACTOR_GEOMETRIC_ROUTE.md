# A matched readout–residual estimate with polynomial gap dependence

2026-10-04. Independent scoped route, frozen before exchanging conclusions.
This is a new deterministic derivation conditional on the assigned source
and fitting theorems. It has not received an independent reconstruction or
promotion review. No experiment, external theorem, other study, or shared
Git mutation was used.

The route **closes the requested comparison estimate**, subject to checking
the derivation below. The current autonomous corrected-readout optimizer
and its source accuracy \(\epsilon=n^{-1}\) are unchanged. The raw estimate is

\[
 \sup_{t\le T,v}|f_C(t,v)-f_n(t,v)|
 \le C\lambda^{-1/2}\epsilon
       \exp\{C(Y/\lambda)(1+M)\}.                         \tag{1}
\]

Here \(M\ge1\) is the actual reference carrier maximum through \(T\).
Using its supplied bound \(M\le1+C(Y/\lambda)\sqrt{\log(en)}\) and
\(Y\le c\lambda\), (1) gives a strict root-width prefactor
\(C\lambda^{-1/2}\), with a structural constant. The all-time tail has
the same sufficient polynomial prefactor. No dataset-dependent
exponential is moved into a new width threshold.

## 1. Contract and frozen inputs

The model, all moving coordinates, fixed metrics, corrected readout,
internal residual equation, and physical time are precisely those of
`STORAGE_QUADRATIC_IMPROVEMENT.md`, equations (6)–(11). The reference is
the same realized canonical width-\(n\) dense network. The query set is
the entire unit sphere in normalized inputs \(v=x/\sqrt d\). Training
data are general compatible finite data; depth is arbitrary and fixed.
Constants below depend on fixed depth, dimension, activation bounds and
the supplied operator bounds, but not on \(m,n,Y,\lambda\), selected
widths, or minimum selected masses. The case \(Y=0\) is stationary.

Take \(0<\lambda\le1\), \(0<Y\le c\lambda\), and define the
dimensionless label scale

\[
                         s=Y/\lambda.                    \tag{2}
\]

The structural smallness constant \(c\) is chosen sufficiently small,
as in the current theorem. Shrinking a structural constant does not add
a gap or sample-count power to its label condition.

The raw coordinate source tolerance remains a free parameter

\[
                  0<\epsilon\le\min(1,Y).                \tag{3}
\]

Only at the final assembly is it set to \(n^{-1}\). The exact paired
source assumptions, exact initial training features, and reference
state \((A_R,B_R,w_R)\) are those in the assigned runtime proof. The
source horizon is \(T=C\lambda^{-1}\log(en)\).

The five complete scientific inputs were:

| File | SHA-256 |
| --- | --- |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| `STORAGE_QUADRATIC_CHECK.md` | `b373ee9212997c6e60002b2cf0ad613b6b58865ab82cc9589bc70931603724d9` |
| `GENERAL_WEIGHTED_COMPARISON.md` | `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306` |
| `DATASET_LABEL_DEPENDENCE.md` | `bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52` |
| `INPUT_DEPTH_REFINEMENT.md` | `9d468fe3469436c1c10cf01f9194cff7fea71339c8964578b83047b4f5c79a3d` |

Canonical notation, its neural-network reference, rigorous-math, and
conjecture-contract/audit instructions were also read. Earlier regimes
quoted historically in the check are superseded by the current input
condition \(Y\le c\lambda\).

## 2. Normalized operators and the refined reference bounds

All selected-neuron norms use their fixed \(H_\ell\) metrics. Hidden
parameter tuples use the first-weight and mixer Hilbert norms in the
runtime theorem. Adjoints in this note are Hilbert adjoints between the
displayed spaces. Sample space is Euclidean after dividing residuals by
\(\sqrt m\).

Let \(V_C,V_R:\mathbb R^m\to\mathbb R^{N_L}\) have columns
\(h_{C,a}^{(L)}/\sqrt m\) and \(h_{n,a,I_L}^{(L)}/\sqrt m\),
respectively. The second operator uses the actual selected reference
features, not a forward pass through \(B_R\). Define the hidden-direction
operator \(\mathcal J_C\) by its \(a\)-th column

\[
 \frac1{\sqrt m}\left(
  \delta_{C,a}^{(1)}v_a^\top,
  \left(\delta_{C,a}^{(\ell)}
      h_{C,a}^{(\ell-1)\top}H_{\ell-1}\right)_{\ell=2}^L
 \right).                                                \tag{4}
\]

Its target is the hidden-parameter Hilbert space. Define
\(\mathcal J_R\) with actual selected reference sources in (4).
Thus the exact equations for the raw hidden parameters and raw readout
are

\[
 \dot\theta_{h,C}=2\mathcal J_C(c_C/\sqrt m),\quad
 \dot\theta_{h,R}=2\mathcal J_R(c_n/\sqrt m),\quad
 \dot w_C=2V_C(c_C/\sqrt m),\quad
 \dot w_R=2V_R(c_n/\sqrt m).                              \tag{5}
\]

The compressed residual matrix divided by \(m\) is exactly

\[
 \mathcal K_C=V_C^*V_C+\mathcal J_C^*\mathcal J_C.
                                                               \tag{6}
\]

These identities use the Gram of the specified update directions. They
do not assert that those directions are the actual output derivatives.

The independently supplied fitting estimates, including their energy
improvement, imply the following bounds. Compressed bounds hold globally;
selected reference bounds hold through the source horizon

\[
 \begin{gathered}
 V_C^*V_C\succeq gI,\quad g=c_0\lambda,\qquad
 \|V_C\|+\|V_R\|\le C,\\
 \|w_C\|+\|\widehat w_C\|+\|w_R\|
       +\|\mathcal J_C\|+\|\mathcal J_R\|
          \le C\frac{Y}{\sqrt\lambda},\\
 \rho_C=\|c_C\|_m,\quad \rho_n=\|c_n\|_m,
 \qquad
 \int_0^\infty(\rho_C+\rho_n)\,dt\le Cs.
 \end{gathered}                                           \tag{7}
\]

The selected reference bounds in (7) require a small refinement of the
coarser source proof. Approximate each actual feature column by a vector
in its source space with coordinate error \(\epsilon\). For any sample
vector \(b\), exact isometry on that space and the column error bounds
give

\[
 \|V_R b\|_{H_L}
 \le \|V_n b\|_n+C\epsilon\|b\|_2,                     \tag{8}
\]

where \(V_n\) is the full-width normalized training-feature operator.
The estimate follows by inserting the same linear combination of the
column approximants on both sides; its operator error is bounded by
the normalized Frobenius error. Integrating the feature approximation
against the reference residual gives a source-space approximation to
\(w_n\) with coordinate error \(C\epsilon s\). Its selected norm is
therefore at most \(CY/\sqrt\lambda+C\epsilon s\). The first term is
the original energy/path-length estimate. Condition (3) and
\(Y\le c\lambda\le c\sqrt\lambda\) absorb the second term.
Selected backward responses have their original RMS bound plus
\(C\epsilon\), so obey the same bound. This proves the remaining
reference estimates in (7).

One particular velocity retains the useful energy scale. Put

\[
       \nu(t)=\|V_R(t)c_n(t)/\sqrt m\|_{H_L}.
\]

By (8), the original energy/path-length bound, and (3),

\[
 \int_0^T\nu(t)\,dt
 \le \frac12\int_0^T\|\dot\theta_n\|_{\rm mob}\,dt
          +C\epsilon\int_0^T\rho_n\,dt
 \le C\frac{Y}{\sqrt\lambda}.
                                                               \tag{9}
\]

Consequently \(\int_0^T\nu/\sqrt\lambda\le Cs\). This retains
the path-length improvement that an estimate \(\nu\le C\rho_n\)
would lose.

Actual compressed forward differentiation needs only bounded gates and
bounded mixer operators, hence

\[
                  \|\dot V_C\|
             \le C\frac{Y}{\sqrt\lambda}\rho_C.          \tag{10}
\]

No activation-adjoint identity or coordinate carrier bound for the
compressed system is used in (10).

## 3. Error variables and the exact readout decomposition

Use the following vectors and nonnegative norms:

\[
 \begin{aligned}
 a(t)&=\|\theta_{h,C}-\theta_{h,R}\|_{\rm hidden},\\
 e(t)&=(c_C-c_n)/\sqrt m,\qquad u(t)=\|e(t)\|_2,\\
 z(t)&=w_C-w_R,\qquad \Delta V=V_C-V_R,\\
 q&=V_C^*V_C,\quad T_C=V_Cq^{-1},\quad P_C=T_CV_C^*,\\
 p(t)&=T_Ce(t),\qquad \zeta(t)=z(t)+p(t),\\
 b(t)&=\|p(t)\|_{H_L}+\|\zeta(t)\|_{H_L}.
 \end{aligned}                                           \tag{11}
\]

The symbols \(T_C\) and \(T\) denote the current right inverse and
the source horizon, respectively. All initial error vectors vanish.
The projector \(P_C\) is orthogonal in the \(H_L\) metric, and

\[
 \|T_C\|\le g^{-1/2},\qquad V_C^*p=e,
 \qquad \|p\|\le g^{-1/2}u.                              \tag{12}
\]

The paired-source action defects and hidden-only forward subtraction
give

\[
 \sup_{\ell,v}\|h_C^{(\ell)}-h_{n,I_\ell}^{(\ell)}\|
        +\|\Delta V\|\le C(a+\epsilon).                 \tag{13}
\]

The selected-reference readout pairing defect satisfies

\[
 d_R:=V_R^*w_R-(y-c_n)/\sqrt m,
                 \qquad \|d_R\|_2\le Cs\epsilon.       \tag{14}
\]

Insert (14) in the exact corrected-readout formula. For its difference
\(\eta=\widehat w_C-w_R\), this gives the identity

\[
 \eta=(I-P_C)z-p-T_C\Delta V^*w_R-T_Cd_R.
                                                               \tag{15}
\]

Since \((I-P_C)p=0\), (7), (12)–(15) imply

\[
       \|\eta\|\le C\left[b+s(a+\epsilon)
                                  +\epsilon/\sqrt\lambda\right].
                                                               \tag{16}
\]

The inverse Gram acts on the residual-normal discrepancy and on feature
perturbations multiplied by the small readout. It does not multiply the
entire raw parameter error by \(\lambda^{-1/2}\).

Backward subtraction with the actual reference carrier, exactly as in
the assigned one-reference proof, now gives

\[
 \|\Delta\mathcal J\|:=\|\mathcal J_C-\mathcal J_R\|
 \le C\left[b+M(a+\epsilon)+\epsilon/\sqrt\lambda\right].
                                                               \tag{17}
\]

To see every factor, the changed gate multiplies the actual selected
reference carrier and costs \(CM(a+\epsilon)\). The changed mixer
multiplies a selected reference response of norm \(CY/\sqrt\lambda\).
The propagated upper response starts with (16). Paired reverse-action
defects cost \(C\epsilon\). Fixed-depth recursion adds these terms;
it does not multiply successive factors of \(M\). The rank-one
directions in (4) then use (13) and the bounded features. This proves
(17) in the hidden-parameter operator norm.

## 4. Matching the residual damping to the raw readout

Let \(\mathcal K_n=K_n/m\) be the actual original tangent Gram.
The source pairing proof supplies

\[
 D=V_R^*V_R+\mathcal J_R^*\mathcal J_R-\mathcal K_n,
                         \qquad \|D\|\le C\epsilon.     \tag{18}
\]

This is an operator estimate in normalized sample space: each normalized
Gram entry is at most its unnormalized pairing error divided by \(m\).
Both feature and backward pairing errors are covered by the source
hypotheses. The backward source norms in (7) only improve (18).

Set \(\Delta\mathcal K=\mathcal K_C-\mathcal K_n\). Its exact
factorization is

\[
 \begin{aligned}
 \Delta\mathcal K={}&V_C^*\Delta V+\Delta V^*V_R\\
 &+\mathcal J_C^*\Delta\mathcal J
       +\Delta\mathcal J^*\mathcal J_R+D.
 \end{aligned}                                           \tag{19}
\]

Define the nonnegative forcing bound

\[
                    F(t)=2\|T_C\Delta\mathcal K
                                      (c_n/\sqrt m)\|.
\]

Using \(T_CV_C^*=P_C\), (7), (9), (13), (17), and (18) yields

\[
 F\le C\left[
   (\rho_n+\nu/\sqrt\lambda+sM\rho_n)(a+\epsilon)
      +s\rho_n b+\epsilon\rho_n/\sqrt\lambda
 \right].                                                \tag{20}
\]

In particular, the \(\Delta V^*V_R\) term costs
\(C(a+\epsilon)\nu/\sqrt\lambda\), whose time integral has the
small coefficient (9). Replacing that velocity by its coarse residual
bound would lose the improvement. Each hidden Gram difference costs
\(C(Y/\lambda)\rho_n\|\Delta\mathcal J\|\), because one
hidden direction has norm \(CY/\sqrt\lambda\) and
\(\|T_C\|\le C/\sqrt\lambda\).

The residual and raw readout errors have exact equations

\[
 \dot e=-2(q+\mathcal J_C^*\mathcal J_C)e
                     -2\Delta\mathcal K(c_n/\sqrt m),\qquad
 \dot z=2V_Ce+2\Delta V(c_n/\sqrt m).                     \tag{21}
\]

Differentiating \(T_C=V_Cq^{-1}\) gives the useful identity

\[
 \dot T_C=(I-P_C)\dot V_Cq^{-1}-T_C\dot V_C^*T_C.
                                                               \tag{22}
\]

Since \(q^{-1}e=T_C^*p\), equations (10), (12), and (22) give

\[
                    \|\dot T_Ce\|\le Cs\rho_C\|p\|.
                                                               \tag{23}
\]

Using \(\langle p,V_Ce\rangle=\|e\|^2\) in the equation for
\(p=T_Ce\) therefore yields

\[
 \frac12\frac d{dt}\|p\|^2
 \le -2u^2
   +2\|p\|\|T_C\|\|\mathcal J_C\|^2u
   +Cs\rho_C\|p\|^2+\|p\|F.
\]

By (7) and (12), the second term is at most \(Cs^2u^2\).
Choose the structural label constant small enough to absorb it. Then

\[
 D^+\|p\|\le-c_1\frac{u^2}{\|p\|}
                      +Cs\rho_C\|p\|+F.                 \tag{24}
\]

At \(p=0\), also \(e=0\), and the norm-regularization argument gives
the same integrated inequalities, with the quotient interpreted as zero.
Because \(u\ge\sqrt g\|p\|\), dropping either the damping or the
terminal nonnegative norm in (24) gives, for every \(t\le T\),

\[
 \begin{aligned}
 \|p(t)\|&\le C\int_0^t[s\rho_C\|p\|+F]\,dr,\\
 \int_0^t u\,dr&\le\frac C{\sqrt\lambda}
                     \int_0^t[s\rho_C\|p\|+F]\,dr.
 \end{aligned}                                           \tag{25}
\]

The second bound loses only \(\lambda^{-1/2}\); its forcing has already
been lifted by the right inverse.

The sum \(\zeta=z+p\) cancels the readout forcing exactly. Equations
(21)–(22) give

\[
 \dot\zeta=2\Delta V(c_n/\sqrt m)+\dot T_Ce
       -2T_C\mathcal J_C^*\mathcal J_Ce
       -2T_C\Delta\mathcal K(c_n/\sqrt m).                \tag{26}
\]

The remaining term involving \(e\) has norm at most
\(C(Y^2/\lambda^{3/2})u\). On integrating it and applying (25),
its coefficient becomes \(CY^2/\lambda^2=Cs^2\). Thus (13),
(23), (25), and (26) prove

\[
 b(t)\le C\int_0^t
       [(a+\epsilon)\rho_n+s\rho_C b+F]\,dr.             \tag{27}
\]

This argument neither differentiates the source observation defect nor
uses a true-gradient identity for non-diagonal activation gates.

## 5. Closing the hidden and readout errors

Subtracting the hidden equations in (5), using (7) and (17), gives

\[
 a(t)\le C\frac{Y}{\sqrt\lambda}\int_0^t u\,dr
       +C\int_0^t\rho_n
             [b+M(a+\epsilon)+\epsilon/\sqrt\lambda]\,dr.
                                                               \tag{28}
\]

Insert (25) in the first term. Its coefficient becomes \(Cs\), so

\[
 a(t)\le Cs\int_0^t[s\rho_Cb+F]\,dr
       +C\int_0^t\rho_n
             [b+M(a+\epsilon)+\epsilon/\sqrt\lambda]\,dr.
                                                               \tag{29}
\]

Let \(E=a+b\). Adding (27) and (29), then inserting (20), using
\(s\le c\), \(M\ge1\), and \(\lambda\le1\), gives

\[
 E(t)\le C\int_0^t
 \left[M\rho_n+\rho_C+\frac{\nu}{\sqrt\lambda}\right]
                 \left[E+\frac\epsilon{\sqrt\lambda}\right]dr.
                                                               \tag{30}
\]

All coefficients on the right are actual reference or compressed
trajectory quantities already bounded independently of the comparison
error. Equations (7) and (9) imply

\[
 \int_0^T\left[M\rho_n+\rho_C+\nu/\sqrt\lambda\right]dr
                        \le Cs(1+M).                    \tag{31}
\]

Differentiate the integral majorant of (30), with initial value
\(\epsilon/\sqrt\lambda\). This proves

\[
 \sup_{t\le T}\left(E(t)+\epsilon/\sqrt\lambda\right)
 \le\frac\epsilon{\sqrt\lambda}\exp\{Cs(1+M)\}.         \tag{32}
\]

Independent fitting already gives the compressed Gram and operator
tube globally. Thus there is no additional small-error first-exit
condition needed to justify this comparison. For every query, use
(13), (16), the bounded top features, and the supplied source readout
pairing defect to get

\[
 |f_C-f_n|
 \le C\|\eta\|+C\|w_R\|(a+\epsilon)+Cs\epsilon
 \le C(E+\epsilon/\sqrt\lambda).
\]

Together with (32), this is (1), uniformly over the full query sphere at
the same physical time.

## 6. Tail with explicit polynomial dependence

The tail can be sharpened using the same projection identities, without
source assumptions after \(T\). Write

\[
 b_C=(y-c_C)/\sqrt m,\qquad
 \widehat w_C=(I-P_C)w_C+T_Cb_C.
\]

Equation (22), and its consequence for the projection derivative, give

\[
 \|\dot T_C\|\le C\lambda^{-1}\|\dot V_C\|,\qquad
 \|\dot P_C\|\le C\lambda^{-1/2}\|\dot V_C\|.            \tag{33}
\]

For completeness,
\(\dot P_C=(I-P_C)\dot V_CT_C^*
                  +T_C\dot V_C^*(I-P_C)\), which proves the second
bound. The globally bounded feature and hidden-direction norms give
\(\|\dot b_C\|\le C\rho_C\) and \(\|\dot w_C\|\le C\rho_C\).
Moreover \(\|b_C\|\le2Y\), \(\|w_C\|\le CY/\sqrt\lambda\),
and (10) remains valid globally. Differentiating the displayed formula
for \(\widehat w_C\) therefore gives

\[
 \|\dot{\widehat w}_C\|
 \le C\left[1+\lambda^{-1/2}
                         +Y^2/\lambda^{3/2}\right]\rho_C
 \le C\lambda^{-1/2}\rho_C.                              \tag{34}
\]

Every query feature has derivative at most
\(C(Y/\sqrt\lambda)\rho_C\). Hence

\[
 \sup_v|\partial_t f_C(t,v)|\le C\lambda^{-1/2}\rho_C(t),
\quad
 \sup_v|f_C(\infty,v)-f_C(t,v)|
     \le CY\lambda^{-3/2}e^{-c\lambda t}.                 \tag{35}
\]

The original flow has the supplied energy-based tail, bounded by the
same sufficient right side in this label regime. Compare each flow to
its value at \(T\), bounding its subsequent motion by its integrated
tail. Equations (1) and (35) yield the explicit raw all-time estimate

\[
 \sup_{t\in[0,\infty],v}|f_C(t,v)-f_n(t,v)|
 \le C\lambda^{-1/2}\epsilon e^{Cs(1+M)}
                 +CY\lambda^{-3/2}e^{-c\lambda T}.        \tag{36}
\]

Both flows continue autonomously. Their fitted limits are included.

## 7. Strict root-width assembly and retained size

The supplied reference event gives
\(M\le1+Cs\sqrt{\ell_n}\), with \(\ell_n=\log(en)\). Inserting
\(\epsilon=n^{-1}\) in (36) therefore gives the finite-horizon term

\[
 C\lambda^{-1/2}n^{-1}
                   \exp\{Cs+Cs^2\sqrt{\ell_n}\}.         \tag{37}
\]

Young's elementary inequality gives
\(Cs^2\sqrt{\ell_n}\le\ell_n/2+C's^4\). Thus (37) is at most

\[
 C\lambda^{-1/2}\exp\{Cs+C's^4\}\,n^{-1/2}
                              \le C\lambda^{-1/2}n^{-1/2}.
                                                               \tag{38}
\]

The last constant is structural because \(s\le c\). Choose the
structural horizon constant so \(e^{-c\lambda T}\le n^{-1}\).
Since \(Y\le c\lambda\), the second term in (36) is then at most
\(C\lambda^{-1/2}n^{-1}\). Consequently

\[
 \sup_{t\in[0,\infty],v}|f_C(t,v)-f_n(t,v)|
                  \le C\lambda^{-1/2}n^{-1/2}.           \tag{39}
\]

At confidence \(1-\eta\), any structural confidence dependence can
be retained as \(C_\eta\); there is no exponential dependence on
\(m\) or \(\lambda^{-1}\) in this runtime prefactor. With
\(\lambda=\gamma/m\), the displayed factor is \(C\sqrt{m/\gamma}\).
This is a sufficient bound, not an optimality or lower-bound claim.

The source tolerance is still exactly \(n^{-1}\), so
`INPUT_DEPTH_REFINEMENT.md` supplies the same retained size

\[
                 C\lambda^{-2}\log^{3d+2}(en)+Cm(d+1),
                                                               \tag{40}
\]

with its existing explicit logarithmic gap version before the usual
width simplification. All fixed and moving coordinates remain counted.
This route changes no runtime equations, stores no extra reference
variables, and needs no new source family. The variables \(p,\zeta\)
are proof devices only.

The inherited source probability theorem and its width threshold remain
inputs. Condition \(n^{-1}\le Y\) is the existing raw-tolerance
condition. Equation (38) holds directly without asking width to exceed
a dataset-dependent exponential, and (37) explicitly records the raw
amplification before using the bounded label ratio.

## 8. Audit and status

The decisive cancellation is (26), paired with the energy-metric
residual estimate (24). Their use of the hidden-direction norm
\(O(Y/\sqrt\lambda)\) produces only the dimensionless coefficient
\(Y^2/\lambda^2\). This is the point where the label hypothesis is
used beyond independent fitting.

The strongest potential failure modes are explicit and checkable:

1. If the selected-reference velocity in (9) were controlled only by
   residual activity, (31) would acquire an extra inverse square-root
   gap. Equation (8) plus original energy gives the required bound.
2. If the Gram difference in (19) lost its two-factor structure, the
   forcing estimate (20) would lose the small hidden response factor.
   Formula (19) is an exact algebraic identity plus the stated source
   Gram defect.
3. Treating gates as self-adjoint in \(H\) would be invalid. This proof
   uses only their bounded operator norms, the specified direction Gram,
   and the original one-reference backward subtraction.
4. A compact-horizon argument alone would not control the endpoint.
   Equations (33)–(36) give the explicit dimension-independent tail.
5. An exponential could be concealed by width absorption. Equations
   (36)–(38) show that only a structural function of bounded \(s\)
   remains before any new width restriction.

The conditional deterministic result is derived here, rather than
independently checked. Its source theorem, carrier event, and refined
source dimension are inherited inputs. An independent reconstruction of
(8), (20), (24)–(30), and (33)–(38) is the necessary next validation step
before treating this route as internally checked.
