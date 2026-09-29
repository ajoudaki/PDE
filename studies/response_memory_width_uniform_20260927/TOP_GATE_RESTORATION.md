# Restoring the top backward gate

This result removes one further oracle dependency from the preceding
width-uniform theorem. The old-clock moment closure now uses its own
residuals, clock, histories, reconstructed matrices, readout, and top
backpropagation gate. Dense gates are supplied only at hidden layers
1,...,L-1. The result holds for arbitrary fixed finite data and depth.

The full top-gate version uses a bounded initial readout, which includes
zero population readout and width-uniform high-probability events for the
canonical small Gaussian readout. Section 7 gives a learned-readout version
under the previous theorem's original RMS-only initial assumptions; at zero
readout it coincides exactly with the full top-gate version.

## 1. Model and oracle information

Take L>=2 hidden tanh layers and m fixed samples q_a=x_a/sqrt(d). Neuron
norms are population L2, or finite-width RMS. Hidden increments have
Hilbert--Schmidt norm, equal to ordinary matrix Frobenius norm at width n.
Initialized hidden matrices/operators W_(0,l) are retained exactly.

The dense trajectory supplies only the fields

\[
 D_{\ell,a}^D(t)=\operatorname{diag}\tanh'(z_{\ell,a}^D(t)),
 \qquad 1\le\ell<L.
 \tag{1}
\]

All forward responses are computed from the closure's own weights.
Its backward responses are

\[
 \bar\delta_{L,a}
   =\bar w\odot\tanh'(\bar z_{L,a}),\qquad
 \bar\delta_{\ell,a}
   =D_{\ell,a}^D\,\bar W_{\ell+1}^*\bar\delta_{\ell+1,a}
       \quad(\ell<L).
 \tag{2}
\]

Use its own predictions and residuals

\[
 \bar f_a=\mathbb E[\bar w\,\bar h_{L,a}],\qquad
 \bar r_a=\bar f_a-y_a,\qquad
 \bar\rho=(m^{-1}\sum_a\bar r_a^2)^{1/2},\qquad
 \bar\tau=1+\int_0^t\bar\rho(s)\,ds.
\]

The first layer and readout follow the canonical updates using these
residuals and (2). For every hidden link the usual old-clock moment equations
record its own forward history h and backward history b=r delta/rho.
The forward prefix is its initial activation and the backward prefix is zero.
The reconstruction is

\[
 \bar W_\ell=W_{0,\ell}
 -\frac2m\sum_a\int_0^{\bar\tau}
    (\Pi_P\bar b_{\ell,a})\otimes
    (\Pi_P\bar h_{\ell-1,a})\,d\xi .
 \tag{3}
\]

At finite width u tensor v is uv^T/n. Projection in (3) is the ordinary
Legendre projection on that process's own current clock interval.
No dense residual, clock, top preactivation, or top gate is an oracle input.
The lower gates in (1) remain externally supplied, so the system is not
the fully autonomous closure.

## 2. Theorem

Assume the dense canonical flow exists regularly on [0,T]. Set

\[
 X=\max_a\|q_a\|,\quad Y=(m^{-1}\sum_a y_a^2)^{1/2},\quad
 R_0=\|w(0)\|_2,\quad B_0=\|w(0)\|_\infty,\quad
 K_{0,\ell}=\|W_{0,\ell}\|_{\rm op}.
\]

For now B_0 is finite. With identical initialized parameters and the stated
moment prefixes, the system (1)--(3) exists uniquely through T for every
P>=1. In the normalized parameter distance

\[
 d(\bar\theta,\theta)=
 \|\bar W_1-W_1\|_{\rm row,L^2}
 +\sum_{\ell=2}^L\|\bar W_\ell-W_\ell\|_{\rm HS}
 +\|\bar w-w\|_2
 \tag{4}
\]

one has

\[
 \sup_{t\le T}d(\bar\theta_P(t),\theta_D(t))
 \le \frac{C_{\rm comp}e^{L_TT}}{\sqrt{P(P+1)}}.
 \tag{5}
\]

All constants below depend only on T, data, depth, R_0, B_0, and initialized
operator norms. They are independent of width and P. No successful-fitting,
input-orthogonality, closure-closeness, or uniform-stability hypothesis is used.

