# Quantitative dataset dependence of analytic neuron compression

2026-10-04. Continuation of the internally checked analytic compression
theorem. This note makes its dataset dependence explicit; it does not
change the original network or the representation contract. The underlying
source and insertion theorems remain internal research dependencies, not
promoted manuscript or book results.

The two quantitative inputs are reconstructed in
[DATASET_SOURCE_CONSTANTS.md](DATASET_SOURCE_CONSTANTS.md) and
[DATASET_LABEL_DEPENDENCE.md](DATASET_LABEL_DEPENDENCE.md). The latter's
sharper real-fitting threshold improves the complete source theorem when
combined with its separate carrier-budget requirement. The
conditioning example has a separate complete derivation in
[DATASET_GEOMETRY_EXAMPLE.md](DATASET_GEOMETRY_EXAMPLE.md).

## 1. Setup and the data quantity

Fix input dimension $d\ge2$, hidden depth $L\ge2$, and $m$ training
inputs $x_a=\sqrt d\,v_a$ with $\|v_a\|_2=1$. The labels $y_a$ are
fixed real numbers and

\[
 Y=\left(\frac1m\sum_{a=1}^m y_a^2\right)^{1/2}.
\]

At each layer the activation $\phi_\ell$ is real on the real axis,
holomorphic on $|\operatorname{Im}z|<b$, and bounded there by
$B_\phi$. Throughout this note $c,C$ depend only on
$d,L,b,B_\phi$, unless another dependence is displayed. Derivative
bounds on narrower strips follow from Cauchy's formula. These constants
are conservative bounds, not numerical or optimal constants.

The original model has width $n$ at every hidden layer:

\[
 z^{(1)}(x)=Ax/\sqrt d,\quad h^{(\ell)}=\phi_\ell(z^{(\ell)}),
 \quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\ (\ell\ge2),
 \quad f_n(x)=w^\top h^{(L)}(x)/n.
\]

Initialization is $A_{ij}\sim N(0,1)$,
$W^{(\ell)}_{ij}\sim N(0,1/n)$, independently, and $w=0$.
The loss is $m^{-1}\sum_a(f_n(x_a)-y_a)^2$, with mobilities
$(n,1,\ldots,1,n)$. In particular the sample sums in every velocity
are divided by $m$, as in the original theorem. No clock is changed.

The limiting **initialized** feature covariance is computed from the
inputs and activations, without running a population training flow:

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \qquad Z\sim N(0,Q^{(\ell-1)}).
 \tag{1}
\]

Define the capped normalized gap

\[
 \boxed{\lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}>0.}
 \tag{2}
\]

The division by $m$ matches the averaged loss. If the cap is inactive,
the original theorem's unnormalized gap $\gamma$ can be taken as
$\gamma=m\lambda$. In this note $\ell_n=\log(en)$, so the logarithm
is never denoted by the same symbol as the gap. Since the last activation
is bounded,

\[
                    m\lambda\le B_\phi^2.             \tag{3}
\]

Thus $m$ and the possible normalized gaps are not independent. A
qualitative assertion that the inputs are distinct does not give a
numerical lower bound for (2).

## 2. Explicit sufficient version of the compression theorem

The construction and autonomous weighted network are exactly those in
[GENERAL_ANALYTIC_COMPRESSION.md](GENERAL_ANALYTIC_COMPRESSION.md),
with the slightly finer source approximation tolerance $n^{-1}$ below.
There exist structural constants $c,C$ such that the following sufficient
conditions and bounds hold. Suppose

\[
                         0<Y\le c\lambda/\sqrt m.      \tag{4}
\]

Fix $0<\eta<1/2$. For every sufficiently large width

\[
 n\ge n_0(d,L,b,B_\phi,m,\lambda,Y,\eta),
 \tag{5}
\]

the initialization-only coordinated neuron selection gives, with
probability at least $1-\eta$, a smaller autonomous weighted dense
network satisfying

\[
 \boxed{
 \sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
       |f_C(t,x)-f_n(t,x)|
 \le \frac{C\exp(CY/\lambda^2)}{\sqrt n}
 \le \frac{C\exp(C/(\lambda\sqrt m))}{\sqrt n}.}
 \tag{6}
\]

Both flows fit and converge; the supremum includes their limits. The
total moving and fixed real coordinates retained after setup are at most

