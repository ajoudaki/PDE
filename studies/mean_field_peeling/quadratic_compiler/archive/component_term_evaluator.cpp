// Exact evaluator for the derivative-forest term format emitted by the main
// enumeration.  It reuses the independently derived connected-component Wick
// recurrence in /tmp/component_fast2.cpp, including its canonical subproblem
// cache and covariance-forest pruning.
#define main component_fast2_hidden_main
#include "/tmp/component_fast2.cpp"
#undef main

#include <fstream>
#include <unordered_map>

struct InputTerm {
  cpp_int coefficient{};
  int components{}, rows{}, cols{};
  std::vector<int> a, x, matrix;
};

static cpp_int parse_int(const std::string &s) {
  cpp_int z = 0;
  for (char c : s) if (c >= '0' && c <= '9') z = 10*z + (c-'0');
  return z;
}

static std::vector<Tree> split_term(const InputTerm &t) {
  int n = t.rows + t.cols;
  std::vector<std::vector<int>> nb(n);
  for (int r=0;r<t.rows;++r) for (int c=0;c<t.cols;++c)
    if (t.matrix[r*t.cols+c]) {
      nb[r].push_back(t.rows+c);
      nb[t.rows+c].push_back(r);
    }
  std::vector<int> seen(n), comp(n,-1);
  std::vector<Tree> out;
  for (int start=0;start<n;++start) if (!seen[start]) {
    std::vector<int> stack{start}, vertices;
    seen[start]=1;
    while (!stack.empty()) {
      int v=stack.back();stack.pop_back();vertices.push_back(v);
      for(int w:nb[v])if(!seen[w]){seen[w]=1;stack.push_back(w);}
    }
    Tree z;
    std::vector<int> rmap(t.rows,-1),cmap(t.cols,-1);
    for(int v:vertices) {
      if(v<t.rows){rmap[v]=z.a.size();z.a.push_back(t.a[v]);}
      else {int c=v-t.rows;cmap[c]=z.h.size();
        if(t.x[c]&1) throw std::runtime_error("odd u power");
        z.h.push_back(t.x[c]/2);
      }
    }
    for(int r=0;r<t.rows;++r)if(rmap[r]>=0)
      for(int c=0;c<t.cols;++c)if(cmap[c]>=0 && t.matrix[r*t.cols+c])
        z.edges.push_back({(unsigned char)rmap[r],(unsigned char)cmap[c]});
    if(z.edges.size()+1 != z.a.size()+z.h.size()) throw std::runtime_error("component not tree");
    out.push_back(std::move(z));
  }
  if((int)out.size()!=t.components) throw std::runtime_error("component count mismatch");
  return out;
}

int main(int argc,char **argv) {
  if(argc!=3){std::cerr<<"usage: component_term_evaluator terms.txt wick_pairs\n";return 2;}
  int wanted=std::stoi(argv[2]);
  std::ifstream in(argv[1]);
  int count;in>>count;
  std::vector<InputTerm> terms(count);
  for(auto &t:terms){
    std::string coef;in>>coef>>t.components>>t.rows>>t.cols;
    t.coefficient=parse_int(coef);
    t.a.resize(t.rows);t.x.resize(t.cols);t.matrix.resize(t.rows*t.cols);
    for(int &v:t.a)in>>v;for(int &v:t.x)in>>v;for(int &v:t.matrix)in>>v;
  }
  PeelingRecursion recurrence;
  std::unordered_map<std::string,cpp_int> component_values;
  cpp_int total=0;size_t selected=0,surviving=0,done=0;
  for(const auto&t:terms){
    int edges=std::accumulate(t.matrix.begin(),t.matrix.end(),0);
    if(edges/2!=wanted)continue;
    ++selected;cpp_int value=1;
    for(const Tree &z:split_term(t)){
      std::string key=canonical_key(z);
      auto found=component_values.find(key);
      if(found==component_values.end())
        found=component_values.emplace(std::move(key),recurrence.base(z)).first;
      value*=found->second;if(!value)break;
    }
    if(value){++surviving;total+=t.coefficient*value;}
    if(++done%500==0)std::cerr<<"done "<<done<<" selected terms; unique "
      <<component_values.size()<<" subproblems "<<recurrence.wick_subproblem_memo.size()<<"\n";
  }
  std::cout<<"selected "<<selected<<" surviving "<<surviving
           <<" unique_components "<<component_values.size()<<"\n";
  std::cout<<"total "<<total<<"\n";
}
