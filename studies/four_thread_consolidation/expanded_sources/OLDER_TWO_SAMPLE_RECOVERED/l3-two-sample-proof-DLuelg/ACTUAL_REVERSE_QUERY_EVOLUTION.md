# An exact linear evolution along a fixed trajectory for the middle reverse query

Root candidate, 2026-09-06. This is an actual-trajectory identity and
propagator estimate, not a global population existence theorem. Its
coefficients depend on the full trajectory; treating them as prescribed
does NOT prove stability between two different training trajectories.
The ordinary RMS bounds below are included to verify the constants,
not advertised as new substitutes for distributional response control.
No external theorem or numerical experiment is used.

Use phi(z)=1+atan(z)/10. Write a=7/6, e=1/10, c=1/5, so
|phi|<=a, |phi'|<=e, |phi''|<=c. The two labels y_a are independently
chosen from {-1,1}; C=[[1,rho],[rho,1]], -1<=rho<1.

## 1. Precise existing-trajectory premises

Let H_ell=L2(Omega_ell,mu_ell), ell=1,2,3, with probability measures.
W^(2):H_1->H_2 and W^(3):H_2->H_3 are bounded operators whose
increments are C1 Hilbert--Schmidt curves. The first sample pair
Z^(1)_a is C1 in H_1; at rho=-1 impose Z^(1)_2=-Z^(1)_1.
The readout w=W^(4) is C1 in H_3 and starts at zero. Define

  H^(ell)_a=phi(Z^(ell)_a),
  Z^(2)_a=W^(2)H^(1)_a, Z^(3)_a=W^(3)H^(2)_a,
  delta^(3)_a=w phi'(Z^(3)_a),
  q^(2)_a=(W^(3))*delta^(3)_a.

Either use the uncut equations, or smooth scalar cuts tau_R satisfying
tau_R(0)=0, |tau_R(v)|<=|v|, and 0<=tau_R(v)/v<=1 for v!=0.
For the cut equations put

  delta^(2)_a=phi'(Z^(2)_a)tau_R2(q^(2)_a),
  q^(1)_a=(W^(2))*delta^(2)_a,
  (Z^(1)_a)'=(1/2)sum_b C_ab y_b phi'(Z^(1)_b)tau_R1(q^(1)_b),
  (W^(ell))'=(1/2)sum_b y_b delta^(ell)_b tensor H^(ell-1)_b,
                         ell=2,3,
  w'=(1/2)sum_b y_b H^(3)_b.                           (1)

Here (v tensor h)u=v E[hu]. In the uncut case both tau maps are
the identity. Primes denote feature time, on an EXISTING interval
[0,S]. The readout and all equations in (1) are the actual uncut
gradient-ascent equations when the cuts are identities. In the cut
case no gradient/action identity is asserted. At finite width use
empirical probability measures, transpose in place of adjoint,
and tensor matrix vh^T/n; (1) then has exactly the 1/(2n) hidden
matrix normalization and the 1/2 first/readout normalization.
No finite residual-mode symmetry is presumed in this feature-flow
statement, and no identification with raw physical GD is claimed.

On H_ell x H_ell use the ordinary product Hilbert norm. Call the
block-diagonal duplication of W^(ell) simply bold W^(ell). Let
Y=diag(y_1,y_2) act on the sample pair. Let P_ell multiply component
a by phi'(Z^(ell)_a), and let Lambda_j multiply it by
tau_Rj(q^(j)_a)/q^(j)_a, continuously extended at zero. For identity
cuts set Lambda_j=I. All have their explicitly stated sample action;
||P_ell||<=e and ||Lambda_j||<=1. Define the scalar feature second
moment matrices

  G_ell,ab=E_ell[H^(ell)_a H^(ell)_b], ell=1,2,

acting on pairs at the next population. They are positive semidefinite
and have norm at most 2a^2. In operator formulas a scalar sample matrix
is tensored with the identity of that population.

## 2. Forward derivative without differentiating the middle gate

Product and along-curve chain rules give, in the pair Hilbert spaces,

  (H^(1))'=(1/2)P_1 C Y P_1 Lambda_1
                          (bold W^(2))*P_2 Lambda_2 q^(2),

  (Z^(2))'=(1/2)[G_1 Y+bold W^(2)P_1 C Y P_1 Lambda_1
                                  (bold W^(2))*]
                                  P_2 Lambda_2 q^(2).

For example, the learned-matrix term in sample a is
(W^(2))'H^(1)_a=(1/2)sum_b G_1,ab y_b delta^(2)_b.
The remaining term is W^(2)(H^(1)_a)', yielding the second display.
Because Y commutes with every block-diagonal operator and multiplier,
but need not commute with C or G_1, the correct factorization is

  (H^(2))'=(1/2)A_2 Y q^(2),
  A_2=P_2[G_1+bold W^(2)P_1 C P_1 Lambda_1
                          (bold W^(2))*]P_2 Lambda_2. (2)

No time derivative of P_2 appears in (2). For identity cuts A_2 is
self-adjoint positive semidefinite: G_1 and C are such matrices,
and the other summand is their operator congruence. For separate
sample cuts this positivity need not hold, and is not used. Always,

  ||A_2||<=2e^2[a^2+e^2||W^(2)||_op^2].               (3)

To justify the chain rule without assuming Frechet differentiability
of an activation map L2->L2, represent a C1 L2 curve as its initial
field plus the Bochner integral of its derivative. Fubini supplies
almost-everywhere absolutely continuous scalar representatives.
Their scalar chain rule has integrand phi'(Z)Z', dominated in L2
by e|Z'|. It gives the Hilbert-valued chain rule. Continuity follows
by truncating the fixed L2 factor in
[phi'(Z(t))-phi'(Z(s))]Z'(s), using bounded gates. The same reasoning
applies to phi' with bounded phi''. Products with bounded C1 operator
curves obey the usual bounded-bilinear product rule.

