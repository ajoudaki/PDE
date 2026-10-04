# A moment-controlled time modulus for deeper backward responses

2026-10-03. Coordinator derivation for the fixed-depth extension. This is a
deterministic lemma, not a completed finite-network moment theorem.
Inputs: current manuscript forward/backward subtraction and physical bounds,
and the present study's two-layer insertion argument. No experiment.

Fix depth, bounded slopes and Lipschitz gates, and a physical tube with
bounded hidden operators, forward feature RMS, and backward RMS at most
CS. The total dense residual activity is at most CS, where S is proportional
to fixed small label RMS. All vector norms below are divided by sqrt(n).
Let s(t) be accumulated residual activity, rescaled so its terminal value
is at most one. The physical speed estimates give
\[
 d_n(\theta(t),\theta(u))\le CS|s(t)-s(u)|.
\]
Assume only for this deterministic lemma that the instantaneous exponential
budget, summed over the fixed layers, obeys
\[
 \sup_t\frac1n\sum_{\ell,i}
 \exp\{\eta\max_a|k^{(\ell)}_{a,i}(t)|/S\}\le B.
 \tag{1}
\]
Here k^(L)=w and k^(ell)=W^(ell+1)T delta^(ell+1).
The stronger sum of coordinatewise time suprema also implies (1).

For any threshold R>0, exponential Markov and
x^2 1_{x>r} <= C_eta exp(-eta r/2)exp(eta x) give
\[
 \max_{\ell,a}\frac{\|k^{(\ell)}_a(u)
           \mathbf1_{|k^{(\ell)}_a(u)|>R}\|_2}{\sqrt n}
 \le C_\eta S\sqrt B\,e^{-\eta R/(4S)}.
 \tag{2}
\]
The manuscript's one-reference backward subtraction, applied to two
physical times of this one dense path, gives
\[
 \max_{\ell,a}\frac{\|\delta^{(\ell)}_a(t)
                    -\delta^{(\ell)}_a(u)\|_2}{\sqrt n}
 \le C[(1+R)d_n(\theta(t),\theta(u))
             +S\sqrt B e^{-\eta R/(4S)}].
 \tag{3}
\]
This follows by descending the backward recursion: a changed gate times a
reference carrier is split at R, while the operator acting on an already
estimated response difference is bounded. Thus there is one power of R,
not one power for each layer.

Write v=|s(t)-s(u)|<=1. Taking
R=(4S/eta)log(e sqrt(B)/v) in (3), including equality at v=0 by
continuity, proves
\[
 \max_{\ell,a}\frac{\|\delta^{(\ell)}_a(t)
                    -\delta^{(\ell)}_a(u)\|_2}{S\sqrt n}
 \le C_\eta v[1+S\log(e+B)+S\log(e/v)]
 \le C_\eta[1+S\log(e+B)]\sqrt v.
 \tag{4}
\]
The normalized response also has diameter C by its RMS bound.
Freezing the path at a reference-measurable stop preserves this modulus.

Consequently the Gaussian process xT delta(t), for an independent
x~N(0,I/n), has conditional metric entropy bounded by
\[
 N(\epsilon S)\le
 1+C_\eta[1+S\log(e+B)]^2/\epsilon^2.
 \tag{5}
\]
Dyadic metric nets and the elementary Gaussian tail imply
\[
 \Pr\{\sup_t|x^\top\delta(t)|/S
   >C_\eta[1+\sqrt{\log(e+S\log(e+B))}]+u\}
 \le C e^{-cu^2}.
 \tag{6}
\]
One can use the weaker but simpler shift C_eta[1+sqrt(log(e+B))].
The finite training-sample maximum changes constants only.
Thus the linear-exponential moment L_eta(B) grows at most as
exp(C_eta sqrt(log(e+B))) times a fixed constant. In particular
L_eta(B)=B^{o(1)} as B tends to infinity.

This resolves a particular apparent obstacle to depth extension:
a bounded total variation estimate for the deeper response is unnecessary.
One may use a supremum empirical budget, obtain its Gaussian reference
entropy through (4), choose B large enough to dominate L_eta(B), and only
then choose the fixed small-label threshold. It does not by itself close
the budget; the fixed-depth insertion trace and nonlinear remainder still
need proof.