\[
 \boxed{
 C(1+m)^4\lambda^{-4}[\log(en)]^{4[d(L+5)+1]}
       +C\,m(d+1).}
 \tag{7}
\]

The last summand counts the data and labels. Formula (7) counts all
small learned matrices, first weights, readouts, and masses, not just
the number of retained neurons. Setup work, temporary arrays and exact
real precision remain outside the resource guarantee, as in the original
theorem. This is an existence theorem for autonomous representations,
not an efficient implementation guarantee or a theorem for the unchanged
order-$q$ memory equations.

The probability statement is for each fixed dataset and each sufficiently
large width. The same bounds apply across the specified dataset class;
no single random event simultaneous over every dataset or every width
is asserted. The width threshold in (5) is finite but not given a
practical closed formula by the source proof. It is part of the dataset
dependence and cannot be omitted. In particular this note does not prove
a result for $m=m(n)$ or a deteriorating gap $\lambda=\lambda(n)$.

The case $Y=0$ has identically zero predictions and can be represented
exactly with a constant zero output. It does not require dividing by $Y$.

## 3. Where the label condition comes from

Write $\rho(t)=m^{-1/2}\|y-f_n(t)\|_2$ and
$s(t)=\int_0^t\rho(u)\,du$. The physical speed estimates use
$m^{-1}\sum_a|y_a-f_a|\le\rho$, without an extra sample-count
factor. In a fixed hidden-operator tube the elementary activity estimates
give readout and backward RMS norms at most $Cs$, hidden displacement
at most $Cs^2$, and normalized training Gram change at most $Cs^2$.
That last bound alone would impose $Y\le c\lambda^{3/2}$.

The real energy proof improves this part. With the canonical mobility
norm, $-d(\rho^2)/dt=\|\dot\theta\|_{\rm mob}^2$.
On a running Gram tube of gap comparable to $\lambda$, it implies
total path length at most $CY/\sqrt\lambda$, hence the same bound
on the readout RMS. Hidden displacement is then at most
$CY^2/\lambda^{3/2}$. A perturbation of the normalized feature matrix
smaller than $c\sqrt\lambda$ preserves its smallest singular value;
this requires only $Y\le c\lambda$. Its complete first-exit proof
and explicit structural constants are in DATASET_LABEL_DEPENDENCE.md.
The weighted and rectangular cavity forms use the same energy identity;
total neuron mass at most one suffices for every upper bound. Their
initialized gap margins are supplied by the source initialization event.

Consequently a fixed fitting rate $\kappa=c_0\lambda$ works under
$Y\le c\lambda$, and a common activity allowance is

\[
                     S=C_0Y/\lambda.                   \tag{8}
\]

The complete source proof needs more than real fitting. Its normalized
single-sample Gaussian reference has a uniformly bounded exponential
moment. A maximum over $m$ samples costs at most a factor $m$:
$e^{q\max_a Z_a}\le\sum_a e^{qZ_a}$. Its empirical carrier
budget can therefore be chosen as $B=Cm$. The sufficient smallness
conditions for all physical, Gaussian-path and trace-series estimates,
after replacing the older real Gram bootstrap by the energy proof, are

\[
                 Y\le c\lambda,\qquad S\le c,
                 \qquad S^2m\le c.                    \tag{9}
\]

The logarithmic budget condition $S^2\log(e+B)\le c$ follows as
well. Equations (4) and (8) imply every condition in (9), after choosing
the single structural constant in (4) sufficiently small. This gives
an explicit sufficient condition for the full compression proof.

It is not an optimal or necessary label threshold. The additional factor
$m^{-1/2}$ comes from the conservative carrier budget $B=Cm$, not from
the real energy identity. The initial source audit's smaller sufficient
condition $Y\le c\lambda^{3/2}$ follows as a special case using
$m\lambda\le B_\phi^2$. The energy refinement eliminates its
unnecessary extra dependence on a tiny gap at fixed sample count.
This note does not claim full compression for every $Y\le c\lambda$
without the remaining sample factor.

## 4. Dataset dependence of the error comparison

Here is a direct quantitative refinement of Sections 3--5 of
[GENERAL_WEIGHTED_COMPARISON.md](GENERAL_WEIGHTED_COMPARISON.md).
It also explains why it is useful to keep the activity factor in the
carrier maximum. All vector RMS norms and operator bounds in this
paragraph use the original empirical measure or selected positive masses,
as appropriate.

