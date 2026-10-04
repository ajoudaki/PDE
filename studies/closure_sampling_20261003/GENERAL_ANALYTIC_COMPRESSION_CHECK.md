# Complete conditional reconstruction of the analytic compression assembly

2026-10-03. Scoped internal reconstruction by the depth agent. This checks
the complete construction and implication in GENERAL_ANALYTIC_COMPRESSION.md,
SHA-256
bae30debcb714f3ecb857fa600b29685cd7e1d392a5934761962595002c8bc5a,
against GENERAL_WEIGHTED_COMPARISON.md, SHA-256
1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306.
The added activation examples, nonproportional-input Gram criterion, and
feature-motion certificate in Section 5 are included in this check.
Both files were read completely. The initialized-jet construction in
TWO_INPUT_STABLE_GEOMETRY.md and the manuscript's exact normalization and
initialized Gram argument were also read and reconstructed.

**Verdict: PASS for the conditional implication.** The named joint
complex-source estimate, together with the named real carrier estimate,
implies the stated initialization-only autonomous compression, total state
exponent, and all-sphere, same-physical-time, all-time error. The assembly
does not hide a further stability, interpolation, selection, normalization,
or endpoint hypothesis. This report gives no verdict on the proof of
DEEP_COMPLEX_SOURCE.md or its activation extension. Their complete separate
reconstructions determine whether the joint theorem can be called proved.
This is a collaborative internal check, not an isolated promotion review:
the checker participated in the source candidate and activation supplement.

Two wording issues identified during this check were corrected before the
hash above: initialized training vectors are included in their respective
layer spaces, and fitting/convergence is asserted on the same probability
event as the approximation. No further correction is required by this
conditional reconstruction.

## 1. Exact assumptions and the two named probabilistic inputs

Fix the input dimension \(d\ge2\), depth \(L\ge2\), sample count \(m\),
inputs \(x_a=\sqrt d\,v_a\) with \(\|v_a\|_2=1\), and labels \(y_a\).
All are independent of width. Put
\[
 Y=\left(\frac1m\sum_a y_a^2\right)^{1/2},\qquad
 \lambda=\log(en),\quad K=L+4,\quad
 T=C_T\lambda,\quad r=c\lambda^{-K}.
\]
Each activation is real on the real axis, holomorphic and bounded on a
fixed horizontal strip. Cauchy's formula on a narrower strip supplies all
bounded real derivatives needed for fitting and the prior carrier theorem.
No sign, monotonicity, oddness, or positive-slope assumption is implicit.

The network and its gradient flow are
\[
 z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n=\frac1n w^\top h^{(L)},
\]
\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\qquad
 \dot W^{(\ell)}=\frac2{mn}\sum_a
       c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
 \dot w=\frac2m\sum_a c_ah_a^{(L)},\qquad c_a=y_a-f_n(x_a).
 \tag{1}
\]
Here \(k_a^{(L)}=w\), \(\delta_a^{(\ell)}
=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\), and
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\).
Equation (1) agrees with loss \(m^{-1}\sum_a(f_n-y_a)^2\) and
mobilities \((n,1,\ldots,1,n)\). Every time derivative in the construction
refers to this physical time.

The Gaussian initialization has independent entries of variance one in
\(A_0\), variance \(1/n\) in every \(W_0^{(\ell)}\), and \(w_0=0\).
The assumed limiting top-feature Gram gap is \(Q^{(L)}\succeq\gamma I_m\),
with the recursive Gaussian expectations stated in the assembly.
Conditionally independent rows give concentration of each empirical
feature pairing. Continuity under covariance convergence follows by
writing the Gaussian as \(Q^{1/2}G\) and using bounded activations;
this also covers singular earlier covariances. Hence the initialized
Gram gap and fixed operator/RMS initialization bounds hold with
probability tending to one.

The source proposition used in this check is exactly the following
named input, not a consequence deduced here from real estimates:

* The actual original-network vectors \(h^{(\ell)}(t,x)\),
  \(W_0^{(\ell)}h^{(\ell-1)}(t,x)\),
  \(\delta_a^{(\ell)}(t)\), and
  \(W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}(t)\), in their natural layer
  ranges, extend jointly holomorphically to the indicated time rectangle
  and all \(d-1\) angular strips of width \(r\).
