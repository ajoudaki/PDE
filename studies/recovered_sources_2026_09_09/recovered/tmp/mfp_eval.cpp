#include <algorithm>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

using i128 = __int128_t;

static std::string show(i128 value) {
    if (value == 0) return "0";
    bool neg = value < 0;
    if (neg) value = -value;
    std::string out;
    while (value) {
        out.push_back(char('0' + value % 10));
        value /= 10;
    }
    if (neg) out.push_back('-');
    std::reverse(out.begin(), out.end());
    return out;
}

static i128 odd_df(int degree_minus_one) {
    i128 out = 1;
    for (int j = degree_minus_one; j > 0; j -= 2) out *= j;
    return out;
}

struct RollbackDSU {
    std::vector<int> parent, size;
    std::vector<std::tuple<int,int,int>> history;
    int classes;

    explicit RollbackDSU(int n): parent(n), size(n,1), classes(n) {
        std::iota(parent.begin(), parent.end(), 0);
    }
    int root(int x) const {
        while (parent[x] != x) x = parent[x];
        return x;
    }
    int snapshot() const { return int(history.size()); }
    void unite(int a, int b) {
        a = root(a); b = root(b);
        if (a == b) {
            history.emplace_back(-1,-1,-1);
            return;
        }
        if (size[a] < size[b]) std::swap(a,b);
        history.emplace_back(b,a,size[a]);
        parent[b] = a;
        size[a] += size[b];
        --classes;
    }
    void rollback(int snap) {
        while (int(history.size()) > snap) {
            auto [b,a,old_size] = history.back();
            history.pop_back();
            if (b >= 0) {
                parent[b] = b;
                size[a] = old_size;
                ++classes;
            }
        }
    }
};

struct Component {
    std::vector<std::pair<int,int>> edges;
    std::vector<int> kind;
    std::vector<int> degree;
};

struct StateKey {
    uint32_t mask;
    uint64_t lo, hi;
    bool operator==(const StateKey &o) const {
        return mask==o.mask && lo==o.lo && hi==o.hi;
    }
};

struct StateHash {
    size_t operator()(const StateKey &s) const {
        uint64_t z = s.lo ^ (s.hi + 0x9e3779b97f4a7c15ULL + (s.lo<<6) + (s.lo>>2));
        z ^= uint64_t(s.mask) * 0xbf58476d1ce4e5b9ULL;
        z ^= z >> 30; z *= 0xbf58476d1ce4e5b9ULL;
        z ^= z >> 27; z *= 0x94d049bb133111ebULL;
        z ^= z >> 31;
        return size_t(z);
    }
};

struct PairingCounter {
    const Component &component;
    RollbackDSU dsu;
    int target;
    std::unordered_map<StateKey,i128,StateHash> memo;

    explicit PairingCounter(const Component &c): component(c), dsu(int(c.kind.size())),
        target(int(c.edges.size()/2 + 1)) {}

    i128 leaf_moment() {
        if (dsu.classes != target) return 0;
        const int n = int(component.kind.size());
        std::vector<int> atop(n,0), xbot(n,0);
        for (int v=0; v<n; ++v) {
            int r = dsu.root(v);
            if (component.kind[v] == 0) atop[r] += component.degree[v];
            else xbot[r] += component.degree[v];
        }
        i128 value = 1;
        for (int v=0; v<n; ++v) if (dsu.root(v) == v) {
            if ((atop[v]&1) || (xbot[v]&1)) return 0;
            value *= odd_df(atop[v]-1);
            value *= odd_df(xbot[v]-1);
        }
        return value;
    }

    i128 recurse(uint32_t mask) {
        if (!mask) return leaf_moment();
        const int pairs_left = __builtin_popcount(mask)/2;
        if (dsu.classes < target || dsu.classes - 2*pairs_left > target) return 0;
        const bool use_memo = true;
        StateKey key{mask,0,0};
        if (use_memo) {
            int next_label=0;
            int root_label[32];
            std::fill(root_label, root_label+32, -1);
            for (int v=0; v<int(component.kind.size()); ++v) {
                int root=dsu.root(v);
                if (root_label[root]<0) root_label[root]=next_label++;
                uint64_t label=uint64_t(root_label[root]);
                if (v<12) key.lo |= label << (5*v);
                else key.hi |= label << (5*(v-12));
            }
            auto found=memo.find(key);
            if (found!=memo.end()) return found->second;
        }
        int e0 = __builtin_ctz(mask);
        uint32_t rest = mask & ~(uint32_t(1) << e0);
        i128 total = 0;
        while (rest) {
            int e1 = __builtin_ctz(rest);
            rest &= rest - 1;
            int snap = dsu.snapshot();
            dsu.unite(component.edges[e0].first, component.edges[e1].first);
            dsu.unite(component.edges[e0].second, component.edges[e1].second);
            total += recurse(mask & ~(uint32_t(1) << e0) & ~(uint32_t(1) << e1));
            dsu.rollback(snap);
        }
        if (use_memo) memo.emplace(key,total);
        return total;
    }

