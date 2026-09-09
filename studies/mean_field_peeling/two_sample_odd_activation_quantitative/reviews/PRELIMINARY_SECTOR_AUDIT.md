# Independent sample-sector and active-inverse audit

This note is a theory audit of the affine chronological source map in the odd two-input problem. It does not by itself prove nonlinear cap removal or a finite GF/GD theorem. It uses the exact source rules in `SOURCE_AND_LIMIT_BRIDGE.md`, the controlled-response source, and the normalized raw affine equations of `/tmp/sharpen_affine.md`.

## 1. Exact affine sample sectors

After label folding, the controls are `(1/2,1/2)`. Let

\[
 P_+=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
 P_-=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \quad r=\sqrt{v_u},\quad v_v=1-v_u.
\]

Use `J_{kj}=h_j 1_{j<k}` for causal integration. The first-layer direct derivative operator is

\[
 K_1=a^2J(v_uP_++v_vP_-).
\]

The top derivative operator, when its output includes the factor `a` in `delta3=aC`, is `K3=a² J P+`.

At the affine base every `A` block commutes with sample exchange. Both `B` arrays are active only:

\[
 B^2=B^2_+P_+,\qquad B^3=B^3_+P_+.
\]

For `B3`, the formal derivative output of `aC` has identical output rows; the top readout control and exchange symmetry give identical columns. The learned delta covariance has the same form. For `B2`, its derivative contribution is `a B3 U`; its learned covariance again has identical sample entries. This reasoning concerns formal derivative slots as distinct slots, including at singular reverse covariance; it does not identify formal slots merely because their actual Gaussian values coincide.

Put

\[
 F=(I-K_1B^2)^{-1}K_1,\quad
 R=(I-a^2A^2B^3)^{-1},\quad L=(I-a^2B^3A^2)^{-1},
\]
\[
 V=a^2RA^2,\quad T=K_3(I-A^3K_3)^{-1},\quad W=a^2B^3R.
\]

All except `T,W` are sample diagonal; `T,W` are active only. The frozen inactive covariance gives exactly

\[
 F_-=a^2v_vJ,\quad A^2_-=2a^2v_vJ,\quad A^3_-=3a^4v_vJ,
 \quad V_-=2a^4v_vJ,\quad R_-=L_-=I.
\]

The factors two and three matter: the formal inactive source coefficients do not vanish even though the actual affine backward fields are active only.

## 2. No inactive feedback instability in the linearized map

For arbitrary causal perturbations, the affine coefficient linearization is

\[
 X_2=FY_2F+E_2,\quad
 X_3=a^2RX_2L+VY_3V+E_3,
\]
\[
 Y_3=TX_3T+H_3,\quad
 Y_2=a^2LY_3R+WX_2W+H_2.
\]

Write `X_{στ}=Pσ X Pτ`. Whenever `(σ,τ) != (+,+)`,

\[
 Y_{3,\sigma\tau}=H_{3,\sigma\tau},\qquad
 Y_{2,\sigma\tau}=a^2L_\sigma H_{3,\sigma\tau}R_\tau+H_{2,\sigma\tau}.
\]

Then `X2` and `X3` follow by direct substitution. Thus every non-active-active sector is acyclic. In particular no arbitrary forcing can create an independent inactive-sector feedback rate of order one acting over original time `S~1/r` at this linearization.

For the inactive-inactive sector one obtains the explicit formulas

\[
 Y_{3,--}=H_{3,--},\quad Y_{2,--}=a^2H_{3,--}+H_{2,--},
\]
\[
 X_{2,--}=E_{2,--}+a^4v_v^2JH_{2,--}J+a^6v_v^2JH_{3,--}J,
\]
\[
 X_{3,--}=a^2E_{2,--}+E_{3,--}
 +a^6v_v^2JH_{2,--}J+5a^8v_v^2JH_{3,--}J.
\]

The actual exchange-invariant nonlinear coefficient perturbations are sample diagonal, so their off-diagonal sectors vanish. This is additional structure, not needed for the acyclic conclusion.

