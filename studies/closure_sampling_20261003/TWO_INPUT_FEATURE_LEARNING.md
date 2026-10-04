# Width-independent feature motion for two orthogonal training inputs

2026-10-03. Internally derived certificate for the actual canonical
two-hidden-layer Gaussian tanh network. This strengthens the nonzero
initial-curvature certificate in `TWO_INPUT_CANONICAL_COMPRESSION.md`.
The argument uses the canonical model and the real regular coordinates
from `TWO_INPUT_STABLE_GEOMETRY.md`. It does not assume the complex
source theorem, bounded neuronwise trained carriers, a population training
limit, or a frozen hidden layer. No experiments or Git operations are used.

## 1. Statement and notation

Train the canonical width-n network on x_1=√2e_1 and x_2=√2e_2,
with label vector y=(y_1,y_2), Y=|y|, loss
\(\tfrac12\sum_a(f_a-y_a)^2\), and mobilities (n,1,n).
Its initialization is the actual iid Gaussian initialization, with zero
readout. There are fixed constants t_*>0, Y_*>0, and c,C>0, and
initialization events whose probability tends to one, such that on these
events, simultaneously for every 0<|y|≤Y_*,

\[
 cY^2\le
 \left(\sum_{a=1}^2\frac{\|h_a(t_*)-h_a(0)\|_2^2}{n}\right)^{1/2}
 \le CY^2,
 \tag{1}
\]
\[
 cY^2\le
 \left(\sum_{a=1}^2\frac{\|g_a(t_*)-g_a(0)\|_2^2}{n}\right)^{1/2}
 \le CY^2.\tag{2}
\]

Thus both hidden feature layers move by an amount independent of width
at one fixed positive physical time. At least one training example
witnesses the motion in each layer. The constants and the event do not
depend on label signs, relative magnitudes, or direction. For any fixed
confidence 1−η these statements hold with that probability for all
sufficiently large n.

Write \(\langle p,q\rangle_n=p^\top q/n\) and
\(\|p\|_n=\|p\|_2/\sqrt n\). At training sample a define

\[
 a_a=Ae_a,\quad h_a=\tanh a_a,\quad z_a=Wh_a,\quad
 g_a=\tanh z_a,\quad c_a=y_a-\langle w,g_a\rangle_n,
\]
\[
 \delta_a=w\odot\operatorname{sech}^2z_a,\quad
 k_a=W^\top\delta_a,\qquad
 u_a=\Psi(a_a),\quad
 \Psi(a)=a/2+\sinh(2a)/4,\quad \sigma=\tanh\circ\Psi^{-1}.
\]

Then σ and its first two real derivatives are bounded, σ is
1-Lipschitz, and the exact physical equations are

\[
 \dot u_a=c_ak_a,\qquad
 \dot W=\frac1n\sum_a c_a\delta_ah_a^\top,\qquad
 \dot w=\sum_a c_ag_a.\tag{3}
\]

