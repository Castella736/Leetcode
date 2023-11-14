from collections import deque;
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        queue = deque(connections);
        seen = {0};
        res = 0;
        
        # We can view all seen nodes as an integrity, view it as the node 0.
        # Use this to determine if the direction is reversed if
        # one of the node had been seen.
        # Postpone the pair if all unseen.
        while queue:
            start, toward = queue.popleft();
            
            if toward in seen:
                seen.add(start);
            elif start in seen:
                res += 1;
                seen.add(toward);
            else:
                queue.append([start, toward]);
        
        return res;