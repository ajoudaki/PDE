# Smooth backward clipping: exact continuation contract

2026-10-01. The user explicitly requests the smooth variant
\(c_M(s)=M\tanh(s/M)\) and a complete root-width error theorem. This is the
requested alternative within the current fixed-backward-clipping investigation.
The hard-clipped notes remain distinct; none is silently relabelled as a smooth
result. The current paper is unchanged.

## Model, target, and scope

Fix m training inputs \(x_a\in\mathbb R^d\), labels \(y_a\), width n, two hidden
tanh layers, and a constant \(M>0\) independent of n. Put \(u_a=x_a/\sqrt d\)
and \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\). The initial sufficient regime remains
fixed sufficiently small \(Y>0\) and a positive population initial feature-Gram
gap. No shrinking-label or zero-cap solution is allowed.

Use the already agreed study coordinates
\(k_a=\bar h_{a,0}/\tau\) and \(v_a=-2\bar\delta_{a,0}\). They are exact
normalizations of the paper's q=1 moments. For every input x,

\[
 h(x)=\tanh(Ax/\sqrt d),\qquad
 B=W_0+\frac1{mn}\sum_a v_a k_a^\top,\qquad
 z(x)=Bh(x),\quad g(x)=\tanh z(x),\quad f(x)=w^\top g(x)/n.
\]

The matrix B is reconstructed from the memories; it is not independently
trained. The fixed initialized mixer and its actual transpose are retained.
Write \(h_a=h(x_a)\), \(z_a=z(x_a)\), \(g_a=g(x_a)\),
\(r_a=f(x_a)-y_a\), and \(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\). The loss is
\(\mathcal L=\rho^2\).

The two recursive post-gate backward signals are now exactly

\[
 d_a=c_M(w\odot\operatorname{sech}^2 z_a),\qquad
 \ell_a=c_M\!\left(
 \operatorname{sech}^2(Au_a)\odot B^\top d_a\right).
\]

The smooth map is applied coordinatewise. Residuals are outside that map.
The autonomous equations are

\[
 \dot w=-\frac2m\sum_a r_ag_a,\qquad
 \dot A=-\frac2m\sum_a r_a\ell_a u_a^\top,\qquad
 \dot v_a=-2r_ad_a,\qquad
 \dot k_a=\frac{\rho}{\tau}(h_a-k_a),\qquad \dot\tau=\rho.
\]

Initially A has iid N(0,1) entries, W_0 has iid N(0,1/n) entries independently,
\(w=v_a=0\), \(k_a=h_a(0)\), and \(\tau=1\).
Dots always denote physical training time.

**Important derivative distinction.** In a prediction derivative the upper
factor is \(w\odot\operatorname{sech}^2z_a\), without the smooth clip.
It is generally different from \(d_a\), however small the labels.
The smooth top clip is never exactly inactive away from zero.
Consequently any hard-clip proof using top inactivity must be rederived
with the unclipped output derivative retained.

The target is the smooth system's own deterministic population predictor,
not the hard-clipped or unclipped population and not a dense trained network.
For a fixed bounded query law \(\mu\), the strongest requested formulation is

\[
 \left(\mathbb E\int\sup_{t\ge0}
       |f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_{M,\mu}/\sqrt n.
\]

The expectation is over initialization. The error includes the finite-width
mean bias. A high-probability formulation and an estimate conditioned on an
initialized fitting event must be distinguished from this all-initialization
second moment. The target also includes the fitted endpoint.

No theorem is assumed for arbitrary depth, all bounded-derivative activations,
unscaled unit labels, or configurations without the stated Gram condition.
A complete result in this initial regime is already substantive.

## Startup and ownership

Current HEAD is 4dfa5c1ef2c5b920eda2bbc84316b189b97da92e. The index was empty.
The previously dirty PDF and another study's README were preserved. The
complete current manuscript and mathematical inputs were read previously;
their hashes, and those of the maintained index and notation contract, remain
unchanged. AGENTS.md and workflow Part 1 were reread for this continuation.
The required research, proof, and canonical-notation skills apply.

Root owns this setup, the smooth synthesis, and the study README.
Fresh scoped routes receive explicit allowed inputs and separate flat outputs.
No manuscript, Git, or experiment changes are planned. No other study is a
scientific dependency.