Choose source coordinate tolerance $\epsilon=n^{-1}\le\min(1,Y)$.
With (9), the source pairing defects have bound $C\epsilon$, with
structural $C$: every feature RMS is bounded, every response RMS is
at most $CS\le C$, and every temporal integral is against total
residual activity at most $S$. The projected reference matrices are
bounded in weighted operator norm. These facts follow exactly from the
paired source construction; there is no dependence on the smallest mass.

Let $d(t)$ be the sum of the weighted parameter distances between the
compressed flow and the retained reference state defined by equation (7)
of the deterministic comparison note. Let $u(t)=c_C(t)-c_n(t)$ be
the difference of their actual residuals. Let
$M=\max\{1,\max_{a,\ell,i,t\le T}|k_{a,i}^{(\ell)}(t)|\}$.
Forward and backward subtraction in that note give feature errors
$C(d+\epsilon)$ and response errors $C(1+M)(d+\epsilon)$.

To avoid hiding a sample-count factor, write the tangent Gram as
$\Gamma=K/m$. Each entry of $K_C-K_n$ has magnitude at most
$C(1+M)(d+\epsilon)$. For an $m$ by $m$ matrix $E$,
$\|E/m\|_{\rm op}\le\max_{a,b}|E_{ab}|$. The exact residual
equation is $\dot c=-2\Gamma c$. The compressed Gram lower bound
therefore yields

\[
 D^+\|u(t)\|_m\le-c\lambda\|u(t)\|_m
       +C(1+M)\rho_n(t)(d(t)+\epsilon),
 \qquad u(0)=0.
 \tag{10}
\]

At a vanishing norm this follows by regularization, as in the comparison
note. Integrating (10) and dropping its nonnegative terminal norm gives

\[
 \int_0^t\|u(s)\|_m\,ds
 \le \frac{C(1+M)}{\lambda}
                 \int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
 \tag{11}
\]

Subtracting each of the two models' actual rank-one velocities gives

\[
 d(t)\le C\int_0^t\|u(s)\|_m\,ds
        +C(1+M)\int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
 \tag{12}
\]

All constants here are structural because $S\le c$, all hidden
operator norms are uniformly bounded, and residuals are averaged over
samples. Substituting (11) into (12), using $\lambda\le1$, and
applying the integral Gronwall inequality to $d+\epsilon$ proves

\[
 d(t)+\epsilon\le\epsilon
      \exp\left(\frac{C(1+M)}{\lambda}
                    \int_0^t\rho_n(s)\,ds\right).
 \tag{13}
\]

The real all-time carrier bound in DATASET_SOURCE_CONSTANTS.md retains
its amplitude factor: $\max|k|\le CS\sqrt{\ell_n}$ for all
sufficiently large widths. Thus

\[
 \frac{C(1+M)S}{\lambda}
 \le \frac{CY}{\lambda^2}
                  +\frac{CY^2}{\lambda^3}\sqrt{\ell_n}.
 \tag{14}
\]

Observation subtraction costs only another structural factor, so (13)
gives the finite-horizon estimate

\[
 \sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
 \le C e^{CY/\lambda^2}\,n^{-1}
              e^{(CY^2/\lambda^3)\sqrt{\ell_n}}.
 \tag{15}
\]

The coefficient $CY^2/\lambda^3$ is finite for fixed data and labels,
but need not be bounded uniformly under (4). The explicit additional
width restriction

\[
                \ell_n\ge C(1+Y^4/\lambda^6)
\]

ensures $e^{(CY^2/\lambda^3)\sqrt{\ell_n}}\le\sqrt n$.
For the smaller subclass $Y\le c\lambda^{3/2}$ this step has a
structural width threshold and (6) is at most
$C\exp(C/\sqrt\lambda)/\sqrt n$. This distinction is retained
in (5), rather than hiding an unbounded coefficient.
Both actual flows have query tails at most $CS e^{-c\lambda T}$.
Taking $T=C\lambda^{-1}\ell_n$ with a sufficiently large structural
constant makes these tails at most $Cn^{-1}$. Adding them to (15)
proves (6), including the endpoints. No same-time claim is inferred from
a different training clock, and the compressed residual is never supplied
by the original network.

## 5. Dataset dependence of the state count

Under (9), the complete complex-source audit gives a time and angular
strip of radius $c\ell_n^{-(L+4)}$ and source coordinate magnitudes
$C\ell_n^{L+2}$, with structural constants. The horizon is
$T=C\lambda^{-1}\ell_n$. Approximating sources to $n^{-1}$
therefore requires time degree and per-angle Fourier degree at most

