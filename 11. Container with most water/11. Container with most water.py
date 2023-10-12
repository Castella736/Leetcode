class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize left and right pointer.
        # Claim the variable "best".
        l = 0;
        r = len(height)-1;
        best = 0;
        
        # Main iteration, stop when left pointer exceed right pointer.
        while l < r:
            # Compare if current area is larger than current best.
            best = max(best,(r - l) * min(height[r],height[l]));
            
            # Move lower side of pointers.
            if height[l] <= height[r]:
                # Confirm move when find height that is higer
                point = l+1;
                while height[point]<height[l] and point <= r-1:
                    point += 1;
                l = point;
            # Mover lower side of pointers.
            else:
                # Confirm move when find height that is higer.
                point = r-1;
                while height[point]<height[r] and point >= l+1:
                    point -= 1;
                r = point;
        
        # Return result.
        return best;