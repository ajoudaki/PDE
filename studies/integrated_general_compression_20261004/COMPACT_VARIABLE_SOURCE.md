# Variable source accuracy, horizon, and compact-width budgets

2026-10-05. Internal source-count extension in the same study. This note
keeps the corrected-readout optimizer, exact initialization additions,
selection metrics, full recurrence label allowance, and retained-coordinate
contract. It proves the deterministic approximation and selection statements
for arbitrary source accuracy. The larger analytic time domain and variable
accuracy comparison are proved in
[ANALYTIC_TAIL_EXTENSION.md](ANALYTIC_TAIL_EXTENSION.md). Consequently the
results below are conditional on the inherited source and fitting event and
the additional deterministic width gates of that note. The original
stochastic source argument alone does not provide the larger time domain.

The complete inputs used here are `UNBOUNDED_COMPRESSOR_BRIDGE.md`,
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`,
`EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`,
`COMPACT_POLYNOMIAL_COMPARISON.md`, `COMPACT_FULL_LABEL_RANGE.md`,
`COMPACT_SOURCE_ENERGY.md`, `ANALYTIC_TAIL_EXTENSION.md`, the bridge and
runtime checks, and `docs/notation.qmd`. No cross-study references were followed. The required
canonical-notation skill path was unreadable (permission denied); the
available rigorous-math skill and repository notation instructions were
applied. This note is not a promotion review.

## 1. Parameters and the domain actually needed

Let \(L\ge2\), \(d,m\ge1\), and let \(n\) be the dense width. Set
\[
Y=\|y\|_2/\sqrt m>0,\qquad \lambda=\gamma/m>0,\qquad
z=Y/\lambda,\quad S=16z,\quad T_0=32\lambda^{-1}\log(en).
\tag{1}
\]
The dense model, Gaussian initialization, physical-time loss and mobilities
are exactly those of the source bridge. The full label allowance remains
\[
z\le\min\{(8H_d\sqrt{F_d})^{-1},
           (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\tag{2}
\]
Here \(H_d,F_d\) are the dense-fitting constants summarized in
`COMPACT_SOURCE_ENERGY.md` (3), \(H_c,F_c\) are the compact-fitting
constants, and \(S_*^{\rm src}\) is source (10). In particular \(S\le1\).
The source's \(a,U,V\) are its strip width and the original recurrences
(24)--(25), evaluated at the actual \(S\). Define
\[
c_t=\frac{a}{64YSU},\qquad c_q=\min\{1/8,a/(8V)\},
\qquad r_t=c_t/\sqrt{\log(en)},\quad r_q=c_q/\sqrt{\log(en)},
\tag{3}
\]
\[
M_0=10\max\{H_{\max},\max_j\tau_j\},\qquad M_n=M_0\sqrt n,
\qquad B=2m+d+1.
\tag{4}
\]
The source recurrences give all these numbers explicitly, without a bound
on activation values. The normalized dense pairing is \(u^Tv/n\);
selected pairings use their fixed positive metrics \(M_j\).

For \(T\ge T_0\), the required analytic-domain assertion is this:
each of the four source families
\[
h^{(j)}(t,v),\quad W_0^{(j)}h^{(j-1)}(t,v),\quad
\delta^{(j)}(t,v),\quad W_0^{(j+1)T}\delta^{(j+1)}(t,v)
\tag{5}
\]
is holomorphic on a neighborhood of the closed time rectangle obtained
by giving \([0,T]\) horizontal and vertical margins \(r_t\), times
the intrinsic complex sphere tube of radius \(r_q\), and every coordinate
has magnitude at most \(M_n\). For \(d=1\), the queries are the two
points \(-1,1\). The inherited source event establishes this assertion
at \(T=T_0\). Its proof uses a time-net length \(O(\log(en))\);
replacing \(T_0\) by an arbitrary \(T\) inside that probability argument
would require a new justification. The deterministic parameter-ball proof
in `ANALYTIC_TAIL_EXTENSION.md`, Sections 2--3, supplies the displayed
domain assertion simultaneously for every finite \(T\), on the same
event and with width gates independent of \(T\) and \(\epsilon\).

Retain the original construction gates, including
\(n^{-1}\le\min(1,Y,S)\), source (31), and the relevant original
coefficient-count gates. Changing source accuracy within this fixed
domain does not change the source event or its probability threshold.

## 2. Exact count at arbitrary tolerance and horizon

Fix
\[
0<\epsilon\le\epsilon_0:=\min(1,Y,S),\qquad
\alpha_T=\frac{r_t}{4T}\le1.
\tag{6}
\]
The latter inequality follows for \(T\ge T_0\) from the original
\(\alpha_{T_0}\le1\) gate. The time change
\(t=T(1+\cos u)/2\) maps \(|\operatorname{Im}u|\le\alpha_T\)
inside the displayed time rectangle: its imaginary displacement is at
most \(T\sinh(\alpha_T)/2\le T\alpha_T\le r_t/4\), and its real
overshoot is at most \(T(\cosh(\alpha_T)-1)/2\le T\alpha_T^2/2\).

For \(d\ge2\), set
\[
b_d=2d-2,\quad D_d=2^{d+1}d^{d-2},\quad
P_T=\frac{18D_db_d!2^{b_d+1}}{\alpha_T r_q^{b_d+1}},
\qquad H(T,\epsilon)=2\log\frac{16M_nP_T}{\epsilon}.
\tag{7}
\]
The source bridge's Fourier and spherical-harmonic argument, before its
substitution \(\epsilon=1/n\), gives coordinate tail at most
\(\epsilon/16\) outside
\(\alpha_T k+r_qj\le H(T,\epsilon)\). The exact real coefficient
count for one source family is
\[
N(T,\epsilon)=
\sum_{j=0}^{\lfloor H(T,\epsilon)/r_q\rfloor}
\left[{j+d-1\choose d-1}-{j+d-3\choose d-1}\right]
\left[1+\left\lfloor\frac{H(T,\epsilon)-r_qj}{\alpha_T}\right\rfloor\right].
\tag{8}
\]
An impossible binomial coefficient is zero. The time cosine symmetry
explains why the temporal multiplicity is one rather than two. The same
unit-cube enlargement as source (33) yields
\[
N(T,\epsilon)\le
\frac{2[H(T,\epsilon)+\alpha_T+(d-1)r_q]^d}
     {d!\alpha_Tr_q^{d-1}}.
\tag{9}
\]
There are at most four source families per layer. Their coefficient
vectors and the exact initialization additions therefore span spaces of
dimension at most
\[
R(T,\epsilon)\le B+4N(T,\epsilon)
\le B+\frac{2^{15}}{d!}\frac Ua\,z^2(\lambda T)
 c_q^{-(d-1)}[\log(en)]^{d/2}
 [H(T,\epsilon)+\alpha_T+(d-1)r_q]^d.
\tag{10}
\]
The coefficient follows from
\(\lambda^{-1}c_t^{-1}=1024(U/a)z^2\). In particular, using
\(T=T_0\), \(\epsilon=1/n\), and the original bound on the enlarged
radius by \(9\log(en)\), (10) is exactly the existing coefficient
\(2^{20}9^d/d!\) in source (35). No asymptotic replacement of that
coefficient has been made.

For \(d=1\), the temporal cosine coefficient of positive order \(k\)
has magnitude at most \(2M_ne^{-\alpha_Tk}\). Since
\(1-e^{-\alpha_T}\ge\alpha_T/2\), define
\[
H_1(T,\epsilon)=\log\frac{64M_n}{\alpha_T\epsilon},\qquad
N_1(T,\epsilon)=1+\lfloor H_1(T,\epsilon)/\alpha_T\rfloor.
\tag{11}
\]
The omitted tail is at most
\(4M_n\alpha_T^{-1}e^{-H_1(T,\epsilon)}=\epsilon/16\).
The two sphere points and four families give
\[
R(T,\epsilon)\le B+8N_1(T,\epsilon)
\le B+8+2^{15}(U/a)z^2(\lambda T)\sqrt{\log(en)}
                     H_1(T,\epsilon).
\tag{12}
\]
These are finite-width counts, including all temporal zero modes.

Finite quadrature and finite continuation of the initial Taylor jets
approximate the finitely many retained coefficient vectors to any required
positive accuracy. Choose that accuracy so the retained-coefficient error
uses at most the remaining \(15\epsilon/16\). The finite basis has
bounded evaluation norms, so such a choice exists. For each initialized
image pair, apply identical scalar operations to its two members; the
image identity is exact even when its coefficient is only approximated.
The image operator and finite basis are known at setup, so the two
coordinate tolerances can be met simultaneously. No extra coefficient
vector is required. This is precisely the inherited initialization-only
setup contract, with a different finite precision requirement.

## 3. Selection, initialization, and genuine width restrictions

For source-space dimension at most an integer \(R\), the inherited
selection has selected dimensions \(q_j\le9R\), exact source isometry,
and fixed metrics
\[
\mathsf D_j/4\preceq M_j\preceq\mathsf D_j,\qquad
\|1\|_{M_j}=1,\quad \|1\|_{\mathsf D_j}\le2.
\tag{13}
\]
Thus a compact neuron budget \(q<n\) is certified by
\[
9\lceil R(T,\epsilon)\rceil\le q.
\tag{14}
\]
When using the exact integer count \(B+4N\), or \(B+8N_1\), the ceiling
is unnecessary. A slightly sharper sufficient condition is that a real
upper bound on the integer rank be at most \(q/9\): the actual rank is
then at most \(\lfloor q/9\rfloor\). One need not first round the real
upper bound upward. This observation is useful for the continuous
sufficient budgets below.

The initialization additions contain every initialized training feature,
its initialized forward image, the first-weight columns, and the constant.
They preserve the actual initialized training Gram exactly. The selected
initial first-weight and hidden operator bounds are at most eight.
Consequently independent compact fitting applies under exactly (2), for
every positive source tolerance in (6). It gives a globally defined
autonomous runtime, positive normalized training Gram, and exact limiting
training fit. Nothing in this fitting proof requires \(\epsilon=1/n\).

These are sufficient width conditions, not necessary rank formulae.
The positive \(m\)-by-\(m\) training Gram forces \(q_L\ge m\), hence
\(q\ge m\). Exact inclusion of first-weight columns also forces
\(q_1\ge\operatorname{rank}(A_0)\), which is \(\min(n,d)\) almost
surely at Gaussian initialization. More generally each selected dimension
is at least the rank of its exact initialization source space. No theorem
for an arbitrary budget below those ranks follows from selection.

The moving arrays use at most
\[
(L-1)q^2+q(d+1)+m
\tag{15}
\]
scalar coordinates. The all-retained inventory stays
\[
1020(L+1)R^2+10m(d+1).
\tag{16}
\]
When an integer rank \(R\le q/9\) is used, (16) is at most
\(13(L+1)q^2+10m(d+1)\). All original-width jets, source vectors,
quadratures, and dense initialization arrays used during setup are
discarded after selection and formation of the runtime arrays and metrics.
There is no retained source trajectory or residual playback.

## 4. Two useful budget endpoints

First, selection can be applied only to the initialization additions, with
rank at most \(B\). The initialized training features and their images
give the same exact initial forward pass, operators, and Gram as before.
Its corrected optimizer therefore fits independently under (2). No
nonzero-time source approximation is claimed for this simpler construction.
For \(q\ge9B\), it provides the all-time sphere bound
\[
\sup_{t\in[0,\infty],\,v\in S^{d-1}}|f_C(t,v)-f_n(t,v)|
\le (10H_c+4H_d)\frac{Y}{\sqrt\lambda}.
\tag{17}
\]
Indeed the compact feature and effective-readout norms are at most
\(2H_c\) and \(5Y/\sqrt\lambda\), and the dense ones are at most
\(2H_d\) and \(2Y/\sqrt\lambda\). This provides an admissible model
when a requested budget does not fit the analytic coefficient collection.

Second, if \(q\ge n\), retain every dense coordinate and set
\(M_j=\mathsf D_j=I_n/n\). This is exact source isometry on the complete
space. Use the original dense first weights and hidden matrices. To check
that the corrected optimizer is then exactly the dense flow, put
\(c=y-f_n\) and \(w_C=w_n\). Its correction term is zero. The metric
adjoint is the ordinary transpose, all coordinate gates are self-adjoint,
and the hidden and raw-readout equations become precisely the dense
equations, including the factor \(1/n\) in a hidden rank-one update.
The dense residual equation is its prescribed Gram equation. Thus the
dense trajectory solves the corrected system with the same initial state;
uniqueness under the positive Gram margin identifies the two trajectories.
The all-time error is exactly zero, including the endpoint. This branch
uses width \(n\), not \(9n\), and needs no analytic-source event once the
dense and compact fitting inputs hold. It is a full-width limit of the
same specified optimizer, not a retained trained reference signal.

## 5. A one-parameter family with an explicit inverse budget

Use the extended domain established in `ANALYTIC_TAIL_EXTENSION.md` for
every finite \(T\ge T_0\). For \(u\ge0\), choose
\[
T(u)=T_0+4u/\lambda,\qquad \epsilon(u)=\epsilon_0e^{-u}.
\tag{18}
\]
For \(d\ge2\), put \(H_0=H(T_0,\epsilon_0)\),
\(\alpha_0=\alpha_{T_0}\), and
\[
h_0=\max\{8\log(en),H_0+\alpha_0+(d-1)r_q\}.
\tag{19}
\]
Since \(P_T\) is proportional to \(T\),
\[
H(T(u),\epsilon(u))
 =H_0+2u+2\log(1+u/(8\log(en)))\le H_0+9u/4.
\]
Also \(\alpha_{T(u)}\le\alpha_0\). Substitution into (10) gives
\[
R(T(u),\epsilon(u))\le B_*+C_d(h_0+u)^{d+1},\qquad
B_*=2m+d+9,
\tag{20}
\]
\[
C_d=\frac{2^{17}(9/4)^d}{d!}\frac Ua\,
 c_q^{-(d-1)}z^2[\log(en)]^{d/2}.
\tag{21}
\]
For \(d=1\), instead take
\(h_0=\max\{8\log(en),H_1(T_0,\epsilon_0)\}\). Then
\(H_1(T(u),\epsilon(u))\le H_1(T_0,\epsilon_0)+9u/8\), and
(12) proves the same (20)--(21), with its deliberately larger factor
\(9/4\). The extra eight zero modes are included in \(B_*\).

The deterministic comparison on the extended domain supplies
\[
\sup_{t\le T,v}|f_C-f_n|\le A_n\epsilon,
\qquad
\sup_{t\in[0,\infty],v}|f_C-f_n|
 \le A_n\epsilon+D_ne^{-\lambda T/4},
\tag{22}
\]
where \(A_n,D_n\) are independent of \(T,\epsilon\).
`ANALYTIC_TAIL_EXTENSION.md`, Sections 4--5, proves (22) using the
extended real training-carrier bound. The full-range coefficient envelopes
give, for a universal numerical \(C\), the choices
\[
A_n=C\beta^{42L}z(1+\lambda^{-1/2})
           (1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}},\qquad
D_n=C\beta^{9L}z(1+\lambda^{-1/2}).
\]
The existing comparison algebra is linear in source accuracy before its
final substitution; its time-domain extension is a separate proved step.

Define
\[
A=\max\{(10H_c+4H_d)Y/\sqrt\lambda,
                  A_n\epsilon_0+D_ne^{-8\log(en)}\}.
\tag{23}
\]
For every integer \(q\ge18B_*\) with \(q<n\), a width-at-most-\(q\)
construction then satisfies
\[
\sup_{t\in[0,\infty],v}|f_C-f_n|
\le A e^{h_0}
 \exp\left[-\left(\frac{q}{18C_d}\right)^{1/(d+1)}\right].
\tag{24}
\]
For the proof, set
\(u=(q/(18C_d))^{1/(d+1)}-h_0\). If \(u\ge0\), (20) gives
\(R\le B_*+q/18\le q/9\), so exact integer-rank selection fits the
budget, and (18), (22) give error at most \(Ae^{-u}\). If \(u<0\),
use the initialization-only construction and (17); the right side of
(24) exceeds \(A\). No accuracy theorem is inferred by merely inverting
the old bound specialized to \(\epsilon=1/n\).

For example, a requested absolute tolerance \(\varepsilon>0\) is met by
the analytic construction with
\[
u=\max\{0,\log(A/\varepsilon)\},\qquad
q\ge9\big[B_*+C_d(h_0+u)^{d+1}\big],
\tag{25}
\]
with an integer ceiling on the final sufficient budget. If that budget
exceeds \(n\), the exact full-width branch replaces it. Formula (25)
is sufficient; it does not assert optimality of compact width.

## 6. Activation-only rank envelope on the full label interval

Let \(\beta\) be the source envelope and put \(X=\beta^L\ge100\).
The label-independent portions of `SIMPLE_CONSTANTS_SOURCE_CHECK.md`
give
\[
H_{\max},f_*\le X^3,\quad K_{\rm src}\le X^{21},
\quad T_Q\le X^{14},\quad T_J\le X^8,
\quad \max_j q_j^{\rm src}\le X^8,
\quad \max_j b_j^{\rm ang}\le X^3.
\tag{26}
\]
Here \(q_j^{\rm src}\) and \(b_j^{\rm ang}\) are only the source
response and angular coefficients from source (24); neither denotes
selected width or activation intercept. With \(S\le1\),
\[
(H_{j-1}^{\rm src})^2+f_{j-1}^2+ST_Q
          +S^2H_{j-1}^{\rm src}q_{j-1}^{\rm src}\le2X^{14}.
\]
Since \(s\le X\) and \(G_d=16\sqrt{d+3}\), source (25) now gives
\[
U\le X^{37}\sqrt{d+3},\qquad V\le X^{31}\sqrt{d+3}.
\tag{27}
\]
Indeed the higher-layer bounds before absorption are
\(4X^{36}+32\sqrt{d+3}X^8+2\) and
\(32\sqrt{d+3}X^3+4X^{30}+2\), respectively. The first-layer
bounds are smaller. Using \(a^{-1}\le\beta/16\) gives
\[
U/a\le X^{38}\sqrt{d+3},\quad
c_q^{-1}\le X^{32}\sqrt{d+3},\quad M_0\le X^5.
\tag{28}
\]
These are valid throughout (2); they do not use the narrower
\(z\le\beta^{-30L}\) cap needed by the older sharper storage envelope.
Consequently
\[
C_d\le\frac{2^{17}(9/4)^d}{d!}
 \beta^{(32d+6)L}(d+3)^{d/2}z^2[\log(en)]^{d/2}.
\tag{29}
\]
The elementary inequality \(d!\ge(d/e)^d\), obtained by integrating
\(\log x\) on \([1,d]\), implies
\[
\frac{(d!)^{1/(d+1)}}{(d+3)^{d/(2d+2)}}\ge\frac{\sqrt d}{8}.
\]
To see the last numerical constant, use \(d+3\le4d\),
\(d^{1/(d+1)}\le2\), and \(2\sqrt2 e<8\). Also
\((18\cdot2^{17})^{1/(d+1)}\le1536\),
\((9/4)^{d/(d+1)}\le9/4\), and
\((32d+6)/(d+1)\le32\). Thus
\[
\left(\frac q{18C_d}\right)^{1/(d+1)}
\ge\frac{\sqrt d}{32768\beta^{32L}}
 \left(\frac q{(Ym/\gamma)^2[\log(en)]^{d/2}}\right)^{1/(d+1)}.
\tag{30}
\]

For \(d\ge2\), the original source count gates and
\(\epsilon_0\ge1/n\) give \(H_0\le7\log(en)\) and hence
\(h_0\le9\log(en)\). For \(d=1\), the explicit sufficient temporal
gate
\[
\log\frac{8192M_0}{c_t\lambda}\le\log(en)
\tag{31}
\]
gives \(H_1(T_0,\epsilon_0)\le(7/2)\log(en)\), so
\(h_0=8\log(en)\). Here
\((3/2)\log\log(en)\le\log(en)\) for \(\log(en)\ge1\).
Combining (24) and (30), one may first replace \(e^{h_0}\) by
\(e^9n^9\). A weaker exponential rate improves this prefactor to \(en\).
Every construction used in (24), including the analytic construction,
satisfies (17), hence has error at most \(A\). Put
\(D=(q/(18C_d))^{1/(d+1)}\). If \(D\le9\log(en)\), then
\(1\le e^{\log(en)-D/9}\). If \(D\ge9\log(en)\), then
\(9\log(en)-D\le\log(en)-D/9\). Applying respectively the bound \(A\)
or (24) proves the single convenient inequality
\[
\sup_{t\in[0,\infty],v}|f_C-f_n|
\le enA\exp\left[-\frac{\sqrt d}{294912\beta^{32L}}
 \left(\frac q{(Ym/\gamma)^2[\log(en)]^{d/2}}\right)^{1/(d+1)}\right].
\tag{32}
\]
This holds for every integer \(q\ge18B_*\), with the exact full-width
branch when \(q\ge n\). Since \(H_d\le\beta^{2L}\),
\(H_c,\sqrt\lambda\le\beta^{3L}\), the initial-only cap in (23)
is at most \(14\beta^{6L}z(1+\lambda^{-1/2})\). Using (22) and
\(1+\sqrt{\log(en)}\le e^{\sqrt{\log(en)}}\), a universal numerical
\(C\) therefore gives the explicit form
\[
\sup_{t\in[0,\infty],v}|f_C-f_n|
\le C\beta^{42L}Y\frac m\gamma
 \left(1+\sqrt{\frac m\gamma}\right)n e^{65\sqrt{\log(en)}}
 \exp\left[-\frac{\sqrt d}{294912\beta^{32L}}
 \left(\frac q{(Ym/\gamma)^2[\log(en)]^{d/2}}\right)^{1/(d+1)}\right].
\tag{33}
\]
All models in this statement fit the training labels at the limit and
remain autonomous. The unknown stochastic source threshold remains visible
and is not claimed polynomial. This bound is a sufficient width-error
tradeoff, not a claim of an optimal exponent or constant.

For zero labels, the original and compressed predictors are identically
zero. That case does not use the formulas dividing by \(Y\).
