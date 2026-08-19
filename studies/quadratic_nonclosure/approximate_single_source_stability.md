# Global stability of an approximate one-source closure

> **Corrected scope.**  The stability implications below are exact under
> their displayed small-defect and target-entry hypotheses.  The current
> quadratic compiler supplies formal annealed fixed-order coefficients, not
> concentration of the random derivatives or a positive-time mean-field
> trajectory.  Any sentence below using a deterministic typical coefficient
> requires that separate bridge.

## Two-hidden-layer quadratic \(\mu\)P network with squared loss and label \(1\)

### Executive conclusion

There is a genuine positive stability result, even though the earlier
prescribed Wick--Taylor finite-closure conjecture fails.

For squared loss, the full feature dynamics are the readout-gradient-ascent dynamics run with the clock

\[
d\tau=2(1-f)\,dt.
\]

On every target-fitting trajectory, physical time \(t\) is infinite but the total feature time \(\tau\) is finite. Therefore a closure error that respects the common residual factor \(1-f\) has only a finite amount of effective time in which to accumulate. At the same time, the loss satisfies a uniformly contracting scalar equation once the output has become positive.

This yields two constructive results.

1. Any finite model whose induced tangent-kernel error is at most \(\delta\) has a uniform-in-time loss error of order \(\delta\), rather than order \(\delta t\).
2. There is an explicit one-field, one-source PDE whose degree-\(M\) polynomial restriction uses only \(M+1\) response coefficients. Those coefficients are computable by the finite derivative/Wick calculus. Its global loss error is controlled by the approximation error of the readout-ascent orbit on one finite feature-time interval.

This is an observable-stability theorem, not a full hidden-state contraction theorem. The parameter dynamics have neutral directions at the target, and a small residual in arbitrary hidden equations does not automatically imply a small tangent-kernel error.

---

## 1. Network and exact squared-loss identities

For one fixed input, suppress the input from the notation and write

\[
h_i^{(1)}=\frac12\left(z_i^{(1)}\right)^2,
\]

\[
z_j^{(2)}=\sum_iW_{ji}^{(2)}h_i^{(1)},
\qquad
h_j^{(2)}=\frac12\left(z_j^{(2)}\right)^2,
\]

\[
f_n=\frac1n\sum_ja_jh_j^{(2)},
\qquad
\mathcal L_n=(f_n-1)^2.
\]

Here (a_j) is the rescaled readout coordinate; the corresponding raw
forward weight is (a_j/n).

The \(\mu\)P metric used throughout the project is

\[
\dot z^{(1)}=-n\nabla_{z^{(1)}}\mathcal L_n,
\qquad
\dot W^{(2)}=-\nabla_{W^{(2)}}\mathcal L_n,
\qquad
\dot a=-n\nabla_a\mathcal L_n.
\]

Define the tangent kernel

\[
\kappa_n
=
n\left\|\nabla_{z^{(1)}}f_n\right\|^2
+\left\|\nabla_{W^{(2)}}f_n\right\|_F^2
+n\left\|\nabla_af_n\right\|^2.
\]

It is a sum of squares, hence \(\kappa_n\ge0\). Direct differentiation gives

\[
\dot f_n=2(1-f_n)\kappa_n,
\qquad
\dot{\mathcal L}_n=-4\kappa_n\mathcal L_n.
\tag{1}
\]

Thus, with \(r_n=1-f_n\),

\[
r_n(t)=r_n(0)
\exp\!\left(-2\int_0^t\kappa_n(s)\,ds\right),
\]

\[
\mathcal L_n(t)=\mathcal L_n(0)
\exp\!\left(-4\int_0^t\kappa_n(s)\,ds\right).
\tag{2}
\]

Equation (1) is exact, but it is not an exact scalar closure: \(\kappa_n\) contains the noncommutative matrix-message hierarchy found in the earlier analysis.

---

## 2. The steelman approximate-closure statement

