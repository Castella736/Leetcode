class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # Since x_i is non-decreasing, for 0-indexed x_j
        # sum_{j\neq i} |x_i-x_j| = x_i(2i-n) + sum_j x_j - 2 sum_{j<i} x_j.
        # Use pre_sum to calculate it.
        pre_sum = sum(nums);
        n = len(nums);
        res = [];
        
        for i, num in enumerate(nums):
            res.append(
                (2*i - n) * num + pre_sum
            );
            pre_sum -= 2 * num;
            
        return res;