## 3. Exact active normalization

With normalized time `t=a³r s`, rescale the active coefficient matrices by

\[
 A^2_+=(r/a)\bar A^2,\quad A^3_+=ar\bar A^3,\quad
 B^2_+=(a/r)\bar B^2,\quad B^3_+=(ar)^{-1}\bar B^3.
\]

All feedback products then lose both `a` and `r`. The direct kernels become `J_t`. The four learned moment density kernels become, respectively,

\[
 \langle p_k,p_j\rangle,\quad
 \langle A_kp_k,A_jp_j\rangle,\quad
 \langle B_k^*C_k,B_j^*C_j\rangle,\quad
 \langle C_k,C_j\rangle.
\]

The normalized active map is consequently the one-sample gain-one map

\[
 A_2=F+M_2,\quad A_3=V+M_3,\quad
 B_3=T+N_3,\quad B_2=W+N_2.
\]

The raw normalized path is universal in `r`; only its terminal level tends to infinity. Normalization alone therefore leaves an active inverse estimate to prove.

## 4. A smoothing identity for arbitrary backward row forcing

The positive-scaling proposal directly dominates strict forcing bounded by a constant times `h_j`. It does not directly dominate a backward forcing known only to have bounded time-row sum. This apparent mesh issue can be removed algebraically, including for current diagonal forcing.

Define

\[
 \widetilde Y_3=Y_3-H_3,\qquad
 \widetilde Y_2=Y_2-a^2LH_3R-H_2.
\]

The same homogeneous coupled map holds for `(X2,X3,Ytilde3,Ytilde2)`, now with zero backward forcing and forward forcing

\[
 \widetilde E_2=E_2+FH_2F+a^2FLH_3RF,
 \qquad \widetilde E_3=E_3+VH_3V.
\]

If strict kernels `A,B` satisfy `|A_kr|<=P_A h_r` and `|B_vj|<=P_B h_j`, and `sup_r sum_v |H_rv|<=epsilon`, then

\[
 |(AHB)_{kj}|\le P_AP_B S\epsilon h_j.
\]

Indeed bound the right kernel by `P_B h_j`, sum `H` over its row, and finally sum `P_A h_r` over `r`. There is no division by a mesh size. The identity works when `H` has current blocks.

Polynomial strict density bounds on `F,V,FL,RF` thus turn arbitrary backward row forcing into forward density forcing. To obtain the needed bounds on `L,R`, use the exact identities

\[
 R=I+VB^3,\qquad L=I+WA^2.
\]

Thus polynomial affine density bounds for `A2,B3,F,V,W` give polynomial row and density bounds for all required products. Single-time Gaussian answer probes supply these affine density bounds, provided their raw comparison uses the integrated affine Hessian bound. At the affine base there are no current backward returns.

## 5. Positive scaling of the active initialized Gaussian variables

In the normalized active problem, scale all independent initialized Gaussian variables `p0,A0,B0` by `beta>0`, keeping `C0=0`. At each fixed positive Euler mesh, every raw coordinate is a polynomial with nonnegative coefficients in these Gaussian variables. This follows inductively from

\[
 p'=A^*B^*C,\quad A'=B^*C\otimes p,\quad
 B'=C\otimes Ap,\quad C'=BAp.
\]

All normalization and positive step factors are nonnegative. Every learned moment is therefore a polynomial in `beta` with nonnegative coefficients: expand the product and use independence of the centered Gaussian entries, whose monomial expectations are either zero or nonnegative. The same assertion holds for the population fixed-program limit, since a fixed finite polynomial has finitely many Wick terms.

The initialized matrix variance is now `beta²`. The source coefficient rules become exactly

\[
 A_2^\beta=\beta^2F(A^\beta,B^\beta)+M_2^\beta,
\quad A_3^\beta=\beta^2V(A^\beta,B^\beta)+M_3^\beta,
\]
\[
 B_3^\beta=\beta^2T(A^\beta,B^\beta)+N_3^\beta,
\quad B_2^\beta=\beta^2W(A^\beta,B^\beta)+N_2^\beta.
\]

