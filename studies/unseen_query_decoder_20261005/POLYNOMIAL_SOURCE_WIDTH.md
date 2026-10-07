# Removing the exponential deterministic analytic-source gate

2026-10-07. Scoped author derivation for the current study. The result is a
deterministic repair of PHYSICAL_PARAMETER_ACCOUNTING.md (28), conditional
on the same fitting and stopped insertion/source inputs. It is not a
polynomial stochastic sufficient-width theorem, a complete decoder theorem,
an independent review, or promotion. No experiments or Git mutation were
performed.

The physical source can use the smaller time-radius coefficient
\[
 c_{\rm safe}=\frac{1}{\beta^{100L}(1+\lambda)},\qquad
 \lambda=\gamma/m.
 \tag{1}
\]
Here \(\gamma>0\) is the unweighted final-layer population covariance
gap defined in Section 1.
Every short-contour condition in accounting (28) then holds for every
integer \(n\ge1\). The old Taylor solver already uses patches eight times
smaller than one eighth of the resulting normalized radius, so its actual
patch length, field count, and gap powers do not worsen. The source proof's
unquantified probability limit remains a separate gap.

## 1. Preserved model and precise input boundary

Let \(L\ge2\) be any fixed hidden depth, \(m\ge d\ge1\), and let
\(v_a=x_a/\sqrt d\in S^{d-1}\) be the given full-rank sphere data.
The argument below also works without the rank assumption. Every hidden
layer has width \(n\). With \(A\in\mathbb R^{n\times d}\),
\(W^{(j)}\in\mathbb R^{n\times n}\) for \(2\le j\le L\), and
\(w\in\mathbb R^n\), the actual network is
\[
 z_a^{(1)}=Av_a,\quad z_a^{(j)}=W^{(j)}h_a^{(j-1)},\quad
 h_a^{(j)}=\phi_j(z_a^{(j)}),\quad f_a=w^\top h_a^{(L)}/n.
 \tag{2}
\]
The independent initialized entries of \(A\) and \(W^{(j)}\) have
laws \(N(0,1)\) and \(N(0,1/n)\), respectively; \(w(0)=0\).
For residuals \(r_a=f_a-y_a\), the loss is
\(\mathcal L=m^{-1}\sum_a r_a^2\). All layers train with the original
mobilities \((n,1,\ldots,1,n)\). Define the residual-free backward pass by
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The unchanged physical equations are
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(j)}=-\frac2{mn}\sum_a
                 r_a\delta_a^{(j)}h_a^{(j-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{3}
\]
For the learned displacement
\(u=(A-A_0,W^{(2)}-W_0^{(2)},\ldots,W^{(L)}-W_0^{(L)},w)\),
use the original physical sum norm
\[
 \|u\|_\Sigma=\|A-A_0\|_F/\sqrt n+
    \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n.
\]

The activations are real on the real line and holomorphic in
\(|\operatorname{Im}z|<a\), with bounded first derivative there. Their
values may be unbounded. Use exactly the accounting envelope
\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
  \max_{j,\,1\le q\le2}\sup_{|\operatorname{Im}z|<a/2}
                 |\phi_j^{(q)}(z)|\right\},\qquad B=\beta^{100L}.
 \tag{4}
\]
Define \(Q^{(0)}_{ab}=v_a^\top v_b\) and
\(Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)]\) for
\(Z\sim N(0,Q^{(j-1)})\). The unweighted gap is
\(\gamma=\lambda_{\min}(Q^{(L)})>0\), and \(\lambda=\gamma/m\).
Linear growth of \(\phi_j\), implied by (4), makes these expectations
finite.
Write
\[
 r=\lambda^{-1}=m/\gamma,\quad
 Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le S_*^{\rm src}\le1,
 \quad \ell=\log(en).
 \tag{5}
\]
The numerical proof uses \(\bar u(\tau)=u(\tau/\lambda)/Y\)
and \(\tau=\lambda t\), without changing (3).
The scalar \(r\) is distinct from a sample residual \(r_a\). Retain
the full original intersection of fitting and source label allowances.
In particular, do not replace it by the optional stronger label cap of
GENERAL_TRAJECTORY_LOWER_BRIDGE.md (5). If \(Y=0\), (3) gives the
stationary zero predictor, separately from every formula dividing by \(Y\).

