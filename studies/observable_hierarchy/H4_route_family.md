# C-H4 independent family route: exact law representation and radius obstruction

Author: scoped agent `/root/h4_route_family`. Date: 2026-09-13.
Status: frozen independent candidate, **partial**. No promotion claim.

The law representation, deterministic integration/refinement bounds, and
membership in the explicit C.4.5 risk/activity ball are proved below. The
additional explicit membership certificate for the C.4.7 population-flow
neighborhood is **not proved**. Its precise missing estimate is identified in
§5. An exceptionally small explicit number cannot substitute for that estimate.

## 1. Scope and actual sources

The assignment permits only the specified established notation and C.4.7
material, together with necessary established dependencies reported before
retrieval. It forbids study histories, other routes, and other studies. This
agent has not read the study README, H4 contract, or another route's output.
No research experiment, implementation change, or Git write was performed.
The parent is the sole Git writer; this report is the sole owned write.

Full scientific reading actually completed:

- `docs/NOTATION.md`, complete.
- `docs/global_nonlinear.md`, C.4.7.1–5, lines 8989–10554, complete; and
  C.4.7.7, lines 11398–11440, complete.
- The exact necessary dependency C.4.5, lines 5270–6903: complete statement,
  numerical margins, geometry, C.4.5.1 reference dynamics and activity proof,
  C.4.5.2 reference source/tail proof, and C.4.5.3 comparison proof. The need
  for C.4.5.1–3 was reported to the supervisor before retrieval. Its enclosing
  theorem statement was read because it specifies the constants assembled
  from those three proof units.

A read endpoint also exposed the introductory C.4.6 paragraph at lines
6904–6920. It supplied no input used below; no C.4.6 theorem or proof was read.
The initial batched read was truncated; subsequent smaller reads covered all
the scientific ranges listed above completely. No external scientific source
was retrieved. Established source-theorem dependencies such as III.F and B.1
were used only through their explicit specializations in the permitted text;
this is not a new audit of their complete proofs.

Process sources read: `AGENTS.md`, `RESEARCH_WORKFLOW.md`, the complete
`investigate-conjectures` and `solve-math-rigorously` skills under
`/etc/codex/skills/`, and the research-contract and adversarial-audit references
of the former skill. Narrow scoped delegation replaces author startup.

Recorded source SHA-256:

| Source | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

HEAD before the report write was
`b2108ee5c3c3e702234cb450afd0af395e10c68e`. The shared index had no staged
paths; concurrent changes were observed as metadata only and preserved.

## 2. Exact fixed family

Use the exact C.4.7 model: input dimension two, two tanh hidden layers, no
biases, independent stored Gaussian variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, unhalved mean squared loss, physical GF time, retained actual
finite readout, and the canonical population initialization `(g,0,0)`.
The data metric is

\[
d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|.
\]

The reference is the specified opposite-label law

\[
\nu_*=\tfrac12\delta_{(\sqrt2e_1,+1)}
       +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]

First let \(r\in(0,1/4)\) be a fixed positive rational with an exact finite
description; its choice is independent of approximation order and accuracy.
Define the rational circle parametrizations

\[
u_1(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),
\qquad
u_2(t)=\left(-\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\right).
\tag{F1}
\]

For rational \(b\in[1/2,1]\), put \(a=br\), and let

\[
A_b=\tfrac12\delta_{(\sqrt2u_1(0),+1)}
    +\tfrac12\delta_{(\sqrt2u_2(a),-1)}.
\tag{F2}
\]

Let \(Z\) be uniform on \([-1,1]\), and define

\[
N_b=\tfrac12\operatorname{Law}(\sqrt2u_1(aZ),+1)
    +\tfrac12\operatorname{Law}(\sqrt2u_2(aZ),-1).
\tag{F3}
\]

For rational \(\alpha\in[0,1]\), our fixed family is

