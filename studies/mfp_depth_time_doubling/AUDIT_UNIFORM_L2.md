# Adversarial audit of the depth-two uniform-remainder attempt

## Scope

This audit checks UNIFORM_L2.md for three possible overclaims:

1. treating representation-dependent source partials as intrinsic at a
   singular Gram;
2. confusing an old-source cylindrical partial with a moving-query
   parameter tangent;
3. inferring the uniform \(t^4|h|^5\) remainder from the causal
   step-factorization without proving the high-moment mixed jets.

## 1. Syntactic causal divisibility

**Result: pass, with the stated scope.**

In the fixed chronological source expression, an old reverse source
\(\chi_i\) first reaches a later bottom state through
\(u_{i+1}=u_i+\varepsilon_i d_i\). Thus
\(\partial_{\chi_i}u_s\) contains \(\varepsilon_i\) for \(s>i\).
The mutual induction in Lemma 3.1 then gives

\[
 \rho_{si}=\varepsilon_i\bar\rho_{si}.
\]

For an old forward source \(\xi_i\), the direct derivative at its source
time is \(a_i\phi''(z_i)\). At a later time, the \(j=i\) contribution to
\(z_s\) carries
\(\rho_{si}+\varepsilon_iQ_{is}\), while every \(j>i\) contribution
carries the inductive factor through \(\delta_j\). Hence

\[
 \sigma_{si}=\varepsilon_i\bar\sigma_{si}\qquad(i<s).
\]

The current response

\[
 \sigma_{ss}=\mathbb E[a_s\phi''(z_s)]
\]

is correctly kept separate and unweighted.

The indices and initial conditions in (4.1)--(4.8) are consistent:

\[
 p_{i+1}^i=\phi'(u_i),\qquad q_i^i=a_i\phi''(z_i),
\]

and the \(j=i\) terms in (4.6)--(4.7) are separated correctly from the
later step-weighted terms.

## 2. Singular-Gram interpretation

**Result: pass after qualification.**

An individual formal partial such as
\(\partial_{\chi_i}x_s\) can depend on the chosen redundant source
representation when its Gram is singular. UNIFORM_L2.md now describes
Lemma 3.1 as a syntactic statement in one fixed inverse-free chronology.
It claims intrinsic meaning only for the aggregate response fields

\[
 \sum_{i<s}\rho_{si}\delta_i,\qquad
 \sum_{i\le s}\sigma_{si}x_i,
\]

which equal the fixed adjoint actions. This is the correct distinction.

## 3. Moving-query derivatives

**Result: no false identification.**

Differentiating a moving fixed-operator action produces new raw variables

\[
 I(\partial_\lambda x_s),\qquad
 J(\partial_\lambda\delta_s).
\]

This is not the same as differentiating with respect to one old formal
source while holding later source coordinates fixed. Section 6 explicitly
records the additional mixed fields

\[
 \partial_\lambda\partial_{\chi_i}x_s,\qquad
 \partial_\lambda\partial_{\xi_i}\delta_s
\]

and does not claim that (4.1)--(4.8) already control them.

## 4. Uniform moment closure

**Result: open.**

The horizon-uniform \(L^2\) parameter estimate (5.8) is valid, as is the
weighted-Gaussian exponential estimate (5.12). Neither controls the
products

\[
 a_s\phi''(z_s)\zeta_s^i,\qquad
 r_s\phi''(u_s)p_s^i
\]

and their mixed moving-query/\(h\)-jets. At highest \(h\)-order, the two
response families are coupled through terms involving
\(\partial_h^3\bar\rho\) and \(\partial_h^3\bar\sigma\). No explicit
horizon-independent inverse bound for this coupled causal block is proved.

Consequently the note correctly stops before asserting

\[
 |F_{t,2}(2h)-F_{2t,2}(h)-\kappa_{\phi,2,t}h^3|
 \le C_{\phi,2}t^4|h|^5.
\]

## Verdict

The new causal factorization and source-tangent recursions pass the
adversarial checks within their syntactic scope. The requested depth-two
uniform remainder does not pass because its mixed generated/source
high-moment estimate remains unproved. The open verdict in UNIFORM_L2.md
is therefore the rigorous one.
