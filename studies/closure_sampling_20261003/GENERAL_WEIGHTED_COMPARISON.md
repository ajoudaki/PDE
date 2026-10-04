# Weighted neuron selection at arbitrary fixed depth: the deterministic bridge

2026-10-03. Coordinator derivation. This note proves a deterministic
source-to-autonomous-flow comparison for arbitrary fixed depth and fixed
finite data. It deliberately separates this proved bridge from the missing
general complex-source construction. No claim that the latter follows
merely from real carrier bounds is made.

Scientific inputs: the current manuscript's exact gradient normalization,
small-label fitting proof and one-reference damping argument; this study's
complete two-input cubature construction; and the user-authorized prior
`dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md` with its
complete local and probability checks. The prior carrier theorem is used
only in Section 7, where it is identified explicitly. All new statements
before that section are deterministic and proved here.

## 1. Model and source assumptions

Fix input dimension $d$, sample count $m$, depth $L\ge2$, and training
vectors $v_a=x_a/\sqrt d\in\mathbb R^d$. No orthogonality is assumed.
For layer $\ell$ let $\phi_\ell\in C^2(\mathbb R)$ and assume

\[
 \max_\ell\bigl(\|\phi_\ell\|_\infty+
 \|\phi_\ell'\|_\infty+\|\phi_\ell''\|_\infty\bigr)\le C_\phi.
\]

The original width-$n$ model is

\[
 z^{(1)}(x)=Av,\quad z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),
 \quad h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),
 \quad f_n(x)=w^\top h^{(L)}(x)/n,
 \qquad v=x/\sqrt d.
\]

Set $c_a=y_a-f_n(x_a)$, $Y=(m^{-1}\sum_a y_a^2)^{1/2}$,
$\rho_n=(m^{-1}\sum_a c_a^2)^{1/2}$,
$k_a^{(L)}=w$,
$\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}$,
and $k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}$ for
$\ell<L$. The squared mean loss and mobilities $(n,1,\ldots,1,n)$ give

\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=\frac2{mn}\sum_a c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
 \quad \dot w=\frac2m\sum_a c_ah_a^{(L)}.                 \tag{1}
\]

The case $Y=0$ is stationary and has zero prediction; below take $Y>0$.
Take $w(0)=0$ and an initialization with fixed hidden operator bounds,
fixed first-weight Frobenius RMS, and a fixed positive initial readout
Gram gap. For sufficiently small fixed $Y$, the real physical estimates
below give global fitting. Fix a finite comparison horizon $T$ and a
bounded query set $\mathcal X$ containing the training inputs. Assume
the actual reference carriers obey

\[
 \max_{a,\ell,i,t\le T}|k_{a,i}^{(\ell)}(t)|\le M,
 \qquad M\ge1.                                           \tag{2}
\]

For each layer let $S_\ell\subset\mathbb R^n$ be a finite-dimensional
real vector space. Assume coordinate-supremum approximations with error
at most $\epsilon$, $0<\epsilon\le\min(1,Y)$, to the following sources
through $T$:

- $h^{(\ell)}(t,x)$ for $x\in\mathcal X$;
- $\delta_a^{(\ell)}(t)$ for each training sample;
- $W_0^{(\ell)}h^{(\ell-1)}(t,x)$ in $S_\ell$, for $\ell\ge2$;
- $W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}(t)$ in $S_\ell$, for $\ell<L$.

Paired forward approximants have the exact form
$v\in S_{\ell-1}, W_0^{(\ell)}v\in S_\ell$, and paired reverse
approximants have the form
$d\in S_{\ell+1},W_0^{(\ell+1)\top}d\in S_\ell$.
Each member of a pair has its own stated approximation error; an operator
norm is not used to infer coordinate error for the other member.
Include every initialized training activation and its initialized forward
image in the respective spaces, and all columns of $A_0$ in $S_1$.

For the conditional construction here, the spaces are given. An
unconditional compression theorem must still construct them from allowed
initial information, at the claimed dimension, for the actual model.

## 2. Weighted construction and its independent fitting

Let $r_\ell=\dim S_\ell$, and choose basis matrices $U_\ell$ with
$U_\ell^\top U_\ell/n=I$. Positive cubature selects indices $I_\ell$
and positive diagonal weights $D_\ell$ of total mass one such that

\[
 U_{\ell,I_\ell}^\top D_\ell U_{\ell,I_\ell}=I,
 \qquad N_\ell=|I_\ell|\le1+r_\ell(r_\ell+1)/2.           \tag{3}
\]

