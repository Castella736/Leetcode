class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Pre-sum two sides.
        # At i-th stage.
        # l_sum = sum to the i-th number (not included) from the left.
        # r_sum = symmetrically.
        # Initialize so that the comparison start from index 0.
        l_sum, r_sum = 0, sum(nums);
        
        # Main comparison.
        for i, num in enumerate(nums):
            r_sum -= num;
            if l_sum == r_sum:
                return i;
            l_sum += num;
        
        
        return -1;