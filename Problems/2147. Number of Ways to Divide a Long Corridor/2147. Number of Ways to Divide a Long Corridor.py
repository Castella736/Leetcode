from collections import deque;
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7;
        stack = deque([]); # Stack to store every two seats.
        
        # Find possible places.
        pos_position = [];
        for i, obj in enumerate(corridor):
            if obj == 'S':
                if len(stack) == 2:
                    pos_position.append(
                        (i - stack[-1]) % mod
                    );
                    stack.clear();
                stack.append(i)
        
        # Exclude not valid case.
        if len(stack) == 1:
            return 0;
        
        # Product up possibilities.
        res = int(bool(stack));
        for gap in pos_position:
            res = (res*gap) % mod;
        
        return res;