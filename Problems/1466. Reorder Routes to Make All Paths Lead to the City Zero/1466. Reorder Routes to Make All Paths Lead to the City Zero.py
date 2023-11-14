from collections import defaultdict;
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0; # Record result.
        seen = set(); # Record seen node.
        
        # Create adjacent list.
        # By construction, the index position always is the node to be pointed.
        # ele. in adj. is of the form adj[i][(j,d)], we always want
        # j -> i. Otherwise it is a reversed direction.
        # d means if the direction reversed, is 1 is reversed, 0 otherwise.
        adj = defaultdict(list);
        for side in connections:
            adj[side[0]].append((side[1], 1));
            adj[side[1]].append((side[0], 0));
        
        # Perform DFS until no new node found.
        def dfs(cur: int) -> None:
            nonlocal res, seen;
            seen.add(cur);
            # Search next unseen node.
            for next, re_dir in adj[cur]:
                if next not in seen:
                    res += re_dir;
                    dfs(next);
            
            return;
        
        # Start search from the root 0.
        dfs(0);
        
        return res;