# Deterministic verification

No training experiment was run. On 2026-09-12 the coordinator copied the complete
established C.4.5.1 rational Gaussian certificate unchanged into
`verify_reference_certificate.py` and ran it from `/home/amir/Codes/PDE`:

    python studies/nonlinear_prediction_selection/verify_reference_certificate.py > data/generated/nonlinear_prediction_selection/reference_certificate_20260912/output.txt

The fresh run exited zero. All assertions are exact rational comparisons;
its readable output was:

    [0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]

This reproduces the established numerical input bounds, including m>=1/10;
it does not validate the new nonlinear selection argument.

Environment: Python 3.10.12; standard library fractions only.
Certificate SHA-256: `07c51c139ebf66912ef7b730201dcc71581b11355dd29dbee6140bf2bba63118`.
Output SHA-256: `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900`.
Source: docs/global_nonlinear.md SHA-256
`bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05`.