* Each coordinate is bounded there by
  \(M_{\mathrm{src}}\le C\lambda^{L+2}\).
* This event has probability tending to one.

The separate real carrier input is
\[
 M_{\mathrm{car}}=
 \max\!\left(1,\max_{a,\ell,i,t\ge0}|k_{a,i}^{(\ell)}(t)|\right)
 \le C_0\sqrt\lambda
 \tag{2}
\]
on an event of probability tending to one. It is the actual finite-network
carrier theorem in the specifically authorized prior route and its two
complete checks. The assembly uses (2) only in the deterministic comparison.
It does not substitute it for the complex source proposition.

## 2. Whole-sphere approximation and its dimension

Use the usual periodic sphere map
\[
 v_1=\cos\theta_1,\quad
 v_2=\sin\theta_1\cos\theta_2,\quad\ldots,\quad
 v_d=\prod_{j=1}^{d-1}\sin\theta_j .
 \tag{3}
\]
Its real torus image is the entire unit sphere. All components are entire
functions of the angles. No inverse chart is used, so poles of spherical
coordinates create no missing query region. A uniform error for all real
angles gives the required uniform error on the entire input sphere.

For one source coordinate, a Bernstein ellipse for the interval
\([0,T]\) with parameter \(\exp(c_1r/T)\), for a small fixed \(c_1\),
lies inside the time rectangle: its imaginary semiaxis is \(O(r)\),
and its real overshoot is \(O(r^2/T)\). Its Chebyshev tail above degree
\(p\) is at most
\[
 C M_{\mathrm{src}}\frac Tr
                    \exp(-c_2pr/T).
 \tag{4}
\]
Shifting each periodic angular Fourier integral inside its strip gives
coefficient decay \(\exp(-c_3r\|k\|_1)\). Summing outside the box
\(\max_j|k_j|\le J\) bounds the angular tail by
\[
 C_d M_{\mathrm{src}} r^{-(d-1)}\exp(-c_4rJ).
 \tag{5}
\]
One may use a narrower strip throughout to avoid any issue with values
on the boundary. Joint holomorphy makes these estimates uniform in the
other variables. Tensor Chebyshev and trigonometric interpolation add
only polynomial factors in \(p,J\), since \(d\) is fixed. For example,
crude discrete-transform bounds give a factor at most
\(2(p+1)(2J+1)^{d-1}\). Its logarithm is \(O(\log\lambda)\).

Set
\[
 \epsilon=n^{-1/2}\exp(-D\sqrt\lambda)/\lambda .
 \tag{6}
\]
Then \(\log(1/\epsilon)=O(\lambda)\). Choosing sufficiently large
fixed constants in
\[
 p=C_p\lambda^{K+2},\qquad J=C_J\lambda^{K+1}
 \tag{7}
\]
makes (4), (5), and their interpolation versions smaller than any fixed
fraction of \(\epsilon\). These degrees follow respectively from
\(T/r=O(\lambda^{K+1})\) and \(1/r=O(\lambda^K)\).
Thus each query-dependent source has at most
\[
 (p+1)(2J+1)^{d-1}
 \le C\lambda^{K+2+(d-1)(K+1)}
 =C\lambda^{d(L+5)+1}
 \tag{8}
\]
real coefficient vectors. Training-only sources need only \(p+1\).
The number of source families is fixed. Real cosine/sine coordinates
give exactly the usual \(2J+1\) modes per angular variable; using
complex Fourier coefficients and splitting their real and imaginary
parts would only change a fixed factor.

## 3. A finite construction using only initialized derivatives

For clarity, the conformal calculation behind the assembly's reference
to the two-input note is reconstructed here. Denote
\[
 q_0=\frac{\pi T}{8r},\quad b=\tanh q_0,\quad
 \alpha=\tanh(q_0+\pi/4),\quad \eta=b/\alpha,\quad
 \psi(\xi)=\frac{\xi-\eta}{1-\eta\xi},
\]
\[
 z(\xi)=\frac T2+\frac{2r}{\pi}
                    \log\frac{1+\alpha\psi(\xi)}
                             {1-\alpha\psi(\xi)} .
 \tag{9}
\]
The unit disk maps into the time rectangle and \(z(0)=0\).
Indeed the logarithm's imaginary part has magnitude below \(\pi/2\),
and its real magnitude is at most \(2\operatorname{artanh}\alpha\);
the latter gives exactly the available real extent \(T/2+r\).
For real \(0\le t\le T\), its inverse is
\[
 q(t)=\alpha^{-1}\tanh\frac{\pi(t-T/2)}{4r},\qquad
 \xi(t)=\frac{q(t)+\eta}{1+\eta q(t)}.
 \tag{10}
\]
It runs from \(0\) to \(\xi_*=2\eta/(1+\eta^2)<1\). In particular,
\[
 \Delta=1-\xi_*=\frac{(1-\eta)^2}{1+\eta^2}
                    \ge c\exp(-CT/r)>0 .
 \tag{11}
\]

