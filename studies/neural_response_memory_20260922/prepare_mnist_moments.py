"""Freeze one balanced MNIST 3/8 subset; no estimated preprocessing."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from torchvision.datasets import MNIST


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    raw = args.output / 'raw_cache'
    train = MNIST(str(raw), train=True, download=True)
    validation = MNIST(str(raw), train=False, download=True)
    rng = np.random.default_rng(20260924)
    train_digits = train.targets.numpy()
    validation_digits = validation.targets.numpy()
    train_ids = np.concatenate([rng.choice(np.flatnonzero(train_digits == digit),
                                           size=500, replace=False)
                                for digit in (3, 8)])
    rng.shuffle(train_ids)
    validation_ids = np.flatnonzero(np.isin(validation_digits, (3, 8)))

    def scaled(images, indices):
        values = images.numpy()[indices].reshape(len(indices), -1).astype(np.float64)
        norms = np.linalg.norm(values, axis=1, keepdims=True)
        if np.any(norms == 0):
            raise ValueError('zero image cannot be normalized')
        return values / norms

    prepared = args.output / 'prepared.npz'
    np.savez_compressed(prepared,
        train_inputs=scaled(train.data, train_ids),
        train_labels=np.where(train_digits[train_ids] == 3, -1., 1.),
        validation_inputs=scaled(validation.data, validation_ids),
        validation_labels=np.where(validation_digits[validation_ids] == 3, -1., 1.),
        train_ids=train_ids, validation_ids=validation_ids,
        train_digits=train_digits[train_ids], validation_digits=validation_digits[validation_ids])
    metadata = dict(seed=20260924, digits=[3, 8], samples_per_class=500,
        training_count=len(train_ids), validation_count=len(validation_ids),
        validation_counts={str(i): int(np.sum(validation_digits[validation_ids] == i))
                           for i in (3, 8)},
        preprocessing='U=x/sqrt(d)=flattened image / image Euclidean norm; d=784',
        splits='official train for fitting; official test used as validation',
        source_mirrors=MNIST.mirrors, resources=MNIST.resources,
        prepared_sha256=sha256(prepared), source_sha256=sha256(__file__),
        raw_sha256={str(p.relative_to(args.output)): sha256(p)
                    for p in sorted(raw.rglob('*')) if p.is_file()})
    (args.output / 'provenance.json').write_text(json.dumps(metadata, indent=2)+'\n')
    print(json.dumps(metadata, indent=2))


if __name__ == '__main__':
    main()
