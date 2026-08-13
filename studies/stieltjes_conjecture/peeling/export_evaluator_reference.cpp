#include <algorithm>
#include <atomic>
#include <boost/multiprecision/cpp_int.hpp>
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

// The order-13 degree/L1 audit bounds every positive intermediate by 275
// bits.  Checked 512-bit arithmetic is therefore exact here and turns any
// violated implementation assumption into an exception instead of wrapping.
using i128 = boost::multiprecision::checked_uint512_t;

static std::string show(const i128 &value) { return value.str(); }

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

        // In a leading quotient each Wick pair supplies one tree edge.  If
        // more than two raw edges already lie in one quotient cell, later
        // identifications can only increase that multiplicity, so the branch
        // can never become a tree.
        const int n = int(component.kind.size());
        int cell_count[32][32]{};
        for (auto [u,v] : component.edges) {
            int ru = dsu.root(u), rv = dsu.root(v);
            if (++cell_count[ru][rv] > 2) return 0;
        }

        // A readout class with odd Gaussian degree must still be merged by an
        // endpoint of an unpaired edge.  Once inactive, its odd moment is
        // permanently zero.
        bool active[32]{};
        for (uint32_t bits=mask; bits; bits &= bits-1) {
            int e=__builtin_ctz(bits);
            active[dsu.root(component.edges[e].first)]=true;
            active[dsu.root(component.edges[e].second)]=true;
        }
        int a_parity[32]{};
        for (int v=0; v<n; ++v)
            if (component.kind[v]==0)
                a_parity[dsu.root(v)] ^= (component.degree[v]&1);
        for (int v=0; v<n; ++v)
            if (dsu.root(v)==v && a_parity[v] && !active[v]) return 0;
        const bool use_memo = component.edges.size() >= 16;
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
        int atop=0, xbot=0;
        for (int v=0; v<int(component.kind.size()); ++v) {
            if (component.kind[v]==0) atop += component.degree[v];
            else xbot += component.degree[v];
        }
        if ((atop&1) || (xbot&1)) return 0;
        if (E >= 32) throw std::runtime_error("edge mask too large");
        return recurse((uint32_t(1) << E) - 1);
    }
};

// Exact Wick recursion on edge multiplicities rather than labelled edge masks.
// One occurrence of the first nonempty edge type is fixed; pairing it with a
// partner type contributes the remaining multiplicity of that partner.  Row
// and column endpoint classes are then merged.  This counts the same labelled
// pairings as PairingCounter, but is often faster for 20--24 edge components.
struct TypePairingCounter {
    int P, target;
    std::unordered_map<std::string,i128> memo;
    // Exact bounded-memory mode: once the transposition table reaches this
    // size, recursion continues without inserting new entries.  Omitting a
    // memo entry can only repeat work; it cannot change the returned sum.
    static constexpr size_t memo_entry_cap = 200000;