The direct time kernels `K1=K3=J` do not acquire an additional factor `beta²`: they arise from the raw update metric and readout update, rather than from Gaussian adjunction. Scaling the first root changes its learned covariances, not its raw update metric.

Causal substitution shows that these coefficient arrays are also polynomials with nonnegative coefficients in `beta`. There is no covariance inverse in this argument; each time-causal inverse is a finite nilpotent series at a fixed mesh.

Differentiation at `beta=1` gives precisely the active Jacobian system above with forcing

\[
 E_2=2F+M_2',\ E_3=2V+M_3',\
 H_3=2T+N_3',\ H_2=2W+N_2'.
\]

Every forcing is nonnegative, and all four dominate `2J`, because `F,V,T,W>=J` entrywise. The active Jacobian is a nonnegative causal map. Its inverse is nonnegative by finite chronological substitution. Consequently its solution for arbitrary signed strict density forcing is dominated by a scalar multiple of the scaling derivative. Section 4 extends this to the existing mixed norm with arbitrary backward row forcing.

For a polynomial `f(beta)=sum_n c_n beta^n` with `c_n>=0`,

\[
 f'(1)\le \frac{f(\beta)}{\beta-1}\qquad(\beta>1),
\]

since `n(beta-1)<=beta^n` for every nonnegative integer `n`. Hence a polynomial coefficient bound at one enlarged initialization scale yields a polynomial active inverse bound.

## 6. How the raw affine estimate can supply the enlarged-scale bound

Homogeneity gives the exact continuous and discrete scaling identities

\[
 \Theta_\beta(t)=\beta\Theta_1(\beta^2t),\qquad
 \Theta_{\beta,k}(h)=\beta\Theta_{1,k}(\beta^2h).
\]

If the terminal affine radius is `R*=sqrt(200+M²)`, choose `beta-1=c/R*²` with a sufficiently small absolute `c`. The cubic raw vector field extends the path for an additional normalized time of order `R*^{-2}`, remaining within a fixed multiple of `R*`. The extra integrated Hessian is `O(1)`. The existing logarithmic integrated-Hessian bound is therefore preserved up to an absolute additive constant.

For sufficiently fine Euler meshes, the same integrated comparison and bound hold with slack. Insert one independent Gaussian answer probe, use raw variation of constants, and extract its Gaussian linear coefficient as in the original source proof. A perturbation confined to one time has its raw update multiplied by that time's step. This yields polynomial coefficient density bounds at `beta`, not merely a row-sum bound. The factor `(beta-1)^{-1}=O(R*²)` in Section 5 is polynomial.

This establishes a concrete route from raw tangent control to the active source inverse. It is more than an unsupported identification of the two objects: the intermediary is a positive Gaussian-initialization scaling derivative, and the arbitrary backward forcing is handled by the exact smoothing identity.

## 7. Conditions still needed for the nonlinear closure

The scaling argument proves the affine inverse estimate once the enlarged-scale single-probe bounds and fine-mesh slack are recorded with uniform constants. To complete a polynomial nonlinear source theorem, a separate closure must still establish:

1. Polynomial subGaussian bounds for source fields on a sufficiently small coefficient neighborhood, using the exact affine resolvents and absorption of the `e` gate perturbations.
2. Derivative bounds via variation of constants through those resolvents. The useful envelope has form `P exp(e P sum h Q)` with the current factor `P(1+eQ_k)` retained. Reusing an envelope `exp(P S)` would lose polynomiality.
3. Polynomial estimates for the response-map quadratic remainder and for the nonlinear gate/moment forcing.
4. Fixed-mesh, fixed-cap continuity in the activation amplitude, including singular source covariances, to close `D <= P(e+D²)` by a small-amplitude homotopy.

The older source construction provides fixed-program continuity without covariance inverses; its rough exponential constants need replacement in the first three items. Nothing in the sector or positive-scaling audit alone certifies the complete population/GF/GD theorem.
