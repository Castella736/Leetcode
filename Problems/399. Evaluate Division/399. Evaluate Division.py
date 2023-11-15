from collections import defaultdict;
from typing import List;
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Convert the data to a adjacency matrix.
        adj = defaultdict(list);
        for i, vars in enumerate(equations):
            mul = values[i];
            u, v = vars;
            # adj[('b', k)] in adj['a'] means 'a' = k*'b'.
            adj[u].append((v,mul));
            adj[v].append((u,1/mul));
            
        # cur = equations[0][0];
        uni_record = {};
        
        # DFS to normalize units in the same component.
        def dfs(cur: str, cur_mul: float, cur_comp: int) -> None:
            nonlocal uni_record;
            uni_record[cur] = (cur_mul, cur_comp);
            
            for next in adj[cur]:
                if next[0] not in uni_record:
                    dfs(next[0], cur_mul/next[1], cur_comp);
            return;
                    
        cur_comp = 0;
        res = [];
        for a, b in queries:
            if a not in uni_record:
                # Check if "a" exists in data
                if a in adj: # Build query of the component.
                    dfs(a, 1, cur_comp);
                    cur_comp += 1;
                else: # Return: query failed.
                    res.append(-1.);
                    continue;
            if b not in uni_record:
                # Check if "b" exists in data
                if b in adj: # Build query of the component.
                    dfs(b, 1, cur_comp);
                    cur_comp += 1;
                else: # Return: query faild.
                    res.append(-1.);
                    continue;
            
            # Check if they are in the same component.
            if uni_record[a][1] == uni_record[b][1]:
                res.append(uni_record[a][0]/uni_record[b][0]);
            else:
                res.append(-1.);
        
        return res;