## 3. The exact reverse evolution and all its terms

Let D_3 be the pair multiplication operator with entries
w phi''(Z^(3)_a). Let J_3,ab=E_3[delta^(3)_a delta^(3)_b].
Write bold v=(w',w'), a pair on population 3. Differentiating the
ACTUAL reverse query, rather than differentiating delta^(2), yields

  (q^(2))'=b+K q^(2),
  K=(1/2)(bold W^(3))*D_3 bold W^(3) A_2 Y,           (4)
  b=(1/2)J_3 Y H^(2)
       +(bold W^(3))*P_3 bold v
       +(1/2)(bold W^(3))*D_3 G_2 Y delta^(3).        (5)

Indeed, (W^(3))'*delta^(3)=(1/2)J_3 Y H^(2).
Also (delta^(3))'=P_3 bold v+D_3(Z^(3))', and
(Z^(3))'=(1/2)G_2 Y delta^(3)+bold W^(3)(H^(2))'.
Inserting (2) proves (4)-(5), including the order of the sample
matrices, their signs, and every factor 1/2. In particular no term
phi''(Z^(2))q^(2) occurs in this equation for q^(2) itself.
It reappears when DIFFERENT trajectories or the coefficient A_2
are compared; (4) does not eliminate that comparison problem.

## 4. Uniform finite-interval constants, independent of the cuts

Let M_ell,0=||W^(ell)(0)||_op. The bounded readout derivative implies
||w(s)||_infinity<=as for s<=S, even though only its initial L2
regularity was stipulated. The common pointwise integral representative
proves this bound; it also gives ||w(t)-w(s)||_infinity<=a|t-s|.
Thus ||delta^(3)_a(s)||_2<=eas and

  ||W^(3)(s)||_op <= M_3(s):=M_3,0+ea^2 s^2/2,
  ||q^(2)_a(s)||_2<=M_3(s)eas,
  ||delta^(2)_a(s)||_2<=M_3(s)e^2as.

Here the matrix derivative norm is bounded by the sum of the two
rank-one norms, including their factor 1/2, and ||tau(q)||_2<=||q||_2.
Applying this once more to W^(2) gives

  ||W^(2)(s)||_op <= M_2(s)
    :=M_2,0+e^2a^2[M_3,0 s^2/2+ea^2 s^4/8].         (6)

No action identity or independent-neuron assumption enters (6).
Let M_ell=M_ell(S). Equations (3)-(5) imply, for s<=S,

  ||K(s)||<=k_S:=ce^2aS M_3^2(a^2+e^2 M_2^2),

  ||b(s)||<=b_S:=sqrt(2)[e^2a^3 S^2+ea M_3
                                      +ce a^4 S^2 M_3].       (7)

For the first term of b, ||J_3||<=2e^2a^2 S^2 and
||H^(2)||<=sqrt(2)a. For the second, ||bold v||<=sqrt(2)a.
For the third, ||D_3||<=caS, ||G_2||<=2a^2, and
||delta^(3)||<=sqrt(2)eaS. These estimates give exactly (7).
The same constants apply to every width with bounded initial operator
norms and to every existing cut or uncut population curve above.

## 5. What the linear propagator estimate says

Along any fixed such curve, K is strongly continuous as a bounded
operator family. Each gate multiplier has this property by continuity
in probability and truncation against a fixed L2 test field; D_3
also uses the established L-infinity continuity of w. The other
operators are norm continuous. The same arguments make b continuous
in its pair Hilbert space. No operator-norm continuity of a Nemytskii
multiplier is required or asserted.

For a prescribed K, the linear integral equation v'=K(s)v has a
unique propagator U(t,r) with

  ||U(t,r)||<=exp(k_S(t-r)), 0<=r<=t<=S.              (8)

For a direct construction, start at a fixed vector, iterate its
integral equation, and bound the j-fold ordered time integral by
[k_S(t-r)]^j/j! times its norm. The series converges uniformly and
defines a bounded linear operator. Strong integrals suffice; no
Bochner integration in the whole bounded-operator space is needed.
The same series and the integral equation prove uniqueness by
iteration of a zero-initial-data difference. Adding the continuous
forcing gives

  q^(2)(t)=U(t,0)q^(2)(0)+integral_0^t U(t,r)b(r)dr,
  q^(2)(0)=0,
  sup_(s<=S)||(q^(2))'(s)||_2
                       <=b_S+k_S sqrt(2)M_3 eaS.     (9)

The derivative norm here is the ordinary PAIR L2 norm. In particular,
q^(2) has an L2 time-Lipschitz bound on the interval, independent
of the cuts and width under the stated operator bounds. Such temporal
regularity is weaker than neuronwise tail control.

For uncut equations, A_2 is positive, but D_3 can have either sign.
Even multiplying by Y only replaces it by entries y_a w phi''(Z^(3)_a);
these are not assumed nonpositive. Thus (8) is a bounded propagator
estimate, not a contraction claim. It controls a perturbation of
the forcing when the full coefficient path is FIXED. Comparing
different trajectories adds (K-tilde K)tilde q^(2). That product is
not bounded linearly by their raw L2 distance using (7) alone.
Nor does an arbitrary bounded L2 operator propagate Gaussian tails
of its input. No exponential neuronwise moment, removal of clips,
global population continuation, or full-sequence joint limit follows
from (4)-(9) without an additional argument controlling the actual
coefficient dependence and its Gaussian action.
