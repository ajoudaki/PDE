"""Fetch checksum-verified MNIST and freeze a train-only binary split."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import struct
import urllib.request
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'data/generated/first_order_dimension_mnist'
BASE = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
FILES = {
    'train-images-idx3-ubyte.gz': 'f68b3c2dcbeaaa9fbdd348bbdeb94873',
    'train-labels-idx1-ubyte.gz': 'd53e105ee54ea40749a09fcbcd1e9432',
    't10k-images-idx3-ubyte.gz': '9fb629c4189551a2d022fa330f9573f3',
    't10k-labels-idx1-ubyte.gz': 'ec29112dd5afa0611ce80d1b7f02629c',
}

def acquire():
    raw = OUT / 'mnist_raw'
    raw.mkdir(parents=True, exist_ok=True)
    provenance = {}
    for name, md5 in FILES.items():
        path = raw / name
        if not path.exists():
            with urllib.request.urlopen(BASE + name, timeout=60) as r:
                data = r.read()
            if hashlib.md5(data).hexdigest() != md5:
                raise ValueError('download checksum mismatch: ' + name)
            path.write_bytes(data)
        data = path.read_bytes()
        assert hashlib.md5(data).hexdigest() == md5
        provenance[name] = {'url': BASE+name, 'md5':md5,
                            'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    (raw/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    return raw

def read_idx(path):
    data = gzip.decompress(path.read_bytes())
    zero, kind, nd = struct.unpack('>HBB', data[:4])
    assert zero == 0 and kind == 8
    shape = struct.unpack('>'+'I'*nd, data[4:4+4*nd])
    a = np.frombuffer(data, dtype=np.uint8, offset=4+4*nd)
    assert a.size == int(np.prod(shape))
    return a.reshape(shape)

def prepare(digits=(3,5), split_seed=20260915):
    raw = acquire()
    destination = OUT / ('data_%d_%d' % tuple(digits))
    destination.mkdir(parents=True,exist_ok=False)
    images=read_idx(raw/'train-images-idx3-ubyte.gz')
    labels=read_idx(raw/'train-labels-idx1-ubyte.gz')
    test_images=read_idx(raw/'t10k-images-idx3-ubyte.gz')
    test_labels=read_idx(raw/'t10k-labels-idx1-ubyte.gz')
    rng=np.random.default_rng(split_seed)
    train_idx=[];val_idx=[]
    for digit in digits:
        ids=rng.permutation(np.flatnonzero(labels==digit))
        val_idx.extend(ids[:500]);train_idx.extend(ids[500:])
    train_idx=rng.permutation(train_idx);val_idx=np.array(val_idx)
    test_idx=np.flatnonzero(np.isin(test_labels,digits))
    arrays={}
    for part, ims,labs,idx in [('train',images,labels,train_idx),('val',images,labels,val_idx),('test',test_images,test_labels,test_idx)]:
        x=ims[idx].reshape(len(idx),-1).astype(np.float64)/255.
        norms=np.linalg.norm(x,axis=1)
        assert np.all(norms>0)
        u=x/norms[:,None]
        arrays[part+'_u']=u.astype(np.float32)
        arrays[part+'_y']=np.where(labs[idx]==digits[0],1.,-1.).astype(np.float32)
        arrays[part+'_ids']=np.asarray(idx)
    assert not np.intersect1d(train_idx,val_idx).size
    np.savez_compressed(destination/'dataset.npz',**arrays)
    meta={'digits':list(digits),'positive_digit':digits[0],'negative_digit':digits[1],
          'split_seed':split_seed,'dimension':784,'preprocessing':'flatten pixels/255, then per-image L2 normalize; u=x/sqrt(d) is the model input; no PCA, whitening, centering, augmentation or test-fitted preprocessing',
          'counts':{p:len(arrays[p+'_y']) for p in ('train','val','test')},
          'class_counts':{p:[int((arrays[p+'_y']==s).sum()) for s in (1,-1)] for p in ('train','val','test')},
          'dataset_sha256':hashlib.sha256((destination/'dataset.npz').read_bytes()).hexdigest(),
          'sources':json.loads((raw/'provenance.json').read_text())}
    (destination/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--download-only',action='store_true')
    parser.add_argument('--digits',type=int,nargs=2,default=[3,5]);args=parser.parse_args()
    if args.download_only: print(acquire())
    else: prepare(tuple(args.digits))
