# Temporal rank: the existing exponent and what a clock must improve

## Scope and provenance

This note separates a reconstruction of the existing finite-panel upper
bound from a new, generic analytic-curve obstruction. The obstruction is
**not** a counterexample within the Gaussian neural-network class and is
not a lower bound for all compression schemes.

Scientific inputs read completely for the rank interface were
`initialization_panel_compression_20261008/PANEL_BOUND.md` and
`finite_panel_absolute_compression_20261005/PANEL_SOURCE.md`.
The late-time continuation proof in `paper/integrated_appendix.tex`, section
`int:harmonic-analytic-extension-proof`, was also inspected. These are
user-authorized research inputs, not newly promoted results. This note
checks what follows from their stated source estimates; it does not claim
a fresh audit of every dependency of the existing compression theorem.

## 1. Where the five powers come from

There are \(m\) labelled training inputs and \(p\) additional passive inputs;
all have norm \(\sqrt d\). Width is \(n\), the number of hidden layers is
\(L\), the initial limiting feature-Gram gap is \(\gamma>0\), and
\(Y=\|y\|_2/\sqrt m>0\). The source studies impose their existing analytic
activation, zero-readout Gaussian initialization, label and width conditions.
Nothing here changes those conditions.

The finite-panel proof constructs a linear source space from forward
responses and their initialized-matrix images on all \(m+p\) inputs, and
backward responses and their initialized-transpose images on the \(m\)
training inputs. This is \(2(2m+p)\) vector curves per layer. The basis is
used only to construct fixed metrics and mixers; the deployed compressed
network subsequently evolves autonomously in physical time.

For fixed problem parameters, the inherited source bounds have the form

\[
T_0=\frac{32m}{\gamma}\log(en),\qquad
r_t=\frac{c_t}{\sqrt{\log(en)}},\qquad
\sup_{|\Im t|\le r_t}\|u(t)\|_\infty\le M_0\sqrt n,
\tag{1}
\]

on the rectangle extending the real interval \([0,T_0]\) by \(r_t\) at
both ends. The positive constants \(c_t,M_0\) are the explicitly defined
source constants in the input proof: they depend on activation, depth,
labels and gap/sample parameters and are not absolute constants. In
particular, this note does not remove their sample or gap dependence.

The angular Chebyshev strip has width \(\alpha=r_t/(4T_0)\). For a source
tolerance \(\eta>0\), the inherited sufficient degree and source rank are

\[
\begin{aligned}
K&=\left\lceil\frac{4T_0}{r_t}
       \log\frac{256M_0\sqrt n\,T_0}{r_t\eta}\right\rceil,\\
R&=2m+d+1+2(2m+p)(K+1).
\end{aligned}
\tag{2}
\]

Equation (2) is just the source proof's degree formula after substituting
\(\alpha=r_t/(4T_0)\), not a new bound. The compressed widths satisfy
\(q_j\le9R\). Its fully counted retained inventory is bounded by

\[
1020(L+1)R^2+10m(d+1)+pd+(m+p)+36R+D_{\rm alg},
\tag{3}
\]

where \(D_{\rm alg}\) is the fixed algorithm description counted in the
input theorem. It includes the fixed metrics/mixers, not only moving
weights. Exact restriction to the input span can replace the input-space
rank contribution \(d\) by at most \(m+p\), with the input representation
separately charged.

For the source tolerances used to match or beat dense variability,
\(\log(1/\eta)=O(\log n)\), holding the problem and confidence fixed.
The nonlinear comparison factor contains \(e^{C\sqrt{\log(en)}}\), but
its logarithm is still \(O(\log n)\); it does not create a further power.
Thus the width-only ledger is

\[
K=O\!\left(
\underbrace{\log n}_{\text{horizon}}
\underbrace{\sqrt{\log n}}_{\text{inverse analytic radius}}
\underbrace{\log n}_{\text{source accuracy}}
\right),\qquad R^2=O((\log n)^5).
\tag{4}
\]

All statements in (4) are fixed-problem asymptotics. They do not identify
\(m,d,1/\gamma,L\) or suppress them in a purported joint asymptotic theorem.

## 2. A clock cannot change the best uniform linear source rank

Let \(u:I\to H\) be a curve in a normed space, and let
\(t:J\to I\) be an onto reparameterization. For every linear subspace
\(E\subset H\),

