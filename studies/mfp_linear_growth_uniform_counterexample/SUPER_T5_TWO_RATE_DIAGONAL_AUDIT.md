# Audit of the two-rate super-`t^5` diagonal

## Verdict

The proposed two-rate diagonal is logically sound and, unlike the earlier
`t=1` construction, would prove genuine super-`t^5` growth along one
sequence of horizons for one activation.  It does not require the final
activation to possess a cubic or fifth jet.

The exact remaining premise is a compact-transition insertion theorem for
the actual width-first coefficient at each fixed finite horizon `t`:

> Given a finite smooth old truncation, a horizon `t`, a target `A`, and an
> arbitrarily small `d_1` radius, one can insert a disjoint compact smooth
> bump, renormalize, and obtain a smooth new truncation with
> `|beta_t|>=A` inside that radius.

The universal local coefficient needed for this premise is nonzero and has
the favorable explicit value derived below.  Thus no temporal cancellation
obstructs the construction.  Promotion to an unconditional full-network
theorem still requires the same response-aware marked intertwining and
remainder grouping as the one-pair insertion theorem, now with the general-
`t` Euler weights.

## 1. Exact general-`t` local principal coefficient

Let `K_N` denote the coefficient of the quadratic highest-excess sector in
the order-five output of `N` Euler steps.  For a scalar ridge this is the
combination

\[
 K_N=5c_D(N)-c_{CA}(N)+c_{B^2}(N),             \tag{1.1}
\]

where `c_D,c_CA,c_B2` multiply respectively
`f^(5)(f')^5`, `f^(4)f''(f')^4`, and
`(f''')^2(f')^4`.  Exact Euler chronology gives

\[
\begin{aligned}
 K_N={}&{1\over24}{N\choose1}
       +{19\over24}{N\choose2}
       +{13\over4}{N\choose3}\\
     &+{9\over2}{N\choose4}
       +2{N\choose5}.                          \tag{1.2}
\end{aligned}
\]

This is a finite identity: an order-five Euler word uses at most five time
slices, hence its coefficient is a binomial polynomial of degree at most
five; direct chain-rule evaluation at `N=0,...,5` gives (1.2).

For

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),
\]

the coarse term acquires the factor `2^5=32`.  Therefore

