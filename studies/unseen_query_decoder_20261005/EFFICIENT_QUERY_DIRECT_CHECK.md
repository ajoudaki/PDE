# Scoped reconstruction of the real-time response claims

2026-10-06. Independent internal check of the new bounded mathematical
claims in `EFFICIENT_QUERY_DIRECT.md`. This is not a reconstruction of the
inherited dense-network estimates, a full decoder review, or a promotion
review.

**Verdict:** the displayed Hessian normalization, integrable curvature
bound, Gauss--Newton contraction, Dyson truncation orders, scalar resolvent
identity, response-trace error, and rank example reconstruct correctly
under their stated hypotheses. The \(O(\log^5 n)\) scalar coefficient
count also reconstructs, conditional on the common complex-time domain
and uniform complex field bounds invoked in the candidate's Section 4.
Those analytic assumptions are additional to its real residual/carrier
bounds (3). No correction of the displayed mathematical formulas is
required. The candidate correctly stops short of an efficient decoder.

## 1. Input and assumption boundary

The complete candidate was the only scientific input read for this check.
Its references to other files were not followed. In accordance with the
assignment, the following are assumptions here, not independently
verified source results:

- the actual normalized network, gradient flow, and activation class;
- uniform real mixer operator bounds and forward/backward RMS bounds;
- the residual integral and all-time carrier maximum bounds in (3);
- for the finite-horizon representation claim, a common complex-time
  neighborhood of \([0,T_n]\), with radius
  \(r_n=c/\sqrt{\log(en)}\), containing the required complex disks,
  on which the forward and backward fields have uniform complex RMS
  bounds and their layer formulas are holomorphic;
- the applicability of the stated response trace to the intended source
  fields and the separate prediction-tail estimate.

The candidate's SHA-256 at this check was
`8a027e2e2b92f538aecf2bde4fc305e9f064fd3f32cea0364b8e9b11331f840b`.

The last two items are not consequences of the real estimates proved
below. The analytic item is the conditional interface expressly used in
the candidate's Section 4; whether a referenced source supplies it is
outside this assignment's input scope.

The required research and proof skills had already been read in this
scoped task and were reused. The custom canonical-notation skill remains
unreadable with `Permission denied`; the supervisor's explicit notation
fallback is applied. No other new route output was read, and only this
check file was written.

## 2. Mobility coordinates and the Hessian

Write \(\theta_A=A/\sqrt n\) and \(\theta_w=w/\sqrt n\), with
the hidden matrices unchanged. The ordinary Euclidean gradient flow for
the loss \(\|e\|_2^2\) in these coordinates has physical mobilities
\((n,1,\ldots,1,n)\): for example,
\(\dot A=\sqrt n\dot\theta_A=-n\nabla_A\|e\|_2^2\).
Thus there is no unaccounted factor of \(n\) in the candidate's flow
equation.

For a variation \(\xi\) in the direct-sum parameter norm, the first
preactivation variation is \(\sqrt n\xi_Av_a\). Since
\(\|v_a\|_2=1\), its norm is at most \(\sqrt n\|\xi_A\|_F\).
At a later layer,

\[
 Dz^{(\ell)}[\xi]
   =\xi_{W^{(\ell)}}h^{(\ell-1)}
                         +W^{(\ell)}Dh^{(\ell-1)}[\xi].
\]

The RMS feature bound supplies \(\|h^{(\ell-1)}\|_2\le C\sqrt n\);
the matrix perturbation's operator norm is at most its Frobenius norm.
Induction using bounded activation slopes and fixed depth therefore gives

\[
 \|Dz^{(\ell)}[\xi]\|_2+\|Dh^{(\ell)}[\xi]\|_2
                                  \le C\sqrt n\|\xi\|_2.   \tag{1}
\]

Differentiate each affine map and activation twice, and contract the
second variation backward. The local activation contribution is

\[
 \frac1n\sum_i k_{a,i}^{(\ell)}\phi_\ell''(z_{a,i}^{(\ell)})
                  Dz_{a,i}^{(\ell)}[\xi]Dz_{a,i}^{(\ell)}[\zeta].
\]

