"""Compatibility checks for the ``pde`` to ``dtdl`` package rename."""

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[2]
CODE = ROOT / "code"


class PackageCompatibilityTests(unittest.TestCase):
    def run_python(self, source, *arguments):
        environment = dict(
            os.environ,
            PYTHONPATH=str(CODE),
            PYTHONDONTWRITEBYTECODE="1",
            OPENBLAS_NUM_THREADS="1",
        )
        return subprocess.run(
            [sys.executable, "-B", *arguments, "-c", textwrap.dedent(source)],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        )

    def test_root_imports_keep_optional_heavy_dependencies_unloaded(self):
        self.run_python("""
            import sys
            import dtdl
            import pde

            forbidden = ("torch", "torchvision", "matplotlib")
            assert not any(
                name == prefix or name.startswith(prefix + ".")
                for name in sys.modules for prefix in forbidden
            )
        """)

    def test_numpy_submodule_identity_and_seeded_result_in_both_import_orders(self):
        program = """
            import importlib
            import numpy as np
            import sys

            first = importlib.import_module("{first}.finite_network")
            second = importlib.import_module("{second}.finite_network")
            assert first is second
            assert sys.modules["pde.finite_network"] is sys.modules["dtdl.finite_network"]
            assert first.Parameters is second.Parameters
            assert first.initialize is second.initialize
            parameters = first.initialize(3, 2, 2, seed=17)
            inputs = np.array([[1.0, -0.5], [0.25, 2.0]])
            np.testing.assert_array_equal(
                first.forward(parameters, inputs).output,
                second.forward(parameters, inputs).output,
            )
        """
        for first, second in (("pde", "dtdl"), ("dtdl", "pde")):
            with self.subTest(first=first):
                self.run_python(program.format(first=first, second=second))

    @unittest.skipUnless(importlib.util.find_spec("torch"), "PyTorch is not installed")
    def test_torch_backed_submodule_and_public_class_are_shared(self):
        self.run_python("""
            import dtdl.compression as canonical
            import pde.compression as compatibility

            assert compatibility is canonical
            assert compatibility.Dense is canonical.Dense
        """)

    def test_radial_explorer_module_help_is_equivalent(self):
        environment = dict(
            os.environ,
            PYTHONPATH=str(CODE),
            PYTHONDONTWRITEBYTECODE="1",
            OPENBLAS_NUM_THREADS="1",
        )

        def help_text(package):
            completed = subprocess.run(
                [sys.executable, "-B", "-m", f"{package}.radial_explorer", "--help"],
                cwd=ROOT,
                env=environment,
                capture_output=True,
                text=True,
                timeout=30,
                check=True,
            )
            return (completed.stdout + completed.stderr).replace(
                f"{package}.radial_explorer", "PACKAGE.radial_explorer"
            )

        self.assertEqual(help_text("pde"), help_text("dtdl"))


if __name__ == "__main__":
    unittest.main()
