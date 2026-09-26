"""Descriptive target diagnostics; PCA rank is not a neural-width lower bound."""
import argparse
import json
from pathlib import Path
import time
import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    started = time.monotonic()
    data = np.load(args.data)
    z, weights = np.polynomial.hermite.hermgauss(64)
    beta = float(np.dot(weights, np.sqrt(2)*z*np.tanh(np.sqrt(2)*z))/np.sqrt(np.pi))
    q = data['V'].T @ data['X_calibration'][:, :8192]
    features = np.tanh(q)-beta*q
    gram = features @ features.T/features.shape[1]
    eigenvalues = np.linalg.eigvalsh(gram)[::-1]
    coefficient = np.linalg.lstsq(data['X_train'].T, data['y_train'], rcond=None)[0]
    result = {
        'diagnostic_only_not_neural_width_lower_bound': True,
        'calibration_samples_used': 8192,
        'gaussian_linear_coefficient': beta,
        'residual_feature_effective_rank': float(eigenvalues.sum()**2/np.sum(eigenvalues**2)),
        'residual_feature_pca_energy_top244': float(eigenvalues[:244].sum()/eigenvalues.sum()),
        'residual_feature_pca_energy_top492': float(eigenvalues[:492].sum()/eigenvalues.sum()),
        'linear_least_squares_nrmse': {
            split: float(np.linalg.norm(coefficient@data['X_'+split]-data['y_'+split]) /
                         np.linalg.norm(data['y_'+split])) for split in ('train', 'passive')},
        'process_seconds': time.monotonic()-started}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
