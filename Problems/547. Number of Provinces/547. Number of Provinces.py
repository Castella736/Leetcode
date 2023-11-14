from typing import List;

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected);
        visited = {i:False for i in range(n)};
        res = 0;
        
        # This function can eliminate all city connected to num-th city.
        def investigate(i: int):
            nonlocal visited;
            
            for j, connection in enumerate(isConnected[i]):
                if not visited[j] and connection:
                    visited[j] = True;
                    investigate(j);
            
            return;
        
        # Start relate each city.
        for i in range(n):
            if visited[i] == False:
                res += 1;
                visited[i] = True;
                investigate(i);
        
        return res;