The elementary elimination proof matches the constant and all basis
products, moving masses along a dependence until a positive node disappears.
It terminates at (3). Set

\[
 B_0^{(\ell)}=U_{\ell,I_\ell}
 \frac{U_\ell^\top W_0^{(\ell)}U_{\ell-1}}{n}
 U_{\ell-1,I_{\ell-1}}^\top D_{\ell-1}.                  \tag{4}
\]

Its weighted adjoint is
$B^{(\ell)*}=D_{\ell-1}^{-1}B^{(\ell)\top}D_\ell$.
The selected basis maps are isometries. Consequently each initial
operator norm is at most that of $W_0^{(\ell)}$, and the forward and
reverse identities hold exactly on paired source vectors. The entire
initialized training forward pass matches the retained original pass,
by induction in $\ell$. The initial top Gram is exactly preserved.

The compressed model has state $(A_C,B_C^{(2)},\ldots,B_C^{(L)},w_C)$,
initialized by $A_C(0)=A_{0,I_1}$, (4), and $w_C(0)=0$. Its forward
pass uses the actual activations and the matrices $B_C^{(\ell)}$;
its output is $f_C=w_C^\top D_Lh_C^{(L)}$. Define its residuals and
backward recursion using its own forward pass and weighted adjoints.
Its autonomous equations are

\[
 \dot A_C=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^\top,
 \quad
 \dot B_C^{(\ell)}=\frac2m\sum_a c_{C,a}
       \delta_{C,a}^{(\ell)}h_{C,a}^{(\ell-1)\top}D_{\ell-1},
 \quad \dot w_C=\frac2m\sum_a c_{C,a}h_{C,a}^{(L)}.        \tag{5}
\]

Use weighted vector norms $\|u\|_{D_\ell}^2=u^\top D_\ell u$ and
matrix norms $\|B\|_{\mathrm{HS}}=
\|D_\ell^{1/2}BD_{\ell-1}^{-1/2}\|_F$. For the first weights use
the weighted sum of squared row norms. A rank-one matrix in (5) has
Hilbert--Schmidt norm $\|\delta\|_{D_\ell}\|h\|_{D_{\ell-1}}$.

Here is the required fitting argument for (5). Until hidden operator
norms leave a fixed tube, bounded gates and zero readout imply
$\|w_C\|_\infty\le CS$, all backward RMS norms are at most $CS$,
and hidden matrix and first-weight displacements have norms at most
$CS^2$, where $S=\int_0^t\|c_C\|_m$. Forward subtraction gives
training-feature displacement at most $CS^2$ at every layer. The residual
matrix is positive semidefinite and dominates its readout Gram, so that
Gram's initial positive gap persists at a fixed small $S$. It follows
that $\|c_C(t)\|_m\le Ye^{-\kappa t}$ and $S\le CY$.
Choosing $Y_*$ small closes the tube and proves global existence.
All constants are independent of the number of selected nodes and their
smallest positive weight. The same proof applies to the full network.
Every bounded query has tail at most $C_{\mathcal X}Ye^{-\kappa t}$.

## 3. Pairing defects and the retained reference state

At layer $\ell$, a real source with empirical RMS at most $C$ and
coordinate error $\epsilon$ from $S_\ell$ has selected RMS at most
$C+2\epsilon$: its approximant has exactly the same selected and
empirical norms. Inserting approximants in a pair therefore gives

\[
 |u_{I_\ell}^\top D_\ell v_{I_\ell}-u^\top v/n|
 \le C\epsilon                                               \tag{6}
\]

for all the real source pairs used here, including different times.
For backward sources the empirical and selected norms are $O(Y)$ since
$\epsilon\le Y$. Their coordinate maxima need not be bounded by $CY$.
The readout is within coordinate error $CY\epsilon$ of $S_L$: approximate
its continuous integral by finite Riemann sums, replace each top training
feature in the sum by an admissible source approximant, and bound the error
by the corresponding sum of absolute residual weights times $\epsilon$.
Pass to the limit using continuity of distance to the closed subspace
$S_L$. This requires no measurable selection of approximants. The
approximation coefficients are proof devices, never runtime input.

Define only for comparison

\[
 B_R^{(\ell)}(t)=B_0^{(\ell)}+\frac2m\sum_a\int_0^t
 c_a(s)\delta_a^{(\ell)}(s)_{I_\ell}
 h_a^{(\ell-1)}(s)_{I_{\ell-1}}^\top D_{\ell-1}\,ds.      \tag{7}
\]