An approximate closure theorem should not require the finite model to preserve
every individual derivative/Wick continuation.  The conditional
continuation-capacity argument targets that stronger requirement under its
bounded-filtration, freeness/faithfulness, and branch-separation hypotheses.
The approximate theorem should require only what is necessary to predict the
chosen observable.

The meaningful statement is the following.

> **Residual-compatible observable-closure conjecture.** For every required accuracy \(\varepsilon>0\), there is a truncation order \(M(\varepsilon)<\infty\), independent of width and physical time, and a finite one-source model constructed from finitely many local derivative/Wick rules such that:
>
> 1. its loss equation retains the exact residual factor \(1-f\);
> 2. its induced readout-ascent orbit, or equivalently its tangent-kernel profile, differs from the true one by a defect \(\delta_M\) on the finite target-reaching feature interval;
> 3. \(\delta_M\to0\) as \(M\to\infty\);
> 4. the resulting loss prediction obeys
>    \[
>    \sup_{t\ge0}|\mathcal L_M(t)-\mathcal L(t)|\le C\delta_M,
>    \]
>    where \(C\) is independent of physical time and width.

The stability implication in item 4 is proved below, with explicit constants. A concrete one-source truncation is also constructed. The remaining model-specific approximation question is whether a chosen Wick/message truncation satisfies \(\delta_M\to0\) uniformly in width. Fixed-order Wick power counting alone does not prove that tail statement.

The dependence of \(M\) on accuracy is essential. Under the hypotheses of the
conditional noncommutative continuation-capacity argument, a single fixed
bounded-filtration commuting-source \(M\) cannot preserve all exact branchwise
continuations. For every fixed accuracy, however, \(M\) is still \(O(1)\)
with respect to width and training time.

---

## 3. The network supplies its own coercivity in the fitting basin

The stability constant is not an external convexity assumption. Once the output is positive, it follows from the trained linear readout.

Set

\[
C_n(t)=\frac1n\left\|a(t)\right\|^2.
\]

The readout-layer part of \(\kappa_n\) is

\[
n\left\|\nabla_af_n\right\|^2
=\frac1{4n}\sum_j\left(z_j^{(2)}\right)^4.
\]

Cauchy--Schwarz therefore gives

\[
f_n^2
\le
C_n\left(\frac1{4n}\sum_j\left(z_j^{(2)}\right)^4\right)
\le C_n\kappa_n.
\tag{3}
\]

The output-weight norm satisfies the exact identity

\[
\dot C_n=4f_n(1-f_n).
\tag{4}
\]

Assume that at some time \(t_*\),

\[
f_n(t_*)=a\in(0,1).
\]

While \(0<f_n<1\), equations (1), (3), and (4) give

\[
\frac d{dt}\frac{C_n}{f_n^2}
=
\frac{4(1-f_n)}{f_n}
\left(1-\frac{C_n\kappa_n}{f_n^2}\right)
\le0.
\]

Consequently, for every \(t\ge t_*\),

\[
\kappa_n(t)
\ge\frac{f_n(t)^2}{C_n(t)}
\ge
\lambda_n,
\qquad
\lambda_n:=\frac{a^2}{C_n(t_*)}>0.
\tag{5}
\]

It follows immediately that

\[
1-f_n(t)
\le
(1-a)e^{-2\lambda_n(t-t_*)},
\]

\[
\mathcal L_n(t)
\le
(1-a)^2e^{-4\lambda_n(t-t_*)}.
\tag{6}
\]

This proves target fitting and exponential attraction after positive entry. It also bounds all parameter groups. Indeed, the exact balance laws are

\[
\frac d{dt}\frac{\|z^{(1)}\|^2}{4n}
=
\frac d{dt}\frac{\|W^{(2)}\|_F^2}{2}
=
\dot C_n,
\]

and (6) makes \(\int_{t_*}^{\infty}\dot C_n\,dt\) finite.

If \(f_n(0)=0\) and \(\kappa_n(0)>0\), then \(f_n(t)>0\) immediately and the argument applies after any small positive time. At the centered Gaussian mean-field initialization used previously,

\[
f_n(0)\xrightarrow{\mathbb P}0,
\qquad
\kappa_n(0)\xrightarrow{\mathbb P}\frac{17}{6}
\]

