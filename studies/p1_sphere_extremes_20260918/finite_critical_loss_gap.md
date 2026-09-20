# Any finite input list: a gap above zero in stationary loss

Lead-author continuation, 2026-09-18. Analytical candidate for internal
review, not established material. Scientific inputs: the complete
`docs/observable_p1.md`, this study's complete `dependent_finite_fitting.md`
and `dependent_basin_functional.md`, and the exact closure equations in
`docs/global_nonlinear.md` C.4.7.9.3--4 and C.4.7.10.D.3. No other study,
numerical experiment, external theorem, or changed model is used.

## 1. Scope and statement

Fix any finite number m of normalized inputs x_i in sqrt(d) S^(d-1),
d>=2, labels y_i in {+1,-1}, positive masses p_i summing to one, and
the exact canonical p=1 marks and odd state space. Retain all trained
blocks, the actual transpose, physical time and unhalved square loss.
The physical coordinates are theta=(w-g,c,M), with the L2/L2/Frobenius
norm. No linear-independence, endpoint boundedness, or separation beyond
the user's distinct-unoriented-input assumption is needed. In fact the
stationary-loss assertion also allows repeated or antipodal inputs.

Let p_min=min_i p_i. Every Hilbert equilibrium obeys

\[
                    L=0\quad\hbox{or}\quad L\ge p_{\min}.
\tag{1}
\]

More precisely, its loss belongs to the finite list defined by signed
partitions in Section 3. This is only a list containing all critical
values; the proof does not assert that every listed value is realized by
an equilibrium of all three blocks.

Consequently, if a trajectory starts with L(0)<p_min and converges in
the physical Hilbert norm, its limiting loss is zero, deterministically.
For equal weights this threshold is 1/m. This is a small-loss result,
not a null-basin theorem for all initial losses below one, and supplies
neither entry into the sublevel nor state convergence.

## 2. The readout equation determines stationary predictions

For any current state set

\[
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt d)],\quad v_i=Ma_i,
\quad H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\quad \phi=\tanh.
\]

The exact readout equation at an equilibrium is

\[
                   \sum_i p_i(f_i-y_i)H_i=0
                   \quad\hbox{in }L^2(\Omega_2).
\tag{2}
\]

Partition the indices into the zero group Z={i:v_i=0} and groups G of
nonzero effective vectors equal up to sign. Choose one representative
v_G for each nonzero group, and write v_i=sigma_i v_G with
sigma_i in {+1,-1}. Thus H_i=sigma_i H_G and f_i=sigma_i f_G,
where H_G=phi(b_2 dot v_G) and f_G=E_2[cH_G].

The functions H_G are linearly independent. Here is the complete needed
finite-family proof. The canonical upper mark has positive density on a
cube about zero. A linear identity among these continuous functions
therefore holds throughout that cube. Choose a direction e such that
the finitely many numbers e dot v_G are nonzero and have pairwise
distinct absolute values; the excluded directions are finitely many
proper hyperplanes. Restrict the identity to b_2=s e and use real
analyticity to extend it from an interval to all real s. Absorb the
signs into the coefficients, obtaining sum_G A_G tanh(a_G s)=0
with distinct a_G>0. At positive infinity sum_G A_G=0. If any
coefficient is nonzero, choose the smallest a_G with this property.
Using tanh(a s)=1-2 exp(-2a s)+O(exp(-4a s)) gives

\[
0=-2A_G e^{-2a_Gs}+o(e^{-2a_Gs}),
\]

a contradiction. Every coefficient is zero. This argument has no
restriction on the number of groups versus dimension.

Write

\[
W_G=\sum_{i\in G}p_i,\qquad A_G=\sum_{i\in G}p_i\sigma_i y_i.
\]

Substitution in (2) and the proved independence give

\[
              W_G f_G-A_G=0\quad\hbox{for every }G.
\tag{3}
\]

The zero group has predictions zero. Thus all stationary predictions
are fixed by the signed grouping and the data weights and labels.

## 3. The finite list and its gap

Set W_Z=sum_(i in Z)p_i, with W_Z=0 if Z is empty. Equation (3)
and binary labels yield the exact critical-loss expression

\[
       L=W_Z+\sum_G\left(W_G-\frac{A_G^2}{W_G}\right).
\tag{4}
\]

For a finite list there are finitely many choices of Z, of the partition
into nonzero groups, and of the signs sigma_i. Formula (4), evaluated
over those choices, is the asserted finite list. No geometry-independent
bound on a decay rate follows from its finiteness.

Within one group, let W_G^+ and W_G^- be the total masses with oriented
labels sigma_i y_i equal to +1 and -1 respectively. Its contribution is

\[
  W_G-\frac{A_G^2}{W_G}
       =\frac{4W_G^+W_G^-}{W_G^++W_G^-}.
\tag{5}
\]

This is zero if one of the two masses is zero. Otherwise both masses
are at least p_min. Writing a=min(W_G^+,W_G^-) and
b=max(W_G^+,W_G^-), its value is 4ab/(a+b)>=2a>=2p_min.
If Z is nonempty, W_Z>=p_min. Every term in (4) is nonnegative, so
any positive value of L is at least p_min, proving (1).

For equal weights, (4) reads

\[
 L=\frac{|Z|}{m}
    +\frac1m\sum_G\frac{4n_G^+n_G^-}{n_G^++n_G^-},
\tag{6}
\]

where n_G^+ and n_G^- count the two oriented labels in G. The same
bound is L=0 or L>=1/m. It is a universal lower bound, not a claim
of the sharp attainable positive critical loss for every particular
input configuration.

## 4. Consequence for convergent trajectories

The exact Hilbert flow has a continuous vector field F. If
theta(t)->theta_* in the Hilbert norm, then F(theta_*)=0. Otherwise
pair the velocity with the fixed nonzero vector F(theta_*). Continuity
makes this pairing at least ||F(theta_*)||^2/2 for all sufficiently
large times, so its time integral is unbounded. The same pairing with
theta(t) converges, a contradiction.

Continuity of L and its dissipation identity give
L(theta_*)<=L(theta(0)). If the latter is below p_min, (1) forces
L(theta_*)=0. This proves the deterministic small-loss implication.

The separate open fitting theorem shows this sublevel is nonempty for
compatible finite data. That existence statement does not show that a
trajectory from canonical initialization ever enters it. Positive limiting
loss without a state limit, general bad-basin nullity above this threshold,
and all-time state convergence remain open here.
