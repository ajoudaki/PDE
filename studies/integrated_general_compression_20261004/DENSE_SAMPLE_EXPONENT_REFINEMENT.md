# Dense comparison with polynomial sample dependence

**Interface correspondence (2026-10-05).** [RESULT.md](RESULT.md),
(dense upper), is this note's bound with `B=beta^(100L)` and
the normalized gap `g=gamma/m` expanded. Its `E_dense(n)` is a certificate for an
independent same-width dense copy, not an approximation to a population
predictor. The local proof notation and numbered arguments below are
unchanged; their small-label and eventual-width conditions remain required.

2026-10-04. **Internally checked refinement.** A two-endpoint parameter
energy identity removes the inverse-gap factor caused by feeding an
integrated residual discrepancy back through scalar Gronwall. The remaining
activity-squared exponential then admits a convexity envelope on the
already stipulated label range. Its actual label coefficient remains in
the displayed bound. All dependence on the sample gap is polynomial
outside the exponential.

This continues the same general study. It changes neither initialization,
training dynamics, activation class, data assumptions, nor the allowed
label range. It does not prove strict root-width self-averaging or quantify
the stochastic source threshold. No canonical statement or earlier note
is edited by this work.

## 1. Result

Fix hidden depth \(L\ge2\), dimension \(d\ge1\), and \(m\) unit
training inputs \(v_a=x_a/\sqrt d\). All hidden layers have width \(n\).
Write
\[
 z^{(1)}(v)=Av,\qquad
 z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
 h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
 f_n(v)=w^\top h^{(L)}(v)/n.
\]
First-weight entries are independent \(N(0,1)\), hidden-mixer entries
are independent \(N(0,1/n)\), all initialized blocks are independent,
and \(w(0)=0\). Train the squared mean loss with mobilities
\((n,1,\ldots,1,n)\). Labels are fixed and signed, and
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\).

The initial population covariances are
\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\qquad
 Z\sim N(0,Q^{(j-1)}),\qquad
 \gamma=\lambda_{\min}(Q^{(L)})>0.
\]
Activations are real on the real axis, holomorphic on
\(|\Im z|<a\), with bounded first derivative on that strip. Values
need not be bounded. Define
\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,{16\over a},
  \max_j\sup_{|\Im z|\le a/2}|\phi_j'(z)|,
  \max_j\sup_{|\Im z|\le a/2}|\phi_j''(z)|\right\},
 \qquad B=\beta^{100L}.                              \tag{1}
\]
The strip hypothesis makes \(\beta\) finite. Assume exactly the
existing common allowance
\[
 0<Y\le{\gamma\over m}\beta^{-30L}.                  \tag{2}
\]
For independently initialized dense copies, let
\[
 \|f_n-f_n'\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|v\|=1}|f_n(t,v)-f_n'(t,v)|.
\]
The endpoint is the fitted physical limit. For \(0<\delta<1\), at
every sufficiently large individual width, with probability at least
\(1-\delta\),
\[
 \boxed{\begin{aligned}
 \|f_n-f_n'\|_*
 &\le BY\left(1+{m\over\gamma}\right)^2
 \left[1+B{Ym\over\gamma}\sqrt{\log(en)}\right]\\
 &\quad\times
 \left[1+B\left({Ym\over\gamma}\right)^2
                 \left(e^{\sqrt{\log(en)}}-1\right)\right]
 \sqrt{{\log[8(n+1)(1+2n)^d/\delta]\over n}}.
 \end{aligned}}                                                   \tag{3}
\]
In particular no sample-count or inverse-gap factor occurs in the
exponent. Expanding the two brackets gives polynomial dependence on
\(m/\gamma\), with explicit actual label factors of orders one
through four. The \(e^{\sqrt{\log(en)}}\) factor remains unbounded
in width, so the result is near-root rather than strict root-width.
For \(Y=0\), both predictors are identically zero.

The finite-width source event still has an unquantified eventual
threshold. Equation (3) concerns each sufficiently large width; it is not
one event over infinitely many independent widths. The same original
physical time is used in both copies throughout.

## 2. Imported physical input and explicit constants

