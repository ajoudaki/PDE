# A single-coefficient envelope for dense comparison and Legendre order

2026-10-04. **Conditional PASS for the finite algebra below.** This note
proves the explicit envelope of the already checked comparison formulas,
including a readout refinement retaining the label amplitude. Its explicit
dependency is the coordinator-supplied source-envelope calculation
\[
 S_*^{\rm src}\ge\beta^{-26L},\qquad
 K_{\rm src}\le\beta^{21L}.                         \tag{1}
\]
That calculation is awaiting the coordinator's check; this note does not
independently certify it or replace the probabilistic source theorem.
Subject to (1), no new trained-moment, sensitivity, or geometry hypothesis
is introduced. The source width threshold remains eventual.

The scientific inputs are confined to this integrated study:
`GENERAL_DENSE_COMPARISON.md` equations (37)--(44), the complete
`GENERAL_EXPLICIT_FITTING.md`, the source definitions in
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, and the already checked
`EXPLICIT_LEGENDRE_COMPARISON.md` and explicit closure fitting formulas.
The canonical-notation and rigorous-math instructions were applied. This
is an internal algebra/interface check, not a promotion review.

## 1. Compact statement and scope

Use the canonical width-\(n\), depth-\(L\ge2\) network, with unit inputs
\(v=x/\sqrt d\), Gaussian first weights of entry variance one, hidden
weights of entry variance \(1/n\), zero readout, mean squared loss, and
mobilities \((n,1,\ldots,1,n)\). The fixed data have
\(\gamma=\lambda_{\min}(Q_L)>0\), and
\(Y=\|y\|_2/\sqrt m\). Activations are real on the real axis,
holomorphic on \(|\Im z|<a\), with bounded first derivative on that
strip; values may be unbounded. Define
\[
 b=\max_j|\phi_j(0)|,\quad
 s=\max\{1,\max_j\sup_{|\Im z|\le a/2}|\phi_j'(z)|\},\quad
 t_2=\max_j\sup_{|\Im z|\le a/2}|\phi_j''(z)|,
\]
\[
 \beta=\max\{10,1+b,16/a,s,\max(1,t_2)\},\qquad
 B=\beta^{100L}(1+m/\gamma)^4.                         \tag{2}
\]
The full-strip slope hypothesis makes these quantities finite by Cauchy's
formula. For \(0<\delta<1\) and
\[
 0<Y\le(\gamma/m)\beta^{-30L},                        \tag{3}
\]
two independent dense initializations satisfy, at sufficiently large
individual widths with probability at least \(1-\delta\),
\[
 \boxed{\displaystyle
 \|f_n-f_n'\|_*
 \le BY\exp\!\left[B{Ym\over\gamma}\sqrt{\log(en)}\right]
       \sqrt{{\log[8(n+1)(1+2n)^d/\delta]\over n}}.     \tag{4}
\]
Here
\(\|f-g\|_* =\sup_{t\in[0,\infty]}\sup_{\|v\|=1}|f(t,v)-g(t,v)|\)
uses the same physical time in both predictors and includes their fitted
limits. The coefficient is a deliberately conservative finite envelope.
The width-dependent exponential remains, so (4) is a near-root result.

The same allowance and coefficient give the simple deterministic order
\[
 q_n=\left\lceil n^{1/4}
                \exp\!\left[B\sqrt{\log(en)}\right]\right\rceil,
 \qquad
 \|f_{n,q_n}-f_n\|_*\le Y/\sqrt n.                    \tag{5}
\]
The Legendre closure has the same width and initialization as its dense
reference and uses its original autonomous residual-RMS clock. Its
comparison is at the original physical times. The probability and source
threshold qualifications are the same component qualifications as in the
checked numerical theorem. For \(Y=0\), all these predictors are
identically zero and no division by \(Y\) is required.

## 2. Elementary bounds and admissibility

The following symbols are temporary proof variables, not further constants
needed in the compact statement:
\[
 g=\gamma/m,\qquad h=1+1/g,\qquad z=Y/g,\qquad
 l_n=\sqrt{\log(en)},\qquad T=9s.
\]
For a standard Gaussian \(Z\), let
\(q_0=1\),
\(q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}Z)^2\), and
\(H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L})\).
Minkowski and linear growth give
\[
 H\le(2\beta)^L\le\beta^{3L/2},\qquad
 g\le H^2\le\beta^{3L},\qquad
 Y=gz\le\beta^{-27L}<1.                              \tag{6}
\]
The first inequality follows from
\(\sqrt{q_j}\le b+s\sqrt{q_{j-1}}\). The Gram inequality follows
from its common diagonal \(q_L\) and \(m\ge1\).

