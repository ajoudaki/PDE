# General input geometry: near-quarter memory order

2026-10-03. Continuation of the same-width order question. **Positive result,
internally reconstructed.** The local insertion lemma and complete
finite-probability argument have both passed the checks linked below.

The construction and checks are internal study research. They do not edit
the paper or constitute promotion into the maintained book.

## 1. Exact scope

This continuation retains the **two-hidden-layer tanh model** of the earlier
orthogonal-input comparison. It removes input orthogonality; it does not
yet establish an arbitrary-depth extension of the new finite carrier
argument.

There are fixed training inputs $x_a\in\mathbb R^d$, $a=1,\ldots,m$,
normalized by $\|x_a\|=\sqrt d$, and fixed real labels $y_a$. Their RMS is
$Y=(m^{-1}\sum_a y_a^2)^{1/2}$. The inputs and labels do not vary with
width. Write $v_a=x_a/\sqrt d$. The dense forward pass is

\[
h_a=\tanh(Av_a),\qquad g_a=\tanh(Wh_a),\qquad
f_a=w^\top g_a/n,\qquad r_a=f_a-y_a.
\]

The read-in is $A\in\mathbb R^{n\times d}$, the hidden matrix
$W\in\mathbb R^{n\times n}$, and the readout $w\in\mathbb R^n$.
Initialization is independent Gaussian, with entries $N(0,1)$ in $A_0$
and $N(0,1/n)$ in $W_0$, and $w_0=0$. Both models share this
initialization. Dense training uses the paper's squared loss and block
mobilities $(n,1,n)$.

The comparison model is the actual order-$q$ autonomous Legendre
response-memory closure from the manuscript. It stores forward and
backward moments, retains $W_0$ exactly, and uses its own clock
$\dot\tau=\widehat\rho$, $\tau(0)=1$, where
$\widehat\rho=(m^{-1}\sum_a\widehat r_a^2)^{1/2}$. No clipping enters
either algorithm. Proof-only deletions, perturbations, stopping times,
and radial truncations do not change those algorithms.

Initially assume the manuscript's positive population readout-feature Gram
gap. For fixed normalized tanh data this gap is automatic when the inputs
are pairwise distinct up to sign. Compatible duplicate/antipodal classes
can be combined with their sample weights, by the exact quotient in
[DATA_QUOTIENT_CLOCK.md](DATA_QUOTIENT_CLOCK.md), checked in
[DATA_QUOTIENT_CHECK.md](DATA_QUOTIENT_CHECK.md). Constants and the
small-label threshold may depend on the fixed geometry. There is no
uniform claim over datasets whose points approach a degeneracy. Labels
that conflict on identical or antipodal inputs are outside this fitting
statement; replacing their residual clock by an effective clock is not
allowed.

## 2. Positive conclusion

For sufficiently small fixed $Y$, there are constants
$C_\mu,K$ and, for each $\delta>0$, a width threshold
$N_\delta$, such that at every $n\ge N_\delta$, with probability at
least $1-\delta$, **simultaneously for every integer $q\ge1$**,

\[
\left(\int\sup_{t\ge0}
 |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2\,d\mu(x)\right)^{1/2}
\le C_\mu \exp\{K\sqrt{\log(e+n)}\}
          \frac{\sqrt{\log(e+q)}}{q^2}.
\tag{1}
\]

Here $\mu$ is any fixed query law with finite second moment. Write
$\Delta A=\widehat A-A_D$, $\Delta W=\widehat W-W_D$,
$\Delta w=\widehat w-w_D$. The same event controls the normalized
parameter distance
\[
d_n(\widehat\theta,\theta_D)
=\|\Delta A\|_F/\sqrt n+\|\Delta W\|_F+\|\Delta w\|_2/\sqrt n
\]
and uniform absolute prediction error on any fixed bounded query set. Constants are
independent of width, order and physical time; $K$ can be chosen
independently of confidence. The width threshold may depend on the fixed
data and fixed label vector as well as confidence; no threshold uniform
as $Y\downarrow0$ is asserted. Probability is asserted separately at each
width, not on one event for infinitely many independent initializations.

Choose a fixed $a>K/2$ and set

\[
q_n=\left\lceil n^{1/4}
          \exp\{a\sqrt{\log(e+n)}\}\right\rceil.
\tag{2}
\]

Then $q_n=n^{1/4+o(1)}=o(n)$, and the right side of (1) is at most
$C_\mu/\sqrt n$. Indeed,