The following are temporary proof quantities. Put
\[
 g=\gamma/m,\qquad z=Y/g,\qquad h=1+1/g,\qquad
 u_n=\sqrt{\log(en)},\qquad \kappa=g/2.
\]
Let
\(s=\max(1,\max_j\sup_{|\Im z|\le a/2}|\phi_j'(z)|)\),
\(t_2=\max_j\sup_{|\Im z|\le a/2}|\phi_j''(z)|\), and
\(T=9s\). For a standard real Gaussian \(Z\), define
\[
 q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}Z)^2,\qquad
 H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}).
\]
The dense fitting theorem and source event give all-time matrix caps
nine, whole-sphere feature RMS at most \(2H\), readout RMS at most
\(R=2Y/\sqrt g\), and
\[
 \rho(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\kappa t},
 \qquad \int_0^\infty\rho\le Y/\kappa,
 \qquad K(t)/m\succeq gI/4.                           \tag{4}
\]
Here \(r_a=f_n(v_a)-y_a\), and \(K\) is the tangent Gram defined
below. The complete source-envelope check in this study gives
\(S_*^{\rm src}\ge\beta^{-26L}\) and
\(K_{\rm src}\le\beta^{21L}\). The common cap (2) implies
\(S=16z\le S_*^{\rm src}\). Its all-time training-carrier bound is
\[
 M=2K_{\rm src}S u_n\le\beta^{22L}z u_n.              \tag{5}
\]
The factor two includes the already justified deterministic post-horizon
tail. This is the same source event and eventual threshold as before.

