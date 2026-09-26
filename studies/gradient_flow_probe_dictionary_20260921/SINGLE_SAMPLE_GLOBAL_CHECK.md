# Independent check of the zero-readout single-sample global certificate

Assignment: audit the frozen `SINGLE_SAMPLE_GLOBAL_BOUND.md` candidate, including constants, population regularity, actual ridge lifting, the radial positivity argument, physical clocks, and passive inputs. Scientific inputs were that candidate, the previously authorized five current-study derivation/specification files, and this reviewer's earlier scoped canonical-model read. No other agent's findings, other studies, new scientific sources, or experiments were used. This is an internal mathematical check, not an independent promotion review.

Final checked candidate SHA-256: `f16e11b19ebef54a1e7dfadf5e0a948e520353513835b892f4048ceaedd37c0d`. This includes the final added defect-finiteness/continuity paragraph, inspected after the complete audit; it changes no hypothesis or estimate used below.

**Verdict: PASS under the candidate's explicit hypotheses.** No mathematical correction is required. The proof establishes the displayed global defect certificate for zero initial readout and positive initial upper-feature energies. It does not establish decay of the defect with dictionary order, a nonzero-readout finite-width transfer, or a width/time interchange. Those boundaries are stated correctly.

## Metric, initialization, and regularity

The candidate uses half squared loss and canonical block mobilities. In feature time its full middle update is `sigma delta h^T/n` at finite width, whose Frobenius norm is `||delta||_n ||h||_n`. The finite first/readout mobilities give exactly the stated first-row/readout equations. Normalized finite vector norms and ordinary matrix Frobenius norms are therefore consistent.

For the actual frozen coefficient model, the coefficient derivative is

\[
 M_s=\sigma(B_2^T\delta_p/n)(B_1^Th_p/n)^T.
\]

Lifting gives `Kp_s=sigma (Q2 delta_p) tensor (Q1 h_p)`. No inverse Gram or orthogonal projector belongs in this update. The initialization `Bp=Q2 W0 Q1` is also exact. Positivity and contraction of both `Q_l` hold for positive scalar ridge, independently of whether the raw tables have dependent columns. Consequently `||Bp||<=A`, and the operator/increment bounds in (5) are valid.

The coordinate transform is correct:

\[
 F(z)=z/2+\sinh(2z)/4,\quad F'(z)=\cosh^2z,
 \quad (F^{-1})'(X)=\operatorname{sech}^2(F^{-1}X)\le1.
\]

The derivative of `tanh(F^{-1}X)` is the square of this last gate, also at most one. Thus both maps are globally Lipschitz on the required `L2` spaces. For a Gaussian initial scalar `g`, `F(g)` belongs to `L2`: its square is bounded by a constant times `g^2+exp(4g)+exp(-4g)`, each of finite Gaussian expectation.

The contraction argument has the needed completeness and invariance properties. On continuous `L2/HS` curves, the condition `|c(s)|<=s` is closed; the integral readout update preserves it. The same updates preserve `||K(s)||HS<=s^2/2` and the corresponding integrated `X` bound. Forward fields are Lipschitz on these sets; the only otherwise problematic gate difference is controlled by the common pointwise readout bound:

\[
 \|cD(z)-\widetilde cD(\widetilde z)\|_2
 \le\|c-\widetilde c\|_2+2S\|z-\widetilde z\|_2.
\]

The bound uses `|tanh''|<=2`, which is valid. Bounded-operator actions and HS perturbations then give a finite Lipschitz constant on every finite feature interval, permitting finitely many contraction steps. Positive ridge can produce unbounded pointwise dictionary fields, but only the bounded `L2` operators `Q_l` occur in these estimates; a pointwise bound on dictionary fields is unnecessary.

The scalar chain rules require no global Frechet smoothness of tanh on `L2`. A `C1(L2)` curve has a first-order expansion along one fixed `L2` direction; bounded continuous scalar derivatives and dominated difference quotients prove the chain rule along that curve. This gives continuous `L2` derivatives of `g,h,z,H`, hence `c` is `C2(L2)`. Conversely, a raw integral solution has a pointwise absolutely continuous representative; the identity `F'(g)g_s=sigma alpha W*delta` shows that its transformed increment is `L2`. Thus the transform does not discard raw competitors or introduce a separate uniqueness class.

## Positive radial acceleration and the training clock

For the full model,

\[
 z_s=\sigma\{\|h\|_2^2 I+\alpha W E^2W^*\}\delta,
\quad c_s=\sigma H,
\]

so the two signs cancel in the second derivative:

\[
 c_{ss}=D\{\|h\|_2^2 I+\alpha WE^2W^*\}Dc.
\]

The first summand is positive and
`<v,WE^2W*v>=||E W*v||_2^2`. For the closure, replacing the first summand by
`<h_p,Q1 h_p> Q2` preserves positivity because both factors are nonnegative in the required scalar/operator senses. This independently verifies the exact PSD operators in the candidate.

For `R=||c||_2>0`, differentiation yields