\[
\mathcal C_r=\{\mu_{b,\alpha}=(1-\alpha)A_b+\alpha N_b:
 b\in\mathbb Q\cap[1/2,1],\ \alpha\in\mathbb Q\cap[0,1]\}.
\tag{F4}
\]

Its law description is the finite tag `(F4,r,b,alpha)`. Both parameters are
ordinary rational inputs. The radius is one common fixed constant; neither
the family nor its members are reselected after choosing an error tolerance.
A singleton atomic law and singleton nonatomic law would suffice; (F4) records
a slightly larger elementary class without changing the argument.

The identity

\[
(1-t^2)^2+4t^2=(1+t^2)^2
\]

proves \(|u_i(t)|=1\), so the input norm is exactly \(\sqrt2\).
The labels are exactly binary. The two normalized atomic inputs have Gram
entry

\[
u_1(0)\cdot u_2(a)=-\frac{2a}{1+a^2}<0.
\tag{F5}
\]

Thus every \(A_b\) is nonorthogonal; no rank limiting or angle-zero
interpretation is being used. For \(N_b\), both maps in (F1) are injective on
\([-a,a]\), since their angular parametrization is \(2\arctan t\) and its
quarter-turn. Equivalently, the inverse of \(u_1\) there is
\(t=u_{1,2}/(1+u_{1,1})\), whose denominator is positive; rotate for \(u_2\).
Every point therefore has a preimage of Lebesgue measure zero. Hence \(N_b\)
is nonatomic. For independently selected parameters \(s,t\in[-a,a]\),

\[
u_1(s)\cdot u_2(t)
=\frac{2(s-t)(1+st)}{(1+s^2)(1+t^2)}.
\tag{F6}
\]

As \(1+st>0\), cross-cluster inner products vanish only when \(s=t\), a
null subset of the parameter square. The nonatomic members do not impose an
orthogonal training geometry.

The exact chord and derivative bounds are

\[
|u_i(t)-e_i|=\frac{2|t|}{\sqrt{1+t^2}}\le2|t|,
\qquad |u_i'(t)|=\frac2{1+t^2}\le2.
\tag{F7}
\]

Couple each component with its corresponding reference atom and retain its
label. For (F2), only the second atom moves; for (F3), average \(|Z|\), whose
expectation is \(1/2\). Consequently

\[
\mathcal W_1(A_b,\nu_*)\le a,
\qquad \mathcal W_1(N_b,\nu_*)\le a,
\qquad \mathcal W_1(\mu_{b,\alpha},\nu_*)\le a\le r.
\tag{F8}
\]

The third inequality uses the mixture of the first two explicit couplings.
These are upper bounds; an optimal transport calculation is unnecessary.

## 3. Executable integration, exact finite laws, and huge exponents

For any integrable observable \(G:\mathcal Z\to\mathbb R\), its exact law
integral is

\[
\begin{split}
\int G\,d\mu_{b,\alpha}
={}&\frac{1-\alpha}{2}
 [G(\sqrt2u_1(0),+1)+G(\sqrt2u_2(a),-1)]\\
&+\frac\alpha4\sum_{i=1}^2
 \int_{-1}^{1}G(\sqrt2u_i(az),y_i)\,dz,
\qquad (y_1,y_2)=(+1,-1).
\end{split}
\tag{F9}
\]

This is a finite sum and two one-dimensional integrals, not an unspecified
conditional-law oracle. For a computable continuous integrand with a supplied
effective modulus, adaptive or uniform interval quadrature is executable.
For an \(L\)-Lipschitz integrand in the stated data metric, the following
fully explicit rule has a rigorous error bound.

Set \(m=2^j\), \(j\ge0\), and
\(z_{j,k}=-1+(2k+1)/m\), \(0\le k<m\). Define

\[
N_{b,j}=\frac1{2m}\sum_{i=1}^2\sum_{k=0}^{m-1}
\delta_{(\sqrt2u_i(az_{j,k}),y_i)},
\quad
\mu_{b,\alpha,j}=(1-\alpha)A_b+\alpha N_{b,j}.
\tag{F10}
\]