For any source \(S(t,\theta)\), the Taylor coefficients of
\(S(z(\xi),\theta)\) at \(\xi=0\) are
\[
 A_j(\theta)=
 \sum_{k=0}^j \frac{\partial_t^kS(0,\theta)}{k!}
                         [\xi^j]z(\xi)^k.
 \tag{12}
\]
The sum is finite because \(z(0)=0\). Cauchy's formula gives the
coordinate bound \(|A_j|\le M_{\mathrm{src}}\). Consequently the
degree-\(N_{\mathrm{jet}}\) truncation at every real time in \([0,T]\)
has coordinate error at most
\[
 \frac{M_{\mathrm{src}}}{\Delta}
                   \exp[-\Delta(N_{\mathrm{jet}}+1)].
 \tag{13}
\]
For any positive nodal tolerance \(\tau\), a finite choice
\[
 N_{\mathrm{jet}}\ge
 \Delta^{-1}\log\frac{M_{\mathrm{src}}}{\Delta\tau}
 \tag{14}
\]
suffices. This order can be enormous, of exponential size in a power
of \(\log n\). The representation contract permits exactly that setup
cost and imposes no such order on the retained state.

At the tensor angular grid with \(2J+1\) nodes in each variable,
compute the derivatives in (12) by differentiating the original ODE
at initialization. Evaluate the finite sums at the \(p+1\) temporal
interpolation nodes and apply the finite scalar transforms. Taking
\(\tau\le \epsilon/[C(p+1)(2J+1)^{d-1}]\) absorbs their norms.
The resulting tensor interpolant has the degrees (7) and coordinate
error at most \(\epsilon\), after reserving the other error fractions
for (4) and (5).

Every apparent temporal nodal value in this construction is a finite
formula in initialized derivatives. No original trained snapshot,
integrated reference trajectory, or actual positive-time ODE solution is
an input. Every derivative in (12) is allowed under the exact-real setup
contract; analyticity supplies its existence. The scalar transforms and
high-order jets are discarded after the final coefficient vectors are
formed.

This also verifies the crucial paired-image condition. Use the same
grid, orders, truncation, and scalar linear operations on a source \(S\)
and \(W_0S\). Since \(W_0\) is independent of time and angles, their
coefficient vectors are exactly \(u\) and \(W_0u\). Use the same procedure
on each backward pair \(S,W_0^\top S\). Both members have their own
coordinate approximation estimate; no coordinate estimate is inferred
from an operator norm. This remains exact despite the nodal truncation.

## 4. Positive selection, initialized training pass, and stored state

For layer \(\ell\), take the real span \(S_\ell\) of its coefficient
vectors. Include each initialized training activation in its own layer,
every corresponding initialized forward image in the next layer, and
the columns of \(A_0\) in \(S_1\). These finitely many additions preserve
\[
 \dim S_\ell\le R=C\lambda^{d(L+5)+1}.
 \tag{15}
\]
Choose \(U_\ell^\top U_\ell/n=I\). Start with mass \(1/n\) at each
original coordinate and match the constant and symmetric products of
the basis columns. Linear dependence of more than
\(1+r_\ell(r_\ell+1)/2\) moment vectors allows a nonzero signed mass
change preserving all moments; its constant component makes its sum
zero. Moving to the first zero mass preserves nonnegativity and removes
a node. Finite repetition gives positive remaining masses \(D_\ell\)
on \(I_\ell\), total mass one, with
\[
 U_{\ell,I_\ell}^{\top}D_\ell U_{\ell,I_\ell}=I,\qquad
 N_\ell=|I_\ell|\le1+r_\ell(r_\ell+1)/2=O(R^2).
 \tag{16}
\]
Thus every pairing of vectors in \(S_\ell\) is exactly preserved.

