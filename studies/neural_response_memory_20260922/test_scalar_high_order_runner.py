"""End-to-end deterministic event/replay test with an exactly solvable flow."""
import argparse
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

import run_scalar_high_order as runner


class RunnerTest(unittest.TestCase):
    def test_exact_linear_flow_event_and_passive_replay(self):
        scratch=runner.DATA/"scalar_high_order_runner_tests"
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as temporary:
            root=Path(temporary); source=root/"source"; source.mkdir()
            m,order=8,5
            labels=(-1.)**np.arange(m)
            coefficients={"T"+str(j):np.zeros((m,)*j) for j in range(1,order+1)}
            coefficients["T2"]=np.eye(m)
            np.savez_compressed(source/"coefficients.npz",**coefficients,labels=labels,inputs=np.eye(m,2))
            (source/"result.json").write_text(json.dumps(dict(status="complete")))
            target=root/"run"
            runner.integrate(argparse.Namespace(source=source,output=target,order=order,rtol=1e-9,seconds=60.))
            record=json.loads((target/"result.json").read_text())
            values=runner.read_npz(target/"trajectory.npz")
            self.assertEqual(record["status"],"fitted")
            self.assertLess(abs(record["time"]-m/4*np.log(1e6)),2e-5)
            self.assertLess(abs(record["loss"]-1e-6),1e-12)
            self.assertGreater(record["crossing_bracket"]["left_loss"],1e-6)
            self.assertLessEqual(record["crossing_bracket"]["right_loss"],1e-6)
            np.testing.assert_allclose(values["train_f"],labels*(1-1e-3),atol=2e-10,rtol=0)
            probes=root/"probes"; probes.mkdir()
            rng=np.random.default_rng(512)
            kernel=np.vstack((rng.normal(size=(64,m)),np.eye(m)))
            passive={"T"+str(j):np.zeros((72,)+(m,)*(j-1)) for j in range(1,order+1)}
            passive["T2"]=kernel
            np.savez_compressed(probes/"coefficients.npz",**passive,labels=labels,angles=np.arange(32),
                                off_angles=np.arange(32))
            (probes/"result.json").write_text(json.dumps(dict(status="complete")))
            output=root/"readout"
            runner.replay(argparse.Namespace(source=probes,run=target,output=output,seconds=60.))
            endpoint=runner.read_npz(output/"endpoint.npz")
            np.testing.assert_allclose(endpoint["grid"],kernel[:32]@(labels*(1-1e-3)),atol=2e-9,rtol=0)
            self.assertLess(json.loads((output/"result.json").read_text())["training_probe_gap"],1e-8)


if __name__=="__main__":
    unittest.main()