The allowed scientific inputs are exactly the eight files listed in
Section 8. All were read completely. Links to further scientific files
were not followed. The fitting theorem and finite-query source theorem
are inherited at their stated claim levels. The complete local insertion
proof and its probability constants are absent from the allowed packet;
their absence is material in Section 7. Required research, rigorous-proof,
canonical-notation, and neural-network instructions were applied. Scoped
input rules replace ordinary author startup; no other study material,
new route, or another agent's findings was read.

## 2. All coefficients needed by the deterministic gate

For clarity, recall the source quantities actually used. Let
\(b=\max_j|\phi_j(0)|\), let \(s\ge1\) bound the first half-strip
derivatives, and let \(t\ge1\) bound the second derivatives. On operator
caps ten and query norm at most two, the source recurrences are
\[
 H_1=\max(1,b+20s),\quad H_j=\max(1,b+10sH_{j-1}),
\]
\[
 k_L=H_L,\quad k_j=10s k_{j+1},\quad \tau_j=sk_j,
 \qquad P_1=3,\quad P_j=H_{j-1}+10sP_{j-1}+1.
 \tag{6}
\]
Here \(H_j\) bounds feature RMS, \(Sk_j\) bounds carrier RMS,
\(S\tau_j\) bounds backward-response RMS, and \(P_j\) bounds
preactivation derivatives in the source's normalized parameter norm.
Accounting (9) and direct substitution in (6) give
\[
 H_j,P_j\le\beta^{3L},\quad k_j\le\beta^{5L},\quad
 \tau_j\le\beta^{6L},\quad
 U_{\rm fin}(S)\le\beta^{72L}\quad(0<S\le1).
 \tag{7}
\]
The last bound is the full-label finite-query response recurrence of
accounting (10); its definition is lower-bridge (9). It is not the
stronger-cap estimate \(\beta^{26L}\).

The normalized complex residual Gram and physical hidden increments use
\[
 \mathcal K=H_L^2+S^2\left[\tau_1^2+
                   \sum_{j=2}^L\tau_j^2H_{j-1}^2\right],\qquad
 D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\}.
 \tag{8}
\]
Since \(L+1\le\beta^L\), (7) gives the convenient bounds
\[
 \mathcal K\le\beta^{20L},\qquad D_W\le\beta^{9L}.
 \tag{9}
\]
For example, every squared hidden gradient bound in (8) is at most
\(\beta^{18L}\); at most \(L+1\) such terms occur. Also
\(\lambda\le H_L^2\le\beta^{6L}\), since a covariance's least
eigenvalue is at most its diagonal and the source feature RMS bounds
dominate the population second moments. These bounds are finite
polynomials in \(\beta^L\).

## 3. Radius choice closes the contour checks at every width

The finite-query theorem permits any fixed coefficient
\[
 0<c\le c_{\max}(S)=\frac{a}{64YSU_{\rm fin}(S)}
                  =\frac{a}{4\lambda S^2U_{\rm fin}(S)},
 \qquad r_t=\frac c{\sqrt\ell}.
 \tag{10}
\]
Its physical-time rectangle extends the real interval
\([0,32r\ell]\) by \(r_t\) in each real and imaginary direction.
The original convenient choice \(c=\chi(S)/\lambda\), where
\(\chi(S)=\min\{1,a/(4S^2U_{\rm fin}(S))\}\), was accompanied by
\[
 \sqrt\ell\ge c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
 \tag{11}
\]
Squaring and exponentiating (11) can require width exponential in
\(r^2\). This is a requirement of that radius choice, not a lower
bound on the width needed by the physical source.