Every weight is rational and every normalized coordinate is rational in the
exact rational inputs. Physical coordinates are \(\sqrt2\) times those
rationals, so a finite atom has an exact algebraic expression. The largest
support count is \(2m+2\); zero-weight atoms may be omitted. No root of an
empirical Gram matrix is needed to describe these laws.

Transport each parameter cell of length \(2/m\) to its midpoint. The
conditional mean displacement in parameter space is \(1/(2m)\); (F7)
multiplies it by at most \(2a\). Therefore

\[
\mathcal W_1(N_b,N_{b,j})\le a/m,
\quad
\mathcal W_1(\mu_{b,\alpha},\mu_{b,\alpha,j})\le\alpha a/m,
\tag{F11}
\]

and the error of replacing (F9) by the finite sum (F10) is at most
\(L\alpha a/m\). Select \(j\) with \(2^j\ge L\alpha a/\varepsilon\) for a
given positive integration tolerance; when the right side is below one,
\(j=0\) suffices. With merely a supplied modulus \(\omega_G\), the maximum
transport displacement gives error at most \(\omega_G(2a/m)\).
This proves a refinement rule for law integration; it does not supply a
population Gaussian contraction algorithm or a trajectory approximation rate.

The finite laws stay in the same geometric ball. Indeed
\(m^{-1}\sum_k|z_{j,k}|\le1/2\): it equals \(1/2\) for even \(m\), while
the single midpoint at \(m=1\) is zero. The coupling proving (F8) thus proves
\(\mathcal W_1(\mu_{b,\alpha,j},\nu_*)\le r\) for every \(j\).

One concrete positive exact radius certifying the C.4.5 part is

\[
N=2^{8192},\qquad r=2^{-N}.
\tag{F12}
\]

This is an ordinary rational number with a short arithmetic expression.
The exponent \(N\) is itself a finite integer of 8193 binary digits. The
denominator \(2^N\) must **not** be expanded as an integer merely to store
the law. Store the expression `Pow2(-Pow2(8192))`, and use sparse dyadic
expressions and rational expression trees for (F1). These representations
contain only explicitly specified integers and arithmetic operations.
They contain no inaccessible real-number oracle or target trajectory.

Its relation to the risk radius is certified without evaluating either
tiny number. From \(\log2>1/2\) and \(\log(\log2)>-1\),

\[
\log\bigl(\log(1/r)\bigr)
=8192\log2+\log(\log2)>4095>3000.
\]

Thus

\[
0<r<\exp\{-\exp(3000)\}.
\tag{F13}
\]

The elementary inequalities used here can be certified by the exponential
series: \(e^{1/2}<2\), \(e>2\), and consequently
\(\log2>1/2>e^{-1}\). No machine evaluation of \(e^{3000}\) is needed.

For an absolute binary precision request \(p\le N\), the enclosure
\([0,2^{-p}]\) already contains \(r\); for \(p>N\), arbitrary-precision
evaluation can in principle emit the needed dyadic bits. Expanding those
bits would require an astronomical but finite computation. The sparse
expression permits exact positivity, nonorthogonality in (F5), norm and
support checks without that expansion. Evaluating (F1) in ordinary floating
point rounds the perturbation to zero; such output is only an approximation
and cannot certify nonorthogonality. Interval evaluation or exact symbolic
rational identities preserve the actual law.

One can replace (F12) by any subsequently certified smaller explicit positive
rational. The formulas and proofs remain unchanged. A tower of exponents has
no automatic implication for the missing C.4.7 certificate in §5.

## 4. What the explicit radius does prove dynamically