Take $A_R=A_{I_1}$ and $w_R=w_{I_L}$. All selected true feature and
response vectors below are from the original network; they are not
defined by the forward pass through (7). Pairing (6), the exact paired
initial actions, and the rank-one integral formulas give, uniformly on
$[0,T]$,

\[
 \|B_R^{(\ell)}h^{(\ell-1)}(t,x)_{I_{\ell-1}}
                   -z^{(\ell)}(t,x)_{I_\ell}\|_{D_\ell}
 \le C\epsilon,                                           \tag{8}
\]
\[
 \|B_R^{(\ell+1)*}\delta_a^{(\ell+1)}(t)_{I_{\ell+1}}
                   -k_a^{(\ell)}(t)_{I_\ell}\|_{D_\ell}
 \le C\epsilon,                                           \tag{9}
\]
\[
 |w_R^\top D_Lh^{(L)}(t,x)_{I_L}-f_n(t,x)|\le C\epsilon.
                                                               \tag{10}
\]

For (8) the learned contribution pairs a past training activation with
a present query activation. For (9) it pairs a past upper backward
response with the present one. Residual activity, at most $CY$, bounds
the integrals. Only RMS bounds enter these products. Equation (7) also
gives bounded $B_R$ operator norms; selecting the true first-layer
velocity and using its selected backward RMS bounds gives
$\|A_R-A_R(0)\|\le CY^2$.

## 4. One-reference forward and backward subtraction

Let $d(t)$ be the sum of the weighted first-weight, hidden
Hilbert--Schmidt, and readout distances between (5) and the reference
state (7). The initial distance is zero. Layerwise forward subtraction
using (8), bounded operator norms and bounded slopes yields

\[
 \max_\ell\|z_C^{(\ell)}(t,x)-z^{(\ell)}(t,x)_{I_\ell}\|_{D_\ell}
 +\|h_C^{(\ell)}(t,x)-h^{(\ell)}(t,x)_{I_\ell}\|_{D_\ell}
 \le C_{\mathcal X}[d(t)+\epsilon].                       \tag{11}
\]

For backward subtraction multiply every changed gate by the **true
selected reference carrier**, whose coordinate maximum is at most $M$:

