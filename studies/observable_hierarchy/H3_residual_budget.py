"""Bounded deterministic residual-route preflight; never advances a trajectory.

Precommit: time N=1 initializations at GH orders 5,7,9; inspect raw/ridge/source
conditioning and actual storage. At GH5 only append exact initialized tanh
queries at the two reference inputs, then a bounded synthetic readout's two
reverse queries. These are static finite programs, not time steps. Compare
N=1 compressed and canonical initial readout velocities as an uncertified
diagnostic. Exact analytic pilot integrals are the independent control.

Pass for *producer feasibility only*: all requested static programs finish
inside 85 CPU seconds and 2 GiB address space; report dimensions/cost. Failure
or floating range/Schur rejection is witness-local. No GH difference is an
accuracy certificate. No trajectory follows automatically. Output is a fresh
H3_residual_preflight_* directory. The 90 core-second allocation includes this
script; RLIMIT_CPU=85 leaves setup/report allowance.
"""
from __future__ import annotations

import datetime
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (85, 85))
resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))

import numpy as np
import H2_prototype_v3 as core

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "data/generated/observable_hierarchy" / (
    "H3_residual_preflight_" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    + "_" + str(os.getpid())
)
RUN.mkdir(parents=True, exist_ok=False)
START_WALL, START_CPU = time.perf_counter(), time.process_time()
RESULT = {
    "design": __doc__, "no_trajectory": True,
    "environment": {"python": sys.version, "numpy": np.__version__,
                    "platform": platform.platform(),
                    "thread_env": {k: os.environ.get(k) for k in
                                   ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}},
    "sources": {}, "initializations": [], "static_extensions": [],
}
for relative in ("studies/observable_hierarchy/H3_residual_budget.py",
                 "studies/observable_hierarchy/H2_prototype_v3.py",
                 "studies/observable_hierarchy/H2_proposed_section_v3.md",
                 "studies/observable_hierarchy/H3_contract.md"):
    RESULT["sources"][relative] = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def persist():
    RESULT["total_cpu_seconds"] = time.process_time() - START_CPU
    RESULT["total_wall_seconds"] = time.perf_counter() - START_WALL
    RESULT["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (RUN / "results.json").write_text(json.dumps(RESULT, indent=2, sort_keys=True) + "\n")


def description(state, program):
    arrays = [state.first.b, state.first.g, state.first.w, state.first.probabilities,
              state.second.b, state.second.c, state.second.probabilities, state.M, state.D]
    answer = {"state_array_bytes": sum(x.nbytes for x in arrays),
              "feature_dimensions": [state.first.b.shape[1], state.second.b.shape[1]],
              "carriers": [], "ridge": []}
    for pop in (1, 2):
        c = program.carriers[pop]
        sv = np.linalg.svd(c.factor, compute_uv=False)
        answer["carriers"].append({"population": pop, "gaussian_dimension": c.nodes.shape[1],
             "nodes": len(c.weights), "named_sources": len(c.sources),
             "factor_singular_values": sv.tolist(),
             "source_covariance_condition": float((sv[0] / sv[-1])**2) if len(sv) else None,
             "carrier_array_bytes": sum(x.nbytes for x in (c.factor,c.nodes,c.weights,c.gaussian))})
        gram = np.array(state.metadata[f"gram{pop}"])
        eigen = np.linalg.eigvalsh(gram + state.metadata["ridge"] * np.eye(len(gram)))
        answer["ridge"].append({"population":pop, "eigenvalues":eigen.tolist(),
                                "condition":float(eigen[-1]/eigen[0])})
    answer["D_norm"] = float(np.linalg.norm(state.D,2))
    answer["negative_schur_corrections"] = [d["negative_schur_roundoff_correction"] for d in program.diagnostics]
    return answer


for gh in (5, 7, 9):
    event = {"GH_order": gh, "hierarchy_order":1}
    sw, sc = time.perf_counter(), time.process_time()
    try:
        state, program = core.initialize(1, core.QuadratureLimits(order=gh, max_nodes=100000,
             max_innovation_dimension=7, max_named_sources=32))
        event.update(status="ok", **description(state,program))
        pilot = core.pilot_words()
        v = program.expectation(core.multiply(pilot["h1"],pilot["h1"]))
        event["pilot_sin_variance_error"] = v - (1-np.exp(-2))/2
    except (ValueError, MemoryError, FloatingPointError) as exc:
        event.update(status="failed", error=repr(exc))
    event["cpu_seconds"],event["wall_seconds"] = time.process_time()-sc,time.perf_counter()-sw
    RESULT["initializations"].append(event)
    persist()
    del state, program

# An initialized exact-word extension, followed by a synthetic static readout.
sw,sc=time.perf_counter(),time.process_time()
event={"GH_order":5,"hierarchy_order":1}
try:
    state,program=core.initialize(1,core.QuadratureLimits(order=5,max_nodes=100000,
          max_innovation_dimension=8,max_named_sources=32))
    h=[core.unary("tanh",core.seed(k)) for k in ("g1","g2")]
    z=[core.action(v) for v in h]
    program.compile(z)
    first_words,second_words,_=core.initial_dictionary(1)
    b1=np.column_stack([program.evaluate(w) for w in first_words]) @ np.array(state.metadata["normalization1"]).T
    b2=np.column_stack([program.evaluate(w) for w in second_words]) @ np.array(state.metadata["normalization2"]).T
    p1,p2=(program.carriers[k].weights for k in (1,2))
    hvalues=np.column_stack([program.evaluate(w) for w in h])
    truez=np.column_stack([program.evaluate(w) for w in z])
    compressedz=b2 @ state.D @ (b1.T @ (p1[:,None]*hvalues))
    canonical_cprime=np.tanh(truez[:,0])-np.tanh(truez[:,1])
    compressed_cprime=np.tanh(compressedz[:,0])-np.tanh(compressedz[:,1])
    event["initial_readout_velocity_defect_diagnostic"] = float(np.sqrt(p2 @ ((canonical_cprime-compressed_cprime)**2)))
    event["canonical_initial_velocity_norm_diagnostic"] = float(np.sqrt(p2 @ canonical_cprime**2))
    event["forward_extension_dimensions"] = [program.carriers[k].nodes.shape[1] for k in (1,2)]
    readout=core.scale(Fraction(1,100),core.add(core.unary("tanh",z[0]),core.scale(-1,core.unary("tanh",z[1]))))
    reverse=[]
    for item in z:
        upperh=core.unary("tanh",item)
        gate=core.add(core.constant(2),core.scale(-1,core.multiply(upperh,upperh)))
        reverse.append(core.action(core.multiply(readout,gate)))
    program.compile(reverse)
    event["reverse_extension_dimensions"]=[program.carriers[k].nodes.shape[1] for k in (1,2)]
    event["reverse_extension_nodes"]=[len(program.carriers[k].weights) for k in (1,2)]
    event["soft_tail_diagnostics"]=[]
    for item in reverse:
        q=program.evaluate(item)
        weights=program.carriers[1].weights
        event["soft_tail_diagnostics"].append({str(k):float(np.sqrt(weights @ np.maximum(np.abs(q)-k,0)**2)) for k in (.01,.1,1)})
    event["new_source_diagnostics"]=program.diagnostics
    event["status"]="ok"
except (ValueError,MemoryError,FloatingPointError) as exc:
    event.update(status="failed",error=repr(exc))
event["cpu_seconds"],event["wall_seconds"]=time.process_time()-sc,time.perf_counter()-sw
RESULT["static_extensions"].append(event)
RESULT["tensor_counts"]=[{"dimension":d,"one_dimensional_order":q,"nodes":q**d,
   "one_value_plus_gradient_8_names_bytes":8*9*q**d} for d in (4,5,6,7,8) for q in (5,7,9,11,15,21)]
RESULT["Bernstein_coefficients"]=[{"mark_dimension":d,"degree":m,"coefficients_per_component":(m+1)**d}
 for d in (2,4,8) for m in (5,10,20,50)]
persist()
print(json.dumps({"run":str(RUN),"cpu_seconds":RESULT["total_cpu_seconds"],
                  "wall_seconds":RESULT["total_wall_seconds"],"peak_rss_kib":RESULT["peak_rss_kib"],
                  "initializations":RESULT["initializations"],"extensions":RESULT["static_extensions"]},indent=2))