The fitting note's sufficient cap \(Y\le g\beta^{-5L}\) and the
closure note's sufficient cap \(Y\le g\beta^{-10L}\) follow from
(3). Also
\[
 S=16z\le\beta^{-29L}\le\beta^{-26L}\le S_*^{\rm src},
                                                               \tag{7}
\]
using \(16\le\beta^L\), so the source cap follows from (1).
There is no replacement of an unknown small-label constant by the power
30: all three sufficient conditions are explicitly checked here.

The dense fitting constant and forward subtraction coefficient obey
\[
 F=s^2\left[T^{2L-2}+4H^2\sum_{j=0}^{L-2}T^{2j}\right]
       \le\beta^{7L},\qquad F_z=2HT^{L-1}\le\beta^{4L}. \tag{8}
\]
Indeed \(T\ge9\), so the geometric sum gives
\(F\le(21/20)H^2s^2T^{2L-2}\); use \(T\le\beta^2\).
In particular \(FY^2/g=Fgz^2\le\beta^{-50L}\le1\).
The source maximum, through all physical time after its eventual tail
threshold, satisfies
\[
 M=2K_{\rm src}S l_n\le\beta^{22L}z l_n.              \tag{9}
\]
The factor two is the one already retained in the numerical dense and
Legendre comparisons. It is not a new source assertion.

## 3. Deterministic comparison and the refined readout

For the dense comparison put
\(\kappa=g/2\), \(R=2Y/\sqrt g\), and define exactly as in the
numerical source
\[
 B_\delta=sT^{L-1}R,\quad P=1+2H(L-1),\quad G=PB_\delta+2H,
\]
\[
 D_\delta=sT^{L-1}(1+B_\delta)+Lt_2F_zT^{L-1}M,
 \qquad J=PD_\delta+[1+(L-1)B_\delta]sF_z.             \tag{10}
\]
The dense physical tube supplies feature RMS \(2H\), readout RMS
\(R\), matrix caps nine, mean tangent-Gram gap \(g/4\), and
\(\rho(t)\le Ye^{-\kappa t}\).

For two actual good trajectories let
\[
 D_h(t)={\|\Delta A(t)\|_F\over\sqrt n}
                +\sum_{j=2}^L\|\Delta W^{(j)}(t)\|_F,
 \qquad D_w(t)={\|\Delta w(t)\|_2\over\sqrt n},
 \qquad D(t)=D_h(t)+D_w(t).
\]
The checked good-pair argument gives
\[
 \int_0^t\|\Delta r(s)\|_2/\sqrt m\,ds
       \le{4GJ\over\kappa}\int_0^t\rho(s)D(s)\,ds,
 \qquad
 \sup_tD(t)\le D(0)e^{E},
\]
\[
 E=2J(1+4G^2/\kappa)Y/\kappa.                        \tag{11}
\]
Here \(\rho\) can be the chosen reference residual. These inequalities
compare two actual trajectories; they impose no tube condition on an
interpolating parameter segment.

The additional label refinement uses only the exact readout equation.
Zero initial readouts give \(D_w(0)=0\). Feature subtraction costs
\(sF_zD_h\), while reference features have RMS at most \(2H\).
Consequently
\[
 D_w(t)\le4H\int_0^t\|\Delta r(s)\|_2/\sqrt m\,ds
                    +2sF_z\int_0^t\rho(s)D_h(s)\,ds.
\]
Applying (11) and \(\int\rho\le Y/\kappa\) yields
\[
 \sup_tD_w(t)
 \le\left({16HGJ\over\kappa}+2sF_z\right)
                         {Y\over\kappa}D(0)e^E.       \tag{12}
\]
Prediction subtraction on the whole sphere costs
\(2HD_w+RsF_zD_h\). Therefore
\[
 \|f-f'\|_*
 \le Y C_Y D(0)e^E,
\]
\[
 C_Y={2H\over\kappa}
               \left({16HGJ\over\kappa}+2sF_z\right)
                   +{2sF_z\over\sqrt g}.             \tag{13}
\]
This is the precise new readout refinement. It is a deterministic
consequence of the previously checked residual and parameter comparison,
not a hypothesis concerning Gaussian sensitivities. All bounds pass to
the fitted endpoint by the physical parameter convergence.