Write \(\delta_{\mathrm{risk}}=\exp\{-\exp(3000)\}\). By (F8),(F13), every
law in \(\mathcal C_r\), and every approximating law (F10), lies strictly
inside the C.4.5 ball. The exact finite Borel-law GF is globally defined:
C.4.7.2 differentiates the compact-domain law integral and uses the
finite-dimensional energy identity to prevent finite-time escape.

The C.4.5.3 comparison applies to actual finite GF with zero discretization
defect. It compares each actual law against actual reference GF on the same
initialized arrays, so it retains the specified nonzero finite readout.
Its constants are

\[
B=12,\quad K=40000000,\quad d_0=10^{-18},\quad
R=e^{2900},\quad M_Q=225400e^{2880}+180,\quad H=16(4+M_Q).
\]

The two required inequalities are C.4.5.3 (15):

\[
KH e^{K(1+R)-R^2/4096}<d_0/4,
\qquad K(1+R)e^{K(1+R)}\delta_{\mathrm{risk}}<d_0/4.
\tag{F14}
\]

The enclosing C.4.5 statement checks these using
\(M_Q<e^{2893}\), \(H<e^{2897}\), \(K<e^{18}\),
\(1+R<e^{2901}\), \(R^2/4096>e^{5791}\), and
\(e^{-100}<d_0/4\). It also checks
\(44928\delta_{\mathrm{risk}}<1/256\) and
\(8B^2\delta_{\mathrm{risk}}<10^{-18}\).
These are constant inequalities, not numerically fitted dynamics.

The reference risk bound is \(e^{-16}\) at time 40. Its paired RMS in
each hidden layer at physical time \(1/200\) is strictly greater than
\(1/2500000\). The latter uses the opposite-label calculation
C.4.5.1 (R24)–(R36); it does not import the equal-label example.
For changed-law activity, the comparison lower bound is

\[
\left(\frac1{2500000}\right)^2
 -2(B+1)d_0-8B^2\delta_{\mathrm{risk}}
 >1.59\times10^{-13}>10^{-13}.
\tag{F15}
\]

In particular the strict limiting finite-GF margins pass the requested
thresholds: risk at time 40 is at most \(1/4\), and both training-averaged
paired squared displacements at \(1/200\) are at least \(10^{-13}\), with
probability tending to one as width tends to infinity. The comparison
also permits arbitrary empirical law sequences converging to a fixed family
member, with width increasing, without a sample/width rate. Exact nonatomic
GF integrals are admitted by the same compact-domain argument.

The proof requires only \(\delta_{\mathrm{risk}}\) for these finite
probability statements. **This does not by itself construct or identify a
changed-law population trajectory.** If a family member is additionally
certified inside C.4.7's \(U_1\), C.4.7.1–5 identify its strong population
flow, and C.4.7.7 then passes these same strict margins to that flow.
Keeping initialized and current hidden fields jointly on each own carrier
is essential; no Wasserstein distance between two unpaired hidden marginals
is substituted for (F15).

## 5. Exact remaining obstruction to the requested full family certificate

C.4.7.7 explicitly requires the **intersection** of the C.4.5 ball and the
C.4.7 population neighborhood. The second condition cannot be inferred from
(F13). C.4.7.4 chooses \(0<\delta_1<\rho/4\), where \(\rho\) is selected
after the coefficient bootstrap in C.4.7.3. The decisive sufficient
inequality is (C.4.7.N31):

\[
C_B e^{40C_B}\{\Phi_{B_*}(q)+q\}^{1/16}\le\frac12,
\qquad q<\rho,\quad B=B_*+1.
\tag{F16}
\]

The reference cap itself **is explicit**. With \(Y=1,T=40\), let

\[
\begin{gathered}
C_0=e^{80}-1,\quad R_0=e^{80},\quad M=10+80R_0C_0,\\
L=100(1+M+C_0+R_0)^4,\quad E=e^{40L},\\
P_0=2(MC_0^2+2R_0MC_0+C_0^2+2R_0C_0+C_0+R_0),\\
K_0=1+2C_0(M+1),\quad
B_{\rm cl}=2C_0+40P_0K_0E,\quad B_*=B_{\rm cl}+1.
\end{gathered}
\tag{F17}
\]

