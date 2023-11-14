from collections import deque;
from typing import List;
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}; # Set used to record visited rooms.
        queue = deque(
            [key for key in rooms[0]]
        ); # Queue used to record pending visiting.
        
        # Start traversing until no possible route.
        while queue:
            # Select current target room.
            cur = queue.popleft();
            
            visited.add(cur);            
            # Collect keys of un-visited rooms.
            for key in rooms[cur]:
                if key not in visited:
                    queue.append(key);
        
        return len(visited) == len(rooms);