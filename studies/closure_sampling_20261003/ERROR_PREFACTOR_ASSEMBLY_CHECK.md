# Assembly check for the polynomial error prefactor

2026-10-04. Scoped internal assembly reconstruction. **PASS for the assembly
obligations checked below**, conditional on the new deterministic comparison
in `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md`. A separate assigned checker is
reconstructing that comparison's principal cancellation and differential
inequalities. This report is not a promotion review or a new independent
review of the inherited source theorem.

The geometric route was read completely at SHA-256
`2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c`.
The complete inherited scientific inputs are the five files and versions
recorded in `ERROR_PREFACTOR_COST_ROUTE.md`: the quadratic storage runtime,
depth-independent source theorem, input/depth synthesis, sample-count
synthesis, and original analytic-compression synthesis. That earlier cost
report was this checker's independent frozen work, not an author-supplied
verdict. The geometric source is new authorized input after that freeze.
No unassigned linked scientific source, other study, experiment, or Git
operation was used. Only this assigned report was written for this check.

The earlier source-tolerance fallback is unnecessary if the geometric
comparison passes its separate algebra reconstruction. No tighter tolerance
or extra retained source vector is used in the assembly below.

## 1. Objects, normalization, and the inherited event

The reference remains the realized width-\(n\) dense network with Gaussian
first weights, Gaussian hidden mixers of entry variance \(1/n\), zero
readout, bounded strip-holomorphic activations, and the canonical physical
gradient flow. The normalized inputs are \(v=x/\sqrt d\in S^{d-1}\).
Depth \(L\), dimension \(d\), sample count \(m\), the training data and
labels are fixed before the width limit.

Let \(Y=\|y\|_2/\sqrt m>0\), let \(\gamma>0\) be the smallest
eigenvalue of the initialized limiting top-feature covariance, and set

\[
\lambda=\min(1,\gamma/m),\quad s=Y/\lambda,\quad
\ell_n=\log(en),\quad q_n=\ell_n+\log(e/\lambda).
\]

Structural constants may depend on \(d,L\) and activation bounds, not on
\(m,\gamma,Y,n\) or elapsed time. The regime is \(Y\le c\lambda\).
For tanh the gap cap is inactive. For general bounded activations,
\(\gamma/m\le C_\phi\), so a structural adjustment of the constant in
\(Y\le c\gamma/m\) gives this capped regime even if the cap is active.

For each fixed confidence \(1-\eta\), the inherited source event has
probability at least \(1-\eta\) for all sufficiently large widths. It
supplies through \(T=C\lambda^{-1}\ell_n\):

- source coordinate accuracy \(\epsilon=n^{-1}\), including the paired
  initialized forward and reverse matrix actions and exact initial
  training features;
- the common time/input-angle analytic radius \(c\ell_n^{-1/2}\);
- original real-trajectory fitting, bounded operators, the Gram margin,
  and carrier bound \(M\le1+Cs\sqrt{\ell_n}\);
- the refined layer-space dimension used in Section 4 below.

These are the same inherited probability and finite-network source inputs
as in the existing strict root-width theorem. The new deterministic proof
does not add a source family or an independent stochastic event.

## 2. Exact source isometry transfers the required energy bounds

Write \(\|u\|_n^2=n^{-1}\sum_i u_i^2\) for the original neuron norm.
At the top layer, the fixed selected metric \(H\) obeys
\(\|s_I\|_H=\|s\|_n\) for every vector \(s\) in the selected source
space, and \(\|e_I\|_H\le2\|e\|_\infty\) for every error vector.
Both properties are explicit consequences of the runtime construction.

Let \(V_n\) have columns \(h_{n,a}/\sqrt m\) in the original neuron
Hilbert space and \(V_R\) have columns \(h_{n,a,I}/\sqrt m\) in the
selected Hilbert space. For each column choose its source approximant
\(\widetilde h_a\), with coordinate error at most \(\epsilon\).
The normalized column-error operators have Hilbert--Schmidt norms at
most \(\epsilon\) originally and \(2\epsilon\) after selection.
Inserting the same linear combination of \(\widetilde h_a\) on both
sides and using exact isometry therefore proves, for every
\(b\in\mathbb R^m\),

\[
\|V_Rb\|_H\le\|V_nb\|_n+3\epsilon\|b\|_2.
\tag{1}
\]

