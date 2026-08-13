# D11 lower-sector provenance audit

Audit date: 2026-08-12

## Conclusion

The reported order-11 sectors `P=1,...,9` are not merely copied values.  Each
was produced by a completed exhaustive differentiated-forest export followed
by a completed Wick contraction run in checked 512-bit integer arithmetic.
The same checked binary first passed the full order-9 sector regression gate.

The evidence is strongest for `P=1,...,6`, which were also obtained directly
inside the exhaustive generator.  `P=7,8` have an earlier second evaluator
run on the same exhaustive exports.  `P=9` has one complete checked-512
evaluation; an older progress file that stopped at `200500/200549` unique
components is incomplete and is not used as evidence.

Thus all nine values are accepted as exact outputs of the audited computer
algebra implementation.  This is a computational certificate under the
proved peeling/Wick reduction and the implementation audit; it is not an
independent hand enumeration of every contraction.

## Exact values

```text
P=1  23170716039905280
P=2  17433397654868459520
P=3  1428455842962100715520
P=4  40114976109177824870400
P=5  530996753942041626279936
P=6  3868170903724215843717120
P=7  16894189549156196962566144
P=8  46146109609021522448793600
P=9  79443613137340581848727552
```

Their exact subtotal is

```text
P=1,...,9: 146924640841705069564035072
```

Combining this with the separately certified high-sector subtotal

```text
P=10,...,12: 145058191545880802771435520
```

gives

```text
D^11 f = 291982832387585872335470592
D^11 f / 11! = 42242886630148419030016/5775
```

As a separate analytic check on the first sector,

```text
36 * 144^5 * 11!! = 23170716039905280,
```

which exactly equals `P=1`.

## Persistent raw artifacts

The exhaustive generator source is
`studies/stieltjes_conjecture/peeling/exhaustive_reference.cpp`.  It is
byte-identical to the source
that generated the four exports:

```text
sha256 5f1b8b1ba3ee4ceec248255d295842092dbdc40f4cfe0ced3723bb0fa8efc041
```

The generator stores all coefficients in arbitrary-precision `cpp_int`.

The historical evaluator source before the checked-integer patch survives as
`/tmp/mfp_eval_unique.cpp`, with hash

```text
7a967d480c4714027067400cdb808e248e47a5ce0dd6f8c9154dae361f883ae9
```

This is also the evaluator hash frozen in
`studies/stieltjes_conjecture/peeling/source_hashes.txt`.
The run binary was compiled from this source after replacing its signed
128-bit accumulator by `boost::multiprecision::checked_uint512_t`.  Its hash
is

```text
studies/stieltjes_conjecture/peeling/export_evaluator_checked512
sha256 c57614ada453e818e9952abd70ced82f93dc3324d16b9f6a5dc394d7d2780d76
```

A successful run therefore cannot silently wrap.  The independent analytic
size bound through order 13 is 275 bits, below the 512-bit capacity.

The raw exhaustive exports have these frozen hashes and record counts:

```text
P=1,...,6
  /tmp/mfp_terms11_p1_6.txt
  sha256 ebfee62e44e0b4a2499699a31fdc4fec120a68620e3b4cfb2dd4ec61d6c95ee5
  header count 84480; line count 84481

P=7
  /tmp/mfp_terms11_p7.txt
  sha256 2b24683e7f55e7bd2cec0eddf1d11565fdeed1cc4a96efda513a7c9ad8b34237
  header count 207997; line count 207998

P=8
  /tmp/mfp_terms11_p8.txt
  sha256 2b515651fc0705729d3245ce30f65f5a235c1b3a3b221a8753463c8057f1412e
  header count 458457; line count 458458

P=9
  /tmp/mfp_terms11_p9.txt
  sha256 b3f79e0e98ed20284311338486bf38b108d4c8cff0199f308f6fe590b2a2e3fa
  header count 661312; line count 661313
```

The term files live in `/tmp` and are therefore not archival storage.  The
hashes, exact scalars, and run provenance in this note are the compact durable
record; retaining the large exports elsewhere would be required for a future
bit-for-bit rerun without regenerating them.

## Commands and completion evidence

The authoritative conversation transcript is

```text
/home/amir/.codex/sessions/2026/08/09/
rollout-2026-08-09T18-38-00-019fe763-6d7f-75d2-946c-d0faab6ff38c.jsonl
```

Immediately before the D11 runs, the checked binary evaluated the full D9
export and exactly reproduced all ten accepted D9 sectors and their total;
see JSONL lines `13696-13720`.

The D11 commands were:

```bash
prlimit --as=20000000000 -- env OMP_NUM_THREADS=24 \
  ./studies/stieltjes_conjecture/peeling/export_evaluator_checked512 \
  /tmp/mfp_terms11_p1_6.txt

prlimit --as=20000000000 -- env OMP_NUM_THREADS=24 \
  ./studies/stieltjes_conjecture/peeling/export_evaluator_checked512 \
  /tmp/mfp_terms11_p7.txt

prlimit --as=20000000000 -- env OMP_NUM_THREADS=24 \
  ./studies/stieltjes_conjecture/peeling/export_evaluator_checked512 \
  /tmp/mfp_terms11_p8.txt

prlimit --as=20000000000 -- env OMP_NUM_THREADS=24 \
  ./studies/stieltjes_conjecture/peeling/export_evaluator_checked512 \
  /tmp/mfp_terms11_p9.txt
```

Complete successful outputs are recorded at JSONL lines:

```text
P=1,...,6: line 13729, exit_code 0
P=7:       line 13737, exit_code 0
P=8:       line 13748, exit_code 0
P=9:       line 13803, exit_code 0
```

The output diagnostics were:

```text
P=1,...,6: 84480 exhaustive terms; 24028 unique components;
            35634 surviving terms
P=7:       207997 exhaustive terms; 59352 unique components;
            85315 surviving terms
P=8:       458457 exhaustive terms; 128656 unique components;
            191719 surviving terms
P=9:       661312 exhaustive terms; 200549 unique components;
            296872 surviving terms
```

Earlier direct exhaustive-generator outputs independently reproduce
`P=1,...,6`; see JSONL lines `8745-8781`.  Earlier second-evaluator outputs
reproduce `P=7` and `P=8`; see lines `8919-8920` and `8949-8961`.

## Certification classification

| Object | Status | Evidence scope |
|---|---|---|
| `P=1,...,6` | accepted exact computational certificate | exhaustive generator plus checked-512 export evaluator, with a second direct evaluation; `P=1` also has a closed-form check |
| `P=7,8` | accepted exact computational certificate | exhaustive export plus checked-512 evaluator, with an earlier second evaluator run |
| `P=9` | accepted exact computational certificate | exhaustive export plus one complete checked-512 evaluator run; the older partial progress file is explicitly excluded |
| `D^11 f` total | accepted exact computational certificate | exact sum of certified `P=1,...,12` sectors |

The remaining audit limitation is route independence, not missing arithmetic:
`P=9` has not yet been recomputed by the newer connected-sector recurrence.
That would strengthen redundancy but is not needed to recover its scalar.

## Supersession warning

`studies/stieltjes_conjecture/theory/EARLIER_REPORT.md` predates these completed
computations.  Its
opening claim that order 11 is still provisional/incomplete is superseded by
the checked runs above and must not be quoted as the current D11 status.  The
newer `studies/stieltjes_conjecture/theory/derivatives_order11.json` contains
the correct
total, but this audit note is the provenance record explaining why that total
is accepted.