\[
\sqrt n\,e^{K\sqrt{\log(e+n)}}q_n^{-2}
                 \sqrt{\log(e+q_n)}
\le C e^{-(2a-K)\sqrt{\log(e+n)}}\sqrt{\log(e+n)}
\le C'.
\]

The supremum in (1) includes the fitted endpoint. The number of moving
coordinates is $2mnq_n+n(d+1)+O(1)=n^{5/4+o(1)}$ at fixed data.
The fixed $n\times n$ initialized mixer is still stored and used.

This resolves the requested positive alternative in the two-layer
tanh scope. It does not prove that $q=O(n^{1/4})$ without the
subpolynomial factor is sufficient, or that this order is necessary.

## 3. What closes the former finite-network gap

Define the actual dense top response and first-layer carrier by

\[
\delta_a=w\odot\operatorname{sech}^2(Wh_a),\qquad
k_a=W^\top\delta_a.
\]

The fitting estimate gives $\rho_D(t)\le Ye^{-\kappa t}$ and
$\|w(t)\|_\infty\le S:=2Y/\kappa$. The new finite-network statement
needed for (1) is a high-probability bound on the actual trained maximum:
there are events $\Omega_n$ with $\Pr(\Omega_n)\to1$ and fixed
$C>0$ such that on $\Omega_n$,

\[
\sup_{t\ge0}\max_{a,i}|k_{a,i}(t)|
       +\sup_{t\ge0}\|w(t)\|_\infty
\le CS\sqrt{\log(e+n)}.
\tag{3}
\]

Zero labels give stationary dynamics and need no division by $S$.
The event in (3) includes a successfully closed finite stopping event.
No expectation bound over every trajectory on the paper's original
fitting event is asserted or needed.

The [full proof](Q_ORDER_POSITIVE_ROUTE.md) has four steps.

1. **Separate an initialized column from the network it drives.**
   Delete a fixed finite set of first-layer neurons. Their bounded
   activation histories become external inputs to the retained network.
   That retained network keeps its actual adaptive residual. Conditional
   on its initialization, the omitted columns are independent Gaussians.
   A net over the bounded external histories permits those histories
   subsequently to be selected by the full training path.

2. **Use average response and worst-direction response for different
   terms.** Inserting one column $x\sim N(0,I_n/n)$ produces
   \[
   k_{a,i}(t)=x^\top\delta_a^{(-i)}(t)+x^\top R_a(t)x
                     +O(S^3)+o(1).
   \]
   Here $\delta^{(-i)}$ is the independently trained cavity response,
   and $R_a$ is its first response to the inserted external field.
   Gaussian concentration replaces the quadratic form by
   $\operatorname{tr}R_a/n$, uniformly over the control net. The
   normalized trace stays $O(S)$ on a finite empirical-moment stop.
   The $O(S^3)$ term is the learned increment of the inserted column.
   The weaker operator bound, a small power of $n$, is used only to
   show that the nonlinear remainder vanishes. It does not multiply the
   leading Gaussian term.

3. **Close the empirical-moment stop instead of assuming it.**
   The actual residual derivative contributes a negative Gram to the
   variational equation. The residual-Hessian perturbation has only
   $O(n)$ instantaneous rank even though the parameter space has
   $O(n^2)$ dimensions. The resulting normalized Schatten estimate
   controls the trace above. Simultaneous deletion of every fixed-size
   block supplies conditional independence for fixed empirical moments.
   The width limit is taken before increasing that fixed moment order.
   A deterministic radial truncation of a cavity-difference path retains
   its independence from the excluded column; this prevents conditioning
   on a full-network stop from invalidating the Gaussian argument.
   Choosing a fixed budget first and then sufficiently small fixed
   labels excludes the budget stop with probability tending to one.
   A temporary logarithmic maximum stop is excluded as well.

4. **Bound the actual maximum and compare the two actual flows.**
   The leading cavity Gaussian process has bounded variance and finite
   curve length in the activity variable. Its supremum has a Gaussian
   tail. A union bound over the $n$ columns, together with the bounded
   reinsertion correction, gives a maximum of order $S\sqrt{\log n}$.
   Deterministic residual decay extends the finite horizon
   $T_n=C\log n$ to every later physical time, proving (3).

For the last comparison, the already checked, general-input closure
defect $E_2$ is the extra term in its reconstructed hidden-matrix
equation:
\[
\dot{\widehat W}
=-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a\widehat h_a^\top+E_2.
\]
The read-in and readout equations have no additional defect, and