The proposed initialized edge is
\[
 B_0^{(\ell)}=
 U_{\ell,I_\ell}
 \left(\frac{U_\ell^\top W_0^{(\ell)}U_{\ell-1}}n\right)
 U_{\ell-1,I_{\ell-1}}^\top D_{\ell-1}.
 \tag{17}
\]
The basis maps on both sides are isometries in their respective weighted
norms, and the middle matrix has operator norm at most
\(\|W_0^{(\ell)}\|_{\mathrm{op}}\). Equation (17) therefore has the same
bound. If \(u\in S_{\ell-1}\) and \(W_0^{(\ell)}u\in S_\ell\),
then \(B_0^{(\ell)}u_{I_{\ell-1}}=(W_0^{(\ell)}u)_{I_\ell}\).
Its weighted adjoint gives the exact analogous reverse identity.
These statements concern paired sources, not an assumed invariant
subspace for arbitrary vectors.

With \(A_C(0)=A_{0,I_1}\), the initialized first preactivations match
exactly. Forward induction using the added training vectors gives the
entire initialized training pass and its top-feature Gram exactly.
The first-weight RMS norm is also preserved, since its columns were
included. The selected network thus inherits every initialization bound
needed for its own fitting argument.

The runtime has the weighted adjoint
\(B^{(\ell)*}=D_{\ell-1}^{-1}B^{(\ell)\top}D_\ell\), prediction
\(w_C^\top D_Lh_C^{(L)}\), and equations
\[
 \dot A_C=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^\top,\quad
 \dot B_C^{(\ell)}=\frac2m\sum_a c_{C,a}
        \delta_{C,a}^{(\ell)}h_{C,a}^{(\ell-1)\top}D_{\ell-1},\quad
 \dot w_C=\frac2m\sum_a c_{C,a}h_{C,a}^{(L)} .
 \tag{18}
\]
Here \(c_{C,a}=y_a-f_C(x_a)\), and every feature and response is
computed from this smaller model. Sample averaging remains \(2/m\);
neuron masses replace the normalized neuron contractions only. There is
no rescaling of physical time.

After setup, the retained real coordinates number at most
\[
 dN_1+\sum_{\ell=2}^L N_\ell N_{\ell-1}+N_L
          +\sum_\ell N_\ell+O(md+m)
 \le CR^4
 \le C[\log(en)]^{\,4[d(L+5)+1]}.
 \tag{19}
\]
This includes all moving dense edge matrices and all fixed masses.
An optional copy of each small initialized matrix has the same order.
The full-width arrays, coefficient vectors, basis matrices, cubature
workspaces, and jets are discarded. Original neuron indices are setup
metadata and are not needed to evolve the resulting matrices. Activations
and fixed data have width-independent descriptions. There is no hidden
original-width runtime state. The exponent is fixed, so (19) is \(o(n)\).

## 5. Independent fitting and full deterministic comparison

The bridge's fitting argument is valid for arbitrary positive masses.
Write \(\|u\|_{D_\ell}^2=u^\top D_\ell u\) and
\[
 \|B\|_{\mathrm{HS},D}
   =\|D_\ell^{1/2}BD_{\ell-1}^{-1/2}\|_F.
 \tag{20}
\]
The rank-one update \(\delta h^\top D_{\ell-1}\) has norm
\(\|\delta\|_{D_\ell}\|h\|_{D_{\ell-1}}\). Until operator norms leave
a fixed tube, if \(S(t)=\int_0^t\|c_C(s)\|_m\,ds\), zero readout and
bounded activations give \(\|w_C\|_\infty\le CS\). Bounded gates and
operators give all backward RMS bounds \(CS\), hence first-weight and
hidden-edge displacements \(CS^2\). Forward subtraction keeps training
features and their readout Gram within \(CS^2\) of initialization.

The actual tangent matrix is the sum of the top-feature Gram and
positive semidefinite tensor-product Grams. In particular its first-layer
term is the Gram of \(\delta_a^{(1)}\otimes v_a\); it is not required
to be diagonal. The initial readout gap therefore implies
\(\|c_C(t)\|_m\le Ye^{-\kappa t}\) and \(S(t)\le CY\) while in the
tube. Choosing fixed \(Y_*>0\) small closes it. This proves fitting and
integrability of all parameter velocities, with constants independent
of the smallest selected mass. At each finite \(n\), positive masses
make the bounded weighted state a bounded finite-dimensional state, so
local smoothness also gives global continuation. The same argument
applies to the full model.

