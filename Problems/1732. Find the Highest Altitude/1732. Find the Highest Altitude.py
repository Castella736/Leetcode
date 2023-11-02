class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Greedy algorithm
        ans = 0;
        height = 0;
        
        # Simulate the road trip.
        # Update highest record.
        for diff in gain:
            height += diff;
            if height > ans:
                ans = height;
        
        return ans
