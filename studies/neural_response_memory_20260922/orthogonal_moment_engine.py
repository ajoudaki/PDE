"""Study-local moving-interval shifted-Legendre history moments.

The fixed virtual prefix has length eta=1, u=0 and h=h1(0). With L=s+1,
A_k and B_k integrate u and h against P_k(2*tau/L-1), k=0,...,P-1.
Only the fixed initialization W0 is stored densely. Learned hidden weights
are -2/(M*n*L) sum_k (2k+1) A_k B_k.T. No quadrature is used by the RHS.
"""

import torch

from moment_engine import MomentEngine as ActivityMomentEngine
from moment_engine import MomentState, factor_action


class OrthogonalMomentEngine(ActivityMomentEngine):
    """Same constructor and state algebra as the activity-bin engine.

    eta is fixed at 1 independently of bins=P. Redundant compatibility
    coordinates C_j all follow L=s+1; factors depend on s+1 directly.
    The optional dynamic h1,h2,rho lift again has a rational RHS for rho>0.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eta = 1.0
        self.degrees = torch.arange(self.P, dtype=self.dtype, device=self.device)
        self.legendre_weights = 2*self.degrees+1
        self.initial.B = torch.zeros_like(self.initial.B)
        self.initial.B[0] = self.h10
        self.initial.C = torch.ones_like(self.initial.C)
        self._constant_tensors = (self.inputs, self.labels, self.W0, self.centers,
                                  self.h10, self.q0, self.degrees, self.legendre_weights,
                                  *self.initial.tensors())
        self._constant_versions = tuple((id(x), x._version) for x in self._constant_tensors)

    def _factors(self, state):
        weighted_a = self.legendre_weights[:, None, None]*state.A
        return (-2/(self.M*self.n))*self._columns(weighted_a), self._columns(state.B/(state.s+self.eta))

    def _training_fields(self, state):
        if self.lifted:
            h1, h2 = state.h1, state.h2
        else:
            h1 = torch.tanh(state.w @ self.inputs.T)
            h2 = torch.tanh(self._apply_hidden(state, h1))
        f = state.c @ h2/self.n
        r = f-self.labels
        loss = r.square().mean()
        rho = state.rho if self.lifted else torch.sqrt(loss)
        delta2 = state.c[:, None]*(1-h2.square())
        delta1 = self._apply_hidden(state, delta2, transpose=True)*(1-h1.square())
        return dict(h1=h1, h2=h2, f=f, r=r, rho=rho, loss=loss,
                    delta1=delta1, delta2=delta2, L=state.s+self.eta)

    def transport_moments(self, moments, endpoint_source, rho, length):
        """Differentiate integral_0^L q(tau)*ell_k(tau/L) dtau.

        endpoint_source=rho*q(L), with Ldot=rho. The prefix sum is the
        exact identity x*ell_k'(x)=k*ell_k(x)+sum_{j<k}(2j+1)*ell_j(x).
        """
        weighted = self.legendre_weights[:, None, None]*moments
        lower = torch.cat((torch.zeros_like(weighted[:1]), torch.cumsum(weighted[:-1], dim=0)), dim=0)
        return endpoint_source[None]-(rho/length)*(self.degrees[:, None, None]*moments+lower)

    def _derivative_factors(self, state, velocity):
        length = state.s+self.eta
        weighted = self.legendre_weights[:, None, None]
        left = (-2/(self.M*self.n))*torch.cat((self._columns(weighted*velocity.A),
                                             self._columns(weighted*state.A)), dim=1)
        right = torch.cat((self._columns(state.B/length),
                           self._columns((velocity.B-state.B*velocity.s/length)/length)), dim=1)
        return left, right

    @torch.no_grad()
    def rhs(self, state):
        self.validate_state(state)
        fields = self._training_fields(state)
        if bool(fields["rho"] == 0):
            return MomentState(**{name: torch.zeros_like(value)
                                  for name, value in zip(state.names(), state.tensors())})
        r, rho, h1, h2, length = (fields[name] for name in ("r", "rho", "h1", "h2", "L"))
        velocity = MomentState(
            (-2/self.M)*(fields["delta1"]*r) @ self.inputs,
            (-2/self.M)*(h2 @ r),
            self.transport_moments(state.A, fields["delta2"]*r, rho, length),
            self.transport_moments(state.B, rho*h1, rho, length),
            rho.expand_as(state.C).clone(), rho.clone(),
        )
        if self.lifted:
            velocity.h1 = (1-h1.square())*(velocity.w @ self.inputs.T)
            z2dot = self._apply_hidden(state, velocity.h1)
            z2dot += factor_action(*self._derivative_factors(state, velocity), h1)
            velocity.h2 = (1-h2.square())*z2dot
            fdot = (velocity.c @ h2+state.c @ velocity.h2)/self.n
            velocity.rho = (r*fdot).mean()/rho
        return velocity

    def endpoint_projections(self, state):
        """Legendre reconstructions u_P(L), h_P(L), each shape (n,M)."""
        self.validate_state(state)
        weights = self.legendre_weights[:, None, None]/(state.s+self.eta)
        return (weights*state.A).sum(dim=0), (weights*state.B).sum(dim=0)

    def defect_factors(self, state):
        """E=DeltaWdot+(2/(Mn))*(delta2*r)@h1.T, with rank at most M.

        E=(2*rho/(Mn))*(u-u_P)@(h1-h_P).T. Its positive sign is the
        product-rule remainder for the orthogonal projection kernel.
        """
        self.validate_state(state)
        fields = self._training_fields(state)
        if bool(fields["rho"] == 0):
            return state.w.new_zeros((self.n, 0)), state.w.new_zeros((self.n, 0))
        u_projection, h_projection = self.endpoint_projections(state)
        u = fields["delta2"]*fields["r"]/fields["rho"]
        return (2*fields["rho"]/(self.M*self.n))*(u-u_projection), fields["h1"]-h_projection

    def moment_diagnostics(self, state):
        """Endpoint projection residuals and redundant C=L invariant drift."""
        fields = self.fields(state)
        u_projection, h_projection = self.endpoint_projections(state)
        u = (fields["delta2"]*fields["r"]/fields["rho"]
             if bool(fields["rho"] > 0) else torch.zeros_like(fields["delta2"]))
        return dict(u_projection=u_projection, h_projection=h_projection,
                    u_error=u-u_projection, h_error=fields["h1"]-h_projection,
                    C_minus_L=state.C-fields["L"])


# Drop-in module selection for runners that import ``MomentEngine``.
MomentEngine = OrthogonalMomentEngine
