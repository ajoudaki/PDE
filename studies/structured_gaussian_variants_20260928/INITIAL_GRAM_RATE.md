# Gaussian block initialization: weak bias and effective sampling size

28 September 2026. This is a self-contained initialization result. It does
not assert a trained replacement theorem. The parent derived it from the
Gaussian covariance recursion, independently of the scoped proof routes.

## Statement

Fix L hidden tanh layers and p normalized inputs u_a=x_a/sqrt(d), including
any finite list of passive inputs. Initialize the first weights with independent
standard Gaussian rows. Each subsequent layer consists of aligned independent
k by k Gaussian blocks of variance 1/k, independently across layers. There
are B blocks and n=Bk neurons per layer. Define the final feature Gram

    Qhat_L,ab = (1/n) sum_i h_L,i(u_a) h_L,i(u_b).

Let Q_0,ab=<u_a,u_b> and define Q_l=F(Q_{l-1}), where

    F(Q)_ab = E[tanh(Z_a)tanh(Z_b)], Z~N(0,Q).

Then constants C_L,p independent of B,k satisfy

    ||E Qhat_L-Q_L||_F <= C_L,p/k,
    E ||Qhat_L-E Qhat_L||_F^2 <= C_L,p/(Bk),
    (E ||Qhat_L-Q_L||_F^2)^(1/2)
        <= C_L,p [1/k + 1/sqrt(Bk)].

For L=1 the bias is zero. The constants are uniform over all normalized
input lists, including singular input Grams. This does not assert a uniform
spectral gap over such lists. On a fixed list with a positive limiting Gram
gap, the displayed estimates quantify its finite-width preservation.

## Smoothness of the covariance map

For a smooth bounded function psi with bounded derivatives through order four,
and a positive definite covariance Q, Gaussian density differentiation and
two integrations by parts give

    DF_psi(Q)[H] = (1/2) sum_ij H_ij E partial_ij psi(Z),
    D^2F_psi(Q)[H,H] = (1/4) sum_ijkl H_ij H_kl
                                      E partial_ijkl psi(Z).

The density derivatives are integrable; bounded derivatives of psi make
the integrations by parts legitimate by inserting large compact cutoffs
and letting their radius grow. Alternatively the density identity follows
by differentiating its Gaussian Fourier transform. The formulas extend
along segments of positive semidefinite covariances: replace every covariance
by Q+epsilon I, use the formulas there, and pass to zero epsilon using
bounded derivatives and convergence of Gaussian vectors. No inverse Gram
bound enters the derivative estimates.

Apply these formulas to psi_ab(z)=tanh(z_a)tanh(z_b), with repeated indices
allowed. All derivatives through order four are bounded. Hence finite
constants A_p,D_p exist such that, for positive semidefinite Q,R,

    ||F(Q)-F(R)||_F <= A_p ||Q-R||_F,
    ||F(Q)-F(R)-DF(R)[Q-R]||_F
                                  <= D_p ||Q-R||_F^2.

DF(R) here is the continuous derivative formula from regularized covariance
matrices; the Taylor statement only uses admissible covariance segments.

## Block recursion

Let V_l,b be the empirical p by p activation Gram inside block b, divided
by k. Conditional on the preceding layer, the k new preactivation rows in
that block are independent N(0,V_{l-1,b}) vectors. Therefore

    E[V_l,b | preceding layer] = F(V_{l-1,b}),
    E[||V_l,b-F(V_{l-1,b})||_F^2 | preceding layer] <= p^2/k.

For layer one the same assertions hold with deterministic covariance Q_0.
The second assertion follows entry by entry: each empirical product is an
average of k conditionally independent variables bounded by one in absolute
value. This conditional independence uses a fresh layer initializer; it is
not an assertion about neuron independence after training.

Put e_l=E||V_l,b-Q_l||_F^2 and b_l=||E V_l,b-Q_l||_F. Conditional centering
eliminates the cross term in the squared norm, giving

    e_1 <= p^2/k,
    e_l <= p^2/k + A_p^2 e_{l-1}.

Thus e_l<=c_l/k for c_1=p^2 and c_l=p^2+A_p^2 c_{l-1}.
For the weak error, Taylor's formula at deterministic Q_{l-1} gives

    b_1=0,
    b_l <= A_p b_{l-1} + D_p e_{l-1}.

Hence b_l<=d_l/k for d_1=0 and d_l=A_p d_{l-1}+D_p c_{l-1}.

The blocks are independent at initialization, and
Qhat_L=(1/B) sum_b V_L,b. It follows exactly that

    E||Qhat_L-E Qhat_L||_F^2
       = (1/B) E||V_L,1-E V_L,1||_F^2 <= c_L/(Bk).

Adding the squared bias proves the statement. In particular, independent
blocks do not force an initialization error 1/sqrt(B): each block Gram
already has variance O(1/k), so the fluctuation is O(1/sqrt(n)).

## Passive-test and probability versions

For any probability measure mu supported on normalized inputs, append a
single test x to the m training inputs. The constants above depend on m+1
and L, not on x. Integrating the squared row estimate with respect to mu
is justified by boundedness and Tonelli's theorem. Thus the initial
train/test kernel row has the same L2(mu), mean-square rate.

For any delta in (0,1), Markov's inequality on these squared norms gives
simultaneously, after adjusting constants and allocating failure probability,
training and integrated test-row errors at most

    C_L,m [1/k + 1/sqrt(n delta)]

with probability at least 1-delta. The training kernel is Qhat_L/m, so a
limiting gap lambda>0 persists at level lambda/2 once this error is small
enough. Fixed test-distribution constants are not worst-case suprema over
all inputs; the claimed norm is L2(mu).

## What survives during training

This proof depends on fresh independent Gaussian rows conditional on the
previous layer. After training, h and delta depend on the same matrices
used in both orientations. Neither conditional iid rows nor the covariance
recursion above describes that situation. The correct trained target
requires response/reuse terms in addition to covariance.

The initialization result can be combined with a separately proved
small-label all-time O(Y^3) comparison to frozen readout-kernel training.
That yields a bound of the form

    C Y [1/k + 1/sqrt(n delta) + Y^2]

for canonical block-trained versus canonical dense-population predictions,
on the appropriate norm/gap events. It does not yield arbitrary accuracy
at one fixed nonzero Y. The Y^3 term cannot be removed by increasing B or k.
This last display is a consequence only after the named deterministic
training comparison is proved, not part of the initialization proof above.