\[
\sup_{s\in J}\inf_{v\in E}\|u(t(s))-v\|
=\sup_{t\in I}\inf_{v\in E}\|u(t)-v\|.
\tag{5}
\]

Indeed, the two suprema range over exactly the same set of curve values.
If the intervals differ only by their limiting endpoint and the curve is
continuous there, taking closures gives the same equality. Therefore the
minimum dimension of a uniformly accurate linear source space is also
unchanged. A clock can improve a *particular polynomial construction* or
the proof of its rank, but not the intrinsic linear rank of that trace.
This does not prohibit an improvement of the existing nonoptimal upper
bound (2).

## 3. Fixed-strip analyticity and exponential flattening alone cannot improve the exponent

The following elementary construction makes the missing information
precise. It already has uniformly bounded exponentially decaying speed,
so controlling total motion does not repair the implication.

**Proposition (generic source class, not a neural trajectory).** For all
sufficiently large integer \(n\), there is an entire curve
\(u_n:\mathbb C\to\mathbb C^n\), real on the real axis, with these
properties. Write \(\|v\|_n=\|v\|_2/\sqrt n\). On the half-strip
\(\Re t\ge-1/\sqrt{\log(en)}\),
\(|\Im t|\le1/\sqrt{\log(en)}\), its normalized norm is bounded by an
absolute constant, and so is its maximum coordinate. On real \(t\ge0\),
both the normalized norm and the maximum coordinate of \(u_n(t)\) and
\(\dot u_n(t)\) are at most an absolute constant times \(e^{-t}\).
Nevertheless every linear subspace approximating its entire real trace
to normalized error \(n^{-1/2}\) has dimension
\(\Omega((\log n)^{5/2})\). This conclusion survives every onto monotone
change of time.

**Proof.** The following symbols are local to this proof. Set

\[
\ell=\log(en),\quad r=\ell^{-1/2},\quad
h=\frac{8\pi r}{\ell},\quad
J=\left\lfloor\frac{\ell}{8h}\right\rfloor,\quad
a=h e^{-\ell/8}.
\tag{6}
\]