Take \(c=c_{\rm safe}\) from (1). To check (10), use
\(64YS=4\lambda S^2\), \(S\le1\), (7), and \(4/a\le\beta/4\):
\[
 \frac{c_{\rm safe}}{c_{\max}}
 =\frac{4\lambda S^2U_{\rm fin}(S)}{aB(1+\lambda)}
 \le\frac{\lambda\beta^{73L}}{B(1+\lambda)}<1.
 \tag{12}
\]
All four terms in (11) are at most one, independently of \(n\):
\[
 \begin{aligned}
 8c_{\rm safe}&\le8/B<1,\\
 \lambda c_{\rm safe}&\le B^{-1}<1,\\
 \frac{4\mathcal Kc_{\rm safe}}{\log2}
     &\le\beta^{21L}/B<1,\\
 32YSD_Wc_{\rm safe}
     &=\frac{2\lambda S^2D_W}{B(1+\lambda)}
       \le\beta^{10L}/B<1.
 \end{aligned}
 \tag{13}
\]
The numerical absorptions use \(\beta\ge10\), \(L\ge2\), so
\(\beta^L\ge100>4/\log2\). Since \(\sqrt\ell\ge1\), (11)
is automatic for every \(n\ge1\).

Here are the underlying domain checks, so the substitution does not rely
only on the syntax of a width gate. On the source's stopped complex tube,
the residual equation has norm growth at most \(2\mathcal K\).
Follow the real solution to its nearest real anchor, then at most two
short pieces of total length \(2r_t\). Consequently
\[
 \rho(z)\le \rho(t_*)e^{4\mathcal Kr_t}\le2\rho(t_*),
 \qquad \rho=\|f-y\|_2/\sqrt m.
 \tag{14}
\]
The same bound controls the nonpositive real variational base on the
short complex pieces by absolute norm; no complex positivity is claimed.
The extra activity \(\int2\rho|dz|\) is at most
\(8Yr_t\le S/2\), because \(\lambda r_t\le1\). Hidden and
normalized first-weight increments are at most
\(8YSD_Wr_t\le1/4\), preserving operator caps ten.

For a fixed training query, the stopped response estimate is
\(\|R_a^{(j)}\|_\infty\le SU_{\rm fin}\sqrt\ell\), with
\(R_a^{(j)}=D_\Theta z^{(j)}\nabla_\Theta(nf_a)\) and
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
The exact equation
\(\partial_tz^{(j)}=-(2/m)\sum_a r_aR_a^{(j)}\), followed by
Cauchy--Schwarz over samples, gives
\(\|\partial_tz^{(j)}\|_\infty\le4YSU_{\rm fin}\sqrt\ell\).
The two pieces thus change a preactivation by at most
\[
 8YSU_{\rm fin}c_{\rm safe}\le a/8.
 \tag{15}
\]
There is no complex query segment in this finite-query construction.
The existing full and cavity pole-stop margins are therefore strictly
improved. Shrinking the domain also preserves every maximum, RMS, and
holomorphy bound supplied on that stopped domain.

These estimates rerun the deterministic part of lower-bridge Sections
2--3 at the new fixed coefficient. Its asymptotic probability argument
is valid at any such fixed coefficient, but does not become quantitative
through this substitution.

## 4. The existing numerical patches already fit

Under normalized time \(\tau=\lambda t\), the repaired radius is
\[
 r_{\tau,\rm safe}=\lambda r_t
       =\frac1{B(1+r)\sqrt\ell}.
 \tag{16}
\]
Thus an assertion \(r_\tau^{-1}\le B\sqrt\ell\) about the old
source domain must be replaced by
\(r_{\tau,\rm safe}^{-1}=B(1+r)\sqrt\ell\). One cannot silently
retain the old domain while deleting its gate.