For a finite-width family, (5) is uniform on common bounds for those initial
quantities. The same proof applies directly in population Hilbert spaces.

## 3. A priori readout and operator bounds

The top gate change does not alter the readout update. In either the dense
or the partially supplied-gate process,

\[
 \frac d{dt}\|w\|_2^2
 =-\frac4m\sum_a r_a f_a
 =Y^2-\frac4m\sum_a(f_a-y_a/2)^2\le Y^2.
 \tag{6}
\]

Define

\[
 R=\sqrt{R_0^2+TY^2},\qquad Q=R+Y,\qquad
 S=TQ,\qquad A=1+S,\qquad B=B_0+2S.
 \tag{7}
\]

Then

\[
 \|w(t)\|_2\le R,\quad
 \rho(t)\le Q,\quad \int_0^T\rho\,dt\le S,\quad
 \|w(t)\|_\infty\le B .
 \tag{8}
\]

The last bound is pointwise, since
|dot w_i|<=2m^{-1}sum_a|r_a|<=2rho. It also holds as an essential-supremum
bound on a population. This is the new estimate that permits the top gate
to change.

Both the top self-gate and all supplied lower gates have operator norm at
most one. Therefore the previous top-down bounds still apply:

\[
 \beta_L=R,\qquad
 K_\ell=K_{0,\ell}+2\sqrt{AS}\,\beta_\ell,\qquad
 \beta_{\ell-1}=K_\ell\beta_\ell .
 \tag{9}
\]

They bound the dense and reconstructed hidden operator norms by K_l and
each backward response's L2 norm by beta_l. To see the middle reconstruction
bound, its backward history has sample-averaged squared mass at most
S beta_l^2; its forward history has squared mass at most A. Projection
contraction and Cauchy--Schwarz give the increment 2sqrt(AS) beta_l.
Then the next backward recursion proves beta_(l-1). Dense exact increments
obey the smaller estimate 2S beta_l. The first-weight increment is at most
2SX beta_1 in its normalized norm.

These estimates precede all trajectory comparison; they are not bootstrap
assumptions.

## 4. Existence in population space and the unchanged defect estimate

With a self-gate, the product w phi'(z) is not a locally Lipschitz map on an
unrestricted L2 x L2 space. The proof must not silently assume otherwise.
To construct the solution, temporarily replace w in the top backward
response only by its pointwise clipping to [-B-1,B+1]. Keep the actual w in
the forward prediction and in the readout update. The clipped multiplier
is bounded and 1-Lipschitz in L2, so this top backward response and the
finite-order raw moment vector field are locally Lipschitz in their Hilbert
states, with the prescribed lower gates acting as bounded multipliers.

Equation (6) is unaffected by clipping. So are the pointwise readout bound
and the operator estimates, since clipping does not increase the L2 norm
of w. The prescribed lower gates are strongly continuous multiplication
operators when the dense fields are L2-continuous; boundedness plus truncation
of any fixed L2 operand verifies that assertion. The moment representations
and (8)--(9) bound every coordinate of the raw moment state. Its denominator
tau is at least one, and its local Lipschitz/velocity bounds are uniform
on the resulting bounded ball for each finite P. Thus its solution continues
through T. By (8), the clipping never activates. Any solution of the original
system obeys the same bounds, hence coincides with this unique solution.

At zero residual, all raw moment and outer-weight velocities vanish; the
state stays stationary even if the supplied lower gates change with time.

The physical parameters satisfy exactly

\[
 \dot{\bar\theta}=G_D(t,\bar\theta)+E,\qquad E_1=E_w=0,
\]
\[
 E_\ell=\frac{2\bar\rho}{m}\sum_a
       (\bar b_{\ell,a}-\bar b_{\ell,a}^*)
          \otimes(\bar h_{\ell-1,a}-\bar h_{\ell-1,a}^*).
 \tag{10}
\]

Here G_D uses self residuals and the mixed backward rule (2); stars are
current endpoint projections. For each history v,

\[
 D_v=\|v-\Pi_Pv\|_{L^2_\xi}^2,\qquad
 \dot D_v=\bar\rho\|v-v^*\|_2^2 .
 \tag{11}
\]