For completeness, every source-selection defect used by the bridge
can be tracked explicitly. Coordinate error \(\epsilon\), total selected
mass one, and (16) imply that empirical and selected RMS norms of a source
differ by at most \(2\epsilon\). Inserting approximants in a pair gives
\[
 \left|u_I^\top Dv_I-\frac1n u^\top v\right|\le C\epsilon,
 \tag{21}
\]
uniformly for the required sources at arbitrary two times. Backward
source norms stay \(O(Y)\), since \(\epsilon\le Y\) for large \(n\)
when \(Y>0\). Integrating top training-feature approximants with the
original residuals places \(w(t)\) within coordinate distance
\(CY\epsilon\) of \(S_L\). Finite Riemann sums and closedness of
\(S_L\) justify this without a measurable choice of approximants.

Define the proof-only retained reference edge
\[
 B_R^{(\ell)}(t)=B_0^{(\ell)}
 +\frac2m\sum_a\int_0^t c_a(s)
    \delta_a^{(\ell)}(s)_{I_\ell}
    h_a^{(\ell-1)}(s)_{I_{\ell-1}}^\top D_{\ell-1}\,ds,
 \tag{22}
\]
and \(A_R=A_I,\ w_R=w_I\). Fixed-edge paired approximation and (21)
give \(O(\epsilon)\) forward, backward, and output defects for this
reference. The learned forward term uses a past training activation
paired with a present query activation. The learned reverse term uses
a past backward response paired with a present one. The total residual
activity is \(O(Y)\), so these errors have no factor \(T\).
The reference edges are bounded in operator norm. No object in (22)
is stored or supplied to the runtime (18).

Let \(d(t)\) be the sum of the weighted block distances from (18) to
this reference. Forward differences are at most \(C(d+\epsilon)\).
For the backward difference use exactly
\[
 \delta_C-\delta_I
 =\phi'(z_C)\odot(k_C-k_I)
  +[\phi'(z_C)-\phi'(z_I)]\odot k_I.
 \tag{23}
\]
The changed gate is multiplied by the actual original carrier. Hence
downward induction through fixed depth gives
\[
 \|\delta_C-\delta_I\|_D
          \le C(1+M_{\mathrm{car}})(d+\epsilon).
 \tag{24}
\]
The factor \(M_{\mathrm{car}}\) is added in each recursion, not
multiplied by a further carrier factor. This calculation requires no
compressed maximum bound and no inverse minimum mass.

Together with (21), equation (24) bounds the difference of the actual
tangent matrices by \(C(1+M_{\mathrm{car}})(d+\epsilon)\). For
\(u=c_C-c_n\), both flows use their own residuals, and exactly
\[
 \dot u=-\frac2m K_Cu-\frac2m(K_C-K_n)c_n.
 \tag{25}
\]
The preserved compressed Gram gap gives
\[
 D^+\|u\|_m\le-\kappa\|u\|_m+
 C(1+M_{\mathrm{car}})\rho_n(t)(d+\epsilon),
 \qquad \rho_n(t)=\|c_n(t)\|_m.
 \tag{26}
\]
Integrating and using \(u(0)=0\) yields
\[
 \int_0^t\|u\|_m
 \le C(1+M_{\mathrm{car}})
                  \int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
 \tag{27}
\]
Subtracting all three update families in (1) and (18) gives
\[
 d(t)\le C\int_0^t\|u\|_m+
 C(1+M_{\mathrm{car}})\int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
 \tag{28}
\]
Thus Gronwall uses the finite measure \(\rho_n(s)\,ds\), of total
mass \(O(Y)\), rather than physical time. Equations (27)--(28) and
the output defect prove
\[
 \sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
 \le C(1+M_{\mathrm{car}})
              e^{C(1+M_{\mathrm{car}})Y}\epsilon
 \le C(1+M_{\mathrm{car}})e^{CM_{\mathrm{car}}}\epsilon .
 \tag{29}
\]
This verifies the entire deterministic bridge, including selection bias,
both matrix orientations, and all learned layers.

## 6. Error, endpoints, and quantifiers

