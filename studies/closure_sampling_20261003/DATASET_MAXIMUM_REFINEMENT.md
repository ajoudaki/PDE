# A sharper sample-count penalty from the Gaussian maximum

2026-10-04. Bounded continuation of `DATASET_SOURCE_CONSTANTS.md` and
`DATASET_DEPENDENCE_CHECK.md`. This is a collaborative internal refinement
of the same compression proof, not an independent promotion review or a
claim of optimality. The earlier checked theorem remains valid. No new
scientific sources, experiments, or other-file edits are used here.

The factor \(m^{-1/2}\) in the previous sufficient label condition is
**not sharp in the existing proof**. Replacing its crude Gaussian
maximum estimate gives structural constants \(c,C>0\) for which the
full source construction is valid under

\[
 0<Y\le c\lambda\exp\{-C\sqrt{\log(em)}\},
 \qquad
 \lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}.
 \tag{1}
\]

Here \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\), and the initialized
covariance \(Q^{(L)}\) is the same recursively defined covariance as
in `DATASET_DEPENDENCE.md`. Structural constants depend only on the
fixed input dimension, depth, and activation strip/bounds. They do not
depend on \(m,\lambda,Y\), or width. The result still takes these
dataset parameters fixed before width tends to infinity.

## 1. Conditional exponential moment of the maximum

The checked activity-normalized Gaussian reference supplies nonnegative
random variables \(Z_a\), one per training sample. Conditional on the
retained cavity initialization, there are structural constants
\(A\ge0,D\ge1,b>0\) such that

\[
 \mathbb P\{Z_a>A+t\mid\text{cavity}\}
 \le D e^{-bt^2},\qquad t\ge0.
 \tag{2}
\]

For the real reference,
\(Z_a=\sup_t|g^\top\delta_a(t)|/S\), where
\(g\sim N(0,I_n/n)\) is the independent omitted root and
\(S=C_0Y/\lambda\) bounds total residual activity. The proof of
(2) is the already-checked Gaussian path calculation. Its constants
are independent of the carrier budget once
\(S^2\log(e+B)\le c\) and \(S\le c\).

For the complex reference, add the normalized short-contour correction.
The checked complex Gaussian calculation bounds its mean by \(o(1)\)
and its tail scale by \(D_n=o(1)\). For sufficiently large width,
these are at most fixed constants. A union bound for the real reference
and its complex correction therefore gives (2), after a structural
enlargement. No independence between those two pieces is needed. The
width needed here may depend on the fixed dataset parameters, as before.

Let \(Z=\max_{a\le m}Z_a\) and
\(u_m=\sqrt{\log(Dm)/b}\). A union bound gives, for every \(t\ge0\),

\[
 \begin{aligned}
 \mathbb P\{Z>A+u_m+t\mid\text{cavity}\}
 &\le Dm\exp\{-b(u_m+t)^2\}\\
 &=\exp\{-2bu_mt-bt^2\}\le e^{-bt^2}.
 \end{aligned}
 \tag{3}
\]

For the nonnegative excess \(V=(Z-A-u_m)_+\), tail integration
therefore proves, for each fixed \(\eta>0\),

\[
 \begin{aligned}
 \mathbb E[e^{\eta V}\mid\text{cavity}]
 &=1+\eta\int_0^\infty e^{\eta t}
                      \mathbb P\{V>t\mid\text{cavity}\}\,dt\\
 &\le1+\eta\sqrt{\pi/b}\,e^{\eta^2/(4b)}.
 \end{aligned}
\]

Since \(Z\le A+u_m+V\), this yields

\[
 \mathcal L_*(\eta)
 :=\mathbb E[e^{\eta\max_a Z_a}\mid\text{cavity}]
 \le C_\eta\exp\{C\eta\sqrt{\log(em)}\}.
 \tag{4}
\]

The right side is deterministic and uniform in the cavity and fixed
deletion count, after the allowed width threshold. The samples can be
arbitrarily correlated. No sample independence has been introduced.

## 2. Substitution into the existing source budget

Keep the budget parameter \(\eta_0>0\) fixed; it does not depend
on the sample count, moment degree, confidence, or width. The checked
fixed-block argument requires

\[
 B>4(L-1)\mathcal L_*(\eta_0)e^{C\eta_0},\qquad
 e^{C\eta_0S^2B}\le2.
 \tag{5}
\]