## 4. Exponent ledger for the dense coefficient

The following estimates hold for every \(n\ge1\) on the good set.
All powers are deliberately rounded upward.

| Quantity | Bound | Verification |
|---|---|---|
| \(R\) | \(\beta^{-28L}\le1\) | \(R=2z\sqrt g\), (3), (6) |
| \(B_\delta\) | \(\beta^{-26L}\le1\) | \(sT^{L-1}\le\beta^{2L}\) |
| \(P,G\) | \(\beta^{3L}\) | Both at most \(1+2HL\), using \(B_\delta\le1\) |
| \(D_\delta\) | \(\beta^{8L}(1+M)\) | Its two terms are at most \(\beta^{3L}\) and \(\beta^{7L}M\) |
| \(J\) | \(\beta^{12L}(1+M)\) | The second term of (10) is at most \(\beta^{5L}\) |
| \(E\) | \(\beta^{20L}hz(1+M)\) | Substitute \(\kappa=g/2\), \(G^2\le\beta^{6L}\) in (11) |
| \(C_Y\) | \(\beta^{21L}h^2(1+M)\) | Expand (13) as below |

For the last row the exact expansion is
\[
 C_Y={128H^2GJ\over g^2}+{8HsF_z\over g}
                                      +{2sF_z\over\sqrt g}.
\]
The three terms are bounded respectively by
\(\beta^{20L}h^2(1+M)\), \(\beta^{8L}h\), and
\(\beta^{6L}\sqrt h\). Their sum satisfies the table's bound.
The elementary allowances used throughout are
\(L\le\beta^{L-1}\), \(2,8,32\le\beta^L\), and
\(128\le\beta^{2L}\), valid for \(L\ge2\), \(\beta\ge10\).

Since \(z\le1\), \(h\ge1\), and \(l_n\ge1\), (9) and the
ledger imply
\[
 E+M\le\beta^{44L}hz l_n.                            \tag{14}
\]
For example, the three terms before rounding upward have coefficients
\(\beta^{20L}\), \(\beta^{42L}\), and \(\beta^{22L}\), all
times \(hz l_n\). The second uses \(z^2\le z\).

## 5. Gaussian extension, confidence, and the sphere endpoint

Let \(\mathsf G\) be the standard Gaussian vector of initialized
blocks \((A_0,\sqrt nW_0^{(2)},\ldots,\sqrt nW_0^{(L)})\).
Because both readouts start at zero,
\[
 D(0)\le{\sqrt L\over\sqrt n}
                           \|\mathsf G-\mathsf G'\|_2.
\]
Equations (11)--(13) give the good-set scalar Lipschitz constant
\[
 \mathcal L_Y={YC_Y\sqrt L\over\sqrt n}e^E.           \tag{15}
\]
This is a pairwise Lipschitz estimate on the actual good set. For each
query and time, extend the scalar prediction by the McShane infimum and
truncate to \([-2HR,2HR]\). The extension agrees on the good set and
is globally \(\mathcal L_Y\)-Lipschitz. No conditional Gaussian
Poincare inequality or differentiation of a good-event indicator occurs.

For two independent Gaussian roots, the difference of these identical
scalar extensions has mean zero and Lipschitz constant
\(\sqrt2\mathcal L_Y\) on the product space. Gaussian concentration
therefore bounds its two-sided tail at level \(u\) by
\(2\exp[-u^2/(4\mathcal L_Y^2)]\).

