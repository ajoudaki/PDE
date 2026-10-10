"""Build a two-hidden-layer MLP, differentiate its output, and compile moments.

Scalar input x=1; no biases. W1_i,W3_i ~ N(0,1), W2_ij ~ N(0,1/n),
all independent. Stored readout W3 has order-one variance (explicitly chosen).
The output is mean(W3 * phi(W2 @ phi(W1))). No numerical width is required.
"""
import argparse
import json

from mfp_compiler import Program


def build_mlp(activation="symbolic"):
    """Return the symbolic program, network nodes, gradients and observables."""
    if activation not in ("symbolic", "identity", "cubic"):
        raise ValueError("activation must be symbolic, identity, or cubic")
    p = Program()
    layer1 = p.vector_type("layer1")
    layer2 = p.vector_type("layer2")

    # W1 is n-by-1, W2 is n-by-n, and W3 is the stored length-n readout.
    W1 = p.root("W1", layer1)
    W2 = p.matrix("W2", layer1, layer2)
    W3 = p.root("W3", layer2)
    phi = p.phi if activation == "symbolic" else (
        (lambda z: z) if activation == "identity" else (lambda z: z**3))

    z1 = W1                      # W1*x, with scalar input x=1
    h1 = phi(z1)
    z2 = W2 @ h1
    h2 = phi(z2)
    f = p.inner(W3, h2)           # W3.T h2 / n

    # Scaled vector gradients and ordinary matrix gradients, all at finite n.
    grad = p.gradient(f, vectors=[W1, W3], matrices=[W2])
    first = p.inner(grad[W1], grad[W1])  # n * ||grad_W1 f||_2^2
    full = first + p.frobenius(grad[W2], grad[W2]) + p.inner(grad[W3], grad[W3])
    observables = dict(
        mean_first_layer_derivative=p.mean(grad[W1]),
        first_layer_derivative_energy=first,
        all_parameter_metric_norm=full,
    )
    network = dict(W1=W1, W2=W2, W3=W3, z1=z1, h1=h1, z2=z2, h2=h2, f=f)
    return p, network, grad, observables


def compile_examples(activation="symbolic"):
    p, network, _, observables = build_mlp(activation)
    return {name: p.compile(value, preactivations=[network["z1"], network["z2"]])
            for name, value in observables.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activation", choices=["symbolic", "identity", "cubic"], default="symbolic")
    parser.add_argument("--json", action="store_true", help="include sources, covariance tables, and rule traces")
    args = parser.parse_args()
    results = compile_examples(args.activation)
    if args.json:
        print(json.dumps({name: dag.to_dict() for name, dag in results.items()}, indent=2))
    else:
        for name, dag in results.items():
            print(name + ":")
            print(dag.formula())
            print()


if __name__ == "__main__":
    main()
