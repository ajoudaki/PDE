"""Standalone CPU equation checks; run with python -B check_compact_flow.py."""
import torch

from compact_flow import Flow


def main():
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float32)
    generator = torch.Generator().manual_seed(741)
    inputs = torch.randn((8, 2), generator=generator, dtype=torch.float64)
    labels = torch.tensor([1., -1.] * 4, dtype=torch.float64)
    checks, maximum = 0, 0.

    def close(actual, expected):
        nonlocal checks, maximum
        torch.testing.assert_close(actual, expected, atol=3e-12, rtol=3e-12)
        assert bool(torch.isfinite(actual).all())
        maximum = max(maximum, float((actual - expected).abs().max()))
        checks += 1

    def make(depth, activation, order=None):
        return Flow(inputs, labels, width=7, depth=depth, activation=activation,
                    order=order, seed=773, device='cpu', dtype=torch.float64)

    custom = (lambda z: torch.tanh(z) + .05 * z,
              lambda z: 1 - torch.tanh(z).square() + .05)
    # Autograd is independent of the implementation's manual backward pass.
    for depth in (1, 2, 4):
        for activation in ('tanh', custom):
            model = make(depth, activation)
            phi = torch.tanh if activation == 'tanh' else custom[0]
            for _ in range(3):
                parameters = [value.detach().clone().requires_grad_(True) for value in model.state]
                hidden = phi(parameters[0] @ inputs.T)
                for matrix in parameters[1:-1]:
                    hidden = phi(matrix @ hidden)
                prediction = parameters[-1] @ hidden / model.n
                loss = (prediction - labels).square().mean()
                gradients = torch.autograd.grad(loss, parameters)
                close(model.predict(inputs), prediction.detach())
                mobilities = [model.n] + [1] * (depth - 1) + [model.n]
                for actual, gradient, mobility in zip(model.rhs(), gradients, mobilities):
                    close(actual, -mobility * gradient)
                model.step(.0003)

    # With no hidden-to-hidden link, moments cannot alter depth-one dynamics.
    for activation in ('relu', 'gelu', 'selu', custom):
        for order in (1, 3):
            dense, closure = make(1, activation), make(1, activation, order)
            for _ in range(3):
                close(dense.predict(inputs), closure.predict(inputs))
                d, c = dense.rhs(), closure.rhs()
                close(d[0], c[0])
                close(d[1], c[1])
                close(c[-1], (closure.predict(inputs) - labels).square().mean().sqrt())
                dense.step(.0003)
                closure.step(.0003)
    # Configured initialization must preserve the same muP gradient equations.
    # Independent PyTorch activations cover deep models and arbitrary input dimension.
    phis={'relu':torch.relu,'gelu':torch.nn.functional.gelu,
          'selu':torch.nn.functional.selu,'tanh':torch.tanh,
          'sigmoid':torch.sigmoid,'silu':torch.nn.functional.silu}
    x3=torch.randn((8,3),generator=generator,dtype=torch.float64)
    for depth in (1,4,20):
        for activation,phi in phis.items():
            model=Flow(x3,labels,width=7,depth=depth,activation=activation,
                       hidden_gain='unit_moment',readout_std=1.,seed=773,
                       device='cpu',dtype=torch.float64)
            parameters=[v.detach().clone().requires_grad_(True) for v in model.state]
            h=phi(parameters[0]@x3.T)
            for matrix in parameters[1:-1]:h=phi(matrix@h)
            pred=parameters[-1]@h/model.n
            gradients=torch.autograd.grad((pred-labels).square().mean(),parameters)
            close(model.predict(x3),pred.detach())
            for actual,g,mobility in zip(model.rhs(),gradients,[model.n]+[1]*(depth-1)+[model.n]):
                close(actual,-mobility*g)
            for order in (1,2,3):
                closure=Flow(x3,labels,width=7,depth=depth,activation=activation,
                             order=order,hidden_gain='unit_moment',readout_std=1.,seed=773,
                             device='cpu',dtype=torch.float64)
                close(closure.predict(x3),model.predict(x3))
                for _ in range(2):closure.step(.00001)
                # Reconstruct full physical matrices, then use autograd for
                # neuron responses: independent of factor actions/manual backprop.
                w=closure.w.clone().requires_grad_(True)
                c=closure.c.clone().requires_grad_(True)
                zs=[w@x3.T]; hs=[phi(zs[0])]
                for i,matrix in enumerate(closure.matrices):
                    A,B=closure.moments[2*i:2*i+2]
                    correction=sum((2*k+1)*(A[k]@B[k].T) for k in range(order))
                    W=matrix-2*correction/(closure.M*closure.n*(1+closure.s))
                    zs.append(W@hs[-1]);hs.append(phi(zs[-1]))
                pred=c@hs[-1]/closure.n
                close(closure.predict(x3),pred.detach())
                residual=pred-labels;rho=residual.square().mean().sqrt().detach()
                gw,gc=torch.autograd.grad(residual.square().mean(),(w,c),retain_graph=True)
                delta=[d.detach()*closure.n for d in torch.autograd.grad(pred.sum(),zs)]
                before=[v.clone() for v in closure.state];velocity=closure.rhs()
                close(velocity[0],-closure.n*gw);close(velocity[1],-closure.n*gc)
                close(velocity[-1],rho)
                transport=torch.tensor([[k if j==k else 2*j+1 if j<k else 0
                                         for j in range(order)] for k in range(order)],dtype=torch.float64)
                for i in range(depth-1):
                    sources=(delta[i+1]*residual.detach(),rho*hs[i].detach())
                    for j,source in enumerate(sources):
                        moment=closure.moments[2*i+j]
                        expected=source[None]-rho/(1+closure.s)*torch.einsum('pq,qnm->pnm',transport,moment)
                        close(velocity[2+2*i+j],expected)
                for actual,old in zip(closure.state,before):close(actual,old)
                closure.step(.00001)
                for actual,old,v in zip(closure.state,before,velocity):close(actual,old+.00001*v)
    print(f'PASS: {checks} CPU assertions; max absolute discrepancy {maximum:.3g}')


if __name__ == '__main__':
    main()