\[
 \delta_{C,a}^{(\ell)}-\delta_{a,I_\ell}^{(\ell)}
 =\phi_\ell'(z_{C,a}^{(\ell)})\odot
       (k_{C,a}^{(\ell)}-k_{a,I_\ell}^{(\ell)})
 +[\phi_\ell'(z_{C,a}^{(\ell)})-
       \phi_\ell'(z_{a,I_\ell}^{(\ell)})]\odot k_{a,I_\ell}^{(\ell)}.
                                                               \tag{12}
\]

The carrier difference follows from (9), the already controlled upper
response difference, and $(B_C-B_R)^*\delta_{a,I}^{(\ell+1)}$.
The latter costs $CYd(t)$. Descending through fixed depth proves

\[
 \max_{a,\ell}\|\delta_{C,a}^{(\ell)}-
             \delta_{a,I_\ell}^{(\ell)}\|_{D_\ell}
 \le C(1+M)[d(t)+\epsilon].                               \tag{13}
\]

The factor $M$ is added at each layer, not multiplied by a further $M$
when an upper response difference propagates. No carrier bound for the
compressed network and no minimum-mass estimate is required.

## 5. Actual residuals and all-time amplification

For either model define its unnormalized sample tangent Gram

\[
 K_{ab}=\langle h_a^{(L)},h_b^{(L)}\rangle
 +\sum_{\ell=2}^L\langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle
                   \langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle
 +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle(v_a^\top v_b).
                                                               \tag{14}
\]

Use original empirical pairings or the corresponding selected masses.
Every term is a Gram matrix; the last is the Gram of tensor products
$\delta_a^{(1)}\otimes v_a$ and remains positive without orthogonality.
The exact residual equation is $\dot c=-(2/m)Kc$.

Equations (6), (11), (13) and the bounded response RMS norms imply

\[
 \|K_C-K_n\|_{\mathrm{op}}
 \le C(1+M)[d(t)+\epsilon].                               \tag{15}
\]

This compares with the true original tangent Gram directly. It avoids
differentiating the observation defect (10). For $u=c_C-c_n$, the exact
equation and the compressed model's preserved Gram gap give

\[
 D^+\|u\|_m\le-\kappa\|u\|_m
 +C(1+M)\rho_n(t)[d(t)+\epsilon].                         \tag{16}
\]

At zero norm regularize by $\sqrt{\|u\|_m^2+\zeta^2}$ and let
$\zeta\downarrow0$. The initial residual difference is zero. Integrating
(16) and dropping its nonnegative terminal value proves

\[
 \int_0^t\|u(s)\|_m ds
 \le C(1+M)\int_0^t\rho_n(s)[d(s)+\epsilon]ds.           \tag{17}
\]

Subtract (5) from the exact selected velocities defining (7). Differences
of a residual, backward response and forward response account for every
rank-one update. Their weighted norms and (11), (13) give

\[
 d(t)\le C\int_0^t\|u\|_m ds
       +C(1+M)\int_0^t\rho_n(s)[d(s)+\epsilon]ds.
                                                               \tag{18}
\]

Insert (17) and apply an integrating factor against
$C(1+M)\rho_n(s)ds$, whose total mass is at most $C(1+M)Y$.
For every terminal time $T$ this proves

\[
 \sup_{t\le T}d(t)
 \le C(1+M)e^{C(1+M)Y}\epsilon.                          \tag{19}
\]

Constants depend only on the fixed data, activation bounds, depth and
initial Gram/operator margins. There is no physical-time factor in (19).
The wider bound $C(1+M)e^{CM}\epsilon$ is often convenient.
Combining (10), (11) and (19) gives the same bound for all queries in
$\mathcal X$.

Each autonomous model has its own query tail $CYe^{-\kappa T}$. Adding
these tails extends the finite-source theorem to all time with error

\[
 C_{\mathcal X}(1+M)e^{CM}\epsilon
       +C_{\mathcal X}Ye^{-\kappa T},                    \tag{20}
\]

including their fitted limits. Neither model is stopped at $T$.

## 6. Stored state and significance of logarithmic amplification

The runtime is precisely (5), with no original matrix, full-width
source, reference state (7), or externally provided residual. Its moving
state has

\[
 dN_1+\sum_{\ell=2}^LN_\ell N_{\ell-1}+N_L
\]

real coordinates. Fixed masses and optional initial-state copies have
the same or smaller order. Thus $r_\ell\le R$ gives total count $CR^4$.
If initialization-only response approximation provides $R\le C\log^b n$
at accuracy

\[
 \epsilon_n=n^{-1/2}\exp[-D\sqrt{\log(en)}]/\log(en),    \tag{21}
\]

and $M\le C\sqrt{\log(en)}$, choose fixed $D$ large and
$T=C_T\log(en)$ to make (20) at most $C/\sqrt n$.
Since $\log(1/\epsilon_n)=O(\log n)$, changing from root-width
source accuracy to (21) does not change a polynomial-in-logarithm
approximation dimension obtained from a polynomially shrinking complex
strip. Width dependence in an intermediate stability factor is therefore
not itself an obstruction to a width-independent final error constant.

This observation removes the need for the special two-layer coordinate
change **in the deterministic comparison**. It does not prove the required
complex-source strip at arbitrary depth or nonorthogonal data.

## 7. What is supplied and what is still missing

The user-authorized prior finite-depth carrier theorem proves
$M\le C\sqrt{\log(en)}$ for the actual canonical finite network,
all physical time, fixed depth and finite data with an initial Gram gap,
and bounded $C^3$ activations with small fixed labels. Its full source is
`../dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`
(SHA-256 `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`),
with complete local reconstruction in `DEPTH_INSERTION_CHECK.md` and
probability reconstruction in `DEPTH_CAVITY_PROBABILITY_CHECK.md` there.
The coordinator read all of that source and both full reconstructions.
These remain internal research inputs, not established-book results.

Consequently the remaining general polylogarithmic-compression problem
is the actual finite network's initialization-only small response spaces,
including both mixer orientations and query sources. A real carrier
maximum is not a complex-time derivative estimate. At the next layer
$\dot z^{(\ell)}$ contains
$W^{(\ell)}\dot h^{(\ell-1)}$, for which operator and RMS bounds
alone allow a coordinate loss $\sqrt n$. This note neither ignores that
term nor replaces it by an assumed polylogarithmic bound.

The lemma is a completed deterministic implication. It is useful because
the earlier dimension-free transformed-field requirement is stronger
than necessary for a polylogarithmic final state count. The complete
joint arbitrary-depth sampling theorem still needs a separate actual
source proof; it has not been renamed into an assumption and declared
resolved here.
