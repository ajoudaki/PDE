import sys
import time

sys.path.insert(0, "/tmp")
import mfp_graph_compiler as m

order = int(sys.argv[1])
max_power = int(sys.argv[2])
path = sys.argv[3]
terms = [m.Term((1,), (2, 2), ((1, 1),), 1, 1)]
for step in range(order):
    start = time.time()
    raw = [u for t in terms for u in m.differentiate(t) if u.power <= max_power]
    terms = m.merge_terms(raw)
    counts = {}
    for t in terms:
        counts[t.power] = counts.get(t.power, 0) + 1
    print("order", step + 1, "raw", len(raw), "types", len(terms),
          "by_power", sorted(counts.items()), "sec", time.time() - start, flush=True)

with open(path, "w", encoding="utf-8") as handle:
    handle.write(f"{len(terms)}\n")
    for t in terms:
        nt, nb = len(t.a), len(t.x)
        fields = [t.coef, t.power, nt, nb]
        fields.extend(t.a)
        fields.extend(t.x)
        fields.extend(c for row in t.edges for c in row)
        handle.write(" ".join(map(str, fields)) + "\n")