For the common-cavity comparison, radial projection of a difference path
onto a deterministic small Euclidean ball preserves independence from the
omitted column and is 1-Lipschitz. Its two endpoint paths satisfy (4).
Its Gaussian diameter is then D_n=o(1), while its entropy is polynomial in
1/epsilon with fixed B-dependent constants. The resulting Gaussian
supremum is O(D_n sqrt(log(e+1/D_n))), sufficient for the same finite-block
moment comparison as in the two-layer proof whenever a polynomially small
diameter has been proved by insertion.

## Endpoint response factors in the reinsertion trace

For this section additionally assume that every activation is C2 with
bounded continuous second derivative, so the displayed classical
parameter derivatives exist everywhere. The modulus argument above only
needs C1 with a globally Lipschitz derivative. The final insertion
candidate uses the stronger bounded C3 class.

The same supremum budget addresses another depth-specific issue. Let
B_a^(j)=D_Theta delta_a^(j), in the mobility-Euclidean coordinates
Theta=(W^(1),sqrt(n)W^(2),...,sqrt(n)W^(L),w).
All forward derivative maps D_Theta z_a^(j) have bounded operator norm
on the physical tube. Descending the differentiated backward recursion gives
\[
 B_a^{(j)}U
 =\operatorname{diag}(\phi_j')W^{(j+1)\top}B_a^{(j+1)}U
  +\operatorname{diag}(\phi_j')
          (U_{H^{(j+1)}}/\sqrt n)^\top\delta_a^{(j+1)}
  +\operatorname{diag}(k_a^{(j)}\phi_j'')D_\Theta z_a^{(j)}U.
 \tag{7}
\]
At the top the first two terms are replaced by
diag(phi_L') U_w. Normalized Schatten norms use n, not parameter
dimension. The output rank is at most n. Thus, for every p>=2, (1) gives
\[
 \|B_a^{(j)}\|_{p,n}\le
 C[1+S p B^{1/p}],
 \qquad
 \|\mathcal H(t)\|_{p,n}\le C[1+S p B^{1/p}],
 \tag{8}
\]
where mathcal H is the residual-Hessian coefficient per unit absolute
residual activity. To justify the second estimate, the output Hessian is
a sum over layers of forward-Jacobian contractions of diagonal
k^(j) phi_j'' and mixed adjacent-weight terms. The latter have operator
norm C and rank O(n); the former have the displayed diagonal moment
bound. Constants depend on fixed depth and eta.

Consider the residual part of the forward reinsertion response,
\[
 \int_0^t r_a(s)\,B_b^{(j)}(t)J(t,s)B_a^{(j)}(s)^\top
                  a(s)\,ds,\qquad |a|\le C.
 \tag{9}
\]
Expand J in residual-Hessian insertions around its negative-Gram
contraction. For the term containing r inserted Hessians, normalized
trace Holder uses r+2 factors, all in Schatten r+2. Supremum budget (1)
controls both endpoint B factors, as well as all inserted Hessians.
The absolute time integrals are at most CS(CS)^r/r!. Therefore
its total normalized trace is bounded by
\[
 CS\sum_{r\ge0}\frac{(CS)^r}{r!}
       [1+S(r+2)B^{1/(r+2)}]^{r+2}
 \le CS+CS^3 B
 \tag{10}
\]
for sufficiently small fixed S. Indeed
(1+x)^(r+2)<=2^(r+1)(1+x^(r+2)); the second series is bounded by
CS^3 B sum_r (CS^2)^r(r+2)^(r+2)/r!, which converges when S is
small. The rank-one adaptive-residual forcing is still estimated
separately by its normalized trace and the weak operator bound; it
contributes o(1) on a logarithmic physical horizon.

For the direct external derivative D_e delta^(j), the normalized trace
is bounded by CS: express its scalar Hessian as the finite sum of
diagonal carrier terms conjugated by bounded forward maps, and use their
RMS carrier bounds. No readout-variation cross term appears when only
the external preactivation is differentiated.

Hence the plausible singleton shift in a deeper proof is
CS(1+S^2 B), replacing CS(1+S^2 sqrt(B)) in the two-layer proof.
Together with (6), a budget closure would have base
L_eta(B) exp(C_eta(1+S^2 B)). Since L_eta(B)=B^{o(1)}, first choosing B
large and then S small leaves a strict fixed-budget margin.
This trace calculation still requires the exact insertion lemma; it does
not assume that a middle-layer neuron has only a forward influence.