For an actual trajectory set
\[
 k_a^{(L)}=w,\quad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\quad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
Then \(\max_{a,j,i,t}|k_{a,i}^{(j)}(t)|\le M\). Define
\[
 F_z=2HT^{L-1},\quad B_\delta=sT^{L-1}R,\quad
 P=1+2H(L-1),\quad G=PB_\delta+2H,
\]
\[
 D_\delta=sT^{L-1}(1+B_\delta)+Lt_2F_zT^{L-1}M,
 \qquad J=PD_\delta+[1+(L-1)B_\delta]sF_z.             \tag{6}
\]
These are the already checked good-pair subtraction coefficients; their
definitions are repeated to make the new energy calculation explicit.
The earlier elementary envelope gives
\[
 H\le\beta^{3L/2},\quad g\le\beta^{3L},\quad
 R\le\beta^{-28L},\quad B_\delta\le1,\quad
 P,G\le\beta^{3L},\quad F_z\le\beta^{4L},
\]
\[
 D_\delta\le\beta^{8L}(1+M),\qquad
 J\le\beta^{12L}(1+M).                              \tag{7}
\]
These uses of (2) keep readout and backward RMS coefficients inside their
existing small-label physical tube; they do not replace the actual label
amplitude in (3).

## 3. Exact two-endpoint Taylor remainder

Use normalized Hilbert coordinates
\[
 \theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]
For two actual good states write \(\Delta=\theta-\theta'\) and
\(d_\theta=\|\Delta\|_2\), with Frobenius norms for matrix blocks.
Let \(D_h\) be the sum of its \(L\) hidden block norms and
\(D_w=\|w-w'\|_2/\sqrt n\). Thus
\[
 D_h\le\sqrt L\,d_\theta,\qquad
 D_h+D_w\le\sqrt{L+1}\,d_\theta.                    \tag{8}
\]
The second inequality has \(L+1\) blocks, including readout.
Forward subtraction gives, for every training sample,
\[
 \|\Delta z^{(j)}\|_2/\sqrt n\le F_zD_h,\qquad
 \|\Delta h^{(j)}\|_2/\sqrt n\le sF_zD_h.            \tag{9}
\]

Anchor all derivatives and backward carriers at the unprimed endpoint.
Write
\[
 a^{(j)}=\Delta h^{(j)}-
      \operatorname{diag}(\phi_j'(z^{(j)}))\Delta z^{(j)},\qquad
 e^{(j)}=\Delta h^{(j)}-D_\theta h^{(j)}[\Delta].
\]
Scalar Taylor's formula on the real interval between the two
preactivations gives
\( |a_i^{(j)}|\le(t_2/2)|\Delta z_i^{(j)}|^2\).
For \(j\ge2\), direct subtraction, using the unprimed mixer, gives
\[
 e^{(j)}=\operatorname{diag}(\phi_j'(z^{(j)}))
       [W^{(j)}e^{(j-1)}-\Delta W^{(j)}\Delta h^{(j-1)}]
            +a^{(j)},\qquad e^{(1)}=a^{(1)}.
\]
Let \(\xi_a(\theta)=\nabla_\theta f_n(v_a)\). Backward expansion
of the last identity proves the exact remainder formula
\[
 \begin{aligned}
 f_n(\theta,v_a)-f_n(\theta',v_a)-\langle\xi_a(\theta),\Delta\rangle
 &=\frac1n\sum_{j=1}^L k_a^{(j)\top}a_a^{(j)}\\
 &\quad-\frac1n\sum_{j=2}^L
        \delta_a^{(j)\top}\Delta W^{(j)}\Delta h_a^{(j-1)}
       -\frac1n\Delta w^\top\Delta h_a^{(L)}.
 \end{aligned}                                                    \tag{10}
\]
Every carrier here belongs to the actual unprimed trajectory. No carrier
bound on an interpolating parameter state is used. The scalar activation
Taylor formula requires only the global real second-derivative bound.

Equations (8)--(10) imply, separately for every training sample,
\[
 |f_n(\theta,v_a)-f_n(\theta',v_a)
       -\langle\xi_a(\theta),\Delta\rangle|
                         \le C_Td_\theta^2,
\]
\[
 C_T=sF_z\sqrt L+LB_\delta sF_z
                           +\frac{L^2t_2F_z^2}{2}M
                \le\beta^{11L}(1+M).                \tag{11}
\]
The three coefficients come respectively from the last, middle, and
first terms in (10). For example the curvature term is at most
\((Lt_2M/2)F_z^2D_h^2\), which gives the stated \(L^2\) factor.
The intermediate mixed terms use
\(\|\delta_a^{(j)}\|_2/\sqrt n\le B_\delta\).

The gradient blocks are exactly
\[
 \xi_a=\left(
 \delta_a^{(1)}v_a^\top/\sqrt n,
 (\delta_a^{(j)}h_a^{(j-1)\top}/n)_{j=2}^L,
 h_a^{(L)}/\sqrt n\right).
\]
The checked endpoint subtraction (6), now using (8), gives
\[
 \|\xi_a\|_2\le G,\qquad
 \|\xi_a-\xi_a'\|_2
              \le J\sqrt{L+1}\,d_\theta.             \tag{12}
\]
This too uses actual endpoint carriers only.

## 4. Residual feedback cancels in parameter energy

The exact normalized parameter flow is
\(\dot\theta=-(2/m)\sum_a r_a\xi_a\). Put
\(v_a^{\rm err}=f_n(\theta,v_a)-f_n(\theta',v_a)=r_a-r_a'\),
and let \(\|v^{\rm err}\|_m^2=m^{-1}\sum_a|v_a^{\rm err}|^2\).
Then
\[
 \frac12\frac d{dt}d_\theta^2
 =-\frac2m\sum_a v_a^{\rm err}\langle\Delta,\xi_a\rangle
  -\frac2m\sum_a r_a'\langle\Delta,\xi_a-\xi_a'\rangle.
                                                               \tag{13}
\]
Substitute (10) into the first pairing and apply (11)--(12). Since
\(\|v^{\rm err}\|_m\le\rho+\rho'\),
\[
 \frac12\frac d{dt}d_\theta^2
 \le-2\|v^{\rm err}\|_m^2
  +2\{C_T(\rho+\rho')+\sqrt{L+1}J\rho'\}d_\theta^2.
                                                               \tag{14}
\]
This negative prediction-difference square is the positive-semidefinite
gradient feedback retained by the new argument. Bounding the residual
discrepancy in absolute value before taking parameter energy loses this
cancellation and produces the extra reciprocal-gap factor.

Integrating (14), using both residual envelopes in (4), gives
\[
 \sup_{t\ge0}d_\theta(t)
       \le d_\theta(0)e^{E_{\mathrm{en}}},\qquad
 E_{\mathrm{en}}=2(2C_T+\sqrt{L+1}J)Y/\kappa.
                                                               \tag{15}
\]
The assertion follows also when the discrepancy vanishes, by a regularized
norm or uniqueness. The explicit ledger (7), (11), and
\(\sqrt{L+1}\le\beta^L\) give
\[
 E_{\mathrm{en}}\le\beta^{14L}z(1+M)
           \le\beta^{14L}z+\beta^{36L}z^2u_n.         \tag{16}
\]
Thus the actual stability exponent has been improved before making any
convexity envelope. It has one residual-activity factor multiplying the
carrier maximum, rather than the previous integrated-residual feedback
factor. Equation (16) still contains inverse gaps; the next step converts
it to a polynomial envelope while preserving its actual label coefficients.

## 5. Readout refinement retains the actual label amplitude

The mean tangent Gram is \(K_{ab}=\langle\xi_a,\xi_b\rangle\).
By (6), the difference between two such matrices obeys
\(\|\Delta K/m\|_{\mathrm{op}}\le2GJ(D_h+D_w)\).
The damped residual-difference equation therefore gives
\[
 \int_0^\infty\|r-r'\|_m\,dt
 \le{4GJ\over\kappa}\int_0^\infty\rho(D_h+D_w)\,dt.
                                                               \tag{17}
\]
This use of the gap is confined to the prefactor after (15) has already
closed stability; it is not fed back into a Gronwall exponent.

The exact readout subtraction and its zero initial discrepancy yield
\[
 D_w(t)\le4H\int_0^t\|r-r'\|_m\,ds
                      +2sF_z\int_0^t\rho D_h\,ds.
\]
Equations (8), (15), (17), and \(\int\rho\le Y/\kappa\) give
\[
 \sup_tD_w(t)
 \le\sqrt{L+1}\left({16HGJ\over\kappa}+2sF_z\right)
                       {Y\over\kappa}d_\theta(0)e^{E_{\mathrm{en}}}.
\]
Prediction subtraction on the whole sphere is at most
\(2HD_w+RsF_zD_h\). Consequently
\[
 \|f-f'\|_*
       \le\sqrt{L+1}\,Y C_Yd_\theta(0)e^{E_{\mathrm{en}}},
\]
\[
 C_Y={2H\over\kappa}
          \left({16HGJ\over\kappa}+2sF_z\right)
                       +{2sF_z\over\sqrt g}
                  \le\beta^{21L}h^2(1+M).            \tag{18}
\]
The last bound is the checked three-term expansion
\(128H^2GJ/g^2+8HsF_z/g+2sF_z/\sqrt g\), with (7).
This exhibits explicitly why inverse gaps remain polynomially in the
prefactor and why the overall comparison still vanishes with the actual
label amplitude.

## 6. Convexity transfers the gap dependence outside the exponential

The only uses of the existing label range in this step are
\[
 0\le\beta^{14L}z\le1,\qquad
 0\le\beta^{36L}z^2\le1,\qquad z\le1.              \tag{19}
\]
For \(0\le a\le1\), convexity gives \(e^a\le1+2a\).
For \(0\le\vartheta\le1\) and \(u\ge0\), convexity gives
\(e^{\vartheta u}\le1+\vartheta(e^u-1)\). Applying these to
the two actual coefficients in (16) gives
\[
 e^{E_{\mathrm{en}}}
 \le(1+2\beta^{14L}z)
             [1+\beta^{36L}z^2(e^{u_n}-1)].           \tag{20}
\]
In particular the actual \(z^2=(Ym/\gamma)^2\) is retained; it is
not replaced by its maximum allowed value. The gap-free exponential is
multiplied by that actual coefficient.

Using (5), \(u_n\ge1\), and \(z\le1\),
\[
 (1+M)(1+2\beta^{14L}z)
 \le(1+\beta^{22L}zu_n)(1+2\beta^{14L}z)
 \le1+\beta^{38L}zu_n.                              \tag{21}
\]
To check the last inequality, expand the product; its three added terms
have total coefficient at most
\(\beta^{22L}+2\beta^{14L}+2\beta^{36L}\) times \(zu_n\).
That coefficient is at most \(\beta^{38L}\). This ordinary polynomial
enlargement still keeps the actual label factor.

Equations (18)--(21) are a uniform envelope on the existing stability
range. They do not assert gap-independent raw dynamical amplification for
arbitrary labels. The genuine energy improvement in (14)--(16) is needed:
the earlier exponent contained an additional unbounded inverse-gap factor,
which (19) would not control by a fixed activation-only convexity range.

## 7. Gaussian concentration and completion of the bound

Let \(\mathsf G\) be the standard Gaussian vector of initialized
\((A_0,\sqrt nW_0^{(2)},\ldots,\sqrt nW_0^{(L)})\) blocks.
In normalized Hilbert coordinates, with both readouts zero initially,
\[
 d_\theta(0)=\|\mathsf G-\mathsf G'\|_2/\sqrt n.
\]
Equation (18) is a global pairwise bound between any two points of the
actual good set. Hence each scalar prediction there has Lipschitz constant
\[
 \mathcal L_n={\sqrt{L+1}\,Y C_Y\over\sqrt n}e^{E_{\mathrm{en}}}.
\]
Use its scalar McShane extension, truncated to the physical amplitude
interval \([-2HR,2HR]\). Two independent copies of the identical
extension have mean-zero difference and product-Gaussian Lipschitz
constant \(\sqrt2\mathcal L_n\). Therefore their two-sided tail
at level \(a\) is at most
\(2e^{-a^2/(4\mathcal L_n^2)}\). This uses neither conditional
Gaussian concentration nor differentiating an event indicator.

The existing physical-time and sphere moduli remain unchanged. With
\(v_t=1-e^{-\kappa t}\), their coefficients are
\[
 K_t={8(H^2+FY^2/g)Y\over\kappa},\qquad
 K_x=RT^L,\qquad
 F=s^2\left[T^{2L-2}+4H^2\sum_{j=0}^{L-2}T^{2j}\right].
\]
The time grid has \(n+1\) points, including \(v_t=1\), and a sphere
\(1/n\)-net has size at most \((1+2n)^d\). Put
\(N_n=(n+1)(1+2n)^d\). The same Gaussian union and two off-grid
moduli give
\[
 \|f_n-f_n'\|_*
 \le2\mathcal L_n\sqrt{\log(4N_n/\delta)}
                            +{2(K_t+K_x)\over n}.    \tag{22}
\]
The two good-path failures cost at most \(\delta/2\), by taking
\(n\ge N_{\rm fit}(\delta/8)\) and then meeting the source's
eventual failure bound \(\delta/8\) per path. The Gaussian union costs
the other \(\delta/2\). This is the same confidence allocation as in
the earlier explicit comparison, without any additional event.

Using (18)--(21) and \(2\sqrt{L+1}\le\beta^{2L}\),
\[
 2\mathcal L_n
 \le{\beta^{23L}Yh^2\over\sqrt n}
 (1+\beta^{38L}zu_n)
           [1+\beta^{36L}z^2(e^{u_n}-1)].             \tag{23}
\]
The earlier explicit fitting envelope has
\(F\le\beta^{7L}\) and \(FY^2/g\le1\), so
\[
 2(K_t+K_x)\le\beta^{5L}hY.
\]
Since every bracket in (23) and the square-root logarithm in (22) is
at least one, and \(n^{-1}\le n^{-1/2}\), the tail can be absorbed
by increasing the leading coefficient to \(\beta^{24L}\).
Finally
\(\beta^{24L},\beta^{38L},\beta^{36L}\le B=\beta^{100L}\),
and replacing \(4N_n\) by \(8N_n\) only enlarges the bound. This
proves (3).

Physical fitting supplies convergence of both parameter trajectories.
Their compact-sphere forward maps are continuous, so the same bound
passes to the endpoint. The clock used for the grid is a proof coordinate,
not a rescaling or synchronization of the training dynamics.

## 8. Evidence and exact claim boundary

Newly derived here: the exact carrier-anchored remainder (10), the
finite-network energy inequality (14), the improved amplification (16),
the use of the readout estimate after energy rather than inside Gronwall,
and the actual-label convexity envelope (20)--(23).

Inherited and explicitly matched: the fitting event and physical moduli
from `GENERAL_EXPLICIT_FITTING.md`; the endpoint gradient/subtraction
constants and Gaussian good-set construction in
`GENERAL_DENSE_COMPARISON.md`; the numerical ledger in
`SIMPLE_CONSTANTS_DENSE_CHECK.md`; and the actual source maximum and its
power envelope in `UNBOUNDED_COMPRESSOR_BRIDGE.md` and
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`. The latter envelope report was read
completely in this continuation. Earlier complete reads of the fitting
and dense comparison sources were reused. No old-study source was fetched
in this continuation, and no experiment was run.

The result removes inverse-gap factors from the displayed exponential,
retaining actual label dependence in a polynomial prefactor. It remains
a near-root independent-dense comparison on the same physical-time,
whole-sphere, fitted-endpoint topology. Strict root-width concentration
and an explicit stochastic source threshold remain open.