In SANE_TAYLOR_SOURCE (16), FAST_TAYLOR_NOISE (8), and
GAP_DEGREE_REFINEMENT (8), the actual old patch length was already
\[
 h_0=\frac1{64B(1+r)\sqrt\ell}.
 \tag{17}
\]
Indeed its two other candidates, \(1/8\) and \(r_\tau/8\), are
at least \(h_0\), because the old lower bound was
\(r_\tau\ge1/(B\sqrt\ell)\). After (16),
\[
 r_{\tau,\rm safe}/8=8h_0,\qquad 4h_0=r_{\tau,\rm safe}/16.
 \tag{18}
\]
The new minimum is still exactly \(h_0\). The equal-patch ceiling
convention is therefore unchanged, as are all disks of radius \(4h_j\).
The smaller domain still contains their neighborhoods with strict slack.
The local centered-activation estimate FAST_TAYLOR_NOISE (13) uses
\(h_j\le h_0\) directly, and remains identical.

Retain the explicit horizon
\[
 T=2\{a_0\log n+\log(1+66Br)\},\qquad 1\le a_0\le12.
\]
The existing gate
\[
 n\ge\max\{1,e^{-1}\sqrt{1+66Br}\}
 \tag{19}
\]
implies \(T<32\ell\); it is polynomial in \(B,r\). Consequently
the physical source never needs a later stochastic domain. Parameter
accuracy through \(T\), the ordinary real whole-sphere forward bound,
and the real fitting tail prove the same all-time whole-sphere predictor
accuracy as before. Complex analyticity is used for the finitely many
training queries only. The dense dynamics, real query set, labels, and
physical training clock have not changed.

In particular, retaining \(Y\ge n^{-1}\) for the moment, the
GAP_DEGREE_REFINEMENT physical bounds stay
\[
 R\le C\{d+mLB^2(1+r)Z^2\sqrt\ell\},\qquad
 K+b_\sigma+b_{\rm value}+b_{\rm work}\le CBZ,
 \tag{20}
\]
where \(Z=(a_0+1)\ell+\log(e+B(1+r)(m+d+2))\).
This is a substitution in the physical source result. Its external
scalar-forcing and finite-packet interfaces are still external; (20)
does not independently certify a full decoder.

## 5. Separate treatment of small nonzero labels

There are three distinct uses of \(n^{-1}\le Y\), which must not
be conflated.

First, none of (12)--(18), the thin parameter tube of SANE_TAYLOR_SOURCE
Section 2, or the forcing inequalities FAST_TAYLOR_NOISE (22)--(29)
requires that lower bound. They use \(Y>0\), \(S/Y=16r\), the
original upper label allowance, and explicit error tolerances. In
particular, that note's small local forcing cap is
\[
 \delta_0=\frac{\beta^{-150L}S q_T}{(1+r)^2\sqrt n},
 \qquad q_T=2^{-\lfloor T/4\rfloor}.
 \tag{21}
\]
It stays positive at every \(Y>0\).

Second, the lower bound is used in precision simplifications. Instead set
\[
 Z_Y=Z+\log_+(Y^{-1}),\qquad \log_+x=\max\{0,\log x\}.
 \tag{22}
\]
Since \(S=16Yr\) and \(r^{-1}=\lambda\le\beta^{6L}\),
\[
 \log_+(S^{-1})\le\log_+(Y^{-1})+6L\log\beta,
 \qquad \log(\delta_0^{-1})\le CZ_Y.
 \tag{23}
\]
Keep the exact local-tolerance construction. To specify the degree
without an implicit reference, the GAP_DEGREE_REFINEMENT inputs are
\[
 \begin{gathered}
 c_L=\sqrt{L+1},\quad M=B(1+r),\quad
 E_+=9\beta^{80L}(1+S\sqrt\ell),\\
 d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n},\quad
 \epsilon=\min\{d_n/(2^{12}c_L),n^{-a_0}/(2^{12}Bc_L)\},\\
 C_N=B^2(1+r)^2\sqrt\ell,\quad
 \delta=\min\left\{\delta_0,
   \frac{\epsilon e^{-4E_+-10}}{2^{20}C_N(T+1)}\right\}.
 \end{gathered}
 \tag{23a}
