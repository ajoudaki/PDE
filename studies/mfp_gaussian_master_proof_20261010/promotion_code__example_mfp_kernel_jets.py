"""Symbolic geometry, labels and final-hidden-layer kernel jets of a deep MLP.

Two hidden layers plus readout. Normalized inputs x1/sqrt(d)=(alpha,0),
x2/sqrt(d)=(beta,gamma), d=2. All parameter blocks train by negative
gradient flow for loss=sum((f-y)^2)/(2m), m=2. Vector mobility n, matrix
mobility 1. First-weight columns and stored readout are iid N(0,1);
hidden matrix entries are iid N(0,1/n), all independent initially.
"""
import argparse
import json
from pathlib import Path
import hashlib
import platform
import sys

from pde import mfp_compiler, mfp_expr

from pde.mfp_compiler import Program


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
    parser.add_argument("--activation", choices=["all", "symbolic", "identity", "quadratic"],
                        default="symbolic")
    parser.add_argument("--order", type=int, default=2)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output-dir", type=Path,
                        help="write formulas and JSON to a new, explicitly chosen directory")
    args = parser.parse_args()
    if args.order < 0:
        parser.error("--order must be nonnegative")
    if args.output_dir is not None:
        args.output_dir.mkdir(parents=True, exist_ok=False)
    activations = ("symbolic", "identity", "quadratic") if args.activation == "all" else (args.activation,)
    json_results = {}
    for activation in activations:
        dags = compile_example(activation, args.order)
        encoded = {f"jet_{r}": dag.to_dict() for r, dag in enumerate(dags)}
        formula = "\n\n".join(
            f"jet_{r} = lim E[d^{r} K_12(0)/dt^{r}] / {r}!:\n" + dag.formula()
            for r, dag in enumerate(dags)) + "\n"
        if args.output_dir is None:
            if args.json:
                json_results[activation] = encoded
            else:
                print(activation + ":\n" + formula)
        else:
            (args.output_dir / (activation + ".txt")).write_text(formula, encoding="utf-8")
            (args.output_dir / (activation + ".json")).write_text(
                json.dumps(encoded, indent=2) + "\n", encoding="utf-8")
    if args.output_dir is None and args.json:
        print(json.dumps(json_results, indent=2))
    if args.output_dir is not None:
        sources = [Path(__file__).resolve(), Path(mfp_compiler.__file__).resolve(),
                   Path(mfp_expr.__file__).resolve()]
        manifest = dict(
            command=[sys.executable, *sys.argv], python=sys.version,
            platform=platform.platform(), order=args.order, activations=list(activations),
            source_sha256={path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in sources},
            output_sha256={path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                           for path in sorted(args.output_dir.iterdir()) if path.is_file()},
        )
        (args.output_dir / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {len(activations)} activation case(s) to {args.output_dir}")


if __name__ == "__main__":
    main()