By (4), choose structural constants \(C_B,c_B>0\) so that

\[
                 B=C_B\exp\{c_B\sqrt{\log(em)}\}
 \tag{6}
\]

is larger than the first right side in (5), and larger than the fixed
initial budget. It suffices to require

\[
                         S^2B\le c.
 \tag{7}
\]

This implies the second condition in (5). Taking \(B\ge1\), it
also implies fixed small \(S\) and
\(S^2\log(e+B)\le c'\), after adjusting structural constants.
Every non-real source smallness condition is therefore satisfied:

- The singleton trace shift \(CS(1+S^2B)\) is at most \(CS\).
- The endpoint trace-series budget terms are controlled by (7).
- The activity-normalized Gaussian path modulus has a structural constant.
- The weak variational propagator and nonlinear insertion estimates use
  fixed small \(S\); factors involving fixed \(B\) in their width
  bounds are absorbed into \(n_0\).
- The stopped maximum \(S\eta_0^{-1}\log(nB)\) is at most
  \(CS\log(en)\) once width absorbs \(\log B\). Forward/angular
  induction, source magnitudes, and exclusion of query poles are unchanged.

The moment degree is still fixed before taking width large. Repeated
indices use finite moments \(\mathcal L_*(q\eta_0)\), with
\(q\) fixed; only collision constants and width thresholds depend
on that degree. The distinct-index moment base in (5) remains independent
of it. Thus no growing-deletion statement or new probability limit is
required.

The separately checked real energy theorem requires \(Y\le c\lambda\)
and supplies \(S=C_0Y/\lambda\). Substituting (6) into (7)
therefore permits

\[
 Y\le c\lambda\exp\{-(c_B/2)\sqrt{\log(em)}\}.
\]

After renaming structural constants this is (1), which also implies
the real energy condition. The earlier condition
\(S^2\le c\lambda\) belonged only to the superseded coarse
real Gram bootstrap, as checked in the appended source audit; it is
not reintroduced here.

## 3. Retained conclusions and limits of sharpness

The source radius and magnitude, time horizon, polynomial degrees,
number of source families, and cubature construction are unchanged.
For sufficiently large width, the refined label class therefore has
the same explicit retained-state bound

\[
 C(1+m)^4\lambda^{-4}[\log(en)]^{4[d(L+5)+1]}
       +Cm(d+1).
 \tag{8}
\]

With source tolerance \(n^{-1}\), its same-time comparison remains

\[
 \sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
 \le C e^{CY/\lambda^2}n^{-1}
      e^{(CY^2/\lambda^3)\sqrt{\log(en)}}.
\]

The already-checked additional condition
\(\log(en)\ge C(1+Y^4/\lambda^6)\) absorbs the final
exponential. Including the query tails and fitted endpoints gives

\[
 \sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
 |f_C(t,x)-f_n(t,x)|
 \le C e^{CY/\lambda^2}/\sqrt n.
 \tag{9}
\]

The previous label-specialized upper bound
\(C e^{C/(\lambda\sqrt m)}/\sqrt n\) should not be used
throughout the larger class (1); (9) is the unchanged general formula.
Both flows fit and converge by the same real energy theorem.

All conclusions retain the full threshold
\(n_0(d,L,b,B_\phi,m,\lambda,Y,\eta)\) for fixed positive
\(Y\), including the existing fixed-moment probability argument.
No practical formula for that entire threshold, uniform claim for
arbitrarily small positive labels, or growing-dataset theorem has been
added.

The improvement replaces a polynomial penalty by
\(\exp\{-C\sqrt{\log(em)}\}=m^{-o(1)}\). It demonstrates
that the earlier power \(m^{-1/2}\) resulted from a loose estimate,
so that power cannot be called sharp for this construction. It does
not establish optimality of the new penalty, a necessary dependence on
\(m\), or an optimal dependence on the Gram gap or label direction.
Those questions would require further upper-bound improvements or
matching obstructions for the actual trained-network problem. The
conditional Gaussian maximum alone supplies no such obstruction.

The union-tail calculation was completed before the supervisor exchanged
an equivalent exponential-moment/Jensen derivation. Both use only the
already-checked per-sample Gaussian bound. This note preserves the
earlier theorem and records the bounded continuation separately.