Its absolute value is at most
\(C\|k_a^{(\ell)}\|_\infty\|\xi\|_2\|\zeta\|_2\), by
(1) and Cauchy--Schwarz. A local hidden-matrix mixed term has the form
\(n^{-1}(\delta_a^{(\ell)})^T\xi_WDh^{(\ell-1)}[\zeta]\).
The two vector norms are \(O(\sqrt n)\) and the prefactor is
\(1/n\), so this term is at most
\(C\|\xi\|_2\|\zeta\|_2\). The readout mixed term has the same
bound because its physical variation is \(\sqrt n\xi_w\).

These are exactly the three types of terms in candidate equation (6).
The first affine preactivation has no second variation. Taking the
supremum over unit variations proves candidate equation (4), with the
direct-sum mobility norm as stated. Bounded real second derivatives are
sufficient here; the candidate's Cauchy argument supplies them from its
stated strip bound on the first derivative.

Since \(e_a=(f_a-y_a)/\sqrt m\), one obtains

\[
 \begin{aligned}
 \|\mathcal H(t)\|_{\rm op}
 &\le\frac1{\sqrt m}\sum_a |e_a(t)|\,
                                  \|\nabla_\theta^2f_a(t)\|_{\rm op}\\
 &\le C\rho(t)\left(1+\max_{a,\ell}
                                      \|k_a^{(\ell)}(t)\|_\infty\right).
 \end{aligned}                                                     \tag{2}
\]

The second line uses \(\sum_a|e_a|\le\sqrt m\rho\), so it does
not introduce an extra \(\sqrt m\) or \(\sqrt n\).

## 3. Curvature mass and the ordered expansion

Under the assumed all-time interface,

\[
 2\int_0^\infty\|\mathcal H(t)\|_{\rm op}\,dt
         \le CY(1+Y\sqrt{\log(en)})=O(\sqrt{\log(en)}),       \tag{3}
\]

where the last constant may depend on the fixed admissible problem.
For the finite-horizon alternative, the exact equation
\(\dot e=-2\mathcal J^T\mathcal J e\) implies
\(d\|e\|_2^2/dt=-4\|\mathcal J e\|_2^2\le0\), hence
\(\rho(t)\le Y\). Integrating (2) to
\(T_n=O(\log(en))\) then gives \(O(\log(en)^{3/2})\).
Both claimed mass bounds are valid, with their distinct assumptions.

The derivative of \(-2\mathcal J e\) is
\(-2(\mathcal J\mathcal J^T+\mathcal H)\); this verifies the
candidate's variational equation and its factors of two. The propagator
\(S\) of \(-2\mathcal J\mathcal J^T\) is contractive even when
these matrices do not commute at different times:

\[
 \frac d{dt}\|S(t,s)v\|_2^2
                   =-4\|\mathcal J(t)^TS(t,s)v\|_2^2\le0.
\]

Iterating the variation-of-constants equation inserts ordered factors
\(-2\mathcal H(u)\) separated by contractive \(S\)'s. Taking
operator norms leaves the ordered integral of the same nonnegative
scalar function \(2\|\mathcal H(u)\|_{\rm op}\) at every slot.
Partitioning the full integration cube into its ordering simplices gives
the factor \(1/k!\). Therefore

\[
 \|U_k(t,s)\|_{\rm op}\le M_n^k/k!,\qquad
 \left\|U(t,s)-\sum_{k=0}^{K}U_k(t,s)\right\|_{\rm op}
                                  \le\sum_{k>K}M_n^k/k!.     \tag{4}
\]

The finite bound on the series proves absolute convergence and permits
substitution into the integral equation. Uniqueness of the finite-time
linear equation identifies its sum with the actual derivative flow.
The uniform estimate in (4) is over finite \(0\le s\le t\); it
does not by itself assert an endpoint derivative.

For \(h=\log(en)\) and \(M_n\le C\sqrt h\), take the first
omitted index \(k_0\) proportional to \(h/\log(e+h)\). At
sufficiently large width,

\[
 \log\frac{k_0}{eM_n}\ge\tfrac13\log h,
 \qquad \frac{M_n}{k_0+1}\le\tfrac12.
\]

Using \(k!\ge(k/e)^k\), the tail is at most
\(2(eM_n/k_0)^{k_0}\le2e^{-c h/4}\). Increasing the fixed
constant \(c\) gives any prescribed \(n^{-A}\) error. This
reconstructs the stated \(O_A(\log n/\log\log n)\) order. With
\(M_n=O(h^{3/2})\), the candidate's alternative
\(k_0\ge\max\{2eM_n,(A\log n+2)/\log2\}\) bounds the tail
by \(2^{1-k_0}\le n^{-A}\), establishing its weaker order.

