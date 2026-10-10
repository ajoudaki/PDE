"""Symbolic geometry, labels and final-hidden-layer kernel jets of a deep MLP.

Two hidden layers plus readout. Normalized inputs x1/sqrt(d)=(alpha,0),
x2/sqrt(d)=(beta,gamma), d=2. All parameter blocks train by negative
gradient flow for loss=sum((f-y)^2)/(2m), m=2. Vector mobility n, matrix
mobility 1. First-weight columns and stored readout are iid N(0,1);
hidden matrix entries are iid N(0,1/n), all independent initially.
"""
import argparse
import json

from mfp_compiler import Program


def build_example(activation="symbolic"):
    """Return the program and named nodes; geometry/labels remain symbolic."""
    if activation not in ("symbolic", "identity", "quadratic"):
        raise ValueError("activation must be symbolic, identity, or quadratic")
    p = Program()
    layer1 = p.vector_type("layer1")
    layer2 = p.vector_type("layer2")
    parameters = {name: p.parameter(name)
                  for name in ("alpha", "beta", "gamma", "y1", "y2")}
    alpha, beta, gamma, y1, y2 = parameters.values()

    # Actual shared first-layer columns, so weight derivatives see the geometry.
    U = p.root("W1_col1", layer1)
    V = p.root("W1_col2", layer1)
    W2 = p.matrix("W2", layer1, layer2)
    W3 = p.root("W3", layer2)
    phi = p.phi if activation == "symbolic" else (
        (lambda z: z) if activation == "identity" else (lambda z: z**2))

    z1 = [alpha*U, beta*U + gamma*V]
    h1 = [phi(z) for z in z1]
    z2 = [W2 @ h for h in h1]
    h2 = [phi(z) for z in z2]
    f = [p.inner(W3, h) for h in h2]
    loss = ((f[0]-y1)**2 + (f[1]-y2)**2)/4

    grad = p.gradient(loss, vectors=[U, V, W3], matrices=[W2])
    flow = {weight: -value for weight, value in grad.items()}
    # Readout contribution to the tangent kernel, with readout mobility n.
    kernel12 = p.inner(h2[0], h2[1])
    network = dict(U=U, V=V, W2=W2, W3=W3, z1=z1, h1=h1,
                   z2=z2, h2=h2, f=f, loss=loss, kernel12=kernel12)
    return p, parameters, network, flow


def compile_example(activation="symbolic", order=2):
    p, _, network, flow = build_example(activation)
    jets = p.jets(network["kernel12"], flow, order=order, moving=True)
    # moving=True differentiates the vector field, including evolving residuals.
    return tuple(p.compile(jet, preactivations=[*network["z1"], *network["z2"]])
                 for jet in jets)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--activation", choices=["symbolic", "identity", "quadratic"],
                        default="symbolic")
    parser.add_argument("--order", type=int, default=2)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    dags = compile_example(args.activation, args.order)
    if args.json:
        print(json.dumps({f"jet_{r}": dag.to_dict() for r, dag in enumerate(dags)}, indent=2))
    else:
        for r, dag in enumerate(dags):
            print(f"jet_{r} = lim E[d^{r} K_12(0)/dt^{r}] / {r}!:")
            print(dag.formula())
            print()


if __name__ == "__main__":
    main()