This is an operator estimate, not a separate-column maximum multiplied by
\(\sqrt m\). The normalization of the columns is essential.

For completeness, the dense path-length estimate follows directly from
its exact physical flow. Define its parameter-velocity norm by

\[
\|\dot\theta_n\|_{\rm par}^2
 ={\|\dot A_n\|_F^2\over n}
   +\sum_{\ell=2}^L\|\dot W_n^{(\ell)}\|_F^2
   +{\|\dot w_n\|_2^2\over n}.
\]

Expanding the squared velocities gives the energy identity
\(-d\rho_n^2/dt=\|\dot\theta_n\|_{\rm par}^2\), where
\(\rho_n=\|c_n\|_2/\sqrt m\). The inherited readout Gram margin
gives \(-\rho_n'\ge2g\rho_n\), with \(g\ge c_0\lambda\).
Thus

\[
\|\dot\theta_n\|_{\rm par}^2
 =2\rho_n(-\rho_n')\le{(-\rho_n')^2\over g},\qquad
\int_0^\infty\|\dot\theta_n\|_{\rm par}\,dt
 \le {Y\over\sqrt g}\le C{Y\over\sqrt\lambda}.
\tag{2}
\]

The continuous zero-residual interpretation covers a trajectory that
reaches zero. Equation (2) uses the original gradient flow, not a
self-adjoint-gate assertion for the selected metric.

Since \(w_n(0)=0\), the integral of the source approximants against
\((2/m)c_{n,a}\) is a vector in the fixed top source space and
approximates \(w_n(t)\) with coordinate error at most
\(C\epsilon\int_0^T\rho_n\le C\epsilon s\). Exact isometry and (2)
therefore give

\[
\|w_{n,I}(t)\|_H\le C Y/\sqrt\lambda+C\epsilon s.
\]

Under \(\epsilon\le Y\le c\lambda\), the last term is absorbed:
\(\epsilon s/(Y/\sqrt\lambda)=\epsilon/\sqrt\lambda\le c\).
Selected backward source vectors similarly satisfy

\[
\|\delta_{n,a,I}^{(\ell)}\|_{H_\ell}
 \le\|\delta_{n,a}^{(\ell)}\|_n+3\epsilon
 \le CY/\sqrt\lambda.
\tag{3}
\]

Their original RMS bound follows from bounded backward operators and the
readout part of (2). The rank-one hidden update directions consequently
have norm \(CY/\sqrt\lambda\). Their normalized sample-column operator
has the same bound by its Hilbert--Schmidt norm, with no factor \(m\).

The specific selected reference velocity needed by the geometric proof is

\[
\nu(t)=\|V_R(t)c_n(t)/\sqrt m\|_H.
\]

Apply (1) with \(b=c_n/\sqrt m\) and use
\(2V_nc_n/\sqrt m=\dot w_n\). Then

\[
\int_0^T\nu\,dt
\le\frac12\int_0^T\|\dot w_n\|_n\,dt
       +3\epsilon\int_0^T\rho_n\,dt
\le C{Y\over\sqrt\lambda}+C\epsilon s
\le C{Y\over\sqrt\lambda}.
\tag{4}
\]

Hence \(\int\nu/\sqrt\lambda\le Cs\), exactly the claimed scale.
This verifies the nontrivial source-to-comparison bridge in the route's
equations (8)--(9). No smaller approximation tolerance is required.

## 3. Raw error, infinite time, and width qualifications

Conditional on the separately checked main comparison, its raw bound is

\[
\sup_{t\ge0,v}|f_C-f_n|
\le C\lambda^{-1/2}\epsilon e^{Cs(1+M)}
       +CY\lambda^{-3/2}e^{-c\lambda T}.
\tag{5}
\]

The tail calculation in its Section 6 is consistent with the independent
projection-derivative calculation in this checker's frozen cost route:
\(\|\dot T_C\|\le C\lambda^{-1}\|\dot V_C\|\) and
\(\|\dot P_C\|\le C\lambda^{-1/2}\|\dot V_C\|\) imply
\(\|\dot{\widehat w}_C\|\le C\lambda^{-1/2}\rho_C\).
Every sphere-query feature has bounded norm and derivative at most
\(C(Y/\sqrt\lambda)\rho_C\). Integrating therefore gives the second
term of (5). Both systems continue autonomously after \(T\); their
limiting outputs are included by this uniform tail. No source statement
after \(T\), trained endpoint, or trajectory freeze is used.