## 4. Kernel formula, resolvent, and the scalar coefficient count

The three types of parameter-gradient blocks are

\[
 \nabla_{\theta_A}e_a=\frac{\delta_a^{(1)}v_a^T}{\sqrt{mn}},
 \quad
 \nabla_{W^{(\ell)}}e_a
                =\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n\sqrt m},
 \quad
 \nabla_{\theta_w}e_a=\frac{h_a^{(L)}}{\sqrt{mn}}.
\]

Their Frobenius inner products at two times give candidate equation (16),
including the two separate \(1/n\) factors in its hidden-layer terms.

Integrating \(\partial_tS=-2\mathcal J\mathcal J^TS\), and
then left-multiplying by \(\mathcal J(t)^T\), gives exactly

\[
 b(t)=g(t)-2\int_s^t\mathcal K(t,u)b(u)\,du,
 \qquad g(t)=\mathcal J(t)^Tv.
\]

If \(\mathcal R=\mathcal K-2\mathcal K*\mathcal R\), with
\(*\) denoting this time-ordered convolution, substitution and a
finite-triangle interchange verify
\(b=g-2\mathcal R*g\). Thus the resolvent signs, orientation of the
matrix products, and the candidate's formulas (17)--(18) are consistent.

Under the explicitly assumed common complex domain and uniform complex
RMS bounds, the bilinear transpose pairings defining \(\mathcal K\)
are holomorphic and bounded: for complex vectors
\(|u^Tv|\le\|u\|_2\|v\|_2\), with no conjugation in the
analytic formula. If \(\|\mathcal K\|\le K_0\), its complex
straight-segment resolvent series has term bounds

\[
 K_0\frac{(2K_0|t-s|)^j}{j!}.
\]

The segment remains inside the convex rectangle. Uniform convergence on
compact subsets proves joint holomorphy, and summing gives
\(\|\mathcal R(t,s)\|\le K_0e^{2K_0|t-s|}\le n^C\) on the
prescribed time range. The fact that some patch pairs have \(t<s\)
causes no problem: the same analytic construction extends the resolvent
there, even though the real evolution only uses \(t\ge s\).

Covering each real time axis by inner half-radius patches requires

\[
 N=O(T_n/r_n+1)=O(\log(en)^{3/2})
\]

patches. On each product patch, Cauchy bounds and evaluation at half
the available radius bound the two-variable Taylor tail by
\(Cn^C2^{-p}\). Thus \(p=O_A(\log(en))\) in each variable
suffices for error \(n^{-A}\). There are \(N^2\) product patches,
\((p+1)^2\) scalar coefficients per kernel entry, and fixed \(m^2\)
entries. The result is

\[
 O\bigl(m^2N^2(p+1)^2\bigr)=O_{m,A}(\log(en)^5).             \tag{5}
\]

This is a scalar coefficient count and polynomial evaluation count once
the coefficients are supplied. It proves neither their causal
acquisition nor that this table replaces the parameter vectors in the
formula for \(S(t,s)v\). Finite-bit coefficient storage also requires
counting precision; (5) is not, as written, a total bit count.

## 5. Response trace and cancellation of the width factors

For a standard-Gaussian initialized hidden block \(M\), its injection
into the mobility initial parameter vector has norm \(1/\sqrt n\).
For a field \(c(s)\) depending on trained parameters, its implicit root
Jacobian is therefore

\[
 D_Mc(s)=D_\theta c(s)\,U(s,0)\,\mathcal I_M/\sqrt n,
\]

where \(\mathcal I_M\) is the isometric block injection. Replacing
\(U\) by an operator approximation with error \(\varepsilon\)
changes this Jacobian by at most \(A_c\varepsilon\) under (21).
The analogous error for \(h\) is \(A_h\varepsilon\).

For the first product-rule term of the trace, define
\((\mathcal B_hz)_{ij}=z_i h_j\). Then

\[
 \sum_{ij}\partial_{M_{ij}}c_i\,h_j
                   =\operatorname{tr}((D_Mc)\mathcal B_h),
 \qquad \|\mathcal B_h\|_{\rm op}=\|h\|_2.
\]

