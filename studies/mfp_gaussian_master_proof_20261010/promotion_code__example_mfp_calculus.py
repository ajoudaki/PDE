"""Reproduce small symbolic MFP calculations; no sampling or quadrature."""
import argparse
import json

from pde.mfp_compiler import Program


def reuse():
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    W = p.matrix("W", lower, upper)
    z = W @ p.one(lower)
    v = W.T @ p.phi(z)
    return p.compile(p.inner(v, v), preactivations=[z])


def cubic_reuse():
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    W = p.matrix("W", lower, upper)
    z = W @ p.one(lower)
    v = W.T @ (z ** 3)
    return p.compile(p.inner(v, v))


def moving_flow(moving=True):
    p = Program()
    neurons = p.vector_type("neurons")
    x = p.root("x", neurons)
    loss = p.mean(x ** 4) / 4
    gradient = p.gradient(loss, vectors=[x])
    derivatives = p.derivatives(p.mean(x ** 2), {x: -gradient[x]}, 2, moving=moving)
    return p.compile(derivatives[2])


def nonlinear_moving_flow():
    p = Program()
    neurons = p.vector_type("neurons")
    x = p.root("x", neurons)
    gradient = p.gradient(p.mean(p.phi(x)), vectors=[x])
    derivative = p.derivatives(p.mean(x ** 2), {x: -gradient[x]}, 2, moving=True)[2]
    return p.compile(derivative, preactivations=[x])


def singular_queries():
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    W = p.matrix("W", lower, upper)
    one = p.one(lower)
    z1, z2 = W @ one, W @ one
    v = W.T @ p.phi(z1 + z2)
    return p.compile(p.inner(v, v))


def rank_update():
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    W = p.matrix("W", lower, upper)
    x, u = p.root("x", lower), p.root("u", upper)
    A = W + p.rank_one(u, x, coefficient=2)
    y = A @ x
    return p.compile(p.inner(y, y))


def gradient_update():
    """One ambient step, tested on its saved pre-update loss derivative."""
    p = Program()
    lower, upper = p.vector_type("lower"), p.vector_type("upper")
    W = p.matrix("W", lower, upper)
    eta = p.parameter("eta")
    z = W @ p.one(lower)
    saved_derivative = z**3
    loss = p.mean(z**4)/4
    state = p.gradient_descent(loss, matrices=[W], step_size=eta)
    reverse = state[W].T @ saved_derivative
    return p.compile(p.inner(reverse, reverse))


EXAMPLES = dict(reuse=reuse, cubic_reuse=cubic_reuse,
                moving_flow=moving_flow, frozen_direction=lambda: moving_flow(False),
                nonlinear_moving_flow=nonlinear_moving_flow,
                singular_queries=singular_queries, rank_update=rank_update,
                gradient_update=gradient_update)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--example", choices=["all", *EXAMPLES], default="all")
    parser.add_argument("--json", action="store_true", help="include covariance tables and transformation traces")
    args = parser.parse_args()
    selected = EXAMPLES if args.example == "all" else {args.example: EXAMPLES[args.example]}
    results = {name: build() for name, build in selected.items()}
    if args.json:
        print(json.dumps({name: dag.to_dict() for name, dag in results.items()}, indent=2))
    else:
        for name, dag in results.items():
            print(name + ":")
            print(dag.formula())
            print()


if __name__ == "__main__":
    main()