On (2), choose the fixed \(D\) in (6) larger than the coefficient of
\(\sqrt\lambda\) in the exponential factor of (29). Then its right side
is at most \(C/\sqrt n\). The remaining factor
\((1+\sqrt\lambda)/\lambda\) is bounded, and increasing \(D\) supplies
any desired fixed margin. This stronger source accuracy did not change
the power in (8), because its logarithm is still \(O(\lambda)\).

Each network independently has uniformly bounded query derivatives on
the real state tube and integrable parameter speeds. Its query tail is
at most \(CYe^{-\kappa T}\), uniformly over the input sphere. Choose
\(C_T\) with \(\kappa C_T>1/2\). Comparing at time \(T\) and adding
the two tails gives \(C/\sqrt n\) for every \(t\ge T\), including
both fitted limits. Both networks continue their own dynamics after
\(T\); neither is frozen, externally driven, or compared at a different
clock.

The initialization, source, and carrier events each have probability
tending to one. Their finite intersection consequently has probability
at least \(1-\eta\) for all sufficiently large \(n\). The threshold may
depend on fixed \(y,\eta\); the conclusion makes no assertion of a
simultaneous event across independently initialized widths. Label signs
are unrestricted, zero components cause no issue, and \(Y=0\) is the
separate stationary zero-prediction case. The small-label restriction
is a fixed upper bound on \(Y\), independent of width.

## 7. Added activation, data, and feature claims

The listed concrete activations satisfy the required strip hypothesis.
For tanh and sigmoid choose a fixed strip avoiding their nearest poles
and use their exponential formulas. Integrating the derivative of erf
vertically from the real axis gives
\[
 |\operatorname{erf}(x+iy)|
 \le1+\frac2{\sqrt\pi}|y|e^{y^2}.
 \tag{30}
\]
For arctan on \(|y|\le b<1\), the analytic branch real on the real
axis has \(|(1+z^2)^{-1}|\le(1-b^2)^{-1}\), so its modulus is at most
\(\pi/2+b/(1-b^2)\). Finally
\(|\sin(x+iy)|^2=\sin^2x+\sinh^2y\le\cosh^2b\).
Finite sums and real affine rescalings preserve boundedness on a
sufficiently narrow common strip. Sine explicitly shows that monotonicity
and absence of real derivative zeros are not necessary.

For nonconstant activations in this bounded class, pairwise
nonproportional nonzero inputs imply the initialized Gram gap.
To verify the first layer, suppose a continuous ridge combination
\(\sum_a b_a\phi_1(u^\top v_a)\) vanishes for every \(u\).
For a nonzero coefficient \(b_a\), choose, for each \(j\ne a\),
a direction orthogonal to \(v_j\) but not to \(v_a\). Applying the
corresponding finite differences eliminates every other term and implies
that all \((m-1)\)-fold scalar differences of \(\phi_1\) vanish.
Mollification followed by differentiation in the increments makes each
mollification a polynomial of degree at most \(m-2\). Interpolation
at \(m-1\) fixed distinct real points and convergence of mollification
give the same conclusion for \(\phi_1\). A bounded nonconstant function
cannot be that polynomial. The \(m=1\) case follows from a nonzero
Gaussian square expectation. Full support of the first Gaussian vector
turns a zero Gram quadratic form into the continuous identity just ruled
out. Once a covariance is positive definite, full Gaussian support on
\(\mathbb R^m\) and variation of one coordinate prove positivity after
each nonconstant activation. This reproduces the manuscript argument
and requires no \(m\le d\). On the sphere, distinct inputs with no
antipodal pair meet the criterion.

The feature-motion assertion has the explicitly narrower assumption of
linearly independent inputs and a nonzero label vector. Put
\[
 v=\dot w(0)=\frac2m\sum_a y_a h_a^{(L)}(0),\quad
 p_a^{(\ell)}=\dot k_a^{(\ell)}(0),\quad
 d_a^{(\ell)}=\dot\delta_a^{(\ell)}(0).
 \tag{31}
\]
The positive initialized training Gram gives \(v\ne0\). A nonconstant
holomorphic activation has isolated derivative zeros and isolated value
zeros unless the value function has no zeros. Each initialized
preactivation has a nondegenerate conditional Gaussian law: the previous
activation vector is nonzero almost surely, inductively from nonzero
inputs. Consequently every initialized gate is nonzero almost surely.
The Gaussian square hidden matrices are invertible almost surely.
The backward recurrence from \(p_a^{(L)}=v\) therefore makes every
\(d_a^{(1)}\) nonzero.

