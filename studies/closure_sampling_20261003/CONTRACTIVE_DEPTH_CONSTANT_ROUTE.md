# Contractive nonlinear gains remove the extra exponential depth constants

2026-10-04. Scoped independent candidate, frozen before scientific exchange.
This is an internal derivation conditional on the current study's stated
local insertion, source-selection, and corrected-readout runtime interfaces.
It is not a promotion review. No experiment, other-study read, Git mutation,
or maintained-book change was made.

Complete assigned scientific inputs read: INPUT_DIMENSION_REFINEMENT.md,
LABEL_DEPTH_RESCALING_ROUTE.md, EXPLICIT_SOURCE_CONSTANTS_ROUTE.md,
DEPTH_CONSTANT_SEPARATION.md, EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md,
SPHERICAL_SOURCE_DIMENSION_ROUTE.md, and DEPTH_INDEPENDENT_EXPONENT.md.
Their references outside this study were not followed. Required
canonical-notation/neural, rigorous-proof, and research-contract/audit
instructions were applied. This candidate derives replacement recurrences
where the old envelopes used derivative bounds at least one.

The positive result is for an explicit subclass, not arbitrary strip-bounded
activations. Every hidden layer remains nonlinear and trainable. The
structural radius constant becomes independent of depth; the sufficient
label coefficient and runtime error constant become polynomial in depth.
The actual data Gram gap remains visible. For the example below that gap
can, and necessarily does in a stated upper-bound sense, collapse with
depth. Thus this is not an overall depth-polynomial theorem at a fixed
absolute label scale.

## 1. Model, subclass, and result

Let L>=2, d,m>=1, and let v=x/sqrt(d) range over the unit sphere.
The width-n dense network is

\[
z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad f_n=w^\top h^{(L)}/n.
\]

The middle recurrence starts at layer two. Entries of A(0) are independent
N(0,1), hidden mixer entries are independent N(0,1/n), the blocks are
independent, and w(0)=0. For training inputs v_a and labels y_a set

\[
r_a=f_n(v_a)-y_a,\quad Y=\|y\|_2/\sqrt m,\quad
k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},\quad
k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

The loss is m^-1 sum_a r_a^2. Its prescribed mobilities
(n,1,...,1,n) give physical-time dynamics

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(\ell)}=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}
h_a^{(\ell-1)\top},\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{1}
\]

Take at every hidden layer

\[
                 \phi_\ell(z)=c\tanh z,\qquad 0<c\le1/40.
\tag{2}
\]

More generally, the argument uses only value bound one on |Im z|<1,
complex derivative bounds s<=1/20 and t<=1/10 on |Im z|<=1/2, and real
derivative bounds |phi'|<=1/40, |phi''|<=1/20. All layers satisfying
these simultaneous conditions are admissible. No derivative lower bound,
identity activation, or frozen hidden layer is assumed.

Define Q^(0)_ab=v_a^T v_b and
Q^(ell)_ab=E[phi_ell(Z_a)phi_ell(Z_b)] for Z~N(0,Q^(ell-1)). Let

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
\lambda=\min(1,\gamma/m),\qquad \ell_n=\log(en).
\tag{3}
\]

Under the completely explicit sufficient label condition

\[
                    0<Y/\lambda\le\frac{2^{-90}}L,
\tag{4}
\]

the existing initialization-only construction and autonomous corrected-
readout runtime admit the following bounds. At any fixed confidence and
all sufficiently large n, the same realized dense initialization is
approximated at equal physical times, including the fitted endpoint, by

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
 \le 2^{150}L\,\frac{Y}{\lambda^{3/2}\sqrt n}.
\tag{5}
\]

Each layer's source dimension can be chosen with

\[
R\le 2^{28d}\frac{(d+3)^{d/2}}{d!}
       \lambda^{-1}\ell_n^{3d/2+1}+2m+d+1.
\tag{6}
\]

Consequently total retained moving and fixed real coordinates satisfy

\[
\begin{split}
\operatorname{size}(C)\le{}&2040(L+1)2^{56d}
 \frac{(d+3)^d}{(d!)^2}\lambda^{-2}\ell_n^{3d+2}\\
 &+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{split}
\tag{7}
\]

