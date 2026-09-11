# Higher-moment weak forcing

The first-round content above was frozen at SHA-256
`6da7885de6e6f701954525f13bfe6039c9570f82736b2fbf7d0758cb05946295`.
This addition was derived after that freeze, without reading another route.

The existing passive-source coefficient estimates yield more than (8).
For every fixed finite p>=2,

\[
 \sup_{\mu,t}\{\|Z_\mu(t,u)-Z_\mu(t,v)\|_p+
                   \|Q_\mu(t,u)-Q_\mu(t,v)\|_p\}
                            \le C_p|u-v|.                    \tag{25}
\]

Proof at a fixed fine Euler graph: N24's proof gives a Lipschitz beta row
in the current passive input, and its preceding argument gives
`sum_p |alpha_(u,p)-alpha_(v,p)|<=C|u-v|`. The learned pieces of F and D
have the same row estimate by the L2 input continuity of h and Delta and
their retained source masses. Subtract N5 at u and v. The Gaussian source
differences have Lp norm `||N(0,1)||_p` times the L2 difference of their
query inputs, by the cross-program covariance rule N21. These L2 differences
are O(|u-v|). In the forward answer, every past response output Delta is
pointwise bounded by C0, so its row coefficient difference costs at most
`C0 sum |F_u-F_v|`. In the reverse answer the past first features are
bounded by one. Its one current term requires also changing `h(u)` to
`h(v)`, which costs `2C0 ||w||_p |u-v|`. There are no other unmatched
current slots. This proves (25), uniformly in graph, mesh and law. Strong
L2 completion and Fatou for each pair u,v pass it to the actual flows.

Consequently the row and readout components of G and fG are Lipschitz
maps of the angle into every fixed Lp. For the lower row use

`||(phi'(w.u)-phi'(w.v))Q(v)||_p
 <= C ||w||_(2p) ||Q(v)||_(2p) |u-v|`,

and use (25) for the other product difference. Upper gates use (25) and
the bounded readout. The scalar f is ordinarily Lipschitz in the input.
All constants are uniform over the same smaller neighborhood.

To convert this to weak-law control in Lp, let g(a,omega) be one of these
scalar components and fix 0<s<1. Define

\[
 D_s(g)^2=\int_{-\pi}^{\pi}|h|^{-1-2s}
             \int_{\mathbb T}|g(a+h)-g(a)|^2\,da\,dh.
\]

Parseval for each difference shows that the coefficient of
`|hat g(k)|^2` in this expression is
`int |h|^(-1-2s)(2-2cos(kh)) dh`, bounded above and below by positive
constants times `|k|^(2s)` for every nonzero k. For the upper bound split
at `|h|=1/|k|`, using respectively `2-2cos(kh)<=k^2h^2` and <=4.
For the lower bound integrate over `[1/(2|k|),1/|k|]`, where the cosine
difference has a positive lower bound. Thus `||g||_(H^s)` is equivalent
to `||g||_L2+D_s(g)` with constants depending only on s.

Minkowski with exponent p/2, followed by the Lp-Lipschitz estimate, gives

\[
 \|g\|_{L^p(\Omega;H^s(\mathbb T))}
 \le C_s\left[\sup_a\|g(a)\|_p+
       \left(\int_{-\pi}^{\pi}|h|^{-1-2s}
              \int_{\mathbb T}\|g(a+h)-g(a)\|_p^2\,da\,dh\right)^{1/2}\right]
 \le C_{s,p}.                                               \tag{26}
\]

The final integral is finite because it is bounded near zero by a multiple
of `int_0^pi h^(1-2s)dh`, and s<1. Apply the pointwise Fourier duality
(5) and then the Lp norm. For the source b_sigma in (18), this proves

\[
 \sup_t\{\|(b_\sigma)_w(t)\|_p+\|(b_\sigma)_c(t)\|_p+
                          \|(b_\sigma)_K(t)\|_{\rm HS}\}
                             \le C_{s,p}q_s(\sigma).          \tag{27}
\]

The HS component uses (8), since it has no extra neuron coordinate after
its operator norm is taken. Moreover the same reasoning applies to the
two named rank actions

\[
 (b_\sigma)_K h(u)
   =-2\int r(a,y)\Delta(a)\langle h(a),h(u)\rangle\,d\sigma,
\]
\[
 (b_\sigma)_K^*\Delta(u)
   =-2\int r(a,y)h(a)\langle\Delta(a),\Delta(u)\rangle\,d\sigma.
\]

Their scalar contraction factors are uniformly Lipschitz in a by the
already established L2 input bounds. Their coordinate factors are
Lipschitz in Lp by (2),(25). Hence each displayed action is uniformly
O(q_s(sigma)) in Lp for every fixed p and every passive u.

This closes the direct weak-forcing moments on the right side of WT.
It does not prove Lp regularity of applying A or A* to an arbitrary
tangent combination, or a cutoff-independent propagated tangent bound.
Those remain the propagation part of WT.
