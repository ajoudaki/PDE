# Rare backward energy from the actual derivative and scalar identity

This note proves a relative, time-integrated estimate for the actual
middle backward vector. It concerns the Gaussian-hidden-weight,
ZERO-initial-readout finite proxy and its fully pruned reference.
It does not assert a global transfer to the prescribed tiny Gaussian
readout, a bound on the full/pruned distance, or global population
continuation.

The proof uses the all-set/time event of
ACTUAL_RARE_BACKWARD_DERIVATIVE.md, together with the checked scalar
identity and off-block estimate. Both networks may instead use the
same prescribed middle clipping, with
\(|\tau(x)|\le |x|\) and Lipschitz constant at most one. The identity
map gives the uncut case. Constants are uniform in this prescribed
clipping; there is no event simultaneous over all clipping maps.

## Statement

Fix a finite feature horizon \(S\) and the initial operator bound
used in those sources. For a middle index set \(E\), put \(p=|E|/n\).
Let \(d_E(s)\) be the full/pruned distance defined in
SINGLE_PRUNED_OFFBLOCK_OSGOOD.md, and set
\[
h(p)=p\log(e/p),\qquad
\mu(d)=d\sqrt{1+\log_+(1/d)},
\]
with both functions extended by zero at zero.
On the common event from the derivative lemma, simultaneously for
every \(E\),
\[
\int_0^S\frac{\|P_E\delta^{(2)}(s)\|_2^2}{n}\,ds
\le C_{S,M}\left[
 h(p)+\varepsilon_n^2+
                     \int_0^S\mu(d_E(s))^2\,ds\right].
\tag{1}
\]
All vector norms here are ordinary Euclidean norms. The probability
and the vanishing width error \(\varepsilon_n\) are exactly those of
the derivative lemma, enlarged by harmless fixed constants.

Unlike an estimate on the signed primitive of
\(P_E\delta^{(2)}\), (1) bounds its nonnegative squared magnitude
integrated over time. It is still a relative estimate because its
right side contains the unclosed full-state distance.

## Proof

For readability only within this proof, let
\[
q_E=P_E(W^{(3)})^\top\delta^{(3)},\qquad
\delta_E=P_E\delta^{(2)},\qquad
h_E=P_E\phi(z^{(2)}).
\]
The last vector is the ACTUAL rare activation. It is not the
identically zero pruned activation. It satisfies
\(\|h_E\|_2/\sqrt n\le(\pi/2)\sqrt p\).