\[
 \boxed{
 K_t^\Delta=K_{2t}-32K_t=-{8t^4+3t\over24}<0
 }
 \qquad(t\ge1).                                \tag{1.3}

At `t=1`, (1.3) is `-11/24`, recovering the previous node symbol.

To make the activation perturbation compact, choose
`p in C_c^infinity((-1/4,1/4))` with

\[
 \int p=0,qquad \int(p'')^2>0,
\]

put `P(y)=int_(-infinity)^y p(s)ds`, and insert

\[
 \delta wP((x-X)/w).                            \tag{1.4}
\]

Both the value perturbation and its slope perturbation are compactly
supported, and

\[
 \|\delta wP((\cdot-X)/w)\|_{C^1}
 \le\delta\{w\|P\|_\infty+\|p\|_\infty\}.    \tag{1.5}

The quadratic singular integrals are

\[
 \int pp''''=\int(p'')^2,qquad
 \int p'p'''=-\int(p'')^2.                    \tag{1.6}

Thus the principal contribution of one activation occurrence is

\[
 -{8t^4+3t\over24}
 r^2sv^4\,\gamma(X){\delta^2\over w^3}
 \int(p'')^2.                                  \tag{1.7}

It is nonpositive at every node.  The lower nodes have strictly positive
mean weight, so (1.7) is strictly negative after the width limit.  With
`w=delta*sqrt(gamma(X))`, its magnitude is proportional to

\[
 (8t^4+3t)\delta^{-1}\gamma(X)^{-1/2}.         \tag{1.8}

For fixed finite `t` and fixed old truncation, this tends to infinity while
the `C^1` distance tends to zero.  Hence the desired stage target is
compatible with every previously imposed tail ceiling, provided the full
marked remainder estimate accompanies (1.7).

### 1.1 General-`t` marked remainder grading

The needed remainder estimate does not require the support of the special
`t=1` 979-term map.  Work in the complete generated-core order-five tensor
before its final Gaussian expectations are flattened.  Give a new
activation derivative `phi^(r)`, `r>=2`, excess `r-1`.  Five learning-rate
marks imply

\[
 e:=\text{total new excess}\le4.               \tag{1.9}
\]

This grading is independent of the number of Euler steps; the horizon only
changes the finite numerical chronology coefficients.

Suppose a term has `k` new high-derivative factors split among `R` distinct
activation-node source classes.  In the `q=1` initialization peel, distinct
classes have independent standard-Gaussian endpoint coordinates; exact
source coincidences are merged into one class.  Localization therefore gives

\[
 C_{t,{\rm old}}P_{t,{\rm old}}(X)
 \delta^k\gamma(X)^R w^{R-e}.                 \tag{1.10}
\]

After `w=delta*sqrt(gamma(X))` and division by the principal scale
`delta^(-1)gamma(X)^(-1/2)`, its two margins are

\[
 m_\delta=k+R-e+1,
 \qquad
 2m_\gamma=3R-e+1.                            \tag{1.11}
\]

For `R>=2`, (1.9) makes `m_gamma>0`.  For `R=1`, all margins are
nonnegative except the apparent linear `(e,k)=(4,1)` fifth derivative;
four integrations by parts, equivalently the four vanishing moments of
`p''''` of degrees zero through three, remove its negative power.
Its first quadratic term has effective `k=2`.  Equality in both margins is
therefore possible only for

\[
 R=1,qquad e=4,qquad k_{\rm eff}=2.           \tag{1.12}
\]

The complete sector (1.12), grouped before absolute values, is precisely
the node symbol (1.7).  Every other term has a positive `delta` or Gaussian
margin.  Since `t` and the old truncation are fixed at a stage, their
possibly enormous constants are finite; choose `X` first and `delta`
second.  This proves the compact-bump insertion premise from the established
fixed-horizon, source-aware generated-core intertwining.  If that
intertwining is not taken as an established input, (1.9)--(1.12) identify
the exact remaining proof obligation.

## 2. Correct order of the diagonal choices

Fix `rho>0` and choose increasing integers `t_m>=2`.  At stage `m`:

1. Start from the already fixed smooth truncation `psi_(m-1)`.
2. Choose a new disjoint compact bump satisfying every old `d_1` ceiling
   and, after RMS normalization, arrange
   \[
     |\beta_m|:=|[h^5]\Delta_{t_m}^{\psi_m}(h)|
     \ge \max\{20,t_m^m\}.                    \tag{2.1}
   \]
3. Let `kappa_m` be the cubic coefficient of this smooth truncation.  Only
   now choose `h_m>0` so small that
   \[
     h_m\le {\rho\over t_m},                  \tag{2.2}
   \]
   and at both `r=h_m,h_m/2`,
   \[
    \left|{Delta_{t_m}^{\psi_m}(r)
       -\kappa_m r^3\over r^5}-\beta_m\right|
       \le {|\beta_m|\over20}.                \tag{2.3}
   \]
4. Apply the width-uniform `d_1` stability lemma to all four terminal
   outputs
   \[
   F_{2t_m}(h_m),\quad F_{t_m}(2h_m),\quad
   F_{2t_m}(h_m/2),\quad F_{t_m}(h_m),          \tag{2.4}
   \]
   and reserve future-amplitude budgets making the combined final-output
   error in each defect at most
   \[
      {|\beta_m|\over20}(h_m/2)^5.             \tag{2.5}
   \]

Every schedule in (2.4) is finite when its budget is created.  Its
continuity constant may grow arbitrarily with `t_m` and with the old narrow
bumps; it is nevertheless finite.  Since (1.8) permits the next transition
amplitude to be arbitrarily small, finitely many old ceilings never block a
later stage.  Geometric allocation of each newly created budget makes all
countably many tail requirements simultaneous.

In parallel, enumerate every pair `(k,R)` of positive integers and reserve
the usual compact-step tail budgets.  The three-epsilon argument then proves
that the one final activation has finite width-first expected outputs for
every fixed finite horizon and every fixed step.  The special budgets (2.5)
preserve the witnesses after that width limit has been taken.

## 3. Two-point minimax and absence of a final cubic jet

For any candidate `kappa in R`, define

\[
 Q_{m,\kappa}(r)
 ={\Delta_{t_m}^{\phi}(r)-\kappa r^3\over r^5},
 \qquad
 x={\kappa_m-\kappa\over h_m^2}.               \tag{3.1}

Equations (2.3)--(2.5) give

\[
 Q_{m,\kappa}(h_m)=x+\beta_m+e_{m,1},
 \qquad
 Q_{m,\kappa}(h_m/2)=4x+\beta_m+e_{m,2},       \tag{3.2}

with, after the harmless allocation constants are combined,

\[
 |e_{m,1}|\vee|e_{m,2}|\le {|\beta_m|\over10}. \tag{3.3}

For every real `x,beta`,

\[
 3|\beta|
 =|4(x+\beta)-(4x+\beta)|
 \le5\max\{|x+\beta|,|4x+\beta|\}.           \tag{3.4}

Hence

\[
 \max_{r\in\{h_m,h_m/2\}}|Q_{m,\kappa}(r)|
 \ge {1\over2}|\beta_m|                       \tag{3.5}

for every `kappa`.  Both rates belong to `(0,rho/t_m]`; taking the supremum
and then the infimum over `kappa` yields

\[
 \boxed{
 B_\phi(t_m,\rho)\ge {1\over2}t_m^m.
 }                                             \tag{3.6}

In particular, for every fixed power `q`,

\[
 {B_\phi(t_m,\rho)\over t_m^q}\longrightarrow\infty.
 \tag{3.7}

No limit of the numbers `kappa_m` is used.  The candidate `kappa` may depend
on `t_m`, exactly as allowed by the infimum in the definition of `B_phi`.
The two rates prevent that one scalar from cancelling the fifth term at
both points.  Consequently the final activation need not have a cubic jet,
a fifth jet, or any specified small-step modulus.

## 4. Normalization and old-bump interactions

The compact bump (1.4) is easier than a permanent slope step:

- higher derivatives of different bumps have disjoint supports;
- the value and slope perturbations vanish outside the new interval;
- the normalizer changes by at most
  \[
   \delta w\|P\|_\infty
      \sqrt{\mathbb P\{|G-X|\le w/4\}},        \tag{4.1}
  \]
  so its additive global-rescaling error is negligible compared with
  (1.8);
- all old high-derivative moments are fixed finite coefficients at the
  current stage.

As in the one-pair audit, a valid proof must classify arbitrary subsets of
moment atoms as new while the complementary atoms remain old.  The
finite-dimensional node symbol (1.7) groups the complete true zero-margin
sector before absolute values; every derivative of a downstream coefficient
loses new singular excess.  Positive-margin constants may depend on the old
truncation and on `t_m`, because `X,w,delta` are chosen only after both are
fixed.

## Claim boundary

The two-rate minimax, countable tail diagonal, fixed-step width-first
transfer, normalization estimate, and super-polynomial conclusion are
complete.  Under the already established fixed-horizon source-aware
generated-core intertwining, Section 1.1 supplies the general-`t` compact-
bump premise and the construction is an unconditional full-`L=2` theorem.
The special `t=1` 979-term map alone would not suffice; without the general
marked intertwining, that premise remains the exact conditional boundary.