For large \(n\), \(1\le2J<n\). With coordinates indexed by
\(k=0,\ldots,n-1\), choose
\(v_j(k)=\sqrt2\cos(2\pi jk/n)\). These vectors are orthonormal in
the normalized Euclidean inner product: product-to-sum reduces their
inner products to discrete sums of exponentials with frequencies
\(j-j'\) and \(j+j'\); only \(j=j'\) gives a frequency divisible by
\(n\). All other sums vanish by the finite geometric-series identity.
Also \(|v_j(k)|\le\sqrt2\). With
\(\operatorname{sinc}(z)=\sin z/z\), continuously extended
by \(1\) at zero, define

\[
u_n(t)=a e^{-t}\sum_{j=1}^J
             v_j\operatorname{sinc}\!\left(\pi(t/h-j)\right).
\tag{7}
\]

Every summand is entire. To estimate the sum, use the exact integral
identity

\[
\operatorname{sinc}\!\left(\pi(t/h-j)\right)
=\frac1{2\pi}\int_{-\pi}^{\pi} e^{i\xi t/h}e^{-ij\xi}\,d\xi.
\tag{8}
\]

The exponentials \(e^{ij\xi}\) are orthonormal for the measure
\(d\xi/(2\pi)\). Subtracting the finite orthogonal projection of
\(e^{i\xi t/h}\) onto those exponentials leaves a nonnegative squared
norm. Expanding that norm proves directly that

\[
\sum_{j=1}^J
 \left|\operatorname{sinc}\!\left(\pi(t/h-j)\right)\right|^2
\le \frac1{2\pi}\int_{-\pi}^{\pi}
           |e^{i\xi t/h}|^2\,d\xi
\le e^{2\pi|\Im t|/h}.
\tag{9}
\]

Since \(\pi r/h=\ell/8\), orthogonality of the \(v_j\) gives

\[
\|u_n(t)\|_n
\le a e^{-\Re t}e^{\pi|\Im t|/h}
\le h e^r
\tag{10}
\]

throughout the stated strip. Coordinatewise Cauchy--Schwarz also gives
\(\|u_n(t)\|_\infty\le\sqrt{2J}\,h e^r\). Since
\(\sqrt{2J}\,h\le\sqrt{2\pi}\,\ell^{-1/4}\), the complex coordinate
bound is uniform in \(n\), stronger than that used in (1).
For real \(t\ge0\), the sharper normalized bound is
\(\|u_n(t)\|_n\le a e^{-t}\).

Differentiating (8) under its bounded integration interval and using the
same projection argument on \((i\xi/h)e^{i\xi t/h}\) gives, for real \(t\),

\[
\sum_{j=1}^J
 \left|\frac d{dt}\operatorname{sinc}\!\left(\pi(t/h-j)\right)\right|^2
\le\frac1{2\pi}\int_{-\pi}^{\pi}\frac{\xi^2}{h^2}\,d\xi
=\frac{\pi^2}{3h^2}.
\tag{11}
\]

Thus

\[
\|\dot u_n(t)\|_n
\le e^{-\ell/8}\left(h+\frac\pi{\sqrt3}\right)e^{-t}.
\tag{12}
\]

In particular, the total normalized path length is bounded independently
of \(n\). The corresponding coordinate bounds for (7) and its derivative
cost at most \(\sqrt{2J}\); their coefficients remain uniformly bounded
because \(\sqrt{2J}e^{-\ell/8}(h+\pi/\sqrt3)\) tends to zero.
The curve starts at zero and tends to zero; adding a fixed nonzero vector
orthogonal to all the \(v_j\) gives the same rank obstruction up to one
dimension if a nonzero plateau is desired. To see this last assertion,
adjoin that vector to any proposed approximating subspace and subtract it.

At the \(J\) real times \(t_j=jh\le\ell/8\), the cardinal identity in
(7) gives

\[
u_n(t_j)=a e^{-t_j}v_j,\qquad
a e^{-t_j}\ge h e^{-\ell/4}.
\tag{13}
\]

Let \(E\) approximate the trace to error \(n^{-1/2}\), and let \(P_E\)
be its orthogonal projection in the normalized inner product. From (13),

\[
\|v_j-P_Ev_j\|_n\le
\frac{n^{-1/2}}{h e^{-\ell/4}}.
\]

Extend the orthonormal set \(\{v_j\}\) to a basis and take the trace of
\(P_E\). It yields

\[
\begin{aligned}
\dim E
&\ge\sum_{j=1}^J\|P_Ev_j\|_n^2\\
&\ge J\left(1-\frac{e^{\ell/2}}{nh^2}\right)
=J\left(1-\frac{\sqrt e\,\ell^3}{64\pi^2\sqrt n}\right).
\end{aligned}
\tag{14}
\]

Finally \(J=\lfloor\ell^{5/2}/(64\pi)\rfloor\), while the subtracted
factor tends to zero. This proves the lower bound, and (5) proves its
invariance under a clock. The same argument works at tolerances
\(n^{-1/2+o(1)}\), not only exactly \(n^{-1/2}\). ∎

**Interpretation and limits.** The theorem rules out deriving
\(o((\log n)^{5/2})\) *linear source rank* from fixed-strip analyticity,
exponential tails and bounded path length alone. It does not show that
the neural sources realize (7), that Gaussian trajectories have this
rank, or that all possible nonlinear encodings need squared-rank storage.
Its source is an oscillatory small transient, not a claim that loss can
oscillate. A proof of improved neural rank must use additional structure
of the actual training equations, not just the generic estimates (1).

## 4. What the existing late-time continuation does and does not supply

The paper's late-time continuation proof uses a safe complex parameter
ball of radius proportional to \(n^{-1/2}\), after the real residual has
decayed through time \(T_0=32m\log(en)/\gamma\). Inside the ball, the
complex residual can grow at most exponentially with the length of a
complex continuation segment. The already tiny residual makes every
disk of radius \(r_t\) safe, allowing extension to arbitrary finite real
horizons.

This supplies all finite horizons with the **same** fixed radius \(r_t\).
It does not supply disks whose radius grows from early training with the
amount of loss already dissipated. Repeating this particular ball
argument earlier would need the residual to be of order \(n^{-1/2}\)
before taking a width-independent complex-time step, again costing a
real time of order \(\log n\). Consequently, merely enlarging the very
late disks cannot remove the contribution already accumulated on
\([0,T_0]\).

The promising unresolved obligation is an estimate tied to the actual
forward/backward source directions, or dissipativity in complex time,
that is sharper than this worst-coordinate parameter ball. The
conditional consequences of several such estimates are derived in
`ADAPTIVE_APPROXIMATION.md`; no such estimate is assumed to hold in the
existing neural theorem.