\]
Here \(d_n\) is a radius in the normalized displacement sum norm;
the physical parameter radius is \(Yd_n\). The positive quantity
\(\delta\) is a local arithmetic/forcing tolerance, distinct from the
confidence parameter introduced in Section 7. For a positive integer
patch count \(H\), define
\[
 \begin{split}
 \mathfrak k(H)=8+\left\lceil
 \frac{4E_++\log[2^{20}(c_L+1)(M+1)(T+1)/\epsilon]
          +\log(1+16c_LH)}{\log2}\right\rceil.
 \end{split}
 \tag{23b}
\]
If \(H_0\) is the old certified integer patch count, take
\(K_0=\max\{\mathfrak k(H_0),
8+\lceil\log_+(Y^{-1})/\log2\rceil\}\). This gives
\(K_0\le CBZ_Y\).

For small labels there is a separate arithmetic issue: raising \(K\)
without changing \(H\) can violate the old estimate \(K\le CH\).
Use the following finite refinement when retaining that arithmetic bound:
\[
 H_1=\max\{H_0,4K_0\},\qquad h_j=T/H_1,
 \tag{23c}
\]
and set \(K_1=\max\{\mathfrak k(H_1),
8+\lceil\log_+(Y^{-1})/\log2\rceil\}\). Only
\(\log(1+16c_LH)\) changes.
Because \(H_1/H_0\le4K_0\), accounting for the ceilings gives
\[
 K_1\le K_0+\log_2(4K_0)+2\le2K_0\le H_1
 \quad(K_0\ge8).
 \tag{23d}
\]
If \(H_1=H_0\), the degree is unchanged and \(K_1=K_0\le H_1/4\);
otherwise \(H_1=4K_0\), which justifies the last inequality. The
inequality \(\log_2(4K_0)+2\le K_0\) holds at eight and its
right-minus-left derivative is positive thereafter. There is no implicit
degree/patch fixed point.

All patches shorten, preserving every source disk, tube, and contraction.
The left sum of the decreasing activity cap stays at most nine. Moreover
\[
 H_1\le CB(1+r)Z_Y\sqrt\ell,\qquad
 h_j^{-1}=H_1/T\le CB(1+r)Z_Y\sqrt\ell.
 \tag{23e}
\]
For the second inequality, \(T>1\): indeed
\(Br\ge\beta^{94L}\), using \(r^{-1}\le\beta^{6L}\).
The new inverse-step factor adds only \(O(\log Z_Y)\) to local
precision requirements. Enlarging the Taylor degree only decreases the
truncation tails. It also permits the interpolation degree \(J\), whose
lower bound includes \(\log\delta^{-1}\), to remain \(O(K_1)\).
Write \(K=K_1\) and \(H=H_1\) for this optional small-label branch.
The old proof then gives the safe envelopes
\[
 R\le C\{d+mLB^2(1+r)Z_Y^2\sqrt\ell\},\qquad
 K+b_\sigma+b_{\rm value}\le CBZ_Y.
 \tag{24}
\]
The training horizon is unchanged. The field-error conversion uses
\(S/Y=16r\), so its amplification still has no inverse-label power.
The refinement also preserves the row-work check in FAST_TAYLOR_NOISE
(40): for \(N=mLH\), \(K\le H\le N\) gives
\(NK^3\le(NK)^2\), while \(R\) dominates \(NK\). Thus its
\(O(R^2)\) activation-arithmetic bound survives with \(Z_Y\); this
does not include a black-box activation-value evaluator's work.

For physical coefficient arithmetic, replace FAST_TAYLOR_NOISE (31a)
by the explicitly stronger requirement
\[
 \rho_{\rm arith}\le
 \frac{\min\{1,Y\}\,\delta}
 {C4^K(n+1)^3[B(1+r)(R+K+1)]^C}.
 \tag{25}
\]
Its previous coordinate-to-normalized-state conversion replaced a factor
\(Y^{-1}\) by \(n\). The added factor \(\min\{1,Y\}\) pays
for \(Y^{-1}\) directly, with the old powers of \(n+1\) left
as slack. Hence its logarithmic working precision is at most \(CBZ_Y\).
The displayed root-coupling target GAP_DEGREE_REFINEMENT (41) already
contains a factor \(Y\); keeping it exactly also costs only
\(O(\log_+(Y^{-1}))\) extra bits. That note's displayed scalar-pair
interface has a local magnitude bound polynomial in \(Y^{-1}\);
its substitution similarly adds \(O(\log_+(Y^{-1}))\), conditional
on that interface. Its unprovided scalar-forcing proof is not reconstructed
here.

