import sys

sys.path.insert(0, "/tmp")
import mfp_graph_compiler as m

order = int(sys.argv[1])
path = sys.argv[2]
terms = m.main(order, True)
with open(path, "w", encoding="utf-8") as handle:
    handle.write(f"{len(terms)}\n")
    for t in terms:
        nt, nb = len(t.a), len(t.x)
        fields = [t.coef, t.power, nt, nb]
        fields.extend(t.a)
        fields.extend(t.x)
        fields.extend(c for row in t.edges for c in row)
        handle.write(" ".join(map(str, fields)) + "\n")
