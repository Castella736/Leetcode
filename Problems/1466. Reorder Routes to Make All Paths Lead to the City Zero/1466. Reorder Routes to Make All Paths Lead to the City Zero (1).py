from collections import defaultdict, deque;
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0; # Record result.
        seen = {0}; # Record seen node.
        stack = deque([0]); # Stack for DFS.
        
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
        while stack:
            cur = stack.pop();
            seen.add(cur);
            
            for next, re_dir in adj[cur]:
                if next not in seen:
                    stack.append(next);
                    res += re_dir;

        return res;