\[
 R''=\frac{\|c_s\|_2^2-(R')^2+\langle c,c_{ss}\rangle}{R}\ge0.
\]

Cauchy--Schwarz controls the first two terms, and the PSD identity controls the last. The expansion `c(s)=sigma s H0+o_L2(s)` gives `R'(0+)=||H0||_2`. On the connected interval where `R>0`, convexity gives `R(s)>=s||H0||_2`, so that interval cannot end by returning to zero. Therefore the radial conclusion extends to every finite feature time. It gives both
`||H||_2>=R'>=sqrt(q0)` and `sigma f=R R'>=q0 s`. The identical proof applies to the ridge closure with `q0p`.

Direct prediction differentiation gives the candidate's (7). The filtered middle term is the nonnegative product
`<delta_p,Q2 delta_p><h_p,Q1 h_p>`, not the unfiltered squared rank-one norm. The readout term alone is at least `q0p`. On `[0,S]`, all three terms sum to at most

\[
 J=1+S^2+M^2S^2.
\]

Thus each signed feature prediction is strictly increasing from zero and reaches `Y` by `Y/q0` or `Y/q0p`. The clocks remain below these roots at finite physical time since their deficits solve `r_t=-K(s(t))r` with `q0<=K<=J` (or the closure analogue). In particular, the lower bounds required for global fitting are proved, rather than assumed along the unknown trajectories. If `q0p=0`, then `H0p=c0p=delta0p=0`; every feature velocity is zero and uniqueness makes the closure stationary, as stated.

## Defect arithmetic and passive inputs

Set `eX=||X-Xp||_2`, `eK=||K-Kp||HS`, `ec=||c-cp||_2`, and write `a,b,d` for the three defects. The candidate's individual upper bounds are correct. Summing them gives exactly these coefficients:

| Term | Coefficient in the summed differential bound |
|---|---:|
| `eX` | `2SM^2+2SM+S+M` |
| `eK` | `2SM+3S+1` |
| `ec` | `M+1` |
| `a` | `2SM+2S+1` |
| `b` | `1` |
| `d` | `1` |

Each is bounded by `L=2+2M+4S+8SM+4SM^2` for nonnegative `M,S`. Since both trained increments and readouts start at zero and the first rows agree, `e(0)=0` is correct; the different initialized actions enter only through `a,b`. Integrating `e'<=Le+L epsilon_p` gives precisely `(exp(LS)-1)epsilon_p`, with no omitted factor of `L`.

The output bound is
`ec+S(M eX+eK+a)<=C e+S a`, using `C=1+S(M+1)`. Thus the candidate's same-feature-time error `E_p` is valid.

The input-ball extension uses a property specific to single-sample training: every first-row update is proportional to `x`, so both systems have the same fixed perpendicular part. Therefore

\[
 (W^1-W^1_p)u=\frac{x\cdot u}{r^2}(g-g_p),
 \qquad\left|\frac{x\cdot u}{r^2}\right|\le1
 \quad(\|u\|\le r).
\]

This proves the same feature error estimates uniformly over the declared ball. The closure prediction speed at any passive `u` has three bounds: readout contribution at most `1`, middle contribution at most `s^2`, and first-row contribution at most `M^2s^2`, because `|x.u|<=r^2<=1`. Their sum is at most `J`; no test-label or test-backward defect is missing.

The defect itself is finite under these hypotheses. In fixed finite input dimension, the closed input ball is compact, the first rows are `L2`, and tanh is Lipschitz, so the fields are jointly continuous in time/input in `L2`. Boundedness of `W0-Bp` gives finite continuous suprema. A crude check, independent of order quality, is

\[
 a\le2A,\qquad b\le2AS,\qquad d\le2S,
 \qquad\epsilon_p\le2A(1+S)+2S.
\]

This is only a finiteness check and supplies no order decay.

## Uniform physical-time comparison and scope

For `d_clock=s-s_p`, subtracting the two scalar clocks and applying the full signed feature prediction's derivative lower bound gives

\[
 (|d_{clock}|)'\le-\kappa|d_{clock}|+E_p,
 \qquad |d_{clock}(t)|\le E_p/\kappa.
\]

The argument compares `F_train(s)` and `F_train(s_p)` within the same full feature curve; the remaining difference at `s_p` is exactly bounded by the same-feature-time certificate. Both clocks lie in `[0,S]`, so every used estimate applies. Combining this contraction with the passive speed bound gives `(1+J/kappa)E_p` uniformly for all physical times. No growing factor involving physical time is introduced.

The training-output minimum with `Y` is valid because both signed predictions stay in `[0,Y]`. The same minimum is not asserted for arbitrary test inputs. Label zero is stationary because readout and all hidden velocities start at zero; this case was separated correctly. The restriction `r>0` makes the first-row comparison division legitimate, while `r<=1` justifies the chosen constants.

The certificate is specific to exact zero readout. The earlier finite initialization mismatch remains relevant to the executed random-readout runs and to exact jet claims; it does not contradict this conditional zero-readout global estimate. Likewise this certificate strengthens the earlier audit's explicitly unresolved zero-readout fitting statement: fitting now follows from the newly proved radial lemma under `q0,q0p>0`. The absence of an explicit bound decreasing with derivative order remains unresolved.