\[
 p\le C\lambda^{-1}\ell_n^{L+6},\qquad
 J\le C\ell_n^{L+5}.                                  \tag{16}
\]

Here the width threshold absorbs fixed logarithmic factors such as
$\log(\lambda^{-1})$. It also ensures $n^{-1}\le Y$.
The initialization-jet construction remains finite and identical in
principle; increasing its precision does not add retained coordinates.

There are a fixed number of whole-sphere query source families per
layer and $O(m)$ training-only backward source families. Set
$a=d(L+5)+1$. The source span dimension per layer consequently obeys

\[
 R\le C\{\lambda^{-1}[\ell_n^a+m\ell_n^{L+6}]+d\}.
 \tag{17}
\]

Positive cubature on their pairwise products selects at most
$1+R(R+1)/2$ neurons per layer. Retaining all learned dense matrices
between those layers costs at most $C(R^4+dR^2)$ coordinates, plus
$C m(d+1)$ for the data. Since $a\ge L+6$ for $d\ge2$,
(17) proves (7). More accurately, one can keep (17) inside
$C(R^4+dR^2)$ to distinguish the query contribution and the
$m$ training-response histories. The simpler fourth-power bound is
deliberately loose.

## 6. What remains in the width threshold

The source audit makes initial Gram concentration explicit. Put
$D_j=\max_\ell\|\phi_\ell^{(j)}\|_\infty$ on the real line,
$A_\phi=B_\phi D_2+D_1^2$, and
$A_L=\sum_{j=0}^{L-1}A_\phi^j$. Gaussian covariance interpolation,
including singular covariances by regularization, and conditional
bounded-variable concentration show that

\[
 n\ge32A_L^2B_\phi^4\lambda^{-2}\log(2Lm^2/\eta)
 \tag{18}
\]

is sufficient for initialized normalized Gram error at most
$\lambda/4$ with probability at least $1-\eta$. This is one
ingredient in (5), not the full threshold.

The insertion/source event still uses fixed-block moments: first choose
a finite moment degree for the requested confidence, then take width
sufficiently large. Control-net and remainder constants depend on that
degree, $m$, the gap and the fixed positive label magnitude. The
existing proof gives existence of (5), without an explicit useful bound
on its entire value. In particular $e^{o(1)/S}$ in cavity-budget
transfer requires care as $Y$ tends to zero; the present result fixes
$Y>0$ before taking $n$ large.

Equations (4), (6), and (7) expose the label threshold, prediction
constant, and retained-state prefactor. They do not make the theorem
uniform over degenerating geometries at arbitrary finite widths. The
explicit prefactors alone cannot justify substituting a growing sample
count into a fixed-dataset theorem.

## 7. Why the geometry and the label direction matter

Take two unit inputs with angular separation $\theta$ and tanh in
every layer. The initialized limiting top Gram has equal diagonal
entries $q_L$ and off-diagonal entry $c_L$. Its normalized eigenvalues
are $\lambda_-=(q_L-c_L)/2$ in direction $(1,-1)$ and
$\lambda_+=(q_L+c_L)/2$ in direction $(1,1)$. As
$\theta\downarrow0$,

\[
 \lambda=\lambda_-\asymp\theta^2,
 \qquad \lambda_+\longrightarrow q_L>0.                \tag{19}
\]

The constants in this fixed-depth asymptotic are strictly positive;
DATASET_GEOMETRY_EXAMPLE.md proves their exact Gaussian formula. Thus
even $m=2$ does not bound the inverse gap. For labels $(\alpha,-\alpha)$,
the minimum initialized-feature readout RMS squared is
$\alpha^2/\lambda_-$; for $(\alpha,\alpha)$ it is
$\alpha^2/\lambda_+$. These are exact statements about that fixed
feature geometry, not a claim that trained features remain fixed.

Our label condition (4) is uniform over all label directions and is
therefore conservative for easy directions. In this two-sample example
it permits $|\alpha|\le c\lambda$, which scales as $\theta^2$.
It does not prove that labels larger than this cannot fit or cannot be
compressed. An improved label-direction-sensitive compression theorem
would require an additional argument; the fixed-feature calculation
alone does not supply it.

All results in this note concern the established within-study analytic
construction. No experiment, manuscript edit, prior-study edit, Git
mutation, or promotion is part of this continuation.
