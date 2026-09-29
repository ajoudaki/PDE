# Exact model for the low-order mechanism investigation

Fix m training pairs (x_a,y_a), hidden depth L>=2, common width n. The
activation is applied coordinatewise; initially take smooth tanh. Set

    z_a^1=W1 x_a/sqrt(d), h_a^ell=phi(z_a^ell),
    z_a^ell=W_ell h_a^(ell-1), f_a=w^T h_a^L/n,
    r_a=f_a-y_a, rho=sqrt(sum_a r_a^2/m).

Backwards (excluding residual):

    delta_a^L=w * phi'(z_a^L),
    delta_a^ell=phi'(z_a^ell) * W_(ell+1)^T delta_a^(ell+1).

All displayed fields use the closure's reconstructed current weights.
The stored outer weights obey

    dot W1=-(2/m)sum_a r_a delta_a^1 x_a^T/sqrt(d),
    dot w=-(2/m)sum_a r_a h_a^L.

For each hidden link ell=2,...,L and sample a there are q forward moments
B_(ell,a,k) and q backward moments C_(ell,a,k), vectors of length n,
k=0,...,q-1. Their equations are

    dot tau=rho, tau(0)=1,
    dot B_k=rho h_a^(ell-1)
            -(rho/tau)[k B_k+sum_(j<k)(2j+1)B_j],
    dot C_k=r_a delta_a^ell
            -(rho/tau)[k C_k+sum_(j<k)(2j+1)C_j],
    W_ell=W0_ell-(2/(mn tau))sum_(a,k)(2k+1) C_k B_k^T.

Initially B_0=h_a^(ell-1)(0); B_k=0 for k>0; all C_k=0; w=0.
The physical network starts from first-layer iid N(0,1), hidden W0 entries
iid N(0,1/n), independent between layers. W0 and its transpose are reused
exactly; they are fixed operators, not independent fresh noise on each call.

For interpreting the moments, on [0,tau(t)] let h(xi) equal h(0) on [0,1]
and the actual forward response at activity xi thereafter. Let
b(xi)=(r_a/rho)delta_a^ell on the activity portion, and b=0 on [0,1].
Then B_k=integral h(xi) p_k(xi/tau) dxi and C_k=integral b(xi)
p_k(xi/tau) dxi, where p_k are shifted Legendre polynomials with p_k(1)=1.
This is an interpretation and exact integral solution of the linear moment
equations for the closure's own histories; no dense reference is supplied.

At rho=0 all raw velocities vanish; the algorithm never divides by rho.
Reparametrization is only used on intervals where rho>0.

Two common analytic facts may be derived directly:

1. An empirical neuron inner product is u^T v/n. A population version, if
defined, replaces it by E[UV]. That replacement alone does not prove a
width limit or independence of the coordinates after training.
2. The canonical physical middle update for comparison of velocities is
   dot W_ell=-(2/(mn))sum_a r_a delta_a^ell h_a^(ell-1)^T.
The closure need not follow this equation: its middle velocity is obtained
by differentiating its moment reconstruction.