The derivative of the minimizing polynomial drops out by orthogonality.
Consequently

\[
 \int_0^T\|E_\ell\|_{\rm HS}\,dt
 \le\frac2m\sum_a\sqrt{D_{b,\ell,a}D_{h,\ell-1,a}}.
 \tag{12}
\]

For completeness, all derivative-energy constants can be given explicitly.
Let Z_l bound the sample-averaged integral of ||h_l'||_2^2 in the process's
own activity coordinate (the prefix derivative is zero). One may take

\[
 Z_1=4S X^4\beta_1^2,\qquad
 Z_\ell=3\left[4S\beta_\ell^2+
       (K_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}\right].
 \tag{13}
\]

Indeed the Legendre tail is at most
A^2 Z_l/[4P(P+1)] in sample-averaged squared norm. Endpoint evaluation
has norm P/sqrt(tau), making the backward endpoint error at most
(P+1)beta_l in sample RMS. Equations (10)--(11) then imply

\[
 \int_0^T\bar\rho\|E_\ell/\bar\rho\|_{\rm HS}^2dt
 \le2A^2\beta_\ell^2 Z_{\ell-1}.
\]

The forward chain rule, applied to the canonical velocity, defect velocity,
and W h' terms, gives (13). This argument uses only bounded backward
responses; it never differentiates a backward gate. It is valid for (2)
just as for the previous all-supplied-gate oracle.

Since the backward history mass is at most S beta_l^2, (12) yields

\[
 \int_0^T\sum_{\ell=2}^L\|E_\ell\|_{\rm HS}dt
 \le\frac{C_{\rm comp}}{\sqrt{P(P+1)}},\qquad
 C_{\rm comp}=A\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}} .
 \tag{14}
\]

## 5. Restored top-gate stability

Let two states satisfy the preceding readout/operator bounds, and use the
same supplied lower gates. Their distance is d from (4). The forward
preactivation and activation differences are bounded by U_l d, where

\[
 U_1=X,\qquad U_\ell=K_\ell U_{\ell-1}+1 .
 \tag{15}
\]

For the top backward difference, split exactly

\[
 \bar w\,\phi'(\bar z_L)-w\,\phi'(z_L)
 =(\bar w-w)\phi'(\bar z_L)
   +w[\phi'(\bar z_L)-\phi'(z_L)].
\]

Using |phi'|<=1, |phi''|<=2 and ||w||_infinity<=B gives

\[
 \|\Delta\delta_{L,a}\|_2
 \le\|\Delta w\|_2+2B\|\Delta z_{L,a}\|_2
 \le V_L d,\qquad V_L=1+2B U_L .
 \tag{16}
\]

This is the newly restored feedback term, bounded with no width factor.
Lower gates are shared, so continue by

\[
 V_\ell=K_{\ell+1}V_{\ell+1}+\beta_{\ell+1},\qquad
 \max_a\|\Delta\delta_{\ell,a}\|_2\le V_\ell d .
 \tag{17}
\]

At a common residual vector, subtraction of the canonical gradient products
has sum norm at most rho Lambda d, with

\[
 \Lambda=2\left[
 X V_1+\sum_{\ell=2}^L(V_\ell+\beta_\ell U_{\ell-1})+U_L\right].
\]

The self residual is also Lipschitz:

\[
 \|\Delta r\|_{\rm sample,RMS}\le C_f d,\quad
 C_f=1+R U_L.
\]

At fixed responses, changing the residual changes the vector field by at
most C_r times that sample RMS, where

\[
 C_r=2\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].
\]

Since rho<=Q, these bounds prove

\[
 \|G_D(t,\theta)-G_D(t,\widetilde\theta)\|_{\rm sum}
 \le L_Td(\theta,\widetilde\theta),\qquad
 L_T=Q\Lambda+C_r C_f .
 \tag{18}
\]

This is a derived estimate on the actual a priori region, not an assumed
uniform stability property. At the dense state, its own top gate and the
supplied lower gates are all the exact dense gates. Thus
dot theta_D=G_D(t,theta_D). Subtracting that equation from (10) gives

\[
 d(t)\le L_T\int_0^t d(s)\,ds+
             \int_0^t\sum_\ell\|E_\ell(s)\|_{\rm HS}\,ds .
\]