For a source-pairing application that separately requires coordinate
tolerance \(\epsilon\le\min\{1,Y,S\}\), choose
\[
 \epsilon_{\rm src}=\tfrac14\min\{n^{-1},Y,S\}.
 \tag{26}
\]
It is still at most the requested \(1/n\), and
\(\log\epsilon_{\rm src}^{-1}\le CZ_Y\). Both \(Y\) and \(S\)
must be included: \(n^{-1}\le Y\) alone need not imply
\(n^{-1}\le S\) when \(\lambda>16\). The exact coefficient-count
and quadrature formulas must use the chosen tolerance; an asymptotic count
derived after setting \(\epsilon=1/n\) cannot simply be reused without
this substitution.

Third, the source probability proof compares cavity budgets with a factor
\(\exp\{\eta o(1)(1+1/S)\}\) and uses fixed-label asymptotics.
Removing a numerical precision gate does not bound this term at finite
width. Thus (22)--(26) remove the numerical need for \(Y\ge1/n\);
they do not prove stochastic uniformity as \(Y\downarrow0\). If the
old scientific statement is imported literally, retain its explicit
polynomial gate \(n\ge Y^{-1}\) until its probability proof is supplied
and quantified. Either convention is compatible with the deterministic
radius repair.

## 6. Related late-time and source-count gates

The Taylor route needs only (19) and the real fitting tail. For completeness,
the two extra deterministic gates in ANALYTIC_TAIL_EXTENSION can themselves
be made polynomial; they need not be treated as opaque eventual conditions.
This paragraph concerns the training-query version of that extension,
with the repaired \(r_t=c_{\rm safe}/\sqrt\ell\).

Let \(P_*=\max_jP_j\) and define
\[
 A_{\rm tail}=2Y\sqrt r+8Y\sqrt{\mathcal K}\,c_{\rm safe},
 \qquad
 b_n=\min\{1/4,SH_L/4,a/(8\sqrt n P_*)\}.
 \tag{27}
\]
The left side of the extension's parameter-ball gate (7) is at most
\(A_{\rm tail}n^{-16}\). It is strictly smaller than \(b_n/2\)
under the sufficient conditions
\[
 n\ge\max\left\{1,(16A_{\rm tail})^{1/16},
       \left(\frac{16A_{\rm tail}}{SH_L}\right)^{1/16},
       \left(\frac{32A_{\rm tail}P_*}{a}\right)^{2/31}\right\}.
 \tag{28}
\]
Indeed the three nontrivial terms bound the left side by, respectively,
\(1/16\), \(SH_L/16\), and \(a/(32\sqrt nP_*)\), which are
the three candidates for \(b_n/4\). The exact \((en)^{-16}\)
factor gives additional slack.

For the carrier-tail coefficient use that extension's finite recurrence
\[
 C_L^k=1,\qquad C_j^k=S\tau_{j+1}+10sC_{j+1}^k
                   +10tSP_{j+1}k_{j+1},\qquad
 C_{\rm tail}=\max_jC_j^k.
\]
It obeys \(C_{\rm tail}\le\beta^{20L}\) by (7), one downward
geometric sum, and \(10s\le\beta^2\). The extension's (9b) is
implied by
\[
 n\ge\max\left\{1,
  \left(\frac{2C_{\rm tail}Y\sqrt r}{K_{\rm src}S}\right)^{1/15}
                       \right\}.
 \tag{29}
\]
This follows by replacing \((en)^{-16}\) by \(n^{-16}\) and
\(\sqrt\ell\) by its lower bound one. Here \(K_{\rm src}\ge1\)
is the original carrier maximum coefficient.