\[
\epsilon_q:=\int_0^\infty\|E_2(t)\|_Fdt
\le CY^{5/2}q^{-2}\sqrt{\log(e+q)}.
\]

It comes from [NONORTHOGONAL_DIRECT_ROUTE.md](NONORTHOGONAL_DIRECT_ROUTE.md),
checked in [NONORTHOGONAL_CHECK.md](NONORTHOGONAL_CHECK.md).
The manuscript's one-reference damping estimate is

\[
\sup_{t\ge0}d_n(\widehat\theta_{n,q},\theta_{n,D})
\le C e^{CYM}\{\epsilon_q+Z_n(M)\},
\]

where the time-integrated dense carrier tail is
\[
Z_n(M)=\int_0^\infty\rho_D(t)
\left[
\max_a\frac{\|k_a(t)\mathbf1_{\{|k_a(t)|>M\}}\|_2}{\sqrt n}
+\frac{\|w(t)\mathbf1_{\{|w(t)|>M\}}\|_2}{\sqrt n}
\right]dt.
\]
The indicators act coordinatewise. From (3), choosing
$M=CS\sqrt{\log(e+n)}+1$ makes $Z_n(M)=0$ exactly.
The damping amplification is then at most
$C\exp\{K\sqrt{\log(e+n)}\}$, proving (1). The cutoff occurs only in
this comparison inequality; no clipped flow is substituted for either
actual flow. This minimal argument does not require an additional
empirical Gaussian-square exponential moment theorem.

There is no dense-to-population bias in this comparison and no new tail
or sensitivity hypothesis in the final claim. The stopping argument
establishes the required finite-network bound for the actual initialized
trajectory.

## 4. The negative route and limits of the conclusion

The separate [negative search](Q_ORDER_LOWER_ROUTE.md) did not find
the requested lower-bound construction. For fixed compatible data, a
population discrepancy $cq^{-p}$ with $p<2$ would contradict the
paper's existing width-first order bound. A negative result requiring a
substantially larger order would therefore need a genuinely joint-width
effect or a subpolynomial loss.

Slow residual-mode rotation near the endpoint was tested. Its forward
primitive is smoother than the normalized backward signal, and the
late clock mass suppresses a Gaussian-sized slow leakage. These are
diagnostic calculations, not an actual-network lower-bound theorem.
Large-label stationary-start and negative frozen-tangent mechanisms
also failed their necessary initial checks.

The [temporal-regularity route](Q_ORDER_REGULARITY_ROUTE.md) derived
actual early-time source and prediction obstructions to a purely
exponential-history argument. Their conservative width dependence is too
weak to establish a necessary order at the root-width target. Neither
negative route is used as a proof dependency for (1).

## 5. Validation record

The core external-source insertion lemma passed complete reconstruction in
[Q_ORDER_INSERTION_CHECK.md](Q_ORDER_INSERTION_CHECK.md), including the
nonlinear residual-adaptation terms, uniform Gaussian control net,
subinterval Schatten estimate, and response trace.
The complete stopping/empirical-moment argument, collisions and bad events,
all-time extension, final rate, and compatible weighted quotient passed
reconstruction in
[Q_ORDER_POSITIVE_PROBABILITY_CHECK.md](Q_ORDER_POSITIVE_PROBABILITY_CHECK.md).
The latter checker also reconstructed the local nonlinear argument.
The coordinator read the complete final proof and checked the transfer
against the direct source bound and current manuscript.

The final proof source has SHA-256
$\texttt{9026935501ce94886d9eee81c6d318d3f45ac2f526597be5de71b0989a959f27}$.
One missing display delimiter after equation (14) was repaired after the
mathematical check at
$\texttt{cb38dfcbd752e50f0cde1ae60a8d16f7db5bcd2fafbd69dc65546a2efeb3e590}$;
both checkers confirmed this formatting-only change.
The scientific version reconstructed before status wording was updated had
SHA-256
$\texttt{d6af07cbced5abc8222466ae67b76cda6d079a21301d631d5bd044eafc4e16af}$.
Both check reports record their source versions. These are collaborative
internal checks, not independent promotion reviews or established book
results.

No training experiment was run: the user's no-GPU restriction remains in
force. No paper edit, commit or push was made. A brief targeted external
search did not supply a theorem used in this proof; every scientific
dependency above is the authorized manuscript or this study.