The scalar integral majorant is at most exp(L_T T) times the total defect.
Equation (14) proves (5).

## 6. Test functions, initialization, and the remaining oracle inputs

For a test input x let X_x=||x||/sqrt(d). Repeat (15) with U_1=X_x.
Bounded top activations give

\[
 |\bar f_P(t,x)-f_D(t,x)|
 \le[1+R U_L(X_x)]\,d(\bar\theta_P(t),\theta_D(t)).
\]

This is O(P^-1) uniformly over bounded input sets, and in L2(nu) when nu has
a finite second input moment. The difference between the two test RMSEs
against the same target is bounded by the prediction discrepancy.

For the canonical readout w_(0,i)~N(0,n^-2),

\[
 \Pr\left\{\|w_0\|_\infty>
       \frac{\sqrt{2\log(2n/\eta)}}{n}\right\}\le\eta.
\]

The threshold is bounded uniformly over n and tends to zero. Thus B_0 is
a legitimate width-independent high-probability initial bound in that
regime. A deterministic uniform bound on every Gaussian realization is
not asserted. Zero initial readout, the population small-readout limit,
has B_0=0 exactly.

For depth L the remaining externally supplied gate fields are precisely
layers 1,...,L-1. In particular with two hidden layers only the first-layer
gate is still supplied. Forward nonlinearities at every layer, the residual,
the clock, all histories, all learned operators, and the readout are generated
by the partially autonomous system itself.

Restoring a lower gate introduces

\[
 [\phi'(\bar z_{\ell,a})-\phi'(z_{\ell,a}^D)]
       (W_{\ell+1}^D)^*\delta_{\ell+1,a}^D.
\]

The multiplying field is now a backpassed field rather than the readout.
An initialized spectral norm bound controls its RMS, not its coordinatewise
supremum. Thus the argument (16) cannot simply be iterated into lower
layers. This theorem removes one complete gate dependency without asserting
that the rest are settled.

## 7. Same-assumptions extension for arbitrary L2 initial readout

To preserve the original oracle theorem's RMS-only initialization class,
let the top backward response instead be

\[
 \bar\delta_{L,a}
 =w_0\odot D_{L,a}^D
   +(\bar w-w_0)\odot\phi'(\bar z_{L,a}).
 \tag{19}
\]

Only the initialized readout component still uses the dense top gate.
The learned readout uses the system's own top gate. At the dense state
(19) equals the dense backward response, so the same reference is compared.

The readout energy (6) is unchanged. Pointwise integration gives

\[
 \|\bar w(t)-w_0\|_\infty,\ \|w_D(t)-w_0\|_\infty\le2S
\]

even when w_0 is merely in L2 and has no finite essential supremum.
For this variant use beta_L=R_0+2S in (9), and keep the physical readout
R in C_f. The supplied w_0 D_L^D term cancels when two states are compared.
Writing v=w-w_0, the top difference becomes

\[
 (\bar v-v)\phi'(\bar z_L)
   +v[\phi'(\bar z_L)-\phi'(z_L)],
\]

so (16) is replaced by V_L=1+4S U_L. All later estimates are identical.
For existence, clip only the increment v inside the self-gated top term
to [-2S-1,2S+1]; the preceding bound proves that clipping is inactive.
The fixed term w_0 D_L^D is an L2 field and poses no local Lipschitz issue.

This proves the same width-independent rate for the full original RMS-only
initialization class while restoring the top gate for the learned readout.
If w_0=0, (19) becomes exactly (2), and there is no top-gate oracle input.
Thus the population small-readout setting needs no new assumption at all.

## 8. Check status

The result continues the same width-uniform study. Its inputs are the complete
SHARED_RESIDUAL_GATE_ORACLE.md proof, the current paper's flow convention,
and the stated elementary tanh and projection identities. The coordinator
derived the top-gate feedback bound, readout bounds, clipping argument,
and RMS-only learned-readout variant. A scoped agent separately checked
these steps and their compatibility with the earlier defect argument;
its report is TOP_GATE_CHECK.md. This is an internally checked research
result, not a promotion review or a change to the main paper. No training,
external literature search, or Git commit was needed.