At unchanged tolerance \(\epsilon=n^{-1}\), the first term in (5) is

\[
C\lambda^{-1/2}n^{-1}
 \exp\{Cs+Cs^2\sqrt{\ell_n}\}.
\]

For \(b=Cs^2\),
\(b\sqrt{\ell_n}\le\ell_n/2+b^2/2\). Therefore this is at most
\(C\lambda^{-1/2}n^{-1/2}e^{Cs+C's^4}\), whose last exponential is
structural because \(s\le c\). This inequality holds directly for every
\(n\ge1\); it imposes no condition \(\log n\gtrsim\lambda^{-a}\).
Taking a sufficiently large structural multiplier in
\(T=C\lambda^{-1}\ell_n\) makes the second term at most
\(C\lambda^{-1/2}n^{-1}\). Thus

\[
\sup_{t\in[0,\infty],\ v\in S^{d-1}}|f_C(t,v)-f_n(t,v)|
\le {C\over\sqrt{\lambda n}}.
\tag{6}
\]

The source tolerance condition requires \(n\ge1/Y\). This is the
explicit admissibility condition for the existing \(n^{-1}\) tolerance;
it does not absorb an exponential error constant. The inherited stochastic
source threshold remains unquantified and may depend on fixed data,
labels, gap and confidence. It would be incorrect to describe the result
as having a fully polynomial width threshold. The new runtime argument
introduces no exponential width condition of its own.

For each fixed dataset and each fixed \(\eta>0\), the conclusion holds
with probability at least \(1-\eta\) for every sufficiently large
\(n\), including the preceding explicit tolerance condition. This is
neither one event over independent widths nor a uniform growing-dataset
claim. On the stated structural carrier event, \(C\) can be structural;
retaining \(C_\eta\) is a harmless weaker confidence convention.

## 4. Runtime and the complete unchanged retained count

The construction still stores only the same moving first weights, hidden
matrices, raw readout and internal residual, the same fixed metrics, and
training data and matrix-solve caches. Its output uses the same corrected
readout; its residual equals its own label-minus-prediction vector. The
reference network, canonical mobilities and physical clock are unchanged.
The proof variables \(V_R,\nu,p,\zeta\) are not runtime coordinates.
In particular \(\nu\) is used only to bound a proof integral, not supplied
as an external signal to the compressed model.

At \(\epsilon=n^{-1}\), the already proved source degree bounds remain

\[
p\le C\lambda^{-1}\ell_n^{3/2}q_n,\qquad
J\le C\ell_n^{1/2}q_n,
\]

so the layer-space dimension remains
\(R\le C\lambda^{-1}\ell_n^{d/2+1}q_n^d\), including the exact
initialization additions. The existing construction selects \(O(R)\)
neurons and stores \(O(R^2)\) total fixed and moving coordinates.
The full bound, before any logarithmic simplification, is therefore

\[
\boxed{\quad
\operatorname{size}\le
C\lambda^{-2}\ell_n^{d+2}
 [\ell_n+\log(e/\lambda)]^{2d}+Cm(d+1).
\quad}
\tag{7}
\]

For \(\ell_n\ge\log(e/\lambda)\), equivalently \(n\ge1/\lambda\),
this gives

\[
\operatorname{size}\le C\lambda^{-2}\ell_n^{3d+2}+Cm(d+1).
\tag{8}
\]

Only a logarithmic gap factor is simplified in (8). There is no additive
accuracy-degree term involving a positive power of \(1/\lambda\), and
no extra training-only source term. With \(\lambda=\gamma/m\), (6)
has prefactor \(C\sqrt{m/\gamma}\), while (7)--(8) keep the previous
quadratic sample prefactor \(Cm^2/\gamma^2\).

## 5. Verdict and boundaries

All assigned assembly obligations pass: exact same runtime and reference;
unchanged tolerance; selected readout and velocity energy scales;
whole-sphere physical-time comparison; polynomial tails including endpoints;
honest fixed-data probability/width quantifiers; and the full unchanged
retained count, including logarithmic gap dependence.

The report does not replace the separate independent reconstruction of
the new matched readout/residual cancellation. A flaw in that comparison
would invalidate the conditional use of (5), while leaving the source
isometry calculations (1)--(4), tail refinement and count audit intact.
No optimality, lower bound, growing-dimensional uniformity, efficient
preprocessing or promotion claim is made.
