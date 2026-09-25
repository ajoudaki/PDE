"""Small CPU verification; run with python -B check_compact_flow.py."""
import torch

from compact_flow import Flow
from activation_moment_engine import ActivationDenseEngine, ActivationMomentEngine


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

    # Same initialization and evolving physical/moment coordinates as the
    # established three-layer implementation, with three simultaneous steps.
    for activation in ('relu', 'gelu', 'selu'):
        for order in (None, 1, 2, 3):
            new = make(3, activation, order)
            arguments = (2, 7, inputs, labels) if order is None else (2, 7, order, inputs, labels)
            kind = ActivationDenseEngine if order is None else ActivationMomentEngine
            old = kind(*arguments, activation=activation, seed=773, device='cpu', dtype=torch.float64)
            state = old.initial_state()
            assert len(new.state) == len(state.tensors())
            for index in range(4):
                for actual, expected in zip(new.state, state.tensors()):
                    assert actual.dtype == torch.float64 and actual.device.type == 'cpu'
                    close(actual, expected)
                close(new.predict(inputs), old.predict(state, inputs))
                before = [value.clone() for value in new.state]
                velocity, reference = new.rhs(), old.rhs(state)
                for actual, expected in zip(velocity, reference.tensors()):
                    close(actual, expected)
                for actual, expected in zip(new.state, before):
                    close(actual, expected)
                if index < 3:
                    new.step(.0003)
                    state = state.add_scaled(reference, .0003)

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
    print(f'PASS: {checks} CPU assertions; max absolute discrepancy {maximum:.3g}')


if __name__ == '__main__':
    main()