The dimension-only ratio is at most 25/4, by the assigned spherical
count. Neither (6) nor (7) contains a factor C^(Ld). The large numerical
bases are conservative explicit certificates, not optimized values.
For (2), lambda=gamma/m, so there is no cap-conversion factor in (4)-(7).
Zero labels give the exact stationary zero predictor separately.

## 2. True gains and existing operator caps

For z=x+iy,

\[
|\tanh z|^2=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
\]

Thus |tanh z|<2 on |y|<1, and |tanh z|<=1 on |y|<=1/2.
Also |sech^2 z|<=sec^2(y)<2 on the latter strip. Differentiation
therefore gives

\[
B=1,\qquad s=2c\le1/20,\qquad t=4c\le1/10
\tag{8}
\]

as complex value/first/second derivative bounds. On the real axis use
|phi'|<=c and |phi''|<=2c. The activation is genuinely nonlinear
for every positive c, including at every layer of the construction.

Retain the inherited initialized, real, and complex mixer caps 8,9,10.
There is no need to invoke sharper Gaussian spectral asymptotics. Their
smaller possible values would enlarge the admissible gain range but are
not needed for this certificate. The source propagation gain and the
runtime propagation gain are, respectively,

\[
q_{\rm src}=10s\le1/2,\qquad
q_{\rm rt}=9(2c)\le9/20<1/2.
\tag{9}
\]

The factor two in q_rt is the existing fixed-neuron-metric diagonal
operator loss. Ignoring that factor would leave a gap between source
contraction and runtime contraction.

All arguments below keep true derivative gains below one. Replacing them
by max(1,s) would destroy (9). All auxiliary *envelopes* that must exceed
one, such as a preactivation error bound, are chosen separately.

## 3. Source and label recurrences are bounded or polynomial

Use S=16Y/lambda and T=32 lambda^-1 ell_n. The physical contour
activity measure is dmu=(2/m)sum_a |r_a| |dt|. Its real activity is at
most S/2 and its extended-contour activity at most S eventually, under
the same real fitting argument. We now quantify its persistent
conditions, retaining the budget proof of LABEL_DEPTH_RESCALING_ROUTE.md.

Define the source derivative and carrier coefficients

\[
P_1=2,\quad P_\ell=2+q_{\rm src}P_{\ell-1},\qquad
K_\ell=2q_{\rm src}^{L-\ell}.
\tag{10}
\]

The actual differentiated forward and backward equations imply these
bounds with no requirement s>=1. In particular P_ell<=4,
K_ell<=2, and sum_ell K_ell<=4. The augmented external-input derivative
is covered by the added one in P_ell, exactly as in the inherited route.
Using mobility coordinates Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)
and F_a=nf_n(v_a), define

\[
\begin{split}
A_H&=2sP_L+2s^2\sum_{\ell=2}^LK_\ell P_{\ell-1}
                                      +tP_L^2K_L,\\
D_H&=t\sum_{\ell<L}P_\ell^2,\\
H_2&=2sP_L+2s^2\sum_{\ell=2}^LK_\ell P_{\ell-1}
                                      +t\sum_{\ell=1}^LP_\ell^2K_\ell.
\end{split}
\tag{11}
\]

These bound the same exact Hessian contractions as in the assigned
source/label proof. Geometric summation gives

\[
                  A_H\le4,\qquad H_2\le7,\qquad D_H\le2L.
\tag{12}
\]

For example the mixed part is at most
2(1/20)^2*4*4=0.08, the readout part is at most 0.4,
and the full curvature part is at most (1/10)*16*4=6.4.
The coefficient D_H uses an unweighted carrier exponential budget and
costs L; it is not asserted uniformly bounded.

The remaining singleton and real-activity constants have the exact
definitions from the label route, with 10s=q_src:

\[
\begin{split}
E&=t\sum_{\ell=1}^L q_{\rm src}^{2(\ell-1)}K_\ell,\\
D_0&=\max\{1,2H_2^2+4A_H^2(e^2-1)+E+s^2K_{\max}^2\},\\
D_1&=576e^3D_H^3,\\
V_1&=sK_1,\quad V_\ell=sK_\ell+q_{\rm src}V_{\ell-1},\\
G_L&=s+2tV_L,\\
G_\ell&=q_{\rm src}G_{\ell+1}+s^3K_{\ell+1}^2+14tV_\ell+s,
\quad G=\max(1,G_1,\ldots,G_L).
\end{split}
\tag{13}
\]

Here E<=0.4, D_0<=512, D_1<=10^5 L^3, V_ell<=0.2, and G=1.
Indeed the last recurrence's forcing is at most 0.3305, its propagation
is at most one half, and its terminal value is at most 0.09.

Take the explicit exponent and budget

\[
\eta=1/512,\qquad \mathcal B=64e^2L<512L,\qquad
\Lambda=\log(e+\mathcal B)+\log512\le14L.
\tag{14}
\]

Then eta D_0<=1 and eta G<=1/128. Every nonvanishing source condition
is implied by

\[
                         S\le\frac1{4096L}.
\tag{15}
\]

For explicit verification, the conditions and resulting upper bounds are

\[
\begin{array}{c|c}
SA_H\le1/4 &4/(4096L)\\
D_HS^2/\eta\le1/4000 &1024/(4096^2L)\\
16eS^2(D_H/\eta)\sqrt{2\mathcal B}\le1
 &1572864/(4096^2\sqrt L)\\
S^2\Lambda/\eta\le1 &7168/(4096^2L)\\
D_1\mathcal BS^4/\eta^2\le1
 &10^5\cdot512^3/4096^4<1/20.
\end{array}
\tag{16}
\]

Also 2sK_1S^2<=1. The real fitting coefficient C_* in the label route
is one: its b_ell=s(9s)^(L-ell) is at most s, and its forward
recurrence has forcing at most s^2 and multiplier at most 9/20.
Thus its real fitting restriction Y/lambda<=1/8 holds under (15).
The physical mixer and first-weight tubes retain their strict margins.

For clarity about the stochastic implication, the inherited singleton
shift is exactly

\[
|k_i-x_i^\top\delta^{-i}|
 \le S\{D_0+D_1\mathcal B S^4/\eta^3\}+o(1).
\tag{17}
\]

Its exponential cost is at most two by (16). The real Gaussian reference
moment has eta G<=1/128, so its complex extension has moment less than
four eventually. The layer-summed budget ratio is at most 1/16 for
the choice (14). For each fixed empirical moment p the limiting hit
probability is at most m16^-p. Width tends to infinity before taking
the infimum over fixed p. This is the same stop-removal argument, with
all persistent smallness coefficients in (16) displayed. The logarithmic
variational coefficient is controlled in (16); it is not moved into
the width threshold. Local fixed-depth insertion remainder coefficients
still multiply strictly vanishing width powers and affect that threshold.

Thus the source alone needs only

\[
                         Y/\lambda\le 2^{-16}/L.
\tag{18}
\]

## 4. Explicit depth-independent analytic radius

We bound the actual endpoint recurrences, rather than a depth-dependent
envelope. Let f_ell=sP_ell, t_ell=sK_ell,
j_ell=20q_src^(ell-1), b_ell=sj_ell, and

\[
g=t_1+\sum_{\ell=2}^Lt_\ell,\quad
r_\ell=P_\ell g,\quad q_\ell=f_\ell g.
\]

Here g<=0.2, f_ell<=0.2, r_ell<=0.8, q_ell<=0.04,
t_ell<=0.1, and b_ell<=1. The symbols r_ell and q_ell in this paragraph
are deterministic response-bound coefficients, distinct from training
residuals r_a and propagation factor q_src.

The normalized Hilbert--Schmidt mixed-endpoint recurrences are

\[
e_1=tr_1P_1,\quad
e_\ell=tr_\ell P_\ell+s(q_{\ell-1}+t_\ell f_{\ell-1})
                                 +q_{\rm src}e_{\ell-1},
\]
\[
a_1=tj_1P_1+2s,\quad
a_\ell=tj_\ell P_\ell+sb_{\ell-1}+q_{\rm src}a_{\ell-1}.
\tag{19}
\]