The physical speed estimate and whole-sphere input Lipschitz estimate
give, in the proof coordinate \(v_t=1-e^{-\kappa t}\), the modulus
\(K_t|v_t-v_{t'}|+K_x\|v-v'\|_2\), where
\[
 K_t={8(H^2+FY^2/g)Y\over\kappa},\qquad K_x=RT^L.
\]
The proof coordinate changes neither network's training time. A grid of
\(n+1\) such time coordinates, including one for infinity, and a sphere
\(1/n\)-net have joint size at most
\(N_n=(n+1)(1+2n)^d\). Concentration and the two physical moduli give
\[
 \|f_n-f_n'\|_*
 \le2\mathcal L_Y\sqrt{\log(4N_n/\delta)}
                              +{2(K_t+K_x)\over n}.   \tag{16}
\]
The concentration union costs \(\delta/2\). For each actual path,
use the explicit fitting initialization threshold
\(N_{\rm fit}(\delta/8)\) from its equation (5), and increase width
until its additional source failure is at most \(\delta/8\), including
the deterministic all-time tail allowance. The two bad paths then cost
at most \(\delta/2\). This establishes the stated confidence. The
second threshold is not quantified by the existing stochastic proof.

It remains to envelope (16). By (13)--(15) and
\(1+M\le e^M\),
\[
 2\mathcal L_Y\le
 {\beta^{23L}h^2Y\over\sqrt n}
                              e^{\beta^{44L}hz l_n}.
\]
Equations (6)--(8) also give
\[
 K_t\le\beta^{4L}z,\qquad K_x\le\beta^{4L}z,
 \qquad 2(K_t+K_x)\le\beta^{5L}hY.
\]
Since \(n^{-1}\le n^{-1/2}\) and the square-root logarithm in (16)
is at least one, its tail can be absorbed. The sum is bounded by
\[
 {\beta^{24L}h^2Y\over\sqrt n}
 e^{\beta^{44L}hz l_n}\sqrt{\log(8N_n/\delta)}.
\]
Both \(\beta^{24L}h^2\) and \(\beta^{44L}h\) are at most
\(B=\beta^{100L}h^4\), proving (4). This supplies the coefficient
and confidence calculation completely, conditional only on the stated
fitting/source inputs and (1).

## 6. Finite envelope for the simple Legendre order

For this subsection use the closure's conservative common tube
\(\kappa_c=g/4\), \(R_c=8Y/\sqrt g\), and its activity cap
\(S_c=8z\). All are the existing closure fitting constants, distinct
from the source allowance \(S=16z\). Equation (3) gives
\(R_c\le\beta^{-28L}\), \(S_c\le1\), and
\(a_0=Y/\kappa_c=4z\le1\).

Use \(F_z,P,B_\delta,G,D_\delta,J\) with \(R_c\) replacing
\(R\). The bounds in Section 4 still apply. The checked numerical
Legendre interface defines
\[
 \mathcal A=(1+4GHB_\delta/\kappa_c)e^{E_c},\qquad
 E_c=2J(1+4G^2/\kappa_c)Y/\kappa_c,
\]
\[
 V_z=2F_zB_\delta P,\quad
 V_\delta=T^{L-1}
 [4sH+4sH(L-1)B_\delta^2+Lt_2MV_z],
\]
\[
 F_h=V_h a_0\sqrt{(1+a_0)/2},\qquad
 b_1={2\sqrt{1+a_0}\over\kappa_c}C_cB_\delta,
\]
\[
 b_0={\sqrt{1+a_0}Y\over\kappa_c}V_\delta
                         +2B_\delta\sqrt{a_0},\qquad
 C_f=2H+R_csF_z,
\]
\[
 q_{\rm abs}=4(L-1)F_hD_\delta\sqrt{a_0}\mathcal A,
 \qquad C_n=4(L-1)C_f\mathcal A F_h(b_0+b_1).          \tag{17}
\]
Its proved conclusion, for \(q\ge q_{\rm abs}\), is
\(\|f_{n,q}-f_n\|_*\le C_n\sqrt{\log(eq)}/q^2\).
Here \(V_h,C_c\) are the actual quantitative closure fitting outputs,
not newly assumed response constants.

For completeness their needed envelopes follow directly from that note.
Its \(D_j=sT^{L-j}\) obeys \(D_j\le\beta^{2L}\), and its
energy recurrence has \(C_j\le C_L\le\beta^{16L}\), as verified
in the explicit closure fitting check. Its block speeds are
\[
 T_1=2D_1R_c,\qquad
 T_j=4HD_jR_c+130D_j\sqrt{C_{j-1}S_c}\,R_c^2.
\]
Since \(S_c,R_c\le1\), these satisfy
\(\max_jT_j\le\beta^{13L}R_c\). Unrolling
\(V_1=sT_1\), \(V_j=s(2HT_j+9V_{j-1})\) gives
\(V_h=\max_jV_j\le\beta^{20L}R_c\). Finally
\[
 C_c=4[4H^2+D_1^2R_c^2+
                 4H^2R_c^2\sum_{j=2}^LD_j^2]+g/2
                                      \le\beta^{12L}.
\]

Substitution in (17) gives the following sufficient ledger:
\[
 \begin{aligned}
 C_f&\le\beta^{6L},& V_z&\le\beta^{8L},&
 V_\delta&\le\beta^{13L}(1+M),\\
 F_h&\le\beta^{24L}z^2,&
 F_h&\le\beta^{23L}Y\sqrt h,&
 b_0+b_1&\le\beta^{16L}h(1+M),\\
 \mathcal A&\le\beta^{6L}h e^{E_c},&
 E_c&\le\beta^{21L}hz(1+M),&
 E_c+M&\le\beta^{46L}hz l_n.
 \end{aligned}                                                   \tag{18}
\]
For example, the two bounds on \(F_h\) use respectively
\(R_c=8z\sqrt g\) and \(R_c=8Y/\sqrt g\), together with
\(a_0=4z\). The response-speed bound is its displayed three-term
recursion with \(B_\delta\le1\). The \(b_0,b_1\) bounds use
\(a_0\le1\), \(1/g\le h\). Thus (18) uses neither a new
trajectory estimate nor a hidden coefficient.

Equations (17)--(18), \(1+M\le e^M\), and
\(4(L-1)\le\beta^{2L}\) imply
\[
 q_{\rm abs}\le\beta^{40L}h e^{E_c+M},\qquad
 C_n/Y\le\beta^{53L}h^{5/2}e^{E_c+M}.                \tag{19}
\]
Consequently
\[
 \max(3,q_{\rm abs},C_n/Y)
 \le\beta^{54L}h^3e^{\beta^{46L}hz l_n}
 \le e^{B l_n/4}.                                   \tag{20}
\]
To verify the last elementary comparison, take logarithms and use
\(z\le1\), \(l_n,h\ge1\),
\(54L\log\beta\le\beta^{3L}\), and
\(3\log h\le\beta^Lh\). Their sum is at most
\(\beta^{48L}h l_n\le B l_n/4\).

The previously checked order is
\(\lceil4Q\sqrt{\log(e+Q)}\rceil\), where
\(Q=\max(3,q_{\rm abs},n^{1/4}\sqrt{C_n/Y})\).
Let \(w=B l_n/4\). Equation (20) gives
\(Q\le n^{1/4}e^w\). Since \(B\ge16\), \(w\ge4\), and
\(l_n\le w\),
\[
 \log(e+Q)\le2+l_n^2/4+w\le(w+2)^2,
 \qquad w+2\le e^w/4.
\]
It follows that
\[
 4Q\sqrt{\log(e+Q)}\le n^{1/4}e^{2w}
                                  \le n^{1/4}e^{B l_n}.
\]
Thus (5)'s integer order dominates the checked one. The upper bound
\(C_n\sqrt{\log(eq)}/q^2\) decreases for \(q\ge1\), and the
absorption condition also persists, so its error is at most \(Y/\sqrt n\).
No monotonicity of the actual closure error is presumed.

At fixed nonzero labels and fixed problem parameters,
\[
 q_n=n^{1/4+o(1)},\qquad
 n(d+1)+1+2(L-1)mnq_n=n^{5/4+o(1)}.
\]
The latter counts moving coordinates only. The \((L-1)n^2\) fixed
initialized mixer entries remain retained. The original single source
event and deterministic fitting event cover every order at a fixed width;
no order-dependent probability union is introduced.

## 7. Limits of this check

The algebra certifies the powers 30 and 100 as conservative consequences
of the displayed component bounds, conditional on (1)'s separate check.
It does not establish the user's conjectural strict independent-dense
rate: the exponential in (4) remains width dependent for fixed positive
labels. It neither quantifies the source probability threshold nor
changes the initialized dense ensemble, closure, physical times, or
topology. No file outside this assigned check was edited.