for \(\gamma=4/3\). A width-uniform version of (5) therefore reduces to a short-time moment/regularity estimate ensuring that \(\kappa_n\) stays bounded below during a fixed small burn-in interval.

The positive-entry qualification is necessary. There are finite-width negative-output initial states in an open dead-feature basin for which \(f_n(t)\to0^-\) and \(\kappa_n(t)\to0\). No uniform global contraction theorem can include those trajectories.

---

## 4. Exact feature time: why infinite physical time has finite error budget

Let \(\Theta(\tau)\) follow \(\mu\)P gradient ascent on the readout itself:

\[
\frac{dz^{(1)}}{d\tau}=n\nabla_{z^{(1)}}f_n,
\qquad
\frac{dW^{(2)}}{d\tau}=\nabla_{W^{(2)}}f_n,
\qquad
\frac{da}{d\tau}=n\nabla_af_n.
\]

Write

\[
F_n(\tau)=f_n(\Theta(\tau)).
\]

Then

\[
F_n'(\tau)=\kappa_n(\Theta(\tau))\ge0.
\tag{7}
\]

Squared-loss flow follows exactly the same parameter-space orbit:

\[
\theta_n(t)=\Theta(\tau_n(t)),
\qquad
\dot\tau_n=2\bigl(1-F_n(\tau_n)\bigr).
\tag{8}
\]

