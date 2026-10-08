"""Four predeclared fresh-population audits; no coupled training runs."""
from pathlib import Path
import json
import os
import subprocess
import sys

STUDY = Path(__file__).resolve().parent
ROOT = Path('data/generated/transparent_learning_dynamics_20261007')
OUT = ROOT / 'frozen_quadrature_v1'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    for source_seed, fresh_seed, repeat in ((1701, 8101, False),
            (1702, 8102, False), (1703, 8103, False), (1701, 8101, True)):
        records = [json.loads(p.read_text()) for p in OUT.glob('*/record.json')]
        used = sum(r.get('wall_seconds', 0.) for r in records)
        if len(records) >= 4 or used >= 1200 or any(r['exit_status'] for r in records):
            raise RuntimeError('Fixed scientific cohort stopped')
        source = ROOT / 'residual_filter_v1' / (
            f'causal_m16_n256_s{source_seed}_h0.2_filtered/trajectory.npz')
        destination = OUT / (f'source{source_seed}_fresh{fresh_seed}_n32768'
                             + ('_repeat' if repeat else ''))
        if destination.exists():
            raise RuntimeError(f'Refusing to overwrite {destination}')
        command = [sys.executable, str(STUDY / 'frozen_population_replay.py'),
                   '--source', str(source), '--out', str(destination),
                   '--n', '32768', '--batch', '1024', '--seed', str(fresh_seed)]
        # The driver records numerical work; timeout additionally caps this
        # child's total elapsed time, including output serialization.
        try:
            subprocess.run(command, env=env, check=True, timeout=1200-used)
        except subprocess.TimeoutExpired:
            (OUT / 'timeout.json').write_text(json.dumps(dict(
                command=command, remaining_seconds=1200-used,
                status='interrupted_at_budget'), indent=2)+'\n')
            raise


if __name__ == '__main__':
    main()