The exact scalar decomposition of the actual rare preactivation is
\[
P_E(z^{(2)})'
      =\alpha_E\delta_E+\widehat g_E+\rho_E,
\qquad 1/4\le\alpha_E\le(\pi/2)^2+1.
\tag{2}
\]
Here \(\widehat g_E=P_EW_0^{(2)}(\widehat h^{(1)})'\)
is the genuine fully pruned unused forward velocity. In particular
it is not an actual bulk velocity assumed independent of a deleted
Gaussian block.

Write
\[
w_E(s)=\sqrt{h(p)}+\varepsilon_n+\mu(d_E(s)).
\]
The derivative lemma and off-block estimate supply, on their common
event,
\[
\frac{\|q_E'(s)\|_2}{\sqrt n}
\le C_{S,M}\left[
            \frac{\|\delta_E(s)\|_2}{\sqrt n}+w_E(s)\right],
\qquad
\frac{\|\widehat g_E(s)\|_2+\|\rho_E(s)\|_2}{\sqrt n}
\le C_{S,M}w_E(s).
\tag{3}
\]
The first inequality deliberately retains the actual rare
self-feedback \(\delta_E\).

For a common clipping define \(u_E=\tau(q_E)\) on \(E\), extended
by zero off \(E\); for the uncut case take \(u_E=q_E\).
Then
\[
\delta_E=\phi'(z^{(2)})\odot u_E,\qquad
u_E(0)=0,\qquad
\|u_E'(s)\|_2\le\|q_E'(s)\|_2\quad\hbox{a.e.}
\tag{4}
\]
The last assertion follows from the Lipschitz chain rule for an
absolutely continuous scalar path in each coordinate. Thus the
clipped energy argument pairs with \(\tau(q_E)\), not with \(q_E\).

Use (2) and (4) to obtain the exact scalar-product identity
\[
\frac{u_E^\top h_E'}n
=\alpha_E\frac{\|\delta_E\|_2^2}n
 +\frac{\delta_E^\top(\widehat g_E+\rho_E)}n.
\tag{5}
\]
Integrate in time and integrate the left side by parts. Its initial
boundary vanishes because \(u_E(0)=0\). For \(0\le t\le S\),
\[
\begin{split}
\int_0^t\alpha_E\frac{\|\delta_E\|_2^2}n\,ds
={}&\frac{u_E(t)^\top h_E(t)}n
 -\int_0^t\frac{(u_E')^\top h_E}n\,ds\\
&-\int_0^t\frac{\delta_E^\top
                         (\widehat g_E+\rho_E)}n\,ds.
\end{split}
\tag{6}
\]
Also \(\|u_E(t)\|_2\le\int_0^t\|u_E'(s)\|_2ds\).
Consequently the sum of the absolute values of the first two terms
on the right of (6) is at most
\[
\pi\sqrt p\int_0^t\frac{\|q_E'(s)\|_2}{\sqrt n}\,ds.
\tag{7}
\]
This is where a bound on the actual rare derivative, rather than
only on the pruned Gaussian query, is required.

Put \(a_E(s)=\|\delta_E(s)\|_2/\sqrt n\), only to write the final
scalar estimate. From (3), (6), and (7),
\[
\frac14\int_0^t a_E(s)^2\,ds
\le C_{S,M}\int_0^t
       \big[\sqrt p\,a_E+\sqrt p\,w_E+a_Ew_E\big]\,ds.
\tag{8}
\]
For each of the two terms containing \(a_E\), the elementary
inequality \(xy\le \epsilon x^2+y^2/(4\epsilon)\), with a
sufficiently small fixed \(\epsilon\), absorbs a total of at most
\(\frac18\int a_E^2\) into the left side. The other term obeys
\(\sqrt p\,w_E\le(p+w_E^2)/2\). Therefore
\[
\int_0^t a_E(s)^2\,ds
\le C_{S,M}\int_0^t[p+w_E(s)^2]\,ds.
\tag{9}
\]
Finally \(p\le h(p)\) and
\[
w_E(s)^2\le
3h(p)+3\varepsilon_n^2+3\mu(d_E(s))^2.
\]
Take \(t=S\) and absorb its fixed length in \(C_{S,M}\).
This proves (1), including \(p=0\), when the rare vectors vanish.

## Consequence for whole rare coordinate paths

The same event also gives a relative estimate for the entire actual
backward path, not only its activation-gated version. With the notation
of the proof, simultaneously for every \(E\),
\[
\begin{split}
&\frac1n\sum_{i\in E}\sup_{0\le t\le S}
 \left(\left|[(W^{(3)}(t))^\top\delta^{(3)}(t)]_i\right|^2
       +|z_i^{(2)}(t)-z_i^{(2)}(0)|^2\right)\\
&\quad+\int_0^S\frac{\|q_E'(s)\|_2^2+
                          \|P_E(z^{(2)})'(s)\|_2^2}{n}\,ds\\
&\le C_{S,M}\left[
 h(p)+\varepsilon_n^2+\int_0^S\mu(d_E(s))^2\,ds\right].
\end{split}
\tag{10}
\]
To prove this, square (3) and integrate. Equation (1) bounds its
backward-action term, while the displayed bound on \(w_E^2\)
bounds the other term. This proves the estimate for
\(\int\|q_E'\|_2^2/n\). Squaring the exact identity (2) and using
the same bounds proves it for
\(\int\|P_E(z^{(2)})'\|_2^2/n\).
Finally, for each absolutely continuous scalar path \(v\),
\[
\sup_{t\le S}|v(t)-v(0)|^2
 \le S\int_0^S|v'(s)|^2\,ds.
\]
Apply this coordinatewise to both paths and use \(q_E(0)=0\).
The supremum is inside the coordinate average in (10);
no interchange of a supremum and an expectation is being assumed.
There is no new probability event. In particular this corollary also
applies to an \(E\) selected from the whole actual trajectory.
Its right side still contains the full/pruned distance.

## What is still missing

The actual rare self-feedback term in (3) is absorbed in the energy
argument; it was not silently removed from the derivative estimate.
No tail premise on \(q_E\) or on \(\delta_E\) was used.
Nevertheless the right side of (1) still depends on \(d_E\).
The uncompressed active matrix and bottom-action comparison must
still be controlled before (1) can imply a global population result.