Let \(\tau_*\) be the first feature time for which \(F_n(\tau_*)=1\). From (5), after positive entry \(F_n'\ge\lambda_n\), so \(\tau_*<\infty\). In particular,

\[
\int_{t_*}^{\infty}2(1-f_n(t))\,dt
=
\tau_* - \tau_n(t_*)
\le
\frac{1-a}{\lambda_n}.
\tag{9}
\]

Suppose a hierarchy truncation makes a feature-vector-field error \(R_M\), but preserves the squared-loss multiplier. In physical time the omitted vector field is

\[
2(1-f_n(t))R_M(t).
\]

Equation (9) gives the exact identity

\[
\int_{t_*}^{\infty}
2(1-f_n(t))\|R_M(t)\|\,dt
=
\int_{\tau_n(t_*)}^{\tau_*}
\|R_M(\tau)\|\,d\tau.
\tag{10}
\]

Thus a persistent bounded error is integrated over a finite feature-time interval, not over infinite physical time. This is the main stability mechanism.

---

## 5. A constructive one-field, one-source PDE

Define

\[
U_n(t,s)=F_n(\tau_n(t)+s).
\]

It obeys the exact transport equation

\[
\partial_tU_n(t,s)
=
2\bigl(1-U_n(t,0)\bigr)\partial_sU_n(t,s),
\qquad
f_n(t)=U_n(t,0).
\tag{11}
\]

The exact initial function \(U_n(0,s)=F_n(s)\) contains the complete future readout-ascent orbit, so using it without restriction would be an oracle encoding, not a closure.

The non-oracular finite approximation retains only the first \(M+1\) response coefficients

\[
h_{k,n}=F_n^{(k)}(0)=D_{+,n}^k f_n(\theta_n(0)),
\qquad k=0,\ldots,M,
\]

where \(D_{+,n}\) is one finite-width readout-ascent derivative. For every
fixed \(M\), the derivative grammar gives the exact random polynomials
\(h_{0,n},\ldots,h_{M,n}\). Wick contraction evaluates their expectations;
only the subsequent fixed-order large-width limit gives deterministic
annealed coefficients. The number of diagrams can grow rapidly with \(M\),
but it is finite at every fixed order. No concentration claim is implicit
here.

Set

\[
F_{M,n}(s)=\sum_{k=0}^M h_{k,n}\frac{s^k}{k!}
\]

and solve the same one-source PDE with this polynomial initial datum:

\[
\partial_tU_{M,n}
=
2\bigl(1-U_{M,n}(t,0)\bigr)\partial_sU_{M,n},
\qquad
U_{M,n}(0,s)=F_{M,n}(s).
\tag{12}
\]

The space of degree-\(M\) polynomials in \(s\) is invariant under (12). If

\[
u_k(t)=\left.\partial_s^kU_{M,n}(t,s)\right|_{s=0},
\]

then (12) is exactly the \(M+1\)-state system

\[
\dot u_k=2(1-u_0)u_{k+1},
\quad k=0,\ldots,M-1,
\qquad
\dot u_M=0,
\tag{13}
\]

initialized by \(u_k(0)=h_{k,n}\). Its predictions are

\[
f_{M,n}(t)=u_0(t),
\qquad
\mathcal L_{M,n}(t)=(1-u_0(t))^2.
\]

The corresponding exact infinite source jet satisfies

\[
\dot u_k=2(1-u_0)u_{k+1},
\qquad k\ge0.
\tag{14}
\]

Thus the only zero-closure defect is the omitted \(u_{M+1}\) flux in the top retained equation. It is multiplied by \(1-u_0\), and therefore vanishes at the target.

In feature time the approximation is simply the Taylor polynomial of \(F_n\). Its exact error is

\[
F_n(\tau)-F_{M,n}(\tau)
=
\int_0^\tau
\frac{(\tau-\sigma)^M}{M!}
F_n^{(M+1)}(\sigma)\,d\sigma.
\tag{15}
\]

Consequently, on \(0\le\tau\le T\),

\[
\|F_n-F_{M,n}\|_\infty
\le
\varepsilon_M(T)
:=
\frac{T^{M+1}}{(M+1)!}
\sup_{0\le\sigma\le T}
|F_n^{(M+1)}(\sigma)|.
\tag{16}
\]

The derivative error satisfies

\[
\|F_n'-F_{M,n}'\|_\infty
\le
\frac{T^M}{M!}
\sup_{0\le\sigma\le T}
|F_n^{(M+1)}(\sigma)|.
\tag{17}
\]

If the right side of (17) is smaller than the minimum true kernel on the feature interval, then \(F_{M,n}\) remains increasing and has a nearby target root. A positivity-preserving finite-width implementation can instead approximate \(\sqrt{\kappa_n(\tau)}\) by a polynomial \(p_{M,n}\), set \(\kappa_{M,n}=p_{M,n}^2\), and define

\[
F_{M,n}(\tau)=f_n(0)+\int_0^\tau\kappa_{M,n}(s)\,ds.
\]

This prevents a truncation artifact from producing a negative tangent kernel.

For the deterministic formal-annealed closure at \(M=1\),
\(F_1(s)=f_0+\kappa_0s\). At the variance-normalized annealed
initialization, \(f_0=0\) and \(\kappa_0=17/6\), so

\[
f_1(t)=1-e^{-17t/3},
\qquad
\mathcal L_1(t)=e^{-34t/3}.
\]

This is the first constant-kernel member of the prescribed formal closure
hierarchy, not an exact full-model equation.

---

## 6. Global clock-shadowing theorem

The following theorem converts feature-orbit accuracy into uniform loss-curve accuracy.

Let \(F\) and \(\widetilde F\) be two increasing feature-time readout profiles with the same initial output \(f_0<1\). Assume that their relevant target-reaching intervals lie in a common interval on which

\[
0<\mu\le F'(\tau)\le K,
\qquad
\|F-\widetilde F\|_\infty\le\varepsilon,
\tag{18}
\]

and assume \(\widetilde F\) is also monotone and reaches \(1\). Let

\[
\dot\tau=2(1-F(\tau)),
\qquad
\dot{\widetilde\tau}=2(1-\widetilde F(\widetilde\tau)),
\]

with equal initial clocks. Then

\[
\sup_{t\ge0}|\widetilde\tau(t)-\tau(t)|
\le\frac{\varepsilon}{\mu}.
\tag{19}
\]

To prove this, put \(e=\widetilde\tau-\tau\). If \(e>0\), monotonicity and (18) give

\[
\dot e
=2\bigl(F(\tau)-\widetilde F(\widetilde\tau)\bigr)
\le-2\mu e+2\varepsilon.
\]

The same inequality holds for the upper Dini derivative of \(|e|\) when \(e<0\). Comparison with \(y'=-2\mu y+2\varepsilon\) proves (19).

It follows that

\[
\sup_{t\ge0}
|F(\tau(t))-\widetilde F(\widetilde\tau(t))|
\le
\varepsilon\left(1+\frac K\mu\right).
\tag{20}
\]

Since both outputs stay between \(f_0\) and \(1\),

\[
\sup_{t\ge0}
|\mathcal L(t)-\widetilde{\mathcal L}(t)|
\le
2(1-f_0)\varepsilon
\left(1+\frac K\mu\right).
\tag{21}
\]

Both losses converge to zero, so their difference also converges to zero. The target feature times differ by at most \(\varepsilon/\mu\).

Combining (16) and (21) gives the explicit finite-jet bound

\[
\sup_{t\ge0}
|\mathcal L_n(t)-\mathcal L_{M,n}(t)|
\le
2(1-f_n(0))
\left(1+\frac K\mu\right)
\frac{T^{M+1}}{(M+1)!}
\sup_{0\le\sigma\le T}
|F_n^{(M+1)}(\sigma)|,
\tag{22}
\]

provided the monotonicity and common-interval conditions hold.

Equation (22) is the requested constructive global stability theorem. The closure error occurs continuously in the top jet equation, but its effect on the entire infinite-time loss curve is bounded by a finite feature-interval remainder.

---

## 7. Direct input-to-state stability for an arbitrary finite PDE

The same conclusion can be stated without using the source-jet construction.

Suppose, after a positive-entry time, the true and approximate loss equations are

\[
\dot{\mathcal L}=-4\kappa\mathcal L,
\qquad
\dot{\widehat{\mathcal L}}
=-4\widehat\kappa\widehat{\mathcal L}+\eta,
\]

and assume

\[
\kappa,\widehat\kappa\ge\lambda>0,
\qquad
|\widehat\kappa-\kappa|\le\delta,
\qquad
|\eta|\le\rho.
\tag{23}
\]

Let \(E_0\) be the loss mismatch at the positive-entry time and let \(L_0\) be the true loss there. Integrating factors give

\[
\sup_{t\ge0}
|\widehat{\mathcal L}(t)-\mathcal L(t)|
\le
E_0
+L_0\,\Psi\!\left(\frac\delta\lambda\right)
+\frac{\rho}{4\lambda},
\tag{24}
\]

where

\[
\Psi(x)=x(1+x)^{-1-1/x}
\le\min\left\{1,\frac xe\right\}.
\]

The rate-error factor is sharp. It is attained by the two constant rates \(\lambda\) and \(\lambda+\delta\). The additive gain \(1/(4\lambda)\) is also sharp.

In particular, a persistent \(O(\delta)\) error in the decay rate creates only an \(O(\delta/\lambda)\) maximum absolute loss error. It does not accumulate linearly in time.

If the closure preserves gradient structure,

\[
\dot{\widehat f}=2(1-\widehat f)\widehat\kappa,
\]

then \(\eta=0\). Both losses converge to zero, and the approximation error eventually vanishes. A truly additive, ungated defect creates the unavoidable terminal floor \(\rho/(4\lambda)\).

This is why merely saying that the finite PDE has a small local residual is insufficient. The residual must either be measured in the observable rate or retain the vanishing squared-loss factor.

---

## 8. How the diagram/Wick hierarchy enters

The formal annealed source coefficients

\[
h_k=\lim_{n\to\infty}
\mathbb E\!\left[D_{+,n}^kf_n(0)\right]
\]

are precisely the aggregate scalar values of the order-\(k\) derivative/Wick
diagrams. The current exact special quadratic forest compiler gives, for each
fixed \(k\):

- a finite diagram expansion;
- a well-defined annealed leading large-width Wick value.

Thus, for every fixed \(M\), the formal annealed coefficients
\(h_0,\ldots,h_M\) provide deterministic initial data for the prescribed
compiler (12). If one separately proves concentration, finite-width
coefficient errors add at most

\[
\sum_{k=0}^M
|h_{k,n}-h_k|\frac{T^k}{k!}
\]

to the feature-profile error on \([0,T]\). The present report does not prove
that this term vanishes for a typical initialization.

The conditional noncommutative continuation-capacity argument is not
contradicted. At order \(k\), exponentially many ordered \(A\)/\(KA\) word
responses can contribute to the single number \(h_k\). That argument concerns
exact branchwise future semantics and additionally requires
freeness/faithfulness and branch separation. The present problem asks only
for one untagged loss orbit and allows the retained order \(M\) to grow with
the desired accuracy.

A more network-local construction retains all rooted message/Wick diagrams of complexity at most \(M\). If \(Y'=\mathcal F(Y)\) is the exact hierarchy in feature time and the finite closure has local residual \(R_M\), then on a feature interval of length \(T\), a Lipschitz estimate gives

\[
\|Y_M-P_MY\|_{[0,T]}
\le
\frac{e^{LT}-1}{L}
\|R_M\|_{[0,T]}.
\tag{25}
\]

Composing the kernel/readout extraction from (25) with (21) yields a global loss bound. Because \(T=\tau_*<\infty\), ordinary finite-interval Galerkin stability is enough; no estimate over infinite physical time is needed.

---

## 9. What is proved, and what is still a separate lemma

The following points are proved:

1. squared-loss dynamics are an exact residual-gated time change of readout ascent;
2. every target-fitting trajectory uses only finite feature time;
3. after positive entry, the network has the explicit kernel lower bound (5);
4. persistent tangent-kernel or loss-channel defects have the uniform bounds (21) and (24);
5. the one-source transport PDE (12) is a concrete finite approximation with an explicit closure residual and error formula;
6. every fixed truncation order is computable at the formal annealed level by
   the special quadratic derivative/Wick compiler.

The remaining statement is not supplied by Wick contraction alone:

\[
\varepsilon_M(T)\longrightarrow0
\quad\text{uniformly in width on the target feature interval.}
\tag{26}
\]

Sufficient conditions for (26) include any one of the following.

- A uniform analytic estimate
  \[
  \sup_{n\ge1}\sup_{0\le\tau\le T}
  |F_n^{(k)}(\tau)|
  \le Ck!R^{-k}
  \quad(k\ge0),
  \]
  with \(C\) and \(R>T\) independent of \(n\) and \(k\).
- A propagated weighted diagram tail
  \[
  \sup_{\tau\le T}\sum_\sigma
  e^{a|\sigma|}w_\sigma|Y_\sigma(\tau)|<\infty.
  \]
- A well-posed Hilbert/Wick-chaos hierarchy for which finite diagram projections converge uniformly on the compact feature interval.

Under the first condition, (16) is geometrically small. Under the second, a depth-\(M\) message truncation has exponentially small residual. Under the third, standard finite-rank Galerkin convergence supplies \(\delta_M\to0\).

Proving one of these width-uniform tail estimates is one required analytic
task.  An unconditional theorem about the network also needs concentration,
existence of the width-first positive-time target, and identification of the
compiler's observable with that target.

---

## Final verdict

Squared loss does change the answer to the approximate-closure question.

It does not remove the proliferating noncommutative hierarchy. Conditional on
the continuation-capacity hypotheses, it also does not restore an exact fixed
bounded-filtration commuting-source continuation encoder. But it makes the
loss observable globally stable in a precise input-to-state sense. A
residual-compatible closure error is seen only over finite feature time, and
a persistent small tangent-kernel error produces a uniformly small absolute
loss error for all physical time.

The concrete degree-\(M\) one-source PDE is (12), or equivalently the
\(M+1\)-state system (13). Its conditional global error is bounded by (22).
To obtain arbitrarily high accuracy for the actual network from increasing
\(M\), one needs a uniform tail estimate such as (26), concentration, and a
constructed and identified positive-time target. Exact branchwise
continuation semantics are not required for the observable-level theorem.