The resulting operator is \(n\times n\), so its trace is bounded
by \(n\) times its operator norm. Multiplying the bounds gives

\[
 n^{-3/2}\,n\,(A_c\varepsilon)\,(B_h\sqrt n)
                              =B_hA_c\varepsilon.           \tag{6}
\]

For the other product-rule term, use
\((\mathcal B'_cz)_{ij}=c_i z_j\) and obtain
\(B_cA_h\varepsilon\). This proves candidate equation (22)
without a lost power of width.

For the asserted field derivative scales, forward differentiation is
already (1). Backward differentiation gives

\[
 D\delta^{(\ell)}
 =\phi_\ell''(z^{(\ell)})\odot Dz^{(\ell)}\odot k^{(\ell)}
                         +\phi_\ell'(z^{(\ell)})\odot Dk^{(\ell)},
\]

and
\(Dk^{(\ell)}=\xi_W^T\delta^{(\ell+1)}
 +(W^{(\ell+1)})^TD\delta^{(\ell+1)}\).
The first term of the first equation costs one carrier maximum;
fixed-depth backward induction adds these costs rather than multiplying
them together. Therefore
\(A_c\le C(1+\max\|k\|_\infty)\), as claimed. A slightly
stronger inverse-polynomial tolerance for \(U\) absorbs this
\(O(\sqrt{\log n})\) factor.

Any explicit initialized-matrix dependence of the fields must indeed be
differentiated separately, as the candidate requires. The present estimate
holds the actual fields fixed and truncates only their implicit response;
it is not a joint error bound for approximate fields or a computation of
the trace itself.

## 6. The rank example

For \(d=m=1\), \(\phi_1=\tanh\), and \(\phi_2\) the identity,
the network is \(f=n^{-1}w^TW\tanh A\). The physical gradient flow
has, at its zero-readout initialization,

\[
 \dot w(0)=2yW_0\tanh A_0,
 \quad \dot A(0)=\dot W(0)=0,
 \quad \dot k^{(1)}(0)=2yW_0^TW_0\tanh A_0.                 \tag{7}
\]

Since differentiating twice in \(A/\sqrt n\) contributes a factor
\(n\), the first-coordinate Hessian block is exactly
\(\operatorname{diag}(k_i^{(1)}\tanh''A_i)\), without an extra
\(1/n\). Each \(A_{0,i}\) is nonzero almost surely. Conditional
on such an \(A_0\), each coordinate of
\(W_0^TW_0\tanh A_0\) is a nonzero polynomial in the matrix
entries, since evaluation at \(W_0=I\) is nonzero. Its zero set has
Lebesgue measure zero, and the Gaussian matrix law has a density.

Consequently each coordinate in the last formula of (7) is nonzero
almost surely. For every such finite realization, continuity supplies a
common sufficiently short positive interval on which all Hessian diagonal
entries remain nonzero and \(e(t)=f(t)-y\ne0\). The corresponding
principal block of \(\mathcal H=e\nabla^2f\) then has rank \(n\),
whereas \(\mathcal J\mathcal J^T\) has rank at most one.

Direct differentiation also gives

\[
 \ddot A_i(0)=4y^2\tanh'(A_{0,i})
                       (W_0^TW_0\tanh A_0)_i\ne0,           \tag{8}
\]

so there is actual hidden-feature motion. Both activation choices fit
the stated strip class. The single-input feature Gram has positive
population variance because \(\mathbb E\tanh^2(G)>0\) for a
standard Gaussian \(G\), and the identity second layer preserves that
positive variance under the specified Gaussian mixing. This example
correctly rejects an exact low-rank conclusion based only on sample count.
It says nothing decisive about approximate rank or compact functional
representations.

## 7. Final scope of the check

No algebraic correction is needed for the checked formulas. The source
qualification needed when reporting the result is explicit: the sharper
all-time truncation rate depends on the assumed integrable residual and
uniform carrier bound, while the \(\log^5 n\) representation count
additionally depends on the common complex-time extension and its uniform
complex RMS bounds.

The representation, curvature contraction evaluation, causal coefficient
acquisition, whole-sphere prediction transfer, and efficient decoder
conclusion remain distinct. This check validates the bounded response
claims under their displayed interfaces; it does not establish any of
those unresolved algorithmic implications.
