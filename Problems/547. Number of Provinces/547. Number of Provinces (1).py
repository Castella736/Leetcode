from collections import deque;
from typing import List;

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected);
        visited = [False for i in range(n)];
        res = 0;
        
        # This function can eliminate all city connected to num-th city.
        def bfs(i: int):
            nonlocal visited;
            queue = deque([i]);
            visited[i] = True;
            
            while queue:
                i = queue.popleft();
                
                for j, connection in enumerate(isConnected[i]):
                    if not visited[j] and connection:
                        queue.append(j);
                        visited[j] = True;
            return;
        
        # Start relate each city.
        for i in range(n):
            if visited[i] == False:
                res += 1;
                bfs(i);
        
        return res;