Writing the first acceleration as
\[
 \ddot A(0)=\frac2m
       [\,y_1d_1^{(1)},\ldots,y_md_m^{(1)}\,]
       [\,v_1,\ldots,v_m\,]^\top
 \tag{32}
\]
shows it is nonzero: the second matrix has full column rank and the
first has a nonzero column. All hidden parameter velocities vanish at
zero because \(w_0=0\). Differentiating the forward pass twice and
pairing it with (31) therefore gives, for each prefix,
\[
 \frac2m\sum_a y_a\,
       \frac{p_a^{(\ell)\top}\ddot h_a^{(\ell)}(0)}n
   =\frac{\|\ddot A(0)\|_F^2}{n}
       +\sum_{s=2}^{\ell}\|\ddot W^{(s)}(0)\|_F^2>0.
 \tag{33}
\]
Indeed the current-edge contribution is
\(\langle\ddot W^{(\ell)},
 (2/mn)\sum_a y_a d_a^{(\ell)}
                       h_a^{(\ell-1)\top}\rangle_F
=\|\ddot W^{(\ell)}\|_F^2\);
the remaining contribution descends by the initialized backward adjoint.
The base case is \(\|\ddot A\|_F^2/n\). This proof works for
nonorthogonal inputs too.

Adding the finitely many \(d_a^{(\ell)}\) and their initialized reverse
images to the spaces preserves the selected values of (31), by downward
induction from the already matched top features. It also preserves the
positive first-acceleration norm, since each column of \(\ddot A\)
is a linear combination of the \(d_a^{(1)}\). The same weighted
calculation gives (33) in the smaller network, with its weighted
first-weight and Hilbert--Schmidt norms. Thus at every hidden layer,
some training feature has nonzero second derivative. These finitely many
extra source vectors do not change (19). This is a finite-width nonzero
motion certificate, with no claimed width-independent lower bound.

## 8. Boundary of this check

The full conditional implication, the Section 5 examples and sufficient
Gram criterion, and the stated feature-motion subcase pass reconstruction.
The complex-source proposition remains a named input here even if its
separate checker subsequently passes it. This report must not be cited
as its proof.

Nothing checked here supplies the analogous result for merely bounded
\(C^3\) activations, growing depth/data/input dimension, efficient or
bounded-precision setup, population centering, or an unchanged finite-order
Legendre closure. Nor does a conditional PASS itself promote any statement
into the maintained book or manuscript. No experiment, Git operation,
manuscript edit, or author-file edit was performed in this check.

## 9. Verified status revision after the assembly check was frozen

The preceding complete report was frozen at SHA-256
002ba4afbc4f3265e473be177f2a7baa1c9876569120575e401d8c43fcd846a4
before reading the separate source reconstruction. I then read the complete
DEEP_COMPLEX_SOURCE_CHECK.md, including its activation supplement check,
at SHA-256
b91d5730d35baf7a2c1ee544fd8c3bdca134ca0680e535eec850205770b88015.
It passes both full source inputs. The author subsequently updated
GENERAL_ANALYTIC_COMPRESSION.md to SHA-256
4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53.

I verified that this assembly revision changes only the status header,
the theorem/section labels, the source-status sentences at the start of
Section 2, and the status discussion in Section 6. Reversing those text
changes in memory reproduces the previously checked SHA-256
bae30debcb714f3ecb857fa600b29685cd7e1d392a5934761962595002c8bc5a
exactly. No equation, hypothesis, quantifier, construction, state count,
or mathematical conclusion changed. The present full conditional PASS
therefore applies to that final version. Its internally checked theorem
status is supported by this assembly reconstruction together with the
separate complete source reconstruction; this report still does not replace
the source proof.

After this report's original freeze, the depth author also updated the two
source-file status headers and made the two explicit scope clarifications
requested by the separate checker. A sphere anchor need not be a training
input; forward applications of the incoming-row adjoint probes belong to
the existing enlarged linear Gaussian event. These changes preserve the
historical source versions and do not change the assembly input. The
separate checker is responsible for confirming those source-file revisions.
