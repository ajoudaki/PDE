"""Retain and check the symbolic kernel-jet example in a fresh output folder."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

import mfp_expr as ex
from symbolic_kernel_jets import compile_example


def quadratic_specialization(dag):
    """Evaluate generic activation atoms at phi(z)=z**2, after compilation."""
    def replace_phi(node):
        if node.op in ("const", "symbol"):
            return node
        values = [replace_phi(x) for x in node.args]
        if node.op == "phi":
            return (values[0]**2 if node.value == 0 else
                    2*values[0] if node.value == 1 else
                    ex.const(2) if node.value == 2 else ex.const(0))
        if node.op == "pow":
            return values[0]**node.value
        if node.op == "add":
            return sum(values, ex.const(0))
        result = ex.const(1)
        for value in values:
            result = result*value
        return result
    def no_integrals_left(expression):
        raise AssertionError("Polynomial specialization retained an integral")
    evaluated = {}
    for atom in dag.expectations:
        integrand = ex.substitute(replace_phi(atom.integrand), evaluated)
        covariance = {(a,b):ex.substitute(atom.covariance[i][j], evaluated)
                      for i,a in enumerate(atom.coordinates)
                      for j,b in enumerate(atom.coordinates)}
        evaluated[atom.symbol] = ex.gaussian_expectation(
            integrand, atom.coordinates, covariance, no_integrals_left)
    return ex.expand(ex.substitute(dag.output, evaluated))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    parameters = [ex.symbol("s_"+s) for s in ("alpha", "beta", "gamma", "y1", "y2")]
    alpha, beta, gamma, y1, y2 = parameters
    q11, q12, q22 = alpha**2, alpha*beta, beta**2+gamma**2
    manifest = dict(started_utc=datetime.now(timezone.utc).isoformat(),
                    command=[sys.executable, *sys.argv], cwd=os.getcwd(),
                    python=sys.version, platform=platform.platform(), results={})
    all_dags = {}
    for activation in ("symbolic", "identity", "quadratic"):
        start = time.monotonic()
        dags = compile_example(activation)
        all_dags[activation] = dags
        text = "\n\n".join(f"jet_{r} = lim E[d^{r}K_12(0)/dt^{r}]/{r}!\n"+dag.formula()
                             for r, dag in enumerate(dags))+"\n"
        (args.out/(activation+".txt")).write_text(text)
        encoded = {f"jet_{r}": dag.to_dict() for r, dag in enumerate(dags)}
        (args.out/(activation+".json")).write_text(json.dumps(encoded, indent=2)+"\n")
        assert json.loads(json.dumps(encoded)) == encoded
        assert dags[1].output == ex.const(0)
        # All retained Gaussian moment definitions must be label-independent.
        for dag in dags:
            for atom in dag.expectations:
                assert not ({y1, y2} & ex.symbols(atom.integrand))
                assert not any({y1, y2} & ex.symbols(c) for row in atom.covariance for c in row)
        second = dags[2].output
        zero = {y1: ex.const(0), y2: ex.const(0)}
        c11 = ex.substitute(ex.diff(ex.diff(second, y1), y1)/2, zero)
        c12 = ex.substitute(ex.diff(ex.diff(second, y1), y2), zero)
        c22 = ex.substitute(ex.diff(ex.diff(second, y2), y2)/2, zero)
        assert ex.expand(second-c11*y1**2-c12*y1*y2-c22*y2**2) == ex.const(0)
        (args.out/(activation+"_label_coefficients.txt")).write_text(
            "jet_2 = C11*y1^2 + C12*y1*y2 + C22*y2^2\n"+
            "\n".join(name+" = "+ex.render(c) for name,c in
                       (("C11",c11),("C12",c12),("C22",c22)))+"\n")
        checks = ["valid JSON", "first jet zero", "second jet homogeneous quadratic in labels"]
        if activation == "identity":
            assert dags[0].output == q12
            expected = ex.const(9)/4*(q11*y1+q12*y2)*(q12*y1+q22*y2)
            assert ex.expand(second-expected) == ex.const(0)
            checks.append("independent linear Gaussian oracle: jet2=(9/4)*(Qy)1*(Qy)2")
        if activation == "quadratic":
            expected = 9*q11**2*q22**2+2*(q11*q22+2*q12**2)**2
            assert ex.expand(dags[0].output-expected) == ex.const(0)
            checks.append("quadratic initial kernel checked by two applications of Gaussian fourth moment")
            s = q11*q22
            A = 5815*s**2+11746*s*q12**2+16702*q12**4
            B = (4542*s**4+14636*s**3*q12**2+30788*s**2*q12**4
                 +13856*s*q12**6+4704*q12**8)
            expected = A*(q11**4*y1**2+q22**4*y2**2)+B*y1*y2
            assert ex.expand(second-expected) == ex.const(0)
            checks.append("reported compact quadratic-activation formula equals expanded output")
            for generic, polynomial in zip(all_dags["symbolic"], dags):
                assert ex.expand(quadratic_specialization(generic)-polynomial.output) == ex.const(0)
            checks.append("generic Gaussian DAG specialized after compilation agrees with direct polynomial compilation")
        result = dict(seconds=time.monotonic()-start, expectations=[len(d.expectations) for d in dags],
                      checks=checks)
        manifest["results"][activation] = result
        print(activation+": "+json.dumps(result), flush=True)
    study = Path(__file__).resolve().parent
    manifest["source_sha256"] = {name:hashlib.sha256((study/name).read_bytes()).hexdigest()
        for name in ("symbolic_kernel_jets.py", "run_symbolic_kernel_jets.py",
                     "mfp_compiler.py", "mfp_expr.py", "master_proof.md")}
    manifest["output_sha256"] = {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in args.out.iterdir() if p.is_file()}
    (args.out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")


if __name__ == "__main__":
    main()