These expressions do not hide inverse-label powers:
\[
 \frac{A_{\rm tail}}{SH_L}
 =\frac1{8H_L\sqrt r}
       +\frac{\sqrt{\mathcal K}c_{\rm safe}}{2rH_L},\qquad
 \frac{2C_{\rm tail}Y\sqrt r}{K_{\rm src}S}
 =\frac{C_{\rm tail}}{8K_{\rm src}\sqrt r}.
 \tag{30}
\]
Use \(r^{-1}\le\beta^{6L}\), \(H_L\ge1\), (9),
\(a^{-1}\le\beta/16\), and \(Y=S/(16r)\) to bound all terms
in (28)--(29) polynomially in \(\beta^L\). No smaller label cap
is used. Their precise displayed maxima are preferable to an unnecessarily
large rounded power envelope.

Other source qualifications have different roles. The variational cap in
UNBOUNDED_COMPRESSOR_BRIDGE Section 3 can also be checked explicitly.
Its original source allowance gives \(SA_*\le1/4\) and
\(D_*S^2/\eta\le1/4000\), so the displayed propagator bound is
at most
\[
 2e^{1/4}(2\mathcal Bn)^{1/4000}.
\]
It is below \(n^{1/1000}\) whenever
\[
 n\ge(2e^{1/4})^{4000/3}(2\mathcal B)^{1/3},
 \qquad\mathcal B=1024e^2L.
 \tag{30a}
\]
The large first factor is numerical; it has no hidden label, gap,
activation, or sample dependence. Here \(A_*,D_*,\eta,\mathcal B\)
are precisely that source's (7)--(10), used only through the two displayed
inequalities. Thus no separate exponential parameter gate is concealed
in this variational absorption.

The old
UNBOUNDED_COMPRESSOR_BRIDGE Section 7 assumption
\(\ell\ge\max\{e^2,2\mathcal B\}\), where
\(\mathcal B=1024e^2L\), is not an exponential-in-gap requirement.
Even literally it needs only \(n\ge\exp(CL)\), a fixed power of
\(\beta^L\). It can also be avoided in its interpolation calculation
by taking \(p=\max\{4,\log(2\mathcal B\ell)\}\) and retaining
\(\log(2\mathcal B)\), instead of bounding it by \(\log\ell\).

The spherical count simplifications in that source's (34) are not needed
by the finite-training-query Taylor source. In a construction that uses
them, retaining the exact positive radius, exact logarithm \(H\), and
exact sum (33) avoids their eventual-width simplifications. It does not
remove the dimension dependence of a spherical coefficient count. No
claim about a full passive-query decoder follows from this observation.

## 7. The exact remaining stochastic bridge

The repaired deterministic radius and polynomial horizon gate do not give
an explicit high-probability source event. The permitted source packet
still has the following unresolved inputs:

| Input in the existing proof | What an effective theorem needs |
|---|---|
| Fixed-deletion coordinate error \(O_p(n^{-1/30})\) | A finite-width tail bound, with constants in depth, activation bounds, labels, sample count, deletion count, and confidence |
| Projected common-cavity errors \(C_p n^{-49/100}\) in Gaussian radius | Explicit growth of \(C_p\) and finite-width exceptional probability |
| Control-uniform insertion and centered-form events | Explicit covering and derivative bounds on the repaired domain, with no hidden eventual absorption of parameter factors |
| Budget removal \(\limsup_n\Pr(\mathrm{hit})\le mL(16L/\mathcal B)^p\) | A quantified remainder valid for the confidence-dependent integer \(p\) |
| Complex-minus-real Gaussian corrections tending to zero | Quantitative means and exponential moments at those same orders |