These are exactly N38–N47 and the raw-reference transfer. There is no
unknown physical trajectory in (F17). The raw-reference mesh threshold
\(h_*\), however, is chosen by N51 with an unspecified constant and modulus.

What is absent numerically is a verified explicit majorant for \(C_B\) in
N24–N31. The text states that these generic constants may increase at each
estimate. N27 uses source-derivative moments, interpolation, random
integrating-factor estimates, and averaging; N29a–b add another Gronwall
amplification. Without tracing those constants, one cannot substitute a
number into (F16). N30a additionally writes

\[
\Phi_{B_*}(q)=Cq\exp\{C\sqrt{\log(e/q)}\}
\]

only with an unspecified enlarged \(C\) and an unspecified small-q branch.
Both the majorant and its valid range are required for an executable check.

This is not a claim that the family fails or that an explicit radius is
mathematically impossible. The allowed proof provides finite constants
through explicit inequalities and therefore suggests a quantitative
completion. This route has not supplied that additional derivation, and
no estimate on the number or height of exponentials is proved here.
In particular, neither “choose a much smaller dyadic” nor
\(r=\min\{\delta_1/8,\delta_{\mathrm{risk}}/8\}\) satisfies the requested
executable certificate: the former lacks a verified bound and the latter
retains the unspecified constant in the law description.

A precise sufficient repair is to produce rationally evaluable constants
\(C_{\mathrm{src}},C_{\mathrm{raw}},q_0>0\), at the explicit cap (F17),
such that N31 holds with \(C_B\le C_{\mathrm{src}}\) and

\[
\Phi_{B_*}(q)\le
C_{\mathrm{raw}}q e^{C_{\mathrm{raw}}\sqrt{\log(e/q)}}
\quad(0<q\le q_0).
\tag{F18}
\]

Select a dyadic \(\rho_0\le q_0\) for which substituting \(q=\rho_0\)
and these constants into (F16) has strict slack and for which the right
side of (F18) is increasing on \((0,\rho_0]\). For example, monotonicity
holds when \(\log(e/\rho_0)>C_{\mathrm{raw}}^2/4\), by differentiating
its logarithm. Then choose the fixed rational
\(r<\min\{\rho_0/8,\delta_{\mathrm{risk}}\}\), using logarithmic comparisons.
The same N-cap and completion proof can take \(\delta_1=\rho_0/8\), so
(F8) certifies every member and every finite refinement in the supported
population regime. If a stopping rule with a certified error tolerance is
also required, the Euler threshold/modulus and Gaussian-integration errors
must additionally be quantified; merely knowing \(h_* >0\) gives a
convergent refinement sequence but no certified finite stopping criterion.

## 6. Frozen conclusion and checks

The independent construction (F1)–(F11) solves the representation and
integration portion exactly, with atomic nonorthogonal and nonatomic laws,
fixed family quantifiers, exact finite descriptions, and explicit Wasserstein
refinement. Formula (F12) proves membership in the explicit finite-GF
risk/activity regime, with the threshold checks (F14)–(F15).

The requested full C-H4 population family certificate remains **open in
this route**, specifically at (F16)–(F18). No existential radius has been
silently treated as computable, and finite-GF risk robustness has not been
upgraded to population-flow identification. The surviving objection is a
missing quantitative proof bridge, not a counterexample to C-H4.

Checks actually performed: complete permitted-source reading after repairing
truncation; manual verification of circle identities, strict positive Gram
entry magnitude, nonatomicity, coupling costs, midpoint error, parameter
independence, law-representation arithmetic, logarithmic radius comparison,
and the distinction between the two neighborhood conditions. The source's
Gaussian rational certificate was read in full but not reexecuted by this
agent. No claim of an independently reproduced training experiment is made.