Their forcing bounds give e_ell<=0.65 and a_ell<=17. Hence

\[
E_Q=\max_\ell(f_\ell H_2+e_\ell)\le3,\quad E_J\le17,
\quad T_Q=8(\max f_\ell)E_Q\le5,\quad T_J\le28.
\tag{20}
\]

The asymmetric trace convergence conditions are already in (16).
The carrier maximum coefficient is

\[
K_{\rm src}=32\max(1,\max K_\ell,\max sK_\ell)=64.
\tag{21}
\]

Use the intrinsic great-circle query tube of the spherical route. Its
Gaussian grid multiplier is G_d'=16 sqrt(d+3). The exact row-insertion
response coefficients can be bounded by

\[
U_1=4sK_{\rm src},\quad
U_\ell=2\{sK_{\rm src}(1+f_{\ell-1}^2+T_Q+q_{\ell-1})
                                    +G_d'q_{\ell-1}+1\},
\]
\[
V_1^{\rm qry}=2(2G_d'+2sK_{\rm src}+1),\quad
V_\ell^{\rm qry}=2\{G_d'b_{\ell-1}
                       +sK_{\rm src}(T_J+b_{\ell-1})+1\}.
\tag{22}
\]

Substituting the preceding bounds, including the final added one, gives

\[
             U_*\le22\sqrt{d+3},\qquad
             V_*^{\rm qry}\le126\sqrt{d+3}.
\tag{23}
\]

Choose the time and query radius coefficients

\[
c_t=\min\{1/8,(512U_*)^{-1}\},\qquad
c_q=\min\{1/8,(128V_*^{\rm qry})^{-1}\}.
\tag{24}
\]

Then c_t^-1,c_q^-1<=2^14 sqrt(d+3), uniformly in L. The complex
time rectangle and intrinsic sphere tube have radii
c_t/sqrt(ell_n) and c_q/sqrt(ell_n), with the strict pole margin
proved in the supplied spherical calculation. The four actual source
families remain h, W_0h, delta and W_0^T delta, and have coordinate
magnitude at most M_0 sqrt(n) with M_0=8. Their temporal horizon and
coordinate tolerance remain T=32 lambda^-1 ell_n and epsilon=n^-1.

The spherical weighted-degree count from the assigned route is

\[
N\le256\,9^d\frac{c_t^{-1}c_q^{-(d-1)}}{d!}
                    \lambda^{-1}\ell_n^{3d/2+1}.
\tag{25}
\]

Taking four families and the exact initial additions proves (6):
1024(9*2^14)^d<=2^(28d) for d>=1. For d=1 the sphere has two
queries. Its separate time-only count is
R<=8(514c_t^-1)lambda^-1 ell_n^(5/2)+2m+2, also bounded by (6).
The scalar coefficient construction preserves both orientations of each
initialized image pair and uses only initial jets and labels, as in the
complete source input. The runtime retains no source trajectory table.

Only explicit logarithmic eventual conditions in the assigned spherical
count absorb M_0 and fixed approximation-tail prefactors. The nonvanishing
inverse radii in (24)-(25) remain displayed, independent of L.

## 5. Runtime: the necessary replacement when gate gains are below one

The fixed-neuron metric obeys D/4<=H<=D and 1^T D1<=4. Therefore a
bounded feature has norm at most h=2, a real gate has operator norm at
most g=2c<=1/20, and a changed gate has Lipschitz coefficient
kappa=4c<=1/10. Set R=9 and q=gR<1/2. Use the corrected direct
source interface from the source addendum:

\[
K=8+4K_{\rm src}=264,\qquad
M\le1+4K(Y/\lambda)\sqrt{\ell_n}.
\tag{26}
\]

The carrier allowance in (26) is not identified with the actual activity
integral. The source multiplier, initialized mixer norm, and mixer tube
are kept distinct.

To state the replacement runtime constants without confusing s with the
complex derivative gain, write u=Y/lambda and alpha=Y/sqrt(lambda).
The backward derivative and hidden Jacobian coefficients are

\[
b_\ell=gq^{L-\ell},\quad b=\max b_\ell\le1/20,\qquad
U=\left(b_1^2+h^2\sum_{\ell=2}^Lb_\ell^2\right)^{1/2}\le1.
\tag{27}
\]

For forward parameter derivatives, preactivation bounds obey
Z_1=1 and Z_ell<=h+q Z_(ell-1); feature derivatives cost a further
factor g. Thus choose the common derivative envelope F=4. This exceeds
both derivatives and one. It avoids the invalid assertion that a
preactivation bound is smaller than its feature bound when g<1.

Use the following constants from the exact runtime proof:

\[
\begin{gathered}
D_\delta=3b+3K,\quad W=32(K+1),\quad
J_0=h\sqrt L(7b+3K),\quad V_0=14FU,\\
P_h=6K+11K^2,\quad P_\delta=18Kb+11K^2,\quad D_r=8P_h,\\
A_0=1+2K(K+1)+8D_\delta P_h+8hP_\delta,\\
C_f=4(1+A_0),\qquad H_0=1+3WC_f+3D_r.
\end{gathered}
\tag{28}
\]

The changed forward preactivation recurrence is
|Delta z_ell|<=h a+q |Delta z_(ell-1)|+A_0 epsilon,
with initial bound a, where a is the hidden-parameter error norm.
Consequently C_f in (28) bounds both preactivation and feature errors
by C_f(a+epsilon): (h+A_0)/(1-q)<=4(1+A_0).

For the backward comparison, let eta be the effective-readout error
in this paragraph only, as in the runtime input; it is unrelated to the
carrier exponent (14). The actual response subtraction obeys

\[
\begin{split}
\|\Delta\delta^{(L)}\|&\le g\|\eta\|+
                    \kappa M C_f(a+\epsilon),\\
\|\Delta\delta^{(\ell)}\|&\le q\|\Delta\delta^{(\ell+1)}\|
 +gD_\delta\alpha a+gA_0\epsilon+
                    \kappa M C_f(a+\epsilon).
\end{split}
\tag{29}
\]

The changed gate multiplies the *reference* carrier. M>=1 and alpha<=1,
so geometric summation, with each forcing summed once, yields

\[
\|\Delta\delta^{(\ell)}\|
 \le b_\ell\|\eta\|+Z_0M(a+\epsilon),\qquad
Z_0=\frac{\kappa C_f+gD_\delta+gA_0}{1-q}.
\tag{30}
\]

This replaces L(gR)^L from the old envelope, which was justified there
only because gR>=1. Substituting gR<1 into that old formula without
replacing the geometric sum would be incorrect. Likewise kappa rather
than g bounds the changed gate; the old common activation norm had
concealed that distinction.

Now put

\[
\begin{gathered}
J_1=\sqrt L(hbH_0+hZ_0+D_\delta C_f),\\
D_0^{\rm rt}=P_h+L(P_\delta h^2+9b^2P_h),\\
F_0=8C_f+24J_0J_1+6D_0^{\rm rt},\quad T_0'=6V_0,\\
G=4(T_0'+F_0)+2C_f+2J_1,\\
C_1=G(8+W/2),\quad C_2=16KG,\quad O_0=2hH_0+WC_f+D_r,\\
W_1=2h+50V_0+6(h^2+J_0^2),\qquad T_1=hW_1+7V_0.
\end{gathered}
\tag{31}
\]

All these constants are defined quantities. The projection identities,
raw energy, source pairing errors, lifted residual damping, and exact
readout cancellation in the runtime input use the coefficients only
through their stated inequalities. Equations (27)-(30) verify the
changed inequalities. Hence the remainder of that proof gives

\[
C_{\rm err}=O_0\{1+\sqrt e(C_1+C_2u_*)
                       e^{C_1u_*+C_2^2u_*^4}\}+8T_1
\tag{32}
\]

under u<=u_*, 224FUu^2<=1, and 6J_0u<=1. Its conclusion is
(5) with coefficient C_err. In particular the raw exponent still has
the form C_1u+C_2u^2 sqrt(ell_n), so conversion of epsilon=n^-1
to a strict n^-1/2 output error is unchanged. There is no logarithmic
loss in (5), no time rescaling, and no extra source differentiation.

Here is explicit arithmetic sufficient for a polynomial envelope:

| Quantity | Upper bound |
| --- | --- |
| D_delta, W, J_0, V_0 | 800, 2^14, 2^11 sqrt(L), 2^6 |
| P_h, P_delta, D_r | 2^20, 2^20, 2^23 |
| A_0, C_f, H_0, Z_0 | 2^33, 2^36, 2^52, 2^38 |
| J_1, D_0^rt | 2^55 sqrt(L), 2^23 L |
| F_0, G | 2^72 L, 2^75 L |
| C_1, C_2, O_0 | 2^89 L, 2^88 L, 2^55 |
| W_1, T_1 | 2^25 L, 2^27 L |

For example Z_0<=2(C_f+D_delta+A_0)<2^38. Multiplication
J_0J_1 costs at most 2^66 L, which gives the rows for F_0,G,C_1,C_2
by their displayed definitions. The only unsummed layer factors left
are sqrt(L) in tuple norms and L in the Gram defect; no layer products
have been hidden in these constants.

Choose u_*=2^-90/L. It implies the fitting inequalities and (18),
and makes the exponent in (32) at most two. Because sqrt(e)<2 and
e^2<8,

\[
C_{\rm err}<2^{55}[1+16(2^{89}L+1)]+2^{30}L
                                      <2^{150}L.
\tag{33}
\]

This proves (4)-(5). The inherited tail bound
4T_1Y lambda^-3/2 exp(-lambda t/4) controls both models after T
and includes their fitted endpoints. The actual runtime state count
1020(L+1)R^2+10m(d+1), followed by (a+b)^2<=2a^2+2b^2,
gives (7).

## 6. What this improvement does and does not resolve

For the explicit nonlinear subclass (2), the old sufficient label cap
Y/lambda<=beta^-62L is smaller than (4) for every L>=2 and beta>=10.
Indeed 62L log_2(10)>90+log_2 L. Thus the old label assumptions
automatically imply this candidate's assumptions in the subclass; the
polynomial cap also certifies a larger relative-label range. The positive
gap assumption, arbitrary label signs, whole-sphere observable, same-run
comparison, all-time clock, and strict root-width rate are preserved.

There is a substantive qualification about gamma. For (2),
|c tanh x|<=c|x| on the real axis. Since Q^(0)_aa=1,

\[
Q^{(\ell)}_{aa}\le c^2Q^{(\ell-1)}_{aa}\le c^{2\ell},
\qquad
\gamma\le\frac{\operatorname{tr}Q^{(L)}}m\le c^{2L}.
\tag{34}
\]

Consequently lambda=gamma/m<=c^(2L)/m. The inverse-gap factors
in (5)-(7) and the admissible absolute labels in (4) still carry real
depth dependence; for example the displayed inverse-gap storage
coefficient lambda^-2 is at least m^2 c^(-4L). This is a property of
the sufficient bound and the actual initialization geometry, not a lower
bound on the complexity of every possible compressor. It must not be
called an overall depth-polynomial storage guarantee.

The result removes the *additional* exponential structural multipliers
at fixed explicit gamma, and quantifies precisely what remains. It
does not settle the general-activation question, prove a depth-uniform
Gram gap, or prove that nonlinear influence remains of uniform size
through arbitrarily deep centered contractive layers. Small derivative
gains alone cannot supply those claims.

The width threshold remains unquantified, as in the supplied insertion
interfaces, and may depend strongly on fixed L,d,m,gamma,c,Y and
confidence. Exact-real preprocessing cost and precision are outside the
retained-coordinate contract. No theorem for simultaneously growing
depth and width is asserted. A separate reconstruction should check the
unclamped-gain substitution in the local source interface and the three
runtime replacements F,C_f,Z_0 before this candidate is called internally
checked.