The first feature derivative is \(\dot h_a=c_a\sigma'(u_a)\odot k_a\),
with \(\sigma'(u_a)=\operatorname{sech}^4a_a\). Subscript 0
below always denotes initialization.

## 2. Uniform short-time RMS estimates

Assume only \(\|W_0\|_{\rm op}\le K\). Every tangent Gram in
the real gradient flow is positive semidefinite, so |c(t)|≤Y while
the solution exists. Bounded tanh, (3), and the rank-one Frobenius
identity therefore give, for 0≤t≤1 and 0<Y≤1,

\[
 \|w(t)\|_\infty\le CYt,\qquad
 \|W(t)-W_0\|_F\le CY^2t^2,\qquad
 \|u_a(t)-u_{a,0}\|_n\le CY^2t^2,
 \tag{4}
\]
\[
 \|h_a(t)-h_{a,0}\|_n+
 \|z_a(t)-z_{a,0}\|_n+
 \|g_a(t)-g_{a,0}\|_n\le CY^2t^2.\tag{5}
\]

Here and below constants depend on fixed K but not on n or y.
For example, δ has normalized norm at most CYt, W stays in a
fixed operator tube, and integrating \(\dot u_a=c_aW^\top\delta_a\)
proves its bound. Lipschitz forward maps give (5). These bounds prevent
finite-time state escape on the displayed interval.

The tangent Gram has bounded operator norm on this tube, so
\(c(t)=y+O(Yt)\) in R². Define the fixed initial readout velocity

\[
 v=\dot w(0)=\sum_b y_bg_{b,0},\qquad \|v\|_\infty\le\sqrt2Y.
\]

Integrating the readout equation and using (5) yields

\[
 \|w(t)-tv\|_n\le CYt^2.\tag{6}
\]

Let \(d_{a,0}^v=v\odot\operatorname{sech}^2z_{a,0}\) and
\(k_{a,0}^v=W_0^\top d_{a,0}^v\). Bounded gate derivatives,
(4)–(6), and \(\|v\|_\infty\le\sqrt2Y\) imply

\[
 \|\delta_a(t)-t d_{a,0}^v\|_n\le CYt^2,
 \qquad \|k_a(t)-t k_{a,0}^v\|_n\le CYt^2.
\]

Substitute these estimates and c_a=y_a+O(Yt) into the first
equation in (3), then integrate. This proves the useful expansion

\[
 \left\|u_a(t)-u_{a,0}
             -\frac{t^2}{2}y_a k_{a,0}^v\right\|_n
 \le CY^2t^3.\tag{7}
\]

It is an estimate in the regular coordinate u. We do not assert that
a coordinatewise quadratic remainder has the same normalized L² bound.
The bounded test used next controls that remainder in normalized L¹,
where (4) is sufficient.

## 3. Initialized moment matrices with positive gaps

Fix a deterministic R_0>0, for example R_0=1, and define

\[
 h_{a,0}^{R}=h_{a,0}\odot\mathbf1_{\{|a_{a,0}|\le R_0\}},
\]
\[
 M_{ab,n}=\left\langle W_0h_{a,0}^{R},
                 g_{b,0}\odot\operatorname{sech}^2z_{a,0}
              \right\rangle_n.\tag{8}
\]

Let Z_0∼N(0,1),
\(q=E\tanh^2Z_0>0\), and
\(q_R=E[\tanh^2Z_0\,\mathbf1_{|Z_0|\le R_0}]>0\).
If Z∼N(0,q), then

\[
 M_n\longrightarrow \tau I_2\quad\hbox{in probability},
 \qquad
 \tau=\frac{q_R}{q}E[Z\tanh Z\operatorname{sech}^2Z]>0.
 \tag{9}
\]

Here is a direct finite-initialization justification. The two initialized
first-layer columns are independent standard Gaussian vectors.
The empirical covariance of
\((h_{1,0},h_{2,0},h_{1,0}^{R},h_{2,0}^{R})\) converges by
the law of large numbers. Cross covariances between different sample
indices vanish, because each coordinate map is odd. Within sample a,
the covariance of h_{a,0} with h_{a,0}^{R} is q_R.
Conditional on these columns, the rows of their W_0 images are iid
Gaussian tuples with that empirical covariance. Their relevant second
moments are uniformly bounded. Conditional Chebyshev and continuity
of Gaussian expectations therefore give the limit of every entry in (8).
In the limiting Gaussian tuple, if Z_a^R is the truncated feature's
image, then E[Z_a^R|Z_a]=(q_R/q)Z_a and the other sample is
independent. This gives the diagonal in (9), while the off-diagonal
vanishes by oddness. The displayed diagonal is strictly positive since
Z tanh Z is positive away from zero.

Two further initialized matrices are needed. Define

\[
 Q_{h,0}=(\langle h_{a,0},h_{b,0}\rangle_n)_{a,b=1}^2,
\]
\[
 H_{a,bc,n}=\left\langle
      g_{b,0}g_{c,0}\operatorname{sech}^4z_{a,0},\mathbf1
                     \right\rangle_n,\qquad a,b,c\in\{1,2\},
 \tag{10}
\]

where multiplication inside the last average is componentwise. Then
Q_{h,0}→qI. At independent Z_1,Z_2∼N(0,q), the limiting H_1
is diagonal with positive entries

\[
 E[\tanh^2Z_1\operatorname{sech}^4Z_1],\qquad
 E[\tanh^2Z_2]E[\operatorname{sech}^4Z_1].
\]

The limiting H_2 has these entries exchanged. Off-diagonal entries
vanish by oddness. Conditional bounded-variable concentration, and the
same covariance limit as above, prove convergence. Therefore fixed
q_0,μ_0>0 exist such that, with probability tending to one,

\[
 \frac{M_n+M_n^\top}{2}\succeq\frac\tau2 I,
 \qquad Q_{h,0}\succeq q_0I,
 \qquad H_{a,n}\succeq\mu_0I\quad(a=1,2).
 \tag{11}
\]

Intersect this event with the Gaussian operator-norm event. It is an
initialization event, independent of the labels. All quadratic-form
conclusions in (11) are uniform over label directions; in particular
they do not exclude opposite-sign or highly unequal labels.

## 4. Width-independent first-layer feature displacement

Use the fixed bounded initialized test vectors

\[
 b_a=h_{a,0}^{R}\odot\operatorname{sech}^{-4}a_{a,0}.
 \tag{12}
\]

They vanish outside |a_{a,0}|≤R_0 and obey
\(\|b_a\|_\infty\le B_0:=\cosh^4R_0\).
Since σ'(u_{a,0})=sech⁴a_{a,0}, their product with that
derivative is exactly h_{a,0}^{R}. Taylor's formula for the scalar
function σ, its bounded second derivative, and (4), (7) now give

\[
 \sum_a\langle b_a,h_a(t)-h_{a,0}\rangle_n
 =\frac{t^2}{2}y^\top M_n y+E_h(t),
\]
\[
 |E_h(t)|\le C B_0(Y^2t^3+Y^4t^4).\tag{13}
\]

To check the nonlinear term, its coordinate absolute value is at most
C|u_a(t)-u_{a,0}|². Averaging against b_a therefore costs at
most \(CB_0\|u_a(t)-u_{a,0}\|_n^2\le CB_0Y^4t^4\).
The linear part of (7) gives the term O(B_0Y²t³).
No maximum of an adaptive carrier or fourth moment of a state increment
is used.

By (11), the leading term is at least τY²t²/4. Choose a fixed
sufficiently small t_*>0, depending only on the fixed constants, so
the remainder in (13) is at most τY²t_*²/8 for Y≤Y_*≤1.
Cauchy--Schwarz and \(\sum_a\|b_a\|_n^2\le2B_0^2\) give

\[
 \left(\sum_a\|h_a(t_*)-h_{a,0}\|_n^2\right)^{1/2}
 \ge\frac{\tau t_*^2}{8\sqrt2 B_0}Y^2.\tag{14}
\]

Equation (5) supplies the corresponding upper bound. This proves (1).

## 5. Width-independent second-layer feature displacement

Keep the initialized label aggregate v=∑_b y_bg_{b,0} fixed, but
evaluate its backward gate and carrier at the current hidden state:

\[
 d_a^v(t)=v\odot\operatorname{sech}^2z_a(t),\qquad
 K_a^v(t)=W(t)^\top d_a^v(t).
\]

By (10)–(11), \(\|d_a^v(0)\|_n^2=y^\top H_{a,n}y\ge\mu_0Y^2\).
Bounded gate derivatives and (5) imply

\[
 \|d_a^v(t)-d_a^v(0)\|_n\le CY^3t^2.
\]

Thus, after reducing Y_* or t_* if needed, throughout [0,t_*],

\[
 \|d_a^v(t)\|_n\ge\tfrac12\sqrt{\mu_0}Y,
 \qquad Q_h(t):=(\langle h_a(t),h_b(t)\rangle_n)_{a,b}
                                      \succeq\tfrac12q_0I.
 \tag{15}
\]

Consider the scalar feature pairing

\[
 P(t)=\sum_a y_a\langle v,g_a(t)-g_{a,0}\rangle_n.
\]

Differentiate the actual second-layer features using (3). The exact
identity is

\[
 \dot P(t)=
 \sum_{a,b}y_ac_b
       \langle d_a^v,\delta_b\rangle_n\langle h_a,h_b\rangle_n
 +\sum_a y_ac_a
       \langle K_a^v,\sigma'(u_a)\odot k_a\rangle_n.
 \tag{16}
\]

The first term is the contribution from the learned mixer, and the
second is the contribution from the learned first-layer features.
From (6), the current-gate decomposition is

\[
 \delta_a(t)=t d_a^v(t)+\varepsilon_a(t),
 \qquad\|\varepsilon_a(t)\|_n\le CYt^2,
\]
\[
 k_a(t)=t K_a^v(t)+W(t)^\top\varepsilon_a(t).
\]

Substitute these formulas and c=y+O(Yt) into (16). All error
terms are bounded in normalized L², using \|d_a^v\|_n+
\|K_a^v\|_n≤CY, bounded operator norm, bounded gates, and
\|h_a\|_n≤1. The result is

\[
 \dot P(t)=t\left\|\frac1n\sum_a y_a d_a^v h_a^\top\right\|_F^2
 +t\sum_a y_a^2
            \|\operatorname{sech}^2a_a\odot K_a^v\|_n^2
 +E_g(t),
 \qquad |E_g(t)|\le CY^4t^2.\tag{17}
\]

For example, replacing δ_b by its error costs at most
\(C|y_a||c_b|\|d_a^v\|_n\|\varepsilon_b\|_n\le CY^4t^2\).
Replacing c_b by y_b in a main term also costs CY⁴t².
The first-layer error obeys the same bound using
\(\|W^\top\varepsilon_a\|_n\le CYt^2\).
There is no derivative of a carrier in this calculation.

Both main terms in (17) are nonnegative for every label sign pattern.
In fact the mixer term has a uniform lower bound. Let D(t) be the
Gram matrix \((\langle d_a^v,d_b^v\rangle_n)_{a,b}\). Since
Q_h≽q_0I/2 and D is positive semidefinite, the Gram identity for
tensor products gives

\[
 \left\|\frac1n\sum_a y_a d_a^v h_a^\top\right\|_F^2
 =\sum_{a,b}y_ay_bD_{ab}Q_{h,ab}
 \ge\frac{q_0}{2}\sum_a y_a^2\|d_a^v\|_n^2
 \ge c_0Y^4.\tag{18}
\]

For the middle inequality, write Q_h=q_0I/2+R with R positive
semidefinite. The remaining matrix with entries D_ab R_ab is a
Gram matrix of tensor-product vectors, hence positive semidefinite.
This verifies the sign without assuming the entries of y are positive.

Reduce the same fixed t_* so CY⁴t²≤c_0Y⁴t/2 on [0,t_*].
Equations (17)–(18), followed by integration, give

\[
 P(t_*)\ge\tfrac14c_0Y^4t_*^2.\tag{19}
\]

Finally, the norm of the fixed test tuple (y_av)_a is
\(Y\|v\|_n\le\sqrt2Y^2\). Cauchy--Schwarz in (19) proves

\[
 \left(\sum_a\|g_a(t_*)-g_{a,0}\|_n^2\right)^{1/2}
 \ge\frac{c_0t_*^2}{4\sqrt2}Y^2.\tag{20}
\]

Together with (5), this proves (2). The argument estimates second-layer
feature motion itself. It does not infer it merely from nonzero mixer
motion or nonzero initial curvature.

## 6. Consequence for the compressed model

The full-network statement (1)–(2) is independent of the complex source
and cubature arguments. A further consequence applies to the compressed
construction in `TWO_INPUT_CANONICAL_COMPRESSION.md`, whose source
and complete compression chain have now passed the internal checks
recorded in the two corresponding `CHECK` files. The additional feature
motion proof in this note remains a separately derived result until its
own complete reconstruction is recorded.

Its source cubature preserves pairings of h_a(t_*),h_a(0), and
of g_a(t_*),g_a(0), up to O(ε), where ε=Cn^{-1/2}. Therefore the
squared weighted feature displacements on selected original neurons
differ from the full empirical squared displacements by O(ε).
The own-dynamics comparison gives weighted first-feature error O(ε)
through the 1-Lipschitz inverse coordinate map, and weighted second-feature
error O(ε) using both state comparison and the forward source defect.
At initialization the selected training features match exactly.

For each fixed nonzero small y, sufficiently large n therefore gives

\[
 \left(\sum_a\|h_{C,a}(t_*)-h_{C,a}(0)\|_{D_1}^2\right)^{1/2}
 \ge c'Y^2,
\]
\[
 \left(\sum_a\|g_{C,a}(t_*)-g_{C,a}(0)\|_{D_2}^2\right)^{1/2}
 \ge c'Y^2.\tag{21}
\]

The width threshold for this transfer can depend on the fixed Y,
because O(ε) pairing errors must be smaller than the O(Y⁴)
squared-motion lower bounds. This does not weaken the uniform initial
full-network certificate (1)–(2). No extra curvature vectors are needed
for (21), although the finitely many such vectors already included in
the construction are harmless.

## 7. Scope and audit

The proof is for the actual finite canonical network and an entire
nonzero small label ball, on one label-independent initialization event.
Its two positive moment conditions are verified directly from Gaussian
initialization. The fixed physical time t_* and both lower bounds are
independent of width. The first-layer test truncates only an initialized
test vector; it does not truncate or change the trained network.

The result proves motion at a fixed positive time, not a separate lower
bound on displacement of the fitted endpoint. It proves at least one
moving training feature per hidden layer, not identical lower bounds
for each sample when a label vanishes or becomes arbitrarily small.
Neither restriction permits the hidden features to freeze in the
fixed-nonzero-label, increasing-width limit addressed here.
