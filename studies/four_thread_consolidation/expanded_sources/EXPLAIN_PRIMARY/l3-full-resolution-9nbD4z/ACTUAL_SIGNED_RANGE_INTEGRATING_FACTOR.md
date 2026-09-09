# Actual range integrating factor and the surviving action–response pairing

Status: exact finite-width identities and a conditional response-energy
inequality. The scalar curvature cancels, including in the actual moving
training range, but the existing rare primal derivative/action estimates
do not close the resulting response estimate. No simulation, generic
operator counterexample, or differentiation of a primal norm inequality
is used. This note does not establish global population continuation.

Sources are ACTUAL_MOVING_RANGE_PROBE_NORMAL_FORM.md,
ACTUAL_RARE_BACKWARD_DERIVATIVE.md, RARE_BACKWARD_ENERGY.md, and
ACTUAL_TWO_TIME_RARE_RETURN.md. The derivative/action consequences below
have the zero-initial-readout scope of the latter primal estimates. The
range algebra itself holds for the actual uncut finite-width trajectory
on its controlled finite feature horizon. All sets below are fixed in
time, but may be selected from the entire actual trajectory and its probe
covariance; they do not depend on the realized auxiliary probe.

## 1. Keep the actual off-block and normal memory

Use the normalized vector norm and the range notation of the moving-range
note. Write D=diag(phi'(z2)), beta=phi''(z2)/phi'(z2),
b=phi''(z2)q=beta delta. For arctangent,

    D_j=1/(1+z_j^2),       beta_j=-2z_j/(1+z_j^2),
    |beta_j|<=1.

The exact reduced equation is

    a'(t)=M_(b_t)[Acal_t a(t)+integral_0^t N(t,s)a(s)ds]+F(t),  (1)

where

    F(t)=Gcal_t R_t a(t)
         +Gcal_t integral_0^t U_H(t,s)Hcal_s R_s a(s)ds
         +f_tilde(t),
    f_tilde=g+Gcal w_0+b T w_0.

Every displayed map multiplying a or its history in F is bounded.
The additive term b T w_0 is controlled by the actual probe-source
estimate, not by a width-uniform operator bound on M_b.
Together the source estimates in the moving-range note give, with
Aprobe(t)=n E_xi||a(t)||_n^2,

    n E_xi||F(t)||_n^2
        <=C_S[1+Aprobe(t)+integral_0^t Aprobe(s)ds].       (2)

This estimate is unweighted. In particular it does not bound D^{-1}F.
The later exact source analysis in
ACTUAL_WEIGHTED_ADDITIVE_PROBE_SOURCE.md proves
n E_xi||D^{-1}f_tilde||_n^2<=C_S: its direct normal response is
purely top-layer, so T w0=0 and Gcal w0 has an exact D factor.
Only the response-dependent parts Gcal R a and Gcal w_a remain
uncontrolled after division by D.

Fix E, put P=P_E, and let alpha_E(t), r_E(t)=ghat_E(t)+rho_E(t)
come from its single fully pruned reference. The exact primal identity is

    P z2'=alpha_E P Dq+r_E.                             (3)

Define the actual returned response

    h_E(t)=P[(Acal_t-alpha_E(t)I)a(t)
                           +integral_0^t N(t,s)a(s)ds]. (4)

It includes all three terms

    (P Acal_t P-alpha_E P)a_E(t),
    P Acal_t (I-P)a(t),
    P integral_0^t N(t,s)a(s)ds.                        (5)

Thus it retains rare self-block error, transport from the large
complement, and recycled normal memory. No rare-to-large-bulk smallness
is presumed. Equation (1) on E is exactly

    a_E'=alpha_E b_E a_E+b_E h_E+P F.                   (6)

## 2. Exact cancellation without differentiating the mobility

Applying the scalar chain rule to the actual primal path in (3),

    (log D_j)'=beta_j z_j'=alpha_E b_j+beta_j r_(E,j),
    alpha_E b_j=(log D_j)'-beta_j r_(E,j),     j in E.  (7)

No time derivative of Acal, T, or alpha_E is needed. Set c_E=D_E^{-1}a_E.
The range response satisfies the exact transformed equation

    c_E'=-beta_E r_E c_E+beta_E q_E h_E+D_E^{-1}P F.   (8)

This is a cancellation for the actual range coordinate, not a variation
of an independent copied or pruned trajectory. The remaining terms are
explicitly the residual times the transformed response, the returned
response times beta q, and a gate-weighted source.

Equivalently the diagonal scalar propagator in (6) is

    Phi_E(t,s)=M_[D_E(t)/D_E(s)
                      exp(-integral_s^t beta_E(u)r_E(u)du)]. (9)

Since a(0)=0, finite-dimensional variation of constants gives

    a_E(t)=integral_0^t Phi_E(t,s)[b_E(s)h_E(s)+P F(s)]ds. (10)

Equations (8) and (10) retain the same unknown response inside h_E.
Neither is an independently forced scalar solution.

## 3. A concrete actual signed energy and conditional majorant

Define

    E_D(t)=n E_xi||c_E(t)||_n^2,
    U_j(t)=n E_xi c_j(t)^2,
    V_j(t)=n E_xi[c_j(t)h_j(t)],              j in E.

All expectations condition on the entire actual path. Finite width
makes these quantities finite; no width-uniform weighted bound is
asserted. Since D<=1, E_D>=n E_xi||a_E||_n^2. Equation (8) gives

    (1/2)E_D'
      =-<beta_E r_E,U>_n+<beta_E q_E,V>_n
                        +n E_xi<c_E,D_E^{-1}P F>_n.    (11)

In particular the scalar term alpha_E b_E U has disappeared. The sign
of the two displayed remaining covariance pairings has not been assigned.

To state a checkable sufficient estimate, put

    R_E=n E_xi||r_E c_E||_n^2,
    Q_E=n E_xi||q_E c_E||_n^2,
    F_D=n E_xi||D_E^{-1}P F||_n^2,
    A_F=n E_xi||(I-P)a||_n^2,
    epsilon_E=||P Acal P-alpha_E P||_op.

Conditional Cauchy--Schwarz, the boundedness of N and Acal, and D<=1
give the actual response inequality

    (1/2)E_D'
      <=sqrt(E_D R_E)
        +sqrt(Q_E)[epsilon_E sqrt(E_D)+C_S sqrt(A_F)
                         +C_S integral_0^t sqrt(Aprobe(s))ds]
        +sqrt(E_D F_D).                                (12)

For the middle term, apply Cauchy--Schwarz to
n E_xi<beta q c_E,h_E>, then use the three terms in (5) separately.
Thus even a small epsilon_E leaves the large-complement and memory
pieces. The two-time rare-return lemma does not control the former:
its two supports must have a rare union. Its smallness premise also
contains the explicitly required full/pruned distances.

For example, a new response-specific estimate

    R_E(t)+Q_E(t)+F_D(t)
       <=C_S[1+E_D(t)+A_F(t)+integral_0^t Aprobe(s)ds]   (13)

would turn (12), by 2xy<=x^2+y^2 and time Cauchy--Schwarz, into a
closed linear bound for E_D coupled to the complementary range energy.
Equation (13) is a sufficient new hypothesis, not an established bound.
A direct bound for the signed combination in (11) could be weaker and
would avoid imposing absolute estimates on each term. The weighted
source F_D is an additional requirement of this particular coordinate;
it is not claimed to be necessary for every possible response method.

## 4. What the new primal derivative/action lemma actually supplies

Put

    kappa_E=h(|E|/n)+epsilon_n^2
                        +integral_0^S mu(d_E(s))^2 ds,
    ell_j^E=integral_0^S[|q_j'(s)|^2+|r_(E,j)(s)|^2]ds.

The actual derivative lemma, its residual estimate, and the rare energy
lemma imply simultaneously for fixed E on their stated event

    (1/n)sum_(j in E) ell_j^E <= C_S kappa_E.           (14)

This uses the already proved delta_E action bound to control q_E'; it
does not differentiate any estimate with respect to initial data.
Because the zero-readout proxy has q(0)=0, time Cauchy--Schwarz gives

    |q_j(t)|^2<=S ell_j^E,
    Q_E(t)<=S<ell^E,U(t)>_n,
    integral_0^S R_E(t)dt
                    <=<ell^E,sup_(t<=S)U(t)>_n.        (15)

The supremum in the last expression is coordinatewise and is taken
after conditional probe averaging; no interchange with E_xi is used.
These are actual primal-action/response-covariance pairings. The
available controls are only

    <ell^E,1>_n<=C_S kappa_E,
    <U(t),1>_n=E_D(t).

They provide no bound for their product pairing in (15). Controlling
that pairing for this particular actual probe, possibly only in the
signed or time-integrated combination in (11), is a concrete missing
estimate. It cannot be obtained by differentiating (14).

The same issue is visible in the propagator itself: (9) and time
Cauchy--Schwarz only yield the coordinate bound

    |Phi_(E,j)(t,s)|
       <=[D_j(t)/D_j(s)] exp(sqrt(S ell_j^E)).          (16)

Equation (14) controls the mean of ell, not this exponential multiplier
acting on the actual response source. Moreover D^{-1}=1+z^2, so (2)
alone does not supply F_D: it lacks the joint factor
(1+z_j^2)^2 F_j^2. The additive f_tilde part is now controlled by
the exact structural cancellation in
ACTUAL_WEIGHTED_ADDITIVE_PROBE_SOURCE.md; this remaining issue
concerns only the response-dependent Gcal R a and Gcal w_a terms.
These are failures of the proposed inference from the available
estimates, not counterexamples for the canonical Gaussian flow.

## 5. Moving exceptional supports and scope

The state-space range projector already moves in time, and all of its
derivative terms are retained through Gcal, Hcal, and N in (1). By
contrast, this note does not differentiate a time-dependent coordinate
support E_R(t). For any one frozen set selected from that path, (7)--(16)
apply on the simultaneous primal events. Substituting E_R(t) into the
differentiated energy (11) would require treating changes of membership;
for a hard support this cannot be done by declaring P_E'=0. A causal
argument using (10), or a smooth localization with its derivative terms,
would need a separate proof.

The advance is the explicit actual range cancellation (8), signed
identity (11), and response/action reduction (15), with every off-block
and memory term retained. The own-site scalar amplification is removed.
The presently surviving resolver is the actual action–response pairing
and weighted return/source in (11)--(15), with the full/pruned distances
still unresolved. No inverse-middle metric identity, favorable sign of
the top feedback, or full global closure is asserted.