For example, putting \(\vartheta=16L/\mathcal B<1\), the main
moment term is at most \(\delta/2\) for
\[
 p\ge\left\lceil
       \frac{\log(2mL/\delta)}{\log(1/\vartheta)}\right\rceil.
 \tag{31}
\]
The source proves only a limit for each fixed \(p\). It supplies no
bound on the finite-width remainder at (31). Choosing this \(p\) is
not a proof of a width polynomial in \(\log(1/\delta)\). Even a
remainder \(C_p n^{-c}\) would be insufficient without suitable
control of \(C_p\), and may give algebraic \(1/\delta\) dependence
rather than polynomial \(\log(1/\delta)\) dependence.

Likewise, deleting the small-radius width gate does not quantify the
initialization fitting probability. GENERAL_EXPLICIT_FITTING (5) uses a
sphere-net cardinality directly and Chebyshev tails; its displayed
threshold has exponential dimension and inverse-confidence dependence.
Improving that different input requires a separate concentration proof.
No assertion about that repair is made here.

Accordingly the present positive conclusion is exact under the inherited
stopped-source estimates: the contour gate is removed and no new
exponential width cost is introduced in the physical solver. The complete
target of a sufficient width polynomial in \(m,d,\gamma^{-1},\beta^L\),
and \(\log(1/\delta)\), with stated label dependence, remains open
until the quantitative stochastic inputs above and the fitting event are
proved. An independent check of this deterministic repair cannot replace
those missing source estimates.

## 8. Counterchecks, claim status, and frozen inputs

The algebraic checks performed in this derivation were:

- Substitute \(S=16Y/\lambda\) into every radius gate, preserving the
  uncapped \(\lambda\); (13) is valid also when \(\lambda>1\).
- Check separately residual growth, activity, operator margin, and pole
  margin on the two short contour pieces; no long horizontal complex
  contour or complex Gram positivity was used.
- Compare the actual minimum defining \(h\), not only asymptotic patch
  counts; (18) proves equality of the old and new numerical patch lengths.
- Keep the full recurrence-based labels and the \(\beta^{72L}\)
  finite-query response envelope; no small-label specialization was used.
- Test \(Y\downarrow0\): the repaired radius remains finite and the
  numerical cost gains \(\log_+(1/Y)\), while the stochastic comparison
  still has explicit unresolved \(1/S\) sensitivity. At \(Y=0\), use
  the exact stationary branch.
- Test \(n=1\): the contour gate is automatic, but initialization and
  scientific source events are not thereby asserted at width one.
- Check the passive-query scope: only training queries need complex time
  control for this physical solver; real parameter-to-output bounds and
  the fitting tail remain uniform on the whole sphere and for all time.
- Retain every missing stochastic interface as a gap; no probability is
  inferred from a deterministic width inequality.

These are author algebraic and source-correspondence checks, not a fresh
independent review. The radius substitution and optional numerical
small-label replacement are candidate proved deterministic implications
of the stated interfaces. The polynomial stochastic-width claim is open.
The result supersedes only the necessity of the large-radius gate for
this physical Taylor witness; it does not invalidate that original gate
as a sufficient condition for its larger domain.

Source hashes recorded by `sha256sum` before writing this file:

| Complete input | SHA-256 |
|---|---|
| PHYSICAL_PARAMETER_ACCOUNTING.md | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| SANE_TAYLOR_SOURCE.md | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| GAP_DEGREE_REFINEMENT.md | `78e209842b99ac054659bf32a2dd9e77ed9fef26af6047d209312152aa619875` |
| FAST_TAYLOR_NOISE.md | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| ../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |
| ../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md | `f3e277e9591be6e48357a13217927c05bcc2c59843a26a3fa5423ae5afc4c7d8` |
| ../integrated_general_compression_20261004/GENERAL_EXPLICIT_FITTING.md | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| ../integrated_general_compression_20261004/ANALYTIC_TAIL_EXTENSION.md | `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349` |

Initial shared HEAD was `e0d0908797a63512b8f91ce234c4597249f8a2ec`.
The shared checkout already had unrelated changes and untracked research;
they were inspected only as Git metadata and preserved. Only this assigned
file was written. The parent task owns shared study-record updates.