    i128 evaluate() {
        int E = int(component.edges.size());
        if (E & 1) return 0;
        if (E >= 32) throw std::runtime_error("edge mask too large");
        return recurse((uint32_t(1) << E) - 1);
    }
};

struct Term {
    i128 coef;
    int power, nt, nb;
    std::vector<int> a, x, matrix;
};

static std::vector<Component> components(const Term &t) {
    const int nv = t.nt + t.nb;
    std::vector<std::vector<int>> adj(nv);
    std::vector<std::pair<int,int>> edges;
    for (int p=0; p<t.nt; ++p) for (int i=0; i<t.nb; ++i) {
        int count = t.matrix[p*t.nb+i];
        if (count != 0 && count != 1) throw std::runtime_error("parallel edge");
        if (count) {
            int u=p, v=t.nt+i;
            adj[u].push_back(v); adj[v].push_back(u);
            edges.emplace_back(u,v);
        }
    }
    std::vector<int> seen(nv,0);
    std::vector<Component> out;
    for (int start=0; start<nv; ++start) if (!seen[start]) {
        std::vector<int> stack{start}, verts;
        seen[start]=1;
        while (!stack.empty()) {
            int v=stack.back(); stack.pop_back(); verts.push_back(v);
            for (int w:adj[v]) if (!seen[w]) { seen[w]=1; stack.push_back(w); }
        }
        std::vector<int> local(nv,-1);
        for (int j=0;j<int(verts.size());++j) local[verts[j]]=j;
        Component c;
        for (int v:verts) {
            c.kind.push_back(v<t.nt ? 0:1);
            c.degree.push_back(v<t.nt ? t.a[v]:t.x[v-t.nt]);
        }
        for (auto [u,v]:edges) if (local[u]>=0 && local[v]>=0)
            c.edges.emplace_back(local[u],local[v]);
        if (int(c.edges.size()) != int(c.kind.size())-1) throw std::runtime_error("not tree");
        out.push_back(std::move(c));
    }
    if (int(out.size()) != t.power) throw std::runtime_error("component/power mismatch");
    return out;
}

int main(int argc, char **argv) {
    if (argc != 2 && argc != 3) { std::cerr << "usage: mfp_eval terms.txt [lambda_power]\n"; return 2; }
    int requested_power = argc == 3 ? std::stoi(argv[2]) : -1;
    std::ifstream in(argv[1]);
    int count; in >> count;
    std::vector<Term> terms(count);
    for (Term &t:terms) {
        long long coef;
        in >> coef >> t.power >> t.nt >> t.nb;
        t.coef=coef;
        t.a.resize(t.nt); t.x.resize(t.nb); t.matrix.resize(t.nt*t.nb);
        for (int &v:t.a) in>>v;
        for (int &v:t.x) in>>v;
        for (int &v:t.matrix) in>>v;
    }
    std::vector<i128> values(count,0);
    std::atomic<int> done{0};
    #pragma omp parallel for schedule(dynamic,1)
    for (int idx=0; idx<count; ++idx) {
        int edge_count=std::accumulate(terms[idx].matrix.begin(),terms[idx].matrix.end(),0);
        if (requested_power >= 0 && edge_count/2 != requested_power) {
            int now=++done;
            continue;
        }
        i128 value=1;
        for (const Component &c:components(terms[idx])) {
            i128 part=PairingCounter(c).evaluate();
            if (!part) { value=0; break; }
            value*=part;
        }
        values[idx]=value;
        int now=++done;
        if (now%500==0) {
            #pragma omp critical
            std::cerr << "evaluated " << now << "/" << count << "\n";
        }
    }
    std::vector<i128> lambda(32,0), power(32,0);
    i128 total=0; int surviving=0;
    for (int idx=0;idx<count;++idx) {
        if (!values[idx]) continue;
        ++surviving;
        i128 contribution=terms[idx].coef*values[idx];
        total+=contribution;
        int edge_count=std::accumulate(terms[idx].matrix.begin(),terms[idx].matrix.end(),0);
        lambda[edge_count/2]+=contribution;
        power[terms[idx].power]+=contribution;
    }
    std::cout << "surviving " << surviving << "/" << count << "\n";
    std::cout << "lambda";
    for (int j=0;j<int(lambda.size());++j) if (lambda[j]) std::cout << " " << j << ":" << show(lambda[j]);
    std::cout << "\npower";
    for (int j=0;j<int(power.size());++j) if (power[j]) std::cout << " " << j << ":" << show(power[j]);
    std::cout << "\ntotal " << show(total) << "\n";
}
