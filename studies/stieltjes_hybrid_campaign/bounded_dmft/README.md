# Bounded-readout DMFT branch

This directory is the isolated dynamical-mean-field-theory branch of the
hybrid mean-field campaign.  It does **not** modify or supersede the older
finite-width, MFP, or tagged-site artifacts.

Current status: **derivation and calibration implementation only**.  No
positive-time DMFT curve is scientific evidence until every unlock gate in
[`PROTOCOL.md`](PROTOCOL.md) passes.

Files:

- [DERIVATION.md](DERIVATION.md): exact finite-width skeleton, the formal
  two-species cavity/response reduction, and the unresolved identification
  bridge.
- [PROTOCOL.md](PROTOCOL.md): machine-frozen bounded experiment and hard
  stopping rules.
- [STAGE0_REPORT.md](STAGE0_REPORT.md): authoritative corrected outcome and
  the reason positive time remains locked.
- [truncated_mfp_reference.py](truncated_mfp_reference.py): independent
  low-order MFP evaluator for a
  symmetric truncated-Gaussian readout law.
- [dmft_contact_prototype.py](dmft_contact_prototype.py): Stage-0
  initialization and density-response contact prototype; it is not a
  positive-time solver.
- [test_bounded_dmft.py](test_bounded_dmft.py): initialization, response, and
  low-order reference
  gates which do not require a positive-time DMFT claim.
- [FROZEN_STAGE0_MANIFEST.json](FROZEN_STAGE0_MANIFEST.json): hashes, corrected
  response convention, test result, and explicit list of runs not performed.

The primary cutoff is

\[
a_0\sim N(0,1)\mid |a_0|\le 3,
\]

without variance renormalization.  Any removal of that cutoff is a separate
future campaign, not an automatic branch of this one.
