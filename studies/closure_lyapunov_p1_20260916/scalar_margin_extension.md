# A normalized-readout monotonicity principle removes the cone gap

Root continuation, 2026-09-16. Candidate proof developed independently while
the two continuation routes worked on initialization and general pairs.
Scope: exact canonical p=1 closure, existing study and established equations
only. This is a continuation of the user-requested investigation, not a
change of architecture or normalization. No numerical experiment is used.

## 1. General scalar geometry

Let the current characteristic state be X=(h,c), where h comprises (w,M)
with the prescribed physical L2/Frobenius metric and c is the population
readout in L2. Suppose a data symmetry gives opposite predictions on the
two equally weighted opposite-label inputs. Define

U(h)=(H^2(x_+)-H^2(x_-))/2,
F(X)=<c,U(h)>, C(X)=||U(h)||^2, q(X)=||c||^2.

Labels are +A,-A with any fixed A>0. On the invariant initialized symmetry
class the exact unhalved square loss is L=(A-F)^2. Its gradient flow is

X_dot=2(A-F) grad F.

Every derivative is in the fixed physical metric. Introduce the autonomous
auxiliary flow X_s=grad F, initialized with c=0 and the canonical hidden
state. It is the same gradient-ascent equation already justified in proof.md.
Its finite-s existence follows directly from
||c||infty<=s, ||M||op<=2+s^2/2,
||w-g||infty<=B_1(s^2+s^4/8), as proved there from the exact equations.
Thus it exists on each finite s interval, independently of whether fitting
has occurred in physical time.

Write
K=||grad F||^2=C+||grad_h F||^2.
Since F is linear in c, this flow obeys the exact identities

F_s=K, q_s=2F.

Assume only C_0=||U(h_0)||^2>0. At s=0, grad_h F=0 because c=0,
so c(s)=s U(h_0)+o(s) in L2 and F(s)=s C_0+o(s). Hence F(s)>0 for
small positive s. Since F_s>=0, F remains positive thereafter. Then q>0,
because F=<c,U> would vanish if c=0. Cauchy-Schwarz yields

F^2<=q C<=q K.

For every s>0 the current-state functional

P(X)=q/F^2

satisfies

P_s = 2/F-2qK/F^3
    = -2(qK-F^2)/F^3 <=0,
lim_(s downarrow0) P(X_s)=1/C_0.

Consequently, at every positive finite s,

q<=F^2/C_0,
C>=F^2/q>=C_0,
F_s=K>=C_0.

No sign condition on an individual backward coefficient or lower-layer
cross term is needed. C itself is not asserted to be pointwise monotone.
The quantity F/||c|| is nondecreasing and is bounded above by ||U||.
The explicit source of improvement is

qK-F^2=(q C-F^2)+q||grad_h F||^2.

The first nonnegative term measures the failure of c to align with the
current contrast U; the second is actual hidden-gradient activity.
This decomposes the normalized-output progress into two current-state terms.
All quantities use the current state and fixed data only.

P is singular at ambient states F=0. Along the initialized path it has
the displayed finite one-sided limit. We do not claim a continuous ambient
extension at every (c,F)=(0,0), nor a strict Lyapunov function on neutral
directions. One may instead state monotonicity on t>0 with its initialized
limit, or use F/||c|| with the analogous positive one-sided limit sqrt(C_0).

## 2. Physical-time theorem

Since F(0)=0 and F_s>=C_0, F crosses A at a unique s_*<=A/C_0.
Uniqueness holds because K>=C_0. On the compact interval [0,s_*], K is
continuous and bounded. The clock s_dot=2(A-F(s)), s(0)=0 stays strictly
below s_* for finite t: e=A-F obeys e_dot=-2K e, so

e(t)=A exp(-2int_0^t K(s(v))dv)>0.

It approaches s_* as t tends to infinity. The composed curve solves the
canonical physical equations and coincides with their unique solution.
Therefore

L(t)<=A^2 exp(-4 C_0 t),
C(X_t)>=C_0,
||c_t||^2<=F(X_t)^2/C_0<=A^2/C_0,
int_t^infty ||X_dot||physical dt<=sqrt(L(t)/C_0).

The last bound uses ||X_dot||=2e sqrt(K)<=-e_dot/sqrt(C_0).
There is a finite fitting endpoint, with strong physical convergence and
joint-law W2 convergence under the identical frozen-mark coupling.
Bounded feature-time speeds on [0,s_*] also give uniform convergence of
w-g and c, and Frobenius convergence of M.

In physical time the new current-state potential obeys exactly

P_dot=-4(A-F)(qK-F^2)/F^3<=0  (t>0).

It is not claimed to decay to zero; its role is to preserve a positive
normalized signed-output margin and hence prevent hidden contrast collapse.
The ordinary loss then controls full-state convergence.

## 3. Which input arrangements this applies to

The theorem applies to every input pair for which the actual closure and
prescribed initialization admit a measure-preserving metric isometry that
exchanges the two inputs and changes the readout sign, AND for which
C_0>0. The reflection family
u_+=(a,b), nu_-=(a,-b), a>=0,b>0,a^2+b^2=1
has this exact p=1 symmetry, as verified in proof.md. It spans every angular
separation in (0,pi], rather than only a neighborhood of pi. Initial C_0>0
for its whole range must still be verified from the exact dictionary; that
calculation is a distinct obligation and is not assumed proved here.

Signed permutations provide additional exact dictionary symmetries.
An arbitrary rotation does not follow from the initialization's Gaussian
root isotropy: the fixed finite dictionary need not be rotation invariant.
For a generic oriented pair, the two prediction residuals need not remain
opposite. Then the physical flow need not be a scalar multiple of grad F,
and q_s=2F does not describe the actual training path. We do not silently
extend this scalar theorem to that case.

## 4. Relation to the earlier result and scope

Once C_0>0 is checked for the reflection family, this theorem supersedes the
cross-sign estimate as a necessary bottleneck for that family's fitting and
state convergence. The sign condition can remain an interesting sufficient
mechanism for monotonic individual signals, but is not needed for convergence.
The earlier quantitative endpoint-increase theorem remains valid; this new
argument yields C>=C_0 and describes when the normalized margin increases.
It does not by itself give a uniform strictly positive endpoint gain for every
pair unless hidden activity or readout misalignment is separately shown.

No numerical evidence, closure-order limit, or full-network identification
is involved. The remaining broad target is arbitrary orientation with unit
opposite labels in the fixed canonical dictionary, without exact residual
symmetry.