    static std::string key(const std::vector<int>&a,const std::vector<int>&h,
                           const std::vector<int>&m,
                           const std::vector<int>&paired) {
        std::string s; s.reserve(2+a.size()+h.size()+m.size()+paired.size());
        s.push_back(char(a.size())); s.push_back(char(h.size()));
        for(int z:a)s.push_back(char(z)); for(int z:h)s.push_back(char(z));
        for(int z:m)s.push_back(char(z));
        for(int z:paired)s.push_back(char(z));
        return s;
    }
    static void merge_rows(int x,int y,std::vector<int>&a,
                           std::vector<int>&m,int cols) {
        if(x==y)return; if(x>y)std::swap(x,y); a[x]+=a[y];
        for(int j=0;j<cols;++j)m[x*cols+j]+=m[y*cols+j];
        a.erase(a.begin()+y); m.erase(m.begin()+y*cols,m.begin()+(y+1)*cols);
    }
    static void merge_cols(int x,int y,std::vector<int>&h,
                           std::vector<int>&m,int rows,int cols) {
        if(x==y)return; if(x>y)std::swap(x,y); h[x]+=h[y];
        for(int i=0;i<rows;++i)m[i*cols+x]+=m[i*cols+y];
        std::vector<int> z; z.reserve(rows*(cols-1));
        for(int i=0;i<rows;++i)for(int j=0;j<cols;++j)if(j!=y)
            z.push_back(m[i*cols+j]);
        h.erase(h.begin()+y); m.swap(z);
    }
    static bool is_forest(const std::vector<int>&paired,int rows,int cols) {
        std::vector<int> parent(rows+cols),rank(rows+cols,0);
        std::iota(parent.begin(),parent.end(),0);
        auto root=[&](int x) {
            int y=x;
            while(parent[y]!=y)y=parent[y];
            while(parent[x]!=x){int z=parent[x];parent[x]=y;x=z;}
            return y;
        };
        for(int i=0;i<rows;++i)for(int j=0;j<cols;++j) {
            int multiplicity=paired[i*cols+j];
            if(multiplicity>1)return false;
            if(!multiplicity)continue;
            int x=root(i),y=root(rows+j);
            if(x==y)return false;
            if(rank[x]<rank[y])std::swap(x,y);
            parent[y]=x;
            if(rank[x]==rank[y])++rank[x];
        }
        return true;
    }
    i128 rec(const std::vector<int>&a,const std::vector<int>&h,
             const std::vector<int>&m,const std::vector<int>&paired,int rem) {
        int V=a.size()+h.size(), pairs=rem/2;
        if(V<target || V-2*pairs>target)return 0;

        // A leading connected quotient has P+1 vertices and P occupied
        // covariance cells.  It is therefore a tree, and every occupied cell
        // contains exactly the two raw W factors consumed by one Wick pair.
        // Vertex identifications only merge cells; they can never split one.
        // Hence a branch is permanently dead as soon as a current cell
        // already contains more than two raw factors.  `m` counts unpaired
        // factors and `paired` counts completed pairs.
        for (size_t q=0;q<m.size();++q)
            if (m[q] + 2*paired[q] > 2) return 0;

        const int rows_now=a.size(), cols_now=h.size();
        // An odd readout-Gaussian class must still participate in a future
        // row merge.  Such a merge can only use an endpoint of a remaining W
        // factor, so an inactive odd row can never acquire an even moment.
        for (int i=0;i<rows_now;++i) if (a[i]&1) {
            bool active=false;
            for (int j=0;j<cols_now;++j) if (m[i*cols_now+j]) {
                active=true; break;
            }
            if (!active) return 0;
        }

        // The completed covariance cells form a forest.  Every one of its
        // current connected components (isolated vertices included) must be
        // touched by a remaining factor unless it is already the sole
        // component; otherwise no future pairing can attach that component
        // to the final connected quotient tree.
        if (rem) {
            std::vector<int> parent(rows_now+cols_now), rank(rows_now+cols_now,0);
            std::iota(parent.begin(),parent.end(),0);
            auto root=[&](int x) {
                int y=x; while(parent[y]!=y)y=parent[y];
                while(parent[x]!=x){int z=parent[x];parent[x]=y;x=z;}
                return y;
            };
            auto unite=[&](int x,int y) {
                x=root(x); y=root(y); if(x==y)return;
                if(rank[x]<rank[y])std::swap(x,y); parent[y]=x;
                if(rank[x]==rank[y])++rank[x];
            };
            for(int i=0;i<rows_now;++i)for(int j=0;j<cols_now;++j)
                if(paired[i*cols_now+j])unite(i,rows_now+j);
            std::vector<unsigned char> touched(rows_now+cols_now,0),seen(rows_now+cols_now,0);
            for(int i=0;i<rows_now;++i)for(int j=0;j<cols_now;++j)
                if(m[i*cols_now+j]) {
                    touched[root(i)]=1; touched[root(rows_now+j)]=1;
                }
            int components=0;
            for(int v=0;v<rows_now+cols_now;++v)if(root(v)==v)++components;
            if(components>1)
                for(int v=0;v<rows_now+cols_now;++v)
                    if(root(v)==v && !touched[v])return 0;
        }
        if(!rem) {
            if(V!=target)return 0; i128 z=1;
            for(int q:a){if(q&1)return 0;z*=odd_df(q-1);}
            for(int q:h){if(q&1)return 0;z*=odd_df(q-1);}
            return z;
        }
        std::string k=key(a,h,m,paired); auto found=memo.find(k);
        if(found!=memo.end())return found->second;
        int rows=a.size(),cols=h.size(),q0=-1;
        // If a current quotient cell contains two unpaired factors, those
        // two factors are forced to pair: pairing either one outside would
        // leave the other factor in a cell already occupied by the completed
        // pair, violating the exact capacity-two condition above.  Choosing
        // such a cell first turns that forced move into a one-branch step.
        for(int q=0;q<int(m.size());++q)if(m[q]==2){q0=q;break;}
        if(q0<0)
            for(int q=0;q<int(m.size());++q)if(m[q]){q0=q;break;}
        int u0=q0/cols,v0=q0%cols; auto first=m; --first[q0]; i128 ans=0;
        for(int q1=0;q1<int(first.size());++q1)if(first[q1]) {
            int mult=first[q1],u1=q1/cols,v1=q1%cols;
            auto aa=a,hh=h,mm=first,pp=paired; --mm[q1];
            merge_rows(u0,u1,aa,mm,cols);
            {
                std::vector<int> dummy(pp.size()/cols,0);
                merge_rows(u0,u1,dummy,pp,cols);
            }
            merge_cols(v0,v1,hh,mm,aa.size(),cols);
            {
                std::vector<int> dummy(cols,0);
                merge_cols(v0,v1,dummy,pp,aa.size(),cols);
            }
            const int new_cols=hh.size();
            const int new_u=std::min(u0,u1),new_v=std::min(v0,v1);
            ++pp[new_u*new_cols+new_v];
            if(!is_forest(pp,aa.size(),new_cols))continue;
            ans += i128(mult)*rec(aa,hh,mm,pp,rem-2);
        }
        if (memo.size() < memo_entry_cap) memo.emplace(std::move(k),ans);
        return ans;
    }
    i128 evaluate(const Component&c) {
        std::vector<int> rows,cols;
        for(int v=0;v<int(c.kind.size());++v)
            (c.kind[v]==0?rows:cols).push_back(v);
        std::vector<int> rmap(c.kind.size(),-1),cmap(c.kind.size(),-1),a,h;
        for(int i=0;i<int(rows.size());++i){rmap[rows[i]]=i;a.push_back(c.degree[rows[i]]);}
        for(int j=0;j<int(cols.size());++j){cmap[cols[j]]=j;h.push_back(c.degree[cols[j]]);}
        std::vector<int> m(rows.size()*cols.size());
        for(auto [u,v]:c.edges) {
            if(c.kind[u]==1)std::swap(u,v);
            ++m[rmap[u]*cols.size()+cmap[v]];
        }
        P=c.edges.size()/2; target=P+1;
        std::vector<int> paired(rows.size()*cols.size(),0);
        return rec(a,h,m,paired,c.edges.size());
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

static std::string rooted_component_code(
    int v, int parent, const Component &c,
    const std::vector<std::vector<int>> &adj) {
    std::vector<std::string> child;
    for (int w : adj[v]) if (w != parent)
        child.push_back(rooted_component_code(w, v, c, adj));
    std::sort(child.begin(), child.end());
    std::string out;
    out.push_back('(');
    out.push_back(char('A' + c.kind[v]));
    out.push_back(char(1 + c.degree[v]));
    for (const auto &z : child) out += z;
    out.push_back(')');
    return out;
}

static std::string component_key(const Component &c) {
    int n = c.kind.size();
    std::vector<std::vector<int>> adj(n);
    for (auto [u,v] : c.edges) { adj[u].push_back(v); adj[v].push_back(u); }
    if (n == 1) return rooted_component_code(0, -1, c, adj);
    std::vector<int> degree(n);
    std::vector<int> leaves;
    for (int v=0; v<n; ++v) {
        degree[v]=adj[v].size();
        if (degree[v]<=1) leaves.push_back(v);
    }
    int remaining=n;
    while (remaining>2) {
        std::vector<int> next;
        remaining -= leaves.size();
        for (int v:leaves) {
            degree[v]=0;
            for (int w:adj[v]) if (degree[w]>0) {
                --degree[w];
                if (degree[w]==1) next.push_back(w);
            }
        }
        leaves.swap(next);
    }
    std::vector<int> centers;
    for (int v=0;v<n;++v) if (degree[v]>0) centers.push_back(v);
    if (centers.empty()) centers=leaves;
    std::string best;
    for (int v:centers) {
        std::string z=rooted_component_code(v,-1,c,adj);
        if (best.empty() || z<best) best=std::move(z);
    }
    return best;
}

int main(int argc, char **argv) {
    if (argc < 2 || argc > 5) { std::cerr << "usage: mfp_eval terms.txt [lambda_power] [term_limit] OR terms power start length\n"; return 2; }
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
    if (argc == 4 && std::stoi(argv[3]) < count) {
        count=std::stoi(argv[3]); terms.resize(count);
    } else if (argc == 5) {
        int start=std::stoi(argv[3]), length=std::stoi(argv[4]);
        int stop=std::min(count,start+length);
        terms=std::vector<Term>(terms.begin()+start,terms.begin()+stop);
        count=terms.size();
    }
    std::unordered_map<std::string,int> component_ids;
    std::vector<Component> unique_components;
    std::vector<std::vector<int>> term_component_ids(count);
    for (int idx=0; idx<count; ++idx) {
        int edge_count=std::accumulate(terms[idx].matrix.begin(),terms[idx].matrix.end(),0);
        if (requested_power >= 0 && edge_count/2 != requested_power) continue;
        for (Component c : components(terms[idx])) {
            std::string key=component_key(c);
            auto [it,inserted]=component_ids.emplace(key,unique_components.size());
            if (inserted) unique_components.push_back(std::move(c));
            term_component_ids[idx].push_back(it->second);
        }
    }
    size_t parity_eligible=0;
    for (const Component &c:unique_components) {
        int atop=0,xbot=0;
        for (size_t v=0;v<c.kind.size();++v)
            (c.kind[v]==0 ? atop : xbot) += c.degree[v];
        if (!(atop&1) && !(xbot&1)) ++parity_eligible;
    }
    std::cerr << "unique components " << unique_components.size()
              << " parity_eligible " << parity_eligible << "\n";
    std::vector<i128> component_values(unique_components.size(),0);
    std::atomic<int> done{0};
    #pragma omp parallel for schedule(dynamic,1)
    for (int idx=0; idx<int(unique_components.size()); ++idx) {
        const Component &c=unique_components[idx];
        // For large components the multiplicity-state recursion counts the
        // same labelled Wick pairings but avoids the 2^E labelled-edge mask.
        // Both implementations are independently regressed below order 10;
        // the crossover is a performance choice only.
        component_values[idx]=c.edges.size() >= 20
            ? TypePairingCounter().evaluate(c)
            : PairingCounter(c).evaluate();
        int now=++done;
        if (now%500==0) {
            #pragma omp critical
            std::cerr << "evaluated components " << now << "/"
                      << unique_components.size() << "\n";
        }
    }
    std::vector<i128> values(count,0);
    #pragma omp parallel for schedule(static)
    for (int idx=0; idx<count; ++idx) {
        int edge_count=std::accumulate(terms[idx].matrix.begin(),terms[idx].matrix.end(),0);
        if (requested_power >= 0 && edge_count/2 != requested_power) continue;
        i128 value=1;
        for (int id:term_component_ids[idx]) {
            value*=component_values[id];
            if (!value) break;
        }
        values[idx]=value;
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
